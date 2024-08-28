'''
try:
    name= int(input('Enter the number : '))
except Exception as e:
    print(e)


import os

file_path = os.path.join(os.getcwd(),'artifacts','train.csv')

print(os.path.dirname())'''