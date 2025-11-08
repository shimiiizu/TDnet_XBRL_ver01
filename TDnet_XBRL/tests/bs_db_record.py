"""
データベースのレコードを作成するプログラム
形式はデータフレームにする。
"""
import pandas as pd
import xbrl_bs_ifrs_parser as px
import xbrl_bs_common_parser as pxc


def create_bs_db_record(xbrl_path):
    columns = ["企業名", "開始日", "終了日", "決算タイプ", "会計の形式", "現金同等物", "流動資産合計", "有形固定資産", "資産合計"]
    df = pd.DataFrame(columns=columns)

    # 基本情報
    try:
        df["企業名"] = [pxc.get_company_name(xbrl_path)]
    except:
        print("企業名の取得に失敗しました。")

    try:
        df["開始日"] = [pxc.get_start_day(xbrl_path)]
    except:
        print("開始日の取得に失敗しました。")

    try:
        df["終了日"] = [pxc.get_end_day(xbrl_path)]
    except:
        print("終了日の取得に失敗しました。")

    try:
        df["決算タイプ"] = [pxc.get_financial_report_type(xbrl_path)]
    except:
        print("決算タイプの取得に失敗しました。")

    try:
        df["会計の形式"] = [pxc.get_AccountingStandard(xbrl_path)]
    except:
        print("会計の形式の取得に失敗しました。")

    # BS（IFRS形式）の情報
    try:
        df["現金同等物"] = [px.get_CashAndCashEquivalent(xbrl_path)]
    except:
        print("現金同等物（IFRS形式）の取得に失敗しました。")

    try:
        df["流動資産合計"] = [px.get_CurrentAssets(xbrl_path)]
    except:
        print("流動資産（IFRS形式）の取得に失敗しました。")

    try:
        df["有形固定資産"] = [px.get_PropertyPlantAndEquipment(xbrl_path)]
    except:
        print("有形固定資産（IFRS形式）の取得に失敗しました。")

    try:
        df["資産合計"] = [px.get_Assets(xbrl_path)]
    except:
        print("資産合計（IFRS形式）の取得に失敗しました。")

    print(df)


if __name__ =='__main__':
    xbrl_path = r"/TDnet_XBRL/zip_files/9163/0300000-acbs03-tse-acediffr-91630-2023-10-31-01-2023-12-13-ixbrl.htm"
    create_bs_db_record(xbrl_path)