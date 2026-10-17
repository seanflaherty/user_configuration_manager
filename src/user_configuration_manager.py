"""A simple settings management system using
 a dictionary to store configuration names and values."""
def add_setting(settings: dict, new_setting: dict) -> str:
    """Adds a setting to the dictionary."""
    key, value = new_setting[0].lower(), new_setting[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, new_setting: dict) -> str:
    """Update the value of an existing setting."""
    key, value = new_setting[0].lower(), new_setting[1].lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings: dict, key: str) -> str:
    """Deletes a configuration name and value."""
    key = key.lower()
    if key not in settings:
        return "Setting not found!"

    del settings[key]

    return f"Setting '{key}' deleted successfully!"


def view_settings(settings: dict) -> str:
    """Returns a readable text representation of all current settings."""

    if not settings:
        return "No settings available."

    formatted_settings = "Current User Settings:\n"
    for key, value in settings.items():
        formatted_settings += f"{key.capitalize()}: {value}\n"

    return formatted_settings

