from read import reading
import datetime
class writing:
    #generates bill in the terminal for renting land
    def generate_bill(customer_name, kitta_number, duration, city, direction, rate, anna):
        # Calculate total amount
        total_amount = duration * int(rate)
        #calculate the final sum
        final=total_amount

        # Create the bill structure
        bill_content = f"--------------------------- Land Rental Bill ----------------------\n"
        bill_content += f"Customer Name: {customer_name:<10}        Kitta Number: {kitta_number}\n"
        bill_content += f"City: {city:<10}                          Direction: {direction}      \n"
        bill_content += f"Duration of Rent: {duration:<3} months   Rent Charge per month: Rs. {rate}\n"
        bill_content += f"Total Amount: Rs. {total_amount:<8}\n"
        bill_content += f"                Final Sum: Rs. {final}      \n"

        # Prints the bill in the terminal
        print(bill_content)

    #writes land information to a file
    def write_land_info(landonrent, land_info):
        try:
            with open(landonrent, 'w') as file:
                for land in land_info:
                    line = ','.join(land) + '\n'
                    file.write(line)
            print("Information added to file.")
        except IOError:
            #Executes if there is an error writing to the file.
            print("Unable to write.")  