[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_9 messages · 5 participants · 2008-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

- **From:** "SeaSideSam" <SeaSideSam@TheBeach>
- **Date:** 2008-02-14T23:06:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET>`

```
in my rm/cobol v6.5 users guide page 10-28 (configuration/run-seq-files/default-type) says that the runtime defaults to binary-sequential unless the file is specifically specified as line-sequential or the runtime config file specifies default-type as line-sequential.  your scenerio pretty much rules out a specific declaration, which leaves a config file situation.  easy to verify.  easy to resolve.

hope this helps.

have a good day.



--------------=  Posted using GrabIt  =----------------
------=  Binary Usenet downloading made easy =---------
-=  Get GrabIt for free from http://www.shemes.com/  =-
```

#### ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-15T07:42:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET>`

```
On Thu, 14 Feb 2008 23:06:22 -0600, "SeaSideSam" <SeaSideSam@TheBeach> wrote:

>in my rm/cobol v6.5 users guide page 10-28 (configuration/run-seq-files/default-type) says that the runtime defaults to binary-sequential unless the file is 
>specifically specified as line-sequential or the runtime config file specifies default-type as line-sequential.  your scenerio pretty much rules out a specific declaration, 
>which leaves a config file situation.  easy to verify.  easy to resolve.

He said the file is line sequential, which means the program is NOT taking the default.
```

##### ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

- **From:** Baba O'Reilly <none@purple3377.local>
- **Date:** 2008-02-16T01:58:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47b64346$0$4071$9a566e8b@news.aliant.net>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com>`

```
On 2008-02-15, Robert <no@e.mail> wrote:
> On Thu, 14 Feb 2008 23:06:22 -0600, "SeaSideSam" <SeaSideSam@TheBeach> wrote:
>
…[5 more quoted lines elided]…
>
Finally back in regular usenet mode.  I saw all the great responses to my question and I thank all
for their input.

Perhaps to clarify things a bit, I might explain our environment a bit better.

Production is an HP-UX box.
Development is an HP-UX box.

On production, there is one environment, /prod
On development there are many.  For example, a user fred would have access to 
/home/fred/
/prod
/main  (maintenance - used to fix production crashes)
/accp
/intg1 (integration testing...there are 16 of these).

So if fred wants to run a program in his home schema, he compiles it and drops
the executable in the proper directory.  Then he submits his job to the job submission process
which then executes it.

Now, if fred is trying to fix a problem, he would drop his compiled code in gthe
maintenance region's executable directory, and submit his job to the job submission process, but
this time, he would specify that he want to run the maintenance version.

What I did was to take the program in question and strip out all the fluff (application specific stuff) 
and add some file status checks etc. just to make the program more readable.
I also added some displays so that I could see what is going on.  
The main input file is NOT a line sequential file, but the program is compiled with the
LINE SEQUENTIAL specification turned on.  If I run this program in my home directory, I get
the results I expect regardless of whether the program is compiled with LINE SEQUENTIAL or
SEQUENTIAL.  It doesn't matter, it just works.  But, if I run the program in the maintenance
area I don't get what I expect.  There is only one record in the file and it can be read
but things aren't where I expect them to be.

So my solution was to tell the programmers to fix their code.  If they fix their program
so that it is SEQUENTIAL, rather than LINE SEQUENTIAL, then we can at least eliminate that
as the problem.  The idea of a ticking time bomb is what I was concerned about.  Just becuase
the program is working today in production, if we can't trust the results on the dev side, who's
to say that someday the code won't suddenly croak in production.

Anyway, to all those who tried to help, I say thanks, but I think I'm going to close this one
off, at least until I'm working with error-free code.

cheers 
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-15T20:45:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net>`

```
On 16 Feb 2008 01:58:31 GMT, Baba O'Reilly <none@purple3377.local> wrote:

>On 2008-02-15, Robert <no@e.mail> wrote:
>> On Thu, 14 Feb 2008 23:06:22 -0600, "SeaSideSam" <SeaSideSam@TheBeach> wrote:
…[25 more quoted lines elided]…
>which then executes it.

Why can't Fred run the job directly? It sounds like your shop is under 'mainframe
tyranny', where the scheduler runs on a mainframe, which kicks off Unix jobs via Tuxedo or
similar. 

>Now, if fred is trying to fix a problem, he would drop his compiled code in gthe
>maintenance region's executable directory, and submit his job to the job submission process, but
…[10 more quoted lines elided]…
>but things aren't where I expect them to be.

What does that mean? This isn't black magic. If the file is readable, the first record
will appear in the record area. 

>So my solution was to tell the programmers to fix their code.  If they fix their program
>so that it is SEQUENTIAL, rather than LINE SEQUENTIAL, then we can at least eliminate that
>as the problem.  The idea of a ticking time bomb is what I was concerned about.  Just becuase
>the program is working today in production, if we can't trust the results on the dev side, who's
>to say that someday the code won't suddenly croak in production.

It sounds like the program is checking to see whether the file exists, is readable, and
the first record contains 'HDR'. If any of those conditions are false, they don't want to
abort the job, they want to set a flag false. They could do all that with a single line of
ksh script; a Cobol program isn't necessary. 

set valid_file = `[ -a filename ] && sed ...

>Anyway, to all those who tried to help, I say thanks, but I think I'm going to close this one
>off, at least until I'm working with error-free code.

Whip them programmers into shape. Bye.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_(reply depth: 4)_

- **From:** The Walrus <I_Am_The_Walrus@invalid.email.com>
- **Date:** 2008-02-16T03:05:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47b652fb$0$4053$9a566e8b@news.aliant.net>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net> <8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com>`

```
On Fri, 15 Feb 2008 20:45:06 -0600, Robert wrote:

> Why can't Fred run the job directly? It sounds like your shop is under
> 'mainframe tyranny', where the scheduler runs on a mainframe, which
> kicks off Unix jobs via Tuxedo or similar.

Close... before I arrived on the scene, the company I work for decided to 
outsource their Y2K conversion so that they could take MF JCL and convert 
it to "something" that would run on Unix but have the same functionality 
of the MF stuff.  When I say "submit to the scheduller", I mean we run a 
script that invokes the job manager which takes the "jcl" and runs it.  
On our production box, it's Maestro that's responsible for this as no 
jobs are run "by hand".  Funny thing is, that if I write a ksh script and 
have it run the Cobol, it works no matter where I run it from..so that's 
why I'm worried..  converting to ksh isn't an option, although I've been 
through an exercise that has proven that we could run everything using 
ksh.

A programmer writes a piece of JCL and calls it FILE.CS  (don't ask what 
the CS stands for).  He/She submits that to the job manager using
either sub (a script) or via sudo -u .... sub ....
sub takes the .CS and sends it to the scheduller called cjm which runs 
the JCL as if it was running on the mainframe, down to the ability to 
have generation data groups.



> What does that mean? This isn't black magic. If the file is readable,
> the first record will appear in the record area.

And it does, but the program in question is expecting to see 'HDR ' in 
bytes 9-12.  The first 8 bytes of the line are binary 0's or something 
like that.  The fd would be

01  et-in-rec.
  02  et-in-part-1   pic x(8).
  02  et-in-part-2   pic x(4).
  02  FILLER         PIC X(243).

but since when the record is read in, the program can't see 'HDR ' in et-
in-part-2 it's invoking an abort routine.

If you vi the file you see something like

 HDR 000002193100039992000   

The first 8 characters, when viewed in hex are I think binary zeros, but
there's still 8 bytes of them so regardless,  et-in-part-2 should show 
'HDR ' 

I have a document at work that I wrote up when I presented my finding to 
the programmers.  I'll grab that tomorrow and add it it here.


> It sounds like the program is checking to see whether the file exists,
> is readable, and the first record contains 'HDR'. If any of those
> conditions are false, they don't want to abort the job, they want to set
> a flag false. They could do all that with a single line of ksh script; a
> Cobol program isn't necessary.

But the real program does a whole lot more than just check the contents 
of the record.  It's doing a read out to an Oracle table and formating a 
report with the information it is finding in the file.

> Whip them programmers into shape. Bye.

I used to be one... this program, the one I am trying to figure out is 
one of the worst coded Cobol programs I've ever seen.  I've always been 
told that when ever you open a file, or read a record, or even close the 
file, you should check the File Status.  But this program isn't even 
specifying that there is a File Status... but that's just my opinion.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-02-16T23:26:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61ns3kF20ddv9U1@mid.individual.net>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net> <8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com> <47b652fb$0$4053$9a566e8b@news.aliant.net>`

```


"The Walrus" <I_Am_The_Walrus@invalid.email.com> wrote in message 
news:47b652fb$0$4053$9a566e8b@news.aliant.net...
> On Fri, 15 Feb 2008 20:45:06 -0600, Robert wrote:
>
…[70 more quoted lines elided]…
>

If the file is defined as LINE SEQUENTIAL it is not expected to have a 
length count at the start of it. The record terminates with CR/LF or 
whatever "terminator" is defined for your OS. (If it is a SEQUENTIAL file, 
it IS expected to have a length count.) The length count is usually 8 bytes 
(depends on the system we are talking about; I THINK it is 8 bytes on 
MicroFocus but it is many years since I wrote MicroFocus COBOL.)

It seems to me that your COBOL definition has been written to accommodate a 
SEQUENTIAL file, but you are reading a LINE SEQUENTIAL file (or vice versa). 
This results in the misplacement of data which you describe.

There are a number of factors that can control this: The COBOL definition, 
the Compiler options, and the OS.

That's probably why it works "sometimes"...

Basically, the program definition needs to match the file definition, and 
vice versa.

Pete.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-16T14:02:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7eer31b49o4t7h22k80tuebj7f3ovpsbi@4ax.com>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net> <8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com> <47b652fb$0$4053$9a566e8b@news.aliant.net>`

```
On 16 Feb 2008 03:05:31 GMT, The Walrus <I_Am_The_Walrus@invalid.email.com> wrote:

>On Fri, 15 Feb 2008 20:45:06 -0600, Robert wrote:
>
…[7 more quoted lines elided]…
>of the MF stuff. 

Realia, still sold by Computer Associates, offers 100% JCL compatibility off the shelf.

> When I say "submit to the scheduller", I mean we run a 
>script that invokes the job manager which takes the "jcl" and runs it.  
…[5 more quoted lines elided]…
>ksh.

We have the same situation -- a mainframe scheduler running Unix jobs through Maestro. We
have one job that runs fine on three out of four production machines, and every test
machine. It crashes with a memory protection error (114) on one production machine. I
determined it's crashing inside SyncSort, which is called by a Cobol SORT verb. The
program runs fine when launched from a ksh script or menu program NOT started by Maestro. 

It seems like a simple problem, there must be something different in the environment set
up by Maestro. I said stick an 'env' in the Maestro script so I can figure out what the
difference is. That's too easy, they'd rather play Finger Pointing. They don't want to
know WHAT the problem is, they want to know WHO is at fault. 

Six months later, it still isn't fixed. Each time they run it directly on Unix, they have
to get special permission from some big shot. 

What's even funnier is we're the company that created Unix. Why are we scheduling jobs
through a mainframe? 

>A programmer writes a piece of JCL and calls it FILE.CS  (don't ask what 
>the CS stands for).  He/She submits that to the job manager using
…[3 more quoted lines elided]…
>have generation data groups.

We don't go through the mainframe scheduler in development and test, only in prod. 

>> What does that mean? This isn't black magic. If the file is readable,
>> the first record will appear in the record area.
…[3 more quoted lines elided]…
>like that. 

Problem solved! By default, nulls are removed from line sequential files, causing the rest
of the record to be shifted left. You can turn that off by entering 
INSERTNULL=OFF in the file handler configuration file. 

Environment variable $EXTFH points to the configuration file. If $EXTFH is not set, the
default location is $COBDIR/etc/extfh.cfg

Check that file on your production machine. I'm sure you'll find the INSERTNULL option.
If you don't have write permission on the non-working machines, copy it to your home and
set EXTFH=~/extfh.cfg

>> Whip them programmers into shape. Bye.
>
…[4 more quoted lines elided]…
>specifying that there is a File Status... but that's just my opinion.

You ERRONEOUSLY think that the absence of File Status means errors will go undetected and
unhandled. In fact, if an error occurs and there IS NO File Status, the Micro Focus file
system aborts the job with an appropriate message such as "Open error on file xxxxxxx". 

If that's all the program is going to do, which is usually the case, it's easier to let
Micro Focus do it for you.
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_(reply depth: 6)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-02-17T14:40:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lovgr35qs4emanvt0i1r98ca2pipj99lh2@4ax.com>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net> <8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com> <47b652fb$0$4053$9a566e8b@news.aliant.net> <j7eer31b49o4t7h22k80tuebj7f3ovpsbi@4ax.com>`

```
On Sat, 16 Feb 2008 14:02:52 -0600, Robert <no@e.mail> wrote:

>On 16 Feb 2008 03:05:31 GMT, The Walrus <I_Am_The_Walrus@invalid.email.com> wrote:
>
…[10 more quoted lines elided]…
>
If things are to be run in a certain order because of either
dependencies or conflict avoidance, the mainframe style scheduling
still makes sense.  Indeed, it is desirable to have as much on
autopilot as possible.

Clark Morris
```

###### ↳ ↳ ↳ Re: Question regarding Line Sequential files on MF Cobol running under HP-UX (by The Walrus I_Am_The_Walrus@invalid.email.com)

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-17T18:11:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6jhr3h74rjc3hvthhgudfo58stt6u1q12@4ax.com>`
- **References:** `<e3073$47b51b73$6214dce0$2548@ALLTEL.NET> <6d5br3tel9tumhh583nf62cc9ssbbn7bk8@4ax.com> <47b64346$0$4071$9a566e8b@news.aliant.net> <8jicr3htnm6jgovst9iq2m53u84lnqiicn@4ax.com> <47b652fb$0$4053$9a566e8b@news.aliant.net> <j7eer31b49o4t7h22k80tuebj7f3ovpsbi@4ax.com> <lovgr35qs4emanvt0i1r98ca2pipj99lh2@4ax.com>`

```
On Sun, 17 Feb 2008 14:40:47 -0400, Clark F Morris <cfmpublic@ns.sympatico.ca> wrote:

>On Sat, 16 Feb 2008 14:02:52 -0600, Robert <no@e.mail> wrote:
>
…[16 more quoted lines elided]…
>autopilot as possible.

Many Big Unix shops use BMC's Control-M, a job scheduler that runs on both z/OS and Unix.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
