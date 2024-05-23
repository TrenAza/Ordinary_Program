#Attendence Calculator

def attendence(classes,present):
    if present<= 0:
        print('Attend some classes dumb nigga')
    if present > classes:
        print('Bruh the hell')
    percentage = (present/classes)*100
    return(percentage)
classes = int(input('Total Number of Classes This Year:'))
print()
present = int(input('Total Number of Classes Attended This Year:'))
print()
Total_percent = attendence(classes,present)

print('PERCENTAGE OF CLASSES ATTENDED',Total_percent,'%')
