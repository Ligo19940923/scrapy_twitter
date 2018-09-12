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

        #抓取测试
        # timeline = response.xpath('//div[@class="stream"]//li[@class="js-stream-item stream-item stream-item\n"]')
        # count = 0
        # for tweet in enumerate(timeline):
        #     count = count + 1
        #
        # print(count)

        # 获取粉丝数
        # follow_number = response.xpath('//*[@id="page-container"]/div[3]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[2]/a/span[3]/text()').extract()
        # print(follow_number)



        #设置种子用户，以种子用户为根节点逐层抓取
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
        # 依次发送请求
        for name in user_name:
            # 发送请求时传递初始层次，level为1，处理返回响应的方法为get_fan2
            yield scrapy.Request(url='https://twitter.com/'+name+'/following',meta={'level': 1, 'user': name}, callback=self.get_fan2)



    # 获取粉丝的测试方法，目前已不使用
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


    # 获取粉丝的方法
    def get_fan2(self,response):
        # 使用twitter API获取每个粉丝的粉丝数，用来判断是否为大V
        # 使用API，对token进行授权
        auth = tweepy.OAuthHandler("NQE7OU3yhqTe6HEvZ7ty2kTLh", "x8UH9ZRWOmqOd7C8Nvkf6XahzloyZ7QOKEj1EYj75j4dpydvvC")
        auth.set_access_token("946989804738134018-EykBrYBvsVh0BX374rvL4Xw0HflnDcB",
                              "lAZJqB0e6IVkkvdihABa0I9MJX3FsPou51lvkgMqzkoj7")

        # 设置API
        api = tweepy.API(auth, proxy="127.0.0.1:1080")

        # 获取粉丝列表
        following = response.xpath('//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div')
        # 获取上一层所在层次
        level = response.meta['level']
        # 获取上一层的用户名
        user = response.meta['user']
        # 打开一个文件用于存储关注关系
        file = open("Army_Following.txt","a")

        # 存储粉丝screen_name列表
        flo_list = []

        # 判断所在层数,当为四层时停止抓取,member为本层需要抓取的粉丝数量
        if level ==1:
            member = 5
        elif level == 2:
            member = 3
        elif level == 3:
            member = 3
        elif level == 4:
            exit(0)

        # 用于存储粉丝，以及每个粉丝所拥有的粉丝数，方便后续根据粉丝数量进行排序
        user_dict = {}

        # 遍历粉丝列表，由于每6个粉丝存储在一个div块中，因此使用两个循环，一个遍历div块，一个遍历每个div中的粉丝
        for followlist in enumerate(following):
            follow_group = followlist[1].xpath('div')
            for flo in enumerate(follow_group):
                flo_name = flo[1].xpath('div//div[@class="ProfileNameTruncated account-group"]//a/text()').extract()
                flo_screen_name = flo[1].xpath(
                    'div//span[@class="ProfileCard-screenname"]//b[@class="u-linkComplex-target"]/text()').extract()
                # 使用API获取所抓到粉丝的粉丝数量
                user_api = api.get_user(flo_screen_name[0])
                following_count = user_api.followers_count

                # 以用户名为键，粉丝数为值存储到字典中
                user_dict[flo_screen_name[0]]=following_count
                time.sleep(2)

        # 根据粉丝数量对列表进行排序，按降序排列，粉丝数多的在前
        user_list = sorted(user_dict, key= lambda x:user_dict[x],reverse=True)

        # 根据每层需要抓取的粉丝数member，抓取排在前member个的粉丝
        count = 0
        for i in range(member):
            selected_user = user_list[i]
            # 存入flo_list,以便后续进一步发送请求进行抓取
            flo_list.append(selected_user)
            print(user_list[i])


            #使用API抓取粉丝主页的twitter，不需要抓取时可以注释掉
            # tweets = api.user_timeline(user_list[i], count=tweet_count)
            # file3 = open("user_timeline.txt", "a",encoding="utf8")
            # for t in tweets:
            #     text = t.text.replace('\n', '')
            #     created_at = t.created_at
            #     id = t.id
            #     file3.write(user_list[i] + '\t' + str(id) + '\t' + str(created_at) + '\t' + text + '\n')
            #
            # file3.close()


            # 将关注关系存入文件
            file.write(user + '\t' + user_list[i] + '\n')
            count = count + 1
            time.sleep(2)

        file.close()

        # 层次加一
        level = level + 1
        print(count)
        print('level:', level)
        # cookie = [{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593163116.007996, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_5sPZC9AKEP63pS81qtjFbA=="'}, {'domain': '.twitter.com', 'expiry': 1845451123, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530112716.888748, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'bbcbd7a0dfba3cd19893313d04906a87'}, {'domain': '.twitter.com', 'expiry': 1593163116.008242, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153009111625535430'}, {'domain': '.twitter.com', 'expiry': 1593163120, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.746318223.1530091121'}, {'domain': '.twitter.com', 'expiry': 1530091180, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845451122.826011, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530177520, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1855516644.1530091121'}, {'domain': '.twitter.com', 'expiry': 1845451122.825764, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577351922.825801, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'BV70DdKxwFi9hI2qi38hAGejFVwltKLrpRCzaC84'}, {'domain': '.twitter.com', 'expiry': 1845451122.825836, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAGaiUBkAToMY3NyZl9p%250AZCIlMGY4ZTFiYzNmN2ZkMGM5NDQwMmE1NzJkYzM2ZjZmODM6B2lkIiUyMzRk%250AZTNkZDk1YjlhNjZlZjQ4MzY3ZDA0Nzc1YzhiNToJdXNlcmwrCQLQVIfs3eUN--b4094c5eb229e5f3123d711db3b28b6f77c5b705'}, {'domain': '.twitter.com', 'expiry': 1845451122.826049, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ba9113d4621da9bebab2060bcadc69f09643d732'}, {'domain': '.twitter.com', 'expiry': 1561540723.064481, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561627123.064564, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]

        # 根据筛选出来的粉丝进行下一层的递归抓取
        for i in range(len(flo_list)):
            yield scrapy.Request(url='https://twitter.com/' + flo_list[i] + '/following', meta={'level': level,'user':flo_list[i]},callback=self.get_fan2)#, cookies=cookie)







