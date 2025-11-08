"""
code毎に分類されたXBRLファイルの中からPLファイルだけを抜き出し、リストを作成する
qcplは四半期毎の決算、acplは本決算
"""
import glob


def get_qcpl_list(folder_path):
    search_string = 'qcpl'  # 検索したい文字列を指定
    matching_files_qcpl = glob.glob(f'{folder_path}/*{search_string}*')  # 特定の文字列が含まれるファイルの一覧を取得
    return matching_files_qcpl


def get_acpl_list(folder_path):
    search_string = 'acpl'  # 検索したい文字列を指定
    matching_files_acpl = glob.glob(f'{folder_path}/*{search_string}*') # 特定の文字列が含まれるファイルの一覧を取得
    return matching_files_acpl


if __name__ == '__main__':
    folder_path = r"C:\Users\SONY\PycharmProjects\pythonProject\TDnet_XBRL\zip_files\3679"  # フォルダのパスを指定
    print(get_qcpl_list(folder_path))
    print(f'四半期のPLファイル数は{len(get_qcpl_list(folder_path))}です')
    print(get_acpl_list(folder_path))
    print(f'通期のPLファイル数は{len(get_acpl_list(folder_path))}です')