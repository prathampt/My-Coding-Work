
import random

ListofPassengers = []
RemainingTickets = [1, 2, 3, 4, 5, 6, 7]
PassangersDictionary = {}


class TrainTicket:

    Train_Name = "Chennai Express"
    
    def __init__(self, passangerName):
        self.passangerName = passangerName

    def Registeration(self):
        print(
            f"Welcome, {self.passangerName} you have regestered successfully...")
        a = RemainingTickets[random.randint(0, len(RemainingTickets) - 1)]
        print("Your ticket number is, ", a)
        RemainingTickets.remove(a)
        ListofPassengers.append(self.passangerName)
        NewDict = {f"Ticket Number {a}": f"Passanger Name {self.passangerName}"}
        PassangersDictionary.update(NewDict)

    def CancelTicket(self):
        b = input("Put the serial number of ticket to be canceled...\n")
        NewDict = {f"Ticket Number {b}": f"Canceled"}
        PassangersDictionary.update(NewDict)

    @staticmethod
    def CheckAvailability():
        print("Number of tickets available are, ", len(RemainingTickets))
        print("Number of Passengers are, ", len(ListofPassengers))




for i in range(1, 8):
    Train1 = TrainTicket(input("Enter your name...\n"))
    Train1.CheckAvailability()
    Reg = input("To Register confirm 'Yes'...\n")
    if Reg == "yes" or Reg == "Yes":
        Train1.Registeration()

print("List of Passangers are...\n", ListofPassengers)
print("Confirmation List is, \n", PassangersDictionary)

Train1.CancelTicket()

print("List of Passangers are...\n", ListofPassengers)
print("Confirmation List is, \n", PassangersDictionary)
