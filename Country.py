"""
Name: N'din Assi 
Course: CIS 216 oBJECT oRIENTED cOMPUTER pROGRAMMING 1 
Lab Tittle: Country

"""


def main():
    
    countries={"+1":"United States of America",
               "+256":"Uganda",
               "+144":"United Kingdom"
        
        }
    program_action="yes"
    headMenu()
    while program_action !="exit":
        program_action=input("Do you wish to continue using the program? ")
        if program_action=="exit":
            break 
        elif program_action=="add":
            addvalues(countries)
        elif program_action=="delete":
            delvalues(countries)
        elif program_action=="display":
            display(countries)
        else:
            print("Error Command not found. Try again. ")
        
def display(dict):
    print("COUNTRIES IN DICTIONARY")
    for i,k in dict.items():
        print(f"{i},{k}")
def addvalues(dicti):
    newkey = input("Enter the country code: i.e +254 : ")
    newcountry=input("Enter the country name: ")
    dicti[newkey]=newcountry
    print(f"{newkey}, {newcountry} added to the dictionary ")
    

def delvalues(dict):
    removecountry= input("Enter the code of the country to remove: (i.e +1)")
    removed_item=dict.pop(removecountry, "Key Not Found")
    print(f"{removed_item} Removed from the dictionary")
    

def headMenu():
    print("Welcome to the Country Application")
    print("MENU")
    print("display : Display countries in dictionary")
    print("add: add country to the dictionary ")
    print("delete: Delete country form the dictionaty ")
    
    

if __name__=="__main__":
    main()