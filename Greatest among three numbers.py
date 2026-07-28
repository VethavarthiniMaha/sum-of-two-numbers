 a  = int(input("Enter the Number for A:"))
 b = int(input("Enter the Number for B:"))
 c = int(input("Enter the Number for C:"))
 if a > b and a > c:
    print("The Greatest Number is:", a)
 elif b > c and b > a:
     print("The Greatest number is:", b)
 else:
    print("The Greatest number is:", c)
