#Write a python program that prints a right triangle or a inverted triangle pattern
#19011

def main():
    print("1)Right Triangle pattern \n2)Inverted Triangle")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        draw1()
    elif(choice==2):
        draw2()
    else:
        print("Wrong Choice Entered!")

def draw1():
    print("\t\t\tRIGHT TRIANGLE PATTERN\t\t\t")
    rows=int(input("Enter the number of rows:" ))
    for i in range(1,rows+1):
         print("*"*i)
    print()     # printing new line

def draw2():
    print("\t\t\tINVERTED TRIANGLE PATTERN\t\t\t")
    rows=int(input("Enter the number of rows:" ))
    nspaces=0
    nstar= 2*rows-1
    for i in range(1,rows+1):
        print(" "*nspaces + '*'*nstar)
        nstar-=2
        nspaces+=1

        
if __name__ == '__main__':
    main()
