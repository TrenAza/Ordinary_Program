#Attendence Calculator

def attendence(classes,leaves):
    if leaves <= 0:
        print('Attend some classes dumb nigga')
    if leaves > classes:
        print('Bruh the hell')
    
    percentage = (leaves/classes)*100
    return(percentage)
classes = int(input('Total Number of Classes This Year'))
leaves = int(input('Total Number of Leaves Taken This Year'))
Total_percent = attendence(classes,leaves)
