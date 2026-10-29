---
name: check-nagarro-deck
description: "This skill should be used when the user asks to \"check this Nagarro deck\", \"review my slides against the master slides\", \"is this deck on brand\", \"audit the Nagarro deck\", or shares a Claude Slides link and wants to know what breaks the Nagarro design system rules. It runs the DS kit checks on every slide and reports the issues by slide.\n"
metadata:
  version: "0.2.0"
---

# Check a Nagarro deck

Audit a Claude Slides deck against the DS Nagarro Master Slides rules without changing it.

Start with one plain-language line for the user: "I'll check every slide against the Nagarro brand rules and list what to fix, slide by slide. I won't change anything unless you ask." Skip it if the start skill already explained this.

1. Read the deck with the Artifact tool: `project/deck.json` and every `project/slides/<id>.html` in `order`. Read the uploaded images it uses (`/_blob/` ids) only if the user wants pictures in the contact sheet.
2. Download the DS kit (no access to the design system: tell the user to ask its owner, Carolina Baptista, carolina.baptista@nagarro.com) from https://claude.ai/artifact/FTePiAfzdDWtb71Bogjpn2, keeping the `project/` layout: `kit/compose.js`, `kit/checks.js`, `kit/compose-runner.html`, `components/bundle.js`, and the fonts `Equip-Regular`, `Equip-Medium`, `EquipExtended-Regular`, `EquipExtended-Medium` under `fonts/`.
3. Run the check script from the build-nagarro-deck skill: `scripts/run_kit.py check --ds <DS project dir> --slides <slides dir> --order <order.json> --out <dir>`.
4. Look at the contact sheet and add what the checks can't see: mint balance, rhythm (the same layout twice in a row, no light/dark mix), chapter numbering (Fluidic Intelligence chapter covers are unnumbered), Fluidic Intelligence openers mixed with classic ones, artwork on a content slide, chapter artwork 1 (the Nagarro symbol) on a chapter not about Nagarro, an agenda split over two slides, empty space, image crops, employee photos used for roles, placeholder text left in.
5. Report by slide number, in plain language, most serious first: what is wrong, which rule it breaks (name the DS page), and the fix. Group repeats ("slides 9, 12, 17: …"). End with the slides that pass.

Change nothing in the deck unless the user asks; then follow the build-nagarro-deck skill's review loop.
