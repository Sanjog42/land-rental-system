import datetime
from read import reading
from write import writing

def rent_land(kitta_number, customer_name, duration, city, direction, rate, anna):
    lands = reading.check()  # Read land data from file

    for land in lands:
        if int(land[0]) == kitta_number and land[5] == "Available":  # Check if land is available
            land[5] = "Not Available"  # Update status to "Not Available"

            # Write updated data back to the file
            writing.write_land_info("landonrent.txt", lands)

            # Calculate total amount
            total_amount = int(land[3]) * duration
            Date = datetime.datetime.now().strftime("%Y-%m-%d")  # Find datetime
            final_sum = total_amount  # Find the final sum

            # Create invoice
            invoice_name = f"Invoice_{customer_name}_{kitta_number}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            invoice_content = f"""
                                TechnoPropertyNepal
______________________________________ Bill______________________________________
|Name: {customer_name:<15}                                 Date:{Date:<14}       |
|________________________________________________________________________________|                              
Kitta Number-{kitta_number:<12}
City-{city:<23}
Direction-{direction:<11}
Area-{anna:<5}
Duration-{duration:<15}
Price-Rs.  {rate:<10}
Total Cost= Rs. {total_amount:<15}               
Overall Total= Rs. {final_sum:<15}    
            """

            with open(invoice_name, 'w') as invoice:
                invoice.write(invoice_content)
            
            print(f"Land with kitta number {kitta_number} has been rented to {customer_name}.")
            print(f"Invoice has been generated as {invoice_name}.")
            return

    print("Invalid kitta number or land is not available for rent.")

def return_land():
    landdat = reading.check()  # Read land data from file
    kitta_number = input("Enter the kitta no of land you want to return:")
    found = False

    for land in landdat:
        if land[0] == kitta_number:
            found = True
            if land[5] == "Available":
                print("Land with that kitta number is not rented yet")
                return
            else:
                customer_name = input("Enter your name:")
                duration = int(input("Enter the duration of time you leased the land for:"))
                return_deadline = int(input("Enter the duration of time during which you are returning the land:"))

                land[5] = "Available"  # Update land availability to "Available"
                
                city = land[1]
                direction = land[2]
                area = land[4]

                exceed_duration = return_deadline - duration
                rent = int(land[3]) * duration
                penalty = calculate_penalty(rent, exceed_duration)

                final_sum = rent + penalty

                writing.write_land_info("landonrent.txt", landdat)

                # Call generate_return_bill from operations
                print(generate_return_bill(kitta_number, customer_name, duration, city, direction, area, exceed_duration, rent, penalty, final_sum))
                return

    if not found:
        print("Land with that kitta number is not found")

def calculate_penalty(rent, exceed_duration):
    if exceed_duration == 1:
        penalty = rent * 1.05
    elif exceed_duration == 2:
        penalty = rent * 2.15
    elif exceed_duration == 3:
        penalty = rent * 3.30
    elif exceed_duration == 4:
        penalty = rent * 4.5
    elif exceed_duration == 5:
        penalty = rent * 5.6
    elif exceed_duration >= 6:
        penalty = rent * 6.75
    else:
        penalty = 0
    return penalty

def generate_return_bill(kitta_number, customer_name, duration, city, direction, area, exceed_duration, rent, penalty, final_sum):
    Date = datetime.datetime.now().strftime("%Y-%m-%d")
    bill = f"""
                                 Techno Property Nepal
    ___________________________________Bill______________________________________
    |Name: {customer_name:<25}                         Date: {Date:<10}         |
    |___________________________________________________________________________|
    Kitta Number - {kitta_number:<15}
    City - {city:<15}
    Direction - {direction:<15}
    Area - {area:<15}
    Duration - {duration:<15}
    Exceeded Duration (months) - {exceed_duration:<18}
    Rent (per month) - Rs. {rent/duration:<10}
    Penalty - Rs. {penalty:<10}
    Overall Total - Rs. {final_sum:<15}
    """
    with open("Return_invoice.txt", "w") as invoice_return:
        invoice_return.write(bill)
    return bill
