#this def is for reading the file contents, cause i was working from an online editoe
def read_columns_from_file(file_name):
    col1 = []
    col2 = []
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into two numbers and append to respective columns
            num1, num2 = map(int, line.strip().split())
            col1.append(num1)
            col2.append(num2)
    return col1, col2

#this def is for solving the 1s quiz
def find_minimum_distance(a,b):
    new_a=[]
    new_b=[]
    distancet=[]
    distance = 0
    for i in range(len(a)):
        minimuma=min(a)
        new_a.append(minimuma)
        a.remove(min(a))
    for j in range(len(b)):
        minimumb=min(b)
        new_b.append(minimumb)
        b.remove(min(b))
    lentables=max(len(new_a),len(new_b))
    for i in range(lentables):
        if i>=len(new_a):distancet.append(abs(0-new_b[i]))
        elif i>=len(new_b):distancet.append(abs(new_a[i]-0))
        else: distancet.append(abs(new_a[i]-new_b[i]))
    for i in distancet: distance+=i
    return distance


file_name="file.txt"
column1, column2=read_columns_from_file(file_name)
print(find_minimum_distance(column1,column2))
