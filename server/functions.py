from bs4 import BeautifulSoup
import requests
import random
from urllib.parse import urlparse

def get_random_img(num):
	sources = [
		"https://www.google.com/search?q=motivational+quotes&rlz=1C1CHBD_enMY902MY902&sxsrf=AOaemvI-ALsJSYuaw9iUcy-pmc_3ogE0vw:1641510744770&source=lnms&tbm=isch&sa=X&sqi=2&ved=2ahUKEwj4zdiGoJ71AhV8wzgGHf8JACUQ_AUoAXoECAEQAw&biw=1280&bih=601&dpr=1.5",
		"https://www.google.com/search?q=insiprational+quotes&tbm=isch&ved=2ahUKEwjxy-WLoJ71AhVHA7cAHYstC-0Q2-cCegQIABAA&oq=insipra+quotes&gs_lcp=CgNpbWcQARgAMgYIABAHEB4yBggAEAcQHjIICAAQBxAFEB4yCAgAEAcQBRAeOgcIIxDvAxAnOgQIABBDOgcIABCxAxBDOgoIABCxAxCDARBDOgUIABCABFCgDFi_H2C-J2gAcAB4AIABTIgBhASSAQE5mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Y3fXYbGOHMeG3LUPi9us6A4&bih=601&biw=1280&rlz=1C1CHBD_enMY902MY902"
	]
	website = requests.get(random.choice(sources))
	soup = BeautifulSoup(website.content, 'html.parser')
	return [img["src"] for img in random.choices(soup.find_all('img'), k=num)]

def get_random_video(num):
	sources = [
		"https://www.google.com/search?q=inspirational+speeches&rlz=1C1CHBD_enMY902MY902&sxsrf=AOaemvK_dsm36aC-Bvkuvjd8nuPMJ3ZPFA:1641517992740&source=lnms&tbm=vid&sa=X&sqi=2&ved=2ahUKEwiIweWGu571AhXs-SoKHc-2D9EQ_AUoAXoECAEQAw&biw=1280&bih=601&dpr=1.5"
	]
	website = requests.get(random.choice(sources))
	soup = BeautifulSoup(website.content, 'html.parser')
	for a in soup.find_all('a'):
		if a.get('href') and 'youtube' in a.get('href'):
			print(a.get('href'))
	return ""

def get_random_quote(num):
	pass

def get_random(num):
	return random.choice([get_random_img(), get_random_video(), get_random_quote()])