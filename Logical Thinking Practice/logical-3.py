# given number is leap year or not



n=int(input("Enter Year"))


def leapyear(n):
    return(((n%4==0) & (n%100!=0)) or (n%100==0) )



if leapyear(n)==True:
    print("Given Number is a Leap Year")


else:
    print("Given Number is Not a Leap Year")

