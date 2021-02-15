#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignment 05 script for creating CDInventory.
# Change Log: Patrick Danileson, 2021-Feb-14, Modified starter script
# DBiesinger, 2030-Jan-01, Created File
# PDanielson, 2021-Feb-14, Modified Starter Script
#------------------------------------------#
import os.path

# Declare Variables
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
data_loaded = False  # becomes True if user loads in existing data

# Check if Inventory File Exists and Create File if it does not
if os.path.exists(strFileName): 
    pass
else:
    objFile = open(strFileName,'w')
    objFile.close()

# Get user Input
print('The Magic CD Inventory\n')
while True:
    
    # 1. Display menu allowing the user to choose:
    print()
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        print('Exiting Program...Done!')
        break
    
    if strChoice == 'l':
        print('Loading Existing Inventory.')
        objFile = open(strFileName,'r')
        for row in objFile:
            lstRow = row.strip().split(',')     # Store Row Values in List
            dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}  # Assign to dictionary
            lstTbl.append(dicRow)
        objFile.close()
        data_loaded = True  # Set condition that file has been read into lstTbl in memory
        
    elif strChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('Displaying Current Inventory:')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')    # print only values of dictionary row

    elif strChoice == 'd':
        del_entry = int(input('Please enter the ID of the entry you want to delete: '))
        for row in lstTbl:
            if del_entry == row['id']:
                lstTbl.remove(row)
            else: pass
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        
        # Override Existing Data in File to prevent duplicate entries
        if data_loaded:
            objFile = open(strFileName, 'w')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            lstTbl.clear()  # Clear List Table of Data Saved to File
            data_loaded = False
            
        # If user did not load in data from file, append additional entries ONLY
        else:
            objFile = open(strFileName, 'a')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            lstTbl.clear()  # Clear List Table of Data Saved to File
            data_loaded = False
            
    else:
        print('Input Error: ')
        print('\tPlease choose either l, a, i, d, s or x!')

