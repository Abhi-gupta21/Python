# you know about it

# docstrings - 

def format_name(fname,lname):
    """take a first name and last name 
    to return the title format of the same"""
    if fname=="" or lname=="":
        return "not a valid input"
    fformat = fname.title()
    lformat = lname.title()
    return f"Result: {fformat} {lformat}"

print(format_name('SAI', 'AbHIshek'))

