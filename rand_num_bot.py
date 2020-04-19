from datetime import datetime

import random
import praw
import re

bot_start_time = datetime.utcnow()

r = praw.Reddit("bot1")

subreddits = ["bots"]

regex = "\s*random_number_bot\s+(\d+)\s+(\d+)"

for subreddit in subreddits:
	for comment in r.subreddit(subreddit).stream.comments():
		comment_time = datetime.utcfromtimestamp(comment.created_utc)

		if comment_time >= bot_start_time:
			matches = re.findall(regex, comment.body)

			if matches:
				nums = list(map(lambda x: int(x), list(matches[0])))

				random_number = random.randint(min(nums), max(nums))

				comment.reply(str(random_number))