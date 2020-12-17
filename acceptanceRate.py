from pynput.keyboard import Controller, Key
from bs4 import BeautifulSoup
import webbrowser
import time
import re
import os

keyboard = Controller()

def getAcceptanceRate(university):
	if ("Institute" in university) or ("University" in university):
		url = "https://www.niche.com/colleges/" + university + "/"
	else:
		url = "https://www.niche.com/colleges/" + university + "-university/"
	
	webbrowser.open(url)
	time.sleep(1)
	with keyboard.pressed(Key.ctrl):
	    keyboard.press("u")
	    keyboard.release("u")
	    time.sleep(1)
	    keyboard.press("a")
	    keyboard.release("a")
	    time.sleep(0.5)
	keyboard.press(Key.ctrl)
	keyboard.press('c')
	keyboard.release('c')
	keyboard.release(Key.ctrl)

	time.sleep(0.5)

	keyboard.press(Key.ctrl)
	keyboard.press('w')
	keyboard.release('w')
	keyboard.press('w')
	keyboard.release('w')
	keyboard.release(Key.ctrl)

	os.startfile('clipboard.txt')

	time.sleep(1)

	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	time.sleep(0.5)
	keyboard.press('v')
	keyboard.release('v')
	time.sleep(0.5)
	keyboard.press('s')
	keyboard.release('s')
	time.sleep(0.5)
	keyboard.press('w')
	keyboard.release('w')
	keyboard.release(Key.ctrl)
	
	with open('clipboard.txt', 'r') as file:
	    html = file.read()

	soup = BeautifulSoup(html, features = "html.parser")

	for script in soup(["script", "style"]):
		script.extract()

	text = soup.get_text()

	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)

	acceptance = re.findall('Acceptance Rate[^%]*', text)
	rate = re.findall('[0-9]', acceptance[0])
	
	return rate[0]

print(getAcceptanceRate("harvard"))
