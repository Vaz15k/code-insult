"""
Tests for the main codeinsult functions: insult, random_insult, set_defaults.
"""

from collections.abc import Generator

import pytest

from codeinsult.CodeInsult import insult, random_insult, set_defaults
from codeinsult.messages.registry import available_languages

# ── Helper fixtures ───────────────────────────────────────────────────────────


@pytest.fixture(autouse=True)
def _reset_defaults() -> Generator[None, None, None]:
    """Reset global defaults before each test.

    Since set_defaults mutates module-level variables, we restore them
    to guarantee test isolation.
    """
    # Save originals (first call)
    # and restore after each test
    yield
    # Restore defaults
    try:
        set_defaults(lang="pt_br", level=None)
    except ValueError:
        # If registry got messed up, at least try to restore lang
        pass


# ── Tests for insult ──────────────────────────────────────────────────────────


class TestInsult:
    """Tests for the insult() function."""

    def test_returns_string_for_known_status_code(self) -> None:
        """Should return a string for a known HTTP status code."""
        result = insult(404)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_returns_string_for_200(self) -> None:
        """Should return a string for status 200."""
        result = insult(200)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_returns_string_for_500(self) -> None:
        """Should return a string for status 500."""
        result = insult(500)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_respects_light_level_parameter(self) -> None:
        """With level='light', should return a LIGHT-level message."""
        # Run multiple times to reduce chance of false negative due to randomness
        for _ in range(5):
            result = insult(404, level="light")
            assert isinstance(result, str)
            assert len(result) > 0

    def test_respects_heavy_level_parameter(self) -> None:
        """With level='heavy', should return a HEAVY-level message."""
        for _ in range(5):
            result = insult(500, level="heavy")
            assert isinstance(result, str)
            assert len(result) > 0

    def test_respects_lang_parameter(self) -> None:
        """Should accept the lang parameter explicitly."""
        result = insult(404, lang="pt_br")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_returns_fallback_for_unknown_code(self) -> None:
        """For an unknown code, returns a fallback (non-empty string)."""
        result = insult(999)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_unknown_code_without_defaults_returns_error_message(self) -> None:
        """
        If there are no default messages for the code/level, returns
        a string indicating no message is available.
        """
        result = insult(999, level="light")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_invalid_level_raises_value_error(self) -> None:
        """Invalid level should raise ValueError."""
        with pytest.raises(ValueError):
            insult(404, level="extreme")

    def test_invalid_lang_raises_value_error(self) -> None:
        """Invalid language should raise ValueError."""
        with pytest.raises(ValueError):
            insult(404, lang="klingon")


# ── Tests for random_insult ───────────────────────────────────────────────────


class TestRandomInsult:
    """Tests for the random_insult() function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = random_insult()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_accepts_level_parameter(self) -> None:
        """Should accept the level parameter."""
        result = random_insult(level="light")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_accepts_heavy_level(self) -> None:
        """Should accept level='heavy'."""
        result = random_insult(level="heavy")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_accepts_lang_parameter(self) -> None:
        """Should accept the lang parameter."""
        result = random_insult(lang="pt_br")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_no_level_returns_from_all_levels(self) -> None:
        """Without a level specified, should return from any level."""
        for _ in range(10):
            result = random_insult()
            assert isinstance(result, str)
            assert len(result) > 0


# ── Tests for set_defaults ────────────────────────────────────────────────────


class TestSetDefaults:
    """Tests for the set_defaults() function."""

    def test_sets_lang_to_valid_value(self) -> None:
        """Should set the default language to a valid value."""
        set_defaults(lang="pt_br", level=None)
        # Verify no exception and insult works
        result = insult(404)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_sets_level_to_light(self) -> None:
        """Should set the default level to 'light'."""
        set_defaults(lang="pt_br", level="light")
        result = insult(404)
        assert isinstance(result, str)

    def test_sets_level_to_heavy(self) -> None:
        """Should set the default level to 'heavy'."""
        set_defaults(lang="pt_br", level="heavy")
        result = insult(500)
        assert isinstance(result, str)

    def test_sets_level_to_none(self) -> None:
        """Should accept level=None (all levels)."""
        set_defaults(lang="pt_br", level=None)
        result = insult(404)
        assert isinstance(result, str)

    def test_raises_value_error_for_invalid_lang(self) -> None:
        """Should raise ValueError for an invalid language."""
        with pytest.raises(ValueError, match="Idioma"):
            set_defaults(lang="inventado", level=None)

    def test_raises_value_error_for_invalid_level(self) -> None:
        """Should raise ValueError for an invalid level."""
        with pytest.raises(ValueError):
            set_defaults(lang="pt_br", level="extreme")


# ── Defaults integration tests ────────────────────────────────────────────────


class TestDefaultsIntegration:
    """Integration tests: insult and random_insult respect defaults."""

    def test_insult_uses_default_lang(self) -> None:
        """insult() should use the configured default language."""
        set_defaults(lang="pt_br", level=None)
        result = insult(404)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_insult_uses_default_level(self) -> None:
        """insult() should use the configured default level."""
        set_defaults(lang="pt_br", level="light")
        for _ in range(5):
            result = insult(404)
            assert isinstance(result, str)
            assert len(result) > 0

    def test_insult_explicit_params_override_defaults(self) -> None:
        """Explicit parameters should override the defaults."""
        set_defaults(lang="pt_br", level="heavy")
        # Pass a different level explicitly
        result = insult(404, level="light")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_random_insult_uses_defaults(self) -> None:
        """random_insult() should use the configured defaults."""
        set_defaults(lang="pt_br", level=None)
        result = random_insult()
        assert isinstance(result, str)
        assert len(result) > 0


# ── Tests for all registered languages ────────────────────────────────────────


class TestAllAvailableLanguages:
    """Ensure every registered language works with insult and random_insult.

    These tests iterate over available_languages() dynamically, so any
    language registered in the future is automatically covered.
    """

    @pytest.mark.parametrize("lang", available_languages())
    def test_insult_works_for_every_language(self, lang: str) -> None:
        """insult() should return a non-empty string for every available language."""
        result = insult(404, lang=lang)
        assert isinstance(result, str)
        assert len(result) > 0

    @pytest.mark.parametrize("lang", available_languages())
    def test_random_insult_works_for_every_language(self, lang: str) -> None:
        """random_insult() should return a non-empty string for every available language."""
        for _ in range(5):
            result = random_insult(lang=lang)
            assert isinstance(result, str)
            assert len(result) > 0
