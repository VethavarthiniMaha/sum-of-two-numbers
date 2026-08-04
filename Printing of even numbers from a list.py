nums=list(map(int,input("Enter the numbers:").split()))
  new_list=[]
  for char in nums:
    if char%2==0:
         new_list.append(char)
  print("Even numbers:",new_list)
