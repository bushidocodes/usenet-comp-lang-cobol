[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# inherited cobol app., can't run (xm.exe)?

_27 messages · 9 participants · 2008-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### inherited cobol app., can't run (xm.exe)?

- **From:** KJ <n_o_s_p_a__m@mail.com>
- **Date:** 2008-03-08T16:37:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com>`

```
Hello. I agreed to take on a COBOL conversion project. I am trying to
run the customer's cobol project (it's called COBEST). It is looking
for a program called XM.exe. I don't have this on my system. Anyone
know where I can get this?
```

#### ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-09T00:01:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t6rqic8fr9u80@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com>`

```

"KJ" <n_o_s_p_a__m@mail.com> wrote in message
news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
> Hello. I agreed to take on a COBOL conversion project. I am trying to
> run the customer's cobol project (it's called COBEST). It is looking
> for a program called XM.exe. I don't have this on my system. Anyone
> know where I can get this?

XM.EXE is the extended memory manager for 16-bit
Micro Focus COBOL. It is used to allow access to
as much as 16 megabytes of memory. Its default
location is C:\COBOL\EXEDLL.
```

##### ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** KJ <n_o_s_p_a__m@mail.com>
- **Date:** 2008-03-08T21:30:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com>`

```
On Mar 9, 12:01 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> "KJ" <n_o_s_p_a...@mail.com> wrote in message
>
…[10 more quoted lines elided]…
> location is C:\COBOL\EXEDLL.

Thanks for the reply Rick.

To say I am in the dark on this project would be a massive
understatement.
You've shed the first light and I thank you.

I have many more questions. First is, where might I get a copy of this
program? I have been given:

* .GNT files
* Cobol data files (no file extension -- named by the entity they
hold, paired with matching .IDX file)
* Exe and batch files (for the COBEX construction management program)

Do I need a copy of DOS too?
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-09T01:14:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t703lonpla614@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com>`

```

"KJ" <n_o_s_p_a__m@mail.com> wrote in message
news:3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com...
> On Mar 9, 12:01 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> > "KJ" <n_o_s_p_a...@mail.com> wrote in message
> >
> >
news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
> >
> > > Hello. I agreed to take on a COBOL conversion project. I am trying to
…[21 more quoted lines elided]…
> * Exe and batch files (for the COBEX construction management program)

You get a copy of XM from the same computer from which
the GNT, data, and other files came. XM versions match
Micro Focus COBOL versions; though the version numbers
are not identical. For example, COBOL 3.2.24 came with
XM 1.4.6. Using a version of XM that predates the COBOL
version may not work.

> Do I need a copy of DOS too?

XM runs on Windows 95, 98, etc, and Windows NT,
2000, etc,; though probably not Vista and maybe not XP.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 4)_

- **From:** KJ <n_o_s_p_a__m@mail.com>
- **Date:** 2008-03-08T23:17:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com>`

```
On Mar 9, 2:14 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> "KJ" <n_o_s_p_a...@mail.com> wrote in message
>
…[43 more quoted lines elided]…
> 2000, etc,; though probably not Vista and maybe not XP.

I will try to get those files from the client's desktop. He seems to
be running it on Windows XP (I need to take a closer look -- this was
only my first visit).

Couple quick questions:

* Can .GNT files be decompiled?
* What is the purpose of the IDX file -- some kind of index into the
main data file?
* Are the data files parseable without knowing the record definitions?
I tried a tool from Siber which did a so-so job of displaying the
data. I'm sure there's some rules to doing it, but I surely don't know
them.
* Is there a tutorial online where I can learn how to read data
properly out of these files? I can see some things which look familiar
in there, but others do not (I'm using a hex text editor -- notepad++
actually)

Thanks so much for your experience on this topic.

-KJ
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-09T06:23:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t7i5n9lcaj89c@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>`

```

"KJ" <n_o_s_p_a__m@mail.com> wrote in message
news:0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com...
> On Mar 9, 2:14 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> > "KJ" <n_o_s_p_a...@mail.com> wrote in message
> >
> >
news:3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com...> On
Mar 9, 12:01 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> > > > "KJ" <n_o_s_p_a...@mail.com> wrote in message
> >
> >
news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
> >
> >
…[3 more quoted lines elided]…
> > > > > Hello. I agreed to take on a COBOL conversion project. I am trying
to
> > > > > run the customer's cobol project (it's called COBEST). It is
looking
> > > > > for a program called XM.exe. I don't have this on my system.
Anyone
> > > > > know where I can get this?
> >
…[37 more quoted lines elided]…
> * Can .GNT files be decompiled?

GNT is machine language. It may be disassembled; but not
decompiled.

> * What is the purpose of the IDX file -- some kind of index into the
> main data file?

Yes, but it may contain multiple indexes based on several
key fields.

> * Are the data files parseable without knowing the record definitions?
> I tried a tool from Siber which did a so-so job of displaying the
> data. I'm sure there's some rules to doing it, but I surely don't know
> them.

Some have used ParseRat:
< http://www.guysoftware.com/parserat.htm >

> * Is there a tutorial online where I can learn how to read data
> properly out of these files? I can see some things which look familiar
> in there, but others do not (I'm using a hex text editor -- notepad++
> actually)

< http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm >

> Thanks so much for your experience on this topic.

You're welcome.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 6)_

- **From:** KJ <n_o_s_p_a__m@mail.com>
- **Date:** 2008-03-09T09:31:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<980133a6-8ba1-4366-b9d5-f95caf933290@m44g2000hsc.googlegroups.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <13t7i5n9lcaj89c@corp.supernews.com>`

```
On Mar 9, 7:23 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> "KJ" <n_o_s_p_a...@mail.com> wrote in message
>
…[85 more quoted lines elided]…
> You're welcome.

I've been using ParseRat this morning. It's helping a lot. Is there a
way to decipher the header in a (binary) data file? The one I'm
working with looks like this: 9611230914266196112309142661

When I parse out a record, it looks like this (XML-formatted):

<RECORD>
<Col1_9>01AC-02</Col1_9>
<Col10_10></Col10_10>
<Col11_20>T01600.200</Col11_20>
<Col21_End>AIR CHISEL                    CP-9356        406
CHICAGO PNEUMATIC</Col21_End>
</RECORD>

Now, obviously this isn't a perfect parse, but it's a start. The data
file holds information about construction tools and equipment.

I can figure out most of the above, except for 01600.200 Any clue what
that is? There are two of those similar values (one per record). One
is that value, the other is: 01600.010 The 'T' before 01600.200 means
it's a tool. Likewise, 01600.010 usually looks like E01600.010, "E"
meaning it's considered equipment in this system.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-09T13:25:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t8av4dpbv0358@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <13t7i5n9lcaj89c@corp.supernews.com> <980133a6-8ba1-4366-b9d5-f95caf933290@m44g2000hsc.googlegroups.com>`

```

"KJ" <n_o_s_p_a__m@mail.com> wrote in message
news:980133a6-8ba1-4366-b9d5-f95caf933290@m44g2000hsc.googlegroups.com...

[snip]

> I've been using ParseRat this morning. It's helping a lot. Is there a
> way to decipher the header in a (binary) data file? The one I'm
…[19 more quoted lines elided]…
> meaning it's considered equipment in this system.

The file header (first 128 bytes) is described in documentation
supplied as part of the COBOL development environment.
It is too detailed to go into here; but it is probably not necessary,
for your use, to know its contents.

The record content depends on the application. I don't know
enough about the application to help. However, as you run
the application, you should be able to assign names to some
of the fields that compose the records.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2008-03-09T14:46:35+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vm7t316trg64scvumfd8fsie9q4vh6udo@4ax.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>`

```
On Sat, 8 Mar 2008 23:17:55 -0800 (PST) KJ <n_o_s_p_a__m@mail.com> wrote:

:>* Are the data files parseable without knowing the record definitions?
:>I tried a tool from Siber which did a so-so job of displaying the
:>data. I'm sure there's some rules to doing it, but I surely don't know
:>them.

Perhaps, if you know something about the data.

:>* Is there a tutorial online where I can learn how to read data
:>properly out of these files? I can see some things which look familiar
:>in there, but others do not (I'm using a hex text editor -- notepad++
:>actually)

Did they not provide you with the original COBOL source code?
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 6)_

- **From:** KJ <n_o_s_p_a__m@mail.com>
- **Date:** 2008-03-09T09:21:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0fb470f-d73c-47c4-a68a-368f8ce43c1f@m34g2000hsc.googlegroups.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <3vm7t316trg64scvumfd8fsie9q4vh6udo@4ax.com>`

```
On Mar 9, 8:46 am, Binyamin Dissen <postin...@dissensoftware.com>
wrote:
> On Sat, 8 Mar 2008 23:17:55 -0800 (PST) KJ <n_o_s_p_a...@mail.com> wrote:
>
…[23 more quoted lines elided]…
> especially those from irresponsible companies.

They didn't give me the source code -- they don't have it. I am going
to call the company that developed the program to see if I can
persuade.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 7)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-03-10T16:30:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19e081e1-24e3-4cb8-b115-73c731ac6513@e23g2000prf.googlegroups.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <3vm7t316trg64scvumfd8fsie9q4vh6udo@4ax.com> <e0fb470f-d73c-47c4-a68a-368f8ce43c1f@m34g2000hsc.googlegroups.com>`

```
On Mar 10, 5:21 am, KJ <n_o_s_p_a...@mail.com> wrote:

> They didn't give me the source code -- they don't have it. I am going
> to call the company that developed the program to see if I can
> persuade.

From:

http://www.awci.org/cd/pdfs/9108_c.pdf

Modern Data
Management, Inc.
363 Washington Street
Hartford, CT 06106
(800) 726-3160

COBEST Construction
Management Software

Modules include: Estimating,
Job Costing & Analysis,
Contract Management, Project
Scheduling, Equipment
Control, POs, Submittal
Control, Order Processing,
General Ledger, APs, ARs,
Union & Certified Payroll.

IBM PC Compatible 646 K
memory, 50 Meg HD, IBM
PS/2, IBM AS/400, UNIX/
AlX, WANG VS, D/G
AViiON

Free 1 year maintenance &
support, 800 hot line
support. Free on-site
installation and training, On-
line HELP.


'Persuade' may require the ability to write cheques for 6 or 7 figure
numbers.

Why would they 'give', or even sell, the source code to a product that
you are contracted to create a competitor or replacement for ?

In fact they may even 'persuade' you via the courts that you are
attempting to steal their IP and/or Trade Secrets. There may even be
EULA or contracts that prevent you, as an agent of the customer, from
doing what you have done so far.  Check your liability and indemnity
clauses in the contract with your customer. Don't have any ? oh bad
luck, get a lawyer.


> * Can .GNT files be decompiled?

No.

If you are trying to run .GNT files, or are wanting to use XM.EXE then
you will need to buy a licensed run-time from Microfocus. With DOS
based MF systems there are ways of building applications that do not
require run-time fees, but .GNT and XM and not within that.

> * What is the purpose of the IDX file -- some kind of index into the
> main data file?

Yes.

> * Are the data files parseable without knowing the record definitions?

No. Not generally anyway. You may be able to work out what many data
items are from knowing the data values and seeing where they are in
the record.

> I tried a tool from Siber which did a so-so job of displaying the
> data. I'm sure there's some rules to doing it, but I surely don't know
> them.

That may be as good as it gets.

> * Is there a tutorial online where I can learn how to read data
> properly out of these files? I can see some things which look familiar
> in there, but others do not (I'm using a hex text editor -- notepad++
> actually)

Stuff may be binary or packed decimal or even proprietary. If you
recognise something then it may be that, otherwise you may never know
what the data represents.

>> I agreed to take on a COBOL conversion project.

It seems that it _isn't_ a "COBOL conversion project" at all. It is a
'ground up' reimplementation of what they are doing with a packaged
solution. That would be fine if:

a) you are paid an hourly or weekly rate suitable for an analyst/
programmer (which you are obviously not).

b) there is an unlimited budget

c) there is no completion date specified.

However, if there are date and budget limits, or specified contractual
performance, then run away now.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 8)_

- **From:** "HeyBub" <heybub@gmail.com>
- **Date:** 2008-03-10T21:53:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tbt22jsmt8dfd@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <3vm7t316trg64scvumfd8fsie9q4vh6udo@4ax.com> <e0fb470f-d73c-47c4-a68a-368f8ce43c1f@m34g2000hsc.googlegroups.com> <19e081e1-24e3-4cb8-b115-73c731ac6513@e23g2000prf.googlegroups.com>`

```
Richard wrote:
>
>
…[64 more quoted lines elided]…
> performance, then run away now.

Maybe he could use Linux or a pile of steaming GNU stuff?
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-03-09T15:58:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fr11f2$65m$1@reader2.panix.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>`

```
In article <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>,
KJ  <n_o_s_p_a__m@mail.com> wrote:
>On Mar 9, 2:14 am, "Rick Smith" <ricksm...@mfi.net> wrote:
>> "KJ" <n_o_s_p_a...@mail.com> wrote in message
…[9 more quoted lines elided]…
>> > > > Hello. I agreed to take on a COBOL conversion project.

[snip]

>> > To say I am in the dark on this project would be a massive
>> > understatement.

This is becoming more and more obvious.

Might I asked what reasoning you used to conclude that 'yes, I can 
honestly and honorably say that I have the skills and experience to 
perform the project for which I contracted myself'?

DD
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 6)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-03-09T11:41:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<orUAj.6202$pl4.5388@newssvr22.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote in message news:fr11f2$65m$1@reader2.panix.com...
> In article
> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com>,
…[10 more quoted lines elided]…
> perform the project for which I contracted myself'?

I often disagree with DD, but in this case I simply must concur with his
assessment, and I'm not shy about taking it to the next step:

Your saying "yes" to this project is nothing less than an insult to all the
true professionals here.

As far as I am concerned you are entitled to and should expect exactly zero
additional assistance here and can wallow in your own arrogance.

The only redeeming feature here is that your use of an alias and fake email 
address seems to
indicate you have a least a modicum of guilt for doing this, and you can 
build on that.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@gmail.com>
- **Date:** 2008-03-09T14:07:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t8danffc7pude@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net>`

```
Michael Mattias wrote:
> <docdwarf@panix.com> wrote in message
> news:fr11f2$65m$1@reader2.panix.com...
…[26 more quoted lines elided]…
> can build on that.

And he's posting via Google Groups...

Although it's unsaid, I'd wager he wants to convert an inventory system in a 
commercial environment to a web-based environment using Java.

In my view, one can't really be a programming professional without knowing a 
little something about FORTRAN and Cobol, BAL, and, of course, the newer 
languages.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-03-09T23:24:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fr1rj2$oki$1@reader2.panix.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net>`

```
In article <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:fr11f2$65m$1@reader2.panix.com...
>> In article
…[17 more quoted lines elided]…
>true professionals here.

Oh, I *cannot* resist...

... wow... you mean *both* of them?

DD
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-11T01:20:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63kncdF2809f3U1@mid.individual.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:orUAj.6202$pl4.5388@newssvr22.news.prodigy.net...
> <docdwarf@panix.com> wrote in message 
> news:fr11f2$65m$1@reader2.panix.com...
…[13 more quoted lines elided]…
>

Are you sure the original poster was contracted, and what bearing does it 
have on whether or not he gets help?

Suppose there was no-one else available who would take it on?

People often find themselves in situiations they'd rather not be in. 
Sometimes it is through over-confidence, sometimes it is through 
foolishness, sometimes it is simply being told to do something if you want 
to keep your job, occasionally it is because they have an eye to the "main 
chance" and try to make a few bob... I don't see it as the province of this 
forum to pontificate or make value judgements about it.

> I often disagree with DD, but in this case I simply must concur with his
> assessment, and I'm not shy about taking it to the next step:
…[3 more quoted lines elided]…
> true professionals here.

I think that's more than a bit harsh and disagree. Besides, as one of the 
professionals here, I don't feel insulted by this... :-) (Maybe I'm not a 
"true" professional by your definition, Michael (whatever that means...), 
but if being one means taking offence where none is intended, then I'd 
rather not be one...)

I don't see arrogance in the posts; I see a request for help with some good 
advice being given.

We don't know the circumstances under which KJ took this on. He may have 
been required to do this, and is doing the best he can. He has certanly made 
some good progress given he doesn't have any source code...

I would be concerned if people asking for help here are now to be subject to 
judgement as to their worthiness of receiving it.

Doc's admonition to "do your own homework" is a fair and reasonable 
response, if he feels that someone is seeking to get their homework done 
here, but that is not the same thing as someone who is working in the IT 
field requesting help for an aspect of programming which he is not expert 
in.

It seems pretty simple to me. If you want to help; do so. If you don't want 
to help, then don't.

Value judgements are in no way constructive or helpful, and actually reflect 
very poorly on the people making them, at least as far as I'm concerned.

Are COBOL "professionals" now so endangered by the diminishing market that 
they will withhold help from others, like a closed Cult protecting its Holy 
Secrets? It was partly because of that attitude that COBOL fell into decline 
in the first place.

Yes, we make a living selling skill, but if you sold bread, would you never 
give the odd bun away? If you were a butcher, would you not give a kid a 
saveloy? I guess it comes down to personality and attitude, just like any 
field of endeavour.

>
> As far as I am concerned you are entitled to and should expect exactly 
> zero
> additional assistance here and can wallow in your own arrogance.

Again, I disagree, although I respect your right to feel that way, Michael.

>
> The only redeeming feature here is that your use of an alias and fake 
> email address seems to
> indicate you have a least a modicum of guilt for doing this, and you can 
> build on that.

Or, it could just be that he doesn't want to reveal who he is in a Usenet 
forum. If using a nom-de-plume is now to be cause for suspicion and 
withholding help, then I guess we won't be seeing any further replies to 
posts from Doc Dwarf.... :-)

Pete.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-03-10T13:47:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i_aBj.22597$R84.6191@newssvr25.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net> <63kncdF2809f3U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:63kncdF2809f3U1@mid.individual.net...
> Value judgements are in no way constructive or helpful, and actually 
> reflect very poorly on the people making them, at least as far as I'm 
> concerned.

I have to disagree with my esteemed colleague from the bottom half of Planet 
Earth.

While such unsolicited value judgements may be in poor taste when offered in 
a public forum, we - the professional IT community - simply must police 
ourselves if we are to earn the professional respect we seek, and part of 
the way we police ourselves is the frank expression of our values.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-03-10T13:47:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i_aBj.22596$R84.6499@newssvr25.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <0457479f-d85a-43da-bd2f-51861fcee256@m44g2000hsc.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net> <63kncdF2809f3U1@mid.individual.net>`

```

```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-03-10T19:20:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fr41mf$ps0$1@reader2.panix.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net> <63kncdF2809f3U1@mid.individual.net>`

```
In article <63kncdF2809f3U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[20 more quoted lines elided]…
>have on whether or not he gets help?

The original poster referred to 'the customer's' work, not 'my employer's' 
or 'my boss's'... hence my conclusion.

>
>Suppose there was no-one else available who would take it on?

The same thing might happen were I to suppose that there were no 
hypothetical questions.  It is rare, in my experience, for someone to say 
to a customer 'No, I do not have the skills for this' and then be told 
'Here, take my money, I don't care!'

DD
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 9)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-03-10T20:05:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8wgBj.16613$Ch6.12386@newssvr11.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <fr11f2$65m$1@reader2.panix.com> <orUAj.6202$pl4.5388@newssvr22.news.prodigy.net> <63kncdF2809f3U1@mid.individual.net> <fr41mf$ps0$1@reader2.panix.com>`

```
>>Suppose there was no-one else available who would take it on?

That's the old law-school ethics discussion: You're the last lawyer in town; 
are you obligated to defend the man accused of stealing from a relative NOT 
immediate family?

(Many variations of same).

MCM
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 4)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2008-03-09T14:00:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4SAj.16463$Ch6.15080@newssvr11.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com>`

```
In article <13t703lonpla614@corp.supernews.com>, "Rick Smith" <ricksmith@mfi.net> wrote:

>XM runs on Windows 95, 98, etc, and Windows NT,
>2000, etc,; though probably not Vista and maybe not XP.

If it runs on 95, 98, NT, and 2000, what reason is there to think that it 
would *not* run on XP in {95, 98, NT, or 2000} emulation mode?

For that matter, if it runs on NT, what reason is there to think that it will 
not run on XP *without* emulation?
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-09T09:47:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t7u6b22sou949@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <d4SAj.16463$Ch6.15080@newssvr11.news.prodigy.net>`

```

"Doug Miller" <spambait@milmac.com> wrote in message
news:d4SAj.16463$Ch6.15080@newssvr11.news.prodigy.net...
> In article <13t703lonpla614@corp.supernews.com>, "Rick Smith"
<ricksmith@mfi.net> wrote:
>
> >XM runs on Windows 95, 98, etc, and Windows NT,
…[3 more quoted lines elided]…
> would *not* run on XP in {95, 98, NT, or 2000} emulation mode?

My experience is limited to Windows versions up to 2000;
therefore, I do not know about emulation modes on XP.

> For that matter, if it runs on NT, what reason is there to think that it
will
> not run on XP *without* emulation?


I had read comments about problems with running DOS
programs on XP due to XP's handling of character output
and that the problems could be resolved by installing a
particular display driver.

Furthermore, I do not recall any comments to the effect that
XM will run on XP.

Bottom-line--"maybe not XP" means I don't know and the
above are the reasons I have for denying any knowledge that
XM will run on XP.
```

###### ↳ ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

_(reply depth: 6)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2008-03-09T15:19:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IdTAj.20110$0w.19094@newssvr27.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <13t6rqic8fr9u80@corp.supernews.com> <3e8041b2-c5ff-465b-af2f-3da5aff45ccc@b1g2000hsg.googlegroups.com> <13t703lonpla614@corp.supernews.com> <d4SAj.16463$Ch6.15080@newssvr11.news.prodigy.net> <13t7u6b22sou949@corp.supernews.com>`

```
In article <13t7u6b22sou949@corp.supernews.com>, "Rick Smith" <ricksmith@mfi.net> wrote:
>
>"Doug Miller" <spambait@milmac.com> wrote in message
…[11 more quoted lines elided]…
>therefore, I do not know about emulation modes on XP.

Google "compatibility mode" for more information, or search the Microsoft 
Knowledge Base. The same facility exists in Windows 2000 SP2 -- it's been 
several years since I used Win2K so I'm going from a possibly-faulty memory 
here, but I'm pretty sure it works the same way as it does in XP: right-click 
on any executable, then select Properties, and click the Compatibility tab.

More info on Win2K compatibility mode here:
http://www.windowsitpro.
com/article/articleid/43388/windows-2000-compatibility-mode.html
```

#### ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-03-09T11:32:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mjUAj.6201$pl4.2475@newssvr22.news.prodigy.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com>`

```
"KJ" <n_o_s_p_a__m@mail.com> wrote in message 
news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
> Hello. I agreed to take on a COBOL conversion project.....

I've met some other people like you - people who don't know when and/or how 
to say "No."

MCM
```

##### ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-11T01:22:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63knfsF287ueaU1@mid.individual.net>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <mjUAj.6201$pl4.2475@newssvr22.news.prodigy.net>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:mjUAj.6201$pl4.2475@newssvr22.news.prodigy.net...
> "KJ" <n_o_s_p_a__m@mail.com> wrote in message 
> news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
…[6 more quoted lines elided]…
>
Be thankful you didn't marry one... :-)

Pete
```

##### ↳ ↳ Re: inherited cobol app., can't run (xm.exe)?

- **From:** "HeyBub" <heybub@gmail.com>
- **Date:** 2008-03-10T08:23:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tadi9qatngj3e@corp.supernews.com>`
- **References:** `<465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com> <mjUAj.6201$pl4.2475@newssvr22.news.prodigy.net>`

```
Michael Mattias wrote:
> "KJ" <n_o_s_p_a__m@mail.com> wrote in message
> news:465b2ca6-3900-41e1-a6eb-0f60b8bb33bf@f47g2000hsd.googlegroups.com...
…[4 more quoted lines elided]…
>

"I'm just the girl who can't say 'N.., n..., nnn..., NNNN!!!..., n,...' "

Best time of my life, when I met her...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
