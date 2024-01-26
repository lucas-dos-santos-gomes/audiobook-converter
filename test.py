import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')])
  root.destroy()
  return file_path

# Use the function to select a PDF file
pdf_file_path = select_pdf_file()
print(f'Selected PDF file: {pdf_file_path}')