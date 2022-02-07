my_file =open("people_Exercise.txt","r")
count=0
for i in my_file:
    count=count+1
print(count)
my_file.close()