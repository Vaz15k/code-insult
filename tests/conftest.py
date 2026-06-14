"""
Shared fixtures for all codeinsult tests.
"""

import pytest
from codeinsult.config import InsultLevel
from codeinsult.messages.base import MessageCatalog


@pytest.fixture
def sample_catalog() -> MessageCatalog:
    """Minimal message catalog for testing."""
    return MessageCatalog(
        lang="test",
        lang_name="Test Language",
        messages={
            200: {
                InsultLevel.LIGHT: ["Smooth sailing."],
                InsultLevel.HEAVY: ["IT FUCKING WORKED!"],
            },
            404: {
                InsultLevel.LIGHT: ["Couldn't find it, sorry."],
                InsultLevel.MEDIUM: ["404: Not here."],
            },
            500: {
                InsultLevel.HEAVY: ["SHIT HIT THE FAN!"],
            },
        },
        default_messages={
            InsultLevel.LIGHT: ["Default light response."],
            InsultLevel.MEDIUM: ["Default medium response."],
            InsultLevel.HEAVY: ["Default heavy response."],
        },
    )
