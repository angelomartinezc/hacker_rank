# Suspicious Activity from logs

# Applications logs are useful in analyzing interaction with an application and may also used to detect suspicious activities.
# A los file is provided as a string array where each entry represents a money transfer in the form "sender_user_id", "recipient_user_id" and "amount"
# Each of the values is separated by a space

# Logs are given in no particular order. 
# Write  a function that returns an array of strings denoting user_id's of suspicious users who were involved in at least threshold number of log times.
# The id's should be ordered ascending by numeric value

# Example
# logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
# threshold = 2

# The transaction count for each user, regardless of role are:
# ID  Transactions
# 99  3
# 88  2
# 12  1 
# 32  1

# There are two users with at least threshold = 2 transactions: 99 and 88. In ascending order, the return array is ['88', '99']
# Note: In the last log entry, user 12 was on both sides of the transaction. This counts as only 1 transaction for user 12.



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold


def processLogs(logs, threshold):
    # Write your code here
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


