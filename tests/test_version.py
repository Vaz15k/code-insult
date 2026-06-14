"""
Tests for codeinsult.__version__ — package version.
"""

import codeinsult


class TestVersion:
    """Tests for the __version__ attribute."""

    def test_version_is_string(self) -> None:
        """__version__ should be a string."""
        assert isinstance(codeinsult.__version__, str)

    def test_version_follows_semver(self) -> None:
        """__version__ should follow the semver format (X.Y.Z)."""
        parts = codeinsult.__version__.split(".")
        assert len(parts) == 3
        for part in parts:
            assert part.isdigit(), f"Part '{part}' is not numeric"

    def test_version_is_accessible_from_package(self) -> None:
        """The version should be accessible as codeinsult.__version__."""
        version = codeinsult.__version__
        assert version is not None
        assert len(version) > 0
