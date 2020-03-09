import time
from random import randrange
from webbot import Browser

web = Browser() #Browser Açılacağını Söylüyor.
web.go_to('https://twitter.com/login') #Twittera gidiyor.
time.sleep(2)
def tweetgonder():
    web.click(xpath='//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[3]/a')  # burada tweetlerin yazıldığı alana tıklıyor.
    time.sleep(2)
##Ayarlar##
file = open('username.txt', 'r') #Kullanıcı Adını çektiği yer.
file1 = open('pass.txt', 'r') #Passwordu çektiği yer.
file2 = open('tweet.txt', 'r') #tweetleri çektiği yer.
while True:
    username = file.readline().rstrip()
    password = file1.readline().rstrip()
    tweet = file2.readline().rstrip()
    Rastgele=str(randrange(99))
    AsılTweet=tweet+Rastgele
    if username == "":
        web.driver.close()
        break
    web.type(username, into='Username')
    web.type(password, into='Password', id='passwordFieldId')
    time.sleep(1)
    web.click(xpath='//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
    time.sleep(1)
    tweetgonder()
    time.sleep(1)
    web.type(AsılTweet)
    time.sleep(1)
    web.click(xpath='//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
    time.sleep(1)
    web.click(xpath='//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[2]/nav/div/div')
    time.sleep(1)
    web.click(xpath='//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div[13]/a')
    time.sleep(1)
    web.click(xpath='//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/span/span')
    time.sleep(2)
    web.go_to('https://twitter.com/login')
    time.sleep(1)

##Teşekkürler.