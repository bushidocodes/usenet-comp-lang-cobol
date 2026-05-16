[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Task Manager Software needed

_9 messages · 6 participants · 2000-07_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Task Manager Software needed

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-29T00:00:00
- **Newsgroups:** comp.lang.basic.powerbasic,microsoft.public.basic.dos,comp.lang.cobol
- **Message-ID:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net>`

```

Wrong newsgroup, I know, but:

Does anyone know of some good 'task manager' software?

What I am looking for is something with the functionality of MS-DOS batch
files:

- Start and execute a DOS or Windows program, with option to run
synchronously or asynchronously (i.e., choice of "launch and return
immediately" or "launch and wait for the program to end before resuming").
- Execute a step conditionally based on the return or error code of previous
task
- User-written scripting
- Test for files' existence and/or file size

But I want a few more features...

- Show on the screen the current step being executed (user-friendly)
- Optional or automatic logging of session to disk file
- Allow user to terminate the script while running (after current invoked
task completes/ends)
- Ability to store multiple scripts and select which one to run
- (Optional) mechanism to prompt and accept user values which can then be
used as parameters to next step. Examples: "Run this step Y/N?" or "Enter
Filename to process"

I would prefer the software be Windows-based, but will look at MS-DOS.
Should cost no more than $250-$300 US (single user).

Scheduling (i.e, "run daily at 2:00 AM") is not necessary - I am looking for
something to assist a user to run a series of 'on-demand'  tasks in the
correct order.

If such an animal is not available commercially, I will consider writing it
myself, but I feel no great compelling reason to re-invent the wheel.

I am not interested in being the first user of a new product.

Product/company names, web sites, other news groups, search tips all
appreciated.

Thanks for all replies,
```

#### ↳ Re: OT: Task Manager Software needed

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-07-29T00:00:00
- **Newsgroups:** microsoft.public.basic.dos,comp.lang.cobol,comp.lang.basic.powerbasic
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net>`

```
Find a copy of the IBM REXX interpreter for the operating system
of your choice. There are versions that run on OS/2, Windows, MS-DOS
PC-DOS VSE, MVS and others.

The main IBM page for REXX is

URL http://www-4.ibm.com/software/ad/obj-rexx/ibmrexx.html

There is also another REXX interpreter called Regina that
is available from other sources.

A search at http://www.alltheweb.com on rexx and regina
should provide a number of leads

Lorne

 Sat, 29 Jul 2000 11:56:33, "Michael Mattias" 
<michael.mattias@gte.net> wrote:

> 
> Wrong newsgroup, I know, but:
…[50 more quoted lines elided]…
> 
```

##### ↳ ↳ OT : Batch files

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39832646.42D95466@home.com>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net> <ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver>`

```
Seeing as Michael raised the topic of Task Manager Software, prompted me
to thinking about batch-files. I threw my old MSDOS manuals away ages
ago. For the life of me can't remember the syntax, but I wanted to do
following :-

	mybatchfile parameter

Cannot remember how to check for existence of that parameter and precise
coding within the batch file if parameter supplied/not supplied. This is
batchfile I had, coding is not necessarily correct :-

rem --------------------- CSTONDT.BAT --------------------------------
echo off                                                              
rem                 cstondt.bat    2000 Feb 17                        
rem                                                                   
rem     Conversion of CS facility files to NDT format                 
rem                                                                   
rem This bat file requires CS Client/Facility as parameter :-         
rem             1% = cccccff                                          
rem                                                                   
rem  Copies files across from CS to NDT system, then runs CSNDT.COB   
rem  which reformats CS Items, Probes and Techs into 6 digit (ccyymm) 
rem  dates for NDT system.                                            
rem                                                                   
rem  **** The following would work if I could remember the syntax to  
rem       ensure that 'other' files don't get deleted because of missi
rem       parameter - Can you remember ????                           
rem                                                                   
rem     Make sure a parameter has been entered :-                     
rem                                                                   
REM echo on                                                           
REM if %1==                                                           
REM pause                                                             
REM goto :ERROR                                                       
rem                                                                   
rem     Delete files just to make sure we don't have any junk :-      
rem                                                                   
rem     del \ndt\data\%1*.*                                           
rem                                                                   
rem  copy data files, renaming from 'dat' to 'dta'                    
rem                                                                   
copy \usr\cs\data\%1C.dat   \ndt\data\%1C.dta                         
copy \usr\cs\data\%1R.dat   \ndt\data\%1R.dta                         
copy \usr\cs\data\%1S.dat   \ndt\data\%1S.dta                         
copy \usr\cs\data\%1V.dat   \ndt\data\%1V.dta                         
rem                                                                   
rem copy index files (both use standard RM suffix 'inx')              
rem                                                                   
copy \usr\cs\data\%1C.inx   \ndt\data\%1C.inx                         
copy \usr\cs\data\%1R.inx   \ndt\data\%1R.inx                         
copy \usr\cs\data\%1S.inx   \ndt\data\%1S.inx                         
copy \usr\cs\data\%1V.inx   \ndt\data\%1V.inx                         
rem                                                                   
rem   Now it runs CSTOND.COB and will prompt you again for Cleint/Faci
rem                                                                   
CD \NDT\PROGRAMS                                                      
RUNCOBOL CSTOND.COB                                                   
REM go to EXIT                                                        
rem                                                                   
REM :ERROR                                                            
REM echo Client/Facility parameter not supplied                       
REM EXIT:                                                             
cd c:\                                                                
rem                                                                   
*---------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: OT : Batch files

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E1AA629DEA7F52A0.2FD073ECCAF42936.51D28A3182B31F54@lp.airnews.net>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net> <ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver> <39832646.42D95466@home.com>`

```
On Sat, 29 Jul 2000 18:46:20 GMT, "James J. Gavan" <jjgavan@home.com>
enlightened us:

>Seeing as Michael raised the topic of Task Manager Software, prompted me
>to thinking about batch-files. I threw my old MSDOS manuals away ages
…[62 more quoted lines elided]…
>*---------------------------------------------------------------------

As I remember it, you could use %1 %2 %3 etc. Or I believe you can use
SHIFT which moves all parameters to the left and check %1 again.
There is also a way to check them using errorlevel, but my MS-DOS
manual is archived in my basement somewhere, so I can't check this.

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Why didn't Noah swat those two mosquitoes?






Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: OT : Batch files

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-07-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C96D2977E2C7001A.8C38020C82F3C135.1ECA7DCA74202318@lp.airnews.net>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net> <ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver> <39832646.42D95466@home.com> <E1AA629DEA7F52A0.2FD073ECCAF42936.51D28A3182B31F54@lp.airnews.net>`

```
On Sat, 29 Jul 2000 16:15:30 -0400, SkippyPB
<swiegand@neo.rr.com.nospam> enlightened us:

>On Sat, 29 Jul 2000 18:46:20 GMT, "James J. Gavan" <jjgavan@home.com>
>enlightened us:
…[93 more quoted lines elided]…
> Steve

Hate to reply to myself but wanted to clarify.  SHIFT is not an MS-DOS
command.  It is REXX.  Sorry, I got confused.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Why didn't Noah swat those two mosquitoes?






Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: OT : Batch files

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xr4h5.5588$qd1.1007356@dfiatx1-snr1.gtei.net>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net> <ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver> <39832646.42D95466@home.com> <E1AA629DEA7F52A0.2FD073ECCAF42936.51D28A3182B31F54@lp.airnews.net> <C96D2977E2C7001A.8C38020C82F3C135.1ECA7DCA74202318@lp.airnews.net>`

```
SkippyPB <swiegand@neo.rr.com.nospam> wrote in message >
> Hate to reply to myself but wanted to clarify.  SHIFT is not an MS-DOS
> command.  It is REXX.  Sorry, I got confused.
>

Actually, SHIFT is a valid MS-DOS batch command, but not a command-line
command.

MCM
```

###### ↳ ↳ ↳ Re: OT : Batch files

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19698D1BA25DB108.3F95051B8AE257EE.B13072F41CFAABEC@lp.airnews.net>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net> <ZpzG4UNLyRNq-pn2-PHvIkP6BI6WC@tcpserver> <39832646.42D95466@home.com> <E1AA629DEA7F52A0.2FD073ECCAF42936.51D28A3182B31F54@lp.airnews.net> <C96D2977E2C7001A.8C38020C82F3C135.1ECA7DCA74202318@lp.airnews.net> <xr4h5.5588$qd1.1007356@dfiatx1-snr1.gtei.net>`

```
On Mon, 31 Jul 2000 01:16:13 GMT, "Michael Mattias"
<michael.mattias@gte.net> enlightened us:

>SkippyPB <swiegand@neo.rr.com.nospam> wrote in message >
>> Hate to reply to myself but wanted to clarify.  SHIFT is not an MS-DOS
…[9 more quoted lines elided]…
>

Thanks Michael.  I guess I wasn't as confused as I thought I was!

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

What do chickens think we taste like?






Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

 Steve
```

#### ↳ Re: OT: Task Manager Software needed

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-29T00:00:00
- **Newsgroups:** comp.lang.basic.powerbasic,microsoft.public.basic.dos,comp.lang.cobol
- **Message-ID:** `<3982E1D3.63573B4@zip.com.au>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> What I am looking for is something with the functionality of MS-DOS batch
…[4 more quoted lines elided]…
> immediately" or "launch and wait for the program to end before resuming").

What about the win95 or NT START command  (they are unfortunately
different but)

START /WAIT will wait for completion.

> - Execute a step conditionally based on the return or error code of previous
> task

if ERRORLEVEL

> - User-written scripting

A Batch file

> - Test for files' existence and/or file size

if exists

> But I want a few more features...
> 
…[7 more quoted lines elided]…
> Filename to process"

Ok now I will get a little more realistic:   Look at source.cygnus.com
for the Unix tools.  It includes (along with all the unix commands you
could want) bash. With bash you have a full scripting language.

You can run the script with 'tee' which copies the file and dumps it
to console at the same time.

In KSH (another shell scripting language) you can use 'set -x' to turn
on debugging so that you can dump the commands as they execute.  (Some
unix guru confirm this).

> I would prefer the software be Windows-based, but will look at MS-DOS.
> Should cost no more than $250-$300 US (single user).

The price is right  ZERO.   I have run these for 12 months without any
problems.

> Scheduling (i.e, "run daily at 2:00 AM") is not necessary - I am looking for
> something to assist a user to run a series of 'on-demand'  tasks in the
> correct order.

Look up the 'at' command in NT.  It is there for you to use.  I have
looked this up but not used it in anger yet.   It appears that
Microsoft ripped off enough from SCO unix to make a decent Cron.  I
would assume that WIn2000 would have the same things.


Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

#### ↳ Re: OT: Task Manager Software needed

- **From:** Neil Hosgood <neilhosgood@partslink.co.nz>
- **Date:** 2000-07-31T00:00:00
- **Newsgroups:** comp.lang.basic.powerbasic,microsoft.public.basic.dos,comp.lang.cobol
- **Message-ID:** `<3985186A.3963AF60@partslink.co.nz>`
- **References:** `<RDzg5.27$qd1.37602@dfiatx1-snr1.gtei.net>`

```
you could just use win9x and Obasic, or even winbatch..........
Our DOS based server at work uses a package which allows us
to run tasks simultaneously (9 tasks at the mo). I can't remmber the name
but its pascal based, if it is of interest to you then let me know and I will
find the details.

Michael Mattias wrote:

> Wrong newsgroup, I know, but:
>
…[45 more quoted lines elided]…
> michael.mattias@gte.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
