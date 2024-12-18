#!/usr/bin/python3
paid_employees=[]
def employee(name, hours, rate):
	wage=hours*rate
	emp={"jina":name, "pay":wage}
	paid_employees.append(emp)
	for e in paid_employees:
		print("Employee Name:",e["jina"])
		print("Salary>>", e["pay"])

name=str(input("Enter Name:"))
hours=int(input("Enter Hours worked:"))
rate=int(input("Enter Rate per hour($):"))
employee(name, hours, rate)

