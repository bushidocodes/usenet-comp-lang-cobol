[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Changing filenames in mid-program-run

_8 messages · 7 participants · 1997-01 → 1997-02_

---

### Changing filenames in mid-program-run

- **From:** "ei..." <ua-author-9703153@usenetarchives.gap>
- **Date:** 1997-01-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5beekc$udt$2@nuacht.iol.ie>`

```

Greetings Y'All.

There follows a silly question !

In the file-section , one sets-up the data-names for each input/output
filenames...( assign xxxxx to yyyyy organization is .... ) ok ?

But , what if one of those files contains the filename of another filename
which wont be known by the program until it actually inputs the first file.

e.g. program server.cbl
has a setup file ( server.ini ) for page-size / frills on-off etc etc
and the actual filename for the output of the 'server.cbl' program.

sever.cbl when run , will read server.ini and find out it needs to open
the output file 'server.res' ( but this filename isnt fixed )
but at that stage it will be into the procedure section and wont be able
to define another assignment.

How can 'you' setup a file-section-assignment to an unknown filename ?

Please , keep flames on low-setting ... I still have the "L-Plates" on.
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "jan paimo" <ua-author-6589465@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

Paul Kearney wrote:
› 
› Greetings Y'All.
…[20 more quoted lines elided]…
› Please , keep flames on low-setting ... I still have the "L-Plates" on.

Hi

define your select statment (look out for differences between cobol dialects)

could work...

SELECT PFREG ASSIGN TO VARYING WS-PFREG
...or this

SELECT PFREG ASSIGN WS-PFREG

where ws-pfreg is what you need....
ORGANIZATION IS INDEXED
ACCESS DYNAMIC
RECORD KEY PFREG-KEY-0
FILE STATUS IS WS1-FSTATUS.

...to define in working storage

03 WS-PFREG PIC X(80) VALUE "PFREG.DAT".

could be a good idea to have a default value assigned

then do your init procedure...

PERFORM READ-INIT-FILE
IF WS-OK = "Y"
MOVE INIT-PFREG TO WS-PFREG

perhaps you should check that what you got is a valid path and such?

Jan
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

Paul Kearney wrote:

› In the file-section , one sets-up the  data-names for each input/output
› filenames...( assign  xxxxx to yyyyy organization is .... )  ok ?
…[13 more quoted lines elided]…
› How can 'you' setup a file-section-assignment to an unknown filename ?

Some flavours of COBOL allow you to specify a variable for yyyyy. In this case, you
simply move the name 'server.res' to the variable before opening the file.


Del.
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "the image trader" <ua-author-3881168@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

Paul Kearney wrote:
› 
› Greetings Y'All.
…[20 more quoted lines elided]…
› Please , keep flames on low-setting ... I still have the "L-Plates" on.

Depends on the hardware platform. On a VAX/VMS machine, there's a VALUE OF ID
clause that can be set at run time, before you open the file. On an AS/400 it's
slightly more complex: once you find out the actual name of the file you wanna
open, call QCMDEXC to post an OVRDBF, and then open the file. Not sure how you'd
accomplish the same thing under MVS or VSE.
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "bl..." <ua-author-17072051@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

ei··.@i··.ie (Paul Kearney) wrote:

› Greetings Y'All.
 
› There follows a silly question !
›  No, but it's fairly straight-forward once you've done it.
 
› In the file-section , one sets-up the  data-names for each input/output
› filenames...( assign  xxxxx to yyyyy organization is .... )  ok ?
 
› But , what if one of those files contains the filename of another filename
› which wont be known by the program until it actually inputs the first file.

select second-file assign to random,
ss-file-name,
organization.......etc etc

01 ss-file-name pic x(20).

read firstfile ..
move firstfile date to ss-file-name
open second-file.

hope this helps.

Glenn Estes bl··.@ep··x.net * My opinions do not reflect those
Accounting Manager * of my boss - unless he happens
B Levy & Son * to be right!
Scranton, PA USA Sol III *
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "rene sondergaard" <ua-author-17073605@usenetarchives.gap>
- **Date:** 1997-01-14T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

Paul Kearney wrote:
› 
 
› e.g.  program  server.cbl
›        has a setup file ( server.ini ) for page-size / frills on-off etc etc
…[5 more quoted lines elided]…
›       to define another assignment.

As others told you, depends on platform. In Micro Focus COBOL you use a
SELECT second-file ASSIGN TO WS-FILE-NAME orga...
..
10 WS-FILE-NAME PIC X(xx).
..
read firstfile
MOVE first-file-data TO WS-FILE-NAME
OPEN second-file

Remember to use the ASSIGN(DYNAMIC) compiler option, otherwise it expects
WS-FILE-NAME to be an environment variable.

On MVS you need an SVC99 subroutine to do the dirty work. Email me and I might be
able to send you the specs for one maybe even the real thing depends on the mood
I'm in.

Rene Sondergaard
IT Support
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1997-01-15T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```

*In article <5beekc$udt$2.··.@nua··l.ie>, ei··.@i··.ie says...
*>
*>Greetings Y'All.
*>
*>There follows a silly question !
*>
*>In the file-section , one sets-up the data-names for each input/outpu
*>t
*>filenames...( assign xxxxx to yyyyy organization is .... ) ok ?
*>
*>But , what if one of those files contains the filename of another file
*>name
*>which wont be known by the program until it actually inputs the first
*>file.
*>
*>e.g. program server.cbl
*> has a setup file ( server.ini ) for page-size / frills on-off e
*>tc etc
*> and the actual filename for the output of the 'server.cbl' prog
*>ram.
*>
*> sever.cbl when run , will read server.ini and find out it needs
*>to open
*> the output file 'server.res' ( but this filename isnt fixed )
*> but at that stage it will be into the procedure section and wont
*> be able
*> to define another assignment.
*>
*>How can 'you' setup a file-section-assignment to an unknown filename ?
*>
*>Please , keep flames on low-setting ... I still have the "L-Plates" on
*>.
*>
*>


If I understand your question, you want to provide the actual name of the
file to open dynamically. The following code fragment (which works with
CA-Realia and I know Micro Focus has the capability) will do what I
believe you are asking:

Select INI-FILE Assign To Varying USER-FILE.

WORKING-STORAGE SECTION.

01 USER-FILE Pic X(50) Value Spaces.


Prior to opening INI-FILE, simply move the file name, including any drive
and path if needed, to USER-FILE. For example:

Move "C:\SETUP.INI" To USER-FILE or, for that matter, a name of a file
retrieved from any other means.


Mike Dodas
```

#### ↳ Re: Changing filenames in mid-program-run

- **From:** "ei..." <ua-author-9703153@usenetarchives.gap>
- **Date:** 1997-02-01T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd0607bcce-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5beekc$udt$2@nuacht.iol.ie>`
- **References:** `<5beekc$udt$2@nuacht.iol.ie>`

```


To those who replied via e-mail and those who also replied via nntp THANK YOU.

I'm sure I'm not the only one to learn more about Cobol from this group.

Bye
Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
