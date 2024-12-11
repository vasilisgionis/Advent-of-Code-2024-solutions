def read_rows_as_lists(file_name):
    rows = []
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line by spaces and convert each element to an integer
            row = list(map(int, line.strip().split()))
            rows.append(row)
    return rows

# Example usage
file_name = 'exaple.txt'  # Replace with your actual file name
rows_as_lists = read_rows_as_lists(file_name)

safe=0
for row in rows_as_lists:
    print(row)
    ascension=0
    decrease=0
    unsafe= False
    for j in range(len(row)-1):
        if row[j]<=row[j+1]:
            ascension+=1 
        elif row[j]>=row[j+1]:
            decrease+=1 
    if ((ascension!=(len(row)-1)) and (decrease!=(len(row)-1))):
        unsafe=True
        print("unsafe" ,ascension, decrease, len(row)-1)
    else :
        distance=0
        j=0
        while(unsafe!=True)and(j<(len(row)-1)):
            distance=abs(row[j]-row[j+1])
            if ((distance>3)or(distance==0)):
                unsafe=True
            j+=1 
    if unsafe==False:
        safe+=1 
print(safe)
    
