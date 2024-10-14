language = 'python'
language_left = ' python'
language_right = 'python '
languge_left_right = ' python '


print(language)
print(language_left)
print(language_right)
print(languge_left_right)

#now using strip() method  we can see that the output aligns with the original string
language_left_stripped = language_left.lstrip()
language_right_stripped = language_right.rstrip()
languge_left_right_stripped = languge_left_right.strip()

print(language)
print(language_left_stripped)
print(language_right_stripped)
print(languge_left_right_stripped)
print('\n')

text = 'Python'
tab_text = '\tPython'

print(text)
print(tab_text)

#now using strip() method  we can see that the output aligns with the original string
tab_text_stripped = tab_text.strip()
print(tab_text_stripped)