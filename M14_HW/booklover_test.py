from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase): 
        
    def test_1_add_book(self):
        bookName = 'Sapiens'
        test1 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test1.add_book(bookName, 5)
        self.assertTrue(test1.has_read(bookName))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bookName = 'Sapiens'
        test2 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test2.add_book(bookName, 5)
        test2.add_book(bookName, 4)
        self.assertEqual(list(test2.book_list['book_name']).count(bookName), 1)        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bookName = 'Sapiens'
        test3 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test3.add_book(bookName, 5)
        self.assertTrue(test3.has_read(bookName))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bookName = 'Sapiens'
        bookName2 = 'HomoDeus'
        bookName3 = 'Lindt'
        test4 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test4.add_book(bookName, 5)
        test4.add_book(bookName2, 4)
        self.assertFalse(test4.has_read(bookName3))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bookName = 'Sapiens'
        bookName2 = 'HomoDeus'
        bookName3 = 'Lindt'
        test5 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test5.add_book(bookName, 5)
        test5.add_book(bookName2, 4)
        test5.add_book(bookName3, 2)
        self.assertEqual(test5.num_books_read(), 3)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        bookName = 'Sapiens'
        bookName2 = 'HomoDeus'
        bookName3 = 'Lindt'
        test5 = BookLover('Taeyoon', 'rbr6vj@virginia.edu', 'Romance')
        test5.add_book(bookName, 5)
        test5.add_book(bookName2, 4)
        test5.add_book(bookName3, 2)
        # Your test should check that the returned books have rating  > 3
        favBooks = test5.fav_books()
        listRatings = list(favBooks['book_rating'])
        self.assertTrue(all(i > 3 for i in listRatings))
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)