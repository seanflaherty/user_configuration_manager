# User Configuration Manager (`user_configuration_manager`)

> A robust Python library designed to handle, validate, and manage user configuration settings and application state seamlessly.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

`user_configuration_manager` provides a simple, structured interface for persisting and loading user preferences and configuration files (such as JSON, YAML, or INI) within Python applications. It abstracts file I/O operations and provides default settings fallback, validation, and safe updating mechanisms.

---

## ✨ Features

* **Centralized Configuration:** Manage key-value settings or nested configuration files with minimal boilerplate.
* **Default Settings Fallback:** Automatically set and restore default user settings when configurations are missing or corrupted.
* **Persistent Storage:** Seamlessly save changes back to disk.
* **Format Flexibility:** Easily handle common structured formats like JSON or YAML.
* **Cross-Platform Compatibility:** Handles pathing and configuration directory selection appropriately across OS environments.

---

## 🚀 Getting Started

### Prerequisites

* Python **3.8** or higher installed.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/seanflaherty/user_configuration_manager.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd user_configuration_manager
   ```

3. *(Optional)* Set up a virtual environment and install in editable mode:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

---

## 💡 Usage Example

Here is a basic example of initializing and managing user configurations:

```python
from config_manager import ConfigManager

# Define default configuration settings
DEFAULT_CONFIG = {
    "theme": "dark",
    "notifications": True,
    "max_connections": 5
}

# Initialize the manager with a target config file path
config = ConfigManager(filepath="user_settings.json", defaults=DEFAULT_CONFIG)

# Retrieve settings
current_theme = config.get("theme")
print(f"Current theme: {current_theme}")

# Update and persist a setting
config.set("theme", "light")
config.save()
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🛠️ Built With

* **Language:** [Python 3](https://www.python.org/)
* **Testing:** [pytest](https://docs.pytest.org/)
* **Focus:** Dictionary data structure.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.