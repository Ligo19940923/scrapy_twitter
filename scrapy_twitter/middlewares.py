from scrapy_twitter.cookies import request_cookies,init_cookie
import base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse

import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware #代理ip，这是固定的导入
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #代理UA，固定导入
import time


class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\sun\\Desktop\\scrapy_twitter\\scrapy_twitter\\chromedriver.exe')
    # 滚动条下拉实现
    def process_request(self,request,spider):
        # cookie = [{'domain': '.twitter.com', 'expiry': 1530085401.300973, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': 'd5f80e7c0ee0231beeae60c0175d2fe1'}, {'domain': '.twitter.com', 'expiry': 1593135797.959365, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153006380223594077'}, {'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.twitter.com', 'expiry': 1593135797.959303, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_t3JE6S8XqAmwq/5QRiKQvw=="'}, {'domain': '.twitter.com', 'expiry': 1845423893.713683, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=946989804738134018"'}, {'domain': '.twitter.com', 'expiry': 1530150315, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1108956550.1530063812'}, {'domain': '.twitter.com', 'expiry': 1530063975, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1593135915, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1701889818.1530063812'}, {'domain': '.twitter.com', 'expiry': 1845423893.71331, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBERAAA="'}, {'domain': '.twitter.com', 'expiry': 1577324693.713437, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'CFv4GDH2JaiNKWsQ99WrOou5NoPdm5Jlk9eyXSuX'}, {'domain': '.twitter.com', 'expiry': 1845423893.713511, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCHXa6D5kAToMY3NyZl9p%250AZCIlMDZhZTQ5YjBkOTE3YjYxODNjM2RiNjM0YjdmYjlkOWY6B2lkIiVlZDRk%250AOTAwODY0ZjQzMDQxZDlkMjQyODYxNWI1NzE1YzoJdXNlcmwrCQJAVcU1YiQN--07ed2b8bc7238d0134a8edeaee68c00daf4e8250'}, {'domain': '.twitter.com', 'expiry': 1845423893.713734, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'f2a7fe371dd4f7266afc8d22ab381cf1cd0298b0'}, {'domain': '.twitter.com', 'expiry': 1561513494.033226, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561599894.03333, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]
        print(request.cookies)
        for co in request.cookies:
            self.driver.add_cookie(co)

        self.driver.get(request.url)
        js = "var q=document.body.scrollHeight ;return(q)"
        Old_Text_height = self.driver.execute_script(js)

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            WebDriverWait(self.driver, 10)
            time.sleep(3)
            js2 = "var q=document.body.scrollHeight ;return(q)"
            New_Text_height = self.driver.execute_script(js2)
            if Old_Text_height == New_Text_height:
                break
            else:
                Old_Text_height = New_Text_height
            time.sleep(1)
        return HtmlResponse(url=request.url,body=self.driver.page_source,request=request,encoding='utf-8',status=200)


# IP池设置
class IPPOOLS(HttpProxyMiddleware):
    ip_pools = [
        {'ip': '101.96.10.5:80'},
        {'ip': '113.200.56.13:8010'},
        {'ip': '94.242.58.108:10010'},
        {'ip': '183.89.120.71:8080'},

        # {'ip':''},
    ]
    def __init__(self,ip=''):
        self.ip = ip
    def process_request(self,request,spider):
        ip = random.choice(self.ip_pools)
        print("使用IP为：",ip)
        try:
            request.meta["proxy"] = "http://"+ip['ip']
        except Exception as e:
            print(e)
            pass


#代理池设置
class UAPOOLS(UserAgentMiddleware):
    user_agent_pools = [
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
        "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    ]
    def __init__(self,user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_pools)
        print("使用用户代理为：",ua)
        try:
            request.headers.setdefault('User-Agent',ua)
        except Exception as e:
            print(e)
            pass


# cookie池设置
class COOKIESPOOL(object):
    cookies_pool=[
        {'cookie':[{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593331832.180842, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_o78m8kdsEkkjDtGqmzKCLQ=="'}, {'domain': '.twitter.com', 'expiry': 1845619856.72932, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530281433.320839, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': '5b245b9645a1a81a9f83ee72d1ef8e2b'}, {'domain': '.twitter.com', 'expiry': 1593331832.180973, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153025984587797331'}, {'domain': '.twitter.com', 'expiry': 1593331846, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.166039280.1530259840'}, {'domain': '.twitter.com', 'expiry': 1530259899, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845619842.748142, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=1001450500112306178"'}, {'domain': '.twitter.com', 'expiry': 1530346246, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.995642488.1530259840'}, {'domain': '.twitter.com', 'expiry': 1845619842.747977, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577520642.748053, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'avp093wd1vexX2iLacv2jndiM4gLjEAJNynPLBeq'}, {'domain': '.twitter.com', 'expiry': 1845619842.748086, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDA3mEpkAToMY3NyZl9p%250AZCIlZTliNGYwZGEwMDQ4YTRhYzNjN2RkMjNkY2IyYTg2NDI6B2lkIiVjNTAw%250AZTY4MzBkMTY4ODdmMTk2NjIyYWJhNzgxZWE3NjoJdXNlcmwrCQLQVIfs3eUN--a2a98a15a69c5e2a2c3f4f74dd806fae45d0275c'}, {'domain': '.twitter.com', 'expiry': 1845619842.748162, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': '387a3c1b6bec20092cbffc73925888d8dda2f35c'}, {'domain': '.twitter.com', 'expiry': 1561709443.057975, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1561795843.05803, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]},
        {'cookie':[{'domain': '.twitter.com', 'expiry': 1530516070.373901, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': '9137c429a3ad6025826cac88f2eb478f'}, {'domain': '.twitter.com', 'expiry': 1593566469.01979, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153049446890929079'}, {'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.twitter.com', 'expiry': 1593566469.01972, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_rCPNtB7vADktUbhPtGLrkQ=="'}, {'domain': '.twitter.com', 'expiry': 1593566486, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.938118017.1530494476'}, {'domain': '.twitter.com', 'expiry': 1530494535, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845854476.491868, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=946989804738134018"'}, {'domain': '.twitter.com', 'expiry': 1530580886, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1790611978.1530494476'}, {'domain': '.twitter.com', 'expiry': 1845854476.491669, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBERAAA="'}, {'domain': '.twitter.com', 'expiry': 1577755276.491704, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'sMkXNlHPH5By1tVzS4a7lnZoH4eGGDCRigVSYD8d'}, {'domain': '.twitter.com', 'expiry': 1845854476.491757, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCDhGlFhkAToMY3NyZl9p%250AZCIlM2Y4ZjM4MTg5MDU4ZGNlNWQ5M2QxOGI4NmRhMjkzOWQ6B2lkIiVmMGU2%250AZWFjOTg2YjZlYTEyNzdhY2VkZDc1MjgwMjgyZDoJdXNlcmwrCQJAVcU1YiQN--32bbef7cc62a33e2d6e911f7a2ae6f6d048d9602'}, {'domain': '.twitter.com', 'expiry': 1845854476.491898, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': '238b3c2907a59110d10b5cf28aa8a07441c1b417'}, {'domain': '.twitter.com', 'expiry': 1561944076.740888, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1562030476.741257, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]},
        {'cookie':[{'domain': '.twitter.com', 'expiry': 1530519305.359709, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': '74cbeecc1a6612717dffe040ad10445b'}, {'domain': '.twitter.com', 'expiry': 1593569704.453845, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153049770460960811'}, {'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593569704.453796, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_ymcR8MHla6npw62zXx6s0g=="'}, {'domain': '.twitter.com', 'expiry': 1593569717, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.450002317.1530497712'}, {'domain': '.twitter.com', 'expiry': 1530497772, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845857714.535729, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=947012406798041090"'}, {'domain': '.twitter.com', 'expiry': 1530584117, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.398055337.1530497712'}, {'domain': '.twitter.com', 'expiry': 1845857714.535598, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBERAAA="'}, {'domain': '.twitter.com', 'expiry': 1577758514.53563, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'duDIKzGPk1bsT3suZYvFmcQcWkdKDiUZ6uPRemnu'}, {'domain': '.twitter.com', 'expiry': 1845857714.535664, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPGlxVhkAToMY3NyZl9p%250AZCIlMTJjMjZiZDRmZTEzMzkwYWFjN2JmOTQ2YWNiNGU1M2E6B2lkIiViZjE2%250AMmNjZDc2ZTg5MzI2ZDJmMDY2MDI1YzA2NzEyMToJdXNlcmwrCQLAFTnEdiQN--f81a0d051addf36ffdb83651aa84aa091320641e'}, {'domain': '.twitter.com', 'expiry': 1845857714.535761, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'd2a0e3b1a9f0fc28cd40bccf1fe94352c78efbf4'}, {'domain': '.twitter.com', 'expiry': 1561947314.778069, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1562033714.778103, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]},
        {'cookie':[{'domain': '.twitter.com', 'expiry': 1530533681.887825, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': '9aaf146cc2fb28a1938baac5bb576a6d'}, {'domain': '.twitter.com', 'expiry': 1593584080.650895, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153051205836561283'}, {'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593584080.65076, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_J5A/ZJ5cjF9p17WffQrAcA=="'}, {'domain': '.twitter.com', 'expiry': 1593584097, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.392208933.1530512087'}, {'domain': '.twitter.com', 'expiry': 1530512147, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845872090.087896, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=728386974831140864"'}, {'domain': '.twitter.com', 'expiry': 1530598497, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.176025447.1530512087'}, {'domain': '.twitter.com', 'expiry': 1845872090.087351, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBERAAA="'}, {'domain': '.twitter.com', 'expiry': 1577772890.087489, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'sw1554KhKeH32IZpIi0Yj43MibyJqMLqJqUlJqJ8'}, {'domain': '.twitter.com', 'expiry': 1845872090.087711, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKysoFlkAToMY3NyZl9p%250AZCIlYjZlMTRkNDMwNzY5NDQwZTFhNTE0MTk3MTZiNjk0NzE6B2lkIiVhNDQ4%250AYmYwOWM0ZTQ1MmZkNTg1NTZjNmZjYzhiYWI1OToJdXNlcmwrCQDg1C0YwBsK--06115fc51ed74b395595f53c3973d797e99c1f12'}, {'domain': '.twitter.com', 'expiry': 1845872090.087968, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': '19f37bac78f55e81bec27bc709ca092cde0c1d7a'}, {'domain': '.twitter.com', 'expiry': 1561961690.374015, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1562048090.374104, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]},
        {'cookie':[{'domain': 'twitter.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'en'}, {'domain': '.twitter.com', 'expiry': 1593570597.289085, 'httpOnly': False, 'name': 'personalization_id', 'path': '/', 'secure': False, 'value': '"v1_JjWt6jLzTGbyliGt0z34yg=="'}, {'domain': '.twitter.com', 'expiry': 1845858612.339145, 'httpOnly': False, 'name': 'dnt', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1530520198.118593, 'httpOnly': False, 'name': 'ct0', 'path': '/', 'secure': True, 'value': '9b99a126c8dd1a055e4ed946ec88bd7a'}, {'domain': '.twitter.com', 'expiry': 1593570597.289159, 'httpOnly': False, 'name': 'guest_id', 'path': '/', 'secure': False, 'value': 'v1%3A153049859752985065'}, {'domain': '.twitter.com', 'expiry': 1593570609, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.111526496.1530498604'}, {'domain': '.twitter.com', 'expiry': 1530498664, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1845858606.744065, 'httpOnly': False, 'name': 'twid', 'path': '/', 'secure': True, 'value': '"u=944107479121543168"'}, {'domain': '.twitter.com', 'expiry': 1530585009, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1535652979.1530498604'}, {'domain': '.twitter.com', 'expiry': 1845858606.743735, 'httpOnly': False, 'name': 'ads_prefs', 'path': '/', 'secure': False, 'value': '"HBESAAA="'}, {'domain': '.twitter.com', 'expiry': 1577759406.743813, 'httpOnly': True, 'name': 'kdt', 'path': '/', 'secure': True, 'value': 'inVJ26P8V1NAEOAUtIm0Nz2Ya3hJRl5CYk4Fe9Vn'}, {'domain': '.twitter.com', 'expiry': 1845858606.743883, 'httpOnly': False, 'name': 'remember_checked_on', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.twitter.com', 'httpOnly': True, 'name': '_twitter_sess', 'path': '/', 'secure': True, 'value': 'BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJJF01hkAToMY3NyZl9p%250AZCIlZDBiNTAyZmZlZTE0YWU2OGFjOWM4YzNkNzg2OTNlM2U6B2lkIiU5MmQz%250AZjYxNzgyOTM5NjYxODg1ZjZhZTA4MjIxMzkzZToJdXNlcmwrCQBA1ArAJBoN--3dfa4f401127f01bb34e676687233fb69a1f8fc8'}, {'domain': '.twitter.com', 'expiry': 1845858606.744142, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': True, 'value': 'ec04f0e33b1f3be9cd8df48413bbae9ed61bd210'}, {'domain': '.twitter.com', 'expiry': 1561948206.979908, 'httpOnly': True, 'name': 'csrf_same_site_set', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.twitter.com', 'expiry': 1562034606.979947, 'httpOnly': True, 'name': 'csrf_same_site', 'path': '/', 'secure': True, 'value': '1'}]}
    ]
    def __init__(self,cookie=[]):
        self.cookie = cookie
    def process_request(self, request, spider):
        ck = random.choice(self.cookies_pool)
        try:
            print(ck['cookie'])
            if(request.url != 'https://twitter.com/robots.txt'):
                request.cookies = ck['cookie']

            print(request.cookies)
        except Exception as e:
            print(e)
            pass