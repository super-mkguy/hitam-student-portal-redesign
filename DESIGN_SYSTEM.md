# HITAM Student Portal — Accessible Design System

**Task 04 · Component library and interactive prototype**  
**Live concept:** [Open the HITAM Student Portal](https://hitam-student-app-redesign-hzapp6mecm8fcswqcuui3nn.streamlit.app/), then choose **Design system** in the main menu.

## Short explanation

This compact system gives the HITAM portal a consistent forest-green identity while keeping text and controls easy to distinguish. The live **Design system** page demonstrates the same native components used on the student-facing screens, including primary and secondary actions, labeled inputs, cards, navigation, and success, warning, error, and information states. The attendance screen is an interactive concept that lets reviewers select a course, adjust an illustrative target, and preview a data-loading error.

All student and academic details are sample content. The prototype does not connect to HITAM systems or save form entries.

## 1. Design tokens

| Token | Value | Use |
|---|---|---|
| Forest | `#155B37` | Primary actions, links, selected navigation |
| Deep forest | `#103D2B` | Dark brand treatment and contrast reference |
| Leaf accent | `#4DB03C` | Decorative accent only; avoid for text on white |
| Ink | `#17251C` | Headings and body text |
| Muted text | `#526157` | Supporting copy and captions |
| Canvas | `#F3F6F4` | Main page background |
| Surface | `#FFFFFF` | Cards and form surfaces |
| Pale green | `#E8F2E9` | Success and selected-state backgrounds |
| Control outline | `#66786A` | Visible control/card boundary and focus support |
| Error | `#8B3026` on `#FFF1EE` | Error text and surface |
| Warning | `#875500` on `#FFF4DD` | Warning text and surface |
| Information | `#1E5278` on `#EAF3F9` | Informational text and surface |

### Typography

- Use the sans-serif system font for body text and headings.
- Body and important helper text use the 16 px text style. Reserve smaller captions for noncritical metadata.
- Heading sizes: 32, 24, 20, and 16 px, using bold or semibold weights.
- Use sentence case for page titles, control labels, and buttons.

### Spacing and shape

- Spacing scale: 4, 8, 12, 16, 24, 32, and 48 px.
- Keep labels close to their fields; separate unrelated content with larger section gaps.
- Use a 12 px base corner radius and clear container boundaries.

### Elevation

- Page canvas: flat, pale neutral surface.
- Cards and grouped fields: white surface with a visible outline.
- No decorative shadows. Use spacing, headings, and borders to communicate hierarchy.

### Icon rules

- Use familiar Material Symbols with a visible text label for actions and navigation.
- Use icons to reinforce a state, never as its only signal.
- Statuses always have a text label such as “On track” or “Below target.”

## 2. Reusable component rules

| Component | Pattern | Accessible behavior |
|---|---|---|
| Primary button | Forest fill, concise verb label, optional familiar icon | White label; use only for the main action; retain native keyboard and focus behavior |
| Secondary button | Bordered/default button | Use for a safe alternative; do not hide the label in an icon |
| Disabled button | Native disabled state | Keep the reason visible nearby when the action is unavailable |
| Text input | Persistent visible label, short example placeholder | Validate after submit; place the error beside the form and identify what to fix |
| Select | Visible label and clear options | Use for a single choice from a longer list |
| Card | Bordered container with heading, summary, and next action | Keep heading order logical; do not rely on color alone to group data |
| Navigation | Persistent sidebar with familiar symbols and text labels | Keep the active page identifiable; labels remain visible |
| Feedback | Native success, warning, error, and info alerts | Use concise text and an action when recovery is needed |

The app implements these with native Streamlit widgets and bordered containers. This keeps keyboard behavior and default focus handling consistent with the framework.

## 3. Contrast check

Ratios below use the WCAG relative-luminance formula. WCAG AA targets are **4.5:1 for normal text**, **3:1 for large text**, and **3:1 for meaningful control boundaries and graphical indicators**.

| Foreground | Background | Ratio | Intended use |
|---|---|---:|---|
| `#17251C` | `#F3F6F4` | 14.64:1 | Body text on canvas |
| `#526157` | `#F3F6F4` | 6.02:1 | Supporting copy on canvas |
| `#FFFFFF` | `#155B37` | 8.13:1 | Primary button label / forest sidebar |
| `#FFFFFF` | `#103D2B` | 12.18:1 | White text on deep forest |
| `#155B37` | `#E8F2E9` | 7.09:1 | Text on pale green |
| `#8B3026` | `#FFF1EE` | 7.48:1 | Error text and surface |
| `#875500` | `#FFF4DD` | 5.78:1 | Warning text and surface |
| `#1E5278` | `#EAF3F9` | 7.38:1 | Information text and surface |
| `#66786A` | `#FFFFFF` | 4.71:1 | Control outline against white |
| `#4DB03C` | `#FFFFFF` | 2.77:1 | Decorative accent only; fails for text |

The live **Contrast checker** on the Design system page lets reviewers explore any foreground/background pair and shows whether it clears the normal-text AA target. These checks cover listed color pairs, not every browser, zoom, focus, or assistive-technology state; a complete accessibility audit still needs manual review.

## Prototype states to review

1. Open **Attendance** and select a course.
2. Adjust **Preview attendance target** to see both on-track and below-target feedback.
3. Turn on **Preview: simulate unavailable attendance records**, then try Retry.
4. Open **Design system** to inspect button, input validation, navigation, card, feedback, and contrast examples.

The 75% target is an illustrative placeholder, not a verified HITAM rule. Confirm the institutional policy before implementation.
