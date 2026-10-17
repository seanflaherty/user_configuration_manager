"""Tests for the various methods in user_configuration_manager.py."""
import pytest
from src.user_configuration_manager import (
    add_setting,
    update_setting,
    delete_setting,
    view_settings,
)  # Assuming your code is in settings_module.py


@pytest.fixture
def sample_settings():
    """Provides a fresh dictionary for each test."""
    return {"theme": "dark"}

def test_add_setting_success(sample_settings):
    """Test adding a new setting successfully."""
    result = add_setting(sample_settings, ("notifications", "enabled"))

    assert result == "Setting 'notifications' added with value 'enabled' successfully!"
    assert sample_settings["notifications"] == "enabled"
    # Check case-insensitivity conversion
    assert "notifications" in sample_settings

def test_add_setting_duplicate(sample_settings):
    """Test trying to add a setting that already exists."""
    # 'theme' already exists in the fixture
    result = add_setting(sample_settings, ("theme", "light"))

    assert (
        result
        == "Setting 'theme' already exists! Cannot add a new setting with this name."
    )
    # Ensure value wasn't overwritten
    assert sample_settings["theme"] == "dark"

def test_update_setting_success(sample_settings):
    """Test updating an existing setting successfully."""
    result = update_setting(sample_settings, ("theme", "light"))

    assert result == "Setting 'theme' updated to 'light' successfully!"
    assert sample_settings["theme"] == "light"

def test_update_setting_non_existent(sample_settings):
    """Test trying to update a setting that doesn't exist."""
    result = update_setting(sample_settings, ("volume", "high"))

    assert (
        result
        == "Setting 'volume' does not exist! Cannot update a non-existing setting."
    )
    assert "volume" not in sample_settings

def test_delete_setting_success(sample_settings):
    """Test deleting an existing setting successfully."""
    result = delete_setting(sample_settings, "theme")

    assert result == "Setting 'theme' deleted successfully!"
    assert "theme" not in sample_settings
    assert len(sample_settings) == 0

def test_delete_setting_not_found(sample_settings):
    """Test trying to delete a setting that doesn't exist."""
    result = delete_setting(sample_settings, "nonexistent")

    assert result == "Setting not found!"

def test_view_settings_populated(sample_settings):
    """Test viewing a populated settings dictionary."""
    output = view_settings(sample_settings)

    assert "Current User Settings:" in output
    assert "Theme: dark" in output  # Note the key capitalization

def test_view_settings_empty():
    """Test viewing an empty settings dictionary."""
    empty_dict = {}
    output = view_settings(empty_dict)

    assert output == "No settings available."
