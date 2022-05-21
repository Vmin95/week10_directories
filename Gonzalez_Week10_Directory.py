#Julia Gonzalez
#CIS245
#5/21/22


import os



# ask user for directory

directory = input("Enter dicrectory to save file: ")

# directory defaults to current directory if user presses enter key

if directory == "":

  directory = "."





# ask user for filename

filename = input("Enter filename: ")



# ask for user name, address, and phone number

name = input("Enter name: ")

address = input("Enter address: ")

phone = input("Enter phone number: (XXX)XXX-XXXX)")



# create file object to write to specified file in directory

with open("{}/{}.csv".format(directory, filename), 'w') as file:

  file.write(",".join([name, address, phone]) + "n")



# create file object to read from specified file in directory

with open("{}/{}.csv".format(directory, filename), 'r') as file:

  print("{}/{}.csv contents".format(directory, filename))

  # loop through each line in file and print to screen

  for line in file:

    print(line)