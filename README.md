# Nagarro Slides

Build and check Nagarro-branded decks in Claude Slides.

## New here?

Type **/nagarro-slides:start** (or ask "how do I use the Nagarro slides plugin?"). Claude explains what the plugin does, asks what you want to do, and takes you through it.

## Skills

- **start**: a plain-language introduction for new users that asks what they want (new deck, rebrand, check) and hands over to the right skill.
- **build-nagarro-deck**: opens with a short welcome that explains the steps, then builds a new deck from a brief, or a colleague's .pptx/PDF rebranded to the Nagarro Master Slides. Asks a short brief (with a checklist of what makes a deck better: hook, tone, must-have slides, takeaways, your own pictures), shows a plain-language slide-by-slide plan for approval, builds the deck from the master templates and the approved composed layouts, checks every slide, and then works through your screenshots.
- **check-nagarro-deck**: reviews an existing Claude Slides deck against the brand rules and lists what to fix, slide by slide, without changing it.

## What it relies on

The design system **DS Nagarro Master Slides** (https://claude.ai/artifact/FTePiAfzdDWtb71Bogjpn2) is the source of truth: its pages hold the rules (colour, type, layout, imagery, composed layouts) and its `kit/` folder holds the code both skills use (`compose.js`, `checks.js`, `compose-runner.html`). Update a rule in the design system and both skills follow it. People using the plugin need view access to the design system artifact; ask its owner, Carolina Baptista (carolina.baptista@nagarro.com).

The script `skills/build-nagarro-deck/scripts/run_kit.py` builds slides from a spec and runs the checks in headless Chromium (Playwright).
