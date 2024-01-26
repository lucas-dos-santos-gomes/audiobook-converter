import PyPDF2, pyttsx3

# Abre o E-book (.pdf)
path = open("codigo-eficiente-com-python.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

# Percorre as páginas do E-book, extrai o texto e faz a leitura
for page in pdf_reader.pages:
  text = page.extract_text()
  speak.say(text)
  speak.runAndWait()
speak.stop()