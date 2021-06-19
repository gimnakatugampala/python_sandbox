# Python has functions for creating, reading, updating, and deleting files.

#Open File
myFile = open('myFile.txt','w')

#Get some info
print('Name :',myFile.name)
print('Is Closed :',myFile.closed)
print('Opening Mode:',myFile.mode)


#Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()


#Append File
myFile = open('myFile.txt','a')
myFile.write(' I also like PHP')
myFile.close()

#Read File
myFile = open('myFile.txt','r+')
text = myFile.read(100)
print(text)
