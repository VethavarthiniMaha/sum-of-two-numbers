 m1=int(input("Enter the Maths Mark:"))
 m2=int(input("Enter the Science Mark:"))
 m3=int(input("Enter the Tamil Mark:"))
 m4=int(input("Enter the English Mark:"))
 m5=int(input("Enter the Social Mark:"))
 Total=m1+m2+m3+m4+m5
 Percentage=Total/5
  print("Total Mark Obtained:",Total)
  print("Percentage obtained :",Percentage)
  if Percentage>=90:
    print("Your Grade is O")
  elif Percentage>80 and Percentage<=89:
    print("Your Grade is A+")
  elif Percentage>70 and Percentage<=79:
    print("Your Grade is A")
  elif Percentage>60 and Percentage<=69:
    print("Your Grade is B+")
 elif Percentage>55 and Percentage<-59:
   print("Your Grade is B")
  elif Percentage>50 and Percentage<=54:
    print("Your Grade is C")
 else:
   print("REAPPEAR")
