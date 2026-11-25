from pathlib import Path

import streamlit as st

from design_system import TOKENS, contrast_ratio, feedback_state, render_course_card, status_badge

LOGO_PATH = Path(__file__).parent / "assets" / "hitam-logo.png"

st.set_page_config(
    page_title="HITAM Student Portal",
    page_icon=str(LOGO_PATH),
    layout="wide",
)

def _set_portal_page(page_name):
    st.session_state["portal_page"] = page_name


def _retry_attendance_preview():
    st.session_state["simulate_attendance_error"] = False


menu_icons = {
    "Dashboard": "dashboard",
    "Academic Calendar": "calendar_month",
    "Time Table": "calendar_view_week",
    "Assignments": "assignment",
    "Attendance": "bar_chart",
    "Results": "school",
    "Transport": "directions_bus",
    "Hostel": "home",
    "Feedback": "chat",
    "Profile": "person",
    "Design system": "tune",
}

st.sidebar.image(str(LOGO_PATH), width=84, alt="HITAM tree logo")
st.sidebar.caption("STUDENT PORTAL  ·  AY 2026–27")
st.sidebar.divider()

page = st.sidebar.radio(
    "MAIN MENU",
    list(menu_icons),
    key="portal_page",
    format_func=lambda item: f":material/{menu_icons[item]}:  {item}",
    width="stretch",
)

st.sidebar.divider()
st.sidebar.caption("A clear view of your campus life.")

st.image(str(LOGO_PATH), width=68, alt="HITAM tree logo")
st.title("HITAM Student Portal")
st.caption("Hyderabad Institute of Technology and Management")
st.space("small")

if page == "Dashboard":
    with st.container(border=True):
        st.badge("Student dashboard", icon=":material/dashboard:", color="green")
        st.header("Welcome back!")
        st.write("Your academic week, organized in one place.")

    st.space("medium")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Attendance", "89%", delta="Across 6 courses")
    col2.metric("Courses", "06", delta="This semester")
    col3.metric("Open assignments", "03", delta="1 due this week")
    col4.metric("Term GPA", "8.4", delta="Current term")

    st.progress(0.89, text="Overall attendance · illustrative sample")
    st.space("small")

    st.subheader("Quick access", icon=":material/bolt:")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.button("Attendance", type="primary", icon=":material/bar_chart:", width="stretch", key="quick_attendance", on_click=_set_portal_page, args=("Attendance",))
    with c2:
        st.button("Time Table", icon=":material/calendar_today:", width="stretch", key="quick_timetable", on_click=_set_portal_page, args=("Time Table",))
    with c3:
        st.button("Assignments", icon=":material/assignment:", width="stretch", key="quick_assignments", on_click=_set_portal_page, args=("Assignments",))
    with c4:
        st.button("Feedback", icon=":material/chat:", width="stretch", key="quick_feedback", on_click=_set_portal_page, args=("Feedback",))

    st.space("medium")
    left, right = st.columns([1.1, 0.9], gap="large")
    with left.container(border=True):
        st.subheader("Up next", icon=":material/schedule:")
        st.markdown("**Data Structures · 11:00 AM**")
        st.caption("Room C-204 · Block C · Monday")
        st.markdown("**Database Systems · 12:00 PM**")
        st.caption("Room B-112 · Block B · Monday")
    with right.container(border=True):
        st.subheader("Due soon", icon=":material/notifications:")
        st.markdown("**Graph Traversal Lab**")
        st.caption("Due Thursday, 12 November · Data Structures")
        st.badge("Due in 4 days", color="orange")

    st.space("medium")
    st.subheader("Academic calendar", icon=":material/event:")
    st.dataframe(
        [
            {"Date": "12 Nov 2026", "Event": "Data Structures lab submission", "Type": "Assignment"},
            {"Date": "21 Nov 2026", "Event": "Library clearance reminder", "Type": "Reminder"},
            {"Date": "14 Dec 2026", "Event": "End-semester exams begin", "Type": "Academic"},
        ],
        width="stretch",
        hide_index=True,
        alt="Upcoming academic dates and campus events",
    )

elif page == "Academic Calendar":
    st.title("Academic calendar", icon=":material/calendar_month:")
    st.write("Key dates for the 2026–27 academic year.")
    st.dataframe(
        [
            {"Start date": "17 Aug 2026", "End date": "10 Oct 2026", "Description": "First spell of instructions"},
            {"Start date": "22 Oct 2026", "End date": "30 Nov 2026", "Description": "Second spell of instructions"},
            {"Start date": "01 Dec 2026", "End date": "12 Dec 2026", "Description": "Revision and practical assessments"},
            {"Start date": "14 Dec 2026", "End date": "24 Dec 2026", "Description": "End-semester examinations"},
        ],
        width="stretch",
        hide_index=True,
        alt="Academic instruction and examination calendar",
    )

elif page == "Time Table":
    st.title("Weekly time table", icon=":material/calendar_view_week:")
    st.write("A weekly schedule, laid out by time and day.")
    st.dataframe(
        [
            {"Time": "09:00–10:00", "Monday": "Data Structures", "Tuesday": "Database Systems", "Wednesday": "Operating Systems", "Thursday": "Computer Networks", "Friday": "DS Lab"},
            {"Time": "10:00–11:00", "Monday": "Database Systems", "Tuesday": "Computer Networks", "Wednesday": "Data Structures", "Thursday": "DB Lab", "Friday": "Software Engineering"},
            {"Time": "11:15–12:15", "Monday": "Mathematics III", "Tuesday": "Data Structures", "Wednesday": "Mathematics III", "Thursday": "Operating Systems", "Friday": "Computer Networks"},
            {"Time": "12:15–13:00", "Monday": "Lunch", "Tuesday": "Lunch", "Wednesday": "Lunch", "Thursday": "Lunch", "Friday": "Lunch"},
            {"Time": "13:00–14:00", "Monday": "Operating Systems", "Tuesday": "Mathematics III", "Wednesday": "Database Systems", "Thursday": "Software Engineering", "Friday": "Project Lab"},
            {"Time": "14:00–15:00", "Monday": "Tutorial", "Tuesday": "Operating Systems", "Wednesday": "Project Lab", "Thursday": "Mathematics III", "Friday": "Mentor Hour"},
        ],
        width="stretch",
        hide_index=True,
        alt="Weekly class timetable by day and time",
    )

elif page == "Assignments":
    st.title("Class assignments", icon=":material/assignment:")
    st.write("A simple view of what is due and what is already underway.")
    a1, a2, a3 = st.columns(3)
    a1.metric("Open", "03")
    a2.metric("Due this week", "01")
    a3.metric("Completed", "02")
    st.dataframe(
        [
            {"Assignment": "Graph Traversal Lab", "Course": "Data Structures", "Due date": "12 Nov 2026", "Status": "In progress"},
            {"Assignment": "Normalization Worksheet", "Course": "Database Systems", "Due date": "15 Nov 2026", "Status": "Not started"},
            {"Assignment": "CPU Scheduling Report", "Course": "Operating Systems", "Due date": "19 Nov 2026", "Status": "In progress"},
            {"Assignment": "Network Topology Exercise", "Course": "Computer Networks", "Due date": "06 Nov 2026", "Status": "Submitted"},
            {"Assignment": "UML Mini Project", "Course": "Software Engineering", "Due date": "04 Nov 2026", "Status": "Submitted"},
        ],
        width="stretch",
        hide_index=True,
        alt="Assignments with their course, due date, and status",
    )

elif page == "Attendance":
    st.title("Attendance", icon=":material/bar_chart:")
    st.write("Review the sample course records and choose a course for details.")
    courses = [
        {"name": "Data Structures", "attended": 9, "held": 14},
        {"name": "Database Systems", "attended": 22, "held": 25},
        {"name": "Operating Systems", "attended": 23, "held": 25},
        {"name": "Mathematics III", "attended": 24, "held": 25},
        {"name": "Computer Networks", "attended": 20, "held": 22},
        {"name": "Software Engineering", "attended": 20, "held": 22},
    ]
    total_attended = sum(int(course["attended"]) for course in courses)
    total_held = sum(int(course["held"]) for course in courses)
    overall = round(total_attended / total_held * 100)
    st.metric("Overall attendance", f"{overall}%", delta=f"{total_attended} of {total_held} classes")
    st.progress(overall / 100, text="Across 6 illustrative courses")

    target = st.slider("Preview attendance target", 50, 100, 75, key="attendance_target")
    st.info(
        f"For this prototype, {target}% is the example target. "
        "At or above the target means on track; below it means below target. "
        "This is not confirmed HITAM policy."
    )
    selected_course_name = st.selectbox(
        "Choose a course", [str(course["name"]) for course in courses], key="attendance_course"
    )
    course = next(item for item in courses if item["name"] == selected_course_name)
    percentage = round(int(course["attended"]) / int(course["held"]) * 100)
    simulate_error = st.toggle("Preview: simulate unavailable attendance records", key="simulate_attendance_error")

    if simulate_error:
        feedback_state(
            "error",
            "Attendance records could not load. Choose Retry loading records to try again, "
            "or return to the dashboard.",
        )
        retry_col, dashboard_col = st.columns(2)
        retry_col.button(
            "Retry loading records", icon=":material/refresh:",
            type="primary",
            on_click=_retry_attendance_preview, key="attendance_retry",
        )
        dashboard_col.button(
            "Back to Dashboard", icon=":material/dashboard:",
            on_click=_set_portal_page, args=("Dashboard",), key="attendance_error_dashboard",
        )
    else:
        st.subheader(str(course["name"]))
        summary, next_step = st.columns(2, vertical_alignment="top")
        with summary.container(border=True):
            st.metric("Current attendance", f"{percentage}%", f'{course["attended"]} of {course["held"]} classes')
            st.progress(percentage / 100, text="Attendance progress")
            status_badge(percentage, target)
        with next_step.container(border=True):
            st.markdown("**Next step**")
            if percentage >= target:
                feedback_state("success", "This course is at or above the preview target.")
                st.caption("Check the overview again after your next class.")
            else:
                feedback_state("warning", "This course is below the preview target.")
                st.write("Review upcoming classes or ask your academic advisor for guidance.")
                action, help_action = st.columns(2)
                action.button(
                    "View time table",
                    type="primary",
                    icon=":material/calendar_today:",
                    width="stretch",
                    on_click=_set_portal_page,
                    args=("Time Table",),
                    key="attendance_timetable",
                )
                help_action.button(
                    "Open feedback",
                    icon=":material/chat:",
                    width="stretch",
                    on_click=_set_portal_page,
                    args=("Feedback",),
                    key="attendance_feedback",
                )

        st.subheader("Course overview")
        with st.grid("auto", min_column_width=220, gap="small"):
            for item in courses:
                render_course_card(item, target)

elif page == "Results":
    st.title("Examination results", icon=":material/school:")
    st.metric("Term GPA", "8.4", delta="Current term")
    st.dataframe(
        [
            {"Course": "Data Structures", "Score": "86 / 100", "Grade": "A"},
            {"Course": "Database Systems", "Score": "82 / 100", "Grade": "A"},
            {"Course": "Operating Systems", "Score": "78 / 100", "Grade": "B+"},
            {"Course": "Mathematics III", "Score": "84 / 100", "Grade": "A"},
            {"Course": "Computer Networks", "Score": "88 / 100", "Grade": "A"},
            {"Course": "Software Engineering", "Score": "90 / 100", "Grade": "A+"},
        ],
        width="stretch",
        hide_index=True,
        alt="Course results, scores, and grades",
    )

elif page == "Transport":
    st.title("Transport", icon=":material/directions_bus:")
    st.write("Route and subscription details.")
    t1, t2, t3 = st.columns(3)
    t1.metric("Subscription", "Active")
    t2.metric("Route", "05")
    t3.metric("Pickup time", "7:35 AM")
    with st.container(border=True):
        st.subheader("Route 05 · Miyapur to campus")
        st.markdown("**Pickup stop:** Miyapur Metro · **Bus:** HITAM-05")
        st.caption("Morning pickup 7:35 AM · Return departure 4:15 PM")
        st.badge("Subscribed", color="green")

elif page == "Hostel":
    st.title("Hostel services", icon=":material/home:")
    st.write("Residence details and request status.")
    h1, h2, h3 = st.columns(3)
    h1.metric("Residence", "Hall C")
    h2.metric("Room", "204")
    h3.metric("Request status", "Approved")
    with st.container(border=True):
        st.subheader("Current residence")
        st.markdown("**Hall C · Room 204**")
        st.caption("Requests for the next term open 1 December.")
        st.badge("Active", color="green")

elif page == "Feedback":
    st.title("Student feedback", icon=":material/chat:")
    st.write("Share feedback about your current courses.")
    term = st.selectbox("Select academic term", ["Select term", "Semester 1", "Semester 2"])
    rating = st.radio(
        "Rate your experience",
        ["Excellent - 4", "Very good - 3", "Good - 2", "Needs improvement - 1"],
    )
    comments = st.text_area("Comments", placeholder="What is working well? What could be better?")
    if st.button("Submit feedback", icon=":material/send:"):
        if term == "Select term":
            st.warning("Please select an academic term.")
        else:
            st.success("Thanks! Your feedback is ready. It is not sent or saved to the college system.")

elif page == "Profile":
    st.title("Student profile", icon=":material/person:")
    st.write("Profile overview.")
    p1, p2, p3 = st.columns(3)
    p1.metric("Student", "Student Name")
    p2.metric("Program", "B.Tech CSE")
    p3.metric("Year", "2nd year")
    with st.container(border=True):
        st.subheader("Contact details")
        email = st.text_input("Email address", placeholder="name@example.edu")
        mobile = st.text_input("Mobile number", placeholder="Enter a contact number")
        if st.button("Update details", icon=":material/save:"):
            st.success("This profile form is a concept and is not connected to HITAM.")

elif page == "Design system":
    st.title("Accessible design system", icon=":material/tune:")
    st.write("A compact HITAM component library, applied in the portal prototype below.")
    st.write("Use the examples on this page to explore buttons, inputs, navigation, cards, and feedback states.")

    st.subheader("Color tokens")
    color_rows = [
        {"Token": "Forest · primary action", "Hex": TOKENS["forest"], "Use": "Primary buttons, links, selected navigation"},
        {"Token": "Deep forest · sidebar", "Hex": TOKENS["forest_deep"], "Use": "Brand navigation surface"},
        {"Token": "Leaf accent · decoration", "Hex": TOKENS["leaf_accent"], "Use": "Small decorative accents; not text on white"},
        {"Token": "Ink · primary text", "Hex": TOKENS["ink"], "Use": "Headings and body text"},
        {"Token": "Muted · supporting text", "Hex": TOKENS["muted"], "Use": "Captions and helper copy"},
        {"Token": "Canvas · page background", "Hex": TOKENS["canvas"], "Use": "Main page surface"},
        {"Token": "Surface · cards and fields", "Hex": TOKENS["surface"], "Use": "Cards and input surfaces"},
        {"Token": "Control outline · focus support", "Hex": TOKENS["control_border"], "Use": "Visible boundaries and control outlines"},
        {"Token": "Success", "Hex": TOKENS["forest"], "Use": "Text and icons on pale green"},
        {"Token": "Warning", "Hex": TOKENS["warning_text"], "Use": "Text on pale amber"},
        {"Token": "Error", "Hex": TOKENS["error_text"], "Use": "Text on pale red"},
        {"Token": "Information", "Hex": TOKENS["info_text"], "Use": "Text on pale blue"},
    ]
    st.dataframe(
        color_rows,
        width="stretch",
        hide_index=True,
        alt="HITAM design system color tokens and their use",
    )

    st.subheader("Typography, spacing, and elevation")
    type_col, spacing_col, elevation_col = st.columns(3)
    with type_col.container(border=True):
        st.markdown("**Typography**")
        st.write("Sans-serif system font. Body and helper instructions use the 16 px text style.")
        st.write("Heading scale: 32 / 24 / 20 / 16 px with semibold-to-bold weights.")
    with spacing_col.container(border=True):
        st.markdown("**Spacing**")
        st.write("4 · 8 · 12 · 16 · 24 · 32 · 48 px scale.")
        st.write("Use generous section spacing; keep related form labels and controls close.")
    with elevation_col.container(border=True):
        st.markdown("**Elevation**")
        st.write("Flat page canvas, white bordered cards, no decorative shadows.")
        st.write("Use spacing and border contrast to show grouping; avoid color-only states.")

    st.subheader("Reusable components")
    st.markdown("**Buttons** · Use forest green for the main action, a bordered secondary action for alternatives, and a real disabled state when unavailable.")
    primary_col, secondary_col, disabled_col = st.columns(3)
    primary_col.button("Primary action", type="primary", icon=":material/check:", key="ds_primary_button")
    secondary_col.button("Secondary action", icon=":material/arrow_forward:", key="ds_secondary_button")
    disabled_col.button("Unavailable", disabled=True, key="ds_disabled_button")

    st.markdown("**Inputs** · Keep visible labels, useful examples, and validation beside the field that needs attention.")
    with st.form("ds_input_form"):
        name = st.text_input("Student name", placeholder="Enter a name")
        term = st.selectbox("Academic term", ["Choose a term", "Semester 1", "Semester 2"])
        submitted = st.form_submit_button("Preview form action", icon=":material/send:")
    if submitted:
        if not name.strip() or term == "Choose a term":
            feedback_state("error", "Add a student name and choose an academic term to continue.")
        else:
            feedback_state("success", "Form is complete. This preview does not save or send student data.")

    st.markdown("**Cards and status** · Keep each course’s number, status label, and next step together.")
    card_cols = st.columns(3)
    for column, state, copy in zip(
        card_cols,
        [("Data Structures", 68), ("Database Systems", 88), ("Operating Systems", 92)],
        ["Review upcoming classes", "Status is visible in text", "Check again next week"],
    ):
        with column.container(border=True):
            st.subheader(state[0])
            st.metric("Sample attendance", f"{state[1]}%")
            status_badge(state[1], 75)
            st.write(copy)

    st.markdown("**Navigation** · Keep the active selection clear and use familiar Material Symbols in the app menu.")
    nav_sample = st.segmented_control(
        "Navigation sample", ["Overview", "Courses", "Help"], default="Overview", key="ds_nav_sample"
    )
    st.caption(f"Selected destination: {nav_sample}")

    st.markdown("**Feedback states** · Pair a meaningful icon with a short message and visible action when needed.")
    feedback_choice = st.segmented_control(
        "Preview a feedback state", ["Success", "Warning", "Error", "Info"], default="Success", key="ds_feedback_choice"
    )
    feedback_messages = {
        "Success": ("success", "Attendance details are up to date."),
        "Warning": ("warning", "This course is below the example target."),
        "Error": ("error", "Attendance records could not load. Retry or return to the dashboard."),
        "Info": ("info", "Sample content is illustrative and is not connected to HITAM systems."),
    }
    feedback_state(*feedback_messages[feedback_choice])

    st.subheader("Contrast checker")
    st.write("Try a foreground and background pair. The live check uses WCAG contrast ratios.")
    foreground_col, background_col = st.columns(2)
    foreground = foreground_col.color_picker("Text or icon color", "#17251C", key="ds_foreground")
    background = background_col.color_picker("Background color", "#FFFFFF", key="ds_background")
    ratio = contrast_ratio(foreground, background)
    ratio_col, target_col = st.columns(2)
    ratio_col.metric("Current contrast", f"{ratio:.2f}:1")
    target_col.metric("WCAG AA body text", "4.5:1 minimum")
    if ratio >= 4.5:
        feedback_state("success", "This color pair meets the WCAG AA contrast ratio for normal text.")
    elif ratio >= 3:
        feedback_state("warning", "This pair meets 3:1 for large text and meaningful controls, but not normal body text.")
    else:
        feedback_state("error", "This pair does not meet the 3:1 minimum for large text or meaningful control boundaries.")
    st.caption("Contrast checks cover these selected colors only; they are not a complete accessibility audit of every browser state.")

st.divider()
st.caption("Concept prototype · Information is illustrative and not connected to HITAM systems.")

