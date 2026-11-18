"""Reusable, native Streamlit patterns for the HITAM portal concept."""

from __future__ import annotations

import streamlit as st


TOKENS = {
    "forest": "#155B37",
    "forest_deep": "#103D2B",
    "leaf_accent": "#4DB03C",
    "ink": "#17251C",
    "muted": "#526157",
    "canvas": "#F3F6F4",
    "surface": "#FFFFFF",
    "surface_green": "#E8F2E9",
    "control_border": "#66786A",
    "error_text": "#8B3026",
    "error_surface": "#FFF1EE",
    "warning_text": "#875500",
    "warning_surface": "#FFF4DD",
    "info_text": "#1E5278",
    "info_surface": "#EAF3F9",
}


def contrast_ratio(foreground: str, background: str) -> float:
    """Return WCAG relative-luminance contrast ratio for two hex colors."""

    def luminance(color: str) -> float:
        channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [
            channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
            for channel in channels
        ]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    lighter, darker = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def status_badge(percentage: int, target: int) -> str:
    """Render a text status badge; color is supplementary to the label."""
    if percentage >= target:
        st.badge("On track", icon=":material/check_circle:", color="green")
        return "On track"
    st.badge("Below target", icon=":material/warning:", color="red")
    return "Below target"


def feedback_state(state: str, message: str) -> None:
    """Render a consistent feedback state using native Streamlit alerts."""
    renderers = {
        "success": st.success,
        "warning": st.warning,
        "error": st.error,
        "info": st.info,
    }
    renderer = renderers.get(state, st.info)
    renderer(message)


def render_course_card(course: dict[str, int | str], target: int) -> None:
    """Render a reusable course summary card with visible status text."""
    percentage = round(int(course["attended"]) / int(course["held"]) * 100)
    with st.container(border=True):
        st.subheader(str(course["name"]))
        st.metric("Attendance", f"{percentage}%", f'{course["attended"]} of {course["held"]} classes')
        status_badge(percentage, target)
