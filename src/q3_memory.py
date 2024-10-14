from collections import Counter
from typing import List, Tuple

from src.utils.generators import mention_generator


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    # Use generator to process mentions
    for username in mention_generator(file_path):
        mention_counter[username] += 1

    # Obtain top 10 of more mentioned users
    return mention_counter.most_common(10)
