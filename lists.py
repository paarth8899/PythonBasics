# # what is a list?
# # A list in python is an ordered, mutable and indexed collection that allow duplicates. 
# # it is writeen in square brackets[].
# # can stored mixed data type like: int float string etc.

# my_list=[10,20,30,40,50,"Parth"]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])          #not the correct way to do.
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# # updating elements
# my_list[5]="SpiderMan"
# print(my_list)
# #Appending elements
# my_list.append("append")
# print(my_list)

# # inserting elements
# my_list.insert(2,"vishal")
# print(my_list)

# #removing elements
# my_list.remove(40)
# print(my_list)

# #for telling the length
# print(len(my_list))

# nums=[5,3,2,1,9,10,11,15,17]
# nums.sort()
# # print("The list  in ascending order is ",nums.sort())
# print("The list  in ascending order is ",nums)
# nums.sort(reverse=True)
# print("the list in descending order is ",nums)

# nums.reverse()
# print(nums)

# nums=[5,3,2,1,9,10,15,17]
# print(nums[0:6:2])

# def second_largest(nums):
#   a=list(set(nums))
#   a.sort()
#   if len(a)<2:
#     return None
#   return a[-2]

# nums=[10,20,4,45,99,20,34,78]

# print("second largest is:", second_largest(nums))

# def reverse_list(ist):
#   return ist[::-1]
# nums=[1,2,3,4,5]
# print("Reversed is ",reverse_list(nums))


# def findpairs(ist,target):
#   pairs=[]
#   for i  in range(len(ist)):
#     for j in range(i+1,len(ist)):
#       if ist[i]+ist[j]==target:
#         pairs.append((ist[i],ist[j]))
#   return pairs
      
# nums=[1,5,7,-1,5]
# target=6
# print("Pairs with sum",target," ",findpairs(nums,target))