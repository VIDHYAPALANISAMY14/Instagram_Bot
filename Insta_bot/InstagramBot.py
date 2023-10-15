from time import sleep
from instabot import Bot
my_bot=Bot()
#login
my_bot.login(username="",password="")

# #follow a user
my_bot.unfollow("art_world_official")

#follow multiple users
my_bot.follow_users(["coders.learning","__code_dev"])

#unfollow the non followers
my_bot.unfollow_non_followers()

#upload an image
my_bot.upload_photo("post.jpg",caption="Love to code")

#send message to user
my_bot.send_message("Hii, see our creations","Art_world")


#like a post
my_bot.like_user("Art_world",amount=2) # last 2 post of the user

#comment 
user_id=my_bot.get_user_id_from_username("Art_world")
media_id=my_bot.get_last_user_medias(user_id)
my_bot.comment(media_id,"Very nice work. Keep rocking")

sleep(20)

#get the list of followers of anyone
followers_list=my_bot.get_user_followers("Art_world")
following_list=my_bot.get_user_following("Art_world")

for each_follower in followers_list:
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))

for each_follow in following_list:
    print(my_bot.get_username_from_user_id(each_follow))

my_bot.logout()

