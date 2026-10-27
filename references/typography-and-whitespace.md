# Typography & Whitespace Guide for Social Graphics

## 1. Golden Ratios for 1080px Width Canvas

| Element Level | Font Size | Weight | Tracking / Letter-Spacing | Line Height |
| :--- | :--- | :--- | :--- | :--- |
| **Hero Headline (H1)** | 72px – 104px | 800 – 900 | `-2px` s/d `-3px` (Tight) + `word-spacing: 8–12px` | 0.95 – 1.02 |
| **Sub-hook / Editorial Serif** | 30px – 42px | 400 – 600 | `-0.2px` s/d `-0.5px` | 1.22 – 1.32 |
| **Secondary Description** | 22px – 26px | 400 – 450 | `-0.1px` s/d `0px` | 1.4 – 1.5 |
| **Kicker (pure tracked text, no pill)** | 18px – 22px | 600 – 700 | `0.16em` s/d `0.22em` (Wide) | 1.0 |
| **Metadata Row (Dates/Info)**| 18px – 21px | 500 / 800 (labels) | `-0.2px` | 1.2 |
| **Counter / Swipe Cue (`01 / 05`, `Geser →`)** | 18px – 22px | 600 | `0.16em` s/d `0.22em` | 1.0 |

> Absolute floor: **no text below 18px** on a 1080px canvas. No pills, no CTA buttons (see SKILL.md §1).

## 2. Whitespace Architecture (The Breathing Rhythm)

* **Top Margin:** 100px – 120px (protects against Instagram UI overlays and ensures clean entry).
* **Side Padding:** 72px – 88px (avoids edge crowding and leaves generous lateral framing).
* **Bottom Margin:** 60px – 90px (room for the quiet counter / swipe cue).
* **Inner Cluster Gaps (Tight Proximity):**
  - Kicker ➔ Headline: 10px – 16px.
  - Headline ➔ Primary Subhead: 10px – 16px.
* **Sectional Gaps (Generous Whitespace):**
  - Primary Subhead ➔ Secondary Description: 36px – 48px.
  - Secondary Description ➔ Metadata Row: 24px – 32px.
  - Headline block ➔ Hero asset ➔ Card: 70px – 85px each, equal within ±10px (SKILL.md §2.6).

## 3. Common Anti-Patterns to Avoid
❌ Distributing elements with `justify-content: space-evenly` (creates a floaty, disconnected look).  
❌ Using font sizes that are too close to each other (e.g., 50px headline and 40px subhead — lack of contrast).  
❌ Pure white text on vibrant pure blue without text shadow (causes eye strain; use subtle drop shadow or soft ambient glow).  
❌ Any text under 18px, pill badges, or CTA buttons on a static feed graphic.  
❌ Cramming text to the canvas edges.
