import os
import json

# Default config structure
DEFAULT_CONFIG = {
    "dataset_directory": None,  # Path to the local dataset directory
    "datasets": {}  # Custom dataset URLs, if any
}

CONFIG_FILE = "config.json"


def load_config(config_file=CONFIG_FILE):
    """
    Load the configuration file. If it doesn't exist, create one with defaults.
    """
    if not os.path.exists(config_file):
        print(f"Config file not found. Creating a new one at {config_file}.")
        save_config(DEFAULT_CONFIG, config_file)
        return DEFAULT_CONFIG

    try:
        with open(config_file, "r") as file:
            config = json.load(file)
            # Merge with default to ensure all keys are present
            return {**DEFAULT_CONFIG, **config}
    except json.JSONDecodeError:
        print(f"Error decoding {config_file}. Recreating it with defaults.")
        save_config(DEFAULT_CONFIG, config_file)
        return DEFAULT_CONFIG


def save_config(config, config_file=CONFIG_FILE):
    """
    Save the configuration to a file.
    """
    try:
        with open(config_file, "w") as file:
            json.dump(config, file, indent=4)
        print(f"Config saved to {config_file}.")
    except IOError as e:
        print(f"Failed to save config: {e}")


def update_config(updates, config_file=CONFIG_FILE):
    """
    Update specific keys in the configuration file.
    """
    config = load_config(config_file)
    config.update(updates)
    save_config(config, config_file)
