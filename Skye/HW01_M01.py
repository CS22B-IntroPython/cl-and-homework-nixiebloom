### CS 22B Module 01 - Homework 1
### Name: Skye Gonigan

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters.

seq = open('/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/Module01_Essentials/adapter_reads.txt')
print(seq)

adapter = 'ATTCGATTATAAGC'
mod_seq = open("mod_seq.txt", "w")

with seq as infile, mod_seq as outfile:
    for line in infile:
       trimmed_line = line.replace(adapter,"")
       outfile.write(trimmed_line)

seq.close()
mod_seq.close()

## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file, bad_reads.txt. 

bases = {"A", "G", "C", "T"}
mod_seq = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/mod_seq.txt", "r")
clean = open("clean_reads.txt", "w")
bad = open("bad_reads.txt", "w")

#have to create set and change type to use command .issubset
#for read in mod_seq:
    #read = set(read.strip())

#this will let us validate without changing to set
valid_read = 0
invalid_read = 0

for line in mod_seq:
    read = line.strip()
    if read == '':
        continue

#setting up a parameter to test against
    is_valid = True
    for base in read:
        if base not in bases:
            is_valid = False
            break
    
    if is_valid:
        clean.write(read + '\n')
        valid_read += 1
        print("Valid Sequence")
    
    else:
        bad.write(read + '\n')
        invalid_read += 1
        print("Invalid Sequence")

mod_seq.close()
clean.close()
bad.close()

## 4. Print as output, the number of valid and invalid reads. 
#valid_reads = sum(1 for line in clean)
#invalid_reads = sum(1 for line in bad)

print(f"The number of valid reads is: ", valid_read)
print(f"The number of infvalid reads is: ", invalid_read)

##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read.
clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")

read_length = [len(read) for read in clean]
print(read_length)

## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length).
clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")

GC = [read.count('G' or 'C') for read in clean]
print(GC)

GC_content = [round(((GC/read_length)*100), 2) for GC, read_length in zip(GC, read_length)]
print(GC_content)

## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

min = min(read_length)
max = max(read_length)
avg_GC = (sum(GC_content)/len(GC_content))

print(f"The minimum length is ",min,".")
print(f"The maximum length is ",max,".")
print(f"The average GC content is ",round(avg_GC,2),".")

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads.

clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")

A_count = [read.count('A') for read in clean]
print(A_count)

clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")
G_count = [read.count('G') for read in clean]
print(G_count)

clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")
C_count = [read.count('C') for read in clean]
print(C_count)

clean = open("/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/clean_reads.txt", "r")
T_count = [read.count('T') for read in clean]
print(T_count)

total_A = sum(A_count)
total_G = sum(G_count)
total_C = sum(C_count)
total_T = sum(T_count)

totals = [total_A, total_G, total_C, total_T]

base_counts = {'A': total_A, 'G':total_G, 'C':total_C, 'T':total_T}

print(base_counts)

## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).

result = 1

for base, total in base_counts.items():
    result = total * result

print(result)

#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure.

def nt_content(seq, nt):
    count = seq.count(nt)
    percentage = (count/len(seq))*100
    rounded = round(percentage,2)
    print(f"The percentage of",nt,"is",rounded,".")
    return rounded
    
nt_content('AATT', 'A')
 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.

assert nt_content('AATT', 'A') == 50.0
assert nt_content('ACCG','T') == 0.00
assert nt_content('ACCT','A') == 25.0

## Use this sequence as your test sequence
sequence = 'TTATAAGCCGATTATAAGCCCGTAACCGGTTAG'

nt_content(sequence,'A')
