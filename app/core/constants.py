# Main constants for the application
# Each view has a title, tooltip, icon name, and otherwise the index is implied by the order in the dictionary
# The icon names are from the FontAwesome icon set using the qtawesome library

STATES = {
    "Splash": 0,
    "Create Project": 1,
    "Home": 2,
    "Results": 3
}

ACTIONS = {
    "Load Dataset": "fa.folder-open",
    "Preprocess Data": "fa.cogs",
    "Train Model": "fa.rocket",
    "Generate Text": "fa.file-text-o"
}

# Default dataset URLs
DEFAULT_DATASETS = {
    "shakespeare": "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt",
    "gadsby": "https://www.gutenberg.org/files/47367/47367-0.txt",
    "bible": "https://www.gutenberg.org/cache/epub/10/pg10.txt",
    "moby_dick": "https://www.gutenberg.org/files/2701/2701-0.txt",
    "alice": "https://www.gutenberg.org/files/11/11-0.txt",
    "poe": "https://www.gutenberg.org/files/2147/2147-0.txt",
    "war_and_peace": "https://www.gutenberg.org/files/2600/2600-0.txt",
    "iliad": "https://www.gutenberg.org/files/6130/6130-0.txt",
    "grimm": "https://www.gutenberg.org/files/2591/2591-0.txt"
}
