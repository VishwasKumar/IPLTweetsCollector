
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "501864645-WZ0ivAcJpujvJqo0Q9Yh4YeQtimywoJBpZIqQL0O"
access_token_secret = "LLQFJMCtB7ZWIZR621aDeXOicInaMk31oEphT90mSMmsY"
consumer_key = "Ku7IdkkLxzyePUMamqpCeCwgY"
consumer_secret = "g0iCdW5ShVnuzaokFC4QEm7jjyMb6NX2723qXpcjbL3y4uozzi"



class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#ipl2016'])