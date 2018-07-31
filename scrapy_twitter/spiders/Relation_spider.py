import scrapy
import sys
import tweepy
import time
class QuotesSpider(scrapy.Spider):
    name = "relation"

    def start_requests(self):
        urls = [

            'https://twitter.com/lijianzhong135',
            # 'https://twitter.com/Keshavbeniwal2'
        ]
        # new_ck = [{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593163116.007996, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_5sPZC9AKEP63pS81qtjFbA=="'}, {'domain': '.twitter.com', 'expiry': 1845451123, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530112716.888748, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'bbcbd7a0dfba3cd19893313d04906a87'}, {'domain': '.twitter.com', 'expiry': 1593163116.008242, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153009111625535430'}, {'domain': '.twitter.com', 'expiry': 1593163120, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746318223.1530091121'}, {'domain': '.twitter.com', 'expiry': 1530091180, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845451122.826011, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530177520, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1855516644.1530091121'}, {'domain': '.twitter.com', 'expiry': 1845451122.825764, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577351922.825801, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'BV70DdKxwFi9hI2qi38hAGejFVwltKLrpRCzaC84'}, {'domain': '.twitter.com', 'expiry': 1845451122.825836, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAGaiUBkAToMY3NyZl9p%250AZCIlMGY4ZTFiYzNmN2ZkMGM5NDQwMmE1NzJkYzM2ZjZmODM6B2lkIiUyMzRk%250AZTNkZDk1YjlhNjZlZjQ4MzY3ZDA0Nzc1YzhiNToJdXNlcmwrCQLQVIfs3eUN--b4094c5eb229e5f3123d711db3b28b6f77c5b705'}, {'domain': '.twitter.com', 'expiry': 1845451122.826049, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ba9113d4621da9bebab2060bcadc69f09643d732'}, {'domain': '.twitter.com', 'expiry': 1561540723.064481, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561627123.064564, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]

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
        count = 0
        for tweet in enumerate(timeline):
            count = count + 1
        follow_number = response.xpath('//*[@id="page-container"]/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[2]/a/span[3]/text()').extract()
        print(follow_number)
        #     tweet_string = ""
        #     tweet_id = tweet[1].xpath('@data-item-id').extract()
        #     user_name = tweet[1].xpath('div/@data-name').extract()
        #     user_screen_name = tweet[1].xpath('div/@data-screen-name').extract()
        #     time = tweet[1].xpath('div//small[@class="time"]/a/@title').extract()
        #     tweet_content = tweet[1].xpath('div//div[@class="js-tweet-text-container"]/p//text()').extract()
        #     for item in tweet_content:
        #         tweet_string = tweet_string + item
        #     retweeted_tweet_flag = tweet[1].xpath('div//div[@class="QuoteTweet-container"]')
        #
        #
        #
        #     print(user_name[0]+"(@"+user_screen_name[0]+") "+time[0])
        #     print(tweet_string)
        #
        #     if (retweeted_tweet_flag):
        #         retweeted_tweet = retweeted_tweet_flag.xpath('div//div[@class="tweet-content"]/div/div[2]//text()').extract()
        #         print(retweeted_tweet[0])
        #     print("\n")




        #follow = response.xpath('//div[@id="page-outer"]//text()')

        #test_cookie[cookie[0]]=cookie[1]v1_3YfkWPTTlqwsUe561l2wvw==
        print(count)

        new_ck =[{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593163116.007996, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_5sPZC9AKEP63pS81qtjFbA=="'}, {'domain': '.twitter.com', 'expiry': 1845451123, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530112716.888748, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'bbcbd7a0dfba3cd19893313d04906a87'}, {'domain': '.twitter.com', 'expiry': 1593163116.008242, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153009111625535430'}, {'domain': '.twitter.com', 'expiry': 1593163120, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746318223.1530091121'}, {'domain': '.twitter.com', 'expiry': 1530091180, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845451122.826011, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530177520, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1855516644.1530091121'}, {'domain': '.twitter.com', 'expiry': 1845451122.825764, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577351922.825801, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'BV70DdKxwFi9hI2qi38hAGejFVwltKLrpRCzaC84'}, {'domain': '.twitter.com', 'expiry': 1845451122.825836, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAGaiUBkAToMY3NyZl9p%250AZCIlMGY4ZTFiYzNmN2ZkMGM5NDQwMmE1NzJkYzM2ZjZmODM6B2lkIiUyMzRk%250AZTNkZDk1YjlhNjZlZjQ4MzY3ZDA0Nzc1YzhiNToJdXNlcmwrCQLQVIfs3eUN--b4094c5eb229e5f3123d711db3b28b6f77c5b705'}, {'domain': '.twitter.com', 'expiry': 1845451122.826049, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ba9113d4621da9bebab2060bcadc69f09643d732'}, {'domain': '.twitter.com', 'expiry': 1561540723.064481, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561627123.064564, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]
        user_name = [
                     'BAESystemsplc',
                     'LockheedMartin',
                     'northropgrumman',
                     'GDMS',
                     'Boeing',
                     'USMilitaryForum',
                     'DeptofDefense',
                     'USNavy',
                     'usairforce',
                     'USArmy',
                     'USMC',
                     'USCommandCyber',
                     'AustralianArmy',
                     'USNationalGuard',
                     'ArmyMediaCommSW/following'
                     ]
        for name in user_name:
            yield scrapy.Request(url='https://twitter.com/'+name+'/following',meta={'level': 1, 'user': name}, callback=self.get_fan2)
        # yield scrapy.Request(url='https://twitter.com/realDonaldTrump/following',meta={'level':1, 'user':'realDonaldTrump'}, callback=self.get_fan2)#, cookies=new_ck)

        # yield scrapy.Request(url='https://twitter.com/search?q=artifical&src=typd', callback=self.parse_search, cookies=new_ck)



    def get_fan(self,response):

        following = response.xpath('//*[@id="page-container"]/div[4]/div/div/div[2]/div/div[2]/div[2]/div[2]/div')

        level = response.meta['level']
        user = response.meta['user']
        file = open("crawlerfollowing_test.txt", "a",encoding="utf8")
        if level == 4 :
            sys.exit(0)
        flo_list = []
        count = 0
        for followlist in enumerate(following):
            follow_group = followlist[1].xpath('div')
            for flo in enumerate(follow_group):
                flo_name = flo[1].xpath('div//div[@class="ProfileNameTruncated account-group"]//a/text()').extract()
                flo_screen_name = flo[1].xpath('div//span[@class="ProfileCard-screenname"]//b[@class="u-linkComplex-target"]/text()').extract()
                flo_list.append(flo_screen_name[0])
                print(flo_name[0] + "(@" + flo_screen_name[0] + ")")
                file.write(user + '\t' + flo_screen_name[0]+'\n')
                count = count + 1
        print(count)
        file.close()
        level = level + 1
        print('level:',level)
        cookie = [{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593163116.007996, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_5sPZC9AKEP63pS81qtjFbA=="'}, {'domain': '.twitter.com', 'expiry': 1845451123, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530112716.888748, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'bbcbd7a0dfba3cd19893313d04906a87'}, {'domain': '.twitter.com', 'expiry': 1593163116.008242, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153009111625535430'}, {'domain': '.twitter.com', 'expiry': 1593163120, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746318223.1530091121'}, {'domain': '.twitter.com', 'expiry': 1530091180, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845451122.826011, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530177520, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1855516644.1530091121'}, {'domain': '.twitter.com', 'expiry': 1845451122.825764, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577351922.825801, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'BV70DdKxwFi9hI2qi38hAGejFVwltKLrpRCzaC84'}, {'domain': '.twitter.com', 'expiry': 1845451122.825836, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAGaiUBkAToMY3NyZl9p%250AZCIlMGY4ZTFiYzNmN2ZkMGM5NDQwMmE1NzJkYzM2ZjZmODM6B2lkIiUyMzRk%250AZTNkZDk1YjlhNjZlZjQ4MzY3ZDA0Nzc1YzhiNToJdXNlcmwrCQLQVIfs3eUN--b4094c5eb229e5f3123d711db3b28b6f77c5b705'}, {'domain': '.twitter.com', 'expiry': 1845451122.826049, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ba9113d4621da9bebab2060bcadc69f09643d732'}, {'domain': '.twitter.com', 'expiry': 1561540723.064481, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561627123.064564, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]
        for i in range(len(flo_list)):
            yield scrapy.Request(url='https://twitter.com/'+flo_list[i]+'/following', meta={'level':level,'user':flo_list[i]}, callback=self.get_fan2)#, cookies=cookie)
        # for name in flo_list:
        #     yield scrapy.Request(url='https://twitter.com/' + name[0], callback=self.follower_timeline)
        #print(followlist)

    def get_fan2(self,response):
        auth = tweepy.OAuthHandler("NQE7OU3yhqTe6HEvZ7ty2kTLh", "x8UH9ZRWOmqOd7C8Nvkf6XahzloyZ7QOKEj1EYj75j4dpydvvC")
        auth.set_access_token("946989804738134018-EykBrYBvsVh0BX374rvL4Xw0HflnDcB",
                              "lAZJqB0e6IVkkvdihABa0I9MJX3FsPou51lvkgMqzkoj7")
        api = tweepy.API(auth, proxy="127.0.0.1:1080")
        following = response.xpath('//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div')
        level = response.meta['level']
        user = response.meta['user']
        file = open("Army_Following.txt","a")
        count = 0
        flo_list = []
        if level ==1:
            member = 5
        elif level == 2:
            member = 3
        elif level == 3:
            member = 3
        elif level == 4:
            exit(0)

        user_dict = {}

        for followlist in enumerate(following):
            follow_group = followlist[1].xpath('div')
            for flo in enumerate(follow_group):
                flo_name = flo[1].xpath('div//div[@class="ProfileNameTruncated account-group"]//a/text()').extract()
                flo_screen_name = flo[1].xpath(
                    'div//span[@class="ProfileCard-screenname"]//b[@class="u-linkComplex-target"]/text()').extract()

                user_api = api.get_user(flo_screen_name[0])
                following_count = user_api.followers_count
                user_dict[flo_screen_name[0]]=following_count
                time.sleep(2)
        user_list = sorted(user_dict, key= lambda x:user_dict[x],reverse=True)
        for i in range(member):
            selected_user = user_list[i]
            flo_list.append(selected_user)
            print(user_list[i])
            # tweets = api.user_timeline(user_list[i], count=tweet_count)
            # file3 = open("user_timeline.txt", "a",encoding="utf8")
            # for t in tweets:
            #     text = t.text.replace('\n', '')
            #     created_at = t.created_at
            #     id = t.id
            #     file3.write(user_list[i] + '\t' + str(id) + '\t' + str(created_at) + '\t' + text + '\n')
            #
            # file3.close()
            file.write(user + '\t' + user_list[i] + '\n')
            count = count + 1
            time.sleep(2)

        file.close()
        level = level + 1
        print(count)
        print('level:', level)
        # cookie = [{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593163116.007996, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_5sPZC9AKEP63pS81qtjFbA=="'}, {'domain': '.twitter.com', 'expiry': 1845451123, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530112716.888748, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'bbcbd7a0dfba3cd19893313d04906a87'}, {'domain': '.twitter.com', 'expiry': 1593163116.008242, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153009111625535430'}, {'domain': '.twitter.com', 'expiry': 1593163120, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746318223.1530091121'}, {'domain': '.twitter.com', 'expiry': 1530091180, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845451122.826011, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530177520, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1855516644.1530091121'}, {'domain': '.twitter.com', 'expiry': 1845451122.825764, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577351922.825801, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'BV70DdKxwFi9hI2qi38hAGejFVwltKLrpRCzaC84'}, {'domain': '.twitter.com', 'expiry': 1845451122.825836, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAGaiUBkAToMY3NyZl9p%250AZCIlMGY4ZTFiYzNmN2ZkMGM5NDQwMmE1NzJkYzM2ZjZmODM6B2lkIiUyMzRk%250AZTNkZDk1YjlhNjZlZjQ4MzY3ZDA0Nzc1YzhiNToJdXNlcmwrCQLQVIfs3eUN--b4094c5eb229e5f3123d711db3b28b6f77c5b705'}, {'domain': '.twitter.com', 'expiry': 1845451122.826049, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ba9113d4621da9bebab2060bcadc69f09643d732'}, {'domain': '.twitter.com', 'expiry': 1561540723.064481, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561627123.064564, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]


        for i in range(len(flo_list)):
            yield scrapy.Request(url='https://twitter.com/' + flo_list[i] + '/following', meta={'level': level,'user':flo_list[i]},callback=self.get_fan2)#, cookies=cookie)






# 这是下拉滚动条刷新的请求
# https://twitter.com/i/profiles/show/ForbesTech/timeline/tweets?include_available_features=1&include_entities=1&max_position=1001583539169603584&reset_error_state=false
