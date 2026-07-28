Secret Scanner is a quick CLI utility that scans a file or directory to see if there's any private keys in plain text within the directory, 
or if there's any Google Authentication Credentials. To run it, first install it and then run it with python, and then select a directory to scan.
Please Note that scanning may take a long time for very large directories, however in my testing I've experienced extremely fast speeds to completion.

At the current point, it will not be able to find other types of credentials, however if you want to expand the list, you can add all sorts of regex
searches to check for by modifying the source code.

If you experience any issues, please reach out and I can correct them quickly.
