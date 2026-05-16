[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question regarding Line Sequential files on MF Cobol running under HP-UX

_9 messages · 7 participants · 2008-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** The Walrus <I_Am_The_Walrus@invalid.email.com>
- **Date:** 2008-02-15T02:45:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net>`

```
I have a very odd scenario that I have been asked to investigate in my 
job.  I am a technical support person and we are responsible for the 
installation and configuration of MF Cobol under HP-UX.  There is a 
program which is running in our production environment which opens a flat 
text file as LINE SEQUENTIAL, but it is really a SEQUENTIAL file.  That's 
not the issue here because the program doesn't do anything with the 
status of the open (I didn't write the code). The program redefines the 
main record and attempts to validate a part of it against a literal of 
"HDR".  The compiled code runs fine in production and under a "test" 
environment.  However, when I run the same program under any other 
environment it is unable to validate the literal as what it is retrieving 
fromt the file is a 0.  Apart from the COBSW variable, is there anything 
else I can check?  I'd like to tell our programmers that they need to 
change their code, and someday, I will.  But it's not having problems in 
our production environment.
comp.lang.cobol
I've spent 4 days on this problem and have come to the conclusion that it 
has something to do with the way that the "LINE SEQUENTIAL" file is being 
read, but all of my research has not revealed anything.

I am not able to post from work, but I can review responses and I will 
reply when I have usenet nntp access again.

Thanks for anyone who can help me with this.  Again, I didn't write the 
program and I know it's not good coding technique to open a file without 
checking the status of it, but it's not my code.
```

#### ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-02-15T06:06:46
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13raavm97bnsu3d@corp.supernews.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net>`

```
On Fri, 15 Feb 2008 02:45:50 +0000, The Walrus wrote:

> ... The program redefines the 
> main record and attempts to validate a part of it against a literal of 
…[3 more quoted lines elided]…
> from the file is a 0.

I don't think you are allowed to access the record field if you have not
read a record into it. I have seen this produce memory faults, random data
etc.

This is like the two legged dog - it's not surprising that it walks badly,
it's surprising it walks at all. With your program, it could crash any
time.

I kill-filed the off-topic discussions. This is a very quiet group now ;-)

Tim
```

##### ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-02-16T00:37:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61lbr2F206lc8U1@mid.individual.net>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net> <13raavm97bnsu3d@corp.supernews.com>`

```


"tim" <TimJ@internet.com> wrote in message 
news:13raavm97bnsu3d@corp.supernews.com...
> On Fri, 15 Feb 2008 02:45:50 +0000, The Walrus wrote:
>
…[16 more quoted lines elided]…
>

Sorry to hear that, Tim, although I understand your reasons.

Apart from the mindless evangelising of Judson sucking us all in, there have 
been some very good OT discussions in this group.

There are lively minds here and their opinions on things other than COBOL 
can be very interesting, even stimulating.

I hope you'll reconsider and simply mark the pointless threads as read... 
(select a message in the thread and press Ctrl/T, if you use Outlook. This 
marks all posts in that thread as read.)

Your contributions have been reasoned and valuable.

Pete.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-15T10:37:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3cb488f-e7ee-4b32-9687-994d6ff5cfdc@s13g2000prd.googlegroups.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net> <13raavm97bnsu3d@corp.supernews.com> <61lbr2F206lc8U1@mid.individual.net>`

```
On Feb 16, 12:37 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

>, if you use Outlook. ..

If you use Outlook then you are damned to hell for all eternity.

Oops, sorry, wrong thread.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-02-16T13:48:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61mq67F1vrh6aU1@mid.individual.net>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net> <13raavm97bnsu3d@corp.supernews.com> <61lbr2F206lc8U1@mid.individual.net> <f3cb488f-e7ee-4b32-9687-994d6ff5cfdc@s13g2000prd.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:f3cb488f-e7ee-4b32-9687-994d6ff5cfdc@s13g2000prd.googlegroups.com...
> On Feb 16, 12:37 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
>

Bugger! That's me gone then... :-)

Pete.
```

#### ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-15T06:19:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w9atj.227233$rl3.44003@fe02.news.easynews.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net>`

```
What exactly happens in those other environments?
```

#### ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-15T01:09:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hcar3h9aq6moqutrgs2rfjlv8im70rj20@4ax.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net>`

```
On 15 Feb 2008 02:45:50 GMT, The Walrus <I_Am_The_Walrus@invalid.email.com> wrote:

>I have a very odd scenario that I have been asked to investigate in my 
>job.  I am a technical support person and we are responsible for the 
>installation and configuration of MF Cobol under HP-UX.  There is a 
>program which is running in our production environment which opens a flat 
>text file as LINE SEQUENTIAL, but it is really a SEQUENTIAL file.  

The only difference is that line sequential has a newline at the end of each record, a
record sequential file (the default) does not, records are fixed length. When you edit the
file with vi , if you see more than one line, it's line sequential.

If it is only reading the first record, it can do so with EITHER file organization. That's
not the problem.

>That's 
>not the issue here because the program doesn't do anything with the 
>status of the open (I didn't write the code). 

Does the select say FILE STATUS? If not, the program will abort on open error or other
error. 

>The program redefines the 
>main record and attempts to validate a part of it against a literal of 
…[3 more quoted lines elided]…
>from the file is a 0.  

Sounds like it's not finding the file at open time. Exactly what does the select say after
ASSIGN TO?  If it is using an environment variable, what value is in that variable?

>Apart from the COBSW variable, is there anything 
>else I can check?

Check the filke pointed to by $COBCONFIG. That file contains runtime options. 
It is possible that prod and test cobconfig are setting an environment variable the
program is using in ASSIGN TO.  It is also possible they are sourcing in an environment
script that sets an environment value the program is using in ASSIGN TO.

> I'd like to tell our programmers that they need to 
>change their code, and someday, I will.  But it's not having problems in 
>our production environment.

If they specify FILE STATUS, they should check it. The alternative is remove it and let
the program abort.
```

##### ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-15T07:28:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ng4br3tq4751f2v8k6qrtioqvlo3rnq10t@4ax.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net> <8hcar3h9aq6moqutrgs2rfjlv8im70rj20@4ax.com>`

```
>On 15 Feb 2008 02:45:50 GMT, The Walrus <I_Am_The_Walrus@invalid.email.com> wrote:

>>Apart from the COBSW variable, is there anything  else I can check?

Maybe the program doesn't have read permission on the file or any directory between the
file and root. Log on as the same user and try to edit the file.
```

#### ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX

- **From:** "HeyBub" <heybub@gmail.com>
- **Date:** 2008-02-15T07:27:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13rb4qrk7epaf2e@corp.supernews.com>`
- **References:** `<47b4fcde$0$4047$9a566e8b@news.aliant.net>`

```
The Walrus wrote:
> I have a very odd scenario that I have been asked to investigate in my
> job.  I am a technical support person and we are responsible for the
…[17 more quoted lines elided]…
> file is being read, but all of my research has not revealed anything.

I'm confused. The program works in a production environment and in a test 
environment, but doesn't work in your environment. What is "your" 
enviornment if it isn't "test" or "production?" Under water?

Further, how are you opening this file? Input?

If you open the file as input and the file doesn't exist then you inspect 
the first record, you'll find garbage or initialization values - not 
anything from a file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
