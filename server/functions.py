from bs4 import BeautifulSoup
import requests

website = requests.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
soup = BeautifulSoup(website.text, 'html.parser')
print(soup.prettify())

def get_random_img():
	pass

def get_random_video():
	pass

def get_random_quote():
	pass