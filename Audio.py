import pyttsx3         # speech library
import PyPDF2
file = open('read.pdf',mode='rb')
pdf_reader = PyPDF2.PdfFileReader(file)
pages = pdf_reader.numPages
print(pages)
melo = pyttsx3.init()
for i in range(7,8):
    page = pdf_reader.getPage(7)
    text = page.extractText()
    melo.say(text)
    melo.runAndWait()
