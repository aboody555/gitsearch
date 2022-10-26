#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

#scrape = input("what page would you like to scrape? ")
cdp = "/home/kali/scripts/selenium/geckodriver"
driver = webdriver.Firefox(executable_path=cdp)
#driver.get(f"{scrape}")
#url = scrape

driver.get("https://github.com/aboody555")
url = "https://github.com/aboody555"


res = driver.find_elements(By.CLASS_NAME, "repo")


def going_for_raw(second_page):
	driver.get(second_page)
	raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
	raw.click()
	html = driver.page_source
	html = f"{html}"
	if "password" in html:
		print(f"found password in : {second_page}")

def loop(next_page):
	global a
	driver.get(next_page)
	res5 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
	for a in res5: 
		if "py" in a.text:
			second_page = f"{next_page}/blob/main/{a.text}"
			going_for_raw(second_page)



flink = []
links = []
for i in res:
	links.append(i.text)

for l in links:
	next_page = f"{url}/{l}"
	flink.append(next_page)
	loop(next_page)

driver.quit()