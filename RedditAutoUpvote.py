
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AutoBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome()

	def login(self):
		bot = self.bot
		bot.get('https://www.reddit.com/login/')
		time.sleep(3)
		user_name = bot.find_element_by_id('loginUsername')
		user_password = bot.find_element_by_id('loginPassword')
		user_name.clear()
		user_password.clear()
		user_name.send_keys(self.username)
		user_password.send_keys(self.password)
		user_password.send_keys(Keys.RETURN)
		time.sleep(3)

	def linkGenerate(self, subreddit):
		bot = self.bot
		bot.get('https://www.reddit.com/r/'+subreddit+'/top/?t=day')
		time.sleep(3)

		lenOfPage = bot.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
		match=False
		while(match==False):
			lastCount = lenOfPage
			time.sleep(3)
			lenOfPage = bot.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			if lastCount==lenOfPage:
				match=True
		
		time.sleep(5)
		ids = bot.find_elements_by_xpath("//a[contains(@id,'PostTopMeta--Created--false--t3_')]")
		list_ids = []
		refined_list = []
		for i in ids:
			list_ids.append(i.get_attribute('id'))
			
		for i in range(len(list_ids)):
			#print(len(list_ids[i]))
			if(len(list_ids[i]) < 50):
				str = list_ids[i].replace('PostTopMeta--Created--false--t3_', '')
				refined_list.append(str)
		#print(refined_list)
		

		for i in refined_list:
			url = 'https://www.reddit.com/r/'+subreddit+'/comments/'+i+'/'
			bot.get(url)
			bot.find_element_by_xpath("//button[contains(@id,'upvote-button-t3_')]").click()
			time.sleep(2)

		bot.quit()
		
		
user = AutoBot('Place_Your_UserName', 'Place_Your_Password')
user.login()
user.linkGenerate('Enter_The_Desired_Subreddit_Name')
