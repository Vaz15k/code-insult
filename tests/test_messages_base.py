"""
Tests for codeinsult.messages.base — MessageCatalog and BaseMessageProvider.
"""

import pytest

from codeinsult.config import InsultLevel
from codeinsult.messages.base import BaseMessageProvider, MessageCatalog


class TestMessageCatalogGetMessages:
    """Tests for MessageCatalog.get_messages()."""

    def test_returns_specific_messages_for_known_code_and_level(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """Should return specific messages for a known code and level."""
        result = sample_catalog.get_messages(200, InsultLevel.LIGHT)
        assert result == ["Smooth sailing."]

    def test_returns_all_level_messages_when_level_is_none(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """When level=None, should return messages from all levels."""
        result = sample_catalog.get_messages(404, None)
        assert "Couldn't find it, sorry." in result
        assert "404: Not here." in result
        assert len(result) == 2

    def test_falls_back_to_default_for_level_not_in_code(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """If the code exists but lacks the requested level, fall back to default."""
        result = sample_catalog.get_messages(200, InsultLevel.MEDIUM)
        assert result == ["Default medium response."]

    def test_falls_back_to_default_for_unknown_code_and_level(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """For an unknown code, fall back to default messages for the level."""
        result = sample_catalog.get_messages(999, InsultLevel.LIGHT)
        assert result == ["Default light response."]

    def test_falls_back_to_default_when_code_has_no_specific_level(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """
        When the code exists but lacks the requested level,
        it should fall back to the default messages.
        """
        result = sample_catalog.get_messages(200, InsultLevel.MEDIUM)
        assert result == ["Default medium response."]

    def test_all_levels_falls_back_to_all_defaults(self) -> None:
        """level=None with an unknown code should fall back to all-level defaults."""
        catalog = MessageCatalog(
            lang="t",
            lang_name="T",
            messages={},
            default_messages={
                InsultLevel.LIGHT: ["L default"],
                InsultLevel.HEAVY: ["H default"],
            },
        )
        result = catalog.get_messages(999, None)
        assert "L default" in result
        assert "H default" in result


class TestMessageCatalogHasMessages:
    """Tests for MessageCatalog.has_messages()."""

    def test_returns_true_for_known_code_and_level(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """Should return True when messages exist."""
        assert sample_catalog.has_messages(404, InsultLevel.LIGHT) is True

    def test_returns_false_for_unknown_code(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """Should return False for a non-existent code."""
        assert sample_catalog.has_messages(999, InsultLevel.LIGHT) is False

    def test_returns_true_when_any_level_has_messages(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """With level=None, returns True if any level has a message."""
        assert sample_catalog.has_messages(200, None) is True

    def test_returns_false_when_no_level_has_messages(self) -> None:
        """With level=None and unknown code, returns False."""
        catalog = MessageCatalog(lang="t", lang_name="T")
        assert catalog.has_messages(999, None) is False

    def test_returns_false_for_level_without_messages(
        self, sample_catalog: MessageCatalog
    ) -> None:
        """Returns False when the code has messages but not for the requested level."""
        assert sample_catalog.has_messages(200, InsultLevel.MEDIUM) is False


class TestMessageCatalogAttributes:
    """Tests for MessageCatalog attributes."""

    def test_lang_is_stored_correctly(self) -> None:
        """The lang attribute should be stored correctly."""
        catalog = MessageCatalog(lang="pt_br", lang_name="Português")
        assert catalog.lang == "pt_br"

    def test_lang_name_is_stored_correctly(self) -> None:
        """The lang_name attribute should be stored correctly."""
        catalog = MessageCatalog(lang="en", lang_name="English")
        assert catalog.lang_name == "English"

    def test_default_messages_dict_is_empty_by_default(self) -> None:
        """default_messages should be an empty dict by default."""
        catalog = MessageCatalog(lang="x", lang_name="X")
        assert catalog.default_messages == {}


class TestBaseMessageProvider:
    """Tests for BaseMessageProvider (abstract class)."""

    def test_cannot_instantiate_directly(self) -> None:
        """Should not be possible to instantiate BaseMessageProvider directly."""
        with pytest.raises(TypeError):
            BaseMessageProvider()  # type: ignore[abstract]

    def test_concrete_subclass_can_be_instantiated(self) -> None:
        """A concrete subclass should be instantiable."""

        class FakeProvider(BaseMessageProvider):
            @property
            def catalog(self) -> MessageCatalog:
                return MessageCatalog(lang="fk", lang_name="Fake")

            @classmethod
            def lang_code(cls) -> str:
                return "fk"

        provider = FakeProvider()
        assert provider.lang_code() == "fk"
        assert provider.catalog.lang == "fk"

    def test_get_messages_delegates_to_catalog(self) -> None:
        """get_messages should delegate to catalog.get_messages."""

        class FakeProvider(BaseMessageProvider):
            @property
            def catalog(self) -> MessageCatalog:
                return MessageCatalog(
                    lang="fk",
                    lang_name="Fake",
                    messages={200: {InsultLevel.LIGHT: ["ok"]}},
                )

            @classmethod
            def lang_code(cls) -> str:
                return "fk"

        provider = FakeProvider()
        result = provider.get_messages(200, InsultLevel.LIGHT)
        assert result == ["ok"]
