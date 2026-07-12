### BROKEN ACCESS CONTROL README ###

1)
There wasn't any handling for if the user couldn't be found, so I added extra handling. If a user could
not be found, it would crash the server completely. My fix handles a 404 issue and increases security. If something was searched for and it
didn't exist, it would just make the server go offline, and sacrifice the Availability.

2)
if the user id was passed in, and it's not in the database, it will pull the next closest option. if a client asks for user 56,
but there's only user 55, 54, 53 and so on, it'll return user 55.
User 55 could be literally anyone, and if they try it enough times (which they will) a hacker could find which user
id has the highest privileges. This is an example of Privilege Escalation.

3)
This had a few issues, namely with the algorithm (MD5) being very insecure, and with there being no generated salt
to go along with the hash. Without a secure algorithm, modern gpus can easily crack any hashing, and without a salt, all
hashes generated with the same set of characters will be the same, leading to some reverse engineering being feesible.
I fixed it by adding a salt, changing the algortihm to SHA256, and finally doing the calculations for hashing said password.

4)
sha1 is severely outdated for secure applications. I also applied utf-8 encoding for the password, just to make sure that it's
entered correctly. New and secure applications should use sha256 or something along the lines of the sha2-sha3 families, which produce
longer and more secure outputs.

5)
In this example, the data was being passed right into the database without being prepared. I fixed it by changing it to a prepared
statement in order to avoid SQL injections. This is a common practice that should be implemented in pretty much every single application.
Applications that do not use prepared statements allow user data to be directly inserted into the database without first being sanitized,
a process in which data is cleaned to avoid sql injection

6)
In this example, trusting query parameters could result into a json payload being passed in and execute things inside the database. Because of this,
I made sure to force the query to be a string to avoid json payloads. This means that if I were to pass in a malicious payload, it would only be recieved
as text and nothing harmful. This is similar to an SQL injection mainly because it is an sql injection.

7)
With the original code, you could change the password of absolutely anyone's account, and access it shortly after, because the email wasn't
validated to be yours. Because of this, I made sure to send an email with the theoretical sendEmail function to the user, to verify that 
the user did actually own the account. I also made sure to give them only 3 attempts to prevent brute force attacks.
Finally, I do one final check to make sure that the email is actually the same as the one the database sent back. This is a common order
of operations that pretty much every website uses to change passwords, because it's secure.

8)
If the site example.com gets comprimised, and the code gets changed, your site is also at risk now, because hackers are allowed to inject any sort of code into your site.
This can be especially bad, because it's almost a remote code execution exploit. This is a supply chain attack, where hackers target the providers
of code to a site when the site itself is too secure to be targeted. It also allows hackers to target hundreds if not thousands of sites
without having to hack each one individually.

9)
This is not a good idea. If someone were to input something like ".env" into this, and the file existed, it would print the entire .env folder.
This can also be used on ssh keys, and pretty much any other file in the system. There's ways to circumvent this, but I chose to
only allow requests that were from http or https. This is a little harder to circumvent if you do actually need certain files to be printed,
but it's definitely possible to do.

10)
This had 2 very big security flaws, namely that the passwords weren't hashed and that they were using the "equals" function. I don't know how they're hashing or not
hashing their passwords, so I just used a stand-in function, but I would go back and try to add a salt aswell to this to really make it secure.
The equals function is a bad practice, because it goes through each character and breaks as soon as a mismatch is found. This could be REALLY small variations,
but allows hackers to guess the way into the password. Instead, with hashes, it's a lot harder to do, but I still used isEqual which doesn't have this issue.
