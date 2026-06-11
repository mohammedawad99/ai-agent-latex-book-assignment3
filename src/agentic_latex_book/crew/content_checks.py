"""Offline checks for generated content/evidence.

Pure-string checks used to spot the failure modes from the first full run before
trusting any output: off-topic content, placeholder cover fields, and missing
mandatory PDF elements. No API key is read and nothing external is called.
"""

from __future__ import annotations

from agentic_latex_book.crew.instructions import MANDATORY_PDF_ELEMENTS

# Specific off-topic title produced by the rejected first full run (D-024).
FORBIDDEN_TOPIC_TERMS = ("Understanding and Implementing Gradient Descent",)

# Placeholder cover markers that must never appear in accepted content.
PLACEHOLDER_MARKERS = (
    "[Your Name/Placeholder Name]",
    "[Optional Affiliation/Institution]",
    "[Your Name]",
    "October 2023",
)


def find_forbidden_terms(text: str) -> list[str]:
    """Return any forbidden off-topic terms present in ``text``."""
    lowered = text.lower()
    return [term for term in FORBIDDEN_TOPIC_TERMS if term.lower() in lowered]


def find_placeholders(text: str) -> list[str]:
    """Return any placeholder markers present in ``text``."""
    lowered = text.lower()
    return [marker for marker in PLACEHOLDER_MARKERS if marker.lower() in lowered]


def is_on_topic(text: str, topic: str) -> bool:
    """True when the topic's leading phrase appears in ``text``."""
    head = topic.split(":", 1)[0].strip().lower()
    return bool(head) and head in text.lower()


def missing_mandatory_elements(text: str) -> list[str]:
    """Return mandatory PDF elements not mentioned in ``text``."""
    lowered = text.lower()
    return [element for element in MANDATORY_PDF_ELEMENTS if element.lower() not in lowered]


def check_content(text: str, topic: str) -> dict:
    """Summarize on-topic, forbidden, and placeholder checks for ``text``."""
    forbidden = find_forbidden_terms(text)
    placeholders = find_placeholders(text)
    on_topic = is_on_topic(text, topic)
    return {
        "on_topic": on_topic,
        "forbidden": forbidden,
        "placeholders": placeholders,
        "ok": on_topic and not forbidden and not placeholders,
    }
