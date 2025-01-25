import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from pandastable import Table

class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dataset Analyzer")
        self.root.geometry("800x600")

        self.dataset = None

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.upload_button = tk.Button(self.root, text="Upload Dataset", command=self.upload_dataset)
        self.upload_button.pack(pady=10)

        self.info_button = tk.Button(self.root, text="Dataset Info", command=self.show_info, state=tk.DISABLED)
        self.info_button.pack(pady=10)

        self.stats_button = tk.Button(self.root, text="Statistics", command=self.show_statistics, state=tk.DISABLED)
        self.stats_button.pack(pady=10)

        self.preview_button = tk.Button(self.root, text="Preview Data", command=self.preview_data, state=tk.DISABLED)
        self.preview_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

        self.text_box = tk.Text(self.root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=80)
        self.text_box.pack(pady=10)

    def upload_dataset(self):
        file_path = filedialog.askopenfilename(
            title="Select Dataset",
            filetypes=[("CSV Files", "*.csv")]
        )
        if file_path:
            try:
                self.dataset = pd.read_csv(file_path)
                messagebox.showinfo("Success", "Dataset uploaded successfully!")
                self.enable_buttons()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset: {e}")

    def enable_buttons(self):
        self.info_button.config(state=tk.NORMAL)
        self.stats_button.config(state=tk.NORMAL)
        self.preview_button.config(state=tk.NORMAL)

    def show_info(self):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        info = self.dataset.info()
        buf = []
        self.dataset.info(buf=buf)
        self.text_box.insert(tk.END, "\n".join(buf))
        self.text_box.config(state=tk.DISABLED)

    def show_statistics(self):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        stats = self.dataset.describe().to_string()
        self.text_box.insert(tk.END, stats)
        self.text_box.config(state=tk.DISABLED)

    def preview_data(self):
        top = tk.Toplevel(self.root)
        top.title("Data Preview")
        frame = tk.Frame(top)
        frame.pack(fill=tk.BOTH, expand=1)
        
        table = Table(frame, dataframe=self.dataset)
        table.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
