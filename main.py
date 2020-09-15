def mergeSortedArrays(arr1, arr2):
  arr1_length = len(arr1)
  arr2_length = len(arr2)

  if arr1_length == 0:
    return arr2
  if arr2_length == 0:
    return arr1

  mergedArray = [None] * (arr1_length + arr2_length)
  i = 0
  j = 0
  k = 0
  
  while i < arr1_length and j < arr2_length:
    if arr1[i] < arr2[j]:
      mergedArray[k] = arr1[i]
      i += 1
      k += 1
    else:
      mergedArray[k]= arr2[j]
      j += 1
      k += 1
  
  while i < arr1_length:
     mergedArray[k] = arr1[i]
     i += 1
     k += 1

  while j < arr2_length:
     mergedArray[k] = arr2[j]
     j += 1
     k += 1
    

  return mergedArray


v = mergeSortedArrays([0,3,4,31], [3,4,6,30]);
print(v)