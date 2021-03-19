newFile = open("content.txt","a")
newFile.write("Welcome to TKM! \n")
newFile.close()

readFile = open("content.txt","r")
print(readFile.readlines())
readFile.close()
