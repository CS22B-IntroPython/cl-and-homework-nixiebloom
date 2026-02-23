### This template is for the class exercises covered in M01_L02_review-files for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL1.1: Count the number of T in the sequence. 
sequence = "ATTGGCTATACCGG"
# ** your code **
T = "T"
num_T = sequence.count(T)
print(num_T)

##### CL1.2: For the sequence above, convert the sequence from the 4th character to the 9 character to lower case
# ** your code **
part1 = sequence[0:3]
lower1 = sequence[3:9].lower()
part2 =sequence[9:]
new_seq = part1+lower1+part2
print(new_seq)

##### CL1.3: Find the noncoding(4th to 9th character) and coding regions(all other characters)
## step 1: open the seq.txt file
# ** your code **
file_obj = open('/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/Module01_Essentials/seq.txt')
file_content = file_obj.read()
print(file_content)
non_coding = file_content[3:9]
non_coding = non_coding.lower()
coding_1 = file_content[0:3]
coding_2 = file_content [9:]
full_coding = coding_1 + coding_2
print("The non coding region is", non_coding)
print ("The coding region is", full_coding)


## step 2: create 2 new files for coding and noncoding
# ** your code **

with open("coding.txt","a") as c:
    c.write(full_coding)

with open("non_coding.txt","a") as n:
    n.write(non_coding)

## write to new files sequence 4-9 as lowercase to noncode file and all other sequence as uppercase to code file. Don't forget to close() to save the files.
# ** your code **

#This was completed above

##### CL1.4: Trim the adapter sequence (14 bp seq at front of each line “ATTCGATTATAAGC”)
## step 1: open the adapter_input.txt file
# ** your code **
ad_obj = open('/Users/skyaen/Documents/GitHub/CS22B_SP26_datafiles/Module01_Essentials/adapter_input.txt')

## step 2: create an output file
# ** your code **
tr_obj = open("trimmed.txt", "w")

## step 3: read in each line in the adapter_input file and trim the first 14 characters. Write the remaining sequence to the output file. Do this for each line. Don't forget to close() to save the file. 
adapter = "ATTCGATTATAAGC"

with ad_obj as infile, tr_obj as outfile:
    for line in infile:
       trimmed_line = line.replace(adapter,"")
       outfile.write(trimmed_line)