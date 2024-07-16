import requests
import Xlsxutils

base_url= "https://reqres.in"

file = r"C:\Users\Chandan\Documents\Test.xlsx" # path of exl
sheetName = "Sheet1"
rows = Xlsxutils.getRowCount(file, sheetName)

for i in range(2,rows+1):
    end_url = Xlsxutils.readData(file,sheetName,i,1)
    Expected_Status_Code= Xlsxutils.readData(file,sheetName,i,3)

    # pass url one by one
    resp = requests.get(base_url + end_url)
    Actual_Status_Code = resp.status_code

    # write Actual_Status_Code in exl sheet
    Xlsxutils.writeData(file,sheetName,i,4,Actual_Status_Code)

    # condition match or not match
    if (int(Expected_Status_Code) == int(Actual_Status_Code)):
        # Print("Validate")
        Xlsxutils.writeData(file, sheetName, i, 5,"Validate")
        Xlsxutils.fillGreen(file, sheetName, i, 5)
    else:
        # Print("Not Validate")
        Xlsxutils.writeData(file, sheetName, i, 5, "Not Validate")
        Xlsxutils.fillRed(file, sheetName, i, 5)


print("successfully run")


