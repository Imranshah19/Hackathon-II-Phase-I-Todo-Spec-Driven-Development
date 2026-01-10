"""Unit tests for validation functions."""

import pytest
from src.utils.validators import validate_title, validate_task_id, MAX_TITLE_LENGTH


class TestValidateTitle:
    """Tests for validate_title function."""

    def test_valid_title(self):
        """Valid title should pass validation."""
        is_valid, error = validate_title("Buy groceries")

        assert is_valid is True
        assert error == ""

    def test_empty_title(self):
        """Empty title should fail validation."""
        is_valid, error = validate_title("")

        assert is_valid is False
        assert "cannot be empty" in error

    def test_whitespace_only_title(self):
        """Whitespace-only title should fail validation."""
        is_valid, error = validate_title("   ")

        assert is_valid is False
        assert "cannot be empty" in error

    def test_title_at_max_length(self):
        """Title at exactly max length should pass."""
        title = "x" * MAX_TITLE_LENGTH
        is_valid, error = validate_title(title)

        assert is_valid is True
        assert error == ""

    def test_title_exceeds_max_length(self):
        """Title exceeding max length should fail."""
        title = "x" * (MAX_TITLE_LENGTH + 1)
        is_valid, error = validate_title(title)

        assert is_valid is False
        assert "exceeds maximum length" in error
        assert str(MAX_TITLE_LENGTH) in error

    def test_title_with_special_characters(self):
        """Title with special characters should pass."""
        is_valid, error = validate_title("Buy groceries! @store #urgent")

        assert is_valid is True
        assert error == ""

    def test_title_with_unicode(self):
        """Title with unicode characters should pass."""
        is_valid, error = validate_title("买杂货 🛒")

        assert is_valid is True
        assert error == ""


class TestValidateTaskId:
    """Tests for validate_task_id function."""

    def test_valid_task_id(self):
        """Valid numeric ID should pass."""
        is_valid, task_id, error = validate_task_id("1")

        assert is_valid is True
        assert task_id == 1
        assert error == ""

    def test_valid_large_id(self):
        """Large numeric ID should pass."""
        is_valid, task_id, error = validate_task_id("999")

        assert is_valid is True
        assert task_id == 999
        assert error == ""

    def test_non_numeric_id(self):
        """Non-numeric input should fail."""
        is_valid, task_id, error = validate_task_id("abc")

        assert is_valid is False
        assert task_id is None
        assert "must be a number" in error

    def test_zero_id(self):
        """Zero should fail (must be positive)."""
        is_valid, task_id, error = validate_task_id("0")

        assert is_valid is False
        assert task_id is None
        assert "must be a positive number" in error

    def test_negative_id(self):
        """Negative number should fail."""
        is_valid, task_id, error = validate_task_id("-1")

        assert is_valid is False
        assert task_id is None
        assert "must be a positive number" in error

    def test_float_id(self):
        """Float string should fail."""
        is_valid, task_id, error = validate_task_id("1.5")

        assert is_valid is False
        assert task_id is None
        assert "must be a number" in error

    def test_empty_id(self):
        """Empty string should fail."""
        is_valid, task_id, error = validate_task_id("")

        assert is_valid is False
        assert task_id is None
        assert "must be a number" in error
