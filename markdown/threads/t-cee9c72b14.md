[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unlocking ISAM data

_9 messages · 4 participants · 2013-07 → 2013-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Unlocking ISAM data

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-24T00:01:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b591sgFe8s8U1@mid.individual.net>`

```
We have a client who wants to be able to point his Fujitsu ISAM files at a
reporting package like Stimulsoft or Tableau.

Most of these packages are designed to talk to a database or XML and
although we can generate an RDB tableset for him and load it in a few
seconds, he isn't ready to do that just yet.

(Later on he is planning to migrate his current Fujitsu COBOL applications
using the PRIMA Toolset, so he would like any solution we give him to be
able to "switch" to RDB as a datasource, instead of ISAM. That's not a
problem as long as we get the datasource right.)

I have decided to build an ISAM file extractor that will take any (Fujitsu)
ISAM file and create the contents wrapped as XML, that can be registered as
a datasource for the reporting packages.

I couldn't find a decent ODBC driver for Fujitsu ISAM (apart from
Relativity, which is far too expensive...) so we are being driven to XML.

Obviously, ISAM files don't contain metadata, (like a database does), so the
final tool will probably need to have the COBOL COPY book with the FD fed to
it.

Fortunately, the COBDATA tool (free from the PRIMA website) can analyze an
FD and we can use this to help build the final XML output.

However, before diving into this I was wondering if anyone here has an
existing tool that can convert ISAM data to XML? Or maybe anyone has some
other thoughts on how they would approach this?

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Unlocking ISAM data

- **From:** "alistair.j.l.maclean" <ua-author-14501550@usenetarchives.gap>
- **Date:** 2013-07-24T10:57:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p2@usenetarchives.gap>`
- **In-Reply-To:** `<b591sgFe8s8U1@mid.individual.net>`
- **References:** `<b591sgFe8s8U1@mid.individual.net>`

```
On Wednesday, 24 July 2013 05:01:18 UTC+1, Pete Dashwood wrote:

›
› However, before diving into this I was wondering if anyone here has an
…[4 more quoted lines elided]…
›

I wrote an XML Parser which would work the other way. Give me four years and I might get around to writing an ISAM to XML tool. Sorry, no. And it wouldn't be a trivial task either.
```

##### ↳ ↳ Re: Unlocking ISAM data

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-24T12:02:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p2@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p2@usenetarchives.gap>`

```
Alistair Maclean wrote:
› On Wednesday, 24 July 2013 05:01:18 UTC+1, Pete Dashwood  wrote:
› 
…[12 more quoted lines elided]…
› no. And it wouldn't be a trivial task either.

Thanks Alistair.

The XML is pretty easy; it's being able to read ANY ISAM file and not
knowing until runtime which one... (NO predefined specific SELECT so no
predefined key information...)

COBOL seems to require the key to be specified (even if access is
sequential) and that will be unknown until run time. I think I can solve
that by specifying it as a sequential file rather than ISAM. If not, I'll
have to resort to the special C++ routines in the Fujitsu COBOL runtime. One
of those will return information about keys and lengths but I'd probably
then have to use some of those routines to do the actual reading and I was
hoping to avoid that. (This is a case where COBOL is definitely the right
tool for that particular job.)

As long as we can input the COBOL COPYbook for the FD, the XML build really
isn't too hard:

(I'll write the extractor in C# so that all the .Net services and classes
are available)

1. Run the COPY book through COBDATA. (Gets all the field names and their
offsets and lengths. I have become a dab hand at calling COBOL from C# and
vice versa, so there should be no problem in using the COBDATA COBOL COM
component.)
2. Call something to read the ISAM file as a sequential file. (Get one
record with automatic open and close as required) Maybe a COBOL component or
maybe C++ to do this.
3. Use the information from COBDATA to fetch data from the returned buffer
and set the values in the XML elements. As I also have the pictures
available, it would be pretty easy to specify the field's data type as well
as its value for each field, but that may be release 2...
4. Write the XML elements for the record using the .Net XML services.

Repeat from 2 until EOF...

It's not a great solution but it will work. It might also be handy in the
future to have an extractor utility that can read Fujitsu ISAM and create
XML that is acceptable to reporting tools.

I don't really mind building it, but I didn't want to re-invent the wheel...

Pete.
.--
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Unlocking ISAM data

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-07-25T09:14:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p3@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p2@usenetarchives.gap> <gap-cee9c72b14-p3@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:

[snip]

› 1. Run the COPY book through COBDATA. (Gets all the field names and their 
› offsets and lengths. I have become a dab hand at calling COBOL from C# and 
…[4 more quoted lines elided]…
› maybe C++ to do this.

Caution is suggested, Mr Dashwood. ISAM implementation is, I believe,
vendor-specific.

My memory is, admittedly, porous but I recall something about how a
deleted ISAM record is marked with X'00' but physically is present until
the dataset is reorganised/defragmented.

DD
```

###### ↳ ↳ ↳ Re: Unlocking ISAM data

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-25T23:18:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p4@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p2@usenetarchives.gap> <gap-cee9c72b14-p3@usenetarchives.gap> <gap-cee9c72b14-p4@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[12 more quoted lines elided]…
› vendor-specific.

Thanks for the heads-up, Doc.

Yes, ISAM does vary widely across vendors and versions (not to mention,
platforms...)

However, the specific ISAM targeted here is Fujitsu for NetCOBOL, so if the
code to access it is written with that, it should work.
›
› My memory is, admittedly, porous but I recall something about how a
› deleted ISAM record is marked with X'00' but physically is present
› until the dataset is reorganised/defragmented.

Yes, that's right. But it is all transparent if you access with COBOL.

I knocked up the code pretty quickly and found to my chagrin that COBOL
requires a RECORD KEY clause with indexed files even if you are accessing
sequentially. That means I couldn't write a generic solution in COBOL
because each file has different key lengths and positions and will require
its own SELECT to identify them.

I tried just reading it as a sequential file (removed ORGANIZATION IS
INDEXED from it) and it returned garbage.

Then I realized that it is possible to access the underlying routines used
by the COBOL runtime from C++ and this is documented so I had a look through
it. Unfortunately, one of the parameters required by the OPEN subroutine
(for INDEXED files) is a pointer to a structure which defines the keys...
so, no advantage in going there.

The only way I could make it work was with a specifc file (specific
SELECT/FD) and that would mean having a separate access module for each of
the files involved.

The real message here is that if you want the facility of some of the really
excellent reporting tools available now, you should move your ISAM files to
RDB...

After sleeping on it I decided to have another look and see if I could bend
the low-level (C++) OPEN routine. In one of a number of web searches I did,
I acquired some later documentation which said you could pass a NULL pointer
to the key structure...

(I haven't tried doing the equivalent through COBOL ("...RECORD KEY IS
NULL") but I should think it will throw a compile error...)

So it is possible to write a generic ISAM handler if you REALLY want to.

Meantime, the client has decided to migrate to RDB :-)

(Sighs of relief all round...)

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Unlocking ISAM data

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-07-28T09:51:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p5@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p2@usenetarchives.gap> <gap-cee9c72b14-p3@usenetarchives.gap> <gap-cee9c72b14-p4@usenetarchives.gap> <gap-cee9c72b14-p5@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
 
› [snip]
 
›› Caution is suggested, Mr Dashwood.  ISAM implementation is, I believe,
›› vendor-specific.
› 
› Thanks for the heads-up, Doc.

You're quite welcome. Is your Grannie available? I've learnt something
interesting about eggs, too!

[snip]

› Meantime, the client has decided to migrate to RDB :-)

The design, however, will have to mimic ISAM because that's what everyone
is accustomed to... until the Old Guard moves along and folks start asking
to do (stuff).

DD
```

###### ↳ ↳ ↳ Re: Unlocking ISAM data

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-07-29T20:42:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p6@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p2@usenetarchives.gap> <gap-cee9c72b14-p3@usenetarchives.gap> <gap-cee9c72b14-p4@usenetarchives.gap> <gap-cee9c72b14-p5@usenetarchives.gap> <gap-cee9c72b14-p6@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[18 more quoted lines elided]…
› folks start asking to do (stuff).

Fortunately, the design isn't tied to ISAM specifically. Rather it is a
series of programs (in PowerCOBOL, as it happens...) which use sequential,
random, and skip sequential processing. (It is just a question of
perception; if you perceive it functionally, that's what it does, if you
perceive it technically, it uses ISAM... :-))

The transformation process we use enables all the old code to access the RDB
without any changes to the processing logic, so it will continue to use
sequential, random, and skip sequential processing. (Without the need for
overnight batch synchronization or downstream feeds to get data from legacy
into new development) The RDB supports these activities just as ISAM used
to. The main advantage is that the data being manipulated by these programs
can now be shared directly with new technology and third party tools (in
this case, they especially want to use the Stimulsoft reporting tool, which
they can't with ISAM unless we write extracts, and that isn't as easy as one
might think...), hence the topic of this thread...

Once the data is unlocked, the transition to new technology can be effected
at a controlled pace and gradually. There is no pressure to migrate or do a
"Big Bang"conversion. Old and New share the same data resources.

"'Tis a consummation devoutly to be wished..." :-)

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Unlocking ISAM data

- **From:** "real-email-in-msg-spam" <ua-author-5864872@usenetarchives.gap>
- **Date:** 2013-11-17T09:56:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p8@usenetarchives.gap>`
- **In-Reply-To:** `<b591sgFe8s8U1@mid.individual.net>`
- **References:** `<b591sgFe8s8U1@mid.individual.net>`

```
On Wed, 24 Jul 2013 16:01:18 +1200, "Pete Dashwood"
wrote:

› We have a client who wants to be able to point his Fujitsu ISAM files at a 
› reporting package like Stimulsoft or Tableau.
…[28 more quoted lines elided]…
› Pete.

Hi Pete,

Been away for too long from newsgroups so only saw this now.

there is a tool you can have a look at and extract the bits you need
from it and do it in c# or other language.

http://record-editor.sourceforge.net/Record03.htm
the product itself would also allow creation of the xml file itself
but for your case I think it would be better you extracted the file
read bits

Frederico


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Unlocking ISAM data

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-11-17T18:13:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cee9c72b14-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cee9c72b14-p8@usenetarchives.gap>`
- **References:** `<b591sgFe8s8U1@mid.individual.net> <gap-cee9c72b14-p8@usenetarchives.gap>`

```
Frederico Fonseca wrote:
› On Wed, 24 Jul 2013 16:01:18 +1200, "Pete Dashwood"
›  wrote:
…[37 more quoted lines elided]…
› Been away for too long from newsgroups so only saw this now.

I understand how you feel... I'm considering some absence myself; it gets
tiresome being constantly beat up ... :-)
› 
› there is a tool you can have a look at and extract the bits you need
…[6 more quoted lines elided]…
› 
The problem has now been solved and everyone is happy. We used a generic
template in COBOL to generate a COBOL ISAM file reader component for any
ISAM file. (It's a NetCOBOL COM component)

A C# module calls the appropriate COBOL ISAM reader and gets COBOL records
passed to it.

It then uses the COBDATA component to get the COBOL structure (offsets and
lengths in the COBOL buffer) and generating XML from that is trivial in C#.

Thanks for your response.

Pete.
"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
