from datetime import datetime



datestring = input("Please enter first a date in form dd/mm/yyyy: ")


try:
    date = datetime.strptime(datestring, '%d/%m/%Y')



except ValueError:
    print("Invalid date entered!")
    
datestring2= input("Please enter second a date in form dd/mm/yyyy: ")
try:

    date2 = datetime.strptime(datestring2, '%d/%m/%Y')
    print(date)
    print(date2)
    starp=date2 - date
    print("Difference in dates:", starp)

except ValueError:
    print("Invalid date entered!")

