employee={"lenin":"present","stalin":"absent", "mao":"present", "gandhi":"present", "mandela":"absent"}
def attendance():
    for employee_name, status in employee.items():
        if status == "absent":
            print(employee_name)
        else:
            print(employee_name, "is present")
attendance()