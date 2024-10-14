import json
from datetime import datetime

from src.utils.emojis import extract_emojis


def valid_line(line):
    # Delete line breaks and spaces
    line = line.strip()

    # Validate JSON format
    if line.startswith('{') and line.endswith('}'):
        # Convert to object
        try:
            tweet = json.loads(line)
            return tweet
        except json.JSONDecodeError as e:
            print(f'Error decoding the line: {line.strip()} - {e}')


def tweet_generator(file_path):
    # Open file in read mode
    with open(file_path, 'r') as f:
        # Read each line
        for line in f:
            tweet = valid_line(line)

            # Save the date and username
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
            username = tweet['user']['username']

            # Use of yield to return data one by one
            yield tweet_date, username


def tweet_generator_emojis(file_path):
    """Generator to process each tweet and their quotedTweet."""
    with open(file_path, 'r') as f:
        # Read the file line by line
        for line in f:
            tweet = valid_line(line)

            # Process emojis from 'content'
            yield extract_emojis(tweet.get('content', ''))

            # Process emojis from 'content' in the 'quotedTweet' if it exists
            quoted_tweet = tweet.get('quotedTweet')
            if quoted_tweet:
                yield extract_emojis(quoted_tweet.get('content', ''))


def mention_generator(file_path):
    """Generator to process mentions of each tweet and their quotedTweet."""
    with open(file_path, 'r') as f:
        # Read the file line by line
        for line in f:
            tweet = valid_line(line)

            # Process mentions in 'mentionedUsers' from main tweet
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users is None:
                mentioned_users = []
            for user in mentioned_users:
                yield user['username']

            # Process mentions in 'mentionedUsers' from 'quotedTweet' if it exists
            quoted_tweet = tweet.get('quotedTweet')
            if quoted_tweet:
                quoted_mentioned_users = quoted_tweet.get('mentionedUsers', [])
                if quoted_mentioned_users is None:
                    quoted_mentioned_users = []
                for user in quoted_mentioned_users:
                    yield user['username']
