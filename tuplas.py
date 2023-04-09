# Creating two tuples.
a = (1, 2, 3 , 4, 5)
b = ('Jose', 'Manuel', 'David')

# Creating a tuple with the values 1, 2, 3, 4.5
c = tuple((1, 2, 3, 4.5))
print(c)
# Printing the type of the variable `a`
print(type(a))
# Printing the tuple `a`
print(a)
print(b)
# Deleting the tuple `a` and then printing it.
#del a 
#print(a)


# Creating a dictionary with two keys, each key is a tuple.
locations = {
    (12.3333, 14.5433):"Saman\n",
    (21.2221, 22.44330):"Guasimal"
}
print(locations)