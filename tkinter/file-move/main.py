import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
from pathlib import Path

class FileMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title('ファイル移動アプリ')

        # デフォルトのフォルダパス
        self.source_folder_path = Path('path/src-dir')
        self.destination_folder_path = Path('path/dist-path')

        self.setup_ui()

    def setup_ui(self):
        self.btn_select_source = tk.Button(self.root, text="移動元フォルダ選択", command=self.on_select_source)
        self.btn_select_source.pack(pady=10)

        self.btn_select_destination = tk.Button(self.root, text="移動先フォルダ選択", command=self.on_select_destination)
        self.btn_select_destination.pack(pady=10)

        self.btn_move = tk.Button(self.root, text="ファイル移動", command=self.on_move)
        self.btn_move.pack(pady=10)

        self.label_source_folder = tk.Label(self.root, text=f"移動元フォルダ: {self.source_folder_path}")
        self.label_source_folder.pack(pady=5)

        self.label_destination_folder = tk.Label(self.root, text=f"移動先フォルダ: {self.destination_folder_path}")
        self.label_destination_folder.pack(pady=5)

        self.btn_quit = tk.Button(self.root, text="終了", command=self.root.destroy)
        self.btn_quit.pack(pady=10)

        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack(pady=5)

    def on_select_source(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.source_folder_path = Path(folder_path)
            self.label_source_folder.config(text=f"移動元フォルダ: {self.source_folder_path}")

    def on_select_destination(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.destination_folder_path = Path(folder_path)
            self.label_destination_folder.config(text=f"移動先フォルダ: {self.destination_folder_path}")

    def on_move(self):
        if self.source_folder_path and self.destination_folder_path:
            files_to_move = list(self.source_folder_path.glob('*'))
            if not files_to_move:
                self.label_result.config(text="エラー: 移動元フォルダにファイルがありません。")
                return

            file_names = '\n'.join([f.name for f in files_to_move])
            message = f"以下のファイルを\n{self.destination_folder_path}に移動しますか？\n\n{file_names}"

            if messagebox.askyesno("ファイル移動の確認", message):
                try:
                    for file in files_to_move:
                        shutil.move(str(file), str(self.destination_folder_path))
                    self.label_result.config(text="ファイルがすべて移動されました。")
                except Exception as e:
                    self.label_result.config(text=f"エラーが発生しました: {e}")
            else:
                self.label_result.config(text="移動がキャンセルされました。")
        else:
            self.label_result.config(text="エラー: 移動元または移動先フォルダが設定されていません。")

def main():
    root = tk.Tk()
    app = FileMoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
