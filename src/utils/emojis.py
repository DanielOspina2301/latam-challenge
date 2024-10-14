import emoji


def extract_emojis(text):
    """Extract emojis from text."""
    # Use emoji package to find emojis
    return [char for char in text if char in emoji.EMOJI_DATA]
