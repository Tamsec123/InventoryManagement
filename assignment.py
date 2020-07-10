#Name: Tan Jun Wei
#Admin Number: 190816J
#Tutorial Group: IT2153-01
#Phase 1:I have learnt a lot about loops and lists from doing this mini project, as this mini project has made me do a lot of research on them, allowing me to learn more things about them
#Phase 2: I have learnt a lot more about binary search, insertion sort and bubble sort. The practicals and tutorials allowed me to understand, but there was still more to the algorithms that i could only find while searching on google, thus learning a lot more about the usefulness of the algorithm.
#This python file consists of phase 1 and 2

inventory = [
    ['Smart Phone', 20, '500', 'Cheap and affordable phone with all the newest specs'],  #Name, Quantity, Price, Description, Release Date
    ['Head Phones', 100, '30', 'Provides a very good audio quality at a cheap price'], 
    ['Screen Guard', 200, '10', 'does not crack even under a lot of pressure'], 
    ['Windows Laptops', 100, '2000', 'Amazing specifications for a very cheap price.'], 
    ['Memory Cards', 120, '50', 'Fastest reading speeds that anyone can ask for'],
    ['VR Headset', 200, '550', 'Virtual reality headset is awesome. '],
    ['Google Glass', 150, '1500', ' Google Glasses is here for you!'],
    ['Segway Board',1000 , '1500', 'Segway board is awesome!'],
    ['Fitbit Watch',120 , '200', 'Want to keep track of fitness? Use Fitbit!'],
  
]
def binarySearch(theValues, target):                           #PHASE 2
    # Start with the entire sequence of elements
    low = 0  #min
    high = len(theValues) - 1  #max

    # Repeatedly subdivide the sequence in half 
    # until the target is found
    while low <= high:
        #Find the midpoint of the sequence
        mid = ((high+low) // 2)
        # SCENARIO 1: is the midpoint value same as the target?
        # If yes, return the index of the midpoint

        if theValues[mid][0] == target:
            return inventory[mid]
        # SCENARIO 2:  is the target before the midpoint? 
        elif target < theValues[mid][0]:
            high = mid - 1
        # SCENARIO 3:  is the target after the midpoint?
        else:
            low = mid + 1
        # If we have gone through the entire list, and the target is not in there
    return "Not Found"



    
while True:
    print('******************************************************')
    print("Welcome to ABC Stock Inventory.")
    print('******************************************************')
    menu = input("What do you want to do?\n1. Add inventory\n2. Remove Inventory\n3. Display Inventory\n4. Sort Inventory\nInput your choice:  ") 
    
    
    if menu == '1':   #ADD ITEM    PHASE 1
        stockName = input("Name of item:")

        i = 0
        invList = []                        #lsit to store item name in list
        while i < (len(inventory)-1):       
            invList.append(inventory[i][0])     #append name into list
            i += 1
            if stockName in invList:            ##if name found in list:
                break                           #Stop loop
          
        if stockName not in invList:            #if name not found, proceed to ask for info to add item
            quantity = int(input("Stock level: "))
            price = float(input("Price: "))
            description = input("Description of item: ")
            inventory.append([stockName, quantity, str(price), description])
            print("Item Added!")
            print("Returning to front page.......")
            

        else:                                   #if item in list
            prod = inventory[i-1]
            quantity = int(input("Stock level: "))
            currentQuantity = prod[1]
            newQuantity = quantity + currentQuantity
            prod[1] = newQuantity
            print("Item has been updated!")
            print("Returning to front page......")

            


        
    elif menu == '2':     #REMOVE ITEM   #PHASE 1
        
        print("Product\t\tIn Stock\tPrice\tDescription")
        print('----------------------------------------------------------------------------------------')
        for item in inventory:
            print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))
        print('----------------------------------------------------------------------------------------')
        itemList = []       #List to store item name
        i = 0             #Count
        while True:
            
            itemToRemove = input("Please input the name of the item that you want to remove: ")       #input to ask for index of item that they want to remove
            while i < (len(inventory)-1):              
                itemList.append(inventory[i][0])        #Append index value into itemList
                i += 1
                if itemToRemove in itemList:                         #If index in item list:
                    break                                   #Break out of loop
            if itemToRemove not in itemList:                #If item not in itemList - 1(because it starts from 0)
                print("Item not in inventory... Please try again.")  #means that index not found
        
            else:
                
                inventory.remove(inventory[i-1])
                print("Item has been removed...")
                print("Returning to front page...")
                break
  
                
    elif menu == '3':                       #DISPLAY ITEM PHASE 1
        print('******************************************************')
        print("Product\t\t\tIn Stock\tPrice\t\t\tDescription")
        for item in inventory:
            print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))
        print('******************************************************')
        specificItem = input("Would you like to search for a specific item? (Y/N)")
        if specificItem.upper() == "Y":
            n = len(inventory)              #This is start Insertion Sort, This is sorting by name.    #PHASE 2
        # Starts with the first item as the only sorted entry.
            for i in range(1, n):
                # Save the value to be positioned
                value = inventory[i]

                # Find the position where value fits in the
                # ordered part of the list.
                pos = i
                while pos > 0 and value[0] < inventory[pos - 1][0]:
                    # Shift the items to the right during the search
                    inventory[pos] = inventory[pos-1]
                    pos -= 1
        
                # Put the saved value into the open slot.
                inventory[pos] = value                          #Insertion Sort end
            specific_name = input("Name of item you want to search: ")
            r = binarySearch(inventory, specific_name)           #Call binary search function
            if r == "Not Found":                                 #if binary search function returns Not Found
                print("Item is not in inventory")                #means item not in inventory
            else:                                                
                print("Name of Item: {}\n Quantity: {}\n Price: {}\n Description: {} ".format(r[0], r[1], r[2], r[3]))    #display item
        else:
            print("Returning to front page...")
            
    
    
    elif menu == '4':                      #SORT ITEM PHASE 2
        whatSort = int(input("What do you want to sort inventory by?\n1. Stock Level\n2. Name\nInput your choice: "))
        if whatSort == 1:
            n = len(inventory)                              #PHASE 2 BUBBLE SORT
            # Perform n-1 bubble operations on the sequence
            for i in range(n - 1, 0, -1):
                # To check occurrence of swapping in inner loop
                Swap = False

                # Move the largest item to the end
                for j in range(i): 
                    if inventory[j][1] > inventory[j+1][1]: 
                    # Swap the j and j+1 items 
                        tmp = inventory[j]
                        inventory[j] = inventory[j + 1] 
                        inventory[j + 1] = tmp 

                        # If swapping occurred 
                        Swap = True          


                # Exit the loop if no swapping occurred in the previous pass 
                if Swap == False:
                    break                                    #BUBBLE SORT END
                
            
            print('******************************************************')
            print("Product\t\tIn Stock\tPrice\t\tDescription")
            for item in inventory:
                print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))
            print('******************************************************')
            
            
        elif whatSort == 2:                 #SORT BY NAME
            n = len(inventory)              #BUBBLE SORT
            # Perform n-1 bubble operations on the sequence
            for i in range(n - 1, 0, -1):
                # To check occurrence of swapping in inner loop
                Swap = False

                # Move the largest item to the end
                for j in range(i): 
                    if inventory[j][0] > inventory[j+1][0]: 
                    # Swap the j and j+1 items 
                        tmp = inventory[j]
                        inventory[j] = inventory[j + 1] 
                        inventory[j + 1] = tmp 

                        # If swapping occurred 
                        Swap = True          


                # Exit the loop if no swapping occurred in the previous pass 
                if Swap == False:
                    break                  #BUBBLE SORT END
            print('******************************************************')
            print("Product\t\tIn Stock\tPrice\t\tDescription")
            for item in inventory:
                print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))
            print('******************************************************')
    
    
    
    else:
        print("Sorry, input error, please try again.")

        

