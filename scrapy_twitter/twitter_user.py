import tweepy
from urllib import request
import time
def getUser(screen_name):

    auth = tweepy.OAuthHandler("xeq0hXGABEFr41n2VcS8jj7Eg", "3v6T4LpoJkGMDeX20Irt9FtL4WGHcNN0NiY6IQXtDOw8mfGiFS")
    auth.set_access_token("728386974831140864-cfpEh7hKdsLLSka179Q5MDuReFAigtZ", "NgUsNKveM9GyPhyocrwGsn7PYouMv9qe5l04WKlpgMZsz")
    api = tweepy.API(auth, proxy="127.0.0.1:1080")

    # user = api.get_user(screen_name)
    # print(user)
    # print("name:",user.name)
    # print("screen_name",user.screen_name)
    # print("created_at", user.created_at)
    # print("homepage:", user.entities['url']['urls'][0]['expanded_url'])
    # print("description:", user.description)
    # print("location:",user.location)
    # print("favorites_count",user.favourites_count)
    # print("followers:",user.followers_count)
    # print("following:",user.friends_count)
    # print("statuses_count",user.statuses_count)
    # print("verify",user.verified)
    # print("photo",user.profile_image_url)
    # request.urlretrieve(user.profile_image_url,'img/'+screen_name+'.jpg')

    file = open("Army_Following.txt","r")
    name_set = set()
    lines = file.readlines()

    for line in lines:
        member = line.split('\t')
        name1 = member[0]
        name2 = member[1].replace('\n','')
        name_set.add(name1)
        name_set.add(name2)
    for s in name_set:
        file2 = open("newArmy_information.txt", "a", encoding="utf8")
        print(s)
        try:
            user = api.get_user(s)
            user_name = user.name
            screen_name = user.screen_name
            created_at = user.created_at
            homepage = user.entities['url']['urls'][0]['expanded_url'] if "url" in user.entities else 'None'
            description = user.description if user.description != '' else 'None'
            location = user.location if user.location != '' else 'None'
            favourites_count = user.favourites_count
            followers = user.followers_count
            following = user.friends_count
            statuses_count = user.statuses_count
            verify = user.verified

            information = screen_name+'\t'+user_name+'\t'+ str(created_at)+'\t'+str(homepage)+'\t'+description.replace('\n',' ')+'\t'+str(location)+'\t'+str(favourites_count)+'\t'+str(followers)+'\t'+str(following)+'\t'+str(statuses_count)+'\t'+str(verify)
            request.urlretrieve(user.profile_image_url, 'img2/' + s + '.jpg')
            file2.write(information+'\n')
            tweets = api.user_timeline(screen_name, count=20)


            file3 = open("newArmy_timeline.txt", "a",encoding="utf8")
            for t in tweets:
                text = t.text.replace('\n', '')
                created_at = t.created_at
                id = t.id
                file3.write(screen_name + '\t' + str(id) + '\t' + str(created_at) + '\t' + text + '\n')
        except Exception as e :
            print(e)
            continue

        file3.close()
        file2.close()
        time.sleep(1)
    print(len(name_set))
if __name__ == '__main__':
    id = '4398626122'
    str2 = getUser("HUDgov")


