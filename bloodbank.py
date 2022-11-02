import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'bloodbankdb')

mycursor = mydb.cursor()



while True:
    print("\nSelect an option from the menu ")
    print("1. Add Donor")
    print("2. View all donors")
    print("3. Search a donor")
    print("4. Update donor")
    print("5. Delete donor")
    print("6.exit\n")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("Donor data entry selected")

        dname = input("Enter donor's name: ")
        dphone = input("Enter phone number: ")
        daddress = input("Enter the address: ")
        bloodgroup = input("Enter the bloodgroup: ")
        dage = input("Enter the age: ")

        sql = 'INSERT INTO `donors`(`name`, `phone`, `address`, `bloodgroup`, `age`) VALUES(%s,%s,%s,%s,%s)'
        data = (dname,dphone,daddress,bloodgroup,dage)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Donor's data inserted successfully.")
    elif(choice == 2):
        print("View all Donor")
        sql = "SELECT * FROM `donors`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice == 3):
        print("Searching a Donor")
        dname = input("Enter the Donor name to search: ")
        sql ="SELECT  `name`, `phone`, `address`, `bloodgroup`, `age` FROM `donors` WHERE `name`='"+dname+"'" 
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif (choice == 4):
        print("update Donor")
    elif(choice == 5):
        print("delete a Donor")
    elif(choice==6):
        break