import json
class User:
    def __init__(self):

        self.List_of_Users = {}
        # As per the Code below, Json file with previous data must exist for error free execution
        # For creation of json file, Dummy detail are given --> The code will Run correctly now.
        UserDetail = {'Full name':'name', 'Phone Number':'p_number', 'Email Id':'email', 'Address':'address', 'Password':'password'}
        self.List_of_Users['Dummy'] = UserDetail
        with open ('List_of_Users.json','w') as f:
            json.dump(self.List_of_Users,f,indent=4)

        self.Select_list={}       
        SDetail = {"Food name": "name", "Quantity": "quantity", "Price": 0, "Discount": 0, "Stock": 0}
        self.Select_list['dummy'] = SDetail
        with open ('Selected_List.json','w') as f:
            json.dump(self.Select_list,f,indent=4)

        self.History_list={}
        HDetail = {"Food name": "name", "Quantity": "quantity", "Price": 0, "Discount": 0, "Stock": 0}
        self.History_list['dummy'] = HDetail
        with open ('History_list.json','w') as f:
            json.dump(self.History_list,f,indent=4)

    def Registeration(self):
        print('-'*20, 'Registeration Page','-'*20)
        self.name = input('Enter Full Name: ')
        self.p_number = (input('Enter Phone Number: '))
        self.email = (input('Enter E-mail Id: '))
        self.address = (input('Enter Address: '))
        self.password = (input('Enter Password: '))
        self.User_detail = {'Full name':self.name, 'Phone Number':self.p_number, 'Email Id':self.email, 'Address':self.address, 'Password':self.password}
        self.User_ID = self.p_number
        self.List_of_Users[self.User_ID] = self.User_detail
        print(self.List_of_Users)
        print('You have Registered successfully!!!')
        '''with open ('List_of_Users.json','r') as f:
            List_of_Users=json.load(f)
            List_of_Users.update(self.List_of_Users)'''
        with open ('List_of_Users.json','r+') as g:
            json.dump(self.List_of_Users, g ,indent=4)
        return self.List_of_Users

    def Login_App(self):
        print('-'*20, 'Log-In Page','-'*20)
        self.Id = input('Enter UserID / Phone Number: ')
        self.Psd = input('Enter Password: ')
        if self.Id in list(self.List_of_Users.keys()):
            if self.Psd == self.List_of_Users[self.Id]['Password']:
                print('You have successfully Logged in !!!')
            else:
                print('Invalid Credential...')
                print('Please Try with Correct details....')
                u.Login_App()
        else:
            print('Invalid Credential...')
            print('Please Try with Correct details.....')
            u.Login_App()


    def Place_new_order(self):
        with open('List_of_foods.json','r') as f:
            self.Food_list = json.load(f)
            print('-------------------List of Food Items--------------------')
        for self.i,self.j in self.Food_list.items():
            print('Item No:',self.i)
            print('Food name:',self.j['Food name'],'---','Quantity:',self.j['Quantity'],'---','Price:',self.j['Price'])
            print('*'*40)
        return self.Food_list

    def Select_food(self):
        L1={}
        L1[Select] = self.Food_list[Select]
        with open ('Selected_List.json','r') as f:
            self.Select_list=json.load(f)
            self.Select_list.update(L1)

        with open ('Selected_List.json','w') as g:
            json.dump(self.Select_list, g ,indent=4)
        print('Item Selected')
        return self.Select_list


    def Place_order(self):
        count=0
        with open('Selected_List.json','r') as f:
            Order_list = json.load(f)
            print('-------------------List of Selected Items--------------------')
        for self.i,self.j in Order_list.items():
            if self.i != 'dummy':
                count += 1
                print('S.No:',count)
                print('Food name:',self.j['Food name'],'---','Quantity:',self.j['Quantity'],'---','Price:',self.j['Price'])
                print('*'*40)
            else:
                continue

        Total_Items = count
        A=list(Order_list.values())
        Amount=0
        for i in A:
            Amount = Amount + int(i['Price'])
        Total_Amount = Amount
        print('Total items:',Total_Items)
        print('Total Amount:',Total_Amount)
        print('*'*40)

        Proceed = input('Enter P -- TO PLACE THE ORDER: ')
        if Proceed == 'P' or Proceed == 'p':
            with open ('History_list.json','r') as f:
                History_list=json.load(f)
                History_list.update(Order_list)
            with open ('History_list.json','w') as g:
                json.dump(History_list, g ,indent=4)
            print('Your Order has been placed successfully!!!')
        else:
            print('Your order has not been placed.....')


    def Order_history(self):
        with open('History_list.json','r') as f:
            History_list = json.load(f)
            print('-------------------History of Ordered Food Items--------------------')
        for self.i,self.j in History_list.items():
            if self.i != 'dummy':
                print('S.No:',self.i)
                print('Food name:',self.j['Food name'],'---','Quantity:',self.j['Quantity'],'---','Price:',self.j['Price'])
                print('*'*40)
            else:
                continue
        

    def Update_profile(self):
        self.Edit= input('Enter UserID / Phone Number to Update: ')
        if self.Edit in self.List_of_Users.keys():
            self.name = input('Enter Full Name: ')
            self.p_number = (input('Enter Phone Number: '))
            self.email = (input('Enter E-mail Id: '))
            self.address = (input('Enter Address: '))
            self.password = (input('Enter Password: '))
            self.Edit_dict = {'Full name':self.name, 'Phone Number':self.p_number, 'Email Id':self.email, 'Address':self.address, 'Password':self.password}
            self.List_of_Users[self.Edit]=self.Edit_dict
            with open ('List_of_Users.json','w') as g:
                json.dump(self.List_of_Users, g ,indent=4)
            print('Profile has been updated!!!')
            print(self.Edit_dict)
        else:
            print('Entered UserID / Phone Number is not available')



u=User()
u.Registeration()
u.Registeration()
u.Registeration()
u.Registeration()
u.Login_App()

while True:
    print('**************************************************************************************')
    print('*******************************USER OPTIONS*******************************************')
    print('-------------------- Enter N --> To PLACE NEW ORDER ----------------------------------')
    print('-------------------- Enter H --> To ORDER HISTORY ------------------------------------')
    print('-------------------- Enter U --> To UPDATE PROFILE -----------------------------------')
    print('-------------------- Enter E --> To EXIT ---------------------------------------------')
    print('**************************************************************************************')
    print('**************************************************************************************')
    Option = input('Enter option: ')
    if Option == 'N' or Option == 'n':
        while True:
            u.Place_new_order()
            print('**************************************************************************************')
            print('*******************************PLACE ORDER HERE***************************************')
            print('-------------------- Enter 1 --> TO SELECT ITEM NO: 1 --------------------------------')
            print('-------------------- Enter 2 --> TO SELECT ITEM NO: 2 --------------------------------')
            print('-------------------- Enter 3 --> TO SELECT ITEM NO: 3 --------------------------------')
            print('-------------------- Enter P --> TO PLACE ORDER --------------------------------------')
            print('**************************************************************************************')
            Select=input('Enter to Select Item:')
            if Select == '1' or Select == 1:
                u.Select_food()
            elif Select == '2' or Select == 2:
                u.Select_food()
            elif Select == '3' or Select == 3:
                u.Select_food()
            elif Select == 'P' or Select == 'p':
                u.Place_order()
                break
            else:
                print('Incorrect Choice.....')

    elif Option == 'H' or Option == 'h':
        u.Order_history()

    elif Option == 'U' or Option == 'u':
        u.Update_profile()
        
    elif Option == 'E' or Option == 'e':
        print('Thanks for the Visit!!!!')
        break
    else:
        print('Incorrect Choice.....')

