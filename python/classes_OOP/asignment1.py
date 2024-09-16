class MyFirstClass:
    # Add a print statement inside it such as “Who wrote this?”.
    print('Who wrote this?')
    
    # Create a string variable named index and initialize it with a string “Author-Book”.
    index = 'Author-Book'
    
    # Define a function called hand_list() with the help of def keyword.\
    # Pass the parameter  self to it. And then pass two parameters, philosopher and book to it. 
    
    def hand_list(self, philosopher, book):
        # print statement using the print() function and pass the class variable by accessing it.
        print(MyFirstClass.index)
        self.philosoper = philosopher
        self.book = book
        
        print(self.philosoper + ' wrote the book: ' + self.book)   
         

whodunnit = MyFirstClass() 

whodunnit.hand_list('Sun Tzu', 'The Art of War')
 