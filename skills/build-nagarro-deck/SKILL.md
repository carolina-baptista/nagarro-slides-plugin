---
name: build-nagarro-deck
description: "This skill should be used when the user asks to \"make a Nagarro deck\", \"build a presentation in the Nagarro style\", \"rebrand this deck to Nagarro\", \"convert this PPT to the Nagarro master slides\", \"create Nagarro slides for a client\", or otherwise wants a Nagarro-branded slide deck in Claude Slides, from a brief or from an existing .pptx/PDF. It builds the deck with the DS Nagarro Master Slides design system: master templates, the approved composed layouts, the fixed frame, the compose kit and its checks, and a screenshot review loop.\n"
metadata:
  version: "0.3.0"
---

# Build a Nagarro deck in Claude Slides

The source of truth is the design system **DS Nagarro Master Slides**: https://claude.ai/artifact/FTePiAfzdDWtb71Bogjpn2. Its pages hold the rules; its `kit/` holds the code. Output is a Claude Slides artifact (Slides type). Read `references/house-rules.md` for the rules in one place and `references/claude-slides-mechanics.md` for how to publish.

## 0. Welcome: orient the user first

Before any tool call, send a short welcome in plain language (no file names, no technical terms), then go straight to the brief:

> I'll build this as a Nagarro deck in Claude Slides, using the Nagarro Master Slides design system. Here's how it goes:
> 1. **A few quick questions**: the deck name, who it's for (and their logo, if it's a client deck), and whether I may split or trim crowded slides.
> 2. **A slide-by-slide plan** for you to approve before I build anything.
> 3. **The deck**, checked against the brand rules before you see it.
> 4. **Your review**: send screenshots of anything that looks off, with slide numbers, and I'll fix it in one pass. You can also edit slides directly in the editor at any time; I'll keep your changes.

Adapt it to what the user already gave: if they attached a PPT, say you'll rebrand it; drop the steps already answered. Skip the welcome when the user has clearly done this before in the conversation (they're asking for changes, or they mention the plan or the review loop), and give one line instead ("Building it the usual way: questions, plan, deck, your review."). Never repeat the welcome later in the same conversation.

## 1. Brief: ask once, before building

First ask the source and the handling questions in one AskUserQuestion round, skipping what is already known:

- Source: an attached .pptx/PDF, or a brief.
- May slides be split, trimmed or merged, or must every word stay?
- Pictures: explain the DS photo library before offering it, unless the start skill already did. It holds about 200 photos, mostly of real Nagarro colleagues in Nagarro offices; good for slides about Nagarro, teams and culture, never to stand for specific people or roles, and not topic images. Options: the DS library, the user's own pictures (now or later, as placeholders), both, or none.
- Opening style (always ask, for new decks and rebrands alike): the classic openers, or the **Fluidic Intelligence set**, where the cover, agenda, chapter covers and closing sit on dark iridescent 3D artwork. Use that name and describe it in those words. Content slides are the same either way; a deck uses the whole Fluidic Intelligence set or none of it. For a rebrand, say which style the source deck's openers are closest to, and make that the first option, unless the user has already chosen a style.
- Rebuilding from a PPT: does any slide need a colour outside the DS (a client brand colour, chart series)? Default is DS colours only; agree exceptions slide by slide.

Then, for a deck from a brief, ask for the content as a short numbered checklist in plain text (users answer it point by point; it works far better than a multiple-choice question for free text). Mark the first six as the essentials:

1. **Deck name** (header and footer).
2. **Topic and key messages**: what the deck must say; bullets or pasted notes are fine.
3. **Audience and purpose**: who is in the room (role, age, background, what they care about) and what the deck is for (pitch, talk, status update, workshop).
4. **Rough slide count**, or "you decide".
5. **Client or host name** and their logo (looked up in the DS client-logo set first, else the official logo, else the file; never redrawn). "[Client]" when generic.
6. **Anything verbatim**: quotes, figures, legal text.

Then the optional extras that make the deck much better (one line each):

7. **Opening**: should it start with a hook (a story, a striking fact, a question)?
8. **Tone and angle**: e.g. balanced rather than alarmist, inspiring, technical, sales-led; what to avoid.
9. **Must-have slides**: a real quote, a company introduction, a speaker or team slide (send the CV and photo), a case study, a closing call to action.
10. **Takeaways**: what the audience should remember or do afterwards (tips, next steps).
11. **Their own pictures**: photos, screenshots, diagrams or logos they want in, now or later.
12. **Sources** they want used or cited.

Never invent a statistic or a quote: research and verify them, and say in the plan where each one comes from.

## 2. Read the DS first

If the design system can't be read (no access), stop and tell the user to ask its owner for access: Carolina Baptista (carolina.baptista@nagarro.com).

Read with the Artifact tool: `project/README.md`, `02-colour.md`, `03-typography.md`, `04-layout.md`, `06-imagery.md`, `08-slide-library.md`, `09-building-decks.md`, `16-composed-layouts.md`, `components/Header/README.md`, `assets/HeaderLogos/README.md`, and for a Fluidic Intelligence deck `api/assets/Artwork.md`, `api/assets/Glow.md` and `api/assets/Light-artwork.md`. Read the catalog sections (`12`–`15`) only for masters under consideration. Then download the kit into the session: `project/kit/compose.js`, `project/kit/checks.js`, `project/kit/compose-runner.html`, `project/components/bundle.js` and the four fonts `project/fonts/Equip-Regular.woff2`, `Equip-Medium.woff2`, `EquipExtended-Regular.woff2`, `EquipExtended-Medium.woff2`, keeping the `project/` layout.

## 3. Slide plan, approved before building

Show the plan as a plain-language table the user can picture: **#**, **slide (the claim it makes)**, **light/dark**, **what goes on it**. Describe the content concretely and, where it helps, the visual in everyday words ("a donut chart of the 45%", "three columns: Trick, Run, Catch", "your photo beside the CV highlights"). Never list template or layout names: they are too abstract for the reader. Mark every picture: **library photo** (say which kind), **your photo**, or **picture placeholder** (what it should show). Wait for approval.

Behind the plan (not shown to the user):

- Masters are the first library; composed layouts (`16-composed-layouts.md`) are the second. Compose a new layout from DS components only when neither fits.
- **Variety**: draw on the whole master library (statements, indexes, data and chart slides, diagrams, do/don't, roadmaps, profiles, closings), not a handful of composed layouts. No two neighbours on the same layout; alternate text-led, visual-led and data-led slides.
- **A statement slide must not look like a cover**: covers and chapter covers are dark with a large title; a statement inside the deck uses a statement master (a light panel with supporting figures, a centred problem statement) so it reads as content.
- Never pad a layout with invented items or cram extra ones in.
- Keep the text unless trimming was allowed; flag anything that must change.
- Number chapter covers 01, 02 … in deck order; never show a number without the covers before it. Fluidic Intelligence chapter covers carry no number.
- **Fluidic Intelligence set** (when chosen): cover (`artCover`, on any dark artwork plate, not always the cover plate) → agenda (`artIndex`) → a chapter cover (`artChapter`) at each chapter → closing (`artClosing`). Chapter titles and subtitles are the deck's own words, never the example titles from Figma.
  - Agenda: one row per chapter on a single slide. With a detail line per chapter it holds about 8 rows; with titles only, chapters that don't fit in one column go two to a row (about 16). Never split the agenda over two slides: when chapters with details don't fit, drop the details (with the user's OK) so they go two to a row.
  - Chapter artworks: **artwork 1 is the Nagarro symbol: only on chapters about Nagarro** (who we are, our studio, our capabilities). Artworks 2–6 go on any chapter and may repeat, up to every chapter on the same one. In the plan describe each in everyday words ("the Nagarro-symbol glass shape", "the light ribbon") and let the user choose.
  - Never mix Fluidic Intelligence openers with the classic cover, chapter or closing layouts in one deck.
- Where a picture would strengthen a slide and the user has none yet, plan a picture placeholder rather than an unsuitable library photo.

## 4. Build

1. Create the deck from the Slides type. In the first publish install the DS (`designSystems` record, `project/ds/nagarro/tokens.json` and the two fonts as `{artifact, path}` copies, `faces` `equip` and `equip-extended`).
2. For a Fluidic Intelligence deck, plan where glow fills, light artwork fills and artwork layers lift content slides (`references/house-rules.md` › Fluidic Intelligence imagery) and list them in the plan. Body copy is `TextXXL`, and row, column and list blocks anchor to the bottom of the content area (house rules).
3. Upload images and copy the header logos (DS asset group Header logos: Horizontal, Mint, and its on-dark version) into the deck; use the returned `/_blob/` urls. For a Fluidic Intelligence deck also copy the artwork plates it uses from the DS asset group Artwork (`art-cover.jpg`, `art-index.jpg`, `art-closing.jpg`, the chosen `art-chapter-N.jpg`) the same way.
4. Composed slides: write a spec and run `scripts/run_kit.py build --ds <DS project dir> --spec spec.json --out <dir>`. The spec is `{cfg, slides:[{layout, content}]}`; `cfg` has `deck`, `client`, `studio`, `year`, `logos {light, dark}` and, for a client deck, `clientLogo {light, dark, width}` (width = 30 × the logo's aspect ratio); for a Fluidic Intelligence deck, `art {cover, index, closing, chapter: [six urls]}` (a slide then picks its chapter artwork with `art: 1`–`6`; unused chapter slots can repeat a copied url). A layout that refuses its content names the slide: split it, trim with permission or choose another layout. Never shrink type.
5. Masters: render with the DS engine (`NagarroSlides.render(name, fields, {theme, meta, footer, useExample:false})`) in the same runner page, flatten to pinned elements (see `references/claude-slides-mechanics.md`), and replace the master's header and footer with the kit's `frame()`.
6. **Centre graphics in their panel**: a chart, diagram or big number that sits on a panel or background is centred on it horizontally and vertically (a donut stays a true circle, inset evenly, with its number centred inside). Re-centre after flattening a master, since fitting it into the frame moves things.
7. **Picture placeholders**: an `fg-5` box with `radius-15`, at the size and place the picture will take (filling its column to y=963 when beside text), with a centred `TextXL` `fg-50` label "Picture: <what it should show>". Note it in the speaker notes. When the user sends the file, upload it and swap the placeholder for the image at the same position and size (`object-fit: cover`, `radius-15`).
8. A one-off layout outside the library: build it from the kit primitives (`ts`, `box`, `rule`, `img`, `icon`, `pageHead`, `section`) so it uses the same tokens, styles and frame.

## 5. Check before every publish

Run `scripts/run_kit.py check --ds <DS project dir> --slides <deck>/project/slides --order order.json --out <dir>` (add `--local-images` to see pictures). It fails on: malformed markup, colours that aren't DS tokens, text that isn't a named DS style, coloured words inside a text element, anything outside y=156–963 or x=40–1880, overlapping text, images without rounded corners or with no `object-fit` (the artwork plate, full-bleed and square, is the one allowed exception), mint bullets on grey cards, and frames that differ between slides. Fix every issue, then look at the contact sheet (`sheet.png`) and judge what the checks can't: mint balance, rhythm, empty space, image crops.

## 6. Review loop

- Publish, then ask the user for screenshots of anything wrong, with slide numbers. Fix everything in one pass.
- The user also edits in the Slides editor. Before every republish, read the live slides and compare them with the last published copy; carry the user's changes into the build instead of overwriting them. If a publish is refused because a slide changed, read the current version and apply the change on top of it.
- The editor's fixed "margin 128" snapping guide doesn't match the DS; keep to 156–963 and 40px.
- When the user states a new rule, apply it to the deck, then propose adding it to the DS page it belongs to (and to `kit/` if it can be checked), so the next deck starts from it.
