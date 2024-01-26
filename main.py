from tkinter import *
from tkinter import filedialog

def select_pdf_file():
  root = Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
  root.destroy()
  return file_path

print(select_pdf_file())