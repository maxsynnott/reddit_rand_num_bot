from datetime import datetime

import random
import praw
import re

bot_start_time = datetime.utcnow()

# touch a praw.ini file in current directory and configure correctly under [bot1]
r = praw.Reddit("bot1")

# all subreddits that you want the bot to watch
subreddits = ["bots"]

# matches strings such as "random_number_bot 1 10"
regex = "\s*random_number_bot\s+(\d+)\s+(\d+)"

for subreddit in subreddits:
	for comment in r.subreddit(subreddit).stream.comments():
		comment_time = datetime.utcfromtimestamp(comment.created_utc)

		# only replys to comments created after the bot was started
		# the .stream will only show each comment once so the bot should never reply twice
		if comment_time >= bot_start_time:
			matches = re.findall(regex, comment.body)

			if matches:
				# grab the two numbers matched and reply with the random number
				nums = list(map(lambda x: int(x), list(matches[0])))

				min_num = min(nums)
				max_num = max(nums)

				random_number = random.randint(min_num, max_num)

				comment.reply(f'A random number between {min_num} and {max_num} is: {str(random_number)}')
