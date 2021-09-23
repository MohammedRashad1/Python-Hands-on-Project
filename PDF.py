import PyPDF2
newPdf = open('sample.pdf', 'rb')  # file object creation
readingPdf = PyPDF2.PdfFileReader(newPdf)
print(readingPdf.numPages)  # No.of pages in the pdf

pdfPage = readingPdf.getPage(1)  # page object creation
print(pdfPage.extractText())

newPdf.close()
