"""Tests for the greeting application."""

from main import greet


def test_greet_uses_default_name() -> None:
    """The default greeting uses the name World."""
    assert greet() == "Hello, World!"


def test_greet_uses_provided_name() -> None:
    """The greeting includes the provided name."""
    assert greet("Alice") == "Hello, Alice!"
