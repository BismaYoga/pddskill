# Typography & Whitespace Guide for Social Graphics

## 1. Golden Ratios for 1080px Width Canvas

| Element Level | Font Size | Weight | Tracking / Letter-Spacing | Line Height |
| :--- | :--- | :--- | :--- | :--- |
| **Hero Headline (H1)** | 72px – 96px | 800 – 900 | `-2px` s/d `-3.5px` (Tight) | 1.05 – 1.1 |
| **Primary Subhead** | 26px – 32px | 500 – 600 | `-0.2px` s/d `-0.5px` | 1.25 – 1.35 |
| **Secondary Description** | 22px – 26px | 400 – 450 | `-0.1px` s/d `0px` | 1.4 – 1.5 |
| **Category Badge / Pill** | 16px – 20px | 600 – 700 | `+0.5px` s/d `+1.5px` (Wide) | 1.0 |
| **Metadata Row (Dates/Info)**| 18px – 21px | 500 / 800 (labels) | `-0.2px` | 1.2 |
| **CTA Button / Pill** | 20px – 22px | 600 – 700 | `+0.2px` | 1.0 |

## 2. Whitespace Architecture (The Breathing Rhythm)

* **Top Margin:** 60px – 80px (protects against Instagram UI overlays and ensures clean entry).
* **Side Padding:** 65px – 80px (avoids edge crowding and leaves generous lateral framing).
* **Bottom Margin:** 70px – 90px (gives the CTA button room to breathe).
* **Inner Cluster Gaps (Tight Proximity):**
  - Category Badge ➔ Headline: 16px – 22px.
  - Headline ➔ Primary Subhead: 10px – 16px.
* **Sectional Gaps (Generous Whitespace):**
  - Primary Subhead ➔ Secondary Description: 36px – 48px.
  - Secondary Description ➔ Metadata Row: 24px – 32px.
  - Metadata Row ➔ Bottom CTA: 100px – 140px.

## 3. Common Anti-Patterns to Avoid
❌ Distributing elements with `justify-content: space-evenly` (creates a floaty, disconnected look).  
❌ Using font sizes that are too close to each other (e.g., 50px headline and 40px subhead — lack of contrast).  
❌ Pure white text on vibrant pure blue without text shadow (causes eye strain; use subtle drop shadow or soft ambient glow).  
❌ Cramming text to the canvas edges.
