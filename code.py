import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from time import sleep

PATH = "./chromedriver.exe"
PROXY = "proxy.soax.com:10002" 
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))
driver = webdriver.Chrome(service=Service(PATH) , options=options)
driver.get('https://twitter.com/login')

subject = "Aditya Sharma"

sleep(3)

username = driver.find_element(By.PATH, "//input[@name='text']")
username.send_keys('XYZ') # Enter your username

next_button = driver.find_element(By.XPATH, "//span[text(), 'Next']")

next_button.click()

sleep(3)

password = driver.find_element(By.PATH, "//input[@name='password']")
password.send_keys('password') #fill password

login = driver.find_element(By.XPATH, "//span[text(), 'Log in']")

login.click()

# Searching 

sleep(3)
search_box = driver.find_element(
    By.XPATH, "//input[@data-testid='SearchBox_search_input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)

people = driver.find_element(By.XPATH, "//span[contains(text(), 'People')]")
people.click()

sleep(3)

profile = driver.find_element(
    By.PATH, "//*[@id='react-root']/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div"
)
profile.click()

userTags = []
timeStamps = []
tweets = []
replies = []
rts = []
likes = []

tweets = driver.find_element(By.XPATH, "//article[@data-testid='tweet']")

while true:
    for tweet in tweets:
        timeStamp = driver.find_element(By.XPATH, ".//time").get_attribute("datetime")
        timeStamps.append(timeStamp)
        
        tweet = driver.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        tweets.append(Tweet)
        
        reply = driver.find_element(By.XPATH, ".//div[@data-testid='reply']").text
        replys.append(Replys)
        
        rts = driver.find_element(By.XPATH, ".//div[@data-testid='retweet']").text
        rts.append(reTweet)
        
        like = driver.find_element(By.XPATH, ".//div[@data-testid='like']").text
        likes.append(Like)
        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    
    tweets = driver.find_element(By.XPATH, "//article[@data-testid='tweet']")
    
    tweets2 = list(set(tweets))
    
    if len(tweets2) > 5:
        break
    
print(tweets)
    
        
        
        