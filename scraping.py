from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://qiita.com/')

items = browser.find_elements_by_class_name('tr-Item_title')

# 取得した複数の記事タイトルをfor文で展開する。
print('------') # 出力結果をわかりやすくするための記号列
for item in items:
    print(item.text) # item.textとすればタイトルを取ることができる。
    print('------') # 出力結果をわかりやすくするための記号列

# ブラウザを閉じる。
browser.close()