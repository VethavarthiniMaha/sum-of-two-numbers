 num=list(map(int,input("Enter the Numbers:").split()))
  start=int(input("Enter the Start Number:"))
 end=int(input("Enter the End Number:"))
 sliced_list=[num[i] for i in range(start,end)]
 odd=[n for n in num if n%2!=0]
 print("Sliced list:",sliced_list)
 print("Odd Numbers:",odd)
