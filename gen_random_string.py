# generate random string
import string
from random import choice
import csv
from datetime import datetime

startTime = datetime.now()

# the string includes below char types
allchar = string.ascii_letters + string.digits # + string.punctuation
# password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
with open('numbers.csv', mode='w') as file:
    writer = csv.writer(file)
    for i in range(1, 10000): # number of records to be generated
        password=""
        passlist = []
        for x in range(1, 10): # length of string
            password += "".join(choice(allchar))
        passlist.append(password)
        writer.writerow(passlist)

print('Done in ', datetime.now() - startTime)
