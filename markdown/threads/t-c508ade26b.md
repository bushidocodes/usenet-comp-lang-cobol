[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ascii from COBOL

_8 messages · 7 participants · 1997-10 → 1997-11_

---

### Ascii from COBOL

- **From:** "jlm..." <ua-author-17072448@usenetarchives.gap>
- **Date:** 1997-10-29T15:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<878155256.22431@dejanews.com>`

```

I missed the chance to reply to the question on ASCII from COBOL. The way
to do it in IBM is to use the JCL. There is no change to the COBOL.
Simply add OPTCD=Q to the DCB parameters.

John

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Ascii from COBOL

- **From:** "richard frankel" <ua-author-6589082@usenetarchives.gap>
- **Date:** 1997-10-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<878155256.22431@dejanews.com>`
- **References:** `<878155256.22431@dejanews.com>`

```

jlm··.@san··a.gov wrote:
› 
› I missed the chance to reply to the question on ASCII from COBOL. The way
…[6 more quoted lines elided]…
›       http://www.dejanews.com/     Search, Read, Post to Usenet
Thanks, but this only works when reading in or writing out to/from
*mass-storage* devices (e.g. tape). I'm writing to DASD.
```

##### ↳ ↳ Re: Ascii from COBOL

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-10-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c508ade26b-p2@usenetarchives.gap>`
- **References:** `<878155256.22431@dejanews.com> <gap-c508ade26b-p2@usenetarchives.gap>`

```

Richard FRANKEL wrote:
› 
› jlm··.@san··a.gov wrote:
…[10 more quoted lines elided]…
› *mass-storage* devices (e.g. tape). I'm writing to DASD.


How badly and how fast to you need it? It is conceivable that if your
output is a flat-file that your program's jobstep writes it to tape and
then you code a GENER to dump it to DASD. Cheap, dirty and ugly... but
it'll work.

DD
```

###### ↳ ↳ ↳ Re: Ascii from COBOL

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-11-03T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c508ade26b-p3@usenetarchives.gap>`
- **References:** `<878155256.22431@dejanews.com> <gap-c508ade26b-p2@usenetarchives.gap> <gap-c508ade26b-p3@usenetarchives.gap>`

```

On Thu, 30 Oct 1997 19:41:58 -0500, The Goobers
wrote:

› Richard FRANKEL wrote:
›› 
…[19 more quoted lines elided]…
› DD

Watch out for mixed in COMP or COMP-3 data though, clear text or text
numbers only. This means signs leading or trailing on the output
file.

(yes I can state the obvious)
```

###### ↳ ↳ ↳ Re: Ascii from COBOL

_(reply depth: 4)_

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c508ade26b-p4@usenetarchives.gap>`
- **References:** `<878155256.22431@dejanews.com> <gap-c508ade26b-p2@usenetarchives.gap> <gap-c508ade26b-p3@usenetarchives.gap> <gap-c508ade26b-p4@usenetarchives.gap>`

```

Ken Foskey wrote:
› 
› On Thu, 30 Oct 1997 19:41:58 -0500, The Goobers 
…[29 more quoted lines elided]…
› (yes I can state the obvious)

If you really need to do it from within your COBOL program, check out the
INSPECT statement with the CONVERTING option. You could define a 256-byte
elementary item with the ASCII equivalents of the EBCDIC translate table values,
which would also be defined as a 256-byte elementary item in the range '00'x
thru 'FF'x. Then you could INSPECT/CONVERTING the entire record or just the
elementary items you want to convert.
Of course, this may turn out to be a performance pig (never tried it) but if the
compiler just generates an assembler translate(/long?) instruction (or
whattevertheheckyoucallit) it might not be too bad.
Again, it depends on how bad (and fast) you need it :-)

***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

###### ↳ ↳ ↳ Re: Ascii from COBOL

_(reply depth: 5)_

- **From:** "richard frankel" <ua-author-6589082@usenetarchives.gap>
- **Date:** 1997-11-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c508ade26b-p5@usenetarchives.gap>`
- **References:** `<878155256.22431@dejanews.com> <gap-c508ade26b-p2@usenetarchives.gap> <gap-c508ade26b-p3@usenetarchives.gap> <gap-c508ade26b-p4@usenetarchives.gap> <gap-c508ade26b-p5@usenetarchives.gap>`

```

Jim Van Sickle wrote:

› If you really need to do it from within your COBOL program, check out the INSPECT statement with the CONVERTING option. You could define a 256-byte elementary item with the ASCII equivalents of the EBCDIC translate table values,
› which would also be defined as a 256-byte elementary item in the range '00'x thru 'FF'x. Then you could INSPECT/CONVERTING the entire record or just the elementary items you want to convert.
…[11 more quoted lines elided]…
› ***********************************************
Jim,

this thread has come around full-circle, because what you propose is
pretty much exactly what we have implemented - a subrountine which does
a Format-4 INSPECT, converting a chars in the EBCDIC alphabet to ASCII
values, and vice-versa. Performance really isn't a problem, (converts
around 1000 bytes in a few microseconds) - I was just concerned (and the
reason for my original posting was) that we may have "cracked a nut with
a sledgehammer", but seeing the responses to this thread it seems that I
have in fact implemented probably the most simple and effective
solution, all other solutions requiring tape-based operations.
Thank you everyone for your comments, please lets consider this
thread-dead !
Richard FRANKEL
```

###### ↳ ↳ ↳ Re: Ascii from COBOL

_(reply depth: 6)_

- **From:** "mark miller" <ua-author-584162@usenetarchives.gap>
- **Date:** 1997-11-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c508ade26b-p6@usenetarchives.gap>`
- **References:** `<878155256.22431@dejanews.com> <gap-c508ade26b-p2@usenetarchives.gap> <gap-c508ade26b-p3@usenetarchives.gap> <gap-c508ade26b-p4@usenetarchives.gap> <gap-c508ade26b-p5@usenetarchives.gap> <gap-c508ade26b-p6@usenetarchives.gap>`

```

Are you running OS390? Do you have FTP(file transfer protocol)? We
routinely transfer files from our IBM mainframe to Tandem unix machines
using FTP which is bundled with OS390. EBCDIC to ASCII conversion is
automatic. It may be something to bear in mind for future applications
development if all the CD processing is done an a ASCII server.
I can provide some sample JCL if you are interested.


Richard FRANKEL wrote:
› 
› Jim Van Sickle wrote:
…[28 more quoted lines elided]…
› Richard FRANKEL
```

#### ↳ Re: Ascii from COBOL

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c508ade26b-p8@usenetarchives.gap>`
- **In-Reply-To:** `<878155256.22431@dejanews.com>`
- **References:** `<878155256.22431@dejanews.com>`

```

Here's a small assembler program I use to perform this conversion.
It uses the MVS XLATE macro which calls a system SVC to do
the conversion. If you change "TO=A" to "TO=E" and flip the
DCB's you can go ascii to ebcdic. There's no special JCL optcd
parameters or anything. It works great.

TITLE 'CONVERT FROM EBCDIC TO ASCII'
EB2AS CSECT
*
USING *,3
STM 14,12,12(13)
LR 3,15
ST 13,SAVEAREA+4
LA 12,SAVEAREA
ST 12,8(0,13)
LR 13,12
OPEN (EFILE,(INPUT),AFILE,(OUTPUT))
LH 4,EFILE+82 GET LENGTH OF INPUT RECORD
READ EQU *
GET EFILE,WORKAREA
XLATE WORKAREA,(4),TO=A
PUT AFILE,WORKAREA
B READ
ENDEFILE CLOSE (EFILE,,AFILE)
GOBACK L 13,SAVEAREA+4
LM 14,12,12(13)
LA 15,0
BR 14
*
SAVEAREA DC 18F'0'
*
AFILE DCB DDNAME=AFILE,MACRF=PM,DSORG=PS
*
EFILE DCB DDNAME=EFILE,MACRF=GM,DSORG=PS,EODAD=ENDEFILE
*
WORKAREA DS CL32760
*
END EB2AS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
