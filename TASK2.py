import streamlit as st

st.set_page_config(
    page_title="HITAM Student Portal",
    page_icon="🎓",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #142B4A 0%, #10243E 100%);
}
[data-testid="stSidebar"] * {
    color: white;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    font-size: 1.125rem !important;
}
h1, h2, h3, h4 {
    color: #000000;
}
div[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 14px rgba(20, 43, 74, 0.06);
}
.welcome {
    background: linear-gradient(120deg, #142B4A 0%, #245081 100%);
    color: white;
    padding: 30px 34px;
    border-radius: 18px;
    box-shadow: 0 10px 28px rgba(20, 43, 74, 0.14);
}
.welcome h2 {
    color: white;
    margin-bottom: 0.25rem;
}
.welcome p {
    color: #E8F0FA;
    margin-bottom: 0;
}
.welcome .eyebrow {
    color: #BBD2EE;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)


def _set_portal_page(page_name):
    st.session_state["portal_page"] = page_name


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
}

st.sidebar.title("🎓 HITAM")
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

if page == "Dashboard":
    st.markdown("""
    <div class="welcome">
        <p class="eyebrow">Student dashboard</p>
        <h2>Welcome back!</h2>
        <p>Your academic week, organized in one place.</p>
    </div>
    """, unsafe_allow_html=True)

    st.space("medium")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Attendance", "92%", delta="On track")
    col2.metric("Courses", "06", delta="This semester")
    col3.metric("Open assignments", "03", delta="1 due this week")
    col4.metric("Term GPA", "8.4", delta="Current term")

    st.progress(0.92, text="Overall attendance")
    st.space("small")

    st.subheader("Quick access", icon=":material/bolt:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("Time Table", icon=":material/calendar_today:", width="stretch", key="quick_timetable", on_click=_set_portal_page, args=("Time Table",))
    with c2:
        st.button("Assignments", icon=":material/assignment:", width="stretch", key="quick_assignments", on_click=_set_portal_page, args=("Assignments",))
    with c3:
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
    )

elif page == "Attendance":
    st.title("Attendance", icon=":material/bar_chart:")
    st.metric("Overall attendance", "92%", delta="Above the 75% target")
    st.progress(0.92, text="Across all courses")
    st.dataframe(
        [
            {"Course": "Data Structures", "Classes attended": "23 / 25", "Attendance": "92%"},
            {"Course": "Database Systems", "Classes attended": "22 / 24", "Attendance": "92%"},
            {"Course": "Operating Systems", "Classes attended": "21 / 24", "Attendance": "88%"},
            {"Course": "Mathematics III", "Classes attended": "24 / 25", "Attendance": "96%"},
            {"Course": "Computer Networks", "Classes attended": "20 / 22", "Attendance": "91%"},
        ],
        width="stretch",
        hide_index=True,
    )

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

st.divider()
st.caption("Concept prototype · Information is illustrative and not connected to HITAM systems.")

