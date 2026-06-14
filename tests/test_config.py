"""
Tests for codeinsult.config — InsultLevel enum.
"""

import pytest

from codeinsult.config import InsultLevel


class TestInsultLevelFromStr:
    """Tests for InsultLevel.from_str()."""

    def test_light_string_returns_light_level(self) -> None:
        """'light' should return InsultLevel.LIGHT."""
        result = InsultLevel.from_str("light")
        assert result is InsultLevel.LIGHT

    def test_medium_string_returns_medium_level(self) -> None:
        """'medium' should return InsultLevel.MEDIUM."""
        result = InsultLevel.from_str("medium")
        assert result is InsultLevel.MEDIUM

    def test_heavy_string_returns_heavy_level(self) -> None:
        """'heavy' should return InsultLevel.HEAVY."""
        result = InsultLevel.from_str("heavy")
        assert result is InsultLevel.HEAVY

    def test_uppercase_string_is_normalized(self) -> None:
        """Uppercase strings should be normalized to lowercase."""
        result = InsultLevel.from_str("LIGHT")
        assert result is InsultLevel.LIGHT

    def test_mixed_case_string_is_normalized(self) -> None:
        """Mixed-case strings should be normalized."""
        result = InsultLevel.from_str("HeAVy")
        assert result is InsultLevel.HEAVY

    def test_none_returns_none(self) -> None:
        """None should return None."""
        result = InsultLevel.from_str(None)
        assert result is None

    def test_invalid_string_raises_value_error(self) -> None:
        """Invalid string should raise ValueError."""
        with pytest.raises(ValueError, match="Nível"):
            InsultLevel.from_str("extreme")

    def test_empty_string_raises_value_error(self) -> None:
        """Empty string should raise ValueError."""
        with pytest.raises(ValueError):
            InsultLevel.from_str("")


class TestInsultLevelValues:
    """Tests for InsultLevel enum values."""

    def test_light_value_is_light_string(self) -> None:
        """InsultLevel.LIGHT.value should be 'light'."""
        assert InsultLevel.LIGHT.value == "light"

    def test_medium_value_is_medium_string(self) -> None:
        """InsultLevel.MEDIUM.value should be 'medium'."""
        assert InsultLevel.MEDIUM.value == "medium"

    def test_heavy_value_is_heavy_string(self) -> None:
        """InsultLevel.HEAVY.value should be 'heavy'."""
        assert InsultLevel.HEAVY.value == "heavy"

    def test_enum_has_three_members(self) -> None:
        """There should be exactly 3 severity levels."""
        members = list(InsultLevel)
        assert len(members) == 3
