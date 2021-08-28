#19011

def main():
    
    print("\t\t**MENU**\t\t\
         \na)Find the length of string.\
         \nb)Return maximum of three strings.\
         \nc)Accept a string and replace all vowels with“#”\
         \nd)Find number of words in the given string.\
         \ne)Check whether the string is a palindrome or  not.")
    choice = input("Enter your choice: ")
                   
    if(choice=='a'):
        slen()        
    elif(choice=='b'):
        maxof3()
    elif(choice=='c'):
        replace()
    elif(choice=='d'):
        find()
    elif(choice=='e'):
        palindrome()
    else:
        print("WRONG CHOICE ENTERED!!")
                   

def slen():
    str1 = input("Enter the string: ")
    count=0
    for i in str1:
        count+=1
    print("Length of the given String:", count)

def maxof3():
    str1 = input("Enter the 1st string: ")
    str2 = input("Enter the 2nd string: ")
    str3 = input("Enter the 3rd string: ")
    if(str1>str2):
        if(str1>str3):
            print(str1, "is maximum")
        else:
            print(str3," is maximum")
    elif(str2>str3):
        print(str2,"is Maximum")
       

def replace():
    str1 = input("Enter the string: ")
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')  
    for i in str1: 
        if i in vowels: 
            str1 = str1.replace(i, "#") 
    print("replaced String: ",str1)
                
def find():
    str1 = input("Enter the string: ")
    x = len(str1.split())

    print("Number of Words are: ",x)
                
def palindrome():
    str1 = input("Enter the string: ")
    if (str1 == str1[::-1]):
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindrome")            
    
if __name__ == '__main__':
        main()

'''
OUTPUT:
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: a
Enter the string: Hello how are you
Length of the given String: 17
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: b
Enter the 1st string: Hello
Enter the 2nd string: this 
Enter the 3rd string: hi
this  is Maximum
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: c
Enter the string: Hello How are you
replaced String:  H#ll# H#w #r# y##
>>> 
======================== RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py =======================
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: d
Enter the string: This is Harry Potter
Number of Words are:  4
>>> 
======================== RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py =======================
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: e
Enter the string: Harry
No, it's not a palindrome
======================== RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\MenuDriven_19011.py =======================
		**MENU**		         
a)Find the length of string.         
b)Return maximum of three strings.         
c)Accept a string and replace all vowels with“#”         
d)Find number of words in the given string.         
e)Check whether the string is a palindrome or  not.
Enter your choice: e
Enter the string: mam
Yes, it's a palindrome
'''
