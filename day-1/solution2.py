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
def sim(a, b):
    flag=0
    similarity_table=[]
    for i in range(len(a)):
        flag=0
        for j in range(len(b)):
            if a[i]==b[j]:
                flag+=1
        similarity_table.append(a[i]*flag)
    similiraty=0
    for i in similarity_table: similiraty+=i
    return similiraty
file_name="file.txt"
column1, column2=read_columns_from_file(file_name)
print(sim(column1,column2))
