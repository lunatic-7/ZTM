# So, to process PDFs, First we need a suitable library for it. So, we are gonna install PyPDF2.
# by typing pip install PyPDF2 in terminal. And then we are gonna import it to use further.

import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)  # To read the pdf file
    print(reader.numPages)  # Will simply tell number of pages in pdf.
    page = reader.getPage(0)  # Will give information of 1st page.
    print(page)
    page.rotateCounterClockwise(90)  # We have rotated page, which is stored in memory only yet.
    writer = PyPDF2.PdfFileWriter()  # To write in the pdf file
    writer.addPage(page)  # To add the rotated page
    with open('tilt.pdf', 'wb') as new_file:  # Another with open to create a pdf of that rotated page.
        writer.write(new_file)  # This will create a new rotated pdf

# PdfReadWarning: PdfFileReader stream/file object is not in binary mode. It may not be read correctly.
# We are getting this error. So, we need to change it in binary format first and to do that,
# we simply have to write 'rb' instead of 'r'. rb means read binary.
