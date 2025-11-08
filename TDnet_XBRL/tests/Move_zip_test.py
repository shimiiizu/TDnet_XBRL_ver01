import shutil
import glob

source_folder = r"C:\Users\SONY\Downloads"

# フォルダ内のファイル名のリストを取得
file_lists = glob.glob(source_folder + "/*.zip")

print(file_lists)

# リストを表示
for file_list in file_lists:
    print(file_list)

"""
    try:
        # ファイルを移動
        shutil.move(source_path, destination_path)
        print(f"ファイルを {destination_path} に移動しました。")

    except FileNotFoundError:
        print("指定されたファイルが見つかりませんでした。")


if __name__ == "__main__":
    # 移動元と移動先のパスを指定
    source_file = "C:\\Users\\SONY\\Downloads
    destination_file = "C:\\Users\\SONY\\PycharmProjects\\pythonProject\\TDnet_XBRL\\zip_files"

    # ファイルを移動
    move_file(source_file, destination_file)
"""