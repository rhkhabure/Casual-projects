#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv 


# In[2]:


def input_grocery_stock():
    
    with open('grocery_stock.csv', 'w', newline='') as csvfile:
        fieldnames = ['item', 'buying_price', 'selling_price', 'quantity_sold', 'quantity_bought', 'Expiry_in_weeks', 'goods_given_away' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        
        while True:
            item = input("Enter the item name (or press Enter to finish): ")
            if item == '':
                break

            try:
                buying_price_str = input("Enter the buying price: ")
                buying_price = float(buying_price_str)
            except ValueError:
                print(f"Invalid buying price for item: {item}. Skipping...")
                continue

            selling_price = input("Enter the selling price: ")
            quantity_sold = int(input("Enter the quantity sold: "))
            quantity_bought = int(input("Enter the quantity bought: "))
            Expiry_in_weeks = int(input("Enter the expiry time in weeks: "))
            goods_given_away = int(input("Enter how many goods were given away: "))
            
            writer.writerow({
                'item': item,
                'buying_price': buying_price,  
                'selling_price': selling_price,
                'quantity_sold': quantity_sold,
                'quantity_bought': quantity_bought,
                'Expiry_in_weeks' : Expiry_in_weeks,
                'goods_given_away' : goods_given_away,
            })

            choice = input("Do you want to add more items (y/n)? ")
            if choice.lower() != 'y':
                break


# In[6]:


def calculate_profit_loss():
   
    with open('grocery_stock.csv', 'r', newline='') as csvfile:
        fieldnames = ['item', 'buying_price', 'selling_price', 'quantity_sold', 'quantity_bought' , ' Expiry_in_weeks' , 'goods_given_away']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)

        
        for row in reader:
            item = row['item']
            try:
                buying_price = float(row['buying_price'])
                selling_price = float(row['selling_price'])
                quantity_sold = float(row['quantity_sold'])
                goods_given_away=float(row['goods_given_away'])
            except ValueError:
                continue

            profit_loss = ((selling_price - buying_price) * quantity_sold )
            loss_from_goods_given_away = (goods_given_away * buying_price)
            total_profit_loss= profit_loss - loss_from_goods_given_away
            
            print(f"Item: {item}")
            print(f"Profit/Loss: ${total_profit_loss:.2f}")


# In[7]:


print("Hello there")
name=str(input("What is your name"))
print("Hello",name)
print("Do you want to see the user manual")
print("1. Yes")
print("2. No")
option = int(input("Enter choice"))
if option == 1:
    print("This is the user manual. It is to explain to you how the application works. You will be required to enter the name,of the good its selling price, buying price,its quantity bought and sold inlcuding of the items shelf life. From there you will be asked if you add a  new item or not.After your choice the program will show you the description of the good at the end of each enter.Once your are done you shall be given a statement of your profits and losses")
elif option == 2:
    print("Welcome",name) 
    
# Call the input_grocery_stock function to input grocery data
input_grocery_stock()

# Call the calculate_profit_loss function to calculate profit/loss
calculate_profit_loss()


# In[ ]:





# In[ ]:




