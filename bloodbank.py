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
    print("6. View donors starting with a specific letter")
    print("7.exit\n")

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
        dname = input("Enter donor's name: ")
        dphone = input("Enter phone number to update: ")
        daddress = input("Enter the address to update: ")
        bloodgroup = input("Enter the bloodgroup to update: ")
        dage = input("Enter the age to update: ")

        sql = "UPDATE `donors` SET `phone`='"+dphone+"',`address`='"+daddress+"',`bloodgroup`='"+bloodgroup+"',`age`='"+dage+"' WHERE `name`='"+dname+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Blood donor data successfully updated.")

    elif(choice == 5):
        print("delete a Donor")
        dname = input("Enter donor name to delete: ")
        sql ="DELETE FROM `donors` WHERE `name`='"+dname+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Donor data deleted.")

    elif(choice == 6):
        print("Search donors by letter")
        dletter = input("Enter the letter to search: ")
        sql = "SELECT `name`, `phone`, `address`, `bloodgroup`, `age` FROM `donors` WHERE `name` LIKE '"+dletter+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==7):
        break