# pddskill - Pro Graphic Designer Skill

Expert graphic design skill for creating human-designer-grade visual assets (Instagram carousels, feed posts 1:1 and 4:5, posters, flyers, banners, social media marketing graphics) using HTML/CSS/SVG and Playwright headless rendering.

Enforces Gestalt proximity, optical centering, tight typographic lockups, balanced whitespace, and dual-output (production-ready PNG + Figma-editable SVG). Avoids floaty AI-slop layout.

## Core Features & Design Principles
- **The Anti-AI-Slop Blacklist**: Strict prohibitions against website-wireframe cards (`.div-card`), mechanical template re-skinning, and fake telemetry pills.
- **Genre-Specific Emotional Psychology**: Dedicated rules for:
  - *Culinary & Food*: Warm indulgence, full-bleed organic macro photography, fleshy rounded/diner typography (*Fraunces, Bricolage Grotesque*), zero sterile cutouts.
  - *Sport & High-Energy*: Kinetic tension, angular skews, industrial condensed sans (*Bebas Neue, Anton, Syne 800*).
  - *Travel & Luxury*: Serenity, breathing negative space, high-fashion serif italic (*Cormorant Garamond, Instrument Serif*).
- **Anti-Monotony Compositional Archetypes**: Escapes the repetitive "Header-Headline-Photo-Footer Sandwich" with 5 radical layout architectures (Bottom-heavy cinema anchor, asymmetric side columns, magazine masthead wraps, etc.).
- **Dual-Output Deliverables**: Generates production-ready 1080x1350/1080x1080 PNG + standalone Figma-compatible SVG vector file.

## Repository Contents
- `SKILL.md`: Main instruction file containing comprehensive rules, failure post-mortems, and agency archetypes.
- `scripts/render_graphic.py`: Low-RAM Playwright renderer (waits for fonts + images) with an automatic layout audit (text < 18px, safe-margin violations, banned bullet glyphs).
- `scripts/prepare_asset.py`: Memory-safe cover crop and `place-seamless` compositor (alpha-aware for transparent PNG cutouts, fits assets inside the zone without cropping, prints `ASSET_BOX` for equal-gap spacing, optional ambient glow).
- `references/`: Agency design archetypes and design reference guides.
- `assets/`: 3D assets and photography resources.
