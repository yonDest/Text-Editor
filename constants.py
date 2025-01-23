from pathlib import Path

# File paths
CONFIG_DIR = Path.home() / ".notes-app"
CONFIG_FILE = CONFIG_DIR / "config.json"

# Default settings
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 12
DEFAULT_THEME = "light"

# Keyboard shortcuts
SHORTCUTS = {
    "new": "<Control-n>",
    "open": "<Control-o>",
    "save": "<Control-s>",
    "save_as": "<Control-Shift-s>",
    "quit": "<Control-q>",
} 