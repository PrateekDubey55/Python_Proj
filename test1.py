# name = input("Enter names separated by commas: ").split(',') 
# name = [x.strip().title() for x in name]
# assignment = input("Enter number of assignments done: ").split(',')
# assignment = [x.strip() for x in assignment]
# grade = input("Enter current grade in number out of 100: ").split(',')
# grade = [x.strip() for x in grade]
# for i in range(len(name)):
#     number = 60 - int(assignment[i])
#     grd = int(grade[i])
#     incgrd = 2*number + grd
#     message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#     print(message.format(name[i],number,grd,incgrd))

# record_dictionary = {
#     1: {
#         'Name': 'Prateek',
#         'Age': 21,
#         'Contact': 1234568970
#     }
# }
# print(len(record_dictionary))

f = open('D:\Python_Progs\student_data.txt','r')
print(f)