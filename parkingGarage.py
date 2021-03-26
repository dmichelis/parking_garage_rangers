class Parking_Garage:
    def __init__(self,parkingSpace,tickets,currentTicket):
        self.parkingSpaceAvail = 10
        self.ticketsAvail = 10
        self.currentTicket = currentTicket

    def takeTicket(self):
        # num_tickets = 0
        num_tickets_needed = int(input("How many tickets do you want? "))
   
        if num_tickets_needed > 0:
            self.ticketsAvail -= num_tickets_needed
            self.parkingSpaceAvail -= num_tickets_needed
            print(f"Tickets Remaining: {self.ticketsAvail}")
            print(f"Parking Spaces Remaining: {self.parkingSpaceAvail}")

        # if num_tickets_needed == isinstance(num_tickets_needed, str):
        #     print("Please enter a number using a number pad.")
        
        if num_tickets_needed < 0:
            print("Please enter a positive number.")       




parkingToday = Parking_Garage(10,10,10)

def run():
    while True:
        park_today = input("Welcome to ABC Parking! Would you like to park here today (yes or no)? ")

        if park_today.lower() == 'yes':
            parkingToday.takeTicket()
        

        if park_today.lower() == 'no':
            print('goodbye')
        break

run()