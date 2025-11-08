from bs4 import BeautifulSoup
import requests
import os

# 解析したいWebサイトのURLを指定
xbrl_path = "file:///C:/Users/SONY/PycharmProjects/pythonProject/TDnet_XBRL/zip_files/9163/0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm"

# Webページを取得
html = requests.get(xbrl_path)

# BeautifulSoupでHTMLをパース
soup = BeautifulSoup(html.content, "html.parser")

# 特定のタグ（例えば<ix:nonNumeric>）からテキストを抽出
company_name = soup.find("ix:nonnumeric", attrs={"name": "jpdei_cor:FilerNameInJapaneseDEI"}).text

print(f"企業名: {company_name}")
