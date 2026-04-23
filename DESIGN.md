# Design System Strategy: The Digital Arboretum

## 1. Overview & Creative North Star
**Creative North Star: "The Modern Conservatory"**
This design system moves away from the clinical, "app-like" feel of standard garden trackers and instead adopts a high-end editorial aesthetic. We are building a digital conservatory—a space that feels breathable, curated, and deeply rooted in nature. 

To achieve this, we break the rigid "box-on-box" template by utilizing **intentional asymmetry** and **tonal layering**. Elements should feel like they are floating in an organic environment rather than locked into a grid. We use Plus Jakarta Sans to bridge the gap between a friendly gardening companion and a professional botanical authority. The experience is not just functional; it is a serene, tactile extension of the garden itself.

---

## 2. Colors
Our palette is derived from the lifecycle of a plant: from the deep chlorophyll of a forest floor to the soft cream of a blooming flower.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections. We define boundaries through **background color shifts** only. For example, a card utilizing `surface-container-low` should sit on a `background` or `surface` base. Contrast is achieved through tone, not stroke.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers—like stacked sheets of fine, heavy-weight paper. 
- **Base:** `background` (#fbf9f1) for the widest areas.
- **Sectioning:** Use `surface-container-low` (#f5f4ec) to group related content.
- **Elevation:** Use `surface-container-highest` (#e4e3db) for interactive or "top-layer" elements.

### The "Glass & Gradient" Rule
To elevate the UI beyond a flat digital interface:
- **Glassmorphism:** Use semi-transparent `surface` colors with a `backdrop-filter: blur(12px)` for floating navigation bars or modal overlays. This allows the lush botanical imagery and greens to bleed through, creating a "frosted glass" effect common in premium greenhouses.
- **Signature Textures:** Apply subtle linear gradients (e.g., `primary` #154212 to `primary-container` #2D5A27) for Hero CTAs. This provides a "soul" and depth that static hex codes cannot replicate.

---

## 3. Typography
We utilize **Plus Jakarta Sans** for its geometric clarity and modern warmth. 

- **Display Scale (`display-lg` to `display-sm`):** Reserved for high-impact editorial moments, like plant names or "Garden Health" scores. These should feel authoritative and large.
- **Headline & Title Scale:** Used for modular headers. We use tight letter-spacing (-0.02em) on headlines to create a sophisticated, "magazine" feel.
- **Body & Label Scale:** Our body text uses `on-surface-variant` (#42493e) to maintain high readability while feeling softer and more organic than pure black.

**Identity Note:** The hierarchy is designed to guide the eye from the "Emotional" (Large Display) to the "Functional" (Small Label) without visual friction.

---

## 4. Elevation & Depth
Depth is achieved through **Tonal Layering** rather than traditional drop shadows.

- **The Layering Principle:** A `surface-container-lowest` card placed on a `surface-container-low` section creates a soft, natural lift. This mimics how leaves overlap in nature.
- **Ambient Shadows:** When a floating effect is required (e.g., a "Watering Reminder" FAB), use extra-diffused shadows. 
    - **Blur:** 24px–48px
    - **Opacity:** 4%-6% 
    - **Color:** Use a tinted version of `on-surface` (#1b1c17) to mimic natural light, never a flat grey.
- **The "Ghost Border" Fallback:** If a container absolutely requires a boundary for accessibility, use the `outline-variant` token at **15% opacity**. High-contrast, 100% opaque borders are strictly forbidden.

---

## 5. Components

### Buttons
- **Primary:** `primary` background with `on-primary` text. Use `xl` (1.5rem) roundedness. Apply a subtle gradient for a premium feel.
- **Secondary:** `secondary-container` background. No border.
- **Tertiary:** Purely typographic using `primary` text color, used for low-priority actions.

### Cards & Lists
**Forbidden:** Divider lines between items.
**Requirement:** Use **Vertical White Space** (min. 24px) or a background shift to `surface-container-low` to separate list items. Cards should have `lg` (1rem) rounded corners and use tonal nesting to define their presence.

### Input Fields
- **Styling:** Use a `surface-container-high` background with no border. 
- **States:** On focus, transition the background to `surface-bright` and add a "Ghost Border" using `primary`.

### Specialized Components
- **Plant Vitality Gauges:** Use organic, thin-line circular strokes. Avoid thick, "dashboard" styles.
- **Botanical Chips:** Use `secondary-fixed` for filter chips (e.g., "Indoor," "Succulent") to provide a soft color punch that doesn't compete with primary actions.

---

## 6. Do's and Don'ts

### Do
- **DO** use generous whitespace. Let the typography breathe like a plant in an open field.
- **DO** use overlapping elements. A plant image slightly breaking the bounds of its container creates a custom, high-end feel.
- **DO** prioritize "softness." Every corner should be rounded (`md` to `xl`) to reflect the organic nature of gardening.

### Don't
- **DON'T** use pure black (#000000). Use `on-background` (#1b1c17) or `primary` (#154212) for text to maintain the natural palette.
- **DON'T** use standard Material Design drop shadows. They feel too "tech" and "cold."
- **DON'T** use 1px lines to separate content. If the layout feels messy without lines, increase your spacing or adjust your tonal layers.