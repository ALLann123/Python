#!/usr/bin/python3

def interest(principal, rate, time):
	SI = principal * rate/100 * time
	print("The Simple interest> ", SI)

interest(principal = int(input("Enter the Principal: ")), rate = int(input("Enter Rate: ")), time = int(input("Enter Time: ")))