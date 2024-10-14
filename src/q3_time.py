from collections import Counter
from typing import List, Tuple

import orjson


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

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

            # Process mentions in 'mentionedUsers' from main tweet
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users is None:
                mentioned_users = []
            mention_counter.update(user['username'] for user in mentioned_users)

            # Process mentions in 'mentionedUsers' from 'quotedTweet' if it exists
            quoted_tweet = tweet.get('quotedTweet')
            if quoted_tweet:
                quoted_mentioned_users = quoted_tweet.get('mentionedUsers', [])
                if quoted_mentioned_users is None:
                    quoted_mentioned_users = []
                mention_counter.update(user['username'] for user in quoted_mentioned_users)

        # Obtain top 10 of more mentioned users
        return mention_counter.most_common(10)
