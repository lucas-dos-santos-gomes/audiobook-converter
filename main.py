from tkinter import filedialog
import tkinter as tk
import PyPDF2 as pdf
import pyttsx3 as pts

# Abre janela para selecionar pdf
def select_pdf_file():
  audio_text["text"] = "Rodando áudio..."

  file_search = tk.Tk()
  file_search.withdraw()
  file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
  file_search.destroy()
  return read_pdf(file_path)

def read_pdf(pdf_path):  
  # Abre o E-book e faz a letura das informações
  path = open(pdf_path, "rb")
  pdf_reader = pdf.PdfReader(path)

  speak = pts.init()

  # Percorre as páginas do E-book, extrai o texto e faz a leitura
  for page in pdf_reader.pages:
    text = page.extract_text()
    speak.say(text)
    speak.runAndWait()
  speak.stop()

  audio_text["text"] = "Áudio finalizado"

# Cria a janela
window = tk.Tk()
window.resizable(False, False)
window.title("Conversor de Audiobook")

text_guindance = tk.Label(window, text="Clique no botão abaixo para selecionar um E-book:")
text_guindance.grid(column=0, row=0, padx=10, pady=[10, 5])

test = 0

button = tk.Button(window, text="Buscar PDF", command=select_pdf_file)
button.grid(column=0, row=1, padx=10, pady=[5, 0])

audio_text = tk.Label(window, text="")
audio_text.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()