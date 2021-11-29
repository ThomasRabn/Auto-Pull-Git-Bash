import subprocess
from subprocess import check_output

filename = "./repos.txt"

# We open the repos.txt file
with open(filename) as file:
    # For each line, we pull the repo
    for line in file:
        line = line.rstrip()
        print(line)
        i = 0
        # For each character, if it is a backslash, we double it
        while i < len(line):
            if line[i] == '\\':
                line = line[:i] + "\\" + line[i:]
                i +=2 
            else:
                i+=1

        # We run the pull and print the output
        print(check_output("\"C:\\Program Files\\Git\\bin\\sh.exe\" --cd=\"" + line + "\" -c \"git pull\"", shell=True).decode())
        print("---------------------------------\n")

print("Every given repo has been pulled!")