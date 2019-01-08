## Objective 4

> Retrieve the encrypted ZIP file from the [North Pole Git repository](https://git.kringlecastle.com/Upatree/santas_castle_automation). What is the password to open this file? 
> For hints on achieving this objective, please visit Wunorse Openslae and help him with Stall Mucking Report Cranberry Pi terminal challenge.

### Challenge


> There's a samba share here on this terminal screen.
> What I normally do is to upload the file,
> With our network credentials (we've shared for a while).
> When I try to remember, my memory's clean!

> Complete this challenge by uploading the elf's report.txt
> file to the samba share at //localhost/report-upload/

For this challenge you will need:

- Commandline passwords: https://blog.rackspace.com/passwords-on-the-command-line-visible-to-ps

We don't have account for `//localhost/report-upload/`, let's check for any current mount:
```
elf@ee159e1af85f:~$ ps ax 
  PID TTY      STAT   TIME COMMAND
    1 pts/0    Ss     0:00 /bin/bash /sbin/init
   11 pts/0    S      0:00 sudo -u manager /home/manager/samba-wrapper.sh --verbosity=none --no-ch
   17 pts/0    S      0:00 /bin/bash /home/manager/samba-wrapper.sh --verbosity=none --no-check-ce
   19 pts/0    S      0:00 sudo -u elf /bin/bash
   20 pts/0    S      0:00 /bin/bash
   24 ?        Ss     0:00 /usr/sbin/smbd
   25 ?        S      0:00 /usr/sbin/smbd
   26 ?        S      0:00 /usr/sbin/smbd
   28 ?        S      0:00 /usr/sbin/smbd
   87 pts/0    S      0:00 sleep 60
   88 pts/0    R+     0:00 ps ax
```

Pids 11 and 17 are interesting:

```
elf@ee159e1af85f:~$ ps -fwwp 11
UID        PID  PPID  C STIME TTY          TIME CMD
root        11     1  0 22:20 pts/0    00:00:00 sudo -u manager /home/manager/samba-wrapper.sh --verbosity=none --no-check-certificate --extraneous-command-argument --do-not-run-as-tyler --accept-sage-advice -a 42 -d~ --ignore-sw-holiday-special --suppress --suppress //localhost/report-upload/ directreindeerflatterystable -U report-upload
elf@ee159e1af85f:~$ ps -fwwp 17
UID        PID  PPID  C STIME TTY          TIME CMD
manager     17    11  0 22:20 pts/0    00:00:00 /bin/bash /home/manager/samba-wrapper.sh --verbosity=none --no-check-certificate --extraneous-command-argument --do-not-run-as-tyler --accept-sage-advice -a 42 -d~ --ignore-sw-holiday-special --suppress --suppress //localhost/report-upload/ directreindeerflatterystable -U report-upload
```

And we got both the user (`report-upload`) and the password (`directreindeerflatterystable`), let's use them to upload the report:

```
elf@ee159e1af85f:~$ smbclient //localhost/report-upload -U report-upload
WARNING: The "syslog" option is deprecated
Enter report-upload's password: 
Domain=[WORKGROUP] OS=[Windows 6.1] Server=[Samba 4.5.12-Debian]
smb: \> put report.txt
putting file report.txt as \report.txt (250.5 kb/s) (average 250.5 kb/s)
smb: \> Terminated
elf@ee159e1af85f:~$ 

                                                                         
                               .;;;;;;;;;;;;;;;'                               
                             ,NWOkkkkkkkkkkkkkkNN;                             
                           ..KM; Stall Mucking ,MN..                           
                         OMNXNMd.             .oMWXXM0.                        
                        ;MO   l0NNNNNNNNNNNNNNN0o   xMc                        
                        :MO                         xMl             '.         
                        :MO   dOOOOOOOOOOOOOOOOOd.  xMl             :l:.       
 .cc::::::::;;;;;;;;;;;,oMO  .0NNNNNNNNNNNNNNNNN0.  xMd,,,,,,,,,,,,,clll:.     
 'kkkkxxxxxddddddoooooooxMO   ..'''''''''''.        xMkcccccccllllllllllooc.   
 'kkkkxxxxxddddddoooooooxMO  .MMMMMMMMMMMMMM,       xMkcccccccllllllllllooool  
 'kkkkxxxxxddddddoooooooxMO   '::::::::::::,        xMkcccccccllllllllllool,   
 .ooooollllllccccccccc::dMO                         xMx;;;;;::::::::lllll'     
                        :MO  .ONNNNNNNNXk           xMl             :lc'       
                        :MO   dOOOOOOOOOo           xMl             ;.         
                        :MO   'cccccccccccccc:'     xMl                        
                        :MO  .WMMMMMMMMMMMMMMMW.    xMl                        
                        :MO    ...............      xMl                        
                        .NWxddddddddddddddddddddddddNW'                        
                          ;ccccccccccccccccccccccccc;                          
                                                                               



You have found the credentials I just had forgot,
And in doing so you've saved me trouble untold.
Going forward we'll leave behind policies old,
Building separate accounts for each elf in the lot.

-Wunorse Openslae
```


**Hint**: TruffleHog: https://github.com/dxa4481/truffleHog


### Objective completion

Let's clone the repo and install the trufflehog tool:

```
# git clone https://git.kringlecastle.com/Upatree/santas_castle_automation.git
Cloning into 'santas_castle_automation'...
[cut]

# pip install trufflehog
[cut]
```

The easiest thing to do is to launch `trufflehog` and inspect the output until something interesting shows up:

```
# trufflehog santas_castle_automation | less

+Our Lead InfoSec Engineer Bushy Evergreen has been noticing an increase of brute force attacks in our logs. Furthermore, Albaster discovered and published a vulnerability with our password length at the last Hacker Conference.
+
+Bushy directed our elves to change the password used to lock down our sensitive files to something stronger. Good thing he caught it before those dastardly villians did!
+
+
+Hopefully this is the last time we have to change our password again until next Christmas.
+
+
+
+
+Password = 'Yippee-ki-yay'
+
+
+Change ID = 'ESC[93m9ed54617547cfca783e0f81f8dc5c927e3d1e3ESC[0m'
```

Lookup for the zip file and unzip it:

```
# find . -name *.zip
./santas_castle_automation/schematics/ventilation_diagram.zip

# 7za l ./santas_castle_automation/schematics/ventilation_diagram.zip

7-Zip (a) [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,2 CPUs Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz (806E9),ASM,AES-NI)

Scanning the drive for archives:
1 file, 740409 bytes (724 KiB)

Listing archive: ./santas_castle_automation/schematics/ventilation_diagram.zip

--
Path = ./santas_castle_automation/schematics/ventilation_diagram.zip
Type = zip
Physical Size = 740409

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2018-12-07 20:01:38 D....            0            0  ventilation_diagram
2018-12-07 19:37:58 .....       415586       366995  ventilation_diagram/ventilation_diagram_2F.jpg
2018-12-07 19:37:43 .....       421604       372752  ventilation_diagram/ventilation_diagram_1F.jpg
------------------- ----- ------------ ------------  ------------------------
2018-12-07 20:01:38             837190       739747  2 files, 1 folders

# 7za e ./santas_castle_automation/schematics/ventilation_diagram.zip

7-Zip (a) [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,2 CPUs Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz (806E9),ASM,AES-NI)

Scanning the drive for archives:
1 file, 740409 bytes (724 KiB)

Extracting archive: ./santas_castle_automation/schematics/ventilation_diagram.zip
--
Path = ./santas_castle_automation/schematics/ventilation_diagram.zip
Type = zip
Physical Size = 740409


Enter password (will not be echoed):
Everything is Ok

Folders: 1
Files: 2
Size:       837190
Compressed: 740409

```

Another more manual way could be to search the git log for interesting deletions:

```
# cd santas_castle_automation/
# git log --diff-filter=D --summary
[cut]
commit 714ba109e573f37a6538beeeb7d11c9391e92a72
Author: Shinny Upatree <shinny.upatree@kringlecastle.com>
Date:   Tue Dec 11 07:23:36 2018 +0000

    removing accidental commit

 delete mode 100644 schematics/files/dot/PW/for_elf_eyes_only.md
[cut]
```

Then search the git log for the commit before:

```
git log | more
[cut]
commit 714ba109e573f37a6538beeeb7d11c9391e92a72
Author: Shinny Upatree <shinny.upatree@kringlecastle.com>
Date:   Tue Dec 11 07:23:36 2018 +0000

    removing accidental commit

commit 5f4f64140ee1388b4cccee577a6afd0b797bfff3
Author: Shinny Upatree <shinny.upatree@kringlecastle.com>
Date:   Mon Dec 10 21:20:01 2018 -1000

    adding AI & ML test scripts
```

Let's go back in time before the deletion:

```
# git checkout 5f4f64140ee1388b4cccee577a6afd0b797bfff3
Note: checking out '5f4f64140ee1388b4cccee577a6afd0b797bfff3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD is now at 5f4f641... adding AI & ML test scripts


# cat schematics/files/dot/PW/for_elf_eyes_only.md
Our Lead InfoSec Engineer Bushy Evergreen has been noticing an increase of brute force attacks in our logs. Furthermore, Albaster discovered and published a vulnerability with our password length at the last Hacker Conference.

Bushy directed our elves to change the password used to lock down our sensitive files to something stronger. Good thing he caught it before those dastardly villians did!


Hopefully this is the last time we have to change our password again until next Christmas.




Password = 'Yippee-ki-yay'


Change ID = '9ed54617547cfca783e0f81f8dc5c927e3d1e3'
```


**Objective answer**: `Yippee-ki-yay`

