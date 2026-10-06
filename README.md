# SimpleX Chat homepage: design concept

**Talk to anyone. Be no one.**

An independent homepage design for [SimpleX Chat](https://simplex.chat/). It presents SimpleX as what it is: the first network where nobody has a user identity. It proves that claim on the page instead of describing it.

Status: design concept, October 2026. Not an official SimpleX release. Not affiliated with or endorsed by the SimpleX Chat project.

## View it

Open [`index.html`](index.html) in a browser. There is no build step, no framework and no dependencies. Everything the page needs is in this repo.

To serve it locally:

```
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

Hosted preview: [claude.ai/artifact/CUXGkNVJAmLZWmWaKVqEHF](https://claude.ai/artifact/CUXGkNVJAmLZWmWaKVqEHF). It is private until the owner shares it from the page's Share menu.

## What is in the repo

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | The whole page: markup, styles and a small script for the demo. |
| [`assets/manrope.css`](assets/manrope.css) | Manrope, subset and embedded as text. No font requests to third parties. Licence in [`assets/OFL.txt`](assets/OFL.txt). |
| [`assets/badge-*.svg`](assets/) | App Store, Google Play and F-Droid badges, as used on simplex.chat. |
| [`design-specification.md`](design-specification.md) | The design system: thesis, audience, page structure, type, colour, motion, accessibility and the evidence rules. Read this before changing anything. |
| [`audit-and-validation.md`](audit-and-validation.md) | The running audit log: every check, finding and fix, newest first. |

## The idea in one paragraph

Every messenger people use today is built on knowing who they are: a phone number, a username, a public key. SimpleX has none of these. The page leads with that shift ("Talk to anyone. Be no one."), then shows it working: one conversation in three views, where both phones see the chat and the server sees only encrypted noise with no sender and no recipient. Everything after the hero is evidence. Who identifies you on other networks, what changed, what can be checked, and what independent reviewers say.

## Page structure

1. **Hero.** One line, one action, one quiet proof line (open source, Trail of Bits, F-Droid).
2. **Live demo.** Your phone, the server, their phone. Pausable. Its limit is stated beside it.
3. **The difference.** What identifies you on each kind of network, with SimpleX's full five-point comparison behind a toggle.
4. **The shift.** Then and now.
5. **Proof.** Six checkable facts: Trail of Bits reviews, open source, run your own server, quantum-resistant encryption, private routing, verifiable builds.
6. **Independent voices.** Verbatim quotes from Privacy Guides and Whonix, plus links to Kuketz Blog and The Opt Out podcast.
7. **Get the app.** Store badges and direct downloads.

## Principles

- **Integrity first.** Every claim links to a primary source. No invented numbers, quotes or endorsements. Limits sit beside the claims they qualify.
- **Show, don't tell.** The demo carries the message. No stock imagery.
- **Type carries hierarchy.** Big type, a strict grid, hairlines. Few boxes, no decoration.
- **Private by construction.** No trackers, no cookies, no third-party requests. The page practises what it describes.
- **Accessible.** WCAG 2.2 AA targets: contrast, 44px tap targets, keyboard use, pause control, reduced motion, works without JavaScript.

## History

This design replaced earlier work in this repo: a raster mockup (4 October 2026) and a light coded homepage with a globe hero (6 October 2026). Both remain in the git history and in the audit log. The current design began as a blue-sky exploration and was promoted to main on 6 October 2026.

## Credits and rights

- Fonts: Manrope by The Manrope Project Authors, SIL Open Font License 1.1.
- Store badges: Apple, Google and F-Droid marks, used only to link to the real store listings. They belong to their owners.
- SimpleX and its marks belong to their owners. Quotes belong to their publishers and are linked to their sources.
