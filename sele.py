from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyautogui import click, locateCenterOnScreen, ImageNotFoundException
from time import sleep

URL = "https://spotifymate.com/"

base = "https://open.spotify.com/track/"

ids = """12TP8c0mlvpZpKo1YhVcKc
5iQDeHszlApK5qgRaqEBTv
28ADc91k22VcUqT4ao4Z8s""".split(
    "\n"
)

for song_id in ids:
    driver = webdriver.Edge()

    driver.get(URL)

    elem = driver.find_element(By.ID, "url")
    elem.clear()
    elem.send_keys(base + song_id)
    elem.send_keys(Keys.RETURN)
    found = False
    while not found:
        try:
            img = locateCenterOnScreen("./image.png", confidence=0.7)
            found = True
        except ImageNotFoundException:
            pass

    click(img.x, img.y)
    sleep(6)

input()
