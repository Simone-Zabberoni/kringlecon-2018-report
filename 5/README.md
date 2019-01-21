## Objective 5

> Using the data set contained in this [SANS Slingshot Linux image](https://download.holidayhackchallenge.com/HHC2018-DomainHack_2018-12-19.ova), find a reliable path from a Kerberoastable user to the Domain Admins group. What’s the user’s logon name (in username@domain.tld format)? Remember to avoid RDP as a control path as it depends on separate local privilege escalation flaws. 
> For hints on achieving this objective, please visit Holly Evergreen and help her with the CURLing Master Cranberry Pi terminal challenge

### Challenge


> Complete this challenge by submitting the right HTTP 
> request to the server at http://localhost:8080/ to 
> get the candy striper started again. You may view 
> the contents of the nginx.conf file in 
> /etc/nginx/, if helpful.

For this challenge you will need:

- HTTP2 Basics: https://developers.google.com/web/fundamentals/performance/http2/
- Chris Davis & Chris Elgee, HTTP2: Because 1 is the Loneliest Number: https://www.youtube.com/watch?v=9E-8HkDs-kQ&t=3s


First of all, try to curl and fail:
```
elf@6ffd29dc7375:~$ curl http://localhost:8080
   ����elf@6ffd29dc7375:~$ 
```
Looking at nginx.conf we can see that http2 is in action
```
server {
        # love using the new stuff! -Bushy
                listen                  8080 http2;
```


Let's curl again with `--http2-prior-knowledge`:
> It requires prior knowledge that the server supports HTTP/2 straight
away.

```
elf@6ffd29dc7375:~$ curl --http2-prior-knowledge  http://localhost:8080 
<html>
 <head>
  <title>Candy Striper Turner-On'er</title>
 </head>
 <body>
 <p>To turn the machine on, simply POST to this URL with parameter "status=on"

 
 </body>
</html>
```

Posting with URL parameters isn't well liked:
```
elf@6ffd29dc7375:~$ curl --http2-prior-knowledge  "http://localhost:8080?status=on"  -X POST
<html>
 <head>
  <title>Candy Striper Turner-On'er</title>
 </head>
 <body>
 <p>To turn the machine on, simply POST to this URL with parameter "status=on"

 <p>Hey, good job!  But I'm picky.  I'd rather just have you POST the status in the body of your request.

 </body>
</html>
```

So we post with `-d 'param=value`:
```
elf@6ffd29dc7375:~$ curl --http2-prior-knowledge  http://localhost:8080  -X POST -d'status=on'
<html>
 <head>
  <title>Candy Striper Turner-On'er</title>
 </head>
 <body>
 <p>To turn the machine on, simply POST to this URL with parameter "status=on"

                                                                                
                                                                okkd,          
                                                               OXXXXX,         
                                                              oXXXXXXo         
                                                             ;XXXXXXX;         
                                                            ;KXXXXXXx          
                                                           oXXXXXXXO           
                                                        .lKXXXXXXX0.           
  ''''''       .''''''       .''''''       .:::;   ':okKXXXXXXXX0Oxcooddool,   
 'MMMMMO',,,,,;WMMMMM0',,,,,;WMMMMMK',,,,,,occccoOXXXXXXXXXXXXXxxXXXXXXXXXXX.  
 'MMMMN;,,,,,'0MMMMMW;,,,,,'OMMMMMW:,,,,,'kxcccc0XXXXXXXXXXXXXXxx0KKKKK000d;   
 'MMMMl,,,,,,oMMMMMMo,,,,,,lMMMMMMd,,,,,,cMxcccc0XXXXXXXXXXXXXXOdkO000KKKKK0x. 
 'MMMO',,,,,;WMMMMMO',,,,,,NMMMMMK',,,,,,XMxcccc0XXXXXXXXXXXXXXxxXXXXXXXXXXXX: 
 'MMN,,,,,,'OMMMMMW;,,,,,'kMMMMMW;,,,,,'xMMxcccc0XXXXXXXXXXXXKkkxxO00000OOx;.  
 'MMl,,,,,,lMMMMMMo,,,,,,cMMMMMMd,,,,,,:MMMxcccc0XXXXXXXXXXKOOkd0XXXXXXXXXXO.  
 'M0',,,,,;WMMMMM0',,,,,,NMMMMMK,,,,,,,XMMMxcccckXXXXXXXXXX0KXKxOKKKXXXXXXXk.  
 .c.......'cccccc.......'cccccc.......'cccc:ccc: .c0XXXXXXXXXX0xO0000000Oc     
                                                    ;xKXXXXXXX0xKXXXXXXXXK.    
                                                       ..,:ccllc:cccccc:'      
                                                                               

Unencrypted 2.0? He's such a silly guy.
That's the kind of stunt that makes my OWASP friends all cry.
Truth be told: most major sites are speaking 2.0;
TLS connections are in place when they do so.

-Holly Evergreen
<p>Congratulations! You've won and have successfully completed this challenge.
<p>POSTing data in HTTP/2.0.
 </body>
</html>
```


**Hint**: BloodHound Tool: https://github.com/BloodHoundAD/BloodHound


### Objective completion

Import the OVF into your VmWare workstation (**important**: v12 does not work), boot it and launch the bloodhound tool.

According to the objective 
> find a reliable path from a Kerberoastable user to the Domain Admins group. What’s the user’s logon name (in username@domain.tld format)? Remember to avoid RDP as a control path as it depends on separate local privilege escalation flaws. 

From the the **Pre-Built Analytics Queries** select **Shortest Paths to Domain Admins from Kerberoastable Users**: you will see that the user `LDUBEJ00320@AD.KRINGLECASTLE.COM` has a direct path to Domain Admins without `CanRDP`

**Objective answer**: `LDUBEJ00320@AD.KRINGLECASTLE.COM`

