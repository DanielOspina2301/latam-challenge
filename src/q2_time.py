from collections import Counter
from typing import List, Tuple

import orjson

from src.utils.emojis import extract_emojis


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()
    with open(file_path, 'r') as f:
        # Read the file line by line
        for line in f:
            # Fix and convert each line in a JSON object
            line = line.strip()
            if not line:
                # Ignore empty lines
                continue

            # Validate the object to process correctly
            if line.startswith('{') and line.endswith('}'):
                try:
                    tweet = orjson.loads(line)
                except orjson.JSONDecodeError as e:
                    print(f'Error decoding the line: {line.strip()} - {e}')

            # Extract emojis from 'content'
            content_emojis = extract_emojis(tweet.get('content', ''))
            emoji_counter.update(content_emojis)

            # Check if quotedTweet exists and extract emojis from their 'content'
            quoted_tweet = tweet.get('quotedTweet')
            if quoted_tweet:
                quoted_content_emojis = extract_emojis(quoted_tweet.get('content', ''))
                emoji_counter.update(quoted_content_emojis)

        # Obtain top 10 of emojis
        return emoji_counter.most_common(10)
