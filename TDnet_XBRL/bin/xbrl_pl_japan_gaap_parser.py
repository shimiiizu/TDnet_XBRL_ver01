from bs4 import BeautifulSoup
import os


# 売上(億円)を取得する関数
def get_NetSales(xbrl_path):
    file_name = os.path.basename(xbrl_path)
    with open(xbrl_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    if 'ac' in file_name:
        contextref = "CurrentYearDuration"
    elif 'qcpl23' in file_name:
        contextref = "CurrentQuarterDuration"
    elif 'qcpl11' in file_name:
        contextref = "CurrentYTDDuration"
    elif 'an' in file_name:
        contextref = "CurrentYearDuration_NonConsolidatedMember"
    elif 'qn' in file_name:
        contextref = "CurrentQuarterDuration_NonConsolidatedMember"

    tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:NetSales"})
    decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
    decimals_value = int(decimals_value)
    exchange_ratio = 10 ** (-8 - decimals_value)
    netsales = tag.text
    netsales = int(netsales.replace(",", ""))  # カンマを削除
    netsales = round(netsales * exchange_ratio, 1)  # 金額を億円単位に換算
    return netsales


# 販売費及び一般管理費(億円)を取得する関数
def get_SellingGeneralAndAdministrativeExpenses(xbrl_path):
    file_name = os.path.basename(xbrl_path)
    with open(xbrl_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    if 'ac' in file_name:
        contextref = "CurrentYearDuration"
    elif 'qcpl23' in file_name:
        contextref = "CurrentQuarterDuration"
    elif 'qcpl11' in file_name:
        contextref = "CurrentYTDDuration"
    elif 'an' in file_name:
        contextref = "CurrentYearDuration_NonConsolidatedMember"
    elif 'qn' in file_name:
        contextref = "CurrentQuarterDuration_NonConsolidatedMember"

    tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:SellingGeneralAndAdministrativeExpenses"})
    if tag == None:
        print('SellingGeneralAndAdministrativeExpensesを取得できませんでした。')
    else:
        decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
        decimals_value = int(decimals_value)
        exchange_ratio = 10 ** (-8 - decimals_value)
        sellingGeneralandadministrativeexpenses = tag.text
        sellingGeneralandadministrativeexpenses = int(sellingGeneralandadministrativeexpenses.replace(",", ""))  # カンマを削除
        sellingGeneralandadministrativeexpenses = round(sellingGeneralandadministrativeexpenses * exchange_ratio, 1)  # 金額を億円単位に換算
        return sellingGeneralandadministrativeexpenses


# 営業利益(億円)を取得する関数
def get_OperatingIncome(xbrl_path):
    file_name = os.path.basename(xbrl_path)
    with open(xbrl_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    if 'ac' in file_name:
        contextref = "CurrentYearDuration"
    elif 'qcpl23' in file_name:
        contextref = "CurrentQuarterDuration"
    elif 'qcpl11' in file_name:
        contextref = "CurrentYTDDuration"
    elif 'an' in file_name:
        contextref = "CurrentYearDuration_NonConsolidatedMember"
    elif 'qn' in file_name:
        contextref = "CurrentQuarterDuration_NonConsolidatedMember"

    tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:OperatingIncome"})
    decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
    decimals_value = int(decimals_value)
    exchange_ratio = 10 ** (-8 - decimals_value)
    operatingincome = tag.text
    operatingincome = int(operatingincome.replace(",", ""))  # カンマを削除
    operatingincome = round(operatingincome * exchange_ratio, 1)  # 金額を億円単位に換算
    return operatingincome


# 経常利益(億円)を取得する関数
def get_OrdinaryIncome(xbrl_path):
    file_name = os.path.basename(xbrl_path)
    with open(xbrl_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    if 'ac' in file_name:
        contextref = "CurrentYearDuration"
    elif 'qcpl23' in file_name:
        contextref = "CurrentQuarterDuration"
    elif 'qcpl11' in file_name:
        contextref = "CurrentYTDDuration"
    elif 'an' in file_name:
        contextref = "CurrentYearDuration_NonConsolidatedMember"
    elif 'qn' in file_name:
        contextref = "CurrentQuarterDuration_NonConsolidatedMember"

    tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:OrdinaryIncome"})
    decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
    decimals_value = int(decimals_value)
    exchange_ratio = 10 ** (-8 - decimals_value)
    ordinaryincome = tag.text
    ordinaryincome = int(ordinaryincome.replace(",", ""))  # カンマを削除
    ordinaryincome = round(ordinaryincome * exchange_ratio, 1)  # 金額を億円単位に換算
    return ordinaryincome


# 純利益(億円)を取得する関数
def get_NetIncome(xbrl_path):
    file_name = os.path.basename(xbrl_path)
    with open(xbrl_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    if 'ac' in file_name:
        contextref = "CurrentYearDuration"
    elif 'qcpl23' in file_name:
        contextref = "CurrentQuarterDuration"
    elif 'qcpl11' in file_name:
        contextref = "CurrentYTDDuration"
    elif 'an' in file_name:
        contextref = "CurrentYearDuration_NonConsolidatedMember"
    elif 'qn' in file_name:
        contextref = "CurrentQuarterDuration_NonConsolidatedMember"

    tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:NetIncome"})
    if tag is None:
        tag = soup.find("ix:nonfraction", attrs={"contextref": contextref, "name": "jppfs_cor:ProfitLoss"})
        decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
        decimals_value = int(decimals_value)
        exchange_ratio = 10 ** (-8 - decimals_value)
        netincome = tag.text
        netincome = int(netincome.replace(",", ""))  # カンマを削除
        netincome = round(netincome * exchange_ratio, 1)  # 金額を億円単位に換算
        return netincome
    else:
        decimals_value = tag.get("decimals")  # お金の単位（‐3の時は千円、‐6の時は百万円 ）
        decimals_value = int(decimals_value)
        exchange_ratio = 10 ** (-8 - decimals_value)
        netincome = tag.text
        netincome = int(netincome.replace(",", ""))  # カンマを削除
        netincome = round(netincome * exchange_ratio, 1)  # 金額を億円単位に換算
        return netincome



if __name__ == '__main__':
    #xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0301000-acpl01-tse-acedjpfr-36790-2015-03-31-01-2015-05-15-ixbrl.htm"
    #xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0301000-acpl01-tse-acedjpfr-36790-2015-03-31-01-2015-05-15-ixbrl.htm"
    #xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0600000-qcpl11-tse-qcedjpfr-36790-2014-06-30-01-2014-08-12-ixbrl.htm"
    #xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0600000-qcpl11-tse-qcedjpfr-36790-2014-06-30-01-2014-08-12-ixbrl.htm"
    xbrl_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\7172\0102010-acpl01-tse-acedjpfr-71720-2014-12-31-01-2015-02-12-ixbrl.htm"

    print(get_NetSales(xbrl_path))
    print(get_SellingGeneralAndAdministrativeExpenses(xbrl_path))
    print(get_OperatingIncome(xbrl_path))
    print(get_NetIncome(xbrl_path))