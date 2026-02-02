
book = [
    {
        "title":"Ward D",
        "writer": "Freida McFadden"
    }, 
    {
        "title": "Harry Potter2",
        "writer": "J.K.Rowling"
    },
    {
        "title": "Eichmann in Jerusalem",
        "writer": "Hannah Arendt"
    },
    { 
        "title": "Harry Potter3",
        "writer": "J.K.Rowling"
    }
]
def Find_writer(writer_name,book):
    count = 0 
    for i in book:
        if i["writer"] == writer_name:
            print(i["title"])
            count +=1
    return count

def Add_book(new_title, new_writer):
    New_book = {
        "title" : new_title,
        "writer" : new_writer
    }
    return New_book
    

Menu_show = print("1.See all information\n2. See the books\n3.See writers\n4. Find books by their writers\n5. Add new book")
Menu = int(input("Please Choose the option (just number)"))

if Menu == 1:
    print(book)    
elif Menu == 2:
    for books in book:
        print (books["title"])
elif Menu == 3:
    for writers in book:
        print(writers["writer"])
elif Menu == 4:
    Writer_name = input("Please write the Writer.")
    count = Find_writer(Writer_name,book)
    print(F"{count} found!")
elif Menu == 5:
    new_title = input("Write the title.")
    new_writer = input("Write the writer.")
    New_book = Add_book(new_title,new_writer)
    book.append(New_book)
    print(book)
    print("Success!")
    
else:
    print("The number is not valid")
        
