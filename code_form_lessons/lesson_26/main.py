def bubbleSort(list_data):
  for i in range(len(list_data)):
    print()

    for j in range(0, len(list_data) - i - 1):
      
      if list_data[j] > list_data[j + 1]:
        temp = list_data[j]
        list_data[j] = list_data[j+1]
        list_data[j+1] = temp
        
        print(list_data)


data01 = [-2, 45, 0, 11, -9]
data02 = [-2, 45, 0, 11, -9, 44, 12, -23, 99, 13, 89, -1]

print(data02)
bubbleSort(data02)

print('Sorted list in ascending order:')
print(data02)