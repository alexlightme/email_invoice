# importing required modules
import PyPDF2
import os
import numpy as np

cwd = os.getcwd()



def get_cuc_bill():
    pdf_folder = "\PDF_testing"
    pdf_file = "\Bill_127061-316292_R.pdf"
    # creating a pdf file object
    pdfFileObj = open(cwd+pdf_folder+pdf_file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.pages.__len__())

    # creating a page object
    pageObj = pdfReader.pages[0]

    # extracting text from page

    test = pageObj.extract_text()
    find_txt = 'Total  Current  Charges'
    start_indx = test.find(find_txt)
    end_indx = start_indx + len(find_txt)


    target = test[start_indx: end_indx +10]
    target = target[target.find('$'): 7 + target.find('$')]
    print(target)

    value = float(target[1:])
    print (value)
    # closing the pdf file object
    pdfFileObj.close()
    return value