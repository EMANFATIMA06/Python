
### Exercise 1: Adding and Accessing Dictionary Elements ###
dictionary_book = {
    "title" : "The Great Gatsby",
	"author" : "F. Scott Fitzgerald",
	"year": 1925
}
#1.	Add a new key "genre" with the value "Fiction"
dictionary_book["genre"] = "Fiction"
print(dictionary_book)

#2.	Update the "year" to 2025
dictionary_book.update({"year" : "2005"})
print(dictionary_book)

#3.	Access and print the value associated with the "author" key
author_value=dictionary_book.get("author")
print(author_value)


### Exercise 2: Removing Elements from a Dictionary ###
movie = {
    "name": "Inception",
    "director": "Christopher Nolan",
    "release_year": 2010,
    "budget": 160000000
}
print(movie)
#1.	Remove the "budget" key using the pop() method and store the removed value in a variable.
movie.pop("budget")
print(movie)
#2.	Delete the "release_year" key using the del keyword
del movie["release_year"]
print(movie)
#3.	Clear the dictionary
movie.clear()
print(movie)


### Exercise 3: Nested Dictionary Manipulation ###
library ={	"book_1": { "title": "1984", "author": "George Orwell", "copies": 10},
	"book_2": { "title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5}
}
print(library)
#1.	Add a third book with "title": "Pride and Prejudice", "author": "Jane Austen", "copies": 7.
library.update({"book3": {"title":"Pride and Prejudice", "author": "Jane Austen", "copies": 7}})
print(library)
#2.	Update the "copies" of "1984" to 15.
library["book_1"]["copies"] = 15
print(library)
#3.	Print the "author" of "To Kill a Mockingbird".
author_value=library["book_2"]["author"]
print(author_value)


### Exercise 4: Looping Through a Dictionary ###
fruits = {	"apple": 50,
	"banana": 30,
	"cherry": 20
}
#1. Use a loop to print each item's name and quantity in the format:
for fruit,value in fruits.items():
    print(f"{fruit}:{value}")


### Exercise 5: Dictionary Comprehension ###
squares ={}
for x in range(1, 11):
    squares[x] = x * x
print(squares)

