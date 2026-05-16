[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# looking for utility to show file layouts from copybooks

_12 messages · 11 participants · 1999-02_

---

### looking for utility to show file layouts from copybooks

- **From:** rob_wolfe@dmr.com
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
This probably sounds strange but......

I am looking for a utility that will take a copybook as input and print out a
file layout (ie start and stop locations for fields). It should handle stuff
like redefs and occurs in some intelligent manner. Oh yeah... it should run
either under win95 or NT or HP/UX and preferably be free too :))

Failing anyone knowing where to find such a beast, I am going to have to write
one and am not really looking forward to the prospect.

Thanks folks

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** "R. Hayes" <rmch@cadvision.com>
- **Date:** 1999-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c10977.0@news.cadvision.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
I'm not exactly sure what you're after, but I wrote a piece of code that
matches copy book fields to the data in a record layout

Unfortunately I made it column specific, but you might be able to adapt it
to your needs.

Let me know if you want the code.


rob_wolfe@dmr.com wrote in message <79qsti$ftc$1@nnrp1.dejanews.com>...
>This probably sounds strange but......
>
>I am looking for a utility that will take a copybook as input and print out
a
>file layout (ie start and stop locations for fields). It should handle
stuff
>like redefs and occurs in some intelligent manner. Oh yeah... it should run
>either under win95 or NT or HP/UX and preferably be free too :))
>
>Failing anyone knowing where to find such a beast, I am going to have to
write
>one and am not really looking forward to the prospect.
>
…[3 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C1C463.EE80A7C0@ASPMnetdoor.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
I've something written in C to handle that as well as a version to show only the
record length.  Distributed as begware <g>.

rob_wolfe@dmr.com wrote:

> I am looking for a utility that will take a copybook as input and print out a
> file layout (ie start and stop locations for fields). It should handle stuff
> like redefs and occurs in some intelligent manner. Oh yeah... it should run
```

##### ↳ ↳ Re: looking for utility to show file layouts from copybooks

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990210180234.10288.00000137@ng102.aol.com>`
- **References:** `<36C1C463.EE80A7C0@ASPMnetdoor.com>`

```
what about EZTrieve??
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** cwestbury@giant.intranet.com (Chris Westbury)
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1999Feb10.011934.19532@giant>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
In article <79qsti$ftc$1@nnrp1.dejanews.com>,
rob_wolfe@dmr.com wrote:
>
> I am looking for a utility that will take a copybook as input and print
…[3 more quoted lines elided]…
> be free too :))

Most compilers already do this.  Look at your compiler options; it's
often called MAP or DMAP.
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c181be@news3.us.ibm.net>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
go to http://www.etk.com download the 'create web interface in 30 secs'.
This will take a copy book and create a browser interface to a data entry
program for the file. As a by-product it produces a file with the layout.
This file could trivially be massaged to produce what YOU want.

rob_wolfe@dmr.com wrote in message <79qsti$ftc$1@nnrp1.dejanews.com>...
>This probably sounds strange but......
>
>I am looking for a utility that will take a copybook as input and print out
a
>file layout (ie start and stop locations for fields). It should handle
stuff
>like redefs and occurs in some intelligent manner. Oh yeah... it should run
>either under win95 or NT or HP/UX and preferably be free too :))
>
>Failing anyone knowing where to find such a beast, I am going to have to
write
>one and am not really looking forward to the prospect.
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79s4op$h7d$1@nnrp1.dejanews.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
Shouldn't be too hard to write something like that -- in COBOL!  With the
introduction of refrence modification, cobol can do free-form string handling
as easily as BASIC.

In article <79qsti$ftc$1@nnrp1.dejanews.com>,
  rob_wolfe@dmr.com wrote:
> This probably sounds strange but......
>
…[12 more quoted lines elided]…
>

Ed Stevens
Nissan Motor Mfg. Corp., USA

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: looking for utility to show file layouts from copybooks

- **From:** "R. Hayes" <rmch@cadvision.com>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c1a26f.0@news.cadvision.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com> <79s4op$h7d$1@nnrp1.dejanews.com>`

```
Yes indeed!

I used reference modification in my little chunk of code and it works great.


Ed.Stevens@nmm.nissan-usa.com wrote in message
<79s4op$h7d$1@nnrp1.dejanews.com>...
>Shouldn't be too hard to write something like that -- in COBOL!  With the
>introduction of refrence modification, cobol can do free-form string
handling
>as easily as BASIC.
>
…[4 more quoted lines elided]…
>> I am looking for a utility that will take a copybook as input and print
out a
>> file layout (ie start and stop locations for fields). It should handle
stuff
>> like redefs and occurs in some intelligent manner. Oh yeah... it should
run
>> either under win95 or NT or HP/UX and preferably be free too :))
>>
>> Failing anyone knowing where to find such a beast, I am going to have to
write
>> one and am not really looking forward to the prospect.
>>
…[10 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c1a6b8.0@news3.uswest.net>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
Rob Wolfe,

In the IBM universe, FILEAID is what you are looking for.  It's a big
purchase, though, something you would buy for your whole shop.
FILEAID allows easy mapping of data to copybooks, plus interactive
allocation and editing of vsam files, and other stuff.


rob_wolfe@dmr.com wrote in message <79qsti$ftc$1@nnrp1.dejanews.com>...
>This probably sounds strange but......
>
>I am looking for a utility that will take a copybook as input and print out
a
>file layout (ie start and stop locations for fields). It should handle
stuff
>like redefs and occurs in some intelligent manner. Oh yeah... it should run
>either under win95 or NT or HP/UX and preferably be free too :))
>
>Failing anyone knowing where to find such a beast, I am going to have to
write
>one and am not really looking forward to the prospect.
>
…[3 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C26B62.FFBB09DC@siber.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
rob_wolfe@dmr.com wrote:
> 
> This probably sounds strange but......
…[12 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own

We have utility called Cobol Reporter that for every data item,
including data items in FDs reports their lcoal and global offsets
and length.

http://www.siber.com/sct/tools/


Vadim Maslov
```

##### ↳ ↳ Re: looking for utility to show file layouts from copybooks

- **From:** Ian Glen <glenir@erols.com>
- **Date:** 1999-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C3A663.F83E287E@xxerols.com>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com> <36C26B62.FFBB09DC@siber.com>`

```
Olivadoti Associates sold something called FDChart that did this too -
but didn't it just merge with another company?

Ian Glen (no ex's)

Vadim Maslov wrote:
> 
> rob_wolfe@dmr.com wrote:
…[22 more quoted lines elided]…
> Vadim Maslov
```

#### ↳ Re: looking for utility to show file layouts from copybooks

- **From:** "John Hicks (Remove \\"nospam\\" from address before replying)" <johnhicks@nospam.ibm.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C86362.11A81D9@nospam.ibm.net>`
- **References:** `<79qsti$ftc$1@nnrp1.dejanews.com>`

```
I have a utility I wrote that creates a database table from a cobol data
copybook: one row per data element and with columns for:

-Data element key (unique sequential number)
-COBOL level number
-Dataname
-Group/elementary indicator
-Redefines indicator
-Maximum occurrences
-Size (elementary and group, aware of redefines and occurs)
-Usage
-Picture
-Sign indicator
-Value
-Record name (i.e. the current 01 level dataname)
-Pointer to group-level parent 
-Copybook name

It would be simple enough to patch it to give a starting point based on
a running sum of the size column.

It's written in Realia COBOL and is DOS-based. The output is a
comma-delimited file which can be imported into most any database.

If you're interested, let me know!

--John Hicks
johnhicks at ibm dot net

rob_wolfe@dmr.com wrote:
> 
> This probably sounds strange but......
…[12 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
