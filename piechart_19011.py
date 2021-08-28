#19011
#HARSH SAXENA
#Write a program that makes use of a function to accept a list of values and labels and displays a pie chart

from matplotlib import pyplot as plt 
import numpy as np 
  
def enter():
    Label =[]
    values= []
    
    n= int(input("Enter the number of elements in Label list: "))
    print("Now enter the elements of the Label List: ")
    for i in range (0,n):
        Label.append(input())
    print("Entered Label List is: ",Label)

    print("\nNow enter the elements of the Values List: ")
    for i in range (0,n):
        values.append(input())
    print("Entered Values List is: ",values)
    
    fig = plt.figure(figsize =(10, 7))
    plt.pie(values, labels = Label )
    plt.show()

def main():
    enter()
    
if __name__ == '__main__':
    main()

'''
OUTPUT:
>>> 
= RESTART: C:/Users/shiv/AppData/Local/Programs/Python/Python38-32/piechart_19011.py
Enter the number of elements in Label list: 5
Now enter the elements of the Label List: 
INR
DOLLAR
YUAN
EURO
DIRAN
Entered Label List is:  ['INR', 'DOLLAR', 'YUAN', 'EURO', 'DIRAN']

Now enter the elements of the Values List: 
35
20
15
20
10
Entered Values List is:  ['35', '20', '15', '20', '10']
>>>
'''
    
