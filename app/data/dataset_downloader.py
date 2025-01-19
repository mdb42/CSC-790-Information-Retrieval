import os
from app.core.config import load_config, update_config
from app.core.utils import ensure_directory_exists
from app.core.constants import DEFAULT_DATASETS
import requests


def setup_datasets(config_file="config.json"):
    """
    Ensures datasets are set up, downloads if not already available.
    """
    config = load_config(config_file)
    dataset_dir = config["dataset_directory"]

    if not dataset_dir or not os.path.isdir(dataset_dir):
        print("Dataset directory not configured. Please select a valid directory.")
        return

    datasets = config.get("datasets", DEFAULT_DATASETS)
    ensure_directory_exists(dataset_dir)

    for name, url in datasets.items():
        dataset_path = os.path.join(dataset_dir, f"{name}.txt")
        if not os.path.exists(dataset_path):
            print(f"Downloading {name} from {url}...")
            download_dataset(url, dataset_path)
        else:
            print(f"{name} is already downloaded.")

    # Save the updated dataset list to the config
    update_config({"datasets": datasets}, config_file)


def download_dataset(url, save_path):
    """
    Downloads a dataset from a URL and saves it to a local path.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded and saved to {save_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")
