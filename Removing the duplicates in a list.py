 list=input("Enter words:").split()
  print("You entered:",list)
 new_list=[]
 for word in list:
  if word not in new_list:
      new_list.append(word)
 print("After removing the duplicate:",new_list)
