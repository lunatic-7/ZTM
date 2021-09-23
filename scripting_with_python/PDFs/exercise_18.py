# PDF Merger (Exercise)

import PyPDF2
import sys

files = sys.argv[1:]  # It will take all the arguments following the first.


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()  # To merge files
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')  # To finally write (create) a pdf file. Here, named super.pdf


pdf_combiner(files)
