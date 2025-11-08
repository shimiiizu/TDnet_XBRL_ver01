import requests
from bs4 import BeautifulSoup
import os

save_folder = "C:/xbrl"
#url = 'https://www.release.tdnet.info/inbs/081220240725554521.zip'
#url= 'https://www2.jpx.co.jp/tseHpFront/JJK010030Action.do'
url= "https://www2.jpx.co.jp/disc/52330/140120240513594349.zip"
#https://www2.jpx.co.jp/disc/52330/140120240513594349.pdf
#https://www2.jpx.co.jp/disc/52330/081220240513594349_tse-acedjpsm-52330-20240514352330-ixbrl.htm
#081220240513594349_tse-acedjpsm-52330-20240514352330-ixbrl.htm
# 指定したURLからZIPファイルをダウンロードする関数

def download_zip_file(url, save_folder):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # ファイル名を取得
            filename = os.path.basename(url)
            # 保存先のパスを作成
            save_path = os.path.join(save_folder, filename)
            # ファイルを保存
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"{save_folder} に保存しました。")
        else:
            print(f"ダウンロードに失敗しました。ステータスコード: {response.status_code}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


# ZIPファイルをダウンロード
download_zip_file(url, save_folder)