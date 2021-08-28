#19011
#Write a program to check if  given String is a palindrome

def main():
    str1=input("Enter the string: ")
    check(str1)
               
def check(str1):
    if (str1 == str1[::-1]):
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindrome")


if __name__ == '__main__':
        main()


'''
OUTPUT:
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\palindrome.py
Enter the string: mam
Yes, it's a palindrome
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\palindrome.py
Enter the string: malayalam
Yes, it's a palindrome
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\palindrome.py
Enter the string: harry
No, it's not a palindrome
>>> 
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\palindrome.py
Enter the string: hogwarts
No, it's not a palindrome
'''
