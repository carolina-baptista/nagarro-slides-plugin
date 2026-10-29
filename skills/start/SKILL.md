---
name: start
description: "This skill should be used when the user types \"/nagarro-slides:start\", asks \"how do I use the Nagarro slides plugin\", \"what can the Nagarro plugin do\", \"help me get started with Nagarro slides\", \"how do I make a Nagarro deck here\", or seems unsure where to begin with Nagarro presentations. It explains the plugin in plain language and hands over to the right skill.\n"
metadata:
  version: "0.2.0"
---

# Getting started with Nagarro Slides

Guide a new user to the right task. Assume this is their first time: no file paths, code, tool names, template names or design-system jargon.

1. **Welcome in a few lines.** Say what the plugin does: it makes Nagarro-branded decks in Claude Slides that follow the Nagarro Master Slides design system (the official layouts, fonts, colours and header and footer), and it can check a deck against those rules. Mention that every deck is built from a short brief and an approved plan, and improved from their screenshots.

   End the welcome with this access note, word for word:

   > **Before you start:** you need access to the Nagarro Master Slides design system. It's an artifact in Claude, not a Figma file or a SharePoint folder. If you can't open it, ask its owner for access: Carolina Baptista (carolina.baptista@nagarro.com).

2. **Ask what they want**, with AskUserQuestion (one question, these options):
   - **Build a new deck from a brief**: "Tell me the topic, audience and roughly how many slides."
   - **Rebrand an existing deck**: "Attach the PowerPoint or PDF and I'll move it onto the Nagarro master slides."
   - **Check a deck**: "Share a Claude Slides deck and I'll list what doesn't follow the brand rules, slide by slide."
   - **Just explain how it works**.

3. **Set expectations in two or three short points**, matched to the choice:
   - What happens: a few questions, then a slide-by-slide plan to approve, then the deck, checked against the brand rules.
   - How to give feedback: screenshots with slide numbers; edits made directly in the editor are kept.
   - Good to know: covers, chapter dividers and the closing are dark; titles stay one colour; pictures have rounded corners; content can be split across slides rather than shrunk. A new or rebranded deck can also use the Fluidic Intelligence style: cover, agenda, chapter covers and closing on dark iridescent 3D artwork.

4. **Explain the pictures before asking about them.** A first-time user doesn't know what "the photo library" is. Say it plainly: the design system includes about 200 photos, mostly of real Nagarro colleagues in Nagarro offices (people working together, workshops, laptops, office life). They suit slides about Nagarro, teamwork and culture; they can't stand in for specific people or roles (a client's CTO, a founder), and they're not topic images (no pictures of code, data centres or products). For anything else, the user can send their own pictures, now or later: the plan marks where a picture would help, and the deck gets a clearly labelled picture placeholder there that Claude fills when the user sends the file.

5. **Hand over.** For a new deck or a rebrand, continue with the build-nagarro-deck skill (it skips its own welcome, since this one covered it). For a check, continue with the check-nagarro-deck skill. For "just explain", answer their questions, then offer the first three options again.

If the user later can't open the Nagarro Master Slides design system, remind them that both other skills need it, that it's an artifact in Claude (not in Figma or SharePoint), and that they should ask its owner for access: **Carolina Baptista (carolina.baptista@nagarro.com)**.
