marks=[10,20,30,40,45,50]
for mark in marks[0:5]:
    print(mark)



for i in range(5):
    print(marks[i])


for i in range(len(marks)):
    if marks[i]==40:
        print("40 is found at index",i)