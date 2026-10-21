# House rules (summary)

The DS pages are canonical; this is the same set in one place. `kit/compose.js` encodes the values and `kit/checks.js` enforces most of them.

## Frame and content area (DS: Canvas and layout)

- Canvas 1920×1080, margins 40px. Content runs from y=156 (32px below the header line) to y=963 (32px above the footer line). Full-height images and panels run exactly 156→963.
- Header: logo (Horizontal, Mint; on-dark version on dark slides) at 40,40, 203×64; divider box 40,40, 1840×84 with a 1px `fg-50` bottom border; meta at y=60 in `TextMD` `fg-50`, separated by 1px rules, page number right-aligned to x=1880. Covers: logo and divider only.
- Client logo: 24px after the logo a 1px rule 30px tall (y=57–87), then 24px, then the client logo in a 30px-tall box, single ink (`fg-100` light, white dark).
- Footer: three 597.3px columns from x=40, 24px apart, 1px `fg-50` top rule at y=995, text at y=1015: deck name, "Prepared for <Client>", "© <year>" right-aligned.
- The full-width header and footer are identical on every slide (page number aside). Non-full-width header variants are allowed where a master uses one, same height.
- PageHeader: caption `TextXL` `fg-50` at 156, title `Heading2` 6px below; intro `Heading5` `fg-50` 6px under the title; content 48px below.

## Themes

Cover, chapter covers and closing are dark. Content slides can be light or dark (most masters have both); mix them for rhythm.

## Colour (DS: Colour › Rules)

- Only DS Theme tokens, at the values the HTML renders. Photos and client logos keep their colours. Exception only for decks rebuilt from a PPT, agreed with the user slide by slide.
- Tokens for their roles: dividers `fg-10`/`fg-20`, tinted cards `fg-5`, captions `fg-50`, reading text `fg-100`/`fg-75`/`fg-60`.
- One colour per text element: never highlight a word of a title or sentence, unless the user asks.
- Mint is balanced, not rationed: one consistent kind of mark (all bullets on white, card bars, index numbers on dark, acronym letters), one panel, or a short all-mint label on dark. One or two kinds per slide, never dominant.
- Mint on grey depends on size: bars and panels are fine on `fg-5`; bullets and small dots are not (use `fg-100`). Mint as text only on dark slides.

## Type (DS: Typography › Rules)

- Only the named styles, exact: TextXS–XL (Equip 400), Heading6–1 and Title (Equip Extended 500, tracking -2% exact).
- Roles: title `Heading2`; caption `TextXL` `fg-50`; intro `Heading5` `fg-50`; card titles `Heading5`/`Heading6`; card and list copy `TextLG`; lead body `TextXL`; index numerals `Heading6`/`Heading3`; cover and statement `Heading1` + `Heading3` `fg-50`.
- Never shrink type to fit: move, split or trim with permission.

## Pictures (DS: Imagery)

- Always rounded corners (`radius-15`; screenshots in a panel `radius-9`). Never a photo as a full background behind text.
- The DS photo library is mostly real Nagarro colleagues in Nagarro offices: use it for Nagarro, team and culture slides. For other subjects use the user's pictures or a labelled picture placeholder (`fg-5`, `radius-15`, "Picture: <what>" in `TextXL` `fg-50`) that is swapped for the user's file later.
- An image beside text fills its column to y=963 when there's room. Photos: `cover` with an `object-position` that keeps the subject; white-ground illustrations: `fg-5` panel, 32px inset, `contain`, `mix-blend-mode: multiply`. Never stretch.
- Don't use DS employee photos to stand for roles such as CTOs or founders; use icons or no photo.

## Deck structure

- Masters first, composed layouts second, a new composition last (flagged in the mapping table).
- Chapter covers numbered in order; no number without the covers before it.
- No two neighbours on the same layout. Alternate text-led, visual-led and data-led slides, drawing on the whole master library.
- A statement slide inside the deck never looks like a cover or chapter cover: use a statement master.
- Charts, diagrams and big numbers on a panel are centred on it, horizontally and vertically.
