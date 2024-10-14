from typing import List, Tuple
from datetime import datetime

from src.json_processing import process_json


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets_per_date = process_json(file_path)

    # List to save dates and total tweets per date
    date_tweet_sums = []
    # Dict to save users with more tweets per date
    top_users_by_date = {}

    # Calculate total tweets and find user with more tweets
    for date, users in tweets_per_date.items():
        total_tweets = sum(users.values())
        top_user = max(users.items(), key=lambda item: item[1])[0]
        date_tweet_sums.append((date, total_tweets))
        top_users_by_date[date] = top_user

    # Sort list by total tweets and save just top 10
    top_10_dates = sorted(date_tweet_sums, key=lambda x: x[1], reverse=True)[:10]

    # Use the date list and users dict to return the list
    return [(tweet_date, top_users_by_date[tweet_date]) for tweet_date, _ in top_10_dates]
