# Audit and validation

## Coded homepage v1 audit — 6 October 2026

Current artifact: [index.html](index.html) + [styles.css](styles.css), rendered at 390px, 768px and 1280px ([renders/](renders/)). This is the first working page in the repo; the raster mockups are now the archived design baseline.

**What changed.** The hero now leads with sovereignty ("Your messages. Your network. No one in the middle.") on a solid navy surface beside the globe image; the page below keeps the ink/cobalt/ice palette. The network section states the three claims in text (no user identity, no central server, data stays with you) beside the supplied illustration. Roadmap and support share one section. The final row is heading, Download SimpleX and All platforms only.

### Status of the 4 October findings

| ID | Status | Evidence |
| --- | --- | --- |
| D01 | Closed | Headings #10234A, body #334155, actions #245CFF, links #2057D4 underlined, cyan only on eyebrow, focus ring and pillar rules. Diagram caption and qualifications use muted #475569. |
| D02 | Closed | Every band uses the same clamp(72px, 9vw, 120px) padding; roadmap and support are one two-column section. |
| D03 | Closed | Hero 600 weight, section headings 500, body 400 (Inter). |
| D04 | Superseded | The generated diagram was replaced by the supplied illustration, which carries its own labels. See D07. |
| D05 | Open | Globe and network images are generated artwork supplied by Kai, not approved SimpleX assets. Rights still need confirming before any production use. |
| D06 | Closed | Final row contains heading, one button and All platforms link. |

### New findings

| ID | Priority | Observed issue | Required refinement |
| --- | --- | --- | --- |
| D07 | Medium | The network illustration has text baked into the image (heading, side panel, labels). It is unreadable at 390px and is not available to assistive technology. The HTML carries the same claims in text and the alt text describes the labels. | Obtain or crop a text-free version of the illustration and move all labels into HTML callouts. |
| D08 | Low | Destinations for directory, roadmap, security, investing and donate links point at plausible simplex.chat and GitHub URLs that were not fetched during this round. | Verify every external link before publishing. |
| D09 | Low | Inter is loaded from Google Fonts. It adds one third-party request. | Self-host the three weights or confirm the system-font fallback is acceptable. |
| D10 | High | The binary assets (assets/ and renders/) could not be pushed through the GitHub API in this session. The branch holds the HTML, CSS and docs only; the page renders without its two images until the assets folder is added. | Add the assets/ and renders/ folders from the delivered zip to this branch. |

### Checks completed this round

- Rendered at 390px, 768px and 1280px with headless Chromium; no horizontal overflow at any width.
- Contrast measured from the CSS values: hero text 17.7:1, hero lede 11.8:1, link on navy 9.4:1, button text 5.2:1, link on ice 5.8:1, body on ice 9.6:1, muted on ice 7.0:1, step numbers 4.8:1. All pass WCAG 2.2 AA.
- Mobile Menu: aria-expanded toggles, first link receives focus on open, Escape closes and returns focus to the button.
- No interactive element below 24 x 24 CSS px; nav links and buttons are 44px or taller.
- Text never sits on an image or translucent layer. The gradient on the hero only covers the image, not the copy.
- Page weight: desktop hero 233KB WebP, mobile hero 83KB WebP, illustration 103KB WebP, CSS 6KB, no JS libraries.

### Still untested

Real-device load time, screen-reader pass, zoom to 200%, link destinations (D08), newcomer comprehension of the sovereignty headline. No conversion improvement is claimed.

## Current desktop audit — 4 October 2026

Current artifact: [homepage-desktop.png](homepage-desktop.png). Scope: desktop website only. The earlier desktop/mobile concept is an archived iteration.

**Assessment:** the cooler blues and desktop composition improve freshness and clarity. Colour roles still overlap, and the lower page loses the spacing established above. The six findings below are open recommendations; they have not yet been applied to the current raster mockup.

| ID | Priority | Observed issue | Required refinement | Acceptance check |
| --- | --- | --- | --- | --- |
| D01 | High | Body copy, links, diagram labels and qualifications all appear blue, weakening the distinction between reading and acting. | Use ink headings, dark slate body copy, cobalt actions, consistent blue links and sparse cyan accents. | Inspect each text role; distinguish links by more than colour where needed. Measure implemented contrast. |
| D02 | High | Directory, roadmap, support and final download form consecutive shallow bands. | Restore consistent section spacing; group roadmap and support in one spacious project section with clear internal separation. | Compare spacing throughout the page at actual desktop widths; lower sections should not feel squeezed. |
| D03 | Medium | Section titles have nearly uniform bold emphasis. | Keep the hero semibold and strongest; use medium-weight section headings and regular body text. | Check that headline, section title and supporting copy are distinguishable without relying on colour. |
| D04 | Medium | Device callouts terminate near people or empty space. | Anchor each leader directly to its phone or server rack; style labels more quietly than links. | Trace every callout visually and confirm that it identifies the intended object without ambiguity. |
| D05 | Medium | Recreated globe has a faceted, more stylised land surface than the original. | Use approved original high-resolution imagery; apply the new palette to surrounding UI surfaces and controls. | Compare with approved SimpleX source artwork and inspect crop/resolution at target size. |
| D06 | Medium | Final download row combines heading, button, secondary link and repeated platform list. | Remove the repeated platform list from that row and increase separation between heading and action. | Final row presents one clear primary action; platform access remains available via All platforms. |

### Strengths to preserve

The hero identifies private messaging, downloads stand out, onboarding is grouped and explicitly includes QR invitations, reports identify their scope, qualifications remain visible, and funding has secondary emphasis.

### Validation boundary

This is a visual review of a generated static image. Exact font metrics, contrast, keyboard behaviour, working destinations and download recovery remain unverified. No conversion improvement or accessibility conformance is claimed.

## Earlier findings addressed in the visual concept

| Finding | Resolution | Evidence boundary |
| --- | --- | --- |
| Network art lacked explanation | Device, relay and contact labels; simplified-illustration caption | Visually inspected; not a formal protocol diagram |
| Report evidence lacked scope | 2022 library assessment and 2024 protocol-design review identified separately | Scope checked against SimpleX announcements |
| Mobile became dense | Recomposition, vertical report rows and stacked footer groups | Exact sizes and spacing require implementation validation |
| Onboarding was disconnected | Heading and steps grouped beside app preview | App UI is illustrative |
| Community photos lacked meaning | Proposed directory categories replace generic avatar collage | Proposed taxonomy, not verified current directory structure |
| Roadmap competed late in journey | Short summary and link replace dated timeline | Supporting detail remains a destination responsibility |
| Hero used specialist jargon | Invitation-based connection described in plain language | Comprehension still needs participant testing |

## Earlier typography follow-up

The latest critique found uniform heading emphasis, small mobile secondary text and inconsistent link treatment. The design specification defines a more disciplined scale, darker body copy, aligned report rows and readable secondary labels. These specifications are not guaranteed by the generated pixels; implement and inspect them before sign-off.

## Checks completed

- Reviewed the full desktop/mobile raster composition, content sequence, imagery use, claims, provenance labels and action hierarchy.
- Verified the scope of the two historical security references.
- Earlier live-site inspection exercised desktop download navigation and mobile Menu → Guide → Quick start, and inspected 390px, 768px and 1280px layouts. Those observations informed the brief; they do not verify this redesign's behavior.

## Checks still required

1. Replace recreated brand imagery and app preview with approved production assets; verify asset rights and current product details.
2. Confirm current security reports, threat-model content, directory structure and supported downloads.
3. Build and test keyboard navigation, menu state, focus, screen-reader names, contrast, zoom, reflow and reduced-motion behavior.
4. Exercise platform selection, download failures/mirror recovery and relevant destination links.
5. Measure performance under stated network/device conditions; distinguish lab results from field data.
6. Observe newcomers explaining the product difference, choosing a download and describing the invitation workflow. Measure comprehension, task success and effort separately from aesthetic preference.

No participant usability testing, accessibility certification, cryptographic assessment or performance measurement is claimed. The project contains a design concept, not a deployed or interactive website.
