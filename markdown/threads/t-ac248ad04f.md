[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting without an output file

_21 messages · 12 participants · 2000-08_

---

### Sorting without an output file

- **From:** "Camenwent" <camslixz@hotmail.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sp70vn36n4t111@corp.supernews.com>`

```
I've been searching the net for examples of just how to do this. All the
examples that I've found require an Input File...a Sort File....and an
Output File ie(sorted file).

I don't want to create a sorted file...I simply want to use the sort (work)
file to create a report.


For those brainiacs that have nothing better to do than kick everyone else
down....yes I have done my homework....I'm using "COBOL From Micro to
Mainframe" published by Prenhall....they have no example or explanation of
sorting like this, so please if you don't want to be part of the solution
drag your dog behind your car or whatever else makes you feel more like men.
```

#### ↳ Re: Sorting without an output file

- **From:** "Jason S. Adams" <jsa@kona.homeip.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000811.220545.4940@kona.homeip.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```
Depending on the capabilities of your compiler
SORT SORT-FILE
  ON ASCENDING ....
   INPUT PROCEDURE IS paragraph-name 
   OUTPUT PROCEDURE IS paragraph-name

-output procedure is where you employ the
RETURN verb to get your records back from
sort to use in your report...


In article <sp70vn36n4t111@corp.supernews.com>, "Camenwent"
<camslixz@hotmail.com> wrote:

> I've been searching the net for examples of just how to do this. All the
> examples that I've found require an Input File...a Sort File....and an
…[13 more quoted lines elided]…
>
```

#### ↳ Re: Sorting without an output file

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n02g4$1fo$1@nntp9.atl.mindspring.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```
Well, there is a relatively easy way to do this.  In your SORT statement have
a "using" statement pointing to the input file; do the sort (as usual) on the
SD description - BUT then also use an OUTPUT procedure instead of a GIVING
file.

My personal suggestion would be to use Report Writer in your OUTPUT
PROCEDURE - but if you want to use the "manual" method, you can do that too.

Now, you haven't told us which compiler and operating system you are using.
If this is *not* a class assignment *and* you are running under OS/390 (IBM
mainframe), then you could also look into "ICETOOL" (a part of DFSort).  This
has some "simple" reporting features that might give you all you want.
```

##### ↳ ↳ Re: Sorting without an output file

- **From:** Frank Yaeger <fyaeger5@vnet.ibm.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39941BD4.ADA035FA@vnet.ibm.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" wrote:

> ...

> If ... you are running under OS/390 (IBM
> mainframe), then you could also look into "ICETOOL" (a part of DFSort).  This
> has some "simple" reporting features that might give you all you want.
>

Bill,
   Thanks for mentioning DFSORT/ICETOOL, but I have to differ with the word
"simple".  DFSORT actually offers fairly sophisticated reporting functions with
the DISPLAY operator of ICETOOL, and quite sophisticated reporting functions with
the OUTFIL feature.  For more information on DFSORT's ICETOOL, see:

http://www.storage.ibm.com/software/sort/srtmatol.htm

For more information on DFSORT's OUTFIL feature, see:

http://www.storage.ibm.com/software/sort/srtmaoft.htm

Frank Yaeger - DFSORT Team (Specialties: Symbols, OUTFIL, ICETOOL, Y2K)
fyaeger@vnet.ibm.com
=> DFSORT/MVS is on the WWW at
     http://www.ibm.com/storage/dfsort/
```

###### ↳ ↳ ↳ Re: Sorting without an output file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39942500.DDF65C3B@brazee.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <39941BD4.ADA035FA@vnet.ibm.com>`

```
Frank Yaeger wrote:

>  For more information on DFSORT's ICETOOL, see:
>
…[4 more quoted lines elided]…
> http://www.storage.ibm.com/software/sort/srtmaoft.htm

That Professor Sort looks familiar, where does he teach?
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 4)_

- **From:** Frank Yaeger <fyaeger5@vnet.ibm.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3994379B.BAA91841@vnet.ibm.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <39941BD4.ADA035FA@vnet.ibm.com> <39942500.DDF65C3B@brazee.net>`

```


Howard Brazee wrote:

> That Professor Sort looks familiar, where does he teach?

He only teaches on the DFSORT Web site (unless he moonlights somewhere
else in his off hours and hasn't told me about it :-)

Frank Yaeger - DFSORT Team (Specialties: Symbols, OUTFIL, ICETOOL, Y2K)
fyaeger@vnet.ibm.com
=> DFSORT/MVS is on the WWW at
     http://www.ibm.com/storage/dfsort/
```

##### ↳ ↳ Re: Sorting without an output file

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399430af.16289217@207.126.101.100>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net>`

```
On Fri, 11 Aug 2000 00:21:14 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:


>My personal suggestion would be to use Report Writer in your OUTPUT
>PROCEDURE - but if you want to use the "manual" method, you can do that too.
>

I was a non report writer uer for a long long time.  For a recent
project I HAD to learn it.  I didn't know what I was missing.  You can
actually learn report writer FASTER than you can code the report
manually.  An you only need to learn it once.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Sorting without an output file

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100>`

```
On Fri, 11 Aug 2000 16:59:55 GMT, thaneH@softwaresimple.com (Thane Hubbell) wrote:

Hello Thane,

welcome to the club (of converted non-RW users)


>On Fri, 11 Aug 2000 00:21:14 -0500, "William M. Klein"
><wmklein@nospam.ix.netcom.com> wrote:
…[12 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Bad command or file name. Go stand in the corner.
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3995D871.FB0D7655@home.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com>`

```


Volker Bandke wrote:
> 
> On Fri, 11 Aug 2000 16:59:55 GMT, thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[3 more quoted lines elided]…
> welcome to the club (of converted non-RW users)

Volker,

I tried the 'club' years ago and it works. But with a PC and wanting
fonts and styles ? And that is exactly why PC-users have latched on to
Crystal Report, although in my case, I'm quite happy with N/E PC_PRINT.

Jimmy
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 5)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com>`

```
On Sat, 12 Aug 2000 23:09:30 GMT, "James J. Gavan" <jjgavan@home.com> wrote:

>
>
…[14 more quoted lines elided]…
>Jimmy

Jimmy, 

didn't I send you a message that RW (NT and OS/2) does support laser printers, styles,
fonts, etc?

And RW is closer to COBOL than an external product, like crystal reports

But .. chaq'un ï¿½ son goï¿½t
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-16T05:43:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399A29E2.DCDE033D@home.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com> <dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com>`

```


Volker Bandke wrote:
> 
> 
…[6 more quoted lines elided]…
> 
Sorry Volker,

Can't remember - but did a quick check on N/E on-line for R/W - just see
standard references and nothing about fonts/styles. That has to be why
they provided PC_PRINT in the first place.

> But .. chaq'un ï¿½ son goï¿½t

Other than putting the above through Babelfish - I aint got gout <G>.
Having spent only 4 hours in la belle France - I don't go much beyond
"La plume de ma tante". I remember when our teacher got Pierre from
France to stand up and read Aesop's 'Crow and the Fox'. With that
guttural Strasbourg accent "Le CORRRRRRbeau et le RRRRRRenaRRRRd" came
out like he was speaking Deutsch !

Jimmy
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ne3vg$89k$1@nntp9.atl.mindspring.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com> <dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com> <399A29E2.DCDE033D@home.com>`

```
Jimmy,
  The font/style support is NOT in the "native" N/E product; it is provided
by a report-writer "add-on product". That provides both ANSI conforming RW,
and IBM compatible RW, and many of the enhancements from the draft Standard
(as well as many extensions).

This is the same product that is used on IBM Mainframes and with a VARIETY of
PC COBOL compilers.

I can get you the details, if you are interested.
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-18T02:29:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399C9F42.1580F247@home.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com> <dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com> <399A29E2.DCDE033D@home.com> <8ne3vg$89k$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Jimmy,
…[9 more quoted lines elided]…
> 
Oui, peut-ï¿½tre. Mais, combien ???($$$$) (I 'cheated' - Babelfish <G>)

Jimmy
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nj7im$nvq$1@slb0.atl.mindspring.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com> <dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com> <399A29E2.DCDE033D@home.com> <8ne3vg$89k$1@nntp9.atl.mindspring.net> <399C9F42.1580F247@home.com>`

```
Jimmy - and others, check out

 http://www.spc-systems.com/
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-22T04:57:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39A207FB.364A164B@home.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <587apscfpur5r9guran3nu3eg5b9qlauug@4ax.com> <3995D871.FB0D7655@home.com> <dmqdpskvioatc92nl20km0pjasoeeiqfdk@4ax.com> <399A29E2.DCDE033D@home.com> <8ne3vg$89k$1@nntp9.atl.mindspring.net> <399C9F42.1580F247@home.com> <8nj7im$nvq$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Jimmy - and others, check out
> 
>  http://www.spc-systems.com/

Thanks for the tip - I didn't realize you were gonna point me to John
Piggott <G>. "Now John, while we are having this nice cup of coffee at
Newbury, howz about a cheapie for a PC ....?"

Jimmy
```

###### ↳ ↳ ↳ Re: Sorting without an output file

- **From:** Jeffry Kennedy <jakcert@attglobal.net>
- **Date:** 2000-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3997DFE4.12924047@attglobal.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100>`

```
I've been using report writer for about 15 years.  When we upgraded to COBOL for
VSE/ESA we had to buy the Report Writer ad on. It was well worth the $10,000
price tag.  I've never understood why more people aren't using the report writer
feature of COBOL.  It's a mighty powerful and easy tool.

Pat Hall

Thane Hubbell wrote:

> On Fri, 11 Aug 2000 00:21:14 -0500, "William M. Klein"
> <wmklein@nospam.ix.netcom.com> wrote:
…[11 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Sorting without an output file

_(reply depth: 4)_

- **From:** jack <jacksleightNOjaSPAM@hotmail.com.invalid>
- **Date:** 2000-08-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0083c2c8.640eb18d@usw-ex0105-034.remarq.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com> <8n02g4$1fo$1@nntp9.atl.mindspring.net> <399430af.16289217@207.126.101.100> <3997DFE4.12924047@attglobal.net>`

```
CAMENWENT's post reminds me of that old story about the guy who
gets a flat in the middle of nowhere. He spies a farmhouse far in
from the road and starts out on the trek to borrow a jack. All
thew way he's beseiged with thoughts of how gingoistic these
small town hicks are; how small minded and selfish, etc., etc.
and this goes on until he's on the farmer's doorstep and knocks;
the farmer answers the door and the driver says "You can take
your jack and shove it!"


-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

#### ↳ Re: Sorting without an output file

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-Upmy4QLSkeKs@tcpserver>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```
On Fri, 11 Aug 2000 04:37:08, "Camenwent" <camslixz@hotmail.com> 
wrote:

> I've been searching the net for examples of just how to do this. All the
> examples that I've found require an Input File...a Sort File....and an
…[12 more quoted lines elided]…
> 

The sort command supports both input and output procedures. The syntax
is something like this

	sort sort-file ascending key key-1 key-2
		input procedure 001-sort-input thru 002-end-input
		output procedure 003-sort-output thru 004-end-output.

You would have an input procedure that assembles the data you want to 
have in your report in the paragraphs 001-sort-input through to 
002-end-input and the code to write out your report in paragraphs 
003-sort-output throughto 004-end-output. Something like the following

001-sort-input.

perform
	read input-file at end exit perform end-read
	do stuff to the data and put it in the sort-record
	release sort-record
end-perform

002-end-input.
	exit.

003-sort-output.

	return sort-file at end go to 004-end-output end-return
	do a bunch of stuff and write out the report lines
	go to 003-sort-output.

004-end-output.
	exit.

The actual program would hopefully have some real logic in it.

The verb "release" is used to send a record to the sort module. The 
verb "return" is used to obtain a record from the sort module. The 
records are returned to the program in the order specified by the 
"ascending key" and "descending key" clauses of the sort verb.

Hope this helps...
```

#### ↳ Re: Sorting without an output file

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<399397A7.36C67F3@home.com>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```


Camenwent wrote:
> 
> I've been searching the net for examples of just how to do this. All the
…[10 more quoted lines elided]…
> drag your dog behind your car or whatever else makes you feel more like men.

Watch it mate - you're talking to a dog lover - AND I also love quiche
<G>

Two possibilities - 

(1) Is there an external sort routine that comes with your compiler, e.g
Merant(Micro Focus) have one for PCs 

(2) Don't like the idea of three files ? - 

(a) determine what the 'Key' is that you want to print with, e.g :-
 
record fields :-
	05 a	pic x(02).
	05 b	pic 9(03).
	05 c	pic x(27).
	05 d	pic x(03).
	05 e etc....

Your print sequence is 'd', then 'a', then 'b', so your PrimKey becomes
:-
	dddaabbb

(b) open as INPUT and read in your sequential(?) file 
(c) open OUTPUT a temporary Indexed file
(d) Now write records from sequential to output with the key
(e) close sequential and temporary
(f) Open INPUT your temporary - now start reading sequentially.......

(3) I'm not going to explain it, (I can't <G>) and you wouldn't want to
know anyway,  but there are algorithms to 'tag' each record with its 
immediate predecessor or successor to read in proper sequence.

Jimmy, Calgary AB
```

#### ↳ Re: Sorting without an output file

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MsSk5.2211$cl.226391@news2.mia>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```
No problem.  Instead of using

    SORT ...
        USING ...
        GIVING ...

use this format

    SORT ...
        USING ...
        OUTPUT PROCEDURE <procedure name> [ THRU <procedure name> ]

or this format

    SORT ...
        INPUT PROCEDURE  <procedure name> [ THRU <procedure name> ]
        OUTPUT PROCEDURE <procedure name> [ THRU <procedure name> ]

In your output procedure, remember these two things:

1) Use the RETURN statement (which is exactly like, and essentially
   is, a sequential file READ of the SD file) to 'read' the sorted
   records from the SD file.

2) Open any output FD files you need, and close them when finished,
   but *do not* open or close the SD file, the SORT mechanism opens
   and closes the SD file for you.

If you do a sort with INPUT PROCEDURE ... use the RELEASE statement
to 'write' the records to the SD file, and also do not open or close
the SD in the input procedure either.  Of course, you must open and
close any normal input FD files you need for the input procedure.

And FYI, the RELEASE and RETURN statements function logically just
like sequential file WRITE and READ statements, respectively.  But,
depending on the system, they may actually pass the records to and
from some other sorting process resident in the system, and may
never actually get written to disk.  The logical result is the same,
however.  It is generally a good idea not to have other files open
during a SORT, except for files opened and closed inside input and
output procedures.
```

#### ↳ Re: Sorting without an output file

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39940335.ED716CCA@brazee.net>`
- **References:** `<sp70vn36n4t111@corp.supernews.com>`

```
You want to use the "OUTPUT PROCEDURE" clause of the sort statement.  Doing a
quick Yahoo search on "sort output procedure cobol" gave me quite a few hits.

Do you have a COBOL manual?

Camenwent wrote:

> I've been searching the net for examples of just how to do this. All the
> examples that I've found require an Input File...a Sort File....and an
…[9 more quoted lines elided]…
> drag your dog behind your car or whatever else makes you feel more like men.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
