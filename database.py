import json
import os
from models import Employee

EMPLOYEES_FILE = os.path.join(os.path.dirname(__file__), "employees.json")

def load_employees(): # type: ignore
    """Load all employees from JSON file"""
    if os.path.exists(EMPLOYEES_FILE):
        try:
            with open(EMPLOYEES_FILE, "r") as f:
                data = json.load(f)
                return data if data else []  # type: ignore #if the json file contains data return it, if empty return empty list
        except json.JSONDecodeError:          #if file is broken or cannot be read, handle error instead of crashing
            return []                #if json is invalid, return empty list safely.
    return []               #if the file does not exist, return an empty list

def save_employee(emp: Employee):
    """Save employee to JSON file"""
    employees = load_employees() # type: ignore

    emp_dict = emp.model_dump()
    emp_dict["employee_id"] = str(emp_dict["employee_id"])      #convert to str bcoz json cannot store UUID objects directly.
    emp_dict["date_of_birth"] = str(emp_dict["date_of_birth"])  #convert to str bcoz json cannot store date objects directly.

    employees.append(emp_dict)   #add employee to existing data

    with open(EMPLOYEES_FILE, "w") as f:
        json.dump(employees, f, indent=2)   #overwrites json file or creates it if does not exist

    print(f"✅ Employee saved to {EMPLOYEES_FILE}")