# Audit and validation

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
