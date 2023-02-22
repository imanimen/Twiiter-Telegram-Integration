import tweepy
import telegram


# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Telegram Bot API credentials
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHANNEL_ID'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get your latest tweets
tweets = api.user_timeline(count=5)

# Initialize Telegram bot
bot = telegram.Bot(token=bot_token)

# Send your latest tweets to your Telegram channel
for tweet in tweets:
    message = f'{tweet.author.name} (@{tweet.author.screen_name}):\n{tweet.text}'
    bot.send_message(chat_id=chat_id, text=message)
