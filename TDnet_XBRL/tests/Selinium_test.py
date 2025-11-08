from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ブラウザを起動
driver = webdriver.Chrome()  # Chromeドライバーを使用
driver.get("https://www2.jpx.co.jp/tseHpFront/JJK010010Action.do?Show=Show")

# 表示数を200件に増やす。(必要ないかもしれない)
# ドロップダウン要素を取得
# dropdown = driver.find_element(By.NAME,"dspSsuPd")
# Selectオブジェクトを作成
# select = Select(dropdown)
# 選択肢のテキストで選択
# select.select_by_visible_text("200件")


# 検索ボックスにキーワードを入力
input_box = driver.find_element(By.NAME,"eqMgrCd")
input_box.send_keys('5233')

search_button = driver.find_element(By.NAME, 'searchButton')
search_button.click()

# 検索結果ページが表示されるまで待機
# driver.implicitly_wait(5)

detail_button = driver.find_element(By.NAME, 'detail_button')
detail_button.click()

# JavaScriptを実行してタブを切り替え
js_code = "javascript:changeTab('2');"  # タブ2をアクティブにするJavaScriptコード
driver.execute_script(js_code)

kaiji_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div[3]/div/table[4]/tbody/tr/th/input')
kaiji_button.click()

youngish_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div[3]/div/table[5]/tbody/tr[3]/td/input')
youngish_button.click()

# alt属性の要素でループ処理を行う。
elements = driver.find_elements(By.XPATH, '//img[@alt="XBRL"]')
print(len(elements))

for element in elements[:10]: # 表示されていないものはダウンロードできないかもしれない。
    print(element)
    element.click()
    time.sleep(3) # 待たないとダウンロードエラーになってしまう。

# WebDriverを終了
driver.quit()



