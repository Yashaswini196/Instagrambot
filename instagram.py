import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
if(cookie_del):
    os.remove(cookie_del[0])
from instabot import Bot
bot=Bot()
bot.login(username="instabot1_234", password="insta1234")
#bot.follow('hamidbarkzi07')
bot.upload_photo("C:/Users/Yashaswini/flower/", caption="Blue Rose")
#bot.unfollow("hamidbarkzi07")
#bot.send_message("hello how are you",["gauravrajwada"]) 
'''followers=bot.get_user_followers("instabot1_234")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following("instabot1_234")
for Following in following:
    print(bot.get_user_info(Following))'''
#bot.upload_video("C:/Users/Yashaswini/flower/videoplayback.mp4",caption="video")
