# ----------------------------------------------------------- #
# Title: Assignment07
# Description: How Pickling and Structured Error Handling Work
# ChangeLog: (Who, When, What)
# Tim Shore, 11.30.2020, Created Script
# ----------------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #

# Pickling

strFileName = 'ToDoFile.dat'
lstToDo = []

# Structured Error Handling

num = ''

# Processing -------------------------------------- #

# Pickle

def save_data_to_file(file_name, list_of_data):
    file = open(file_name, 'ab')
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    file = open(file_name, 'rb')
    list_of_data = pickle.load(file)  # load() only loads one row of data.
    file.close()
    return list_of_data


# Presentation ------------------------------------ #

# Pickle

print('Things to do for Fido')
strTask = str(input('Enter a Task: '))
strPriority = str(input('Daily, Weekly, or Monthly?: '))
strLeash = str(input('Leash or No Leash: '))
lstToDo = [strTask, strPriority, strLeash]

save_data_to_file(strFileName, lstToDo)

print(read_data_from_file(strFileName))

# Structured Error Handling

print('\nDo you know the definition of a whole number?')

try:
    num = int(input('Enter a whole number: '))
except ValueError as e:
    print('That is not a whole number. \nThe programming language says:')
    print(e)