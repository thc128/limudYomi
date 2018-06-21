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
        outputStream = file(folder + "\\week_" + str(j) + "_" + name, "wb")
        output[j].write(outputStream)
        j = j + 1

book1=read_book("sample1.pdf")
book2=read_book("sample2.pdf")
book3=read_book("sample3.pdf")
my_book1=daily_learn.Mybook(book1,2,5,17)
my_book2=daily_learn.Mybook(book2,1,5,0,2)
my_book3=daily_learn.Mybook(book3,2,7,205)
my_file = daily_learn.books_into_weeks([my_book1,my_book2,my_book3],4)
write_files(my_file,'splitted','my_learning.pdf')
