# Creating the LinearSearch function

def linearSearch(value):
      for i in range(0, len(array)):
            if(array[i] == value):
                  return True
            return False

#main
array = [1,2,3,4,5,,6,7,8,9,10]

num = int(input("Enter number to search in array"))   #input number to search 
linearSearch(num)   #run the function
          
