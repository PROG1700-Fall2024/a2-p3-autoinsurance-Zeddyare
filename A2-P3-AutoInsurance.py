#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #: 0433704
#Student Name: Zachary Rudolf

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Variable initialize
    sex=""
    price=0.0
    age=0
    rate=0.0
    monthlyPay=0.0
    months=12
    #Welcome message
    print("Welcome to Scooter's Insurance!\n")
    #Input for vehicle price, sex, and age
    sex=input("Are you 'Male' or 'Female'?: ").lower()
    age=int(input("\nEnter your age: "))
    price=float(input("\nEnter the purchase price of the vehicle: $"))
    #if statements to find rate based on inputs
    if sex=="male" or sex=="m":
        if age >=15 and age <25:
            rate=0.25
        elif age >=25 and age <40:
            rate=0.17
        elif age >=40 and age <70:
            rate=0.10
    elif sex=="female" or sex=="f":
        if age >=15 and age <25:
            rate=0.20
        elif age >=25 and age <40:
            rate=0.15
        elif age >=40 and age <70:
            rate=0.10
    else: 
        print("No charge for those outside the binary.") 
    monthlyPay=(price*rate)/months
    #print output for final price
    print("\nYour monthly insurance will be: ${0:,.2f}".format(monthlyPay))
    # YOUR CODE ENDS HERE

main()