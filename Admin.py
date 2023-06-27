import json
class Admin:
    def __init__(self):
        self.List_of_foods = {}
        self.FoodID = len(self.List_of_foods)+1
    def Add_food_Item(self):
        self.name = input('Enter Food Name: ')
        self.quantity = (input('Enter Quantity: '))
        self.price = int(input('Enter Price: '))
        self.discount = int(input('Enter Discount: '))
        self.stock = int(input('Enter Stock: '))
        self.Food_details = {'Food name':self.name, 'Quantity':self.quantity, 'Price':self.price, 'Discount':self.discount, 'Stock':self.stock}
        self.FoodID = len(self.List_of_foods)+1
        self.List_of_foods[self.FoodID] = self.Food_details
        with open('List_of_foods.json','w') as f:
            json.dump(self.List_of_foods,f)
        return self.List_of_foods

    def View_food_menu_list(self):
        print('Menu List of Food Items')
        for i,j in self.List_of_foods.items():
            print('Food ID:',i)
            for k,l in j.items():
                print(k,':',l)
            print('*'*20)
        return self.List_of_foods


    def Edit_food_item(self):
        Edit= int(input('Enter Food ID to edit: '))
        if Edit in self.List_of_foods.keys():
            name = input('Enter Food Name: ')
            quantity = (input('Enter Quantity: '))
            price = int(input('Enter Price: '))
            discount = int(input('Enter Discount: '))
            stock = int(input('Enter Stock: '))
            Dict2 = {'Food name':name, 'Quantity':quantity, 'Price':price, 'Discount':discount, 'Stock':stock}
            self.List_of_foods[Edit]=Dict2
            print('Edited Food list: ',self.List_of_foods)
            with open('List_of_foods.json','w') as f:
                json.dump(self.List_of_foods,f)
        else:
            print('Entered Food ID is not available in the Menu List')
        return self.List_of_foods

    def Remove_food_item(self):
        Remove= int(input('Enter Food ID for removal: '))
        if Remove in self.List_of_foods.keys():
            del self.List_of_foods[Remove]
            print('Remaining Food list: ',self.List_of_foods)
            with open('List_of_foods.json','w') as f:
                json.dump(self.List_of_foods,f)
        else:
            print('Entered Food ID is not available in the Menu List')
        return self.List_of_foods
        


X = Admin()
print(X.Add_food_Item())
print(X.Add_food_Item())
print(X.Add_food_Item())
print(X.Add_food_Item())
print(X.View_food_menu_list())
print(X.Edit_food_item())
print(X.Remove_food_item())





