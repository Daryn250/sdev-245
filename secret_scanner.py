# secret scanner
import re
import os
from pathlib import Path

# global variables
is_directory = None

# get all files in a path and search recursively through directories
def get_all_files(path):
    if is_directory: 
        to_check = [path]
        files = []
        # while we still have directories to check, continue
        while to_check!=[]:
            item = to_check[0]
            if item.is_dir():
                for i in item.iterdir():
                    if i not in to_check:
                        to_check.append(i)
            else:
                files.append(item)

            to_check.remove(item)
    else:
        return [path] # we don't have to worry about sorting through directories.
    return files


# the different regex tests that we try. More can be easily added.
regex_tests = [
    "-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----",  # private keys
    "\\b(?:A3T[A-Z0-9]|AKIA|ASIA|ABIA|ACCA)[A-Z2-7]{16}\\b",                   # AWS access key
    "\\bAIza[0-9A-Za-z_-]{35}\\b",                                             # Google API key
    "\\b[0-9]+-[0-9a-z]{32}\\.apps\\.googleusercontent\\.com\\b",              # Google OAUTH client ID
    "\\bGOCSPX-[0-9A-Za-z_-]{28}\\b"                                           # Google OAUTH client secret
    ]

def check_common_secrets(files):
    secrets_scraped = []
    for file in files:
        print(f"processing file {file} ({round(os.path.getsize(file)/1000, 2)} kb)") # debugging and processing statements
        try:
            text = file.read_text()
            for regex in regex_tests:
                x = re.findall(regex, text)
                if x != []:
                    for item in x:
                        secrets_scraped.append([text, file, x])
        except Exception as e:
            print(f"Error: {e}. Continuing...") # usually happens when not a text file or other kind of default file python can read

    return secrets_scraped

            
        
while True:
    input_data = input("Input a file or directory to search for Secrets! \nPath: ")
    path = Path(input_data)
    if path.exists():
        if path.is_dir():
            is_directory = True # if the path is a directory, we'll have to search it.
        else:
            is_directory = False
        break
    else:
        print("Could not resolve path. Please Try Again. \n")

files = get_all_files(path)
secrets = check_common_secrets(files)

print("Completed Tasks! \n\n\nSecrets Found:")
for key in secrets:
    print(f"File {key[1]} has secret {key[2]}: \n{key[0]}\n")