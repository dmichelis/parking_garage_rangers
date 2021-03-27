    def __init__(self,parkingSpaceAvail,ticketsAvail,currentTicket):
        self.parkingSpaceAvail = [i for i in range(1,11+1)]
        self.ticketsAvail = [i for i in range(1,11+1)]
        # self.ticketsAvail = [1,2,3,4,5,6,7,8,9,10]
        # self.currentTicket = {'ticket_num': '', 'status': ''}
        self.currentTicket = {
            1 : '',
            2 : '',
            3 : '',
            4 : '',
            5 : '',
            6 : '',
            7 : '',
            8 : '',
            9 : '',
            10: '',
            }



    def takeTicket(self):
        tickets_used = []
        last_ticket_popped = self.ticketsAvail.pop(0)

        spaces_used = []
        last_space_popped = self.parkingSpaceAvail.pop(0)

      

        if self.ticketsAvail != []:

            print(f'Please take your ticket {last_ticket_popped}')
            tickets_used.append(last_ticket_popped)
            spaces_used.append(last_space_popped)

            # currentTicket = dict.fromkeys(str(last_ticket_popped))
            # print(currentTicket)

            # print(*self.ticketsAvail)

            # print(*tickets_used)
            # print(f'Ticket numbers used: {tickets_used}')
            # print(spaces_used)

        else:
            print("Sorry, the parking garage is full.")   

          



    def payForParking(self):
        ticket_num = int(input("Please enter your ticket number: "))
        payment_amt = int(input("Please enter your payment amount: "))
        

        if payment_amt != "":
            print("Your ticket has been paid. Please exit the parking garage within the next 15 minutes.")

        if payment_amt >= 0:
            self.currentTicket[ticket_num] = 'paid'

        else:
            print('Thank you for your business! Please exit the parking garage within the next 15 minutes.')

        print(self.currentTicket)





parkingToday = Parking_Garage(10,10,10)

def run():
    while True:
        park_today = input("Welcome to ABC Parking! Do you need to park or pay? (Type 'park' to park, 'pay' to pay, or 'exit' to stop the program.) ")
        
        if park_today.lower() == 'exit':
            print("Program has been exited. Goodbye!")
            break

        elif park_today.lower() == 'park':
            parkingToday.takeTicket()
 

        elif park_today.lower() == 'pay':
            parkingToday.payForParking()
            # break

run()