from bs4 import BeautifulSoup
import os
from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
from lxml import html


def extract_company_name_from_xbrl(xbrl_path):
    with open(xbrl_path, encoding='utf-8') as f:
        #soup = BeautifulSoup(f.read(), 'htm')
        soup = BeautifulSoup(html, 'lxml')
        nonnumeric_tags = soup.find_all('ix:nonnumeric')
        for tag in nonnumeric_tags:
            if tag.get('name') == 'jpdei_cor:FilerNameInJapaneseDEI':
                return tag.text

# XBRLファイルのパスを指定
folder_path = r'/TDnet_XBRL/zip_files/9163'
filename = '0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm'
xbrl_path = os.path.join(folder_path, filename)
company_name = extract_company_name_from_xbrl(xbrl_path)
print(f"企業名: {company_name}")





# init parser
parser = EdinetXbrlParser()

folder_path = r'/TDnet_XBRL/zip_files/9163'
filename = '0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm'
xbrl_path = os.path.join(folder_path, filename)
xbrl_file = open(xbrl_path, "r", encoding="utf-8").read()
xbrl_object = parser.parse_file(xbrl_path)

# 企業名の取得
# key = "jpdei_cor:FilerNameInJapaneseDEI"
key = "ix:nonNumeric"

context = "FilingDateInstant"

cname = xbrl_object.get_data_by_context_ref(key, context).get_value()

print(f'企業名{cname}の取得に成功しました')


def fn_parse(sic , xbrl_path):

    # htmファイル読み込み
    xbrl_file = open(xbrl_path, "r", encoding="utf-8").read()
    soup = BeautifulSoup(xbrl_file, "html.parser")
    print(xbrl_file)

    # ix:nonnumeric
    print("■ ix:nonnumeric")

    nms = soup.find_all("ix:nonnumeric")

    for nm in nms:
        print(str(nm.get("name")))

        lst = ['SecuritiesCode', 'URL', 'CompanyName', 'FilingDate', 'FiscalYearEnd']
        lst = lst + ['AccountingStandardsDEI', 'EDINETCodeDEI', 'CurrentFiscalYearStartDateDEI',
                     'CurrentPeriodEndDateDEI'
                     ]
        x = [print(i, nm.text) for i in lst if i in "tse-ed-t:" + nm.get("name")]


if __name__ == '__main__':
    sic = 9163
    folder_path = r'/TDnet_XBRL/zip_files/9163'
    filename = '0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm'
    xbrl_path = os.path.join(folder_path, filename)
    fn_parse(sic, xbrl_path)