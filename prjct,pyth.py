repository={
"Ashish Bedi":'8661267713', 
    "Aastha Khanna":'7579199576', 
    "Abhay Singh Gill":'9973887297', 
    "Abhishek":'9088169383', 
    "Abhishek Singh":'9303551094', 
    "Ahlib Farhat Shah":'9198004110', 
    "Akash Babu":'7471681289', 
    "Akash Sharma":'7979518879', 
    "Alan James":'7177985421', 
    "Ali Quadir Ahmad":'9992071355', 
    "Aman Jaiswal":'8396745063', 
    "Amit Kumar":'7821786487', 
    "Anisur Rahman":'7961286187', 
    "Ankur Kumar":'7344055082', 
    "Arshdev Singh":'7030723463', 
    "Atheev Gokul":'7170910431', 
    "Atiqur Rahman":'8010023377', 
    "Ayush Pratap Singh":'9007230405', 
    "Bhavyansh Jain":'9692360798', 
    "Chandra Bhan Singh":'7375286337', 
    "Choudhary Harshit Rawat":'7142978535', 
    "Deepak Kumar":'8763845112', 
    "Devesh Tripathi":'8767544836', 
    "Dhruv":'7212723669', 
    "Gurnam Singh":'7195291371', 
    "Hanish Vardhan Kotte":'9881352646', 
    "Hari Madhav S S":'8395380500', 
    "Harsh Anand":'9207535948',
    "Harsh Kumar":'8574368765', 
    "K Chandra Shekhar":'8123204767', 
    "K Ganesh":'9460496917', 
    "Khushi Singh":'8795585767', 
    "Kishor Kumar":'9243554682', 
    "Kushagr Sharma":'7962101245', 
    "Lokesh Yadav":'7379813769', 
    "Mohammed Kaleem":'7995435975', 
    "Muhammed Rashid A T":'8680531944', 
    "Muskan Kumari":'7797555025', 
    "Naveed Farook":'7447637941', 
    "Neha Priya":'7216945103', 
    "Radheshyam Thakur":'8353288760', 
    "Rahul Krishnan M":'7363207262', 
    "Raj Shekhar Sahani":'8408360873', 
    "Ritika Varshney":'7547972461', 
    "Rohit Kumar":'7350843348', 
    "Sachin Rana":'9823878944', 
    "Sahil Shekhar":'8283830862', 
    "Sahil Kumar":'9053779895', 
    "Sakkiya K S":'8771613433', 
    "Samra Mariyam":'8082815555', 
    "Sangam Raj":'8615934108', 
    "Shadab Akhter":'8973783949', 
    "Shalvia Nawal M C":'7049837302', 
    "Shashank Kumar":'8679454564', 
    "Shekhar":'8087052383', 
    "Shreya Sharma":'7482014531', 
    "Shreyansh":'9880179221', 
    "Shubham Kumar Yadav":'8132706704', 
    "Sonu Kumar":'9525122824', 
    "Subham Mishra":'7086791819', 
    "Suraj":'7550707801', 
    "Umme Haney":'7377563369', 
    "Utkarsh Gaur":'8192957696', 
    "Sai Kumar":'9563312687', 
    "Vansh":'8665477815', 
    "Vanshika Panwar":'8974232855', 
    "Vanshika Thakur":'9476003596', 
    "Ahamad Thahseel":'9701887902'
}


def nameFormatted(name):
    nameFormatted=name.strip()
    nameFormatted=nameFormatted.title()
    return(nameFormatted)

def numFormatted(number):
    numFormatted=number.strip()
    numFormatted=numFormatted.replace(" ","")
    numFormatted=numFormatted.replace("-","")
    if numFormatted[0]=="+":
        return(numFormatted[3:])
    else:
        return(numFormatted)
def main():
    print("-"*43)
    print("-"*5,"WELCOME","-"*2,"TO","-"*2,"PHONEBOOK","-"*10)
    print("-"*43)
    print("Select The Option\n1.List All Contacts\n2.Search The Contacts\n3.Search Multiple Contacts\nX.Exit The Program")
    selector=input("$> ")
    selector=selector.strip()
    if selector=="1":
        for i in repository:
            print("-"*43)
            print(i,":",repository[i])
            print("-"*43)
            
        main()
    elif selector=="2":
        singleSearch()

    elif selector=="3":
        searchMultiple()
    elif selector=="x" or selector=="X":
        exit()
    else:
        print("The entered selector is out of range")
        main()
def searchMultiple():
    n_of_contact=int(input("Enter The Number Of Contacts To Display: "))
    list_n=[]
    for i in range(n_of_contact):
        name=input("Enter the name: ")
        name_formatted=nameFormatted(name)
        list_n.append(name_formatted)
    for i in list_n:
        if i in repository:
            print("-"*43)
            print(i,":",repository[i])
            print("-"*43)
        else:
            print("-"*43)
            print("Contact Not Found")
            print("-"*43)
    main()
def singleSearch():
    global repository
    print("-"*43)
    print("Select the options\n0.Go Back\n1.Search by Name\n2.Search by Number\nX.to quit the program")
    selector=input("$> ")
    selector=selector.strip()
    if selector=="1":
        name=input("Enter the name to search(without any special chars):> ")
        name_formatted=name.strip()
        name_formatted=name_formatted.title()
        if name_formatted in repository:
            num_formatted=repository[name_formatted]
        else:
            print("-"*43,"\nThe entered name is not found\n","-"*43)
            singleSearch()
        

        
    elif selector=="2":
        number=input("Enter the number to search:> ")
        num_formatted=numFormatted(number)
        
        if num_formatted in repository.values():
            name_formatted=(list(repository.keys())[list(repository.values()).index(num_formatted)])
        else:
            print("-"*43,"\nThe entered name is not found\n","-"*43)



    elif selector=="X" or selector=="x":
        exit()
    elif selector=="0":
        main()
    else:
        print("The entered selector is out of range")
        singleSearch()
    print("-"*43)
    print(name_formatted,":",num_formatted)
    print("-"*43)
    singleSearch()

main()


