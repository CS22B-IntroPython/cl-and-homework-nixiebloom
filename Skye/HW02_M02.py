### CS 22B Module 02 - Homework 2
### Name: Skye Gonigan

##### Homework practicing Control flow and Regular expression #####

## Import library
import re

##### Problem 1 - if/elif/else
## You are given a list of log lines. Classify each line into one of these buckets:
## - "ERROR": contains ERROR and an error code like E1234
## - "WARN": contains WARN and a module tag in brackets like [auth]
## - "INFO": contains INFO and a user id like user=ab_12
## - "SKIP": anything else
## Return a dictionary with counts per bucket.

lines = [
    "2026-02-11 10:00:01 ERROR E1042 [db] user=ab_12 msg=timeout",
    "2026-02-11 10:00:02 WARN [auth] user=xy_77 msg=bad password",
    "2026-02-11 10:00:03 INFO user=ab_12 msg=login ok",
    "2026-02-11 10:00:04 ERROR [api] msg=missing code",
    "garbage line"
]

### step 1: Define the count variables
#/b can be used to find whole workds
error_count = re.compile(r"\bERROR\b")
warn_count  = re.compile(r"\bWARN\b")
info_count  = re.compile(r"\bINFO\b")

### step 2: Initialize the count dictionary 
counts = {"ERROR": 0, "WARN": 0, "INFO": 0}

### step 3: Loop throught the dictionary with if-elif-else
for line in lines:
    if error_count.search(line):
       counts["ERROR"] += 1
    elif warn_count.search(line):
        counts["WARN"] += 1
    elif info_count.search(line):
        counts["INFO"] += 1
    else:
        pass

print(counts)


##### Problem 2 - Check passwords with boolean logic and regex
## Write a function check_password(pw) that returns one of:
# "STRONG" if:
# - length ≥ 10
# - contains at least 1 lowercase, 1 uppercase, 1 digit, 1 symbol from !@#$%^&*
# - does not contain whitespace
# otherwise "WEAK" 
## Test the function on a list of passwords using a loop

test_pw = ["Short7!", "LongerPass7!", "GoodPassw0rd!", "Bad Passw0rd!", "N0SymbolHereAAA"]

### step 1: Define variables
#length = len
#lowercase = re.search(r"[a-z]")
#uppercase = re.search(r"[A-Z]")
#digit_case = re.search(r"[0-9]")
#symbol_case = re.search(r"[!@#$%^&*]")
#space_case = not re.search(r"\s", pw)


### step 2: Write a function that check password (str) to test cases
def check_password(pw):
    length = len(pw) >= 10
    lowercase = re.search(r"[a-z]", pw)
    uppercase = re.search(r"[A-Z]", pw)
    digit_case = re.search(r"[0-9]",pw)
    symbol_case = re.search(r"[!@#$%^&*]", pw)
    space_case = not re.search(r"\s", pw)


    if length and lowercase and uppercase and digit_case and symbol_case and space_case:
        return "STRONG"
    else:
        return "WEAK"
       
### step 3: Use case. Test list test_pw

for pw in test_pw:
    print(f"{pw}: {check_password(pw)}")