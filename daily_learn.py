def split_book(book,book_daily,book_week):
    i = 1
    days = []
    all = []
    for page in book:
        days.append(page)
        if i % book_daily == 0:
            all.append(days)
            days = []
        i = i + 1
    week = []
    weeks = []
    i = 1
    for day in all:
        week.append(day)
        if i % book_week == 0:
            weeks.append(week)
            week = []
        i = i + 1
    return weeks

def merge_books(books):
    my_file = books.pop(0)
    for weeeeek in my_file:
        for book in books:
            if book != []:
                oneweek = book.pop(0)
                for day in oneweek:
                    weeeeek.append(day)
    return my_file
'''
book1=range(100,200)
book2=range(200,300)
book3=range(300,400)
book1_daily=2
book1_week=5

book1_split = split_book(book1,book1_daily,book1_week)
book2_split = split_book(book2,3,7)
book3_split = split_book(book3,3,5)

new_file=merge_books([book1_split,book2_split,book3_split])
for wok in new_file:
    for day in wok:
        print day
    print '===='
'''