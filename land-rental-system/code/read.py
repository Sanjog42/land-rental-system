class reading:
    #This function displays the land stored in landonrent.txt file
    def display():
        data=[] #list that contains data from the file
        file=open("landonrent.txt","r")
        for row in file.readlines():
            row=row.replace("\n","").split(",")
            if row[5] == "Available":
                data.append(row)
        file.close()
        return data

    #this function checks and retrieves data from the file
    def check():
        info=[]
        file=open("landonrent.txt","r")
        for row in file.readlines():
            row=row.replace("\n","").split(",")
            info.append(row)
        file.close()
        return info

    #prints land data in a proper way
    def p(data):
        for row in data:
             print(row[0]+" "* (10 - len(row[0])) + row[1] + " " * (10 - len(row[1])) + row[2]+ " " * (10 - len(row[2])) + row[3] + " " * (8 - len(row[3]))+ row[4]+ " " * (6 - len(row[4])) + row[5])
