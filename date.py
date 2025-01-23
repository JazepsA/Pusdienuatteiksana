from datetime import datetime
import sys



datestring = input("Ievadiet datumu no kura vēlaties atteikt pusdienas dd/mm/yyyy: ")


try:
    date = datetime.strptime(datestring, '%d/%m/%Y')



except ValueError:
    print("Nepareizi ievadīts datums!")
    sys.exit()
    
datestring2= input("Ievadiet datumu līdz kuram vēlaties atteikt pusdienas dd/mm/yyyy: ")
try:

    date2 = datetime.strptime(datestring2, '%d/%m/%Y')
    print(date)
    print(date2)
    starp=date2 - date
    print("Dienas:", starp)

except ValueError:
    print("Nepareizi ievadīts datums!")
    sys.exit()

