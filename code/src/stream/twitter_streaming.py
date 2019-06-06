import json
import boto3
import requests
from textblob import TextBlob
from ConfigParser import SafeConfigParser
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


# Create an S3 client
s3 = boto3.client('s3')
bucket = "image-bucket-266"

# Firehose delivery stream to stream tweets
fh = boto3.client('firehose')
deliverystream_name = "twitter-stream"
# Twitter Configuration keys
consumer_secret =  "k0lTtj6DTsPfUWtkXynpQalFkF79xyovixmS1W6hMMN0VGJtgW"
consumer_key = "XunErNB3P5XXRCx06KvzpgXkg"
access_token = "1121188546318962690-R2cFYRzVMneHAPqczhO66yms9wrsG1"
access_token_secret = "v98uvfWzP6Yk4kPgYIFNLzGtYxUeqLUJdjPyTHuvsd801"

# Twitter user
user = "Dummy69710367"

if __name__ == '__main__':

    try:

        oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
        twitter_stream = TwitterStream(auth = oauth, secure = True)
        tweets = twitter_stream.statuses.filter(track=user)
        print "Inside"
        for tweet in tweets:
            print tweet
            #print json.dumps(tweet, indent=2, sort_keys=True)
            #entities = tweet.get("entities")
            entities = tweet.get("extended_entities")
            print json.dumps(entities, indent=2, sort_keys=True)
            if (entities):
                print json.dumps(entities, indent=2, sort_keys=True)
                media_list = entities.get("media")
                if (media_list):
                    for media in media_list:
                        if (media.get("type", None) == "photo"):
                            #print json.dumps(media, indent=2, sort_keys=True)
                            twitter_data = {}
                            description = tweet.get("user").get("description")
                            loc = tweet.get("user").get("location")
                            text = tweet.get("text")
                            coords = tweet.get("coordinates")
                            geo = tweet.get("geo")
                            name = tweet.get("user").get("screen_name")
                            user_created = tweet.get("user").get("created_at")
                            followers = tweet.get("user").get("followers_count")
                            id_str = tweet.get("id_str")
                            created = tweet.get("created_at")
                            retweets = tweet.get("retweet_count")
                            bg_color = tweet.get("user").get("profile_background_color")
                            blob = TextBlob(text)
                            sent = blob.sentiment
                            image_url = media.get("media_url")

                            twitter_data['description'] = description
                            twitter_data['loc'] = loc
                            twitter_data['text'] = text
                            twitter_data['coords'] = coords
                            twitter_data['geo'] = geo
                            twitter_data['name'] = name
                            twitter_data['user_created'] = user_created
                            twitter_data['followers'] = followers
                            twitter_data['id_str'] = id_str
                            twitter_data['created'] = created
                            twitter_data['retweets'] = retweets
                            twitter_data['bg_color'] = bg_color
                            twitter_data['sent'] = sent
                            twitter_data['image_url'] = image_url

                            # Stream the content via Kinesis Firehose Deliver to S3
                            print("Sending to Kinesis")
                            print twitter_data
                            response = fh.put_record(
                                DeliveryStreamName=deliverystream_name,
                                Record = {'Data': json.dumps(twitter_data, indent = 4)}
                                )
    except Exception as e:
        print (e)