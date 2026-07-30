print("Welcome to the Data Analyzer and Transformer Program")
Arrays=[]

def input_data():
    global Arrays
    
    print("1.1D array")
    print("2.2D array")

    select=int(input("Enter a number for array:"))

    if select==1:

        num =list(map(int,input("Enter data for a 1D array(seprated by space):").split()))

        Arrays.append(num)
        print("Data has been stored successfully!")

    elif select==2:

        num = []

        for i in range(3):
            row = list(map(int , input(f"Enter Row {i + 1} : ").split()))

            num.append(row)

            
        Arrays.append(num)
        print("Data has been stored successfully!")
 
    else:
        print("Invalid choice")


def Display_data():
    global Arrays

    
   
    
    print("\nData Summary:")
    print("- Total elements:",len(Arrays[0]))
    print("- Minimum Value:",min(Arrays[0]))
    print("- Maximum Value:",max(Arrays[0]))
    print("- Sum of all Values:",sum(Arrays[0]))
    print("- avarage value:",sum(Arrays[0])/len(Arrays[0]))
    
    

def Cal_fact(n):
    
    #num=int(input("Enter a num:"))
    if n==0 or n==1:
        return 1
    
    fact = n*Cal_fact(n-1)
    num=int(input("Enter a num:"))
    print(f'factorial of {num} is {fact}')
    return fact
#num=int(input("Enter a num:"))
    
print(f'factorial of {num} is {fact}')

def filter_data():
    
    """filter all data using filter."""
    
    value=int(input("Enter a threshold value to filter out data above this value:"))

    numbers=list(filter(lambda x:x >= value,Arrays[0]))
    print(f"Factorial of {value} is : {numbers}")
    print(filter_data.__doc__)
    return numbers
   

def Sort_data():

    print("1. Ascending")
    print("2. Descending")

    choose=int(input("Enter a number for sorting data:"))

    if choose==1:

        print(sorted(Arrays[0]))
    else:
        print(sorted(Arrays[0],reverse=True))
def display_dataset(*args,**kwargs):

    print("Dataset Statistics:")

    Minimum=min(args)
    Maximum=max(args)
    Total=sum(args)
    Average=sum(args)/len(args)
    
    if kwargs.get("show",True):
         
        print("- Minimum value:",Minimum)
        print("- Maximum value:",Maximum)
        print("- Sum of all values:",Total)
        print("- Average value:",Average)

    return Minimum,Maximum,Total,Average

def exit():
    print("Thank you for using the data Analyzer and Transformer")
    print("Program. Goodbye!")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summery(Built-in Functions)")
    print("3. Calculate Factorial(Recurtion)")
    print("4. Filter Data by Threshld(Lamda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics(Return Multiple Values)")
    print("7.Exit Program")

    choice = int(input("Please enter your choice:"))

    if choice==1:
        input_data()
    elif choice==2:
        Display_data()
    elif choice==3:
        #num=int(input("Enter a num for fectorial"))
        Cal_fact(num)
    elif choice==4:
        filter_data()
    elif choice==5:
        Sort_data()
    elif choice==6:
        display_dataset()
    elif choice==7:
        exit()
        break

        
        
    
    
    

    
    

    

        

        
