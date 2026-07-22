from models import Employee, Department
from database import save_employee, load_employees
from pydantic import ValidationError

def get_user_input(): # type: ignore
    print("\n" + "="*60)
    print("CREATE NEW EMPLOYEE")
    print("="*60 + "\n")

    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
    salary = input("Enter salary: ").strip()

    print("\nDepartments available:")
    for dept in Department:
        print(f"  - {dept.value}")
    department = input("Enter department: ").strip().upper()

    benefits = input("Has benefits? (yes/no): ").strip().lower() in ["yes", "y", "true"]

    try:
        salary_value = float(salary)
    except ValueError:
        salary_value = -1  # force validation error

    return {
        "name": name,
        "email": email,
        "date_of_birth": dob,
        "salary": salary_value,
        "department": department,
        "benefits": benefits,
    } # type: ignore

def create_employee_from_input():
    try:
        user_data = get_user_input() # type: ignore

        print("\n⏳ Validating data...")
        emp = Employee.model_validate(user_data)

        save_employee(emp)

        print("\n" + "="*60)
        print("EMPLOYEE CREATED SUCCESSFULLY!")
        print("="*60)
        print(f"Employee ID: {emp.employee_id}")
        print(f"Name: {emp.name}")
        print(f"Email: {emp.email}")
        print(f"Department: {emp.department.value}")
        print(f"Salary: {emp.salary}")
        print("="*60 + "\n")

    except ValidationError as e:
        print("\n" + "="*60)
        print(" VALIDATION FAILED!")
        print("="*60)
        for error in e.errors():
            field = error['loc'][0]
            msg = error['msg']
            print(f"  • {field}: {msg}")
        print("="*60 + "\n")
        print("Please try again with correct data.\n")

def view_all_employees():
    employees = load_employees() # type: ignore

    if not employees:
        print("\n No employees saved yet.\n")
        return

    print("\n" + "="*60)
    print(f"ALL EMPLOYEES ({len(employees)})") # type: ignore
    print("="*60 + "\n")

    for i, emp in enumerate(employees, 1): # type: ignore
        print(f"{i}. {emp['name']}")
        print(f"   ID: {emp['employee_id']}")
        print(f"   Email: {emp['email']}")
        print(f"   Department: {emp['department']}")
        print(f"   Salary: {emp['salary']}")
        print(f"   Benefits: {'Yes' if emp['benefits'] else 'No'}")
        print()

    print("="*60 + "\n")