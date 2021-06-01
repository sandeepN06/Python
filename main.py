# 1: Write a Python program to read a file line by line and store it into a list.

from pathlib import Path as p

file_path = p("demo.txt")

lines = file_path.read_text().splitlines()

print(lines)

# 2: Write a Python program to calculate the number of days between two dates.

#Sample dates : (20200702), (20200711)

from datetime import date

sample_date1 = "20200702"
sample_date2 = "20200711"

# Or we can provide input from the user as well

Year = int(sample_date1[0:4])

Month = int(sample_date1[4:6])

Date = int(sample_date1[6:8])

Year2 = int(sample_date2[0:4])

Month2 = int(sample_date2[4:6])

Date2 = int(sample_date2[6:8])


start_date = date(Year,Month,Date)

end_date = date(Year2,Month2,Date2)

days_between = end_date - start_date

print(days_between.days)


#3: Write a Python program to convert the Python dictionary object (sort by key) to
#JSON data. Print the object members with indent level 4.

#JSON - JAVASCRIPT OBJECT NOTATION (Similar to key value pairs)

import json as js

json_data = {'78':4 , '85':11 , '123':145 }

print(js.dumps(json_data,sort_keys=True,indent=4)) #We could later create our own rest api as well using this data
                                                    #Using flask microframework


'''
4: Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

original_list = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

#We can clearly see that from the required output , we need to sort based on colors .

sorted_list = sorted(original_list, key = lambda x: x['color'])

print(sorted_list)


'''
5: Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space.
'''

def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("demo.txt"))


'''
6: Write a Python program to convert an array to an array of machine values and
return the bytes representation.
Expected Output:
Original array:
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000'
'''

import array
import binascii
result = array.array('i', [1,2,3,4,5,6])

final_result = result.tobytes()
print('Array of bytes:', binascii.hexlify(final_result))


'''

8: Program to Generate random logs and write in a file , once the file size reaches 2Mb
open new file and continue writing

'''

import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=20, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for i in range(20):
    my_logger.debug('i = %d' % i)

# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)

for filename in logfiles:
    print(filename)


'''

9: Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc)

'''


import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in range(1, 10):
                ip="192.168.0.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active")


