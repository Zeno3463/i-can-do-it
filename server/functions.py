from bs4 import BeautifulSoup
import requests
import random

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
		"https://www.google.com/search?q=inspirational+speeches&rlz=1C1CHBD_enMY902MY902&sxsrf=AOaemvK_dsm36aC-Bvkuvjd8nuPMJ3ZPFA:1641517992740&source=lnms&tbm=vid&sa=X&sqi=2&ved=2ahUKEwiIweWGu571AhXs-SoKHc-2D9EQ_AUoAXoECAEQAw&biw=1280&bih=601&dpr=1.5",
		"https://www.google.com/search?q=motivational+videos&rlz=1C1CHBD_enMY902MY902&biw=1280&bih=601&tbm=vid&sxsrf=AOaemvLqSf_HNIYH8e6aROO23bZbn8rh-Q%3A1641596424815&ei=CMbYYceSMb2_3LUPusWNwAo&ved=0ahUKEwjHto-e36D1AhW9H7cAHbpiA6gQ4dUDCA4&uact=5&oq=motivational+videos&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEAoyBAgAEAoyBQgAEIAEMgUIABCABDoECCMQJzoHCCMQ6gIQJzoECAAQQzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOggIABCxAxCDAToHCAAQsQMQQzoHCAAQgAQQCjoFCAAQkQJQ9QZY9DtgjT1oAnAAeACAAUqIAY8JkgECMjGYAQCgAQGwAQrAAQE&sclient=gws-wiz-video",
		"https://www.google.com/search?q=celebrity+motivational+speeches&rlz=1C1CHBD_enMY902MY902&biw=1280&bih=601&tbm=vid&sxsrf=AOaemvKd3Ie7V4RTCFwtc3OfGwO7zsCkPg%3A1641596436401&ei=FMbYYerrF4bWz7sPvdSoiAY&oq=celebrity+motiv&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMYADIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCggAEIAEEIcCEBQyBQgAEIAEOgQIIxAnOgUIABCRAjoLCAAQgAQQsQMQgwE6CAgAELEDEIMBOggIABCABBCxAzoECAAQQzoFCAAQsQNQAFjbHGDbKWgAcAB4AIABW4gBkAeSAQIxNZgBAKABAcABAQ&sclient=gws-wiz-video"
	]
	website = requests.get(random.choice(sources))
	soup = BeautifulSoup(website.content, 'html.parser')
	yt_links = [a.get('href') for a in soup.find_all('a', href=True) if 'youtube' in a.get('href')]
	pingless_yt_links = [f"https://www.youtube.com/watch?v={a.replace('/url?q=https://www.youtube.com/watch%3Fv%3D', '').split('&sa')[0]}" for a in yt_links]
	return random.choices(pingless_yt_links, k=num)

def get_random(num):
	return random.choices(get_random_img(num) + get_random_video(num), k=num)