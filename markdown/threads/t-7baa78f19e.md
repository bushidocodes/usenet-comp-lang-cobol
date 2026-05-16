[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] JCL DD name for CEE msgs?

_10 messages · 5 participants · 2003-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] JCL DD name for CEE msgs?

- **From:** docdwarf@panix.com
- **Date:** 2003-12-30T10:56:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bss76m$gjc$1@panix1.panix.com>`

```

All righty... environment's IBM mainframe and I'm looking for a DD 
statement to redirect various Language Environment messages.  The 
jobstream contains a //SYSOUT DD SYSOUT=A for the program's counters 
(DISPLAYed) but now we're getting CEE9999I informational messages and 
other... stuff interspersed with them; what used to be a SYSOUT of:

BEGIN PROGNAME

TIME/DATE COMPILED = (stuff)
CURRENT DATE       = (date)

TOTAL INPUT RECS   =  12,345
TOTAL REJECT RECS  =     345
TOTAL GOOD RECS    =  12,000

... is now something like:

CEE3608I The following messages pertain to the invocation command (trunc)
(other messages)

BEGIN PROGNAME

TIME/DATE COMPILED = (stuff)
CURRENT DATE       = (date)

TOTAL INPUT RECS   =  12,345
TOTAL REJECT RECS  =     345
TOTAL GOOD RECS    =  12,000

Storage Report for Enclave PROGNAME 12/30/03 10:30:49 AM
Language Environment V02 R10.00

    STACK statistics:
      Initial size:                                       524288
      Increment size:                                     524288
      Maximum used by all concurrent threads:               5040
(other messages)

... and this, of course, changes the appearance of the DISPLAY reports 
that people have been used to seeing since 1900.

I've tried:

//CEEMSG   DD SYSOUT=A
//CEEMSGS  DD SYSOUT=A
//CEEOUT   DD SYSOUT=A

... all to no effect; might someone be able to tell me where I can look to 
find the DDname that will segregate the Language Enironment messages from 
the program's SYSOUT?

Thanks much.

DD
```

#### ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-30T16:46:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_ZhIb.26245$Pg1.4923@newsread1.news.pas.earthlink.net>`
- **References:** `<bss76m$gjc$1@panix1.panix.com>`

```
See the MSGFILE run-time option described at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3130/2.3.32
```

##### ↳ ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** docdwarf@panix.com
- **Date:** 2003-12-30T12:05:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bssb9e$9gn$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com> <_ZhIb.26245$Pg1.4923@newsread1.news.pas.earthlink.net>`

```
In article <_ZhIb.26245$Pg1.4923@newsread1.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>See the MSGFILE run-time option described at:
>
> http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3130/2.3.32

Magnificent, Mr Klein... a simple //MSGFILE DD SYSOUT=A sends all of 
that... stuff to the bitbucket.

Thanks much!

DD

><docdwarf@panix.com> wrote in message news:bss76m$gjc$1@panix1.panix.com...
>>
…[56 more quoted lines elided]…
>
```

##### ↳ ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** docdwarf@panix.com
- **Date:** 2003-12-30T13:19:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bssfjr$bv3$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com> <_ZhIb.26245$Pg1.4923@newsread1.news.pas.earthlink.net>`

```
In article <_ZhIb.26245$Pg1.4923@newsread1.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>See the MSGFILE run-time option described at:
>
> http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3130/2.3.32

I hope I cancelled my first reply to this... the 'solution' I thought I 
had come to was the result of my looking in the wrong part of the JESLOG.

What *really* happened was... I was passing a PARM to the program to use 
as part of printing the report-header, in this jobstream the PARM was 
'SYS1EDIT/REFORMAT INQUIRY REPORT', where SYS1 was the system to be used 
and EDIT/REFORMAT INQUIRY REPORT was supposed to appear in the report's 
headings.

The Language Environment uses the '/' as a delimiter between program
parameters and LE run-time options (as per
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA2130/1.9.2.6?DT=20020626105928#HDRRTOHCOB>
, which also seems to be the reverse of the sequence specified in
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA2130/1.5.1.3?DT=20020626105928#HDRMVSEXEC>, 
so LE tried to interpret my header-line as run-time opts and turned REPORT 
on.

The solution?  Change the header-line from EDIT/REFORMAT to EDIT-REFORMAT.

DD

><docdwarf@panix.com> wrote in message news:bss76m$gjc$1@panix1.panix.com...
>>
…[56 more quoted lines elided]…
>
```

#### ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** Habitant <berlutte@sympatico.ca>
- **Date:** 2003-12-30T12:37:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ned3vv8puh8bp78qjqtk4eh7bh55enqlnd@4ax.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com>`

```
On 30 Dec 2003 10:56:06 -0500, docdwarf@panix.com wrote:

>
>All righty... environment's IBM mainframe and I'm looking for a DD 
>statement to redirect various Language Environment messages.

'Twas ever thus, nay?

Oprah G'Matick
```

#### ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-12-30T12:02:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0312301202.503d6c10@posting.google.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<bss76m$gjc$1@panix1.panix.com>...
> All righty... environment's IBM mainframe and I'm looking for a DD 
> statement to redirect various Language Environment messages.  The 
…[3 more quoted lines elided]…
> 
Message snipped

Look up the OUTDD compiler option in the language guide.  I haven't
used it myself, but it takes the form OUTDD(user-specified-ddname). 
Within a program it would go on a CBL or PROCESS statement in the
source code, or in a PARM statement in the EXEC statement in the JCL. 
The guide is more comprehensive as to options and caveats such as
installation defined defaults which you might trip over if unlucky.

Robert
```

##### ↳ ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** docdwarf@panix.com
- **Date:** 2003-12-30T20:58:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bstagt$1je$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com> <fcd09c56.0312301202.503d6c10@posting.google.com>`

```
In article <fcd09c56.0312301202.503d6c10@posting.google.com>,
Robert Jones <robert@jones0086.freeserve.co.uk> wrote:
>docdwarf@panix.com wrote in message news:<bss76m$gjc$1@panix1.panix.com>...
>> All righty... environment's IBM mainframe and I'm looking for a DD 
…[5 more quoted lines elided]…
>Message snipped

And likewise snipped... thanks much for your time

DD
```

#### ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2003-12-30T14:26:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9YmIb.430$b77.569@dfw-service2.ext.raytheon.com>`
- **In-Reply-To:** `<bss76m$gjc$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> All righty... environment's IBM mainframe and I'm looking for a DD 
> statement to redirect various Language Environment messages.  The 
…[52 more quoted lines elided]…
> 

In addition to what you learned about the PARM input you specified, you 
should be aware that LE's Message File is normally empty.  If you hadn't 
stirred up a hornet's nest by sending invalid options to LE, your 
program's output would not have looked any different from any other run.

Also, it is the LAST " / " in the PARM field that tells LE that options 
that it should process follow.  So you could put "EDIT/REFORMAT..." into 
the PARM field, as long as you end the PARM field with another slash.

With regard to separating the LE and COBOL program output, I have the 
following opinions:
1.  I actually feel that COBOL programmers are lucky that DISPLAY 
outputs to the same file as LE (by default), compared to users of other 
LE languages.  For one thing, no JCL changes are required to see all the 
job output.  One of the things that is different about LE compared to 
older COBOL run times is that IBM advises us to start debugging by 
looking for messages, rather than abend codes.  It's easy to look for 
DDname SYSOUT - we already output some useful information there in many 
cases.

2.  I prefer Bill Klein's suggestion to change the LE MSGFILE setting to 
Thane Hubbell's suggestion to change where COBOL's output goes.  Most 
likely, your COBOL program predates LE, so it was there first.  That 
means your JCL is written to support use of SYSOUT for the COBOL 
program's output, so if you changed COBOL's output DDname, you'd have to 
make JCL changes, or the output might end up going someplace where the 
user wouldn't see it.  If you change LE's MSGFILE setting to keep it 
away from SYSOUT, it's up to you what you do with those messages - there 
would probably be no user impact.  Finally, you have to recompile to use 
COBOL's OUTDD option, but only change the execution time JCL (or perhaps 
relink with a modified CEEUOPT) to use MSGFILE.  Usually, this would be 
an easier change to get implemented in the Change Control processes.
```

#### ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2003-12-30T14:51:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AjnIb.432$b77.655@dfw-service2.ext.raytheon.com>`
- **In-Reply-To:** `<bss76m$gjc$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> All righty... environment's IBM mainframe and I'm looking for a DD 
> statement to redirect various Language Environment messages.  The 
…[52 more quoted lines elided]…
> 

A couple of points that might prove useful to you:

1.  You can have the slash where you have it, as long as you end your 
PARM field with another slash.  LE interprets the LAST slash as the one 
meant to delimit LE options from the COBOL program's options.  It's OK 
to have the slash followed by no LE options.

2.  To separate COBOL's messages from LE's messages, you have two 
replies that will do the job.  SORT utilities also use DDname SYSOUT for 
their output by default.  Personally, I'm glad that the messages all end 
up together, but you do have options if you don't agree.

I like Bill's suggestion to use MSGFILE to change LE's output DDname 
better than Robert Jones' suggestion to use OUTDD.  OUTDD requires a 
program recompile.  OUTDD would also likely require a JCL change. 
Finally, OUTDD would require some way of remembering that this one 
program out of perhaps thousands, should ALWAYS be compiled with OUTDD 
set to "SYSUGLY" or whatever.  I'd rather just change the JCL PARM field 
(or perhaps link in a CEEUOPT module), and add a DD statement.
```

##### ↳ ↳ Re: [OT] JCL DD name for CEE msgs?

- **From:** docdwarf@panix.com
- **Date:** 2003-12-30T21:01:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bstama$3s4$1@panix1.panix.com>`
- **References:** `<bss76m$gjc$1@panix1.panix.com> <AjnIb.432$b77.655@dfw-service2.ext.raytheon.com>`

```
In article <AjnIb.432$b77.655@dfw-service2.ext.raytheon.com>,
Colin Campbell  <cmcampb@adelphia.net_remove_this> wrote:
>docdwarf@panix.com wrote:
>
>> All righty... environment's IBM mainframe and I'm looking for a DD 
>> statement to redirect various Language Environment messages. 

[snip]

>A couple of points that might prove useful to you:
>
>1.  You can have the slash where you have it, as long as you end your 
>PARM field with another slash.

That'll be something to try on the next run... as mentioned I changed the 
literal from EDIT/REFORMAT to EDIT-REFORMAT and I don't think the users 
will object too strongly to the alternative punctuation.  On t'other 
hand... Give 'Em What They're Used To is, frequently, a crowd-pleaser.

Thanks much for your time!

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
