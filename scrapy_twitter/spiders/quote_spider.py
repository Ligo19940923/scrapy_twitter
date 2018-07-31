import scrapy
import requests
import base64

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [

            'https://twitter.com/realDonaldTrump',
            # 'https://twitter.com/Keshavbeniwal2'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)







    def parse(self, response):
        # test_tweet = response.xpath('//*[@id="stream-item-tweet-1000645217727336453"]//div[@class="js-tweet-text-container"]/p//text()').extract()
        # print(test_tweet)



        # text = response.xpath('//div[@class="stream"]//li//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()').extract()
        # #print(text)
        # id = response.xpath('//div[@class="stream"]//li/@data-item-id').extract()
        # #print(id)

        timeline = response.xpath('//div[@class="stream"]//li[@class="js-stream-item stream-item stream-item\n"]')
        #
        # file = open("Trump.txt","a",encoding='utf8')
        # for tweet in enumerate(timeline):
        #     tweet_string = ""
        #     tweet_id = tweet[1].xpath('@data-item-id').extract()
        #     user_name = tweet[1].xpath('div/@data-name').extract()
        #     user_screen_name = tweet[1].xpath('div/@data-screen-name').extract()
        #     time = tweet[1].xpath('div//small[@class="time"]/a/@title').extract()
        #     tweet_content = tweet[1].xpath('div//div[@class="js-tweet-text-container"]/p//text()').extract()
        #     for item in tweet_content:
        #         tweet_string = tweet_string + item
            # retweeted_tweet_flag = tweet[1].xpath('div//div[@class="QuoteTweet-container"]')
        #
        #
        #
        #     print(user_name[0]+"(@"+user_screen_name[0]+") "+time[0])
        #     print(tweet_string)
        #     file.write(tweet_string+'\n')
        # file.close()
        #
        #     if (retweeted_tweet_flag):
        #         retweeted_tweet = retweeted_tweet_flag.xpath('div//div[@class="tweet-content"]/div/div[2]//text()').extract()
        #         print(retweeted_tweet[0])
        #     print("\n")




        #follow = response.xpath('//div[@id="page-outer"]//text()')

        #test_cookie[cookie[0]]=cookie[1]v1_3YfkWPTTlqwsUe561l2wvw==
        new_ck = [{'domain': '.twitter.com', 'expiry': 1526550495.219523, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'f4a00d70952e93e11405dbc2d9b83742'}, {'domain': '.twitter.com', 'expiry': 1589600894.389054, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A152652889509819105'}, {'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.twitter.com', 'expiry': 1589600894.388925, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_ikoVJRd0nD9aoKyWUSHknA=="'}, {'domain': '.twitter.com', 'expiry': 1589600910, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1285794099.1526528904'}, {'domain': '.twitter.com', 'expiry': 1526528963, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1841888904.650549, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=946989804738134018"'}, {'domain': '.twitter.com', 'expiry': 1526615310, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.3890153.1526528904'}, {'domain': '.twitter.com', 'expiry': 1841888904.650234, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBERAAA="'}, {'domain': '.twitter.com', 'expiry': 1573789704.650307, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'dJ3Q3cwaMdD7xjFuqvD5LW7YhXbcn2H0FqJGmTv9'}, {'domain': '.twitter.com', 'expiry': 1841888904.650376, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCHJrNmxjAToMY3NyZl9p%250AZCIlOGJkNTRhMWVlZTRjOGZmMTkyZjk0Mjk0ZmFhNjdkN2Y6B2lkIiUzZmI5%250ANmIxN2Y1ZDE4ZDczN2RhMzlhMTk3NTU5YmRlZDoJdXNlcmwrCQJAVcU1YiQN--471eef6825ed73008713bc29a7877924e8cc7819'}, {'domain': '.twitter.com', 'expiry': 1841888904.650627, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': '20275e0dfec8df43ba516293ca74d004812b28a7'}, {'domain': '.twitter.com', 'expiry': 1557978504.892401, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1558064904.89253, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]


        # yield scrapy.Request(url='https://twitter.com/lijianzhong135/following', callback=self.get_fan, cookies=new_ck)

        yield scrapy.Request(url='https://twitter.com/search?f=news&vertical=default&q=5G&src=typd', callback=self.parse_search, cookies=new_ck)



    def get_fan(self,response):
        followlist = response.xpath('//*[@id="page-container"]/div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div')

        followers = followlist.xpath('div//b[@class="u-linkComplex-target"]/text()').extract()
        flo_list = []
        for flo in enumerate(followlist):
            flo_name = flo[1].xpath('div//div[@class="ProfileNameTruncated account-group"]//a/text()').extract()
            flo_screen_name = flo[1].xpath('div//span[@class="ProfileCard-screenname"]//b[@class="u-linkComplex-target"]/text()').extract()
            flo_list.append(flo_screen_name)
            print(flo_name[0]+"(@"+flo_screen_name[0]+")")

        for name in flo_list:
            yield scrapy.Request(url='https://twitter.com/' + name[0], callback=self.follower_timeline)
        #print(followlist)

    def follower_timeline(self,response):

        text = response.xpath('//div[@class="stream"]//li//p[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()').extract()


        timeline = response.xpath('//div[@class="stream"]//li[@class="js-stream-item stream-item stream-item\n"]')

        for tweet in enumerate(timeline):
            tweet_string = ""
            tweet_id = tweet[1].xpath('@data-item-id').extract()
            user_name = tweet[1].xpath('div/@data-name').extract()
            user_screen_name = tweet[1].xpath('div/@data-screen-name').extract()
            time = tweet[1].xpath('div//small[@class="time"]/a/@title').extract()
            tweet_content = tweet[1].xpath('div//div[@class="js-tweet-text-container"]/p//text()').extract()
            for item in tweet_content:
                tweet_string = tweet_string + item
            retweeted_tweet_flag = tweet[1].xpath('div//div[@class="QuoteTweet-container"]')



            print(user_name[0]+"(@"+user_screen_name[0]+") "+time[0])
            print(tweet_string)

            if (retweeted_tweet_flag):
                retweeted_tweet = retweeted_tweet_flag.xpath('div//div[@class="tweet-content"]/div/div[2]//text()').extract()
                print(retweeted_tweet[0])
            print("\n")

    def parse_search(self,response):
        timeline = response.body
        f = open('search12.html', 'wb')
        f.write(timeline)
        f.close()
        # for tweet in enumerate(timeline):
        #     tweet_id = tweet[1].xpath('@data-item-id').extract()
        #     user_name = tweet[1].xpath('div/@data-name').extract()
        #     user_screen_name = tweet[1].xpath('div/@data-screen-name').extract()
        #     time = tweet[1].xpath('div//small[@class="time"]/a/@title').extract()
        #     tweet_content = tweet[1].xpath('div//div[@class="js-tweet-text-container"]/p/text()').extract()
        #     retweeted_tweet_flag = tweet[1].xpath('div//div[@class="QuoteTweet-container"]')
        #
        #
        #
        #     print(user_name[0]+"(@"+user_screen_name[0]+") "+time[0])
        #     print(tweet_content[0])
        #
        #     if (retweeted_tweet_flag):
        #         retweeted_tweet = retweeted_tweet_flag.xpath('div//div[@class="tweet-content"]/div/div[2]//text()').extract()
        #         print(retweeted_tweet[0])
        #     print("\n")







# 这是下拉滚动条刷新的请求
# https://twitter.com/i/profiles/show/ForbesTech/timeline/tweets?include_available_features=1&include_entities=1&max_position=1001583539169603584&reset_error_state=false
