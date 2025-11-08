"""
企業コードを入力すると対応するXBRLファイルを解析してBS情報のレコードを出力する

入力①：XBRLファイルが入っているフォルダパス folder_path
入力②：企業コード code
出力①：BS関連のデータフレーム(レコード) df
出力②：BS関連のプリント出力
"""

import bs_list_maker as mb  # 自作モジュール： BSのXBRLファイルパスのリストを作成する
import xbrl_bs_common_parser as px  # 自作モジュール： XBRLの基本情報を抽出する
import bs_db_record as cd  # 自作モジュール：BSのレコードを作成する
import bs_common_printer as pbc  # 自作モジュール：BSの基本情報をプリントアウトする
import bs_ifrs_printer as pbi  # 自作モジュール：BS（IFRS）情報をプリントアウトする
import bs_japan_gaap_printer as jgp # 自作モジュール：BS（Japan_Gaap）情報をプリントアウトする

class BsReporter:

    # コンストラクタ（インスタンス変数の初期化）
    def __init__(self, code, new_folder_path):
        self.code = code  # 企業コード
        self.new_folder_path = new_folder_path  # XBRLが入っているフォルダ
        self.ac_bs_list = mb.get_acbs_list(self.new_folder_path)  # 通期のBSファイルのリスト
        self.qc_bs_list = mb.get_qcbs_list(self.new_folder_path)  # 四半期のBSファイルのリスト

    def process_bs_files(self, bs_list):
        for bs_file_path in bs_list:
            print(f'処理対象ファイル：{bs_file_path}')
            print(f'{self.code}のBSの基本情報を表示')
            pbc.print_bs_common_info(bs_file_path)

            accounting_standard = px.get_AccountingStandard(bs_file_path)
            if accounting_standard == "IFRS":
                print(f'{self.code}のBSの情報を表示（IFRS形式）')
                pbi.print_bs_ifrs_info(bs_file_path)
            elif accounting_standard == "Japan GAAP":
                print(f'{self.code}のBSの情報を表示（Japan GAAP形式）')
                jgp.print_bs_japan_gaap_info(bs_file_path)
            else:
                print('IFRSでもJapan GAAPでもありません')

            print("レコードを作成開始")
            cd.create_bs_db_record(bs_file_path)

    def record_bs_info(self):
        self.process_bs_files(self.ac_bs_list)
        self.process_bs_files(self.qc_bs_list)
