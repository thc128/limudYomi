class Mybook(object):
    def __init__(self,book,book_daily,book_week,bookmark=0,redundent=0):
        self.book=book
        self.book_daily=book_daily
        self.book_week=book_week
        self.bookmark=bookmark
        self.redundent=redundent


def refine_book(book,pages,bookmark,redundent):
    for i in xrange(redundent):
        book.pop(0)
    if len(book) == pages:
        return book
    diff = pages/len(book)
    little_diff = len(book) - (pages % len(book))
    new_order=[]
    for i in xrange(bookmark):
        new_order.append(book.pop(0))
    book+=new_order
    if diff != 0:
        book *= (diff+1)
    for i in xrange(little_diff):
        book.pop(-1)
    return book

def split_book(book):
    i = 1
    days = []
    all = []
    for page in book.book:
        days.append(page)
        if i % book.book_daily == 0:
            all.append(days)
            days = []
        i += 1
    week = []
    weeks = []
    i = 1
    for day in all:
        week.append(day)
        if i % book.book_week == 0:
            weeks.append(week)
            week = []
        i = i + 1
    return weeks

def merge_books(books):
    my_books=books[:]
    my_file = my_books.pop(0)
    for weeeeek in my_file:
        for book in my_books:
            if book != []:
                oneweek = book.pop(0)
                for day in oneweek:
                    weeeeek.append(day)
    return my_file


def books_into_weeks(books,weeks_num):
    splitted_books=[]
    for book in books:
        sum_pages = book.book_daily * book.book_week * weeks_num
        book.book=refine_book(book.book, sum_pages,book.bookmark,book.redundent)
        splitted_books.append(split_book(book))
    new_file = merge_books(splitted_books)
    return new_file

'''
book1=range(100,200)
book2=range(200,300)
book3=range(300,400)
book1_daily=2
book1_week=5

book01 = Mybook(book1,book1_daily,book1_week)
book02 = Mybook(book2,3,7,0,3)
book03 = Mybook(book3,3,5,17)

'''
'''
book1_split = split_book(book01,10)
book2_split = split_book(book02,10)
book3_split = split_book(book03,10)

new_file=merge_books([book1_split,book2_split,book3_split])

new_file=book1_split
'''
'''
my_new_file = books_into_weeks([book01,book02,book03],4)
i=1
for wok in my_new_file:
    print i
    for day in wok:
        print day
    print '===='
    i+=1

'''
