"""
Tests for codeinsult.messages.registry — language provider registration.
"""

import pytest

from codeinsult.messages.base import BaseMessageProvider, MessageCatalog
from codeinsult.messages.registry import (
    available_languages,
    get_provider,
    register_provider,
)

# ── Helper fixtures ───────────────────────────────────────────────────────────


class _FakeProvider(BaseMessageProvider):
    """Fake provider used for registration tests."""

    @property
    def catalog(self) -> MessageCatalog:
        return MessageCatalog(lang="fake", lang_name="Fake Language")

    @classmethod
    def lang_code(cls) -> str:
        return "fake"


class _FakeProvider2(BaseMessageProvider):
    """Second fake provider for testing multiple registrations."""

    @property
    def catalog(self) -> MessageCatalog:
        return MessageCatalog(lang="fake2", lang_name="Fake 2")

    @classmethod
    def lang_code(cls) -> str:
        return "fake2"


class _NotAProvider:
    """Class that is NOT a provider — used to test type errors."""

    pass


# ── Tests ──────────────────────────────────────────────────────────────────────


class TestRegisterProvider:
    """Tests for register_provider()."""

    def test_registers_valid_provider(self) -> None:
        """Should register a valid provider without errors."""
        # Should not raise an exception
        register_provider(_FakeProvider)

    def test_raises_type_error_for_non_provider(self) -> None:
        """Should raise TypeError for a class not inheriting from BaseMessageProvider."""
        with pytest.raises(TypeError, match="must be a subclass"):
            register_provider(_NotAProvider)  # type: ignore[arg-type]


class TestGetProvider:
    """Tests for get_provider()."""

    def test_returns_registered_provider(self) -> None:
        """Should return the registered provider for the language."""
        register_provider(_FakeProvider)
        provider = get_provider("fake")
        assert isinstance(provider, _FakeProvider)

    def test_raises_value_error_for_unknown_lang(self) -> None:
        """Should raise ValueError for an unregistered language."""
        with pytest.raises(ValueError, match="Idioma"):
            get_provider("mars")


class TestAvailableLanguages:
    """Tests for available_languages()."""

    def test_returns_list_of_strings(self) -> None:
        """Should return a list of strings."""
        langs = available_languages()
        assert isinstance(langs, list)
        for lang in langs:
            assert isinstance(lang, str)

    def test_includes_pt_br_by_default(self) -> None:
        """'pt_br' should be available (registered on package import)."""
        langs = available_languages()
        assert "pt_br" in langs
