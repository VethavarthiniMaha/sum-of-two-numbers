items=[]
 keyword="stop"
 print(f"Enter Value (type'{keyword}'to finish):")
  while True:
    user_input=input("Enter the value:")
 if user_input.lower()==keyword:
       break
   items.append(user_input)
 result_tuple=tuple(items)
 print("Final tuple:",result_tuple)
