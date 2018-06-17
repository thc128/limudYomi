from PyPDF2 import PdfFileWriter, PdfFileReader
import daily_learn

def read_book(path):
    input1 = PdfFileReader(open(path, "rb"))
    my_book=[]
    for i in xrange(input1.getNumPages()):
        my_book.append(input1.getPage(i))
    return my_book

def write_files(output_file,folder,name):
    j=0
    output = []
    for wok in output_file:
        output.append(PdfFileWriter())
        for day in wok:
            for page in day:
                output[j].addPage(page)
        outputStream = file(folder + "\\" + str(j) + name, "wb")
        output[j].write(outputStream)
        j = j + 1

book1=read_book("korban.pdf")
book2=read_book("har_habait.pdf")
book1_split=daily_learn.split_book(book1,2,5)
book2_split=daily_learn.split_book(book2,1,5)
my_file = daily_learn.merge_books([book1_split,book2_split])
write_files(my_file,'split','torah.pdf')
