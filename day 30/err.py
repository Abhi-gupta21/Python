# FileNotFound
# with open("file.txt") as file:
#   file.read()

# KeyError for Dictionaries

# IndexError for Lists

#TypeError when you try to add different datatypes like string and int.

# catching exceptions -

# try: smthng that might cause an exception

# except: do this if there was an exception

# else: do this if there were no exceptions

# finally: do this no matter what happens

try:
    file = open("day 30/file.txt")
    dict = {"key": "value"}
    print(dict["key"])

except FileNotFoundError:
    file = open("day 30/file.txt",'w')
    file.write("something")

except KeyError as error_message:
    print(f"key {error_message} not found")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File is closed")



# raising your own exceptions -
# raise TypeError("This is an error that I made up")
    

# json dara - 
# dictionary type data.
# use inbuilt json library.