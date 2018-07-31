import tweepy

def status_test():
    auth = tweepy.OAuthHandler("NQE7OU3yhqTe6HEvZ7ty2kTLh", "x8UH9ZRWOmqOd7C8Nvkf6XahzloyZ7QOKEj1EYj75j4dpydvvC")
    auth.set_access_token("946989804738134018-EykBrYBvsVh0BX374rvL4Xw0HflnDcB",
                          "lAZJqB0e6IVkkvdihABa0I9MJX3FsPou51lvkgMqzkoj7")
    api = tweepy.API(auth, proxy="127.0.0.1:1080")

    api.get_status()
if __name__ == '__main__':
    status_test()