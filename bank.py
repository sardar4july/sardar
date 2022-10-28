# class Bank_detail:
#     def __init__(self):
#         self.bank_name="SBI"
#         self.IFSC ="SBI10002"
#         self.branch_name="Madhapur"
#         self.manager_name="Karthik"
#
# class Account_details(Bank_detail) :
#     # super().__init__()
#     def __init__(self, name, accno, id, balance):
#         super().__init__()
#         self.balance=balance
#         self.name=name
#         self.id=id
#         self.accno=accno
#
#
#
#
# class Customer(Account_details):
#
#     def bank_details(self):
#         print("Bank Name:",self.bank_name,"\n","Branch Name:",self.branch_name,"\n","IFSC Code:",self.IFSC,"\n","Manager Name:",self.manager_name)
#
#     def withdrawl(self,amuont):
#
#         if self.balance<amuont:
#             print("Dear",self.name,"your account have insufficient funds")
#         else:
#             inittial=self.balance
#             self.balance -= amuont
#             print("Accont holders name:",self.name,"your initial balance is:",inittial,"final amount is:",self.balance)
#     def deposit(self,amount):
#
#         inittial = self.balance
#         self.balance +=amount
#         print("Accont holders name:", self.name, "your initial balance is:", inittial,"final balance is:",self.balance)
#
#
# customer_1=Customer('sardar',100002346,4001,0)
# # customer_1.b_details()
# customer_1.bank_details()
# customer_1.deposit(2000)
# customer_1.withdrawl(1500)
#
# customer_2=Customer('Manoj',100002378,4002,0)
# customer_2.bank_details()
# customer_2.deposit(3000)
# customer_2.withdrawl(2500)












