import pyttsx3
import PyPDF2

book = open('oop-book.pdf', 'rb')      
pdf_reader = PyPDF2.PdfFileReader(book)
speaker = pyttsx3.init()
total_page_count = pdf_reader.numPages

for page in range(total_page_count):
    current_page = pdf_reader.getPage(7)
    text_to_read = current_page.extractText()
    speaker.say(text_to_read)
    speaker.runAndWait()