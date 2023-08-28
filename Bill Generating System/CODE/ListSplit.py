#creating a program to display dictionary and list of in proper format of tabular form
#importing datetime module 
import datetime

#function created to read the already provided file containg list of
def read_file():
    file = open("Text.txt","r")
    print(file.read())
    file.close

#function created to display the  in tabular form
def print_dictionary():
    print("\n--------------------------------------------------------------------------------")
    print("ID\tCostume Name\tCostume Brand\tPrice\tQuantity" )
    print("--------------------------------------------------------------------------------")

    #creating empty dictionary
    dictionary ={}
    file = open("Text.txt","r")
    costumeID = 0

    #using for loop to display book 
    for line in file:
        costumeID = costumeID + 1
        line = line.replace("\n","")
        dictionary [costumeID] = line.split(',')
        line = line.replace(",", "\t")
        
        print(costumeID, "\t", line) 
    print("\n-------------------------------------------------------------------------------\n")
    print(dictionary)
    file.close()

#function created to display dictionary of available 
def dictionary_costume():
    dic ={}
    file = open("Text.txt","r")
    id_costume = 0
    for line in file:
        id_costume = id_costume + 1
        line = line.replace("\n","")
        dic [id_costume] = line.split(',')
        line = line.replace(",", "\t")

    file.close()
    return dic

#function created to call date and time function
def random_number():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    micro = str(datetime.datetime.now().microsecond)

    Random = minute + second + micro
    return Random
