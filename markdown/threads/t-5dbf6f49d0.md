[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read from a empty VSAM file

_29 messages · 18 participants · 2000-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Read from a empty VSAM file

- **From:** "Pepper" <guest@mec.es>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<866ult$gtf$1@bronx.mec.es>`

```
I need help.

How i can read a empty VSAM file without a 3000 return code? If the VSAM
file is empty i can write it but i can't read it.

I have to initialize it or i need a special clause?

Thank you.
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OLCq0z0Y$GA.271@cpmsnbbsa02>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
It has been customary to add a record to a VSAM file to prevent errors.
This is usually a record with a low-values key.

This means that you have to program around this, when the file is accessed
sequentially.

If you can avoid keeping this record on file, do it.

Pepper <guest@mec.es> wrote in message news:866ult$gtf$1@bronx.mec.es...
> I need help.
>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ SV: Read from a empty VSAM file

- **From:** "Bjorn Alvik" <bjorn.alvik@asp.no>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9tEh4.8609$in5.141189@news1.online.no>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02>`

```
Have you tried an initial OPEN OUTPUT / CLOSE
Wit that method, you should have no need for any "initialisation" record
Bjorn
DennisHarley <LegacyBlue@email.msn.com> skrev i
meldingsnyheter:OLCq0z0Y$GA.271@cpmsnbbsa02...
> It has been customary to add a record to a VSAM file to prevent errors.
> This is usually a record with a low-values key.
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Read from a empty VSAM file

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02>`

```
I thought that the low-values record was only necessary with older
versions of VSAM?

In article <OLCq0z0Y$GA.271@cpmsnbbsa02>, DennisHarley
<LegacyBlue@email.msn.com> writes
>It has been customary to add a record to a VSAM file to prevent errors.
>This is usually a record with a low-values key.
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eNMJvi1Y$GA.312@cpmsnbbsa03>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk>`

```
You are probably right.

I haven't seen any new development using VSAM in quite some time.
Most new work (mainframe) uses DB2.

The systems I do see use IAM, a VSAM replacement.

Thank you for the information.

Alistair Maclean <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk...
> I thought that the low-values record was only necessary with older
> versions of VSAM?
>
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 4)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eIlzwv5Y$GA.313@cpmsnbbsa03>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03>`

```

DennisHarley <LegacyBlue@email.msn.com> wrote in message
news:eNMJvi1Y$GA.312@cpmsnbbsa03...
> You are probably right.
>
…[4 more quoted lines elided]…
>

  What does IAM stand for?  (Indexed Access Method?  If so, it's a lot like
what VSAM replaced: ISAM.)


> Thank you for the information.
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 5)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#noU7V8Y$GA.257@cpmsnbbsa03>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03>`

```
Actually it is replacement for VSAM. I have used it in several shops.

You code your program as if you were using VSAM. No changes to file
definition, or I/O statements are needed. (Batch & CICS).

It uses IDCAMS to define files. Usually OWNER=($IAM) indicates the file is
IAM, not VSAM.

It supports larger cluster sizes. (I think 2048M is the largest VSAM cluster
size). This is the main reason that it is used.

It has data compression. I have been told the space savings are significant.

ChrisOsborne <chris_n_osborne@yahoo.com> wrote in message
news:eIlzwv5Y$GA.313@cpmsnbbsa03...
>
> DennisHarley <LegacyBlue@email.msn.com> wrote in message
…[9 more quoted lines elided]…
>   What does IAM stand for?  (Indexed Access Method?  If so, it's a lot
like
> what VSAM replaced: ISAM.)
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ VSAM

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38886FF2.64C97069@NOSPAMwebaccess.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03> <#noU7V8Y$GA.257@cpmsnbbsa03>`

```
My first experience with VSAM was when I moved from a Univac 9030 and
made all of our relative, flat, and keyed files VSAM, to keep our old
functionality.  But over the years, VSAM use has dropped considerably.

What is interesting is that when FILE-AID came out, it was an extremely
valuable tool.  Over time, TSO could handle larger files, and databases
have replaced KSDS files, so that FILE-AID is becoming less and less
valuable.  Currently I work in an environment without FILE-AID, but the
only VSAM file I care about will be going away this year.  This is also
the only VSAM file I have ever used via IDMS and I am very glad to see
its data move into standard database records.

Shops with relational databases have even less reason to go with VSAM. 
I still see a few cases where we might want a temporary indexed dataset
(VSAM really is designed for permanent files), even in a database shop
(aren't ALL shops database shops?), but databases are the way most shops
think nowadays.
```

###### ↳ ↳ ↳ Re: VSAM

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7bu0TCZ$GA.254@cpmsnbbsa02>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03> <#noU7V8Y$GA.257@cpmsnbbsa03> <38886FF2.64C97069@NOSPAMwebaccess.net>`

```

Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:38886FF2.64C97069@NOSPAMwebaccess.net...
>
> What is interesting is that when FILE-AID came out, it was an extremely
…[5 more quoted lines elided]…
> its data move into standard database records.

File-Aid DB2 is available. But as usual, the manuals are hard to find.
On-line help is available, but I would rather have something I can read on
the train. Most people I know use SPUFI or QMF. There is a facility in
File-Aid DB2 which analyzes the Plan Table for a query.

I still use File-Aid for a look see at sequential files, and existing VSAM
files.

> Shops with relational databases have even less reason to go with VSAM.
> I still see a few cases where we might want a temporary indexed dataset
> (VSAM really is designed for permanent files), even in a database shop
> (aren't ALL shops database shops?), but databases are the way most shops
> think nowadays.

I haven't see any new development in VSAM.
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 6)_

- **From:** Bill Lynch <WBLynch@att.net>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3888EB2B.5268973A@att.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03> <#noU7V8Y$GA.257@cpmsnbbsa03>`

```
DennisHarley wrote:
> 
> Actually it is replacement for VSAM. I have used it in several shops.
…[8 more quoted lines elided]…
> size). This is the main reason that it is used.

Historically (meaning from the mid-70's) IAM pushed performance and
their ability to exceed VSAM's 4 GB limit (per cluster). VSAM has since
(4-6 years ago?) addressed the 4 GB limit and IIRC the current limit is
4 GB CI's.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#ftqPaOZ$GA.276@cpmsnbbsa04>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03> <#noU7V8Y$GA.257@cpmsnbbsa03> <3888EB2B.5268973A@att.net>`

```
Thanks for the info.
Bill Lynch <WBLynch@att.net> wrote in message
news:3888EB2B.5268973A@att.net...
> DennisHarley wrote:
> >
…[5 more quoted lines elided]…
> > It uses IDCAMS to define files. Usually OWNER=($IAM) indicates the file
is
> > IAM, not VSAM.
> >
> > It supports larger cluster sizes. (I think 2048M is the largest VSAM
cluster
> > size). This is the main reason that it is used.
>
…[5 more quoted lines elided]…
> Bill Lynch
```

###### ↳ ↳ ↳ Thanks (was: Re: Read from a empty VSAM file)

_(reply depth: 6)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Op3j5rFZ$GA.269@cpmsnbbsa02>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <OLCq0z0Y$GA.271@cpmsnbbsa02> <L$6WgQBj0xh4EwDQ@ld50macca.demon.co.uk> <eNMJvi1Y$GA.312@cpmsnbbsa03> <eIlzwv5Y$GA.313@cpmsnbbsa03> <#noU7V8Y$GA.257@cpmsnbbsa03>`

```
Thank you.
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eSFh4.156$nx5.6588@dfiatx1-snr1.gtei.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
I think VSAM will return a status '35' on the open if the file contains no
records ("is not available to the program").

What I do is...

05  VSAM-FILE-STATUS   PIC X(02).
     88  VSAM-VIRGIN-FILE  VALUE '35'.   << check this, I'm working from
memory!
     88   VSAM-FILE-OK       VALUE '00'.
     88  (a couple more)...

  OPEN  INPUT (or I-O, as needed)  THE-VSAM-FILE
   IF VSAM-VIRGIN-FILE
       OPEN OUTPUT THE-VSAM-FILE
       CLOSE THE-VSAM-FILE
       OPEN INPUT THE-VSAM-FILE
   END-IF
   IF NOT VSAM-FILE-OK
     (error handler)...

-
Michael Mattias
Racine WI USA

Pepper wrote in message <866ult$gtf$1@bronx.mec.es>...
>I need help.
>
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eNNh4.1736$Xs.41212@news4.mia>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
VSAM Keyed Files (VSAM does NOT mean Indexed / Keyed! It means
Virtual Storage Access Method)  have three (3) states:

UNLOADED  - just created, nothing else done
LOADED  - at least one Data Record WRITten to file
EMPTY - All RECORDS Deleted   - - - @@@!!!  NOT THE SAME as UNLOADED.

AN UNLOADED FILE CAN ONLY be written to in OUTPUT mode.
When creating VSAM Keyed Files, do one of three things:

1) Immediately after IDCAMS CREATE,  do an IEDBG with a properly formatted
LOW-VALUES or
HI-VALUES) record, (THEN optionally do and IDCAMS DELETE

2) Have someone write an Assembler or 'C' program that gets the File LRECL
from the JSCB
(it must be a DD for the routine), and writes a 'dummy' record, ten deletes
same)

3) in the hi-level program, use DECLARATIVES to trap the error, and then
OPEN it OUPUT and
write and delete the rec.


Pepper <guest@mec.es> wrote in message news:866ult$gtf$1@bronx.mec.es...
> I need help.
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<868as6$5f1$1@nntp2.atl.mindspring.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
Assuming this is Batch, MOVE LOW-VALUES to Data-Field and issue a START KEY
NOT LESS THAN "Data-Field". I believe you'll get an immediate End-of-File
condition after the command completes. Note that your ACCESS must specify
SEQUENTIAL or DYNAMIC. RANDOM won't work.

If this is CICS, issue a STARTBR, specifying a RIDFLD Data-Field of
LOW-VALUES and use the NOHANDLE option. After completing the STARTBR, check
"IF EIBRESP IS EQUAL TO DFHRESP(NOTFND)". If this is condition true, then
the file is empty.

Do you know that the file is empty when you're about to read it ? If this is
true, why bother with the read at all ?

Chao,

WOB

Pepper <guest@mec.es> wrote in message news:866ult$gtf$1@bronx.mec.es...
> I need help.
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Read from a empty VSAM file

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3887D0FA.70ED51A7@worldnet.att.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
Pepper wrote:
> 
> I need help.
> 
> How i can read a empty VSAM file without a 3000 return code? If the VSAM
> file is empty i can write it but i can't read it.

Right, you can't read from an empty cluster. Aren't you going to write
records to it? RC=3000, what's your platform? In the IBM world you
couldn't open an empty cluster for input.

HTH,
Bill Lynch
```

##### ↳ ↳ Re: Read from a empty VSAM file

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<868s5r$cbq$1@nnrp1.deja.com>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <3887D0FA.70ED51A7@worldnet.att.net>`

```
In article <3887D0FA.70ED51A7@worldnet.att.net>,
  wblynch@worldnet.att.net wrote:
> Pepper wrote:
> >
> > I need help.
> >
> > How i can read a empty VSAM file without a 3000 return code? If the
VSAM
> > file is empty i can write it but i can't read it.
>
…[6 more quoted lines elided]…
>

Bill,

I guess I've been working in CICS too long. I didn't realize (or maybe
I just plain forgot) the manner in which Batch handles an empty VSAM
file.

I stand corrected.

Chao,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ RE: Read from a empty VSAM file

- **From:** "Pepper" <guest@mec.es>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<869bub$ks7$1@bronx.mec.es>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
Thank you everybody.

I'm testing the 35 return code and then opening and closing the VSAM file
and this work fine. But now, when i'm trying to read a record it's giving me
a 23 return
code and i don't know what's meaning. It's like 'record not found', but, why
this isn't control in the 'invalid key' clause?. (i'm working in batch)

Thank you again.
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "George McGinn" <gmcginn@home.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LR0i4.752$M2.6554@ha1>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
What is happening is that the RBA of the file is zero.  In order to set it,
you only need to write a record to the file, then delete it.  Now the file
can be opened empty in both Batch and CICS.

Anything that can open the VSAM file as OUTPUT, WRITE a record, then DELETE
a record will work.  COBOL, PL/I, REXX, ASSEMBLER will all work fine.


----------------------------------------------------
George McGinn
Systems Engineer
Information Technology - Tampa
201 N. Franklin Street, MS6B
Tampa  FL    33601

* Email - gmcginn <@> tsi <.> gte <.> com
* Voice - (813) 273-4939
* Fax - (813) 273-3324
* Pager - (941) 750-3735



Pepper <guest@mec.es> wrote in message news:866ult$gtf$1@bronx.mec.es...
> I need help.
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Read from a empty VSAM file

- **From:** Barry Steinholtz <Bstein@Castle.Net>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3888BED3.CF6E5BB0@Castle.Net>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
Pepper wrote:
> 
> I need help.
…[6 more quoted lines elided]…
> Thank you.

Hi:

	When you open the empty database the file status will come back with a
return code, a 35 I believe. When this happens, open the database for
output and load it. Then you can do anything you want with it.
```

#### ↳ Re: Read from a empty VSAM file

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86b2tt$fsi$1@nntp2.atl.mindspring.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
I haven't seen anyone mention this, so I'm almost thinking I must be missing
something, but...

SELECT OPTIONAL FILE-NAME
    ASSIGN TO DDNAME.

As far as I know, and I have used this, you will get a '00' when you open
the file, and a '10' (EOF) when you attempt to read a record.  (There are
some cases, maybe SAM files, where you'll get an '05' instead of the '00'
when you open the file, but anything '10' and below is a "non-error" code.
```

##### ↳ ↳ Re: Read from a empty VSAM file

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86b9ff$56b$1@nnrp1.deja.com>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net>`

```
In article <86b2tt$fsi$1@nntp2.atl.mindspring.net>,
  "Frank Swarbrick" <infocat@sprynet.com> wrote:
> I haven't seen anyone mention this, so I'm almost thinking I must be
missing
> something, but...
>
…[3 more quoted lines elided]…
> As far as I know, and I have used this, you will get a '00' when you
open
> the file, and a '10' (EOF) when you attempt to read a record.  (There
are
> some cases, maybe SAM files, where you'll get an '05' instead of
the '00'
> when you open the file, but anything '10' and below is a "non-error"
code.
> --
> Frank Swarbrick
> home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
> "Ignorance and prejudice - and fear - walk hand in hand" --
Rush  "Witch
> Hunt"
> Pepper <guest@mec.es> wrote in message
news:866ult$gtf$1@bronx.mec.es...
> > I need help.
> >
> > How i can read a empty VSAM file without a 3000 return code? If the
VSAM
> > file is empty i can write it but i can't read it.
> >
…[6 more quoted lines elided]…
>

Frank,

I had mentioned something similar, but other postings indicated that
this wouldn't work. Now, after your post, I'm not sure who's right.

Chao,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Read from a empty VSAM file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CYhi4.105$Xn1.4359@dfiatx1-snr1.gtei.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net>`

```
Yeah, I think you are right about that. The IBM literature mentions that by
making the file OPTIONAL it will make "the file available to the program"
when opened, even if it never contained any records. I just use the OPEN
OUTPUT/CLOSE/OPEN INPUT|I-O sequence because that's also in the IBM
literature, it works, and I thought it would be less confusing to the next
poor schmuck who had to maintain the program. (Especially true when I might
be that next poor schmuck). To me, OPTIONAL files should never be files
which are always opened; they should be, well, optional.
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86e1np$60k$1@nntp2.atl.mindspring.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net> <CYhi4.105$Xn1.4359@dfiatx1-snr1.gtei.net>`

```
I'm not quite sure what you mean.  I don't think OPTIONAL has anything to do
with the program making some decision whether or not the file will be open
this run.  You can do that with any file, OPTIONAL or not.  OPTIONAL only
means that the file need not contain any records.  At least that's my
understanding.
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ekGi4.2570$Xn1.54797@dfiatx1-snr1.gtei.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net> <CYhi4.105$Xn1.4359@dfiatx1-snr1.gtei.net> <86e1np$60k$1@nntp2.atl.mindspring.net>`

```
I mean that although the use of a file which is..

    SELECT OPTIONAL THE-VSAM-FILE.....

..will "automagically" solve the problem of using a VSAM file which has
never held any records, as "the next poor schmuck" who has to maintain the
program, I would be looking for the conditions under which the program does
or does not require the presence of the file; I would not expect the file to
be mandatory.

I guess that's because my mom and dad taught me English before I learned to
speak COBOL.

MCM


Frank Swarbrick wrote in message <86e1np$60k$1@nntp2.atl.mindspring.net>...
>I'm not quite sure what you mean.  I don't think OPTIONAL has anything to
do
>with the program making some decision whether or not the file will be open
>this run.  You can do that with any file, OPTIONAL or not.  OPTIONAL only
…[3 more quoted lines elided]…
>--
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 5)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86fdpv$hoc$1@news.inet.tele.dk>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net> <CYhi4.105$Xn1.4359@dfiatx1-snr1.gtei.net> <86e1np$60k$1@nntp2.atl.mindspring.net> <ekGi4.2570$Xn1.54797@dfiatx1-snr1.gtei.net>`

```
Did they succeed?
regards
Ib
Michael Mattias skrev i meddelelsen ...
>I mean that although the use of a file which is..
>
…[5 more quoted lines elided]…
>or does not require the presence of the file; I would not expect the file
to
>be mandatory.
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Read from a empty VSAM file

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86iv7s$eg2$1@nntp2.atl.mindspring.net>`
- **References:** `<866ult$gtf$1@bronx.mec.es> <86b2tt$fsi$1@nntp2.atl.mindspring.net> <CYhi4.105$Xn1.4359@dfiatx1-snr1.gtei.net> <86e1np$60k$1@nntp2.atl.mindspring.net> <ekGi4.2570$Xn1.54797@dfiatx1-snr1.gtei.net>`

```
Don't expect me to defend the terminology "OPTIONAL."  I don't think it's a
proper description, either.
```

#### ↳ Re: Read from a empty VSAM file

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000122163914.14794.00000133@ng-ba1.aol.com>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
put one record in with low- or high- values
```

#### ↳ Re: Read from a empty VSAM file

- **From:** slarsen22@aol.com (SLarsen22)
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000129153014.28337.00000320@ng-cd1.aol.com>`
- **References:** `<866ult$gtf$1@bronx.mec.es>`

```
If it is empty you shouldn't need  to read it. Anyway, I think you need to make
it "dynamic" and open it I-O.
.Pray to God but row the boat for shore....
 >http://members.aol.com/SLarsen22>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
