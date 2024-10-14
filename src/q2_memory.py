from collections import Counter
from typing import List, Tuple

from src.utils.generators import tweet_generator_emojis


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    # Use generator to process tweets one by one
    for emoji_list in tweet_generator_emojis(file_path):
        for emoji_char in emoji_list:
            emoji_counter[emoji_char] += 1

    # Obtain top 10 of emojis
    return emoji_counter.most_common(10)
