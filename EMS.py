#Employee Management System!

#Add EMPLOYEE
employees=dict()
def add_emp():
    emp_id= int(input("Employee ID: "))
    if emp_id in employees:
            b=print("Employee ID already exists!")
            return b
    val=dict()
    val['name']=name=input("Employee's name: ")
    val['age']=age=int(input("Employee's age: "))
    val['department']=department=input("Employee's department: ")
    val['salary']=salary=int(input("Employee's monthly salary:"))
    
    

    employees[emp_id] = val 
    print(employees)   
    print("Employee was successfully added.")    


#All EMPLOYEE
def all_emp():  
   for emp_id, value in employees.items():
        print(f"ID: {emp_id}, Name: {value['name']}, Age: {value['age']}, "
                f"Department: {value['department']}, Salary: ${value['salary']}\n")
    
#Search Employee 
def search_emp():
    emp_id = int(input("Enter Employee ID to search: "))
        
    if emp_id in employees:
        print(employees[emp_id])
        value = employees[emp_id]
        print(f"ID: {emp_id}, Name: {value['name']}, Age: {value['age']}, "
            f"Department: {value['department']}, Salary: ${value['salary']}\n")
    else:
        print("Employee not found.\n")

# MAIN MENU

print("......MENU......")
menu=print('''1. Add Employee
2. View All Employees
3. Search for Employee
4. Exit''')
   
choice = input("Choose one of the above option: ")
    
while choice !="4":
    if choice == "1":
        add_emp()
        choice = input("Choose one of the above option: ")
    elif choice == "2":
        all_emp()
        choice = input("Choose one of the above option: ")
    elif choice=="3":
        search_emp()
        choice = input("Choose one of the above option: ")
    elif choice == "4":
        ("Thankyou For Using the Employee Management System!")
    else:
        print("Invalid choice. Please try again.\n")
        
 

