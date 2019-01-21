
# KringleCon - SANS Christmas Hacking Challenge writeup - Simone Zabberoni
 
## Links

Game interface and badges: https://kringlecon.com/badge?section=objectives

History and answers: https://www.holidayhackchallenge.com/2018/story.html


## Report Format

Each objective has its own directory with its own `README.md` file describing all the steps for each objective and challenge.


### [Objective 1](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/1/README.md)
Read through the old CFPs to answer the questions.

Answer: `Happy Trails`


### [Objective 2](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/2/README.md)
Find the CSV via misconfigured server which exposes the cfp/ directory.

Answer: `John McClane`


### [Objective 3](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/3/README.md)
Use a de Bruijn 4-4 sequence to crack the code.

Answer: `Welcome unprepared speaker!`


### [Objective 4](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/4/README.md)
Use TruffleHog or explore the git log to find a deleted file with the passwords.

Answer: `Yippee-ki-yay`


### [Objective 5](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/5/README.md)
Boot the provided VM and use BloodHound to find a kerberoastable user to the domain admins.

Answer: `LDUBEJ00320@AD.KRINGLECASTLE.COM`


### [Objective 6](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/6/README.md)
Bypass the door code injecting SQL inside the QR code to get an authorized and enabled access.

Answer: `19880715`


### [Objective 7](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/7/README.md)
Upload a CSV file crafted with an injection attack to move the target file in a public website directory.

Answer: `Fancy Beaver`


### [Objective 8](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/8/README.md)
Analyze the backend code of packalyzer to obtain the SSL keylogs, the use it to decrypt http2 traffic and capture Alabaster's password.

Use Alabaster's account to logon and examine his captures to find the PDF with the answer.

Answer: `mary had a little lamb`


### [Objective 9](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/9/README.md)

##### Snort
Create snort rules to match all the malware communications

Answer: Match via snort PCRE the subdomain `77616E6E61636F6F6B69652E6D696E2E707331`


##### Download domain
Analyze the infected doc file do extract the malware loader and the domain from where it downloads the malware itself.

Answer: `erohetfanu.com`


##### The killswitch
Analyze the malware to find the domain name that acts as kill switch, then register it into HoHoHo Daddy

Answer: `Successfully registered yippeekiyaa.aaay!`


##### The vault password
Analyze the malware to understand how it encrypts the files and how it protects the encryption key. 

Get access to the attacker private key via dns and use it to decrypt the file encryption key, then decrypt alabaster's SQLite database.

Answer: `ED#ED#EED#EF#G#F#G#ABA#BA#B`


##### Access the vault
Play the vault password on the piano vault door, transposing it from the current E key to the wanted D key (Alabaster's favorite!)

Answer: `You have unlocked Santa's vault!`


### [Objective 10](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/10/README.md)
Read through the history to get the culprit

Answer: `Santa`


Simone Zabberoni