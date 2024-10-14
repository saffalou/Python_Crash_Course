url = 'https://somewhere.com'

mini_url = url.removeprefix('https://')


print(url)

print(mini_url)

test = ('pre-fix, pre-date, pre-eminent')

#check the ouput. This method removes only the first instance of "pre-"
mini_test = test.removeprefix('pre-')

print(test)
print(mini_test)



# this works without error because the start and end quaotes are single so do not conflict with the double quotes used in the quote
famous_quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
famous_person = 'Albert Einstein'
famous_quote_shortened = 'A person who never made a mistake never tried anything new.'
print(famous_quote)

print(f'{famous_person} once said, "{famous_quote_shortened}"')

filename = 'python_notes.txt'

print(filename.removeprefix('python_'))
print(filename.removesuffix('.txt'))