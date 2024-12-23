def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# the above requires that we provide a value for each of the 3 arguments
# what if the person doesn't have a middle name?
# we can make parameters optional
# we set middle_name with default value of empty string and move it to the end of the arguments list
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# note that middle name needs to be passed as last parameter
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# or we can use keyword arguments to add names in order
musician = get_formatted_name(first_name ='john', middle_name = 'lee', last_name ='hooker')
print(musician)

