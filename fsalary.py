basicsalary=int(input("Enter the basic salary\n"))
def salary(basic):
    hra=basic*0.20
    da=basic*0.10
    tax=basic*0.05
    netsalary=basic+hra+da-tax
    print("HRA: ",hra)
    print("DA: ",da)
    print("TAX: ",tax)
    print("The net salary is ",netsalary)
    return netsalary
salary(basicsalary)

  