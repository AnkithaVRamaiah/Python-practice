import os

folders = input("give folder names with spaces in between: ").split() # taking input from user 

for folder in folders:

    try:
      files = os.listdir(folder)
      print("=========== Listing files in folder - " + folder)
    except FileNotFoundError:
       print("please provide valid folder name, looks like the folder does not exist - " + folder)
       break

    for file in folder:
        print(file)

