from selenium import webdriver
import re

browser = webdriver.Chrome()
# 徳島県ホームページ
browser.get('https://www.city.tokushima.tokushima.jp/kurashi/recycle/gomi/h30_schedule.html#cmslabel10')


#tableクラスの情報を取得
tables = browser.find_elements_by_xpath('//table[@class="table01"]')

garbage = []
# print(items)
# print(mounths.text)
# print(mounths)
# for tab in tabs:
#     print(tab.text)

for table in tables:
    if table.text.startswith("ごみ"):
        garbage.append(table.text)
        # print(table.text)
    print('------')

for a in garbage:
    print(a)
#C地区のゴミ出しの情報
print(garbage[2].split("\n"))


# ブラウザを閉じる。

