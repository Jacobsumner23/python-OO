class ParkingGarage():
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.parking_spaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25]
        self.active_tickets = {}
    def takeTicket(self):
        total_active_tickets = len(list(self.active_tickets.keys()))
        total_tickets = len(self.tickets)
        if total_active_tickets != total_tickets:
            ticket = self.tickets.pop()
            self.active_tickets[ticket] = ''
            print(f"Welcome your ticket number is {ticket}")

    def payForParking(self):
        ticket_number = int(input("What is your ticket number?:"))
        if ticket_number not in list(self.active_tickets.keys()):
            print("we could not find that ticket number")
        for i in list(self.active_tickets.keys()):
            if i == ticket_number:
                pay_now = input("Ticket found, please pay now by entering payment type; Card or Cash: ")
                if pay_now.lower() == 'Card'or'Cash':
                    self.active_tickets[i] = "Paid"
                    print('Payment succesful, You have 15 minutes to Exit!')

    def leave_garage(self):
        ticket_number = int(input("What's your ticket number?: "))
        if self.active_tickets[ticket_number] == 'Paid':
            self.active_tickets.pop(ticket_number)
            self.tickets.append(ticket_number)
            self.parking_spaces.append(ticket_number)
            print("Thank You, Have a nice day!")
        else:
            print("Please pay for your ticket before exiting")

parking = ParkingGarage()  
def run():
    while True:
        response = input("Would you like to Enter, Exit, Pay, or Quit?: ")
        if response.lower() == 'quit':
            print("Thank you, have a nice day")
            break
        elif response.lower() == 'enter':
            parking.takeTicket()
        elif response.lower() == 'pay':
            parking.payForParking()
        elif response.lower() == 'exit':
            parking.leave_garage()
        else:
            print('Input Error')    
run()