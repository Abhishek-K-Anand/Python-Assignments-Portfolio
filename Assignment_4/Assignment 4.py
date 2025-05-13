try:
    file1 = open('sample.txt','r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print('''Error: The "sample.txt" is doesn't exist''')

print("==================================================================================")

text = input("Enter the text: ")

file2 = open("output.txt","w")
writing_txt = file2.write(text + "\n")
file2.close()

additional_text = input("Enter the text: ")
file2 = open("output.txt","a")
appending_txt = file2.write( additional_text + "\n" )
file2.close()

file2 =open("output.txt",'r')
reading_file = file2.read()
print("\nFinal content of output.txt:")
print(reading_file)
file2.close()


