#19011
#HARSH SAXENA
#Menu-Driven program of Searching and Sorting

def lsearch(lst,x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1


def bsearch(lst,x):
    low = 0
    high = (len(lst) - 1)
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        if lst[mid] < x: 
            low = mid + 1
  
        # If x is greater, ignore left half 
        elif lst[mid] > x: 
            high = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
  
    return -1


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]  
        j = i-1
        while j >=0 and key < lst[j]:
            lst[j+1] = lst[j] 
            j -= 1
        lst[j+1] = key
        print("The List after ",i,"th iteration is: ")
        print(lst)
    print ("\n------Final Sorted List is:-------- ")
    print(lst)


def s_sort(lst):
    l=len(lst)
    for i in range(l):
        print("Value of i ",i)
        for j in range(i+1,l):
            if lst[i]> lst[j] :
                lst[i],lst[j]=lst[j],lst[i]
        print("The List after ",i,"th iteration is: ")
        print(lst)
                
    print("\n-------Final Sorted List is:-------- ")
    print(lst)


def b_sort(lst):
    l=len(lst)
  
    for i in range(l-1):
        for j in range(0, l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print("List after ",i+1
              ,"th iteration: ",lst)
        
    print("\n-------Final Sorted List is:-------- ")
    print(lst)


def main():
    choice=999
    while(choice!=6):
        lst=[]
        n=int(input("\nEnter the number of elements: "))
        print("Enter the elements: ")
        for i in range(0,n):
            val=input()
            lst.append(val)
        print("Entered list is: ",lst)
        print("\n\t\t**MENU**\t\t\n")
        print("1.) Linear Search")
        print("2.) Binary Search")
        print("3.) Insertion Sort")
        print("4.) Selection Sort")
        print("5.) Bubble Sort")
        print("6.) Quit") 
    
        choice = int(input("Enter your choice: "))
                   
        if(choice== 1):
            key=input("Enter the name you want to search: ")
            res = lsearch(lst,key)
            if(res<0):
                print(key," not found in list !!")
            else:
                print(key," found at index ",res)

        elif(choice== 2):
            key=input("Enter the name you want to search: ")
            lst.sort()
            print("\nFor Bianry search Entered List must be Sorted")
            print("Sorted List is: ",lst)
            res = bsearch(lst,key)
            if(res<0):
                print(key," not found in list !!")
            else:
                print(key," found at index ",res)

        elif(choice== 3):
            insertion_sort(lst)

        elif(choice== 4):
            s_sort(lst)

        elif(choice== 5):
            b_sort(lst)

        else:
            print("EXITING...")


if __name__ == '__main__':
    main()        

'''
OUTPUT:
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\19011_SearcMenuDriven.py

Enter the number of elements: 6
Enter the elements: 
f
d
e
c
b
a
Entered list is:  ['f', 'd', 'e', 'c', 'b', 'a']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 1
Enter the name you want to search: b
b  found at index  4

Enter the number of elements: 5
Enter the elements: 
5
4
3
2
1
Entered list is:  ['5', '4', '3', '2', '1']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 2
Enter the name you want to search: 2

For Bianry search Entered List must be Sorted
Sorted List is:  ['1', '2', '3', '4', '5']
2  found at index  1

Enter the number of elements: 5
Enter the elements: 
4
1
3
0
2
Entered list is:  ['4', '1', '3', '0', '2']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 3
The List after  1 th iteration is: 
['1', '4', '3', '0', '2']
The List after  2 th iteration is: 
['1', '3', '4', '0', '2']
The List after  3 th iteration is: 
['0', '1', '3', '4', '2']
The List after  4 th iteration is: 
['0', '1', '2', '3', '4']

------Final Sorted List is:-------- 
['0', '1', '2', '3', '4']
Enter the number of elements: 5
Enter the elements: 
5
4
3
2
1
Entered list is:  ['5', '4', '3', '2', '1']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 4
Value of i  0
The List after  0 th iteration is: 
['1', '5', '4', '3', '2']
Value of i  1
The List after  1 th iteration is: 
['1', '2', '5', '4', '3']
Value of i  2
The List after  2 th iteration is: 
['1', '2', '3', '5', '4']
Value of i  3
The List after  3 th iteration is: 
['1', '2', '3', '4', '5']
Value of i  4
The List after  4 th iteration is: 
['1', '2', '3', '4', '5']

-------Final Sorted List is:-------- 
['1', '2', '3', '4', '5']

Enter the number of elements: 6
Enter the elements: 
6
2
3
1
5
4
Entered list is:  ['6', '2', '3', '1', '5', '4']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 5
List after  1 th iteration:  ['2', '3', '1', '5', '4', '6']
List after  2 th iteration:  ['2', '1', '3', '4', '5', '6']
List after  3 th iteration:  ['1', '2', '3', '4', '5', '6']
List after  4 th iteration:  ['1', '2', '3', '4', '5', '6']
List after  5 th iteration:  ['1', '2', '3', '4', '5', '6']

-------Final Sorted List is:-------- 
['1', '2', '3', '4', '5', '6']

Enter the number of elements: 5
Enter the elements: 
5
4
3
2
1
Entered list is:  ['5', '4', '3', '2', '1']

		**MENU**		

1.) Linear Search
2.) Binary Search
3.) Insertion Sort
4.) Selection Sort
5.) Bubble Sort
6.) Quit
Enter your choice: 6
EXITING...
>>>
'''
