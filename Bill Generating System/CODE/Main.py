
print ("*******************************************************************")
print ("               WEL-COME to Costume Rental Shop              ")
print ("*******************************************************************")
print ("\n")

#using def function
def Shop(ask_user):
    return(ask_user) 
loop = True

while loop == True:
    print ("Select your Option")
    print ("Press 1 to Rent a costume.")
    print ("Print 2 to Return a costume.")
    print ("Press 3 to Exit.")

    ask_user =input("Enter a Your option:")
    print("\n")
    
    if ask_user== "1":
        print ("Let's Rent a Costume")
        print("\n")
        
        print("*******************************************************************")
        print("ID\tCostume Name\tCostume Brand\tPrice\tQuantity")
        print("*******************************************************************")
        
        file = open("Text.txt","r")
        a = 1
        for line in file:
            print(a,"\t"+line.replace(",", "\t"))
            a = a+1

        print("*******************************************************************")
        file.close()
        print("\n")

        def costumes(costumeDictionary):
            return(costumeDictionary)
        file = open("Text.txt","r")
        costumeDictionary = {}
        costumeID = 1
        for line in file:
            line = line.replace("\n","")
            costumeDictionary.update({costumeID: line.split(",")})
            costumeID = costumeID + 1
        file.close()

        def valid(validID):
            return(validID)
        
        if ask_user == "1":

            validID = int(input("Enter the ID of costume you want to rent: "))
            print("\n")
            
            while validID <= 0 or validID > len(costumeDictionary):
                print("\n")
                print("*******************************************************************")
                print("             Please provide a valid costume ID !!!                 ")
                print("*******************************************************************")
                print("\n")
                
                print("*******************************************************************")
                print("ID\tCostume Name\tCostume Brand\tPrice\tQuantity")
                print("*******************************************************************")

                file = open("Text.txt","r")
                a = 1
                for line in file:
                    print(a,"\t"+line.replace(",", "\t"))
                    a = a+1
                print("*******************************************************************")
                
                print("\n")


                
                validID = int(input("Enter the ID costume you want to rent:"))
                print("\n")
            print("Costume ID is" , validID)        
            print("Costume is available")
            print("\n")
            

            def quantity(userQuantity):
                return(userQuantity)

            userQuantity = int(input("Enter the quantity of costume:"))
            print("\n")

            
            def quantity_sel(quantity_of_selected_costume):
                return(quantity_of_selected_costume)
            quantity_of_selected_costume = costumeDictionary[validID][3]

            while userQuantity <= 0 or userQuantity >int(quantity_of_selected_costume):
                print("quantity not available")
                print("\n")
                userQuantity = int(input("Enter the quantity of costume:"))
                print("\n")
            print("\n")       
                            
                            
                            

            costumeDictionary[validID][3] = int(costumeDictionary[validID][3])-int(userQuantity)

            file = open("Text.txt","w")

            for values in costumeDictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                file.write("\n")
            file.close()
            print(costumeDictionary)
            print("\n")

                    
            
            a = input("Please enter your name: ")
            print("\n")

            
        costname = costumeDictionary[validID][0]
        totalquantity = userQuantity
        brand = costumeDictionary[validID][1]
        price = costumeDictionary[validID][2]
        itemprice = costumeDictionary[validID][2].replace("$"," ")
        totalprice = float(itemprice)*float(totalquantity)

        import datetime

        t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
            datetime.datetime.now().day)
        d = str(t)
        u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
            datetime.datetime.now().second)
        e = str(u)

        print ("*******************************************************************")
        print ("\t\tCostume Rental Shop")
        print ("*******************************************************************")
        print("--------------------------------------------------------------------")
        print("\t\t\tBILL Details")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("Date: " + d + "\t\t\t\t\tTime: " + e + "")
        print("\nName of Customer: " + str(a) + "")
        print("--------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("COSTUME\t\t\tQUANTITY\tPRICE\t\tTOTAL")
        print("--------------------------------------------------------------------")
        print(costname,"\t",totalquantity,"\t","\t",price,"\t","\t","$",str(totalprice))
        print("\n------------------------------------------------------------------")
        print("\nItems in Rent are: ",costname)
        print("\nBrand of Items are: ",brand)
        print("\n------------------------------------------------------------------")
        print("\n")
        print("\tThank You " + a + " For Shopping.\n\t\tPlease Visit Again")
        print("\n------------------------------------------------------------------")
        print("\n")
        print("--------------------------------------------------------------------")
        print("\tRent Details Bill has been Generated")
        print("--------------------------------------------------------------------")
        print("\n")
        
        file = open(a + ".txt", "w")  # generate a unique Bill name and open it in write mode.
        file.write("*******************************************************************")
        file.write("\n\t\tCostume Rental Shop")
        file.write("\n*******************************************************************")
        file.write("\nDate: " + d + "\t\t\t\t\tTime: " + e + "")
        file.write("\nName of Customer: " + str(a) + "")
        file.write("\n*******************************************************************")
        file.write("\n----------------------------------------------------------------------")
        file.write("\nCOSTUME\t\t\t\tQUANTITY\tPRICE\t\tTOTAL")
        file.write("\n----------------------------------------------------------------------")
        file.write("\n" + costname)
        file.write("\t\t\t" + str(totalquantity))
        file.write("\t\t" + price)
        file.write("\t\t" + str(totalprice))
        file.write("\n-------------------------------------------------------------------------")
        file.write("\nItems in Rent are: " + costname)
        file.write("\nBrand of Items are: " + brand)
        file.write("\n-------------------------------------------------------------------------")
        
        file.write("\n-----------------------------------------------------------------------")
        file.write("\n\tThank You " + a + " For Shopping.\n\tPlease Visit Again")
        file.write("\n-----------------------------------------------------------------------")
        file.write("\n")
        file.close()



    elif ask_user == "2":
        print("Let's return a Costume")
        print("\n")
        import ReturnCostume
        ReturnCostume.returnCostume()
        
            
            

    elif ask_user == "3":
        print("************************************************************")
        print("\t Thank You for using our application")
        print("************************************************************")
        print("\n")
        loop = False
    else:
        print("Invalid Input !!!")
        print("\n")
