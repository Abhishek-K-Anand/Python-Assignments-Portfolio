stu_marks = {'Rama' : 85, 'Aditya' : 78, 'Raj' : 88, 'Shiva' : 95, 'Atul' : 90, 'Manisha' : 70 }

name = input("Enter the name of student : ")

if name in stu_marks:
    print(f'The marks of {name} is {stu_marks[name]}')
else:
    print("Student not found")

print("====================================================================")

my_list = [1,2,3,4,5,6,7,8,9,10]

extracted_list = my_list[0:5]

reversed_list = extracted_list[::-1]

print(f'original_list : {my_list}')
print(f'First five extracted elements : {extracted_list}')
print(f'Reversed extracted elements : {reversed_list}')