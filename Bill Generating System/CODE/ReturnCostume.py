import ListSplit
import datetime

random = ListSplit.random_number()
dictionary = ListSplit.dictionary_costume()

def dictionary_write():
    file = open("Text.txt","w")
    for values in dictionary.values():
        file.write(str(values[0]) + ","+ str(values[1])+ ","+str(values[2]) + ","+str(values[3]))
        file.write("\n")
    file.close()

def correctID():
    correct_id = False
    while correct_id == False:
        try:
            value = int(input("Enter the ID of costume you want to Return: "))
            return value
            correct_id = True
            returnCostume()
        except:
            print("***************************************")
            print("Please provide a valid costume ID !!! ")
            print("***************************************")
            print("\n")

def anotherCorrectID():
    correct_id = False
    while correct_id == False:
        try:
            value = int(input("Enter the ID of another costume you want to Return: "))
            return value
            correct_id = True
            returnCostume()
        except:
            print("***************************************")
            print("Please provide a valid costume ID !!! ")
            print("***************************************")
            print("\n")

def day_costumeKept():
    correct_day = False
    while correct_day == False:
        try:
            value = int(input("\nEnter the number of days you have kept the costume for: "))
            return value
            correct_day = True
            returnCostume()
        except:
            print("***************************************")
            print("Please provide a valid Days !!! ")
            print("***************************************")
            print("\n")

def day_costumeKept2():
    correct_day = False
    while correct_day == False:
        try:
            value = int(input("\nEnter the number of days you have kept the another costume for:"))
            return value
            correct_day = True
            returnCostume()
        except:
            print("***************************************")
            print("Please provide a valid Days !!! ")
            print("***************************************")
            print("\n")

def correctName():
    correct_name = False
    while correct_name == False:
        try:
            value = input("\nEnter the name of person who wants to return Costume: ")
            int(value)
            print("Please enter name correctly.(eg. Roshan Mandal) ")
        except:
            value.isalpha()
            return value
            correct_name = True
            returnCostume()

def returnCostume():
    returnList=[]
    fineList =[]
    
    ListSplit.print_dictionary()

    name = correctName()
    returnCostume = correctID()
    days = day_costumeKept()

    dictionary[returnCostume][3] = int(dictionary[returnCostume][3]) + 1
    returnList.append(dictionary[returnCostume][0])
    dictionary_write()

    if 0 < days < 5:
        print("\nNo fine is charged for this Costume.")
        print("Thank you for returning Costume on time.")

    elif days > 5:
          fineAmount = (days-5) * 0.10 * float(dictionary[returnCostume][2].replace("$",""))
          fineList.append(fineAmount)
          totalFine = sum(fineList)
          print("\nCharge for not returning Costume in time: $", totalFine)

    date = str(datetime.date.today())
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    time_display = date+ " " + hour + ":" + minute + ":" +second

    print("Date and time of return: ",time_display)
    print("\n*************************************************************************")
    print("\n\t\tCostumes after return")
    print("\n*************************************************************************")

    ListSplit.print_dictionary()

    count = True
    while count == True:
        print("\nDo you want to return another Costume ?")
        another = input("Enter 'y' to return more Costume or else provide any other value: ")

        if another == "Y" or another == "y":
            #calling new variables using other functions
            returnCostume = anotherCorrectID()
            other_days = day_costumeKept2()

            dictionary[returnCostume][3] = int(dictionary[returnCostume][3]) + 1
            returnList.append(dictionary[returnCostume][0])
            dictionary_write()

            if 0 < other_days < 5:
                print("\nNo fine is charged for this Costume.")
                print("Thank you for returning Costume on time.")

            elif other_days > 5:
                fineAmount = (other_days -5) * 0.10 * float(dictionary[returnCostume][2].replace("$",""))
                fineList.append(fineAmount)
                totalFine = sum(fineList)
                print("\nCharge for not returning Costum in time: $", totalFine)

            dictionary_write()
            print("\n*************************************************************************")
            print("\n\t\tCostumes after return")
            print("\n*************************************************************************")
            ListSplit.print_dictionary()

        else:
            count = False
            totalFine = sum(fineList)


            print("************************************************************************")
            print("\t\t\t  Costume Rental Shop System")
            print("************************************************************************")
            print("=========================================================================")
            print("\t\t\tReturn Coustume BILL Details")
            print("=========================================================================")
            print("\n")
            print("*************************************************************************")
            print("Date and time of Costume returned: ", time_display)
            print("\nName of the person who returned Costume: ",name)
            print("*************************************************************************")
            print("\n-------------------------------------------------------------------------")
            print("\nFine Amount: $",totalFine)
            print("\n-------------------------------------------------------------------------")
            print("\nList of Costume returned: ")
            for i in range(len(returnList)):
                print(returnList[i])
            print("-------------------------------------------------------------------------")

            print("\n")
            print("\t\t     Thank You For Returning.\n\t\t\tPlease Visit Again")
            print("\n=======================================================================")
            print("\n")
            print("-------------------------------------------------------------------------")
            print("\tReturn Bill Details has been Generated")
            print("-------------------------------------------------------------------------")
            print("\n")

            file1 = open("Return_"+name+"("+random+")"+".txt","w")
            file1.write(" -----------------------------------------------------------------------")
            file1.write("\t\tCostume Rental System")
            file1.write("\n-----------------------------------------------------------------------")
            file1.write("\n=========================================================================")
            file1.write("\n\t\t\tReturn Coustume BILL Details")
            file1.write("\n=========================================================================")
            file1.write("\n")
            file1.write("\n*************************************************************************")
            file1.write("\nDate and time of Costume returned: " + str(time_display))
            file1.write("\nName of the person who returned Costume: " + str(name))
            file1.write("\n*************************************************************************")
            file1.write("\n")
            file1.write("-------------------------------------------------------------------------")
            file1.write("\nFine Amount : $" + str(totalFine))
            file1.write("\n-------------------------------------------------------------------------")
            file1.write("\nList of Costume returned: ")
            file1.write("\n\t")
            for i in range(len(returnList)):
                file1.write(returnList[i])
            
            file1.write("\n-------------------------------------------------------------------------")

            file1.write("\n")
            file1.write("\tThank You " + name + " For Returning.\n\t\tPlease Visit Again ")
            file1.write("\n=======================================================================")
            file1.write("\n")
            file1.write("-------------------------------------------------------------------------")
            file1.write("\n\tReturn Bill Details has been Generated")
            file1.write("\n-------------------------------------------------------------------------")
            file1.write("\n")
            file1.close()
