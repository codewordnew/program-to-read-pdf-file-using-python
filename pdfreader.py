import PyPDF2 #Import the 'pyPdf2' module for working with PDF files.
import os # Import the 'os' module for interaction with the operating system.

def reader(filename, road_from_which_page_number=0,startfille=True):
    #check if the 'startfile' flag is set to true ,and if so, open the PDF file using the default viewer.
    if startfile == True:

      os.startfile(filename)

      #Open the Pdf file in binary mode for reading.
      book = open(filename,"rb")

      #Create a Pdf file Reader object to read the Pdf file.
      pdf_reader = pyPDF2.PdfFileReader(book)

      #Get the total number of page in the PDF.
      Pages = pdf_reader.getNumPages()
      print("Number of Pages = ",pages) #Print the number of pages in the PDF.

      #Get the specified page using the provided 'read_from_which_pages-number'.
      page = pdf_reader.getPage(read_from_which_page_number)

      #Extract text from the selected page.
      text = page.extract_text()

      #close the opened PDF file.
      book.close()

      #Return the extracted text from the specified page.
      return text
    
reader(r"biodegredable solvents.pdf")
    
    