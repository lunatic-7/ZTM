# Watermark adder (Exercise)

# So, in this one, we have to add wtr.pdf (watermark) in all pages of our super.pdf

import PyPDF2
import sys

water_marker = sys.argv[1]
water_marking = sys.argv[2]

template = PyPDF2.PdfFileReader(open(water_marker, 'rb'))  # Just a short way to open file
watermark = PyPDF2.PdfFileReader(open(water_marking, 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))  # .mergePage is good, while adding watermarks instead PdfFileMerger
    output.addPage(page)
    print('watermarking...')

with open('watermarked.pdf', 'wb') as file:
    output.write(file)

print('watermarked!')
