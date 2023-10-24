# Banking simulator. Write a code in python that simulates the banking system.
# The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
class Client:
    def __init__(self, client_name, client_surname, client_age, client_balance):
        self.client_name = client_name
        self.client_surname = client_surname
        self.client_age = client_age
        self.client_balance = client_balance

    client_balance = 1000


class Bank:
    def __init__(self, name):
        self.name = name

    client_list = []

    def add_client(self):
        pass

    def deposit(self, client_id, deposit_ammount):
        client_id.balance += deposit_ammount

    def withdraw(self, client_id, withdraw_ammount):
        if Client.client_balance < withdraw_ammount:
            print("not enough money to withdraw")
        else:
            client_id.balance -= withdraw_ammount

    def transfer_balance(self, client1_id, client2_id, transfer_ammount):
        if client1_id.client_balance < transfer_ammount:
            print("not enough money to transfer")
        else:
            client1_id.client_balance -= transfer_ammount
            client2_id.client_balance += transfer_ammount


if __name__ == "__main__":
    Bank("test_bank")
    Client("Test", "Client", 45, 2500)


