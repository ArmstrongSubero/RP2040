import os

# create file
print("Current Directory:", os.getcwd())
print("Opening file")
fp = open("MyFile.txt", "w")
fp.write("Hello")
fp.close()
print("Closing file")

# read created file
print("Open the file and read its contents")
fp = open("MyFile.txt", "r")
str = fp.read(80)
fp.close()
print(str)