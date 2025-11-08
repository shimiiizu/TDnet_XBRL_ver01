"""
データベースにPLデータを保管する

"""

import sqlite3
import xbrl_pl_ifrs_parser
import xbrl_pl_japan_gaap_parser
from pl_filename_parser import PlFilenameParser
import os


class PlDBInserter:

    def __init__(self, pl_file_path):
        self.pl_file_path = pl_file_path  # 通期のPLファイルのリスト
        self.file_name = os.path.basename(pl_file_path)
        self.DB = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\db\PL_DB.db"


    def insert_to_pl_db(self):

        plfilenameparser = PlFilenameParser(self.pl_file_path)
        filename = plfilenameparser.get_filename()
        code = plfilenameparser.get_code()
        publicday = plfilenameparser.get_public_day()
        conn = sqlite3.connect(self.DB)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM PL WHERE FileName = ?', (filename,))
        if cursor.fetchone()[0] == 0: # codeの情報がない場合にDBに挿入

            first_string = 'iffr'
            second_string = 'pl'
            if first_string in self.file_name and second_string in self.file_name:
                revenueifrs = xbrl_pl_ifrs_parser.get_RevenueIFRS(self.pl_file_path)
                sellinggeneralandadministrativeexpensesifrs = xbrl_pl_ifrs_parser.get_SellingGeneralAndAdministrativeExpensesIFRS(self.pl_file_path)
                operatingprofitlossifrs = xbrl_pl_ifrs_parser.get_OperatingProfitLossIFRS(self.pl_file_path)
                profitLossifrs = xbrl_pl_ifrs_parser.get_ProfitLossIFRS(self.pl_file_path)
                dilutedearningslosspershareifrs = xbrl_pl_ifrs_parser.get_DilutedEarningsLossPerShareIFRS(self.pl_file_path)

                cursor.execute('''INSERT INTO PL 
                        (Code,FileName,PublicDay,RevenueIFRS,SellingGeneralAndAdministrativeExpensesIFRS,OperatingProfitLossIFRS,ProfitLossIFRS,DilutedEarningsLossPerShareIFRS)
                        VALUES (?,?,?,?,?,?,?,?)''',
                               (code, filename, publicday, revenueifrs, sellinggeneralandadministrativeexpensesifrs,
                                operatingprofitlossifrs, profitLossifrs, dilutedearningslosspershareifrs))

            first_string = 'jpfr'
            second_string = 'pl'
            if first_string in self.file_name and second_string in self.file_name:
                netsales = xbrl_pl_japan_gaap_parser.get_NetSales(self.pl_file_path)
                sellinggeneralandadministrativeexpenses = xbrl_pl_japan_gaap_parser.get_SellingGeneralAndAdministrativeExpenses(
                    self.pl_file_path)
                operatingincome = xbrl_pl_japan_gaap_parser.get_OperatingIncome(self.pl_file_path)
                ordinaryincome = xbrl_pl_japan_gaap_parser.get_OrdinaryIncome(self.pl_file_path)
                netincome = xbrl_pl_japan_gaap_parser.get_NetIncome(self.pl_file_path)
                cursor.execute('''INSERT INTO PL 
                                        (Code,FileName,PublicDay,NetSales,SellingGeneralAndAdministrativeExpenses,OperatingIncome,OrdinaryIncome,NetIncome)
                                        VALUES (?,?,?,?,?,?,?,?)''',
                               (code, filename, publicday, netsales, sellinggeneralandadministrativeexpenses, operatingincome, ordinaryincome, netincome))

        else:
            print(f'すでに{filename}は登録されています。')

        conn.commit()
        conn.close()


if __name__ == '__main__':
    #pl_file_path = r'C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0301000-acpl01-tse-acedjpfr-36790-2016-03-31-01-2016-05-13-ixbrl.htm'
    #pl_file_path = r'C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0301000-acpl03-tse-acediffr-36790-2019-03-31-01-2019-05-14-ixbrl.htm'
    pl_file_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679\0600000-qcpl11-tse-qcedjpfr-36790-2014-06-30-01-2014-08-12-ixbrl.htm"

    plfilenameparser = PlFilenameParser(pl_file_path)
    plfilenameparser.get_code()
    plfilenameparser.get_filename()
    print(f'企業コードは{plfilenameparser.get_code()}です。')
    print(f'ファイル名は{plfilenameparser.get_filename()}です。')
    print(f'公表日は{plfilenameparser.get_public_day()}です。')

    pldbinserter = PlDBInserter(pl_file_path)
    pldbinserter.insert_to_pl_db()
