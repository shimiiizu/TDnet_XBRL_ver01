import Parse_xbrl_common as px
import Make_BS_list as mb
import Create_DB_record as cd
import Print_BS_common_info as pbc
import Print_BS_IFRS_info as pbi

# 依存性の注入を使った疎結合の例

class BSReportProcessor:
    def __init__(self, code, folder_path, bs_list_maker, record_creator, common_info_printer, ifrs_info_printer):
        self.code = code
        self.folder_path = folder_path
        self.bs_list_maker = bs_list_maker
        self.record_creator = record_creator
        self.common_info_printer = common_info_printer
        self.ifrs_info_printer = ifrs_info_printer

    def process_bs_files(self, bs_list):
        for bs_file_path in bs_list:
            print(f'{self.code}のBSの基本情報を表示')
            self.common_info_printer(bs_file_path)

            accounting_standard = self.parser.get_AccountingStandard(bs_file_path)
            if accounting_standard == "IFRS":
                print(f'{self.code}のBSの情報を表示（IFRS形式）')
                self.ifrs_info_printer(bs_file_path)
            elif accounting_standard == "Japan GAAP":
                print(f'{self.code}のBSの情報を表示（Japan GAAP形式）')
                print("")
            else:
                print('IFRSでもJapan GAAPでもありません')

            print("レコードを作成開始")
            self.record_creator.Create_DB_record()

    def process_bs_reports(self):
        ac_bs_list = self.bs_list_maker.get_ac_bs_list(self.folder_path)
        self.process_bs_files(ac_bs_list)

        qc_bs_list = self.bs_list_maker.get_qc_bs_list(self.folder_path)
        self.process_bs_files(qc_bs_list)

# クラスのインスタンスを作成
code = "YOUR_COMPANY_CODE"
folder_path = "YOUR_FOLDER_PATH"
bs_list_maker_instance = mb.Make_BS_list()
record_creator_instance = cd.Create_DB_record()
common_info_printer_instance = pbc.print_bs_common_info()
ifrs_info_printer_instance = pbi.print_bs_ifrs_info()

report_processor = BSReportProcessor(code, folder_path, parser_instance, bs_list_maker_instance,
                                     record_creator_instance, common_info_printer_instance, ifrs_info_printer_instance)

# レポートの処理を実行
report_processor.process_bs_reports()
