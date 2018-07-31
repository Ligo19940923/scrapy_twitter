import pymongo as pm
from bson.objectid import ObjectId
def main():
    client = pm.MongoClient()
    db = client.twitter
    tweets = db.twitter_data1
    file = open("extradata_Liu.txt","a",encoding='utf-8')
    all_tweets = tweets.find()
    # {"_id": {"$gte": ObjectId("5b1562000000000000000000"), "$lte": ObjectId("5b1aa8000000000000000000")}}
    count = 0
    for tweet in all_tweets:
        count = count + 1
        id = tweet['id_str']
        created_at = tweet['created_at']
        # user_name = tweet['user']['name']
        # user_screenname = tweet['user']['screen_name']
        # user = user_name+"(@"+user_screenname+")"
        # url = "https://twitter.com/" + str(user_screenname) + "/status/" + str(id)
        # tags = []
        if('extended_tweet' in tweet.keys()):
            string = tweet['extended_tweet']['full_text'].replace('\n','')
            hashtags = tweet['entities']['hashtags']

        elif('retweeted_status' in tweet.keys()):
            if('extended_tweet' in tweet['retweeted_status'].keys()):
                string = tweet['retweeted_status']['extended_tweet']['full_text'].replace('\n','')
            else:
                string = tweet['retweeted_status']['text'].replace('\n','')
            hashtags = tweet['retweeted_status']['entities']['hashtags']
        else:
            string = tweet['text'].replace('\n','')


        string = string.replace('\r','')
        string_length = len(string)

        # if(len(hashtags) != 0):
        #     for item in hashtags:
        #         tags.append(item['text'])
        time = str(created_at).replace('+0000','CDT')

        file.write(string + "\n")

        # file.write(str(tweet['user']['followers_count']) +"\n")


    file.close()



if __name__ == '__main__':
    main()