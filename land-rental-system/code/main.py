from read import reading
from write import writing
from operations import rent_land, return_land

def main():
    #prints the logo of the company on top of the shell
    print("\t\t\t |---------------------|")
    print("\t\t\t | TechnoPropertyNepal |")
    print("\t\t\t |---------------------|")
    
    running = True #keeps the program running
    customer_name = None  # Initializing customer name outside the loop
    invoice_generated = False  # Tracking invoice 

    
    while running:
        #menu
        print("Type 1 to rent land.")
        print("Type 2 to return land.")
        print("Type 3 to exit.")
        #catches if string is entered and displays appropriate errormessage
        try:
            useroption = int(input("Enter a value: "))
        except ValueError:
            print("Invalid, enter correct integer.")
            continue
        #enters this loop when 1 is entered
        if useroption == 1:
            #displays the availabe lands in correct format
            lands = reading.display()
            print("Available Lands:")
            print("Kitta no."+" "+"City"+"      "+"Direction"+" "+"Rate"+"    "+"Anna"+"  "+"Availability")
            reading.p(lands)
            while True:
                #catches if string is entered and displays appropriate errormessage also goes to menu if its left empty
                kitta_input = input("Enter kitta number (or leave empty to cancel): ")
                if not kitta_input:
                    print("Canceled rent process.")
                    break
                try:
                    one = int(kitta_input)
                except ValueError:
                    print("Invalid input. Please enter a valid integer for kitta number.")
                    continue
                found = False
                for land in lands:
                    if int(land[0]) == one and land[5] == 'Available': #checks the availability status of the land seleted and only enters the if status when the status is availabe
                        found = True
                        if not invoice_generated:  # Generates invoice if not already generated
                            customer_name = input("Enter your name: ")
                            duration = int(input("Enter the duration of rent (in months): "))
                            city = land[1]#city gets value from land file which has the city value stored in it
                            direction = land[2]
                            rate = land[3]
                            anna = land[4]
                            #calling renting function to execute the renting process
                            rent_land(one, customer_name, duration, city, direction, rate, anna)
                            #generating bill by calling generate_bill function 
                            writing.generate_bill(customer_name, one, duration, city, direction, rate, anna)
                            invoice_generated = True
                        else:
                            duration = int(input("Enter the duration of rent (in months): "))
                            city = land[1]
                            direction = land[2]
                            rate = land[3]
                            anna = land[4]
                            rent_land(one, customer_name, duration, city, direction, rate, anna)
                        break
                if found:
                    rent_more = input("Do you want to rent more land? (yes or no): ")
                    if rent_more.lower() == 'no':
                        break
                    #exits the loop when ni is entered
                else:
                    print("Invalid kitta number or land is not available for rent.")
        elif useroption == 2:
            #calling return_land function to execute returning land
            return_land()
        elif useroption == 3:
            #when option 3 is entered the program is terminated
            running = False
        else:
            print("Enter valid input")

if __name__ == "__main__":
    main()