#!/usr/bin/env python3
"""Build and/or check Nagarro Claude Slides slides with the DS compose kit.

The DS folder is a local copy of the design system's `project/` files, keeping the layout
kit/, fonts/ (Equip-Regular, Equip-Medium, EquipExtended-Regular, EquipExtended-Medium), components/bundle.js.

Build from a spec (and check what was built):
  run_kit.py build --ds DS/project --spec spec.json --out OUT
    spec.json = {"cfg": {deck, client, studio, year, logos:{light,dark}, clientLogo?:{light,dark,width}},
                 "slides": [{"layout": "ideaPhoto", "content": {...}}, ...]}
    Writes OUT/slides/<id>.html, OUT/order.json, OUT/report.json and OUT/sheet.png.
    Page numbers are filled in from the slide order when a slide has no "page".

Check existing slide files (a deck's project/slides):
  run_kit.py check --ds DS/project --slides DIR [--order order.json] [--local-images MAP.json] --out OUT
    MAP.json maps "/_blob/<id>" urls to local files so screenshots show the pictures.

Exit code 1 when any slide has an issue or the frame differs between slides.
"""
import argparse, json, pathlib, re, sys
from playwright.sync_api import sync_playwright

CHROME = ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome"]


def launch(p):
    for exe in CHROME:
        if pathlib.Path(exe).exists():
            return p.chromium.launch(executable_path=exe, args=["--allow-file-access-from-files"])
    return p.chromium.launch(args=["--allow-file-access-from-files"])


def sheet(pg, shots, out):
    cells = "".join(f"<div style='display:inline-block;margin:6px;font:14px sans-serif'><img src='file://{s}' style='width:470px;border:1px solid #ccc'><br>{pathlib.Path(s).stem}</div>" for s in shots)
    tmp = out / "_sheet.html"; tmp.write_text(f"<body style='margin:0;background:#ddd;width:1940px'>{cells}</body>")
    pg.set_viewport_size({"width": 1940, "height": 800}); pg.goto("file://" + str(tmp)); pg.wait_for_timeout(400)
    pg.screenshot(path=str(out / "sheet.png"), full_page=True); tmp.unlink()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["build", "check"])
    ap.add_argument("--ds", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--spec"); ap.add_argument("--slides"); ap.add_argument("--order"); ap.add_argument("--local-images")
    a = ap.parse_args()
    ds = pathlib.Path(a.ds).resolve(); out = pathlib.Path(a.out).resolve(); (out / "slides").mkdir(parents=True, exist_ok=True); (out / "shots").mkdir(exist_ok=True)
    runner = ds / "kit/compose-runner.html"
    if not runner.exists():
        sys.exit(f"missing {runner}: copy the DS kit/, fonts/ and components/bundle.js first")
    local = json.load(open(a.local_images)) if a.local_images else {}
    rewrite = lambda h: re.sub(r'src="(/_blob/[0-9a-f]{32})"', lambda m: f'src="file://{local[m.group(1)]}"' if m.group(1) in local else m.group(0), h)

    with sync_playwright() as p:
        b = launch(p); pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto("file://" + str(runner)); pg.evaluate("NagarroRunner.ready"); pg.wait_for_timeout(300)
        slides = []
        if a.mode == "build":
            spec = json.load(open(a.spec))
            for i, s in enumerate(spec["slides"]):
                c = dict(s["content"]); c.setdefault("page", f"{i + 1:02d}")
                try:
                    sl = pg.evaluate("([cfg, l, c]) => NagarroCompose.init(cfg).layouts[l](c)", [spec["cfg"], s["layout"], c])
                except Exception as ex:
                    print(f"BUILD FAILED {c.get('id')}: {str(ex).splitlines()[0]}"); b.close(); sys.exit(1)
                (out / "slides" / f"{sl['id']}.html").write_text(sl["html"]); slides.append((sl["id"], sl["html"]))
        else:
            d = pathlib.Path(a.slides)
            order = json.load(open(a.order)) if a.order else sorted(f.stem for f in d.glob("*.html"))
            slides = [(sid, (d / f"{sid}.html").read_text()) for sid in order]
        report, sigs, shots, bad = {}, {}, [], 0
        for sid, h in slides:
            issues = pg.evaluate("(h) => NagarroRunner.check(h)", h)
            th = "dark" if re.match(r'<section[^>]*background:#010716', h.strip()) else "light"
            sigs.setdefault(th, {}).setdefault(pg.evaluate("(h) => NagarroRunner.signature(h)", h), []).append(sid)
            pg.evaluate("(h) => NagarroRunner.mount(h)", rewrite(h)); pg.wait_for_timeout(200)
            shot = out / "shots" / f"{sid}.png"; pg.locator("#stage section").screenshot(path=str(shot)); shots.append(str(shot))
            report[sid] = issues; bad += bool(issues)
            print(sid, "OK" if not issues else issues)
        # covers use the logo-only header, so compare frames among the non-cover slides of each theme
        for th, groups in sigs.items():
            if len(groups) > 2:
                bad += 1; print(f"FRAME: {len(groups)} different {th} frames:", [v[:3] for v in groups.values()])
        sheet(pg, shots, out); b.close()
    json.dump([s for s, _ in slides], open(out / "order.json", "w")); json.dump(report, open(out / "report.json", "w"), indent=1)
    print(f"{len(slides)} slides, {bad} with issues. Contact sheet: {out / 'sheet.png'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
