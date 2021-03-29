class Parking_Garage:
    """Initialize Attributes for class Parking_Garage"""
    def __init__(self,parkingSpaceAvail,ticketsAvail,currentTicket):
        self.parkingSpaceAvail = [i for i in range(1,11)]
        self.ticketsAvail = [i for i in range(1,11)]
        self.currentTicket = {}


    def takeTicket(self):
        """
            takeTicket(self) Method/Function 
            When a ticket is distributed:
            item(0) is popped from self.ticketsAvail (range 1, 11) for 10 total tickets (decreases ticketsAvail by 1 until list is empty)
            
            item(0) is popped from self.parkingSpaceAvail (range 1,11) for 10 total spaces (decreases parkingSpaceAvail by 1 until list is  empty)
        """
   
      
        # Provide ticket as long as self.ticketsAvail list is not empty
        if self.ticketsAvail != []:
            # Store popped ticket in a variable
            last_ticket_popped = self.ticketsAvail.pop(0)
            
            # Store popped parking space in a variable
            last_space_popped = self.parkingSpaceAvail.pop(0)
            
            print(f'Please take your ticket {last_ticket_popped}')
            self.currentTicket[last_ticket_popped] = ""
            
            
            print(f"\nTickets Available: {self.ticketsAvail}")
            print(f"\nSpaces Available: {self.parkingSpaceAvail}")
            
            print(f"\nTicket Status: {self.currentTicket}")

        
        # If self.ticketsAvail list is empty, say that garage is full
        else:
            print("Sorry, the parking garage is full.")   
    

    def payForParking(self):
        """
            Ask user to input ticket number and store in variable ticket_num
            Ask user to input payment amount and store in variable payment_amt

            If paid (payment_amt is not empty)-tell user to exit garage within 15 minutes

            Update currentTicket dictionary to Paid
        """

        # Define ticket_num and payment_num as global variables to use outside of this method/function
        global ticket_num
        global payment_amt


        # Store user input for ticket_num and payment_amt in variables
        ticket_num = int(input("Please enter your ticket number: "))
        payment_amt = input("Type any letter to pay. ")
        

        # If payment_amt variable is not empty, print msg to exit and
        # also use the ticket_num variable to update currentTicket dictionary
        if payment_amt != "":
            print("Your ticket has been paid. Please exit the parking garage within the next 15 minutes.")
            self.currentTicket[ticket_num] = 'paid'

        else:
            self.currentTicket[ticket_num] = 'not paid'

            # for key, value in self.currentTicket.items():
            #     if value == 'paid':
            #         del self.currentTicket[key]
            #         break


        print(f"\nCurrent Status of Tickets: {self.currentTicket}")


    def leaveGarage(self):
        """
            leaveGarage method/function checks to see if ticket has been paid.
            If paid, says "Thank you, have a nice day."
            If unpaid, prompts for payment, then "Thank you, have a nice day."
            Update ticketsAvail list to increase by 1 (ticket is avail again)
            Update parkingSpace list to increase by 1 (space is avail again)
            Removes ticket k/v from currentTicket dictionary once paid
        """
        global ticket_num2

        ticket_num2 = int(input("Please enter your ticket number: "))
        if self.currentTicket[ticket_num2] == 'paid':
            self.parkingSpaceAvail.append(ticket_num2)
            self.ticketsAvail.append(ticket_num2)
            print("Thank you, have a nice day!")


            print(f"\nTickets Available: {self.ticketsAvail}")
            print(f"\nSpaces Available: {self.parkingSpaceAvail}")
            print(self.currentTicket)


        if self.currentTicket[ticket_num2] != 'paid':
            payment_amt2 = input("Type any letter to pay. ")
            if payment_amt2 != "":
                self.currentTicket[ticket_num2] = 'paid'
                self.parkingSpaceAvail.append(ticket_num2)
                self.ticketsAvail.append(ticket_num2)
                print("Thank you, have a nice day!")

        for key, value in list(self.currentTicket.items()):
            if value == 'paid':
                del self.currentTicket[key]
                print(f"\nTickets Available: {self.ticketsAvail}")
                print(f"\nSpaces Available: {self.parkingSpaceAvail}")
                print(f"\nTicket Status: {self.currentTicket}")
                break

                      
            print(f"\nTickets Available: {self.ticketsAvail}")
            print(f"\nSpaces Available: {self.parkingSpaceAvail}")
            print(f"\nTicket Status: {self.currentTicket}")


parkingToday = Parking_Garage(10,10,10)

def run():
    while True:
        park_today = input("Welcome to ABC Parking! Do you need to Park, Pay, or Finish? (or type stop to stop this program) ")
        
        if park_today.lower() == 'stop':
            print("Program has been stopped. Goodbye!")
            break

        elif park_today.lower() == 'park':
            parkingToday.takeTicket()
   
        elif park_today.lower() == 'pay':
            parkingToday.payForParking()
            # break

        elif park_today.lower() == 'finish':
            parkingToday.leaveGarage()
  


run()