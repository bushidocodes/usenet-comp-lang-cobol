[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Layout Hell.

_96 messages · 17 participants · 2004-07_

---

### Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T17:33:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
Hi,
Could I have some help with this layout?
I am new to the layout scene, but if I could see some real examples, I might
get it. Then again, I might club myself with a shovel.
Thank you.
I just need to convert this file to Access or something normal.
Do you have any thoughts?
Thanks you.

       77  FILLER      PIC X(16)  VALUE 'CTLG==(ANDERA)===='.
       01  WWICTLG.
           10 CTLGOP-CO-NO              PIC X(3).
           10 CTLGCONTROL-SET-SEQ-NO    PIC S9(9) USAGE COMP.
           10 CTLGINVOICE-SEQ-NO        PIC S9(4) USAGE COMP.
           10 CTLGAP-CNTRL-ENTITY-CD    PIC X(4).
           10 CTLGINVOICE-TYPE-CD       PIC X(2).
           10 CTLGLEGACY-VENDOR-NO      PIC X(10).
           10 CTLGAP-VENDOR-NO          PIC X(30).
           10 CTLGAP-PO-NO              PIC X(30).
           10 CTLGAP-INVOICE-NO         PIC X(30).
           10 CTLGINVOICE-DT            PIC X(10).
           10 CTLGTOTAL-INVOICE-AM      PIC S9(11)V9(2) USAGE COMP-3.
           10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3.
           10 CTLGTERMS-CD              PIC X(2).
           10 CTLGCARRIER-CD            PIC X(10).
           10 CTLGCARRIER-PRO-NO        PIC X(10).
           10 CTLGSHIP-DT               PIC X(10).
           10 CTLGSHIP-VIA-CD           PIC X(3).
           10 CTLGSHIP-LOC-NO           PIC X(3).
           10 CTLGSHIP-WT               PIC X(10).
           10 CTLGSHIP-UNITS-DC         PIC X(10).
           10 CTLGSHIP-TY               PIC X(2).
       77 POSBOP-CO-NO             PIC S9(4) COMP.
       77 POSBCONTROL-SET-SEQ-NO   PIC S9(4) COMP.
       77 POSBINVOICE-SEQ-NO       PIC S9(4) COMP.
       77 POSBAP-CNTRL-ENTITY-CD   PIC S9(4) COMP.
       77 POSBINVOICE-TYPE-CD      PIC S9(4) COMP.
       77 POSBLEGACY-VENDOR-NO     PIC S9(4) COMP.
       77 POSBAP-VENDOR-NO         PIC S9(4) COMP.
       77 POSBAP-PO-NO             PIC S9(4) COMP.
       77 POSBAP-INVOICE-NO        PIC S9(4) COMP.
       77 POSBINVOICE-DT           PIC S9(4) COMP.
       77 POSBTOTAL-INVOICE-AM     PIC S9(4) COMP.
       77 POSBTOTAL-MERCH-AM       PIC S9(4) COMP.
       77 POSBTERMS-CD             PIC S9(4) COMP.
       77 POSBCARRIER-CD           PIC S9(4) COMP.
       77 POSBCARRIER-PRO-NO       PIC S9(4) COMP.
       77 POSBSHIP-DT              PIC S9(4) COMP.
       77 POSBSHIP-VIA-CD          PIC S9(4) COMP.
       77 POSBSHIP-LOC-NO          PIC S9(4) COMP.
       77 POSBSHIP-WT              PIC S9(4) COMP.
       77 POSBSHIP-UNITS-DC        PIC S9(4) COMP.
       77 POSBSHIP-TY              PIC S9(4) COMP.
```

#### ↳ Re: Layout Hell.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-15T23:59:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FTEJc.1591$4L7.319@newssvr33.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote in message
news:JZCdnZ690pjbiWrd4p2dnA@comcast.com...
> Could I have some help with this layout?
> I am new to the layout scene, but if I could see some real examples, I
might
> get it. Then again, I might club myself with a shovel.
> Thank you.
> I just need to convert this file to Access or something normal.

Um, if by "convert this file" you mean "convert the record layout" then your
X fields are alpha, your PIC 9 fields are numeric, usage immaterial...
CREATE TABLE  tablename (co_no VARCHAR(3), set_seq_no INTEGER,
...total_invoice_am NUMBER(11,2) (although specifically with MS-Access or
other engines based on Jet, CURRENCY might be a better choice for the
decimal money fields.).....

Or did you mean, convert some DATA currently residing in a file described by
this layout?

Well, that's a horse of another color; as well as a current topic here....
witnesseth this clip and my response, equally applicable.....

== BEGIN QUOTEe===
Scott Hooper" <shooper@rxworks.com> wrote in message
news:a8341757.0407142138.560efc01@posting.google.com...
> I have read through all the newsgroups I could find and am getting
> very confused about what to do with my files. I have a heaps of
…[5 more quoted lines elided]…
> reading these.

Tutorial: Using COBOL-created data with non-COBOL programs.

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm

The price is right (free for use).

Basically that will tell you you MUST have the COBOL FD or other record
layout documentation - but if you have the *.COB files, you have these
descriptions, so you are probably beyond the most frequent barrier to
success.

I have a Win/32 DLL which uses the FD info and then converts the data to
IEEE format; and several "base" conversion programs (BASIC language). Sounds
like that software would probably be exactly what you want.... except the
part where you say, " What I can't do is spend any money on a one-off tool."

But if you change your mind and are interested in a package of BASIC
language source/executable (PowerBASIC/Windows, very usable with Microsoft
Visual BASIC or any "C" for Windows)   - with the understanding it is not
free - please contact my office.

== END QUOTE ===
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Charles W. Cribbs II" <charlescribbs@earthlink.net>
- **Date:** 2004-07-16T00:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3FJc.9261$sV2.769@newsread2.news.atl.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FTEJc.1591$4L7.319@newssvr33.news.prodigy.com>`

```
You are not making yourself clear at all.  You have provided one record:

        01  WWICTLG.
>            10 CTLGOP-CO-NO              PIC X(3).
>            10 CTLGCONTROL-SET-SEQ-NO    PIC S9(9) USAGE COMP.
…[19 more quoted lines elided]…
>

I looked up what the 77 levels are used for and the book says, "You use 77
level to define an independent data item -- one that is not related in any
way to any of the data around it. There is nothing you can do with a 77
level you can't do with an 01 level."

So what you have here is one record, the part under the 01 to the next 77
level and a series of independent data variable names marked with the 77
levels.

A record layout is just an expression of a data record and its component
parts.  Say if I wanted to do something like the following:

01 test-record              pic x(132).

01 test-record-parts redefines
     test-record.
    05 alpha-data         pic x(30).
    05 date-data           pic 9(10).
    05 more-alpha-data pic x(30).
    05 numeric-data     pic 9(20).
    05 some-more-numeric-data pic 9(20).
    05 filler                    pic x(22).

You can break the record down to each individual byte of the record if you
want but typically you have information taking more than one byte and you
are just telling the  the program by the use of the variable name what bytes
belong with what variable.

Don't get all bound up in the "comp" fields they are just a way of defining
a storage method for the data.  A record is not required to use comp fields
but as you get more experience with cobol you will find out that you want to
store data in the most efficient way you can so you save disk/tape space and
programs can do certain tasks faster when stored with comp fields.



The stuff dealing with 77 levels don't appear to function as part of the
record layout listed in the 01 level.

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:FTEJc.1591$4L7.319@newssvr33.news.prodigy.com...
> "Carol" <kgdg@helkusa.com> wrote in message
> news:JZCdnZ690pjbiWrd4p2dnA@comcast.com...
…[7 more quoted lines elided]…
> Um, if by "convert this file" you mean "convert the record layout" then
your
> X fields are alpha, your PIC 9 fields are numeric, usage immaterial...
> CREATE TABLE  tablename (co_no VARCHAR(3), set_seq_no INTEGER,
…[4 more quoted lines elided]…
> Or did you mean, convert some DATA currently residing in a file described
by
> this layout?
>
…[27 more quoted lines elided]…
> IEEE format; and several "base" conversion programs (BASIC language).
Sounds
> like that software would probably be exactly what you want.... except the
> part where you say, " What I can't do is spend any money on a one-off
tool."
>
> But if you change your mind and are interested in a package of BASIC
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T18:54:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VLSdnUGwEp_EumrdRVn-ig@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FTEJc.1591$4L7.319@newssvr33.news.prodigy.com>`

```
You are right.
I am not making myslef clear at all.
Still, the info you sent is helping me.

I have a job to convert these tapes form cobol to ascii text.
I have a program to do this, but as you know I have to script it with the
file layout.
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "Charles W. Cribbs II" <charlescribbs@earthlink.net>
- **Date:** 2004-07-16T01:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rdGJc.9373$sV2.2454@newsread2.news.atl.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FTEJc.1591$4L7.319@newssvr33.news.prodigy.com> <VLSdnUGwEp_EumrdRVn-ig@comcast.com>`

```
Well that will be pretty simple then.

Take that record layout and for the fields with comp in them just make your
text file show a pic 9(same length as what comp field specifies).


"Carol" <kgdg@helkusa.com> wrote in message
news:VLSdnUGwEp_EumrdRVn-ig@comcast.com...
> You are right.
> I am not making myslef clear at all.
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Layout Hell.

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-07-16T01:17:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<P0GJc.8950$OA6.6225@newssvr23.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```

77's always precede 01-99's. Other than that, I didn't really look
at the definition detail.


Gary




"Carol" <kgdg@helkusa.com> wrote in message
news:JZCdnZ690pjbiWrd4p2dnA@comcast.com...
> Hi,
> Could I have some help with this layout?
> I am new to the layout scene, but if I could see some real examples, I
might
> get it. Then again, I might club myself with a shovel.
> Thank you.
…[49 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-16T02:03:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0IGJc.4104$mL5.2263@newsread1.news.pas.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <P0GJc.8950$OA6.6225@newssvr23.news.prodigy.com>`

```
Huh ???

I think that MAY have been required by the '68 Standard - but not since.  Is
there a compiler still supported that requires 77 levels to be coded before
01-levels?
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2004-07-16T05:23:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PDJJc.8982$Dr.8865@newssvr23.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <P0GJc.8950$OA6.6225@newssvr23.news.prodigy.com> <0IGJc.4104$mL5.2263@newsread1.news.pas.earthlink.net>`

```

Perhaps not. I thought about that just as I was making that post.

But, I still was not aware that 77's & 01-99's could be mixed,
and further, why would someone want to? Frankly, I haven't
seen much use in 77's in some time anyway.

Thanks, for the update....

Gary




"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:0IGJc.4104$mL5.2263@newsread1.news.pas.earthlink.net...
> Huh ???
>
> I think that MAY have been required by the '68 Standard - but not since.
Is
> there a compiler still supported that requires 77 levels to be coded
before
> 01-levels?
>
…[76 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-17T16:07:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10fj59aes30p499@corp.supernews.com>`
- **In-Reply-To:** `<PDJJc.8982$Dr.8865@newssvr23.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <P0GJc.8950$OA6.6225@newssvr23.news.prodigy.com> <0IGJc.4104$mL5.2263@newsread1.news.pas.earthlink.net> <PDJJc.8982$Dr.8865@newssvr23.news.prodigy.com>`

```
The Family wrote:

> Perhaps not. I thought about that just as I was making that post.
> 
> But, I still was not aware that 77's & 01-99's could be mixed,

01-99?  Try 01-49, 66, 77, 88.  :)
```

#### ↳ Re: Layout Hell.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-15T21:28:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FfWdnajyuePaoGrdRVn-hw@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
Carol wrote:
> Hi,
> Could I have some help with this layout?
…[3 more quoted lines elided]…
> I just need to convert this file to Access or something normal.

No you don't. It's already more normal than anything to which you could
convert it.

> Do you have any thoughts?

I have placed the number of bytes each field uses (usually, beware of
compiler dependencies) in square brackets. If that's insufficient, come back
with more specific questions.

(P.S., "77" levels are not involved in the record. They may be ignored for
this purpose.)

> Thanks you.
>
…[11 more quoted lines elided]…
>            10 CTLGTOTAL-INVOICE-AM      PIC S9(11)V9(2) USAGE COMP-3.
[7]**
>            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3. [7]
>            10 CTLGTERMS-CD              PIC X(2). [2]
…[7 more quoted lines elided]…
>            10 CTLGSHIP-TY               PIC X(2). [2]

* = Binary Fullword, 4 bytes because of its size (>4 digits)
** = Packed Decimal (number-of-digits + 1) / 2. No other database system
uses Packed Decimal. You have your work cut out to convert to a "normal"
number.
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:11:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L5GdnQtPursa_mrdRVn_iw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com>`

```
I guess the progblem is that it does not work.
I have 20 tapes and 20 file layoiuts. Maybe this file layout does not go
with this tape?


"JerryMouse" <nospam@bisusa.com> wrote in message
news:FfWdnajyuePaoGrdRVn-hw@giganews.com...
> Carol wrote:
> > Hi,
…[12 more quoted lines elided]…
> compiler dependencies) in square brackets. If that's insufficient, come
back
> with more specific questions.
>
…[18 more quoted lines elided]…
> >            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3.
[7]
> >            10 CTLGTERMS-CD              PIC X(2). [2]
> >            10 CTLGCARRIER-CD            PIC X(10). [10]
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:11:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5mdnXlYUuYD_mrdRVn-hQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com>`

```
Thanks a lot that is neat.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:FfWdnajyuePaoGrdRVn-hw@giganews.com...
> Carol wrote:
> > Hi,
…[12 more quoted lines elided]…
> compiler dependencies) in square brackets. If that's insufficient, come
back
> with more specific questions.
>
…[18 more quoted lines elided]…
> >            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3.
[7]
> >            10 CTLGTERMS-CD              PIC X(2). [2]
> >            10 CTLGCARRIER-CD            PIC X(10). [10]
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:21:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lfednc4MK9dd-GrdRVn-vw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com>`

```
Jerry, is there some table out there that lists all possible COBOL fields
( PIC X(3),PIC S9(9) ) and the number of bytes they take up, so that I can
just copy and paste or even write a little script?
thanks






"JerryMouse" <nospam@bisusa.com> wrote in message
news:FfWdnajyuePaoGrdRVn-hw@giganews.com...
> Carol wrote:
> > Hi,
…[12 more quoted lines elided]…
> compiler dependencies) in square brackets. If that's insufficient, come
back
> with more specific questions.
>
…[18 more quoted lines elided]…
> >            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3.
[7]
> >            10 CTLGTERMS-CD              PIC X(2). [2]
> >            10 CTLGCARRIER-CD            PIC X(10). [10]
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-16T09:15:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IsKdnWvHOZOIfmrd4p2dnA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <Lfednc4MK9dd-GrdRVn-vw@comcast.com>`

```
Carol wrote:
> Jerry, is there some table out there that lists all possible COBOL
> fields ( PIC X(3),PIC S9(9) ) and the number of bytes they take up,
> so that I can just copy and paste or even write a little script?
> thanks

No.

It's terribly confusing for the neophyte. Several CHAPTERS are necessary in
a COBOL manual to go through all the permutations. For your purposes,
though, you may consider:

PIC ("Picture") X(nn) to be "nn" bytes long.

If the picture line ends in COMP-something, you have to be attuned to your
operating system and compiler. In general:

COMP 9(1) through 9(4) use two bytes (binary half-word)
COMP 9(5) through 9(9) use four bytes (binary full-word)

With each of these, you must be aware of whether your machine stores the
data as big-endian or little-endian.

COMP-3 is Packed Decimal. The last half-byte stores the sign and the
least-significant digit (usually). All other bytes store two digits each.
Viz:

123 = 12 3+
1234 = 01 23 4+
12345 = 12 34 5+
123.45 = 12 34 5+
0.12345 = 12 34 5+

So! Where's the decimal point stored? There is no decimal point stored in
COMP fields. The program just has to KNOW where the decimal point belongs.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T10:53:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hKGdnUmFB-RmmmXdRVn-uw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <Lfednc4MK9dd-GrdRVn-vw@comcast.com> <IsKdnWvHOZOIfmrd4p2dnA@giganews.com>`

```
good. thank you very much Mr. Mouse.



"JerryMouse" <nospam@bisusa.com> wrote in message
news:IsKdnWvHOZOIfmrd4p2dnA@giganews.com...
> Carol wrote:
> > Jerry, is there some table out there that lists all possible COBOL
…[6 more quoted lines elided]…
> It's terribly confusing for the neophyte. Several CHAPTERS are necessary
in
> a COBOL manual to go through all the permutations. For your purposes,
> though, you may consider:
…[25 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:46:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T8KdnQfCif1T9mrd4p2dnA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com>`

```
I add these up and I get 201.

My block length is 32600 for sure.
that divides by 200 * 163
but not 201

what do I do?




"JerryMouse" <nospam@bisusa.com> wrote in message
news:FfWdnajyuePaoGrdRVn-hw@giganews.com...
> Carol wrote:
> > Hi,
…[12 more quoted lines elided]…
> compiler dependencies) in square brackets. If that's insufficient, come
back
> with more specific questions.
>
…[18 more quoted lines elided]…
> >            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE COMP-3.
[7]
> >            10 CTLGTERMS-CD              PIC X(2). [2]
> >            10 CTLGCARRIER-CD            PIC X(10). [10]
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-16T10:58:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HxOJc.37329$eH1.17845939@newssvr28.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <T8KdnQfCif1T9mrd4p2dnA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote in message
news:T8KdnQfCif1T9mrd4p2dnA@comcast.com...
> I add these up and I get 201.
>
…[5 more quoted lines elided]…
>

Create a report showing size of all elementary and group items, with
documentation:
http://www.flexus.com/ftp/cobfd.zip
Be aware: the size of COMP[-n] fields may vary with operating system and/or
compiler directives!

Text/graphics tutorial on COBOL data:
http://www.flexus.com/ftp/cobdata.zip


Tips/techniques for converting COBOL-created data for use with other
software (link previously supplied):
http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm


That ain't enough? Consider outside help.
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-17T00:01:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40f86929.445252074@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <T8KdnQfCif1T9mrd4p2dnA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>I add these up and I get 201.
>
…[4 more quoted lines elided]…
>what do I do?

Length of the third field is 2, not 4, so the record length is 199. Look at the
data to see how long records are. It should be easy to spot CO-NO, which appears
to be a constant or at least the same for several records.

I used to process 1-10 requests per week for such conversions. I charged a flat
rate of $50 per, with possible discount to $25 if they could supply a copybook.
They almost never could. Instead they sent a text document that management
thought was usable. 


>"JerryMouse" <nospam@bisusa.com> wrote in message
>news:FfWdnajyuePaoGrdRVn-hw@giganews.com...
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T20:20:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o7idnWV4PcqYEGXdRVn-tw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <T8KdnQfCif1T9mrd4p2dnA@comcast.com> <40f86929.445252074@news.optonline.net>`

```
Thanks, yet 199 does not go into the block length 32600 evenly.

I thought that was a requirement.
Is that a problem?



"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40f86929.445252074@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[8 more quoted lines elided]…
> Length of the third field is 2, not 4, so the record length is 199. Look
at the
> data to see how long records are. It should be easy to spot CO-NO, which
appears
> to be a constant or at least the same for several records.
>
> I used to process 1-10 requests per week for such conversions. I charged a
flat
> rate of $50 per, with possible discount to $25 if they could supply a
copybook.
> They almost never could. Instead they sent a text document that management
> thought was usable.
…[22 more quoted lines elided]…
> >> (P.S., "77" levels are not involved in the record. They may be ignored
for
> >> this purpose.)
> >>
…[28 more quoted lines elided]…
> >> ** = Packed Decimal (number-of-digits + 1) / 2. No other database
system
> >> uses Packed Decimal. You have your work cut out to convert to a
"normal"
> >> number.
> >>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-17T03:44:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qg1Kc.5771$Qu5.4296@newsread2.news.pas.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <T8KdnQfCif1T9mrd4p2dnA@comcast.com> <40f86929.445252074@news.optonline.net> <o7idnWV4PcqYEGXdRVn-tw@comcast.com>`

```
IBM (and possibly other vendors) allow for SPANNED records - that span multiple
blocks. I *doubt* this is your case, but it at least represents a possibility.

The other is that the copy-book you have was used in the COBOL working-storage
and the data was MOVED to a file bugger - where records were larger, e.g.
working-storage was 199 - but the file defined a record of 200.  In that case
you should see some "filler" (hex-zeroes, spaces, or even JUNK) at the end of
each individual record.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T22:00:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DsCdnaVMHNbCOWXdRVn-hA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <T8KdnQfCif1T9mrd4p2dnA@comcast.com> <40f86929.445252074@news.optonline.net> <o7idnWV4PcqYEGXdRVn-tw@comcast.com> <qg1Kc.5771$Qu5.4296@newsread2.news.pas.earthlink.net>`

```
hmm ok thanks
!

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:qg1Kc.5771$Qu5.4296@newsread2.news.pas.earthlink.net...
> IBM (and possibly other vendors) allow for SPANNED records - that span
multiple
> blocks. I *doubt* this is your case, but it at least represents a
possibility.
>
> The other is that the copy-book you have was used in the COBOL
working-storage
> and the data was MOVED to a file bugger - where records were larger, e.g.
> working-storage was 199 - but the file defined a record of 200.  In that
case
> you should see some "filler" (hex-zeroes, spaces, or even JUNK) at the end
of
> each individual record.
>
…[24 more quoted lines elided]…
> > > Length of the third field is 2, not 4, so the record length is 199.
Look
> > at the
> > > data to see how long records are. It should be easy to spot CO-NO,
which
> > appears
> > > to be a constant or at least the same for several records.
> > >
> > > I used to process 1-10 requests per week for such conversions. I
charged a
> > flat
> > > rate of $50 per, with possible discount to $25 if they could supply a
> > copybook.
> > > They almost never could. Instead they sent a text document that
management
> > > thought was usable.
> > >
…[6 more quoted lines elided]…
> > > >> > I am new to the layout scene, but if I could see some real
examples,
> > > >> > I might get it. Then again, I might club myself with a shovel.
> > > >> > Thank you.
> > > >> > I just need to convert this file to Access or something normal.
> > > >>
> > > >> No you don't. It's already more normal than anything to which you
could
> > > >> convert it.
> > > >>
> > > >> > Do you have any thoughts?
> > > >>
> > > >> I have placed the number of bytes each field uses (usually, beware
of
> > > >> compiler dependencies) in square brackets. If that's insufficient,
come
> > > >back
> > > >> with more specific questions.
> > > >>
> > > >> (P.S., "77" levels are not involved in the record. They may be
ignored
> > for
> > > >> this purpose.)
…[5 more quoted lines elided]…
> > > >> >            10 CTLGCONTROL-SET-SEQ-NO    PIC S9(9) USAGE COMP.
[4]*
> > > >> >            10 CTLGINVOICE-SEQ-NO        PIC S9(4) USAGE COMP.
[4]*
> > > >> >            10 CTLGAP-CNTRL-ENTITY-CD    PIC X(4). [4]
> > > >> >            10 CTLGINVOICE-TYPE-CD       PIC X(2). [2]
…[5 more quoted lines elided]…
> > > >> >            10 CTLGTOTAL-INVOICE-AM      PIC S9(11)V9(2) USAGE
COMP-3.
> > > >> [7]**
> > > >> >            10 CTLGTOTAL-MERCH-AM        PIC S9(11)V9(2) USAGE
COMP-3.
> > > >[7]
> > > >> >            10 CTLGTERMS-CD              PIC X(2). [2]
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** B Hobbs <bdhobbs18@yahoo.com>
- **Date:** 2004-07-16T14:10:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com>`

```
In article <FfWdnajyuePaoGrdRVn-hw@giganews.com>,
 "JerryMouse" <nospam@bisusa.com> wrote:

> I have placed the number of bytes each field uses (usually, beware of
> compiler dependencies) in square brackets. If that's insufficient, come back
> with more specific questions.

May I suggest that one specify what hardware, operating system, compiler 
combination was used?

> >            10 CTLGOP-CO-NO              PIC X(3). [3]
> >            10 CTLGCONTROL-SET-SEQ-NO    PIC S9(9) USAGE COMP. [4]*
> >            10 CTLGINVOICE-SEQ-NO        PIC S9(4) USAGE COMP. [4]*

The last data item would be two bytes on DEC/Compaq/HP Alpha, VMS 7.2, 
Compaq COBOL 2.8.

http://h71000.www7.hp.com/doc/73final/6296/6296_profile_015.html#data_typ
es_unscaled_tab 

I agree with an earlier poster about developing a COBOL program using 
the specified record layout to read the data and then spit it out in a 
format the lesser program will find agreeable.  There still could be a 
problem using different compilers, or possibly different compiler 
versions, on the same hw/os.  Heck, the data and program he found could 
have been left over from a Honeywell 6000 and GCOS, which I vaguely 
recall as being a bit peculiar ... was it a 36 bit word?

A few blocks from the data tape should probably be dumped to hex or 
octal and analyzed to try to determine overall record size, fixed or 
variable length records, if there are multiple record types, and if the 
character set is ASCII, EBCDIC, or something else.  The tape headers and 
trailers may have a few clues also.

Hmmm, just how important is this data?  If its been rotting for a few 
years and just now its "value" has been discovered, how do they know it 
is the correct data?
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** docdwarf@panix.com
- **Date:** 2004-07-16T11:04:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd8qq9$2nn$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net>`

```
In article <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net>,
B Hobbs  <bdhobbs18@yahoo.com> wrote:

[snip]

>Hmmm, just how important is this data?  If its been rotting for a few 
>years and just now its "value" has been discovered, how do they know it 
>is the correct data?

For trend-analysis or other historical purposes it should be 'correct'; if 
one is looking to see how many widgets were used by the company during (x) 
period it should be just fine.

If one is looking, say, to put together a mailing-list of widget-users 
from (x) period then it might be a bit more dicey; at least in the USA 
folks have a tendency to change addresses rather frequently.

DD
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T10:57:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9idnSfgcbiTlGXdRVn-hA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net>`

```
The data is current.
This data came from another company.
I do not have access to the people at that company because of political
stuff.
All I have are 20 tapes and 20 file layouts and no experience.
Plus I am supposed to represent our company as being real smart .tee hee.


When you guys ask what compiler is used..

Do you mean what machine dumped the data?
Or what machine do I have that is reading the data.



"B Hobbs" <bdhobbs18@yahoo.com> wrote in message
news:bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net...
> In article <FfWdnajyuePaoGrdRVn-hw@giganews.com>,
>  "JerryMouse" <nospam@bisusa.com> wrote:
>
> > I have placed the number of bytes each field uses (usually, beware of
> > compiler dependencies) in square brackets. If that's insufficient, come
back
> > with more specific questions.
>
…[33 more quoted lines elided]…
> -- mailto:bdhobbs18@yahoo.com
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-16T18:25:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D4VJc.4629$mL5.1575@newsread1.news.pas.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net> <e9idnSfgcbiTlGXdRVn-hA@comcast.com>`

```
What we need to know is the "vendor", operating system, and specific compiler
(and possibly the compiler options) where the program was run that CREATED the
tape).

For example,
   With the Micro Focus compiler when run on an Intel (Windows) type
environment - if the IBM-COMP compiler  option is turned on
   Pic S9 COMP
will take 2 bytes
but if the same program were compiled with the NOIBM-COMP compiler option, then
it would take one byte.

Given you other note about the "political issues" in getting information about
the "creation" of the data, then this may be very difficult to get.

Similarly, if you have PIC XX data - and don't know if the program that created
the data was in an ASCII or EBCDIC environment, you may be able to figure out
how many bytes you need but you won't be able to make ANY sense of the data.

Using the tool at:
  http://www.flexus.com/ftp/cobfd.zip

mentioned elsewhere may be able to HELP you figure out what you have, but you
really REALLY need to know how (what compiler, what operating system, and what
compiler options/directives) were in effect WHEN THE DATA WAS FIRST created.
(Nothing to do with making a "tape copy" of existing data - but the actual
creation of the data)
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T20:00:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<maadnSkYz9DLFWXdRVn-jw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <FfWdnajyuePaoGrdRVn-hw@giganews.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net> <e9idnSfgcbiTlGXdRVn-hA@comcast.com> <D4VJc.4629$mL5.1575@newsread1.news.pas.earthlink.net>`

```
Thank you very much.  I will take a look. I really appreciate it.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:D4VJc.4629$mL5.1575@newsread1.news.pas.earthlink.net...
> What we need to know is the "vendor", operating system, and specific
compiler
> (and possibly the compiler options) where the program was run that CREATED
the
> tape).
>
…[5 more quoted lines elided]…
> but if the same program were compiled with the NOIBM-COMP compiler option,
then
> it would take one byte.
>
> Given you other note about the "political issues" in getting information
about
> the "creation" of the data, then this may be very difficult to get.
>
> Similarly, if you have PIC XX data - and don't know if the program that
created
> the data was in an ASCII or EBCDIC environment, you may be able to figure
out
> how many bytes you need but you won't be able to make ANY sense of the
data.
>
> Using the tool at:
>   http://www.flexus.com/ftp/cobfd.zip
>
> mentioned elsewhere may be able to HELP you figure out what you have, but
you
> really REALLY need to know how (what compiler, what operating system, and
what
> compiler options/directives) were in effect WHEN THE DATA WAS FIRST
created.
> (Nothing to do with making a "tape copy" of existing data - but the actual
> creation of the data)
…[11 more quoted lines elided]…
> > Plus I am supposed to represent our company as being real smart .tee
hee.
> >
> >
…[12 more quoted lines elided]…
> > > > I have placed the number of bytes each field uses (usually, beware
of
> > > > compiler dependencies) in square brackets. If that's insufficient,
come
> > back
> > > > with more specific questions.
> > >
> > > May I suggest that one specify what hardware, operating system,
compiler
> > > combination was used?
> > >
…[7 more quoted lines elided]…
> > >
http://h71000.www7.hp.com/doc/73final/6296/6296_profile_015.html#data_typ
> > > es_unscaled_tab
> > >
…[4 more quoted lines elided]…
> > > versions, on the same hw/os.  Heck, the data and program he found
could
> > > have been left over from a Honeywell 6000 and GCOS, which I vaguely
> > > recall as being a bit peculiar ... was it a 36 bit word?
…[3 more quoted lines elided]…
> > > variable length records, if there are multiple record types, and if
the
> > > character set is ASCII, EBCDIC, or something else.  The tape headers
and
> > > trailers may have a few clues also.
> > >
> > > Hmmm, just how important is this data?  If its been rotting for a few
> > > years and just now its "value" has been discovered, how do they know
it
> > > is the correct data?
> > >
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-19T21:01:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9DAk-RieflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net> <e9idnSfgcbiTlGXdRVn-hA@comcast.com>`

```
.    Am  16.07.04
schrieb  kgdg@helkusa.com (Carol)
    auf  /COMP/LANG/COBOL
     in  e9idnSfgcbiTlGXdRVn-hA@comcast.com
  ueber  Re: Layout Hell.

k> The data is current.
k> This data came from another company.
k> I do not have access to the people at that company because of
k> political stuff.

   Then you have to figure it out all by yourself -- and with the help  
of some friends.

k> All I have are 20 tapes and 20 file layouts and no experience.

   Having no experience is a challenge to acquire it.

   And this apparently goes well with this:

k> Plus I am supposed to represent our company as being real smart
k> .tee hee.

   Sure, having no experience at all is very smart, but only if you  
figure out what you don't know yet.


   I think under these circumstances your best way forward is to get a  
dump of a couple of records of each of those tapes, use the COBOL  
record descriptions you have, and apply your best guess as to what is  
what in the record layout.

   When the COBOL description says "PIC X(somenumber)" it is easy --  
you will typically have one byte per character, and depending on the  
source machine, you will have a choice of EBCDIC or ASCII.

   COMP-3 is nearly always packed-decimal, i.e. a numeric format where  
each digit of a 10-based-system (i.e. decimal) is represented by one  
half byte of a byte, and (normally) the last half byte does represent  
the sign of the number (if it is a hex "C". i.e. binary 1100, this  
means it is positive, and another value says the number is negative,  
but people with more current acquaintance with those big iron  
following the IBM byte architecture will know it better).

   Other COMP-USAGEs are probably some kind of machine-dependent  
representation -- and which n of those COMP-n does mean byte, 16-bit- 
entity, 32-bit-word, or more, is something you know better if you have  
some idea of the originating hardware and operating system, and also  
if it uses the regular bit sequence -- the most significant coming  
first -- or that peculiar Intel shuffeling of the more and less  
significant bytes or half-words...


k> When you guys ask what compiler is used..
k>
k> Do you mean what machine dumped the data?

  This is number 1 in the equation.

k> Or what machine do I have that is reading the data.

   Also, but you have already the main part when you can dump some  
records of those tapes using some tape analasys utility of the machine  
wehre you are supposed to get the data from those tapes.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

  "Nach meiner Ansicht besitzt die Presse _das_ _Recht_,
Schriftsteller, Politiker, Komï¿½dianten und andere ï¿½ffentliche
Charaktere zu _beleidigen_. Achtete ich [so einen Angriff gegen mich]
einer Notiz wert, so galt mir in solchen Fï¿½llen der Wahlspruch: ï¿½
corsaire, corsaire et demi [auf einen Schelmen anderthalben]."
                  - Karl Marx   17.11.1860  (Herr Vogt, Kapitel XI)
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-20T23:12:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ufWdnY63Q-3NZmDdRVn-uA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <bdhobbs18-DEB6D3.07101016072004@news2.west.earthlink.net> <e9idnSfgcbiTlGXdRVn-hA@comcast.com> <9DAk-RieflB@jpberlin-l.willms.jpberlin.de>`

```
thanks, my friend

"Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9DAk-RieflB@jpberlin-l.willms.jpberlin.de...
> .    Am  16.07.04
> schrieb  kgdg@helkusa.com (Carol)
…[73 more quoted lines elided]…
>                   - Karl Marx   17.11.1860  (Herr Vogt, Kapitel XI)
```

#### ↳ Re: Layout Hell

- **From:** "Mike" <NoSpam@StopSpam.org>
- **Date:** 2004-07-15T22:30:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C6mdnXT-R-dX1mrdRVn_vA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
> Could I have some help with this layout?
> I am new to the layout scene, but if I could see some real examples, I might
…[4 more quoted lines elided]…
> Thanks you.



What is it that makes this record layout abnormal as opposed to
something you don't know anything about?

Normal record layouts similar to this have been in very successful use
since Bill Gates was in diapers.  You can't do packed-decimal in
Access, you can't do redefines in Access, you can't even have group
levels in Access, you can't define a primary key as more than one
field in Access. That seems pretty abnormal and deficient to me.
```

##### ↳ ↳ Re: Layout Hell

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:16:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eJOdnYwjlbQl-Wrd4p2dnA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com>`

```


> What is it that makes this record layout abnormal as opposed to
> something you don't know anything about?

It doesn't work with this tape. Maybe the tape is wrong with this file
layout after all.


>you can't even have group levels in Access,
I think that is what joins are all about

>  you can't define a primary key as more than one field in Access.
Yes you can

>That seems pretty abnormal and deficient to me.
It is painful
```

##### ↳ ↳ Re: Layout Hell

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-17T16:04:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10fj52o8228h9ec@corp.supernews.com>`
- **In-Reply-To:** `<C6mdnXT-R-dX1mrdRVn_vA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com>`

```
Mike wrote:
> Normal record layouts similar to this have been in very successful use
> since Bill Gates was in diapers.  You can't do packed-decimal in
> Access, you can't do redefines in Access, you can't even have group
> levels in Access, you can't define a primary key as more than one
> field in Access.

I was with you 'til the last one - you can have multiple-field PK's in 
Access (I believe at least as far back as version "97")...
```

###### ↳ ↳ ↳ Re: Layout Hell

- **From:** "Mike" <NoMoreSpam@SpamStopper.Org>
- **Date:** 2004-07-17T21:44:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T66dneu6LeWIeWTdRVn_vA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com> <10fj52o8228h9ec@corp.supernews.com>`

```
> I was with you 'til the last one - you can have multiple-field PK's in
> Access (I believe at least as far back as version "97")...

I said that poorly. You can't have multiple primary key fields that you
treat as one field or one name - like a group level name is the key which
consists of many fields underneath it - at least as far I know. If you
have 3 columns F1, F2, F3 as primary keys you can't say F-All is the key?

Record Key is F-All.
05 F-All.
   10 f1 pic x.
   10 f2 pic x.
   10 f3 pic x.
```

###### ↳ ↳ ↳ Re: Layout Hell

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-17T22:31:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10fjrobkm2s7u8a@corp.supernews.com>`
- **In-Reply-To:** `<T66dneu6LeWIeWTdRVn_vA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com> <10fj52o8228h9ec@corp.supernews.com> <T66dneu6LeWIeWTdRVn_vA@giganews.com>`

```
Mike wrote:
>>I was with you 'til the last one - you can have multiple-field PK's in
>>Access (I believe at least as far back as version "97")...
…[11 more quoted lines elided]…
>    10 f3 pic x.

Right.  But, instead of assembling the pieces to an intermediary field 
and then doing a read based on 1 key, you'd just use those pieces in the 
select statement...

select * from f_table where (f1 = [value for f1] and f2 = [value for f2] 
and f3 = [values for f3])

...whereas, in the COBOL file equivalent, you'd say...

move [value for f1] to f1
move [value for f2] to f2
move [value for f3] to f3
read f-file record

.  You're still dealing with the pieces, just not on the actual 
retrieval command.

SQL is a different beast from an indexed file (of course, you seem to 
know enough about SQL to know that... ;> )  And, although Access does 
its best to hide stuff, you can still create indexes and primary keys to 
help speed things up (and maintain data integrity).  My biggest grip 
with Access is when you have more than one user hitting it - in my 
experience, it's locking mechanism doesn't seem to be designed well for 
multi-user applications.
```

##### ↳ ↳ Re: Layout Hell

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-17T21:31:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com>`

```
"Mike" <NoSpam@StopSpam.org> wrote in message
news:C6mdnXT-R-dX1mrdRVn_vA@giganews.com...
> Normal record layouts similar to this have been in very successful use
> since Bill Gates was in diapers....

And probably will be when he's back in diapers, too..

MCM
```

###### ↳ ↳ ↳ Re: Layout Hell

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-17T22:12:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H-CdnVnyFMI7ZWTdRVn-hA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com> <UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com>`

```
Then what are all these improvements that have been made?

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com...
> "Mike" <NoSpam@StopSpam.org> wrote in message
> news:C6mdnXT-R-dX1mrdRVn_vA@giganews.com...
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-07-18T18:01:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10fm0as4hhpns37@corp.supernews.com>`
- **In-Reply-To:** `<H-CdnVnyFMI7ZWTdRVn-hA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com> <UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com> <H-CdnVnyFMI7ZWTdRVn-hA@comcast.com>`

```
Carol wrote:

> "Michael Mattias" <michael.mattias@gte.net> wrote in message
> news:UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com...
…[9 more quoted lines elided]…
> Then what are all these improvements that have been made?

Who knows - but the point is that code similar to the record layout you 
were given has been around for a long time, and probably at least one of 
your bank / credit accounts utilize something similar.  And, I know that 
your tax return is processed using something like that (I work next to 
someone who's previous job was DBA for the IRS's Unisys mainframes in 
Memphis, TN).  :)
```

###### ↳ ↳ ↳ Re: Layout Hell

_(reply depth: 5)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-18T22:11:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cGdnWvhzoNK1GbdRVn-qw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <C6mdnXT-R-dX1mrdRVn_vA@giganews.com> <UUgKc.38365$eH1.18190015@newssvr28.news.prodigy.com> <H-CdnVnyFMI7ZWTdRVn-hA@comcast.com> <10fm0as4hhpns37@corp.supernews.com>`

```
cool thanks
```

#### ↳ Re: Layout Hell.

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-07-15T23:37:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40F75BA6.95D2BD15@mb.sympatico.ca>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
Carol wrote:
> 
> Hi,
…[8 more quoted lines elided]…
>

As I suggested to someone else - get a Cobol programmer to write a Q & D
program to blat out the data in comma-seperated field format  (which
will change the COMP fields to normal numbers on the fly) and then just
import it into Access.

Piece of cake.

PL
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:06:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_JOdnZ-vNKDB_2rdRVn-uw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40F75BA6.95D2BD15@mb.sympatico.ca>`

```
Thanks, but what is Q & D

"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
news:40F75BA6.95D2BD15@mb.sympatico.ca...
> Carol wrote:
> >
> > Hi,
> > Could I have some help with this layout?
> > I am new to the layout scene, but if I could see some real examples, I
might
> > get it. Then again, I might club myself with a shovel.
> > Thank you.
…[13 more quoted lines elided]…
> PL
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-16T09:22:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4OadnU6hlNMgeWrdRVn-sA@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40F75BA6.95D2BD15@mb.sympatico.ca> <_JOdnZ-vNKDB_2rdRVn-uw@comcast.com>`

```
Carol wrote:
> Thanks, but what is Q & D

Pick from list:

Quick and Dirty
Quadriceps and Deltoids
Quaker Oats and Decaf
Quintuplets and Diapers
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-16T11:13:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Upidnbs8d4A4kWXdRVn-gg@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40F75BA6.95D2BD15@mb.sympatico.ca> <_JOdnZ-vNKDB_2rdRVn-uw@comcast.com> <4OadnU6hlNMgeWrdRVn-sA@giganews.com>`

```

Quite a Dufus






"JerryMouse" <nospam@bisusa.com> wrote in message
news:4OadnU6hlNMgeWrdRVn-sA@giganews.com...
> Carol wrote:
> > Thanks, but what is Q & D
…[8 more quoted lines elided]…
>
```

#### ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-15T23:09:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jv6dnZCvNo2__mrd4p2dnA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
You guys are great.

Still, what do i do with this Filler field at the beginning?

Second what then, is the record length?

I see that all the 10s are repeated as 77s as PIC S9(4)
why?

You guys are great, man




>        77  FILLER      PIC X(16)  VALUE 'CTLG==(ANDERA)===='.
>        01  WWICTLG.
…[43 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-16T09:03:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1vadnQAQT_-DfWrdRVn-ig@giganews.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <Jv6dnZCvNo2__mrd4p2dnA@comcast.com>`

```
Carol wrote:
> You guys are great.
>
> Still, what do i do with this Filler field at the beginning?

Ignore it. This is a common technique to find the begining of program
storage in a memory dump.

>
> Second what then, is the record length?

This cannot be answered without knowing how YOUR compiler treats various
data definitions. For example, PIC S9(9) COMP could be several different
lengths (from 4 to 10 bytes) depending on the compiler and operating system.
"COMP" fields are implementor-defined.

>
> I see that all the 10s are repeated as 77s as PIC S9(4)
> why?

They are not repeated. They have different names. You'll have to ask the
original programmer why, but I suspect it's for temporary storage of the
previous record.

>
> You guys are great, man
…[47 more quoted lines elided]…
>>        77 POSBSHIP-TY              PIC S9(4) COMP.
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-16T12:06:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407161106.49e3c41@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <Jv6dnZCvNo2__mrd4p2dnA@comcast.com> <1vadnQAQT_-DfWrdRVn-ig@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> > I see that all the 10s are repeated as 77s as PIC S9(4)
> > why?
…[3 more quoted lines elided]…
> previous record.

All the following 77s are named POS.. and are 4 digit numbers.  They
are probably POSitions.  Either set to being the offsets in the
record, or screen I/O positions, or something.
```

#### ↳ Re: Layout Hell.

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-22T16:21:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40ffe8da.70647174@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>Could I have some help with this layout?
>I am new to the layout scene, but if I could see some real examples, I might
…[4 more quoted lines elided]…
>Thanks you.

See one solution in a new thread -- Demo: convert Cobol file to csv
```

##### ↳ ↳ Re: Layout Hell.

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-22T15:51:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jYGdnXoArP5yq53cRVn-hQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net>`

```
Thanks, man!

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40ffe8da.70647174@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
> >Could I have some help with this layout?
> >I am new to the layout scene, but if I could see some real examples, I
might
> >get it. Then again, I might club myself with a shovel.
> >Thank you.
…[4 more quoted lines elided]…
> See one solution in a new thread -- Demo: convert Cobol file to csv
```

##### ↳ ↳ Re: Layout Hell.

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-22T14:52:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407221352.2c2002c4@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 

> >Could I have some help with this layout?
> >I am new to the layout scene, but if I could see some real examples, I might
…[6 more quoted lines elided]…
> See one solution in a new thread -- Demo: convert Cobol file to csv

I think that you _completely_ miss the point Robert.
```

###### ↳ ↳ ↳ Re: Layout Hell.

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-22T23:35:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410042b5.93653409@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[10 more quoted lines elided]…
>I think that you _completely_ miss the point Robert.

The point was to convert Carol's file to a format that Access (or Excel) could
handle. 

I'm not into 'Zen wisdom' so just say what you think the point was. Hint: she
wasn't looking for an education in 'the idiosyncrasies of Cobol that only we
geniuses can understand'. She just wanted to get the damn file converted and
move on. I gave her and the numerous others who post similar queries a free tool
to get the job done. I spent four (billable) hours writing it. It worked the
third time. I love writing this type software.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-23T00:02:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net>`

```
Robert,
   In this thread, Carol stated,

"When you guys ask what compiler is used..

Do you mean what machine dumped the data?
Or what machine do I have that is reading the data."

This lead some of us to believe that Carol neither has, nor has access to a
COBOL compiler.

She also stated,

"I do not have access to the people at that company because of political
stuff.
All I have are 20 tapes and 20 file layouts and no experience.
Plus I am supposed to represent our company as being real smart .tee hee."

which makes it look as if anyone trying to get the original provider to do the
conversion, is not providing an adequate solution.

This is why I (and possibly others) didn't think that your "COBOL program to do
the conversion" solution - was a responsive solution.  However, the thread has
gone on long enough that you may have missed these "restrictions" on what
solution would be viable.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-23T11:55:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J07Mc.2722$5U2.1954@newssvr15.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net...
> This is why I (and possibly others) didn't think that your "COBOL program
to do
> the conversion" solution - was a responsive solution.  However, the thread
has
> gone on long enough that you may have missed these "restrictions" on what
> solution would be viable.

Threads in _this_ newsgroup which get so long they wander from the original
question and forget stated restrictions?

I'm shocked, shocked.

MCM
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T07:57:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdques$b5r$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net> <J07Mc.2722$5U2.1954@newssvr15.news.prodigy.com>`

```
In article <J07Mc.2722$5U2.1954@newssvr15.news.prodigy.com>,
Michael Mattias <michael.mattias@gte.net> wrote:
>"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
>news:rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net...
…[8 more quoted lines elided]…
>I'm shocked, shocked.

Your winnings, Sir?

DD
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T16:17:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41013968.156817958@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <rAYLc.10317$mL5.8164@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Robert,
>   In this thread, Carol stated,
…[7 more quoted lines elided]…
>COBOL compiler.

I acknowledged that, followed by suggestions of enlisting a Cobol programmer and
downloading a free compiler.

>She also stated,
>
…[6 more quoted lines elided]…
>conversion, is not providing an adequate solution.

You're right. I'd forgotten the part about "political stuff".

>This is why I (and possibly others) didn't think that your "COBOL program to do
>the conversion" solution - was a responsive solution.  However, the thread has
>gone on long enough that you may have missed these "restrictions" on what
>solution would be viable.

A Cobol solution is easy because of packed decimal. Outside the mainframe world,
few languages can handle that format.  It can be done with shifts or division by
256, but the code would be ugly and inappropriate to this Cobol newsgroup.

I used to bristle when people used the phrase 'Cobol file'. I'd say, 'Cobol
doesn't define unique data types, they are universal to all languages.' That
used to be true when mainframes ruled the land. In today's world of PCs and Unix
machines, Cobol is the last bastion of packed decimal.

The best solution would be an Excel plugin written in Cobol as a COM object.
That would be interesting. It would take (me) longer than four hours to write.


>"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
>news:410042b5.93653409@news.optonline.net...
…[17 more quoted lines elided]…
>> The point was to convert Carol's file to a format that Access (or Excel)
could
>> handle.
>>
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-07-23T01:04:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o2l0g01u9c46pdhg673kodrma62fiu5r0f@4ax.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net>`

```
On Thu, 22 Jul 2004 23:35:44 GMT, robert.deletethis@wagner.net (Robert
Wagner) wrote:

>riplin@Azonic.co.nz (Richard) wrote:
>
…[22 more quoted lines elided]…
>third time. I love writing this type software.
YOU DID miss the point.

She does not have the FD for the file, so your program is useless to
her unless she can find the missing info.
Even if she does have a FD, if it contains redefines she will still be
unable to figure out how to deal with them.

I have customers that on the same file have hundreds of different
record layouts. Having a FD that says 
01 tbl-record.
   05 tbl-key pic x(50).
   05 tbl-data pic x(2000).

does not help anyone. This type of information can be normally
retrieved by program rmpmapinx.cob that is supplied with the RM/COBOL
runtime/compiler. Other compilers have similar tools (e.g. Acucobol
has VUTIL).

So although your program may work very well on some situations, and
can also be a base for someone to build their own converters, it is
not A tool for every job, and certainly not for this one.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T16:17:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41013661.156043454@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <o2l0g01u9c46pdhg673kodrma62fiu5r0f@4ax.com>`

```
Frederico Fonseca <real-email-in-msg-spam@email.com> wrote:

>On Thu, 22 Jul 2004 23:35:44 GMT, robert.deletethis@wagner.net (Robert
>Wagner) wrote:
…[3 more quoted lines elided]…
>>>robert.deletethis@wagner.net (Robert Wagner) wrote 

>>>I think that you _completely_ miss the point Robert.
>>
…[6 more quoted lines elided]…
>>move on. I gave her and the numerous others who post similar queries a free
tool
>>to get the job done. I spent four (billable) hours writing it. It worked the
>>third time. I love writing this type software.
…[3 more quoted lines elided]…
>her unless she can find the missing info.

What information? When I write an FD, it says 'fd input-file.' Examples are in
the demo.

>Even if she does have a FD, if it contains redefines she will still be
>unable to figure out how to deal with them.

She posted a single copybook, which means all records have that format.

>I have customers that on the same file have hundreds of different
>record layouts. Having a FD that says 
…[11 more quoted lines elided]…
>not A tool for every job, and certainly not for this one.

Granted, there are files with complex record formats. I've written tools to
handle them. But in this case, which is typical of most, records have a single
format defined in the copybook. 

You are taking a simple problem and trying to make it complicated.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-23T00:32:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407222332.538d74c5@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> >I think that you _completely_ miss the point Robert.
> 
…[3 more quoted lines elided]…
> I'm not into 'Zen wisdom' 

That had been noticed.

> so just say what you think the point was. 

If she had a Cobol compiler and an FD that provably matched the data
_tapes_ then she wouldn't have the problem.

C >> I have 20 tapes and 20 file layoiuts. Maybe this file layout does
C >> not go with this tape?

C>> I have a job to convert these tapes form cobol to ascii text.
C>> I have a program to do this, but as you know I have to script it 
C>> with the file layout.

> Hint: she
> wasn't looking for an education in 'the idiosyncrasies of Cobol that only we
> geniuses can understand'. 

Yet you sent her something that required her to know things that 'only
we geniuses' could so something with, such as compile.  And BTW how
would Fujitsu v3 read a _tape_ ?

> She just wanted to get the damn file converted and
> move on. I gave her and the numerous others who post similar queries a free
> tool
> to get the job done. 

She already had a tool, what she didn't have was an FD that made
sense.

I'll repeat that bit, you probably missed it _again_:

C>> I have a program to do this, but as you know I have to script it 
C>> with the file layout.

Given that your 'solution' required a usable FD it doesn't make any
progress at all.  As I said you _completely_ missed the point, as you
seem to do so frequently.

> I spent four (billable) hours writing it. It worked the third time. I love
> writing this type software.

Yes and you grab every opportunity to try to show how you are one of
"we geniuses" when a few minutes of reading the actual problem domain
would have gone a lot further in doing that.

BTW, I thought the problem _might_ be that it is in EBCDIC on an ASCII
machine, or vice versa, and thus nonsense is coming out of her
converter program.  There is no evidence either way in this thread.
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 5)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-07-23T12:59:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410151FB.F86ACC2D@mb.sympatico.ca>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com>`

```
Richard wrote:
> 
 > writing this type software.
…[5 more quoted lines elided]…
>

IMHO there are several people in this NG that spend entirely too much
time trashing RW.  He may be right or wrong but he's entitled to his
opinion.  If you think he's wrong, say so and let it go. If you leave it
at that the controversy will necessarily stop.  You ought to know by now
that some things can't be settled once-and-for-all, especially when egos
come into play.  

So far as his program is concerned, I think it's overkill but at least
it is a CONCRETE suggestion as opposed to the volumes of speculation
that have appeared in response to "Carol's" original question.  Many of
the people that took time to explain the data representations did so out
of the best of motives but they missed the point, which was that she
doesn't care about the details, she just wants to convert the file.  And
the easiest way to do it is to write a "Quick & Dirty" program to create
a flat or CSV file to read into Access or whatever it si she needs.

Let it go!

PL
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 6)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T12:05:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F_6dnaHOFu7_zpzcRVn-rA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca>`

```
I'm still here and i can answer any questions for which i have an answer,
and for which there is a question.
Zen

"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
news:410151FB.F86ACC2D@mb.sympatico.ca...
> Richard wrote:
> >
…[26 more quoted lines elided]…
> PL
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T14:06:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdrk2g$ah3$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca>`

```
In article <410151FB.F86ACC2D@mb.sympatico.ca>,
Peter Lacey  <lacey@mb.sympatico.ca> wrote:

[snip]

>Many of
>the people that took time to explain the data representations did so out
…[3 more quoted lines elided]…
>a flat or CSV file to read into Access or whatever it si she needs.

Mr Lacey, I'm not sure I agree.  What was demonstrated was that a person 
with sufficient experience (in Mr Wagner's case a few decades and change) 
and the appropriate tools might generate a quick & dirty program to 
convert the files; until such time, however, as such a person is allowed 
access to the files the question of whether the generated program will 
actually *do* the job can be answered only conjecturally.

This is the problem that I saw... a person without the skills, without the 
experience and without the appropriate corporate resources ('I cannot talk 
to them for political reasons') was assigned a task.  This reminds me of 
those Old, Bad Movies where The Hero is given a similarly impossible 
task... and when he walks back into his boss' office after successful 
completion he is greeted with 'You've caused us a *great* deal of 
trouble... you were supposed to fail.'

Then again... perhaps I watch too many old, bad movies.

DD
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 7)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T12:39:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TcOdnRWD-sbFxpzcRVn-ow@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com>`

```
I will let you if my progress causes annonyances at my company.
I've had very similar experiences so far on this project.

1.  I need these 21 tapes converted as soon as possible.
2.  I should told you  two weeks ago that these were Expense Payable tapes
not Accounts Payable tapes.
3.  The copy books I gave you are for the wrong tapes. Sorry.
4.  These copy books are photocopies.  You'll have to type all the
information in. Some are 100 fields long (In computer gibberish).
5.  My employees are real disapointed in me.  The only way I can get back
their trust is if you get these tapes converted as fast as possible.
6.  Sorry, I didn't tell you I would be out for a week. Sorry you had to sit
idle while I was gone.
7.  The guy who did this job before you quit in disqust.
8.  This job and the company's future depends on you getting these tapes
out.
9.  I understand that you have no experience.
10.  Please work extra hard on this project.
11.  Let's think of a way we can give you a big raise.
12.   Let's wait 6 months to talk about a raise.
13. I forgot to tell you I will be on vacation next week.


<docdwarf@panix.com> wrote in message news:cdrk2g$ah3$1@panix5.panix.com...
> In article <410151FB.F86ACC2D@mb.sympatico.ca>,
> Peter Lacey  <lacey@mb.sympatico.ca> wrote:
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-07-23T19:21:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8zdMc.41246$eH1.19514232@newssvr28.news.prodigy.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com> <TcOdnRWD-sbFxpzcRVn-ow@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote in message
news:TcOdnRWD-sbFxpzcRVn-ow@comcast.com...
> 9.  I understand that you have no experience.

Um, WHO has no experience?

MCM
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 8)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-07-23T16:18:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iseMc.15641$Fj.581106@news20.bellglobal.com>`
- **In-Reply-To:** `<TcOdnRWD-sbFxpzcRVn-ow@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com> <TcOdnRWD-sbFxpzcRVn-ow@comcast.com>`

```
Carol wrote:
> I will let you if my progress causes annonyances at my company.
> I've had very similar experiences so far on this project.
…[20 more quoted lines elided]…
> 

  I think you should hand him the tapes back, telling him you 
accidentally erased them trying to convert them. Then blame it all on 
the experts in the NG, and go out and get drunk.  At least that way, 
some other poor bugger will be off the hook ...

Donald
(hell, it's friday)
;<)
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-23T21:34:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdsear$hpd$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com> <TcOdnRWD-sbFxpzcRVn-ow@comcast.com>`

```
In article <TcOdnRWD-sbFxpzcRVn-ow@comcast.com>,
Carol <kgdg@helkusa.com> wrote:
>I will let you if my progress causes annonyances at my company.

By all means, do!

>I've had very similar experiences so far on this project.

There are at least 21 standard responses to each of these.

>
>1.  I need these 21 tapes converted as soon as possible.

A lack of planning and foresight on your part does not constitute an 
emergency on my part.

>2.  I should told you  two weeks ago that these were Expense Payable tapes
>not Accounts Payable tapes.

When you can go back two weeks ago and do that I'll keep to the 
project-schedule we agreed to then; until you can do that the last two 
weeks are wasted work and need to be added to the deadline.

>3.  The copy books I gave you are for the wrong tapes. Sorry.

All work I have done based on those copybooks is wasted.  Add that time on 
to the deadline.

>4.  These copy books are photocopies.  You'll have to type all the
>information in. Some are 100 fields long (In computer gibberish).

It takes me (n) hours to type in each copybook.  This will add 20n hours 
to the project.

>5.  My employees are real disapointed in me.  The only way I can get back
>their trust is if you get these tapes converted as fast as possible.

How much of your salary is earned based on trust?  Once I start earning 
that I'll start doing the work associated with it.

>6.  Sorry, I didn't tell you I would be out for a week. Sorry you had to sit
>idle while I was gone.

Add that week on to the project's deadline with sorrow, then.

>7.  The guy who did this job before you quit in disqust.

Did he say where he went for a job afterwards?

>8.  This job and the company's future depends on you getting these tapes
>out.

If the company will fail without these tapes then let's go to a lawyer, 
right now, and draft up an agreement for me to own, as a transferrable 
asset, x% of the company; if I fail then I get nothing, if I succeed I 
get a piece of what I have saved.

>9.  I understand that you have no experience.

When someone 'understands' something they usually do not need to have it 
repeated to them constantly.

>10.  Please work extra hard on this project.

In whose dictionary is 'work extra hard' defined as 'accomplish the 
impossible'?

>11.  Let's think of a way we can give you a big raise.

I know of a way; we go to the person who cuts my paychecks and say 'Change 
the decimal-point to right over *here*'; if that person doesn't do it then 
it is time to fire them.

>12.   Let's wait 6 months to talk about a raise.

Let's add that time on to the project deadline.

>13. I forgot to tell you I will be on vacation next week.

Good... make sure you add that time onto the deadline before you go.

DD

><docdwarf@panix.com> wrote in message news:cdrk2g$ah3$1@panix5.panix.com...
>> In article <410151FB.F86ACC2D@mb.sympatico.ca>,
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 9)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T00:39:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2pmdnRmvEtKJmZ_cRVn-gg@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com> <TcOdnRWD-sbFxpzcRVn-ow@comcast.com> <cdsear$hpd$1@panix5.panix.com>`

```
Good DD!

<docdwarf@panix.com> wrote in message news:cdsear$hpd$1@panix5.panix.com...
> In article <TcOdnRWD-sbFxpzcRVn-ow@comcast.com>,
> Carol <kgdg@helkusa.com> wrote:
…[14 more quoted lines elided]…
> >2.  I should told you  two weeks ago that these were Expense Payable
tapes
> >not Accounts Payable tapes.
>
…[21 more quoted lines elided]…
> >6.  Sorry, I didn't tell you I would be out for a week. Sorry you had to
sit
> >idle while I was gone.
>
…[40 more quoted lines elided]…
> ><docdwarf@panix.com> wrote in message
news:cdrk2g$ah3$1@panix5.panix.com...
> >> In article <410151FB.F86ACC2D@mb.sympatico.ca>,
> >> Peter Lacey  <lacey@mb.sympatico.ca> wrote:
…[4 more quoted lines elided]…
> >> >the people that took time to explain the data representations did so
out
> >> >of the best of motives but they missed the point, which was that she
> >> >doesn't care about the details, she just wants to convert the file.
And
> >> >the easiest way to do it is to write a "Quick & Dirty" program to
create
> >> >a flat or CSV file to read into Access or whatever it si she needs.
> >>
> >> Mr Lacey, I'm not sure I agree.  What was demonstrated was that a
person
> >> with sufficient experience (in Mr Wagner's case a few decades and
change)
> >> and the appropriate tools might generate a quick & dirty program to
> >> convert the files; until such time, however, as such a person is
allowed
> >> access to the files the question of whether the generated program will
> >> actually *do* the job can be answered only conjecturally.
> >>
> >> This is the problem that I saw... a person without the skills, without
the
> >> experience and without the appropriate corporate resources ('I cannot
talk
> >> to them for political reasons') was assigned a task.  This reminds me
of
> >> those Old, Bad Movies where The Hero is given a similarly impossible
> >> task... and when he walks back into his boss' office after successful
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-24T09:48:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdtpam$j33$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <TcOdnRWD-sbFxpzcRVn-ow@comcast.com> <cdsear$hpd$1@panix5.panix.com> <2pmdnRmvEtKJmZ_cRVn-gg@comcast.com>`

```
In article <2pmdnRmvEtKJmZ_cRVn-gg@comcast.com>,
Carol <kgdg@helkusa.com> wrote:
>Good DD!

Shucks, t'weren't nothin'... at times one lives through a bit and learns a 
bit, that is all.

DD
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 7)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-07-24T11:11:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41028A19.FA1EAAB0@mb.sympatico.ca>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
>>a flat or CSV file to read into Access or whatever it si she needs.
> 
…[5 more quoted lines elided]…
> actually *do* the job can be answered only conjecturally.

A few decades???  All you need is an input fd using the copybook for
field defs, an output fd with the same fields but just pic 9() instead
of comp etc., and processing to open the files, read the records, move
all the fields from input to output, and write.  Any rookie could
program that.  It is correct that unless the copybook matches one of the
tapes the program will bomb, but on the information so far presented we
can't be more specific.
> 

> This is the problem that I saw... a person without the skills, without the
> experience and without the appropriate corporate resources ('I cannot talk
…[5 more quoted lines elided]…
> 


  You're probably right about the assignment.  Carol is in an uneviable
position.  

> Then again... perhaps I watch too many old, bad movies.
> 
> DD

Hee hee.  Have you ever seen "The Blob" with Steve McQueen?  An exemplar
of old, bad movies, I'd say.

PL
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 8)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-24T19:30:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9DVRl0l9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <cdrk2g$ah3$1@panix5.panix.com> <41028A19.FA1EAAB0@mb.sympatico.ca>`

```
.    Am  24.07.04
schrieb  lacey@mb.sympatico.ca (Peter Lacey)
    auf  /COMP/LANG/COBOL
     in  41028A19.FA1EAAB0@mb.sympatico.ca
  ueber  Re: Layout Hell.: leave it

PL> A few decades???  All you need is an input fd using the copybook for
PL> field defs, an output fd with the same fields but just pic 9()
PL> instead of comp etc.,

   No, the PIC 9() are OK, just COPY the copybook using
     REPLACING
         == COMP ==   BY == DISPLAY ==
         == COMP-1 == BY == DISPLAY ==
         == COMP-2 == BY == DISPLAY ==
         == COMP-3 == BY == DISPLAY ==
         == COMP-4 == BY == DISPLAY ==


   for the output file, and you are set.

PL> and processing to open the files, read the
PL> records, move all the fields from input to output,

   use a MOVE CORRESPONDING which is just one statement, and which is  
OK without mentioning the names of the individual fields

PL> and write.

   So this is one program template, identical for all 20 tapes

PL> Any rookie could

   sure. When the rookie has access to the machine and compiler which  
produced the originating tapes. But that is unfortunately not the  
case.



Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Es sind nicht die Generï¿½le und Kï¿½nige, die die Geschichte machen,
sondern die breiten Massen des Volkes"                - Nelson Mandela
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 9)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-25T00:26:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oNydnTPpC_IKz57cRVn-iQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <cdrk2g$ah3$1@panix5.panix.com> <41028A19.FA1EAAB0@mb.sympatico.ca> <9DVRl0l9flB@jpberlin-l.willms.jpberlin.de>`

```
I have 20 tapes which are all different data!
The 20 tapes are not just one big table.

I have 20 different stinking tables@!!!!!


"Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9DVRl0l9flB@jpberlin-l.willms.jpberlin.de...
> .    Am  24.07.04
> schrieb  lacey@mb.sympatico.ca (Peter Lacey)
…[41 more quoted lines elided]…
> sondern die breiten Massen des Volkes"                - Nelson Mandela
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 10)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-25T11:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9DZUMn$uflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DVRl0l9flB@jpberlin-l.willms.jpberlin.de> <oNydnTPpC_IKz57cRVn-iQ@comcast.com>`

```
.     Am  25.07.04
 schrieb  kgdg@helkusa.com (Carol)
     bei  /COMP/LANG/COBOL
      in  oNydnTPpC_IKz57cRVn-iQ@comcast.com
   ueber  Re: Layout Hell.: leave it

k> I have 20 tapes which are all different data!
k> The 20 tapes are not just one big table.


   I know, I know.

   Robert Wagner has shown you how to handle your problem using the  
NovaStor utilities NovaXchange "Tape Inspector" for this tape drive in  
his message no 4102600c.1996735@news.optonline.net of 24.07.2004,  
which you have read and answered. That is your way to go.

   My contribution was to show that it _could_ be easy in COBOL _if_  
you would have access to the original machine or machine type and the  
COBOL compiler being used there, which is not the case, as we all know  
now. It is more intended to those old COBOL hacks lurking here.

  What I said in my contribution is that the actual COBOL program to  
do these conversions would be the same for all 20 different file  
layouts, and would differ only in the COPY element describing the  
files record layout; everything else in that program would not need to  
be altered, except maybe the file description in the ENVIRONMENT  
DIVISION and the DATA DIVISION, FILE SECTION (the FD entry, FD being  
the abbreviation for File Description).

  One would COPY the original COPY-book unchanged for the input file,  
and with the REPLACING clause for the output file; one could produce  
20 identical copies of that utility program, just by changing the name  
of the COPY element.


Yours
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Das Volk, das ein anderes Volk unterjocht, schmiedet seine eigenen
Ketten."                         - Karl Marx           (1. Januar 1870)
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 11)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-25T17:34:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9DZW$M2eflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <oNydnTPpC_IKz57cRVn-iQ@comcast.com> <9DZUMn$uflB@jpberlin-l.willms.jpberlin.de>`

```
.    Am  25.07.04
schrieb  L.Willms@JPBERLIN.de (Lueko Willms)
    auf  /COMP/LANG/COBOL
     in  9DZUMn$uflB@jpberlin-l.willms.jpberlin.de
  ueber  Re: Layout Hell.: leave it

LW>    My contribution was to show that it _could_ be easy in COBOL _if_
LW> you would have access to the original machine or machine type and the
LW> COBOL compiler being used there, which is not the case, as we all
LW> know now. It is more intended to those old COBOL hacks lurking here.
LW>
LW>   What I said in my contribution is that the actual COBOL program to
LW> do these conversions would be the same for all 20 different file
LW> layouts, and would differ only in the COPY element describing the
LW> files record layout; everything else in that program would not need
LW> to be altered, except maybe the file description in the ENVIRONMENT
LW> DIVISION and the DATA DIVISION, FILE SECTION (the FD entry, FD being
LW> the abbreviation for File Description).
LW>
LW>   One would COPY the original COPY-book unchanged for the input file,
LW> and with the REPLACING clause for the output file; one could produce
LW> 20 identical copies of that utility program, just by changing the
LW> name of the COPY element.

   The program could look like this:


--------- schnipp -----------------------------------------

        IDENTIFICATION DIVISION.
        PROGRAM-ID.
           COPYDEMO.
        ENVIRONMENT DIVISION.
        INPUT-OUTPUT SECTION.
        FILE-CONTROL.
           SELECT INFILE
               ASSIGN TO "INFILE.DAT"
               FILE STATUS IS FILE-STATUS-INPUT
               .
           SELECT OUTFILE
               ASSIGN TO "OUTFILE.DAT"
               FILE STATUS IS FILE-STATUS-OUTPUT
               .

        DATA DIVISION.
        FILE SECTION.
        FD  INFILE
                .
        01  INRECORD
            .
        COPY RECDES01
               REPLACING
                 == 01 == BY ==     02 ==
            .

        FD  OUTFILE
                .
        01  OUTRECORD
            .
        COPY RECDES01
              REPLACING
                == 01 == BY ==     02 ==
                == COMP   == BY == DISPLAY ==
                == COMP-1 == BY == DISPLAY ==
                == COMP-2 == BY == DISPLAY ==
                == COMP-3 == BY == DISPLAY ==
                == COMP-4 == BY == DISPLAY ==
                == COMP-5 == BY == DISPLAY ==
            .

        WORKING-STORAGE SECTION.
        01  FILE-STATUS-INPUT.
            88  FILE-OK         VALUE '00'.
            02  FILLER          PIC 9.
                88  FILE-AT-END    VALUE 1.
            02  FILLER          PIC 9.
        01  FILE-STATUS-OUTPUT.
            88  FILE-OK         VALUE '00'.
            02  FILLER          PIC 9.
                88  FILE-AT-END    VALUE 1.
            02  FILLER          PIC 9.


        PROCEDURE DIVISION.
        MY-MAIN SECTION.
        ANFANG.
           OPEN INPUT INFILE
           OPEN OUTPUT OUTFILE
           READ INFILE
           PERFORM
               WITH TEST BEFORE
               UNTIL NOT (FILE-OK IN FILE-STATUS-INPUT)
             MOVE CORRESPONDING INRECORD TO OUTRECORD
             WRITE OUTRECORD
             READ INFILE
           END-PERFORM
           .
        ENDE.
           STOP RUN.



------------------ schnapp --------------------------------




MfG,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Ohne Pressefreiheit, Vereins- und Versammlungsrecht ist keine
Arbeiterbewegung mï¿½glich"        - Friedrich Engels      (Februar 1865)
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 12)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-26T15:37:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Dcb70q9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DZUMn$uflB@jpberlin-l.willms.jpberlin.de> <9DZW$M2eflB@jpberlin-l.willms.jpberlin.de>`

```
.    Am  25.07.04
schrieb  L.Willms@JPBERLIN.de (Lueko Willms)
    auf  /COMP/LANG/COBOL
     in  9DZW$M2eflB@jpberlin-l.willms.jpberlin.de
  ueber  Re: Layout Hell.: leave it

LW>>   What I said in my contribution is that the actual COBOL program to
LW>> do these conversions would be the same for all 20 different file
LW>> layouts, and would differ only in the COPY element describing the
LW>> files record layout; everything else in that program would not need
LW>> to be altered, except maybe the file description in the ENVIRONMENT
LW>> DIVISION and the DATA DIVISION, FILE SECTION (the FD entry, FD being
LW>> the abbreviation for File Description).
LW>>
LW>>   One would COPY the original COPY-book unchanged for the input
LW>> file, and with the REPLACING clause for the output file; one
LW>> could produce 20 identical copies of that utility program, just
LW>> by changing the name of the COPY element.


   here comes an enhanced version of that program which produces the  
output file as a CSV-file, actually by prefixing each field with a  
semikolon ";".  Some explanations are added in the text.

   Both versions of the program were compiled and verified with  
Fujitsu's COBOL V.3, but not tested in practice for lack of real test  
data.


--------- schnipp -----------------------------------------

000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID.
000030     COPYCSV.
000040 ENVIRONMENT DIVISION.
000050 INPUT-OUTPUT SECTION.
000060 FILE-CONTROL.
000070     SELECT INFILE
000080         ASSIGN TO "INFILE.DAT"
000090         FILE STATUS IS FILE-STATUS-INPUT
000100         .
000110     SELECT OUTFILE
000120         ASSIGN TO "OUTFILE.DAT"
000130         FILE STATUS IS FILE-STATUS-OUTPUT
000140         .
000150
000160 DATA DIVISION.
000170 FILE SECTION.
000180 FD  INFILE
000190          .
000200 01  INRECORD
000210      .
000220 COPY RECDES01
000230         REPLACING
000240           == 01 == BY ==     02 ==
000250      .
000251* The Recorddescription is being INCLUDEd in toe program here
000252* with REPLACING the level number from 01 to 02
000253* so that one can use a standard record name independently
000254* of the name given in the original record description.
000255* Just change the name of the COPY element here and for all the other
000256* record descriptions and leave the rest of the program unchanged.
000257*
000260
000270 FD  OUTFILE
000280          .
000290 01  OUTRECORD
000300      .
000310 COPY RECDES01
000320        REPLACING
000330          == 01 == BY ==     02 ==
000340          == COMP   == BY == DISPLAY ==
000350          == COMP-1 == BY == DISPLAY ==
000360          == COMP-2 == BY == DISPLAY ==
000370          == COMP-3 == BY == DISPLAY ==
000380          == COMP-4 == BY == DISPLAY ==
000390          == COMP-5 == BY == DISPLAY ==
000400          == . == BY == .
000410          10 FILLER  PIC X .
000420          ==
000430      .
000431* For the output, all USAGE COMP-n are being replaced by DISPLAY,
000432* so that this record is text only and can be read in in any kind of program
000433* before each elementary item (they happen to be written with level number 10)
000434* a one character field is being placed which will take up a semikolon: ";"
000440
000450 WORKING-STORAGE SECTION.
000460
000470 01  EDITRECORD
000480      .
000490 COPY RECDES01
000500        REPLACING
000510          == 01 == BY ==     02 ==
000520          == COMP   == BY == DISPLAY ==
000530          == COMP-1 == BY == DISPLAY ==
000540          == COMP-2 == BY == DISPLAY ==
000550          == COMP-3 == BY == DISPLAY ==
000560          == COMP-4 == BY == DISPLAY ==
000570          == COMP-5 == BY == DISPLAY ==
000580          == .
000590          10
000600          == BY == .
000610          10 FILLER  PIC X VALUE ";".
000620          10 ==
000630      .
000640* This is the same record descriptions, but the one character field
000641* is defined as with predefined value of ";"
000650
000660
000670 01  FILE-STATUS-INPUT.
000680      88  FILE-OK         VALUE '00'.
000690      02  FILLER          PIC 9.
000700          88  FILE-AT-END    VALUE 1.
000710      02  FILLER          PIC 9.
000720
000730 01  FILE-STATUS-OUTPUT.
000740      88  FILE-OK         VALUE '00'.
000750      02  FILLER          PIC 9.
000760          88  FILE-AT-END    VALUE 1.
000770      02  FILLER          PIC 9.
000780
000790
000800 PROCEDURE DIVISION.
000810 MY-MAIN SECTION.
000820 ANFANG.
000830     OPEN INPUT INFILE
000840     OPEN OUTPUT OUTFILE
000850     READ INFILE
000860     PERFORM
000870         WITH TEST BEFORE
000880         UNTIL NOT (FILE-OK IN FILE-STATUS-INPUT)
000890       MOVE CORRESPONDING INRECORD TO EDITRECORD
000900       WRITE OUTRECORD FROM EDITRECORD
000910       READ INFILE
000920     END-PERFORM
000930     CLOSE INFILE
000940     CLOSE OUTFILE
000950     .
000960 ENDE.
000970     STOP RUN.


------------------ schnapp --------------------------------


   I have also added the two CLOSE statements which I had forgotten in  
the first version.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Es sind nicht die Generï¿½le und Kï¿½nige, die die Geschichte machen,
sondern die breiten Massen des Volkes"                - Nelson Mandela
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 13)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-26T16:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9DccbwE9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DZW$M2eflB@jpberlin-l.willms.jpberlin.de> <9Dcb70q9flB@jpberlin-l.willms.jpberlin.de>`

```
.    Am  26.07.04
schrieb  L.Willms@JPBERLIN.de (Lueko Willms)
    auf  /COMP/LANG/COBOL
     in  9Dcb70q9flB@jpberlin-l.willms.jpberlin.de
  ueber  Re: Layout Hell.: leave it


   oops, something went wrong here:

LW> 000290 01  OUTRECORD
LW> 000300      .
LW> 000310 COPY RECDES01
LW> 000320        REPLACING
LW> 000330          == 01 == BY ==     02 ==
LW> 000340          == COMP   == BY == DISPLAY ==
LW> 000350          == COMP-1 == BY == DISPLAY ==
LW> 000360          == COMP-2 == BY == DISPLAY ==
LW> 000370          == COMP-3 == BY == DISPLAY ==
LW> 000380          == COMP-4 == BY == DISPLAY ==
LW> 000390          == COMP-5 == BY == DISPLAY ==
LW> 000400          == . == BY == .
LW> 000410          10 FILLER  PIC X .
LW> 000420          ==
LW> 000430      .

    this last clause should be the same as in the Working Storage  
Section, with the exception of the VALUE clause:


LW> 000500        REPLACING

LW> 000580          == .
LW> 000590          10
LW> 000600          == BY == .
LW> 000610          10 FILLER  PIC X VALUE ";".
LW> 000620          10 ==
LW> 000630      .

    The effect of the different REPLACING clause in the OUTRECORD is  
just that one additional character is being added at the end to the  
record, which would remain blanc or undefined.



Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Die Arbeit in weiï¿½er Haut kann sich nicht dort emanzipieren, wo sie
in schwarzer Haut gebrandmarkt wird."     - Karl Marx     12.11.1866
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 14)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-26T22:23:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410583cd.207788887@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DZW$M2eflB@jpberlin-l.willms.jpberlin.de> <9Dcb70q9flB@jpberlin-l.willms.jpberlin.de> <9DccbwE9flB@jpberlin-l.willms.jpberlin.de>`

```
l.willms@jpberlin.de (Lueko Willms) wrote:

>.    Am  26.07.04
>schrieb  L.Willms@JPBERLIN.de (Lueko Willms)
…[24 more quoted lines elided]…
>Section, with the exception of the VALUE clause:

1.  There will be an extra delimiter before the first field. The fix is 'inspect
editrecord replacing first '(delimiter)' by space. If you want to be fancy, do
the same for the trailing delimiter via REVERSE. Alternatively, redefine
editrecord to eliminate the first byte.

2.  Delimiters in the data should be filtered out, not possible in this case, or
delimiter should be Tab, which will not appear in data.

3.  Numeric fields need '.' in place of 'v' and '-' in place of 's9'. Doing so
seems impossible with this model.

4.  On a PC, the output should be LINE SEQUENTIAL. This makes COPY under output
FD superfluous. Make it x(2000).




>
>
…[20 more quoted lines elided]…
>in schwarzer Haut gebrandmarkt wird."     - Karl Marx     12.11.1866
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 15)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-27T11:37:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DccbwE9flB@jpberlin-l.willms.jpberlin.de> <410583cd.207788887@news.optonline.net>`

```
.    Am  26.07.04
schrieb  robert.deletethis@wagner.net (Robert Wagner)
    auf  /COMP/LANG/COBOL
     in  410583cd.207788887@news.optonline.net
  ueber  Re: Layout Hell.: leave it


   Thanks for your remarks regarding my Quick-and-dirty little  
program.

RW>
RW> 1.  There will be an extra delimiter before the first field.

   Right, and I noted that either in my message or in the comments in  
the program

RW> The fix is 'inspect editrecord replacing first '(delimiter)' by
RW> space.

   Better is reference modification, like this:

   MOVE SPACE TO EDITRECORD(1:1)

RW> If you want to be fancy, do the same for the trailing
RW> delimiter via REVERSE.

   There is no trailing delimiter.

RW> Alternatively, redefine editrecord to eliminate the first byte.

   For this I would have to know the record, but the main idea behind  
this program is that it should work even _without_ that knowledge.

RW> 2.  Delimiters in the data should be filtered out, not possible in
RW> this case, or delimiter should be Tab, which will not appear in data.

   OK. I define TAB as SYMBOLIC CHARACTER in the SPECIAL-NAMES  
paragraph and use TAB instead of ";".


RW>
RW> 3.  Numeric fields need '.' in place of 'v' and '-' in place of 's9'.
RW> Doing so seems impossible with this model.

   The latter can be solved by a clause on the 01 record level:

   SIGN IS LEADING SEPARATE CHARACTER

   I thought about the decimal separator, and concluded that the  
application importing the data would have to multiply all values of  
that filed by 100 ... one could try a REPLACING ==V9== BY ==.9==, but  
that could also affect the data name of an item in the record.

   I tried it, but I got syntax errors on compilation.


RW> 4.  On a PC, the output should be LINE SEQUENTIAL. This makes COPY
RW> under output FD superfluous. Make it x(2000).

   Well, I have no practical experience with COBOL on PCs, and  
actually the last time I programmed COBOL for production programs is 9  
years ago...

   So, LINE SEQUENTIAL induces the system to add a CR/LF to the end of  
the record, right?


   Here is the changed program:


--------- schnipp -----------------------------------------

000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID.
000030     COPYCSV.
000031 AUTHOR.
000032     Lueko Willms, http://www.willms-edv.de
000033     .
000034 DATE-WRITTEN.
000035     July 2004
000036     .
000040 ENVIRONMENT DIVISION.
000041 CONFIGURATION SECTION.
000042 SPECIAL-NAMES.
000043     ALPHABET ASCII IS STANDARD-1
000044     SYMBOLIC CHARACTERS TAB IS 9 IN ASCII
000045     .
000050 INPUT-OUTPUT SECTION.
000060 FILE-CONTROL.
000070     SELECT INFILE
000080         ASSIGN TO "INFILE.DAT"
000090         FILE STATUS IS FILE-STATUS-INPUT
000100         .
000110     SELECT OUTFILE
000120         ASSIGN TO "OUTFILE.TAB"
000121         ORGANIZATION IS LINE SEQUENTIAL
000130         FILE STATUS IS FILE-STATUS-OUTPUT
000140         .
000150
000160 DATA DIVISION.
000170 FILE SECTION.
000180 FD  INFILE
000190          .
000200 01  INRECORD
000210      .
000220 COPY RECDES01
000230         REPLACING
000240           == 01 == BY ==     02 ==
000250      .
000251* The Record description is being INCLUDEd in the program here
000252* with REPLACING the level number from 01 to 02
000253* so that one can use a standard record name independently
000254* of the name given in the original record description.
000255* Just change the name of the COPY element here and for all the other
000256* record descriptions and leave the rest of the program unchanged.
000257*
000260
000270 FD  OUTFILE
000280     RECORD IS VARYING IN SIZE
000281          .
000290 01  OUTRECORD  SIGN IS LEADING SEPARATE
000300      .
000310 COPY RECDES01
000320        REPLACING
000330          == 01 == BY ==     02 ==
000340          == COMP   == BY == DISPLAY ==
000350          == COMP-1 == BY == DISPLAY ==
000360          == COMP-2 == BY == DISPLAY ==
000370          == COMP-3 == BY == DISPLAY ==
000380          == COMP-4 == BY == DISPLAY ==
000390          == COMP-5 == BY == DISPLAY ==
000430          == .
000431          10
000432          == BY == .
000433          10 FILLER  PIC X .
000434          10 ==
000439      .
000440* For the output, all USAGE COMP-n are being replaced by DISPLAY,
000441* so that this record is text only and can be read in in any kind of program
000442* before each elementary item (they happen to be written with level number 10)
000443* a one character field is being placed which will take up a separator chracter
000444
000450 WORKING-STORAGE SECTION.
000460
000470 01  EDITRECORD SIGN IS LEADING SEPARATE CHARACTER
000480      .
000490 COPY RECDES01
000500        REPLACING
000510          == 01 == BY ==     02 ==
000520          == COMP   == BY == DISPLAY ==
000530          == COMP-1 == BY == DISPLAY ==
000540          == COMP-2 == BY == DISPLAY ==
000550          == COMP-3 == BY == DISPLAY ==
000560          == COMP-4 == BY == DISPLAY ==
000570          == COMP-5 == BY == DISPLAY ==
000580          == .
000590          10
000600          == BY == .
000610          10 FILLER  PIC X VALUE TAB.
000620          10 ==
000633      .
000640* This is the same record description, but the one character field
000641* is defined as with predefined value of TAB (see SPECIAL-NAMES).
000650
000660
000670 01  FILE-STATUS-INPUT.
000680      88  FILE-OK         VALUE '00'.
000690      02  FILLER          PIC 9.
000700          88  FILE-AT-END    VALUE 1.
000710      02  FILLER          PIC 9.
000720
000730 01  FILE-STATUS-OUTPUT.
000740      88  FILE-OK         VALUE '00'.
000750      02  FILLER          PIC 9.
000760          88  FILE-AT-END    VALUE 1.
000770      02  FILLER          PIC 9.
000780
000790
000800 PROCEDURE DIVISION.
000810 MAIN SECTION.
000820 ANFANG.
000821     MOVE SPACE TO EDITRECORD(1:1)
000830     OPEN INPUT INFILE
000840     OPEN OUTPUT OUTFILE
000850     READ INFILE
000860     PERFORM WITH TEST BEFORE
000880         UNTIL NOT FILE-OK IN FILE-STATUS-INPUT
000890       MOVE CORRESPONDING INRECORD TO EDITRECORD
000900       WRITE OUTRECORD FROM EDITRECORD
000910       READ INFILE
000920     END-PERFORM
000930     CLOSE INFILE
000940     CLOSE OUTFILE
000950     .
000960 ENDE.
000970     STOP RUN.


------------------ schnapp --------------------------------

Yours,
Lï¿½ko Willms                               http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Ohne Pressefreiheit, Vereins- und Versammlungsrecht ist keine
Arbeiterbewegung mï¿½glich"        - Friedrich Engels      (Februar 1865)
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 16)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-27T22:08:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4106c68d.21310588@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9DccbwE9flB@jpberlin-l.willms.jpberlin.de> <410583cd.207788887@news.optonline.net> <9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de>`

```
l.willms@jpberlin.de (Lueko Willms) wrote:

>   Thanks for your remarks regarding my Quick-and-dirty little  
>program.
…[17 more quoted lines elided]…
>   There is no trailing delimiter.

One of your versions placed the delimiter after the field by replacing period
with delimiter. This version puts the delimiter before the data. You  could have
eliminated both with move editrecord(2:length of editrecord - 2) to outrecord.

>RW> 2.  Delimiters in the data should be filtered out, not possible in
>RW> this case, or delimiter should be Tab, which will not appear in data.
>
>   OK. I define TAB as SYMBOLIC CHARACTER in the SPECIAL-NAMES  
>paragraph and use TAB instead of ";".

Or x'09'

>RW> 3.  Numeric fields need '.' in place of 'v' and '-' in place of 's9'.
>RW> Doing so seems impossible with this model.
…[3 more quoted lines elided]…
>   SIGN IS LEADING SEPARATE CHARACTER

Very good.

>   I thought about the decimal separator, and concluded that the  
>application importing the data would have to multiply all values of  
>that filed by 100 ... 

That's fair. Why must money amounts be in dollars or euros? Why not pennies?
Percentages and ratios come out the same.

>one could try a REPLACING ==V9== BY ==.9==, but  
>that could also affect the data name of an item in the record.

REPLACING works on words, not portions of words. 

REPLACE, new in the 2002 standard, works on portions of words:

REPLACE ==V9== BY ==.9==.
01  editrecord COPY ... REPLACING ...
REPLACE OFF.

It is unlikely a data name will contain 'V9'. To be cautious, you could say
REPLACE ==9V9== BY ==9.9== ALSO ==)V9== by ==).9==.

>RW> 4.  On a PC, the output should be LINE SEQUENTIAL. This makes COPY
>RW> under output FD superfluous. Make it x(2000).
…[6 more quoted lines elided]…
>the record, right?

Right. It also removes trailing spaces.
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 17)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-28T12:10:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Dkq5$G9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de> <4106c68d.21310588@news.optonline.net>`

```
.    Am  27.07.04
schrieb  robert.deletethis@wagner.net (Robert Wagner)
    auf  /COMP/LANG/COBOL
     in  4106c68d.21310588@news.optonline.net
  ueber  Re: Layout Hell.: leave it


   Thanks again for your comments.

>> RW> If you want to be fancy, do the same for the trailing
>> RW> delimiter via REVERSE.
>>
>>   There is no trailing delimiter.

RW> One of your versions placed the delimiter after the field by
RW> replacing period with delimiter.

   Yes, that was the error which I pointed out, since I made the  
change for EDITRECORD but forgot to make it for OUTRECORD.

   BTW, I have now, as you recommended eliminated the COPY of the  
original record descriptions from the OUTFILE FD, and defined this as  
LINE SEQUENTIAL with a  variable length record.

   I just wonder about the relationship of the RECORD VARYING IN SIZE  
clause in the FD and the corresponding OCCURS ... DEPENDING ON clause  
in the record description for that file.


RW> before the data. You  could have eliminated both with move
RW> editrecord(2:length of editrecord - 2) to outrecord.

   That is a very good idea.

   Is "LENGTH OF dataname" standard COBOL? I did not find it in the  
one printed document on COBOL-85 in my possession, which is the 1981  
draft standard .... but it was compiled without problems by Fujitsu  
COBOL 3.0.

   Before I used a
     INSPECT EDITRECORD TALLYING counter-item FOR CHARACTERS
   which also gave me the length of the record.


>> one could try a REPLACING ==V9== BY ==.9==, but
>> that could also affect the data name of an item in the record.

RW> REPLACING works on words, not portions of words.

   well, it did in this Fujitus COBOL 3.0, but, as I wrote, the  
compiler then choked on that PICTURE clause, so I removed it again and  
did not explore that further.

   My program is more an exercise in COBOL for me than a serious  
production program...


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Das Volk, das ein anderes Volk unterjocht, schmiedet seine eigenen
Ketten."                         - Karl Marx           (1. Januar 1870)
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 18)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-28T23:57:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41083812.115921649@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de> <4106c68d.21310588@news.optonline.net> <9Dkq5$G9flB@jpberlin-l.willms.jpberlin.de>`

```
l.willms@jpberlin.de (Lueko Willms) wrote:

>   BTW, I have now, as you recommended eliminated the COPY of the  
>original record descriptions from the OUTFILE FD, and defined this as  
…[4 more quoted lines elided]…
>in the record description for that file.

They define a proprietary variable-length-record file. A general-purpose LINE
SEQUENTIAL file looks like fixed-length, but actually writes variable length
records delimited by cr/lf (or nl on Unix).

>   Is "LENGTH OF dataname" standard COBOL? I did not find it in the  
>one printed document on COBOL-85 in my possession, which is the 1981  
>draft standard .... but it was compiled without problems by Fujitsu  
>COBOL 3.0.

No, it is not. FUNCTION LENGTH(dataname) is standard per the '89 addendum to the
'85 standard. LENGTH OF is supported by (at least) IBM, Micro Focus and Fujitsu.

>   My program is more an exercise in COBOL for me than a serious  
>production program...

We are in concord.
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 17)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-07-30T13:26:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Dp6eSsPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de> <4106c68d.21310588@news.optonline.net>`

```
.    Am  27.07.04
schrieb  robert.deletethis@wagner.net (Robert Wagner)
    auf  /COMP/LANG/COBOL
     in  4106c68d.21310588@news.optonline.net
  ueber  Re: Layout Hell.: leave it

>>   So, LINE SEQUENTIAL induces the system to add a CR/LF to the end of
>> the record, right?

RW> Right. It also removes trailing spaces.

   It does not in the program compiled by Fujitsu COBOL 3.0


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Regierung aus dem Volke, durch das Volk und fï¿½r das Volk"
   - Abraham Lincoln, Ansprache in Gettysburg, 19.11.1863
"... was in die revolutionï¿½re Sprache von heute ï¿½bersetzt heiï¿½t:
eine Regierung von Arbeitern, durch Arbeiter und fï¿½r Arbeiter"
                                  - Fidel Castro, November 1994
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-30T13:51:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407301251.222a9b9b@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <9Dgh5v3PflB@jpberlin-l.willms.jpberlin.de> <4106c68d.21310588@news.optonline.net> <9Dp6eSsPflB@jpberlin-l.willms.jpberlin.de>`

```
l.willms@jpberlin.de (Lueko Willms) wrote

> RW> Right. It also removes trailing spaces.
> 
>    It does not in the program compiled by Fujitsu COBOL 3.0

That is correct. Fujitsu 3 writes line sequential files to the length
of the record specified plus CR/LF.

Later versions also did this unless you specified an envionment
variable or run time file COBOL.CBR item
CBR_TRAILING_BLANK_RECORD=REMOVE.

In the V3 manual it suggests using

    FD  Text-File
        RECORD IS VARYING IN SIZE FROM 1 TO 80 CHARACTERS
        DEPENDING ON Record-Length.
    01  Text-Record.
        02  text-character-string.
         03 character-data PIC X OCCURS 1 TO 80 TIMES
                           DEPENDING ON record-length.


    WORKING-STORAGE SECTION.
    01  record-length   PIC 9(3) BINARY.

You would have to set the required record-length before WRITEing.
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 10)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-25T12:55:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4103ac60.87085680@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <cdrk2g$ah3$1@panix5.panix.com> <41028A19.FA1EAAB0@mb.sympatico.ca> <9DVRl0l9flB@jpberlin-l.willms.jpberlin.de> <oNydnTPpC_IKz57cRVn-iQ@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>I have 20 tapes which are all different data!
>The 20 tapes are not just one big table.
>
>I have 20 different stinking tables@!!!!!

You don't have 20 conversion programs. You have one program, NovaXchange, which
can convert any file when directed by a script. 

Lueko's solution is the same -- a program template that can convert any file
when specialized by a copybook describing the file.


>"Lueko Willms" <l.willms@jpberlin.de> wrote in message
>news:9DVRl0l9flB@jpberlin-l.willms.jpberlin.de...
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-07-24T22:33:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdv66e$quv$1@panix5.panix.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com> <41028A19.FA1EAAB0@mb.sympatico.ca>`

```
In article <41028A19.FA1EAAB0@mb.sympatico.ca>,
Peter Lacey  <lacey@mb.sympatico.ca> wrote:
>docdwarf@panix.com wrote:
>>>a flat or CSV file to read into Access or whatever it si she needs.
…[8 more quoted lines elided]…
>A few decades???

In Mr Wagner's case I believe this to be so, yes.

>All you need is an input fd using the copybook for
>field defs, an output fd with the same fields but just pic 9() instead
>of comp etc., and processing to open the files, read the records, move
>all the fields from input to output, and write.  Any rookie could
>program that.

That was not contested at all, Mr Lacey; what was stated (and what you 
quoted) stated a general condition ('a person with sufficient experience') 
and a specific manifestation ('in Mr Wagner's case a few decades and 
change').

>It is correct that unless the copybook matches one of the
>tapes the program will bomb, but on the information so far presented we
>can't be more specific.

Plural majestatus est, Mr Lacey; all I commented on what what I saw, what 
others can and cannot do might be another thing, entire.

>> 
>
…[17 more quoted lines elided]…
>of old, bad movies, I'd say.

Let's not forget... 'The Crawling Eye'.

DD
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 7)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T17:29:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<410291b4.14710792@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca> <cdrk2g$ah3$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>This is the problem that I saw... a person without the skills, without the 
>experience and without the appropriate corporate resources ('I cannot talk 
>to them for political reasons') was assigned a task. 

This is SOP in Big Consulting -- Accenture, EDS, et al. They hire recent college
grads with no programming experience, with degrees in biology, psychology, etc.
They give them a few weeks cursory training whose purpose is not to train but
rather to get a signature on a contract. Then they throw them into the deepest
water, to work 70 hours per week for sub-standard wages. On larger projects,
they contract with a few experienced programmers like me to rescue newbies when
(not if) they get into technical trouble. We function as lifeguards and JIT
educators. We're the only support they have; there are no manuals and sometimes
no internet access. 

In testimony to human adaptability, more than half the neophytes survive the
process. I remember one especially plucky young woman who took on production
support and system administration .. with less than one year IT experience. When
a Partner made a suggestive remark, she shot back without hesitation "Kiss my
ashes. You're out of line."

That reminds me of a true story about Laura Pederson, youngest Specialist on the
American Stock Exchange at 20. She ran the chaotic SPX pit (index options) the
day the market crashed, then skateboarded to the NYU Stern School to teach a
graduate course (Laura was a college dropout).  When she was a lowly Runner, a
Senior Partner asked "Why aren't you selling perfume at Bloomingdale?" She
retorted, "Why aren't you selling used cars in Paramus, New Jersey?" My kinda
woman. Theirs too. Instead of firing her, he made her a Specialist before she
could drink legally.
```

###### ↳ ↳ ↳ Re: Layout Hell.: leave it

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-23T15:38:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407231438.3160e55b@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <410151FB.F86ACC2D@mb.sympatico.ca>`

```
Peter Lacey <lacey@mb.sympatico.ca> wrote 

> the best of motives but they missed the point, which was that she
> doesn't care about the details, she just wants to convert the file.  And
> the easiest way to do it is to write a "Quick & Dirty" program to create
> a flat or CSV file to read into Access or whatever it si she needs.

Actually, you have this completely inverted. According to what has
been posted by her, she does have a program that appently will do the
task and all that she needs, or what she says she needs, is 'the
details' of what the layout is to tell the program.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T12:04:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I8WdnfOp0YGtzpzcRVn-qA@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com>`

```
just ask me!

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0407222332.538d74c5@posting.google.com...
> robert.deletethis@wagner.net (Robert Wagner) wrote
>
> > >I think that you _completely_ miss the point Robert.
> >
> > The point was to convert Carol's file to a format that Access (or Excel)
could
> > handle.
> >
…[17 more quoted lines elided]…
> > wasn't looking for an education in 'the idiosyncrasies of Cobol that
only we
> > geniuses can understand'.
>
…[5 more quoted lines elided]…
> > move on. I gave her and the numerous others who post similar queries a
free
> > tool
> > to get the job done.
…[13 more quoted lines elided]…
> > I spent four (billable) hours writing it. It worked the third time. I
love
> > writing this type software.
>
…[6 more quoted lines elided]…
> converter program.  There is no evidence either way in this thread.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-07-23T20:50:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duq2g0hgfemn8u5003ejo4k74lajueq7dd@4ax.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com>`

```
On Fri, 23 Jul 2004 12:04:37 -0600, "Carol" <kgdg@helkusa.com> wrote:

>just ask me!
Carol,

If you still haven't solved your problem please contact me by email.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-23T15:20:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407231420.40ce2e5e@posting.google.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote

> just ask me!

> > C >> I have 20 tapes and 20 file layoiuts. Maybe this file layout does
> > C >> not go with this tape?

Do you 20 different file layouts, one for each tape ?  Are the tapes
supposed to be of 20 different files or of one file for 20 different
time periods ?

Are these reel to reel or cartridge tapes ?  
What machine and operating system were used to write the tapes ?
Can you physically read them on some machine ?
Are they data tapes or archive tapes ?

A data tape is likely to have just one file on it, an archive tape may
have one or more data files 'bundled' using, say tar, or similar, and
may be data compressed.

Are the tapes (or the files within) in EBCDIC or ASCII or some other ?

> > C>> I have a job to convert these tapes form cobol to ascii text.

> > C>> I have a program to do this, but as you know I have to script it
> > C>> with the file layout.

What particular program is that ?  What results has it given ?

Probably the most useful thing would be if you could provide a hex
dump of the first 1000 bytes of the tape and what you believe to be
the record description.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 7)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T00:40:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J_udnaMJNNnYmZ_cRVn-qQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com> <217e491a.0407231420.40ce2e5e@posting.google.com>`

```
20 different tapes. 20 different piles of data.
All in the Same year.

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0407231420.40ce2e5e@posting.google.com...
> "Carol" <kgdg@helkusa.com> wrote
>
…[29 more quoted lines elided]…
> the record description.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T22:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4101922c.20784546@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>just ask me!

OK. 

Is the conversion running on a mainframe?

Does the machine have a Cobol compiler?

Could you move the file to a PC (by FTP, NDM or email) and convert it there?
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 7)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T00:41:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvKdnenBVcHimZ_cRVn-tw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com> <4101922c.20784546@news.optonline.net>`

```
The files are being read by Novastor tape drive and software.
This software converts the data, if only it knew how to read the copybooks.
I have to do all the parameters by hand.

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:4101922c.20784546@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[8 more quoted lines elided]…
> Could you move the file to a PC (by FTP, NDM or email) and convert it
there?
>
>
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 8)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T16:15:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4102600c.1996735@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com> <4101922c.20784546@news.optonline.net> <vvKdnenBVcHimZ_cRVn-tw@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>The files are being read by Novastor tape drive and software.
>This software converts the data, if only it knew how to read the copybooks.
>I have to do all the parameters by hand.

The NovaXchange manual is at
http://www.novastor.com/pub/docs/NovaXchange3.pdf

Go to Tape Inspector and select View to use the Hex Editor.

Toggle between ASCII and EBCDIC. Pic x fields will be readable in one, not the
other. That will be the type for pic x in your script.

Next look at comp-3 fields. On the hex screen, you should see a digit 0-9 in
each position (half byte) except the rightmost, which should have a C positive
sign. If you see anything different, post it here and someone will figure it
out.

Finally, look at comp fields to see whether zero values are predominantly on the
left or right side. These are called small-endian and big-endian, respectively.
If text is EBCDIC, the file was created on a mainframe, where comp is always
small-endian. 

Now you are ready to write the script, where types will be:

Pic x  -- EBCDIC or ASCII
Comp-3 -- pack_lowsign
Comp -- bin_msb if zeros were on left or bin_lsb if they were on the right
Pic 9 without comp -- ebc_zon_ls if text is EBCDIC. If text is ASCII and sign is
'zoned', you are out of luck. NovaXchange doesn't support that format.

Examples:

field = CTLGOP-CO-NO EBCDIC pic xxx 
field = CTLGCONTROL-SET-SEQ-NO bin_msg pic 999999999.
field = CTLGINVOICE-SEQ-NO bin_msb pic 9999
...
field = CTLGAP-VENDOR-NO EBCDIC * 30
field =  CTLGTOTAL-INVOICE-AM pack_lowsign pic 99999999999v99

field = DUE-DATE pack_lowsign date pic yymmdd -20
 (sliding date window of current year - 20)

If there are large comp fields, observe carefully how many bytes NovaXchange
allocates. Mathematically, pic s9(15) requires seven bytes for representation.
Most, but not all, Cobol compilers will allocate eight.
 

>"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
>news:4101922c.20784546@news.optonline.net...
…[11 more quoted lines elided]…
>there?
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 9)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T12:23:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eKdnVlSQISqNJ_cRVn-iQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <I8WdnfOp0YGtzpzcRVn-qA@comcast.com> <4101922c.20784546@news.optonline.net> <vvKdnenBVcHimZ_cRVn-tw@comcast.com> <4102600c.1996735@news.optonline.net>`

```
hoily moly robert . That's great
!

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:4102600c.1996735@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
> >The files are being read by Novastor tape drive and software.
> >This software converts the data, if only it knew how to read the
copybooks.
> >I have to do all the parameters by hand.
>
…[5 more quoted lines elided]…
> Toggle between ASCII and EBCDIC. Pic x fields will be readable in one, not
the
> other. That will be the type for pic x in your script.
>
> Next look at comp-3 fields. On the hex screen, you should see a digit 0-9
in
> each position (half byte) except the rightmost, which should have a C
positive
> sign. If you see anything different, post it here and someone will figure
it
> out.
>
> Finally, look at comp fields to see whether zero values are predominantly
on the
> left or right side. These are called small-endian and big-endian,
respectively.
> If text is EBCDIC, the file was created on a mainframe, where comp is
always
> small-endian.
>
…[5 more quoted lines elided]…
> Pic 9 without comp -- ebc_zon_ls if text is EBCDIC. If text is ASCII and
sign is
> 'zoned', you are out of luck. NovaXchange doesn't support that format.
>
…[12 more quoted lines elided]…
> If there are large comp fields, observe carefully how many bytes
NovaXchange
> allocates. Mathematically, pic s9(15) requires seven bytes for
representation.
> Most, but not all, Cobol compilers will allocate eight.
>
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-23T22:29:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41018a1d.18721187@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote

>If she had a Cobol compiler and an FD that provably matched the data
>_tapes_ then she wouldn't have the problem.

She has a way of reading tapes. I took that to mean she has access to a
mainframe. She cannot write 20 conversion programs because she doesn't know
Cobol. Whether she has access to a Cobol compiler isn't clear. Most mainframes
do. Getting a programmer, even one from another shop, to compile my program *one
time* would give her the tool she needs.

>C>> I have a job to convert these tapes from cobol to ascii text.
>C>> I have a program to do this, but as you know I have to script it 
>C>> with the file layout.

Again, "to ascii text" sounds like the conversion is running on a mainframe. My
program 'writes its own script'.

>Yet you sent her something that required her to know things that 'only
>we geniuses' could so something with, such as compile. 

Companies with mainframes have programmers capable of compiling a program. If
she asks nicely, they'll do it 'under the radar'. If she asks them to write 20
programs, they'll require paperwork and approvals.

> And BTW how would Fujitsu v3 read a _tape_ ?

She could FTP (or NDM) the files to a PC in Binary mode and do the conversion
there. That would require a one-statement EBCDIC-to-ASCII conversion in my
convert-string paragraph. Someone here could easily provide that statement ..
and start another long thread.

>C>> I have a program to do this, but as you know I have to script it 
>C>> with the file layout.
…[3 more quoted lines elided]…
>seem to do so frequently.

I 'wrote the script' internally, then used it to convert the file. If she
prefers to use her own tool and is willing to describe its scripting language,
I'll modify my program to spit script into a text file. It seems pointless to
run two tools rather than one.

>BTW, I thought the problem _might_ be that it is in EBCDIC on an ASCII
>machine, or vice versa, and thus nonsense is coming out of her
>converter program.  There is no evidence either way in this thread.

The data is very likely in EBCDIC. Unix and PC shops do not exchange data via
tape. They do it with FTP, NFS Mount, Samba, email, etc. Worst case, they'd
write the files to a CD, not a tape.
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 6)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T00:42:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1eSdnfzs65VZmZ_cRVn-jw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <41018a1d.18721187@news.optonline.net>`

```
CD is not big enough.
We are talking mabye 200 gig of data.,


"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:41018a1d.18721187@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
…[6 more quoted lines elided]…
> mainframe. She cannot write 20 conversion programs because she doesn't
know
> Cobol. Whether she has access to a Cobol compiler isn't clear. Most
mainframes
> do. Getting a programmer, even one from another shop, to compile my
program *one
> time* would give her the tool she needs.
>
…[4 more quoted lines elided]…
> Again, "to ascii text" sounds like the conversion is running on a
mainframe. My
> program 'writes its own script'.
>
…[3 more quoted lines elided]…
> Companies with mainframes have programmers capable of compiling a program.
If
> she asks nicely, they'll do it 'under the radar'. If she asks them to
write 20
> programs, they'll require paperwork and approvals.
>
> > And BTW how would Fujitsu v3 read a _tape_ ?
>
> She could FTP (or NDM) the files to a PC in Binary mode and do the
conversion
> there. That would require a one-statement EBCDIC-to-ASCII conversion in my
> convert-string paragraph. Someone here could easily provide that statement
..
> and start another long thread.
>
…[8 more quoted lines elided]…
> prefers to use her own tool and is willing to describe its scripting
language,
> I'll modify my program to spit script into a text file. It seems pointless
to
> run two tools rather than one.
>
…[4 more quoted lines elided]…
> The data is very likely in EBCDIC. Unix and PC shops do not exchange data
via
> tape. They do it with FTP, NFS Mount, Samba, email, etc. Worst case,
they'd
> write the files to a CD, not a tape.
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 7)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T16:15:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4102890f.12497045@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <41018a1d.18721187@news.optonline.net> <1eSdnfzs65VZmZ_cRVn-jw@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>CD is not big enough.
>We are talking mabye 200 gig of data.,

For Expenses Payable? You are going to load 200G into a Jet (Access) database?
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 8)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-24T12:24:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I4udndySVvHKNJ_cRVn-iw@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <41018a1d.18721187@news.optonline.net> <1eSdnfzs65VZmZ_cRVn-jw@comcast.com> <4102890f.12497045@news.optonline.net>`

```
A whole bunch of them.
The whole thing is pointless, isn't it!!!

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:4102890f.12497045@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[3 more quoted lines elided]…
> For Expenses Payable? You are going to load 200G into a Jet (Access)
database?
>
>
>
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 9)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-24T19:17:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4102af3a.22269709@news.optonline.net>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net> <217e491a.0407222332.538d74c5@posting.google.com> <41018a1d.18721187@news.optonline.net> <1eSdnfzs65VZmZ_cRVn-jw@comcast.com> <4102890f.12497045@news.optonline.net> <I4udndySVvHKNJ_cRVn-iw@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>A whole bunch of them.
>The whole thing is pointless, isn't it!!!

I haven't worked with Jet much, but have seen MANY reports on the Web
complaining about corruption and slow performance when loaded with 1G tables. 

Google and Yahoo use MySQL for databases much larger than yours. It's free, very
fast and reported to be reliable.

I fear you're setting yourself up for failure by using Jet.

The _point_ is doing something 'they' thought you couldn't. Even if the project
is poorly managed from a business point of view, getting it done would be a
personal success. It'll look good on your resume, and will probably make sense
at the next company.

>"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
>news:4102890f.12497045@news.optonline.net...
…[6 more quoted lines elided]…
>database?
```

###### ↳ ↳ ↳ Re: Layout Hell.

_(reply depth: 4)_

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-23T12:01:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nKqdnV6A8b4Vz5zcRVn-qQ@comcast.com>`
- **References:** `<JZCdnZ690pjbiWrd4p2dnA@comcast.com> <40ffe8da.70647174@news.optonline.net> <217e491a.0407221352.2c2002c4@posting.google.com> <410042b5.93653409@news.optonline.net>`

```
I do not have a cobol compiler.  I have colbol tapes, and i sit waiting at a
windows computer.


"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:410042b5.93653409@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
…[3 more quoted lines elided]…
> >> >I am new to the layout scene, but if I could see some real examples, I
might
> >> >get it. Then again, I might club myself with a shovel.
> >> >Thank you.
…[8 more quoted lines elided]…
> The point was to convert Carol's file to a format that Access (or Excel)
could
> handle.
>
> I'm not into 'Zen wisdom' so just say what you think the point was. Hint:
she
> wasn't looking for an education in 'the idiosyncrasies of Cobol that only
we
> geniuses can understand'. She just wanted to get the damn file converted
and
> move on. I gave her and the numerous others who post similar queries a
free tool
> to get the job done. I spent four (billable) hours writing it. It worked
the
> third time. I love writing this type software.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
