top_dates_query = """
    with 
    total_by_date as (
      select DATE(date) fecha, count(*) total
      from challenge_data.tweets
      group by 1
      order by 2 desc
      limit 10
    ),
    user_date as (
      select DATE(date) fecha, u.username, count(*) user_tweets
      from challenge_data.tweets t
      join challenge_data.users u on t.user_id = u.id
      where DATE(date) in (select fecha from total_by_date)
      group by 1,2
      order by 3 desc
    )
    select fecha, username
    from (
    select *, sum(user_tweets) over (partition by fecha) total_date, row_number() over (partition by fecha order by user_tweets desc) rank_
    from user_date
    )
    where rank_ = 1
    order by total_date desc
"""
