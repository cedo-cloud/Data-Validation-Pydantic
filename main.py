from services import create_employee_from_input, view_all_employees

def main():
    while True:
        print("\n" + "="*60)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("="*60)
        print("1. Create new employee")
        print("2. View all employees")
        print("3. Exit")
        print("="*60)

        choice = input("\nSelect option (1-3): ").strip()

        if choice == "1":
            create_employee_from_input()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()