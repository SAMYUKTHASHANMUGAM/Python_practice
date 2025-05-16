#write function
def write_file():
   try:
       with open("task.txt", "w") as f:
           data = input("Enter text to write: ")
           f.write(data)
           print("File written successfully!!")
   except Exception as e:
       print("Error writing file:", e)

#read function
def read_file():
   try:
       with open("task.txt", "r") as f:
           print("File content:\n", f.read())
   except FileNotFoundError:
       print("File not found!!")
   except Exception as e:
       print("Error reading file:", e)

#append function
def append_file():
   try:
       with open("task.txt", "a") as f:
           data = input("Enter text to append: ")
           f.write("\n" + data)
           print("File appended successfully!!")
   except Exception as e:
       print("Error appending file:", e)

#options

while True:
   print("ENTER THE CHOICE OF FILE HANDLING \n1. Write\n2. Read\n3. Append\n4. Exit")
   choice = input("Enter your choice: ")
   if choice == '1':
       write_file()
   elif choice == '2':
       read_file()
   elif choice == '3':
       append_file()
   elif choice == '4':
       print("Exiting program!!")
       break
   else:
       print("Invalid choice. Try again.")