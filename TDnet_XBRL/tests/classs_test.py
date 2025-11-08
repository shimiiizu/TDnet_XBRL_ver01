from bs4 import BeautifulSoup
#from config import xbrl_path

class XbrlParser:
    def __init__(self, xbrl_path):
        self.xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files/9163/0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm"
        self.html_content = self._read_html_content()

    def _read_html_content(self):
        with open(self.xbrl_path, 'r', encoding='utf-8') as f:
            return f.read()

    def _get_value(self, tag_name):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        tag = soup.find("ix:nonfraction", attrs={"contextref": "CurrentYearInstant", "name": tag_name})
        decimals_value = int(tag.get("decimals"))
        exchange_ratio = 10 ** (-8 - decimals_value)
        value = int(tag.text.replace(",", ""))
        return round(value * exchange_ratio, 1)

    def get_CashAndCashEquivalent(self):
        return self._get_value("jpigp_cor:CashAndCashEquivalentsIFRS")

    def get_CurrentAssets(self):
        return self._get_value("jpigp_cor:CurrentAssetsIFRS")

# クラスのインスタンスを作成
xbrl_parser = XbrlParser(self.xbrl_path)

# メソッドを呼び出して値を取得
cash_equivalent = xbrl_parser.get_CashAndCashEquivalent()
current_assets = xbrl_parser.get_CurrentAssets()

print(f"現金同等額（億円）: {cash_equivalent}")
print(f"流動資産合計（億円）: {current_assets}")
