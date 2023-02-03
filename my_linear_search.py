def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            print("Target found at index :",i)
        else:
            print("Target not found")

numbers=[2,3,4,5,6,7,8,9,10]  
linear_search(numbers,8)         
        