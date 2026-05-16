[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL to CICS

_2 messages · 2 participants · 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: COBOL to CICS

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70p4kn$7fv$1@supernews.com>`
- **References:** `<70o190$agh$1@supernews.com> <70ovsk$fml$1@nnrp1.dejanews.com>`

```
 I do believe that I am using the most recently compiled versions of both
the program and the mapset, and the loadlib is accessible by the CICS.  As
far as DSECT is, I have no clue, this is only my second semester on the
system.

This is the field with problems.

00284 ENTRYF   DFHMDF POS=(17,29),
X
 00285                LENGTH=1,
X
 00286                ATTRB=(NORM,UNPROT,NUM,IC),                          X
 00287                INITIAL='_'
 00288          DFHMDF POS=(17,31),
X
 00289                LENGTH=1,
X
 00290                ATTRB=ASKIP
 00291          DFHMDF POS=(17,34),
X
 00292                LENGTH=22,
X
 00293                ATTRB=(NORM,PROT),
X
 00294                INITIAL='THEN PRESS ENTER.'
terrychen@ibm.net wrote in message <70ovsk$fml$1@nnrp1.dejanews.com>...
>In article <70o190$agh$1@supernews.com>,
>  "Jason" <superj@door.net> wrote:
>> I am working on a program that displays a map through cics.  The map
sends
>> correctly, but when the program is run with it, the field where the user
is
>> to make a selection always comes up with trash in it.  The field also
>> doesn't allow any entry into it (it is coded as unprotected in cics),
been
>> stumped for weeks, need help, no-one else has been able to help.
>> Thanks
>>
>>
>We may need to see the full definition of the field then we just can tell
you
>how to do.
>
>-----------== Posted via Deja News, The Discussion Network ==----------
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: COBOL to CICS

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363182A2.CA118EBC@att.net>`
- **References:** `<70o190$agh$1@supernews.com> <70ovsk$fml$1@nnrp1.dejanews.com> <70p4kn$7fv$1@supernews.com>`

```
DSECT is an Assembler term (Dummy Section, if you're interested) for the
data structure, i.e., what's copied into your program to describe the
mapped data. 

Sorry for any confusion,
Bill Lynch

Jason wrote:
> 
>  I do believe that I am using the most recently compiled versions of both
> the program and the mapset, and the loadlib is accessible by the CICS.  As
> far as DSECT is, I have no clue, this is only my second semester on the
> system.

Every BMS map must be Assembled twice, once to produce the physical map
(this is a load module) and once to produce the data structure (many of
us still call this a DSECT, even though it usually isn't anymore). The
output from the second pass is usually stored as a member in a PDS and
is, usually, copied into your Working Storage.

> This is the field with problems.
> 
…[3 more quoted lines elided]…
>  00287                INITIAL='_'

>  00288          DFHMDF POS=(17,31),     x
>  00289                LENGTH=1,         x
>  00290                ATTRB=ASKIP

Jason, what's the purpose of this field? If it's intended as a "field
stopper" it's redundant, just start the next DFHMDF in (17,31). The
attribute byte of this field will limit the ENTRYF(I) field (all
attribute bytes are hidden and ASKIP). If you want some space between
the "_" and "THEN ..." insert some spaces in the INITIAL parameter just
before "THEN PRESS ENTER".

>  00291          DFHMDF POS=(17,34),       x
>  00292                LENGTH=22,          x
>  00293                ATTRB=(NORM,PROT),  x
>  00294                INITIAL='THEN PRESS ENTER.'

BTW, this is three fields - in which one do you get "trash"?

If you want to discuss mapping in some more detail, feel free to email
me offline.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
