# Claude Slides mechanics for Nagarro decks

## Slide files

- `project/deck.json` (v4: `order`, `sections`, `cover`, `faces`, `designSystems`, `lists: "css"`) and one `project/slides/<id>.html` per slide, each a single `<section>` with inline styles only.
- **Pin every element** (`position:absolute` with left, top and width). The viewer ignores section padding and the editor strips it; never rely on flex layout on the section.
- **Well-formed markup only.** An unclosed tag makes the viewer drop the whole slide. `kit/checks.js` parses every file.
- Speaker notes go in `<aside>` inside the section.

## Installing the DS in a new deck (first publish)

- `designSystems: [{title: "DS Nagarro Master Slides", namespace: "nagarro", artifact: "https://claude.ai/artifact/FTePiAfzdDWtb71Bogjpn2", version, copiedAt}]`.
- Files `project/ds/nagarro/tokens.json`, `project/ds/nagarro/fonts/Equip-Regular.woff2`, `project/ds/nagarro/fonts/EquipExtended-Medium.woff2` as `{artifact, path}` copies from the DS (DS paths `project/tokens.json`, `project/fonts/…`).
- `faces: {equip: {family: "Equip", src: "project/ds/nagarro/fonts/Equip-Regular.woff2"}, "equip-extended": {family: "Equip Extended", src: "project/ds/nagarro/fonts/EquipExtended-Medium.woff2"}}`.

## Images and logos

- Copy DS assets (header logos and the like) with `publish asset:true, from_url, asset_ids` (up to 10 per call); upload local images with `file_paths` (up to 25 per call). Use the returned `/_blob/<id>` urls verbatim.
- Header logos: DS asset group Header logos, Horizontal Mint and Horizontal Mint on-dark.
- A client logo: make a single-ink version (alpha = 255 − min(r, g, b) over the logo's ground), one dark-ink and one white, about 120px tall; width in the header = 30 × aspect ratio.

## Rendering masters in Claude Slides

- In the runner page, `NagarroSlides.render(name, fields, {theme, meta, footer, useExample:false})`, then flatten: for every element take computed position, size, font, colour, background and per-side borders; inline each SVG child's computed fill and stroke (otherwise icons and the wordmark disappear); keep image sources.
- Drop the master's own header and footer (elements above y=100, the 84px divider box, anything from y=980), add the kit's `frame()`, and move content into 156–963 if it sits outside. Strip any coloured highlight spans the master puts in titles. Then run the checks like any other slide.

## Publishing

- `publish` with `file_path` = `project/deck.json`, `root` = the deck folder, `files` = the slide files (no path twice).
- If a publish is refused because the user edited a slide, read the live version and apply the change on top of it; never resend an older copy.
- Before republishing, read the live slides and diff them with the last published copy, so the user's edits carry forward.
