list1=[]
FileHandle = open("test.txt", "r")
LineofText = FileHandle.readline()
while len(LineofText) >0:
    list1.append(LineofText)
    LineofText = FileHandle.readline()
    
FileHandle.close()

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        i = 1
        while i < n:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Swap the elements
                swapped = True
            i += 1
bubble_sort(list1)
print(list1)
with open('output.txt', 'w') as file:
    for item in list1:
        file.write(str(item) + '\n')

print(output.txt)
