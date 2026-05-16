[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using COMREG to get date

_11 messages · 3 participants · 1999-08_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Using COMREG to get date

- **From:** "Tim Mueller" <tmiller16@yahoo.com>
- **Date:** 1999-08-06T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol,alt.cobol
- **Message-ID:** `<37aad36d@news2.one.net>`

```
I'm experimenting with the code that Bob Botsis posted on using COMREG to
get the system date and other info, but so far, I'm getting garbage.
Following is the code I'm using to just retrieve and display the info.  Can
anyone tell me what I'm doing wrong?


000210 WORKING-STORAGE SECTION.
000220
000230 01  PAGE-ZERO.
000240     03                           PIC X(20).
000250     03  POINT-COMREG             USAGE POINTER.
000260
000270 01  WS-CURRENT-DATE              PIC X(11).
000280 01  WS-VSE-JOB-NAME              PIC X(8).
000290 01  WS-CURRENT-SYSTEM-DATE       PIC X(8).
000300 01  WS-CURRENT-SYSTEM-DATE-CC    PIC XX.
000310 01  WS-PARTITION-ID              PIC XX.
000320 01  WS-PROGRAM-NAME              PIC X(8).
000330
000340 LINKAGE SECTION.
000350
000360 01  COMREG.
000370     03  CURRENT-DATE.
000380         05  CURRENT-DATE-MM PIC XX.
000390         05  CURRENT-DATE-S1 PIC X.
000400         05  CURRENT-DATE-DD PIC XX.
000410         05  CURRENT-DATE-S2 PIC X.
000420         05  CURRENT-DATE-YY PIC XX.
000430         05  CURRENT-DATE-S3 PIC X.
000440         05  CURRENT-DATE-CC PIC XX.
000450     03                      PIC X(13).
000460     03  VSE-JOB-NAME        PIC X(8).
000470     03                      PIC X(47).
000480     03  CURRENT-SYSTEM-DATE.
000490         05  CURRENT-SYSTEM-DATE-MM PIC XX.
000500         05  CURRENT-SYSTEM-DATE-DD PIC XX.
000510         05  CURRENT-SYSTEM-DATE-YY PIC XX.
000520         05  CURRENT-SYSTEM-DATE-DDD PIC XXX.
000530     03                      PIC X(12).
000540     03  CURRENT-SYSTEM-DATE-CC PIC XX.
000550           03                      PIC X(110).
000560           03  PARTITION-ID        PIC XX.
000570           03                      PIC XX.
000580           03  PROGRAM-NAME        PIC X(8).
000590
000600 PROCEDURE DIVISION.
000610 MAINLINE.
000620          SET ADDRESS OF COMREG TO POINT-COMREG.
000630          MOVE  CURRENT-DATE TO WS-CURRENT-DATE
000640          MOVE  VSE-JOB-NAME TO WS-VSE-JOB-NAME
000650          MOVE  CURRENT-SYSTEM-DATE TO WS-CURRENT-SYSTEM-DATE
000660          MOVE CURRENT-SYSTEM-DATE-CC TO WS-CURRENT-SYSTEM-DATE-CC
000670          MOVE  PARTITION-ID TO WS-PARTITION-ID
000680          MOVE  PROGRAM-NAME TO WS-PROGRAM-NAME
000690
000700          DISPLAY WS-CURRENT-DATE
000710          DISPLAY WS-VSE-JOB-NAME
000720          DISPLAY WS-CURRENT-SYSTEM-DATE
000730          DISPLAY WS-CURRENT-SYSTEM-DATE-CC
000740          DISPLAY WS-PARTITION-ID
000750          DISPLAY WS-PROGRAM-NAME
000760        STOP RUN
```

#### ↳ Re: Using COMREG to get date

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-08-06T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol,alt.cobol
- **Message-ID:** `<37aae07c$1$tfs$mr2ice@news>`
- **References:** `<37aad36d@news2.one.net>`

```
In <37aad36d@news2.one.net>, on 06 Aug 1999 at 08:26, "Tim Mueller"
<tmiller16@yahoo.com> said:

>I'm experimenting with the code that Bob Botsis posted on using COMREG to
>get the system date and other info, but so far, I'm getting garbage.
>Following is the code I'm using to just retrieve and display the info. 
>Can anyone tell me what I'm doing wrong?

I have no VSE system to run a test, but I would try to move these lines
from the Working-Storage to the Linkage Section:

 000230 01  PAGE-ZERO.
 000240     03                           PIC X(20).
 000250     03  POINT-COMREG             USAGE POINTER.

and perhaps add

         SET Address of Page-Zero to NULL

to the top of the Proc Div.

Gilbert Saint-flour
```

##### ↳ ↳ Re: Using COMREG to get date

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.1216b585b777f2598969d@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news>`

```
In article <37aae07c$1$tfs$mr2ice@news>, gsf@ibm.net says...
> In <37aad36d@news2.one.net>, on 06 Aug 1999 at 08:26, "Tim Mueller"
> <tmiller16@yahoo.com> said:
…[22 more quoted lines elided]…
> 
I am interested in retrieving the comreg area in a Cobol II ver 4 program 
in an OS/390 environment. I think that I can follow the examples 
discussed in this thread. However, what I would be interested in is a 
copybook of the COMREG area. I know assembler well enough to be able to 
decipher the AMACLIB member for the COMREG area if someone could direct 
me to it.

Please either post the replies to the comp.lang.cobol newsgroup or email 
me directly
```

##### ↳ ↳ Re: Using COMREG to get date

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.1216b74e5442f53598969e@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news>`

```
In article <37aae07c$1$tfs$mr2ice@news>, gsf@ibm.net says...
> In <37aad36d@news2.one.net>, on 06 Aug 1999 at 08:26, "Tim Mueller"
> <tmiller16@yahoo.com> said:
…[22 more quoted lines elided]…
> 
I am interested in retrieving the comreg area in a Cobol II ver 4 program 
in an OS/390 environment. I think that I can follow the examples 
discussed in this thread. However, what I would be interested in is a 
copybook of the COMREG area. I know assembler well enough to be able to 
decipher the AMACLIB member for the COMREG area if someone could direct 
me to it.

Please either post the replies to the comp.lang.cobol newsgroup or email 
me directly
```

##### ↳ ↳ Re: Using COMREG to get date

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.1216b9f6cf827f859896a2@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news>`

```
In article <37aae07c$1$tfs$mr2ice@news>, gsf@ibm.net says...
> In <37aad36d@news2.one.net>, on 06 Aug 1999 at 08:26, "Tim Mueller"
> <tmiller16@yahoo.com> said:
…[22 more quoted lines elided]…
> 
I am interested in retrieving the comreg area in a Cobol II ver 4 program 
in an OS/390 environment. I think that I can follow the examples 
discussed in this thread. However, what I would be interested in is a 
copybook of the COMREG area. I know assembler well enough to be able to 
decipher the AMACLIB member for the COMREG area if someone could direct 
me to it.

Please either post the replies to the comp.lang.cobol newsgroup or email 
me directly
```

##### ↳ ↳ Re: Using COMREG to get date

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.1216bb001f7ee6a79896a3@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news>`

```
In article <37aae07c$1$tfs$mr2ice@news>, gsf@ibm.net says...
> In <37aad36d@news2.one.net>, on 06 Aug 1999 at 08:26, "Tim Mueller"
> <tmiller16@yahoo.com> said:
…[22 more quoted lines elided]…
> 
I am interested in retrieving the comreg area in a Cobol II ver 4 program 
in an OS/390 environment. I think that I can follow the examples 
discussed in this thread. However, what I would be interested in is a 
copybook of the COMREG area. I know assembler well enough to be able to 
decipher the AMACLIB member for the COMREG area if someone could direct 
me to it.

Please either post the replies to the comp.lang.cobol newsgroup or email 
me directly
```

###### ↳ ↳ ↳ Re: Using COMREG to get date

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-08-08T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<37ad927d$2$tfs$mr2ice@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news> <MPG.1216bb001f7ee6a79896a3@news>`

```
In <MPG.1216bb001f7ee6a79896a3@news>, on 08 Aug 1999 at 03:52,
clastname@nospam.com (Charles Haatvedt Jr.) said:

>I am interested in retrieving the comreg area in a Cobol II ver 4 program
> in an OS/390 environment. I think that I can follow the examples 
…[3 more quoted lines elided]…
>me to it.

There is no Communication Region (COMREG) in MVS.  What kind of
information are you trying to retrieve?  Date? JOB name? UPSI? 

Gilbert Saint-flour <gsf@ibm.net>
```

###### ↳ ↳ ↳ Re: Using COMREG to get date

_(reply depth: 4)_

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.1217f9527a83ef3a9896bb@news.rdc1.wa.home.com>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news> <MPG.1216bb001f7ee6a79896a3@news> <37ad927d$2$tfs$mr2ice@news>`

```
[This followup was posted to bit.listserv.vse-l and a copy was sent to 
the cited author.]

In article <37ad927d$2$tfs$mr2ice@news>, gsf@ibm.net says...
> In <MPG.1216bb001f7ee6a79896a3@news>, on 08 Aug 1999 at 03:52,
> clastname@nospam.com (Charles Haatvedt Jr.) said:
…[14 more quoted lines elided]…
> 

	At my prior employer they had an assembler routine which would move 
information from "comreg" to a 224 byte variable passed to the routine. 
It used to get to the comreg area by loading a register from absolute 
address decimal 20. Then this register was used as the "from" location in 
an MVC to move 224 bytes to the variable passed to the routine. 

This module could be called from either Cobol 74 or Cobol II. At the time 
it was an MVS environment...

My current environment is actually OS/390   

===>>>  what I am specifically looking for is the layout for that 224 
byte area.  I am planning on using the jobname, jobstep, procstep, lpar, 
system date, system time fields. I would like to put the layout into a 
copybook member. Our shop still uses Panvalet, so I would use a ++INCLUDE 
member. We are moving to Endevor, but it is a slow process.
```

###### ↳ ↳ ↳ Re: Using COMREG to get date

_(reply depth: 5)_

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<37aed4a0$2$tfs$mr2ice@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news> <MPG.1216bb001f7ee6a79896a3@news> <37ad927d$2$tfs$mr2ice@news> <MPG.1217f9527a83ef3a9896bb@news.rdc1.wa.home.com>`

```
In <MPG.1217f9527a83ef3a9896bb@news.rdc1.wa.home.com>, on 09 Aug 1999 at
02:30, clastname@nospam.com (Charles Haatvedt Jr.) said:

> At my prior employer they had an assembler routine which would move 
>information from "comreg" to a 224 byte variable passed to the routine. 
>..... This module could be called from either Cobol 74 or Cobol II. 
>At the time it was an MVS environment...

Again, there is no such thing as a "communication region" in MVS or
OS/390.  Your prior employer may have converted from VSE some time before
and used a comreg simulation routine in MVS, but this would have been
managed at the application level, not by the operating system itself.  

What makes you think your _current_ employer has comreg simulation
routines on their OS/390 system?

Gilbert Saint-flour <gsf@ibm.net>
```

###### ↳ ↳ ↳ Re: Using COMREG to get date

_(reply depth: 5)_

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** bit.listserv.vse-l,comp.lang.cobol
- **Message-ID:** `<MPG.12180a994df5f6a29896bc@news.rdc1.wa.home.com>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news> <MPG.1216bb001f7ee6a79896a3@news> <37ad927d$2$tfs$mr2ice@news> <MPG.1217f9527a83ef3a9896bb@news.rdc1.wa.home.com>`

```
> 
what I am looking for is a mechanism to retrieve certain "environment" 
information in an OS/390 COBOLII ver4 program. The information that I am 
looking for is Jobname, Stepname, Procstepname, Logical Partition ID 
(LPAR ?), 
system date and time etc...

I had seen a post earlier about retrieving this information from 
"comreg". It mentioned that the address pointing to comreg is at location 
decimal 20 bytes from memory location zero. The "comreg" area pointed to 
is a 224 byte area containing jobname, stepname, partition, date, time 
etc....
```

###### ↳ ↳ ↳ Re: Using COMREG to get date

_(reply depth: 6)_

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37af108a$4$tfs$mr2ice@news>`
- **References:** `<37aad36d@news2.one.net> <37aae07c$1$tfs$mr2ice@news> <MPG.1216bb001f7ee6a79896a3@news> <37ad927d$2$tfs$mr2ice@news> <MPG.1217f9527a83ef3a9896bb@news.rdc1.wa.home.com> <MPG.12180a994df5f6a29896bc@news.rdc1.wa.home.com>`

```
In <MPG.12180a994df5f6a29896bc@news.rdc1.wa.home.com>, on 09 Aug 1999 at
03:44, clastname@nospam.com (Charles Haatvedt Jr.) said:

>what I am looking for is a mechanism to retrieve certain "environment" 
>information in an OS/390 COBOLII ver4 program. The information that I am 
>looking for is Jobname, Stepname, Procstepname, Logical Partition ID 
>(LPAR ?), system date and time etc...

Look here: http://x42.deja.com/=dnc/[ST_rn=ps]/getdoc.xp?AN=364997163

Gilbert Saint-flour <gsf@ibm.net>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
