# HITAM Student Portal Redesign — Usability Test & Case Study

**Task 05 · Usability study with three individual testers**
**Interactive prototype:** [Open the public HITAM portal](https://hitam-student-app-redesign-hzapp6mecm8fcswqcuui3nn.streamlit.app/)  
**Current testing state:** Three individual testers attempted the five tasks. Results below reflect only the outcomes provided; elapsed times, exact hints, and reasons for difficulty were not recorded.

> **Study note:** The three testers are labeled P1–P3. Where notes only say “was able to find” or “submitted successfully,” hint use was not specified, so those outcomes are not counted as confirmed unassisted completions.

## Short explanation

This case study follows one student goal: check course attendance and decide what to do next. Three individual testers tried five tasks. All three needed a hint on Task 2 and could not complete Task 3. The prototype now explains the preview target more plainly and gives Retry stronger emphasis. The reasons for those outcomes still need to be explored in a follow-up test.

## Project overview

- **Product:** HITAM Student Portal redesign concept
- **Target user:** A student who checks academic status, attendance, schedules, and course feedback on a phone or laptop.
- **Primary journey:** Dashboard → Attendance → choose a course → understand its status → take an appropriate next step.
- **Scope:** The prototype is a visual interaction concept. It is not connected to HITAM records.
- **Content:** All student names, classes, percentages, schedules, and other records are illustrative.

## Evidence and decision trail

| Evidence | What it suggested | Design decision | How to validate |
|---|---|---|---|
| In the initial screenshot review, the requester said headings blended into the background and asked for dark text on a white surface. | Text and surface contrast must be obvious at a glance. | Established dark ink on a light canvas, forest green actions, semantic feedback colors, and a live contrast checker. | Verify text/control pairs against the AA thresholds; observe whether testers can read and interpret status labels. |
| The portal task flow includes attendance, timetable, assignments, and feedback. | A student needs a short route from status to action. | Made Attendance a direct Dashboard quick action and added course detail with timetable/advisor routes. | Measure unassisted completion and time for Tasks 1, 2, and 4. |
| Heuristic walkthrough of the previous Attendance page: it showed an aggregate metric and a plain course table, without a course-level recovery step or an unavailable-record state. | A percentage alone does not explain what to do, and missing data needs recovery. | Added selectable course detail, attended/held counts, visible status text, next steps, and a simulated load-error state with Retry and Dashboard actions. | Measure whether testers interpret the number and recover from Task 3 without moderator help. |
| Earlier wireframe work used 75% as a placeholder; no official HITAM attendance rule was verified. | A prototype value could be mistaken for college policy. | Label the control as a preview target and disclose that policy needs verification. | Ask testers what they think the threshold represents; confirm it with HITAM before any production use. |
| Three testers completed Tasks 1, 4, and 5; the notes do not say whether hints were used or how long tasks took. | Those tasks were completed by all three, but unassisted success and efficiency cannot be measured from these notes. | Record the 3/3 reported completion and mark hint use/time as not recorded. | Capture hint use and elapsed time during the next round. |
| All three testers needed a hint on Task 2. | This task has a repeated assistance need, but the hint and point of confusion were not recorded. | Added a direct explanation of the example target and its status outcomes. | Re-test and ask what was unclear before giving a hint. |
| All three testers were unable to complete Task 3. | The recovery task is a high-priority problem; the specific blocker is unknown. | Clarified the error guidance and emphasized Retry as the primary action. | Observe where each tester gets stuck and whether Retry works as expected. |

The earlier heuristic walkthrough is design inspection evidence; the last three rows are reported participant outcomes. The notes contain outcomes only, not times or detailed observations.

## Before and after

The comparison below reconstructs the baseline from the earlier repository version and the updated flow from the current prototype. It is a schematic, not a participant screenshot. The current version includes clearer Task 2 target guidance and a more prominent Task 3 Retry action in response to the reported outcomes.

![Schematic before-and-after comparison of the HITAM attendance prototype](docs/task-05-before-after.svg)

### What changed

- **Before:** dashboard access relied on the main menu; the Attendance page showed an aggregate and a plain table.
- **After:** Dashboard has a prominent Attendance shortcut; students select a course, see the calculation and text status, and get a next step.
- **Task 2 update:** The attendance target now explains the “at or above” and “below target” labels directly and says the value is not confirmed HITAM policy.
- **Recovery:** an unavailable-record preview shows an explanation plus Retry and Back to Dashboard, replacing the unavailable course detail.
- **Task 3 update:** The error message explains the recovery choices and Retry is the primary action.
- **Accessibility:** color is paired with status text, controls have visible labels, the green-on-light and white-on-green pairs meet the documented contrast targets, and the app uses native keyboard-operable controls.

## Five moderated usability tasks

Read each scenario as written. Let the participant work without hints unless they ask to stop. Start a timer at the end of the prompt; record the first meaningful hesitation, wrong turn, and recovery. Do not collect names, email addresses, student IDs, grades, or personal comments.

| # | Scenario to read | Success measure | Time target |
|---:|---|---|---:|
| 1 | “You want to check whether Data Structures needs attention. Starting from the dashboard, find its current attendance and tell me what the portal says.” | Reaches Attendance, selects Data Structures, and reports **64%** and **Below target** without a hint. | ≤60 sec |
| 2 | “You are checking Database Systems. Is it on track against the example target shown here?” | Selects Database Systems, finds **88%**, and correctly interprets the visible status as on track for the current preview target. | ≤45 sec |
| 3 | “Attendance records are temporarily unavailable. Show me how you would recover.” | Moderator turns on the error-preview switch before the task. Participant explains the error, chooses Retry, and sees course details return; no hint. | ≤45 sec |
| 4 | “You want to see when Data Structures meets. Starting from its attendance details, find its timetable entries.” | Uses the timetable action, identifies at least one Data Structures time slot, and returns or explains where they are. | ≤60 sec |
| 5 | “You want to leave course feedback. Choose a term, give a rating, and submit a short non-personal comment.” | Completes the labeled form, sees confirmation, and understands that this concept does not send or save the feedback. | ≤90 sec |

**Overall success criteria:** Record completion for each task as unassisted, completed with a hint, or not completed. Track time, wrong turns, and critical errors separately. For the three-person sample, the initial design goal is at least **2 of 3 unassisted completions per task** and **zero critical errors**; any task with fewer than 2 unassisted completions, repeated confusion, or a critical error becomes a revision candidate. This small sample is directional and is not statistically representative.

From the notes provided, Task 2 had **0 of 3 unassisted completions** because all three needed a hint, and Task 3 had **0 of 3 completions**. Unassisted completion cannot be determined for Tasks 1, 4, or 5 because hint use was not specified.

## Session protocol and anonymous observation sheet

### Moderator opening

“I’m evaluating the prototype, not you. Some content is sample data and nothing is sent to HITAM. Please think aloud as you go. You can stop at any time. I’ll take anonymous notes and won’t record your name or student details.”

Use participant codes **P1**, **P2**, and **P3** only. Record device class (phone/laptop) and broad familiarity (new/occasional/frequent) only if the participant agrees. Do not record identifying or sensitive details. Ask neutral follow-ups such as “What are you expecting here?” or “What would you do next?”

Before each session, open a fresh browser session, leave the attendance target at its default 75, and leave the unavailable-record preview switched off. For Task 3 only, the moderator should turn on the preview switch immediately before reading the task prompt; do not explain what the screen should say.

### Participant results

The notes supplied for these sessions did not include elapsed times, the text of the Task 2 hints, or the reasons Task 3 was not completed. “Completed” does not mean “unassisted” unless that was explicitly recorded.

| Participant code | Task 1 | Task 2 | Task 3 | Task 4 | Task 5 | Time / hint details / reason |
|---|---|---|---|---|---|---|
| P1 | Completed; hint use not recorded | Needed a hint | Not completed | Completed; hint use not recorded | Submitted successfully; hint use not recorded | Not recorded |
| P2 | Completed; hint use not recorded | Needed a hint | Not completed | Completed; hint use not recorded | Submitted successfully; hint use not recorded | Not recorded |
| P3 | Completed; hint use not recorded | Needed a hint | Not completed | Completed; hint use not recorded | Submitted successfully; hint use not recorded | Not recorded |

### Outcome summary

| Task | Reported outcome | What can be concluded |
|---:|---|---|
| 1 · Find attendance | 3/3 were able to find it | Completed by all three; hint use and time were not recorded. |
| 2 · Check the example target | 3/3 needed a hint | No unassisted completions were reported; hint wording and point of confusion were not recorded. |
| 3 · Recover from unavailable records | 0/3 completed | All three were unable to complete it; the specific blocker was not recorded. |
| 4 · Find the timetable | 3/3 were able to find it | Completed by all three; hint use and time were not recorded. |
| 5 · Submit feedback | 3/3 submitted successfully | Successful submissions were reported; hint use, time, and understanding of the confirmation were not recorded. |

### Observation log

The supplied notes contain aggregate outcomes but no detailed actions or hesitation notes. The two entries below preserve what was reported without guessing at the cause.

| Participant | Task | Observed action / hesitation | Expected result (participant’s words or paraphrase) | Outcome / time / hint | Design implication |
|---|---|---|---|---|---|
| P1–P3 | 2 | All three needed a hint | Not recorded | Hint needed; time not recorded | Explore what required the hint; target guidance was clarified provisionally. |
| P1–P3 | 3 | All three were unable to complete the task | Not recorded | Not completed; time not recorded | Observe the exact point of difficulty in a retest; error guidance and Retry emphasis updated provisionally. |

## Issue prioritization

The first issue below comes from the earlier heuristic review. The repeated Task 2 and Task 3 outcomes are reported tester findings; their specific causes were not captured.

| Priority | Candidate issue | Evidence source | Current response | Follow-up |
|---|---|---|---|---|
| P1 | None of the three testers completed the unavailable-record task. | Reported Task 3 result; exact blocker not captured. | Clarified error guidance and made Retry the primary action. | Re-test and record the exact point of failure before drawing conclusions about cause. |
| P1 | All three testers needed a hint to check the example target. | Reported Task 2 result; hint text and confusion point not captured. | Added a direct explanation of “at or above” versus “below” the example target. | Re-test and capture the unassisted outcome and what was unclear. |
| P2 | Hint use and time are unknown for Tasks 1, 4, and 5. | Notes report completion/submission only. | Avoided labeling these outcomes unassisted. | Record hints and elapsed time per task in the next round. |
| P2 | The 75% example can be mistaken for official policy. | Policy source not available in the project. | Labeled as a preview-only example and stated it is not confirmed HITAM policy. | Verify with HITAM; test participant understanding of the label. |

## Revision log

| Revision | Change | Reason | Evidence status |
|---|---|---|---|
| R1 | Replaced the Attendance-only aggregate/table screen with a course selector, detail summary, status, and contextual next steps. | Improve course-level decision support and support the required primary journey. | Heuristic design decision; awaiting user validation. |
| R2 | Added a recoverable unavailable-record state with Retry and Dashboard navigation. | Make the failure path explicit and recoverable. | Heuristic design decision; the interaction is present in the prototype, awaiting user validation. |
| R3 | Added an Attendance quick action to the Dashboard. | Reduce navigation effort to the main task. | Added during this iteration; test against Task 1. |
| R4 | Paired status color with text and labeled the 75% target as illustrative. | Avoid color-only communication and unsupported policy claims. | Contrast pairs documented; policy remains unverified. |
| R5 | Added plain-language guidance for the example target and what “at or above” versus “below” means. | All three testers needed a hint on Task 2; exact confusion point was not recorded. | Provisional response; re-test to see if it helps. |
| R6 | Clarified the unavailable-record message and made Retry the primary action. | All three testers were unable to complete Task 3; exact blocker was not recorded. | Provisional response; observe and re-test the recovery path. |

## Limitations and next step

- Only task outcomes were captured. Times, the Task 2 hint wording, the Task 3 blockers, and detailed observations were not recorded, so explanations for the results remain uncertain.
- The sample is small; report counts and examples, not broad claims about all HITAM students.
- Re-test Tasks 2 and 3 after these changes; record hint use, elapsed time, and the exact step where a tester hesitates or gets stuck.
- Confirm the real attendance threshold, schedule, and student-support route with HITAM.
- The prototype is not connected to student records and does not persist feedback.
- The Task 2 and Task 3 UI changes are provisional; do not claim they fixed the problems until a follow-up test supports that conclusion.

## Supporting project work

- [Task 03 — Information architecture and wireframes](TASK3_IA_WIREFRAMES.md)
- [Task 04 — Accessible design system](DESIGN_SYSTEM.md)
- [Prototype source repository](https://github.com/super-mkguy/hitam-student-portal-redesign)
- [Open the interactive prototype](https://hitam-student-app-redesign-hzapp6mecm8fcswqcuui3nn.streamlit.app/)

## Task guide

Prepared against the supplied [Usability Test and Portfolio Case Study brief](https://edvyro.in/datasets/task-kits/ui-ux-design-task-4.html) and the [student support design brief](https://edvyro.in/datasets/source-materials/task-source-library.html#ui-ux). The supplied task-kit URLs were not accessible through the web reader at the time of preparation; the checklist above follows the requirements included in the assignment prompt.
