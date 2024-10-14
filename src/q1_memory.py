import gc
import heapq
from typing import List, Tuple
from datetime import datetime

from src.json_processing import process_tweets


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    top_dates_heap = []
    tweets = process_tweets(file_path)

    # Process file in an incremental way and free memory whenever possible
    for date, user_data in tweets.items():
        # Total tweets by user
        total_tweets = sum(user_data.values())
        top_user = max(user_data, key=user_data.get)
        top_user_count = user_data[top_user]

        # Use heap
        heapq.heappush(top_dates_heap, (total_tweets, date, top_user, top_user_count))

        # Limit the heap to 10 elements
        if len(top_dates_heap) > 10:
            heapq.heappop(top_dates_heap)

        # Free memory manually
        del user_data
        gc.collect()

    # Convert the heap to sorted list
    top_dates_sorted = sorted(top_dates_heap, key=lambda x: x[0], reverse=True)

    return [(date, top_user) for _, date, top_user, _ in top_dates_sorted]
