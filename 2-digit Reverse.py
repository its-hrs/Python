#19011
#Write a function that takes a number with two or more digits as an input and finds its reverse and sum of its digits

def main():
    num=int(input("Enter a two or more digit number: "))
    find(num)

def find(num):
    rev=0
    dsum=0
    val=num
    while(val>0):
        x=val%10
        dsum= dsum+x                                  #dsum for sum of digits
        rev= rev*10+x                                 #rev for storing reverse of the number  
        val= val//10
    print("Reverse of ",num, " is: ",rev)    
    print("Sum of digits of ",num," is: ",dsum) 

if __name__ == '__main__':
    main()
        
#Output:

'''
Enter a two or more digit number: 561
Reverse of  561  is:  165
Sum of digits of  561  is:  12
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\A18_19011.py
Enter a two or more digit number: 942
Reverse of  942  is:  249
Sum of digits of  942  is:  15

'''
