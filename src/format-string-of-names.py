# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas 
# except for the last two names, which should be separated by an ampersand.
# Example:

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''

# Format a string of names like 'Bart, Lisa & Maggie'.

# large version
# def namelist(names):
#     str_arr = []
#     string = ""
   
 
#     if not names:
#         return string
#     elif (len(names) == 1):
#         string = [name[value] for name in names for value in name]
#         return "".join(string)
#     else:
#         for name in names:
#             for value in name:
#                 str_arr.append(name[value])
    
#         last_element_index = len(str_arr) - 1
#         last_element = str_arr[last_element_index]
#         str_arr.remove(last_element)
    
#         string = ", ".join(str_arr) + " & " + last_element
    
#         return string

# refactor version
def namelist(names):
    string_result = ''
    
    if not names: return string_result
    elif len(names)==1: 
        string_result = names[0]['name']
        return string_result
    else:
        string_result = ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
        return string_result
    
 

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])) #'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])) #'Bart, Lisa & Maggie', "Must work with many names")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}])) #'Bart & Lisa', "Must work with two names")
print(namelist([{'name': 'Bart'}]))
print(namelist([])) #'', "Must work with no names")
