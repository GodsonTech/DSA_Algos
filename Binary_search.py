def binary_search(list, item):
  low = 0
  high = len(list)-1 #Getting the length of the list and taking away 1 from the length of list
  
  while low <= high:
     mid = (low + high)
     guess = list[mid] #square bracket to access the middle list element 
    
    if guess == item:
      return mid
    if guess < item:
      low = mid + 1
     else:
      high = mid - 1
   return None 
