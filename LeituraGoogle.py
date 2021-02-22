# sudo apt-get update && sudo apt-get install espeak
# pip install google_speech
# 1. pip install pyttsx3
# 2. sudo apt install libespeak1
# 3. pip install pypdf2

from google_speech import Speech
import PyPDF2

# ABRIR O ARQUIVO PDF
book = open("tx2.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)

# OBTER O TEXTO
page = pdfReader.getPage(20)
text = page.extractText().encode("utf-8").decode("utf-8")
text = text.replace('\n', '')
#print(text)

# LER O TEXTO
lang = "pt_br"
speech = Speech(text, lang)

#TOCA TEXTO
speech.play()

#GRAVAR ARQUIVO
speech.save("saida.mp3")
