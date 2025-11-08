import requests
from bs4 import BeautifulSoup
import os

# 銘柄コードを指定
ticker = '7011'

# TDNETの適時開示情報一覧ページのURL
base_url = f'https://www.release.tdnet.info/inbs/I_list_001.html?code={ticker}'

# 保存先ディレクトリ
save_dir = 'xbrl_files'
os.makedirs(save_dir, exist_ok=True)

# ページのソースを取得
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# XBRLファイルのリンクを抽出
xbrl_links = []
for link in soup.find_all('a', href=True):
    if 'xbrl' in link['href']:
        xbrl_links.append(link['href'])

# XBRLファイルをダウンロード
for xbrl_link in xbrl_links:
    xbrl_url = 'https://www.release.tdnet.info/inbs/' + xbrl_link
    xbrl_response = requests.get(xbrl_url)
    file_name = os.path.join(save_dir, xbrl_link.split('/')[-1])
    with open(file_name, 'wb') as file:
        file.write(xbrl_response.content)

print("XBRLファイルのダウンロードが完了しました。")