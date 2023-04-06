def findSmallest(arr):
  smallest = [0] #this is the first index of array
  smallest_index = 0 #this is index of smallest index 
  
  for i in range(1, len(arr)): #iterating through array starting from second number 
    if arr[i] < smallest:
      smallest = arr[i] # this is the smallest value 
      smallest_index = i #index of the smallest value 
    return smallest_index 
  
def selectionSort(arr):
  newArr = [] #new empty array 
  
  for i in range(len(arr)):
    smallest = findSmallest(arr) #smallest calls the findsmallest function on the array
    newArr.append(arr.pop(smallest)) #this removes the smallest from smallest and adds it to the new array
   return newArr

print selectionSort([4, 6, 76, 5, 7, 3, 2, 10])
                 
    
