import os
import json
from pathlib import Path

def ensure_directory_exists(directory_path):
    """
    Ensures that a directory exists. Creates it if it does not exist.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
    except Exception as e:
        print(f"Error ensuring directory exists: {e}")

def read_json_file(file_path):
    """
    Reads a JSON file and returns the data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return {}

def write_json_file(file_path, data):
    """
    Writes data to a JSON file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error writing JSON to {file_path}: {e}")

def get_dataset_directory(config_file="config.json"):
    """
    Reads the dataset directory from the config file. Prompts the user to set one if not present.
    """
    config = read_json_file(config_file)
    dataset_dir = config.get("dataset_directory")
    
    if dataset_dir and os.path.isdir(dataset_dir):
        return dataset_dir
    else:
        print("Dataset directory not found. Please set a valid directory.")
        return None

def update_config(config_file="config.json", **kwargs):
    """
    Updates the configuration file with the provided keyword arguments.
    """
    config = read_json_file(config_file)
    config.update(kwargs)
    write_json_file(config_file, config)

def human_readable_size(size_in_bytes):
    """
    Converts a file size in bytes to a human-readable string.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"
