[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to revert when Source PDS changes to Loadlib attributes

_6 messages · 6 participants · 2006-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to revert when Source PDS changes to Loadlib attributes

- **From:** dibalok@gmail.com
- **Date:** 2006-01-02T10:30:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com>`

```
Hi,

While Compiling a program, by mistake i have given my Source Program
PDS name in the Loadlib. As a result the entire PDS has been changed
to the properties of a LoadLib.

How to revert it ?

I tried copying the Source PDS with different Attributes but it has
not helped.

Thanks,
Dib
```

#### ↳ Re: How to revert when Source PDS changes to Loadlib attributes

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-02T18:35:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpbrq6$bit$1@reader2.panix.com>`
- **References:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com>`

```
In article <1136226632.621615.203120@g44g2000cwa.googlegroups.com>,
 <dibalok@gmail.com> wrote:
>Hi,
>
…[4 more quoted lines elided]…
>How to revert it ?

Assuming that you are working in some manner of IBM mainframe environment: 
call Ops and have them restore from the previous day's backup.

DD
```

#### ↳ Re: How to revert when Source PDS changes to Loadlib attributes

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2006-01-02T23:56:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rh7jr1tdketvfv5g8eoiefgce9radleugf@4ax.com>`
- **References:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com>`

```
On 2 Jan 2006 10:30:32 -0800 dibalok@gmail.com wrote:

:>While Compiling a program, by mistake i have given my Source Program
:>PDS name in the Loadlib. As a result the entire PDS has been changed
:>to the properties of a LoadLib.

:>How to revert it ?

:>I tried copying the Source PDS with different Attributes but it has
:>not helped.

The typical solution is to use IEBGENER to create a new member, specifying the
correct DCB attributes.

The member created by the linkage editor is lost, but the others can be read.
```

##### ↳ ↳ Re: How to revert when Source PDS changes to Loadlib attributes

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-01-03T06:40:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o%ouf.219145$qk4.11597@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<rh7jr1tdketvfv5g8eoiefgce9radleugf@4ax.com>`
- **References:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com> <rh7jr1tdketvfv5g8eoiefgce9radleugf@4ax.com>`

```


Binyamin Dissen wrote:

> On 2 Jan 2006 10:30:32 -0800 dibalok@gmail.com wrote:
> 
…[12 more quoted lines elided]…
> The member created by the linkage editor is lost, but the others can be read.

Now that's a useful tip!  All I need to do is make sure I know the 
correct BLKSIZE on the DCB (what it was before):

//STEP010 EXEC PGM=IEBGENER
//SYSOUT   DD SYSOUT=*
//SYSPRINT DD SYSOUT=*
//SYSUT1   DD DUMMY,DCB=LRECL=80
//SYSUT2   DD DSN=MY.SCREWED.UP.SOURCE.PDS(NULLMBR),DISP=SHR,
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=24000)
//SYSIN    DD DUMMY

I don't use IEBGENER much, so this sample JCL may be chock full of errors.
```

###### ↳ ↳ ↳ Re: How to revert when Source PDS changes to Loadlib attributes

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-01-03T11:59:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136318357.204867.320330@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<o%ouf.219145$qk4.11597@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com> <rh7jr1tdketvfv5g8eoiefgce9radleugf@4ax.com> <o%ouf.219145$qk4.11597@bgtnsc05-news.ops.worldnet.att.net>`

```
I suppose there are several ways to work out the original blocksize

a) look at the JCL that originally created the PDS
b) restore the previous day's/week's version from backup and look at
that
c) guess that it might the the same as it currently is.
d) guess that it might be 4 or 8 bytes less than it currently is,
loadlibs used to have recfm=U, so there may be a block descriptor and
perhaps a record descriptor fullword added.
e) guess according to commonly used blocksizes by yourself or your
installation.
```

###### ↳ ↳ ↳ Re: How to revert when Source PDS changes to Loadlib attributes

- **From:** "Joel C. Ewing" <jcREMOVEewing@CAPSacm.org>
- **Date:** 2006-01-04T04:08:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pTHuf.4440$M%4.3254@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<o%ouf.219145$qk4.11597@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<1136226632.621615.203120@g44g2000cwa.googlegroups.com> <rh7jr1tdketvfv5g8eoiefgce9radleugf@4ax.com> <o%ouf.219145$qk4.11597@bgtnsc05-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> 
…[22 more quoted lines elided]…
> correct BLKSIZE on the DCB (what it was before):

Sequential processing is tolerant of short blocks, so you don't 
necessarily have to restore the exact old BLKSIZE value.  You should be 
able to recover the data as long as you set the the BLKSIZE to a legal 
value (based on the RECFM and LRECL) that is >= the original BLKSIZE. 
On the other hand, if you set BLKSIZE to a value that is less than the 
original BLKSIZE, you will get a Wrong-Length record I/O error if you 
attempt to read a member that contains a longer block.
> 
> //STEP010 EXEC PGM=IEBGENER
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
