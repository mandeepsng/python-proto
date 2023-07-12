import PyPDF2

pdfFileObj = open('/Users/Mandeep/Downloads/Customer.csv', 'rb')

pdfread = pdfFileObj.PdfFileReader(pdfFileObj)

print(pdfread.numPages)

