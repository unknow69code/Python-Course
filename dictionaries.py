# Creating a dictionary.
__Price_Books = {
"Name": "Book",
"quantity": 3,
"price": 4.99
}
print(__Price_Books)

# Creating a dictionary.
__persons = {
    "Firstname" : "Jose\n",
    "Age" : 19
}

# Printing the type of the variable.
#print(type(__persons))

# Printing the keys of the dictionary.
print(__persons.keys())

# Printing the items in the dictionary.
print(__persons.items())

__persons.clear()
print(__persons)

# Creating a list of dictionaries.
products = [
    {"Name" : "Book", "price" : 10.99},
    {"Name" : "laptop", "Price" : 1000}
]
print(products)