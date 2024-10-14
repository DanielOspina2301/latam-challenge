from collections import defaultdict
from datetime import datetime

from orjson import orjson

from src.utils.generators import tweet_generator


def process_json(file_path):
    tweets_per_date = defaultdict(lambda: defaultdict(int))
    # Open the file in read mode
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

                # Obtain date and username of each tweet
                tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date()
                username = tweet['user']['username']

                # Add to the count of that date and user
                tweets_per_date[tweet_date][username] += 1

    return tweets_per_date


def process_tweets(file_path):
    # Dict to count tweets by date and user
    tweets_per_date = defaultdict(lambda: defaultdict(int))

    # use generator to process each tweet
    for tweet_date, username in tweet_generator(file_path):
        # Add to dict
        tweets_per_date[tweet_date][username] += 1

    return tweets_per_date
