class Parking_Garage:    
    def __init__(self,parkingSpaceAvail,ticketsAvail,currentTicket):
        self.parkingSpaceAvail = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.ticketsAvail = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
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
            #tickets_used.append(last_ticket_popped)
            #spaces_used.append(last_space_popped)

            # currentTicket = dict.fromkeys(str(last_ticket_popped))
            # print(currentTicket)

            # print(*self.ticketsAvail)

            # print(*tickets_used)
            # print(f'Ticket numbers used: {tickets_used}')
            # print(spaces_used)

        else:
            print("Sorry, the parking garage is full.")   

          



    def payForParking(self):
        global ticket_num
        global payment_amt
        ticket_num = int(input("Please enter your ticket number: "))
        payment_amt = int(input("Please enter your payment amount: "))
        

        #if payment_amt == "":
            #self.currentTicket[ticket_num] = 'not paid'
        
        if payment_amt != "":
            print("Your ticket has been paid. Please exit the parking garage within the next 15 minutes.")

        if payment_amt >= 0:
            self.currentTicket[ticket_num] = 'paid'
           

        else:
            self.currentTicket[ticket_num] = 'not paid'

        print(self.currentTicket)
    

    def leaveGarage(self):
        if self.currentTicket[ticket_num] == 'paid':
            self.parkingSpaceAvail.append(ticket_num)
            self.ticketsAvail.append(ticket_num)
            print("Thank you, have a nice day!")


            print(*self.ticketsAvail)
            print(*self.parkingSpaceAvail)
            print(self.currentTicket)
        
        if self.currentTicket[ticket_num] != 'paid':
            ticket_num2 = int(input("Please enter your ticket number: "))
            



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

        elif park_today.lower() == 'finish':
            parkingToday.leaveGarage()

run()

