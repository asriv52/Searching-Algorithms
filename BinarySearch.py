# Creating the BinarySearch funtion

def BinarySearch(target):
      min = 0
      max = len(array) -1
      found = False
      position = -1
      while (found == False and min<=max):
            mid = (max+min)//2

            if array[mid] > target:
                  max = mid -1
            elif array[mid] < target:
                  min = mid +1
            else:
                  position = mid
                  found = True
      if position == -1:
        print("the value is not in array")
      else:  
      print(f"the value is at postion {position}")  
      
#main
array = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Enter number to be found")) #taking an input
BinarySearch(num) #running the function
      
