## Objective 3

> The KringleCon Speaker Unpreparedness room is a place for frantic speakers to furiously complete their presentations. The room is protected by a [door passcode](https://doorpasscoden.kringlecastle.com/). Upon entering the correct passcode, what message is presented to the speaker?
> For hints on achieving this objective, please visit Tangle Coalbox and help him with Lethal ForensicELFication Cranberry Pi terminal challenge.



### Challenge

> Certain text editors can leave some clue.
> Did our young Romeo leave one for you?

> Find the first name of the elf of whom a love poem 
> was written.  Complete this challenge by submitting 
> that name to runtoanswer.

For this challenge you will need:

- Vim artifacts: https://tm4n6.com/2017/11/15/forensic-relevance-of-vim-artifacts/


Check `.viminfo` for clues:

```
more .viminfo

# This viminfo file was generated by Vim 8.0.
# You may edit it if you're careful!

# Viminfo version
|1,4

# Value of 'encoding' when this file was written
*encoding=utf-8


# hlsearch on (H) or off (h):
~h
# Last Substitute Search Pattern:
~MSle0~&Elinore

# Last Substitute String:
$NEVERMORE

# Command Line History (newest to oldest):
:wq
|2,0,1536607231,,"wq"
:%s/Elinore/NEVERMORE/g
|2,0,1536607217,,"%s/Elinore/NEVERMORE/g"
:r .secrets/her/poem.txt
|2,0,1536607201,,"r .secrets/her/poem.txt"
:q
|2,0,1536606844,,"q"
:w
|2,0,1536606841,,"w"
:s/God/fates/gc
|2,0,1536606833,,"s/God/fates/gc"
:%s/studied/looking/g
|2,0,1536602549,,"%s/studied/looking/g"
:%s/sound/tenor/g
|2,0,1536600579,,"%s/sound/tenor/g"
:r .secrets/her/poem.txt
|2,0,1536600314,,"r .secrets/her/poem.txt"
[cut]
```

The last substitute pattern seems relevant:
```
# Last Substitute Search Pattern:
~MSle0~&Elinore
```

Pass it to `runtoanswer`:

```
elf@04dd4a984da0:~$ runtoanswer 
Loading, please wait......



Who was the poem written about? Elinore


WWNXXK00OOkkxddoolllcc::;;;,,,'''.............                                 
WWNXXK00OOkkxddoolllcc::;;;,,,'''.............                                 
WWNXXK00OOkkxddoolllcc::;;;,,,'''.............                                 
WWNXXKK00OOOxddddollcccll:;,;:;,'...,,.....'',,''.    .......    .''''''       
WWNXXXKK0OOkxdxxxollcccoo:;,ccc:;...:;...,:;'...,:;.  ,,....,,.  ::'....       
WWNXXXKK0OOkxdxxxollcccoo:;,cc;::;..:;..,::...   ;:,  ,,.  .,,.  ::'...        
WWNXXXKK0OOkxdxxxollcccoo:;,cc,';:;':;..,::...   ,:;  ,,,',,'    ::,'''.       
WWNXXXK0OOkkxdxxxollcccoo:;,cc,'';:;:;..'::'..  .;:.  ,,.  ','   ::.           
WWNXXXKK00OOkdxxxddooccoo:;,cc,''.,::;....;:;,,;:,.   ,,.   ','  ::;;;;;       
WWNXXKK0OOkkxdddoollcc:::;;,,,'''...............                               
WWNXXK00OOkkxddoolllcc::;;;,,,'''.............                                 
WWNXXK00OOkkxddoolllcc::;;;,,,'''.............                                 

Thank you for solving this mystery, Slick.
Reading the .viminfo sure did the trick.
Leave it to me; I will handle the rest.
Thank you for giving this challenge your best.

-Tangle Coalbox
-ER Investigator

Congratulations!
```



**Hint**: De Bruijns sequence generator: http://www.hakank.org/comb/debruijn.cgi

Also, check Wikipedia: https://en.wikipedia.org/wiki/De_Bruijn_sequence

### Objective completion

You need to insert the correct code at https://doorpasscoden.kringlecastle.com/ which happens to be a De Bruijn code.

Open the browser debug console and click on the symbols: you'll se the cyclic append of symbols:

```
Passcode: 0
(index):86 Passcode: 01
(index):86 Passcode: 012
(index):86 Passcode: 0123
```

And their respective mapping:
- triangle = 0
- square = 1
- circle = 2
- star = 3

Also, note the network connections:
```
https://doorpasscoden.kringlecastle.com/checkpass.php?i=0123&resourceId=undefined
```

And the resulting json
```
{"success":false,"message":"Incorrect guess."}
```

So, we're dealing with a De Bruijn code with:
- lenght 4
- 4 alphabet symbols

Open the De Bruijn code generator and set it for k=4, n=4 to obtain the sequence:
```
0 0 0 0 1 0 0 0 2 0 0 0 3 0 0 1 1 0 0 1 2 0 0 1 3 0 0 2 1 0 0 2 2 0 0 2 3 0 0 3 1 0 0 3 2 0 0 3 3 0 1 0 1 0 2 0 1 0 3 0 1 1 1 0 1 1 2 0 1 1 3 0 1 2 1 0 1 2 2 0 1 2 3 0 1 3 1 0 1 3 2 0 1 3 3 0 2 0 2 0 3 0 2 1 1 0 2 1 2 0 2 1 3 0 2 2 1 0 2 2 2 0 2 2 3 0 2 3 1 0 2 3 2 0 2 3 3 0 3 0 3 1 1 0 3 1 2 0 3 1 3 0 3 2 1 0 3 2 2 0 3 2 3 0 3 3 1 0 3 3 2 0 3 3 3 1 1 1 1 2 1 1 1 3 1 1 2 2 1 1 2 3 1 1 3 2 1 1 3 3 1 2 1 2 1 3 1 2 2 2 1 2 2 3 1 2 3 2 1 2 3 3 1 3 1 3 2 2 1 3 2 3 1 3 3 2 1 3 3 3 2 2 2 2 3 2 2 3 3 2 3 2 3 3 3 3 (0 0 0) 
```

Now you can insert the codes in sequence by hand or write a python script (see [`bru.py`](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/3/bru.py)) to do the job for you:

```
# python bru.py
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0000&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0001&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0010&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0100&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=1000&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0002&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0020&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0200&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=2000&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0003&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0030&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0300&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=3001&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0011&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0110&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=1100&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=1001&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0012&resourceId=undefined
Trying: https://doorpasscoden.kringlecastle.com/checkpass.php?i=0120&resourceId=undefined
Code found: 0120
{u'resourceId': u'undefined', u'message': u'Correct guess!', u'hash': u'0273f6448d56b3aba69af76f99bdc741268244b7a187c18f855c6302ec93b703', u'success': True}
```

Insert the code in the web page to get the answer!

**Objective answer**: `Welcome unprepared speaker!`
