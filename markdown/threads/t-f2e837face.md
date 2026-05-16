[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Stategy for (Large?) 16bit COBOL code conversion to Net Express

_42 messages · 11 participants · 2007-10_

---

### Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** "news" <greg@primesoft.co.nz>
- **Date:** 2007-10-16T11:32:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4713eb53$1@news.orcon.net.nz>`

```
I'm looking for comment on any issues I may encounter in a conversion for 
Microsoft COBOL V5 (Which was licenced off Micro Focus) and Version 5 of Net 
Express.

Background

I am the owner/operator of the company that owns the copyright to the source 
code. I am not a programmer (Although I understand the principals of 
programming and suprise myself at what bugs I can fix)
The system is currently a PC Based Financial suite.
There are between 500,000 and a million lines of code (Is that large?)
There are about 100 installations of the 16 bit version of the system.
Companys using it range from NZ$400M turnover to $100K turnover (What New 
Zealand would regard as Small to Medim sized businesses)
ISAM data structure.
Current system is 16bit console based, stable and fast.
User Support for the product just won't die (They like it) However 
development constraints such as memory issues of staying under 640K and 
printing issues are getting more expensive to support.
I have an Evaluation Edition (Time constrained latest full version) of Net 
Express and Visual studio 2005 loaded on a Windows 2003 Terminal server.
I have paid for and completed the initial phase of a proof of Concept. One 
Module (100,000 lines of code compiled and has produced working executables 
but not fully tested)
I now have to assess cost of several logical phases. i.e. assess the min and 
max cost possible for each phase - This is where any issues I need to 
consider would be valuable, I can't research what I don't know.
On completion of this analysis I will go out to the Userbase with an 
indication of costs they will need to absorb.(several key players in this 
group have been informed of this process)  If I get support, the conversion 
will go ahead, if not, I will create a strategy to exit the market.

Phases

1.    Straight conversion to a 32bit console version of the system. Possible 
consolidation of executables. No improvements. Users having memory issues 
would no longer get these symptoms.
2.    Write a module to replace ASSIGN PRINTER to handle printed output.
3.    Write a web interface using Net Express and hopefully AJAX to replace 
the screen I/O of the current version. Duplication of look and feel of 
exsisting interface envisagaged. Compile as a .Net application.
4.    Port to Linux using MONO (.NET framework for Linux)
5.    Revisit the user interface (3.) altering bigger sections of underlying 
business logic to enable us to produce a "prettier" more flexible interface. 
Possible conversion of some code to Object orientated code.
6.    Alter Code to handle security for system to run as a web application 
in a bureau environment.5. & 6. may occur simultaneously.
7.    Port to a relational database (Probably Postgres)  for easier 3rd 
party reporting.

Progammer Strategy

1.    Devide the tasks into managable portions.
2.    Clearly define deliverables for each portion.
3.    Go to Global tender for each Task using probably using outsourcing 
websites (payment on deliverables or agreed milestones).
4.    Coding done using my Terminal server.
5.    Manage coding pactice, the meeting of timeframes, quality of 
deliverables, documentation practices etc, using VoIP, video conferencing, 
and remote control of RDP sessions, personally.

Anyone interested at this level is welcome to make contact. Please be aware 
that without support of the userbase that this project will be all over 
within the next 6-8weeks as I won't have justified the purchase of the 
development tools.

Comment to help me assess if the project is indeed feasible would be greatly 
appreciated.

Thanks in Advance.

Greg
```

#### ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-15T18:58:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192499904.272716.5990@v23g2000prn.googlegroups.com>`
- **In-Reply-To:** `<4713eb53$1@news.orcon.net.nz>`
- **References:** `<4713eb53$1@news.orcon.net.nz>`

```
I've done Microfocus Cobol conversion and I knew certain issues.

To top it all, you have to focus mainly on "DataFile Conversion" from
16bit to 32bit. 16bit generated Cobol files ARE NOT compatible with
your NetExpress V5.00. So what you'll going to do is basically (a)
create a program based on your 16bit Cobol compiler and read ALL Cobol
datafiles into a flatfile and (b) create a program based on your
NetExpress V5.00 or 32bit Cobol compiler and read the flatfiles back/
write this time to 32bit datafiles.

As long as you have your file structure (or COPY files) intact, then
it will be no problem in data conversion. Concerning Cobol program
codes, nothing much is changed. Once your data conversion is done, you
could play with it using your "new" compiled 32bit Cobol programs. You
would probably need some compiler directives but for sure it would
only consist of at least 10% of the Cobol code change workload.

90% goes to DataFile Conversions.

Best of luck!

Rene
```

##### ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** "news" <greg@primesoft.co.nz>
- **Date:** 2007-10-16T22:18:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<471482db@news.orcon.net.nz>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com>`

```
Thanks Rene

I converted the first module and it seems to read and write to some test 
ISAM files produced by the 16bit version. What symptoms of failure am I 
likely to get?

We did a similar process to what you describe when we added the century to 
dates when the year 2000 clicked over. If we have to I guess we can do it 
again but I'd prefer not to.

Regards
Greg


"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1192499904.272716.5990@v23g2000prn.googlegroups.com...
> I've done Microfocus Cobol conversion and I knew certain issues.
>
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-16T07:02:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13h9a2emejja115@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz>`

```
news wrote:
> Thanks Rene
>
…[7 more quoted lines elided]…
>

I don't know what symptoms of failure you're likely to get, but I bet 
there'll be some. At a minimum, the 32-bit version won't be able to use all 
it's nifty internal stuff against an older rendition. For example, our 
32-bit ISAM creates SMALLER files than the flat file used in its creation!

We had to do the same thing: 16-bit ISAM files (Realia) to a 32-bit system 
(Fujitsu). We couldn't read the input files directly, so we had to go 
ISAM-FLAT-ISAM. The conversion was trivial.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-16T20:08:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qT8Ri.162189$6L.29256@fe03.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <13h9a2emejja115@news.supernews.com>`

```
Check the FILE-TYPE and INXFORMAT directives.  Micro Focus provides upward 
compatibility for all index file types - back to Level II (1980's compiler). 
Although the "default" and the "most efficient" may (or may not) be the same 
from the 16-bit Microsoft Product to the current 32-bit Micro Focus product, MF 
certainly DOES provide compatibility - if that is your goal.

FYI, in the online documentation there is a LONG list of all the directives that 
can impact file-handling.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-16T20:11:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192590690.178752.314350@y27g2000pre.googlegroups.com>`
- **In-Reply-To:** `<471482db@news.orcon.net.nz>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz>`

```
> I converted the first module and it seems to read and write to some test
> ISAM files produced by the 16bit version. What symptoms of failure am I
> likely to get?

Reading a 16bit DataFile coming from a 32bit NetExpress Cobol program
could "somehow" read ISAM files directly, but it will MESS UP your
index files during updating/writing (direct IO). It will make you
"think" it is possible.... but disaster will come when updating/
writing the indexed files.

> We did a similar process to what you describe when we added the century to
> dates when the year 2000 clicked over. If we have to I guess we can do it
> again but I'd prefer not to.

This is a program code mods. If you have the old conventional PIC 99
(YY) coding, it needs proper monitoring (a lot plus QA/testing)....
especially when interest rates are concerned.

Moving back to your deployment platform, it is very clear to me that
Linux is not the mature enough. As the forum advises, you will end up
searching for "unknown" printer drivers. Might as well focus on
Microsoft OS.

AJAX in Microfocus NetExpress works well. I am going to let you view
our example (link below) that uses pure ASP/AJAX and Microfocus COM
generated program in the background that handles data input/outputs.

http://infowaters.infodynamicsconsult.com

At first, the COM (Cobol component will load in the background, so you
will notice a delay) will initializes and will execute faster on
succeeding request. You could include your own security afterwards.


Rene
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-17T03:18:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I9fRi.137916$zt4.94480@fe08.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192590690.178752.314350@y27g2000pre.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1192590690.178752.314350@y27g2000pre.googlegroups.com...
>> I converted the first module and it seems to read and write to some test
>> ISAM files produced by the 16bit version. What symptoms of failure am I
…[7 more quoted lines elided]…
>

As I stated earlier, I do NOT think you will mess up your files IF you use the 
correct FILE-TYPE and IDXFORMAT directives - that Micro Focus documents as 
"compatible" between the products. (You may need other directives too - 
depending upon what other compression, file-sharing, record-locking, etc) 
features of MF files that you used in the old application - or are using with 
the new one.

As I also said before, you may get performance (and other) advantages by 
UPGRADING to a newer format, but that doesn't mean that you have to.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 5)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-16T20:37:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192592268.307477.280580@v23g2000prn.googlegroups.com>`
- **In-Reply-To:** `<I9fRi.137916$zt4.94480@fe08.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192590690.178752.314350@y27g2000pre.googlegroups.com> <I9fRi.137916$zt4.94480@fe08.news.easynews.com>`

```
> As I stated earlier, I do NOT think you will mess up your files IF you use the
> correct FILE-TYPE and IDXFORMAT directives - that Micro Focus documents as
…[3 more quoted lines elided]…
> the new one.

Yes. I agree.

But you need to include these "$set" compiler directives in all your
Cobol program codes. If you're talking about a HUGE compilations of
Cobol programs (which I think you have) then you need a lot of time in
these stage. And eventually you need the help of Microfocus guys on
how far these compatibilities will go.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-17T03:55:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BIfRi.30450$m81.14206@fe01.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192590690.178752.314350@y27g2000pre.googlegroups.com> <I9fRi.137916$zt4.94480@fe08.news.easynews.com> <1192592268.307477.280580@v23g2000prn.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1192592268.307477.280580@v23g2000prn.googlegroups.com...
>> As I stated earlier, I do NOT think you will mess up your files IF you use 
>> the
…[13 more quoted lines elided]…
>

Update your default ".dir" file - depending on how you are doing the mass 
compile, that isn't very hard.  You probably want to change other compiler 
directive defaults as well - if moving from Microsoft COBOL V5 to Micro Focus 
Net Express V5.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T00:36:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192606602.710777.288200@v29g2000prd.googlegroups.com>`
- **In-Reply-To:** `<1192592268.307477.280580@v23g2000prn.googlegroups.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192590690.178752.314350@y27g2000pre.googlegroups.com> <I9fRi.137916$zt4.94480@fe08.news.easynews.com> <1192592268.307477.280580@v23g2000prn.googlegroups.com>`

```
On Oct 17, 4:37 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > As I stated earlier, I do NOT think you will mess up your files IF you use the
> > correct FILE-TYPE and IDXFORMAT directives - that Micro Focus documents as
…[11 more quoted lines elided]…
> how far these compatibilities will go.

As it is only necessary to use the $set directives in programs thatr
will create the file and other programs will adjust to the the way
that the file has been created then I find your comments are
uninformed.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-16T20:20:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192591222.043970.265630@v29g2000prd.googlegroups.com>`
- **In-Reply-To:** `<471482db@news.orcon.net.nz>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz>`

```
> I converted the first module and it seems to read and write to some test
> ISAM files produced by the 16bit version. What symptoms of failure am I
> likely to get?

Reading a 16bit DataFile coming from a 32bit NetExpress Cobol program
could "somehow" read ISAM files directly, but it will MESS UP your
index files during updating/writing (direct IO). It will make you
"think" it is possible.... but disaster will come when updating/
writing the indexed files.

> We did a similar process to what you describe when we added the century to
> dates when the year 2000 clicked over. If we have to I guess we can do it
> again but I'd prefer not to.

This is a program code mods. If you have the old conventional PIC 99
(YY) coding, it needs proper monitoring (a lot plus QA/testing)....
especially when interest rates are concerned.

Moving back to your deployment platform, it is very clear to me that
Linux is not the mature enough. As the forum advises, you will end up
searching for "unknown" printer drivers. Might as well focus on
Microsoft OS.

AJAX in Microfocus NetExpress works well. I am going to let you view
our example (link below) that uses pure ASP/AJAX and Microfocus COM
generated program in the background that handles data input/outputs.

http://infowaters.infodynamicsconsult.com

At first, the COM (Cobol component will load in the background, so you
will notice a delay) will initializes and will execute faster on
succeeding request. You could include your own security afterwards.


Rene
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T00:33:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192606433.159320.283290@i38g2000prf.googlegroups.com>`
- **In-Reply-To:** `<1192591222.043970.265630@v29g2000prd.googlegroups.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com>`

```
On Oct 17, 4:20 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > I converted the first module and it seems to read and write to some test
> > ISAM files produced by the 16bit version. What symptoms of failure am I
…[6 more quoted lines elided]…
> writing the indexed files.

Having done this several times and never having a problem with doing
so I consider your comment to be uninformed.

> > We did a similar process to what you describe when we added the century to
> > dates when the year 2000 clicked over. If we have to I guess we can do it
…[9 more quoted lines elided]…
> Microsoft OS.

Having had zero problems accessing many different printer types I find
you comment to be uninformed.

Certainly there are 'Winprinters' that are useless, but as these are
designed for casual home use they are of no consequence to business
users.

> AJAX in Microfocus NetExpress works well. I am going to let you view
> our example (link below) that uses pure ASP/AJAX and Microfocus COM
…[8 more quoted lines elided]…
> Rene
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-17T09:06:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ff4jb5$pck$1@reader1.panix.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com>`

```
In article <1192606433.159320.283290@i38g2000prf.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Oct 17, 4:20 pm, Rene_Surop <infodynamics...@yahoo.com> wrote:
>> > I converted the first module and it seems to read and write to some test
…[10 more quoted lines elided]…
>so I consider your comment to be uninformed.

How very curious, Mr Plinston... what you consider to be 'uninformed' I 
consider to be 'formed by experiences other than mine'.

DD
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T11:38:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192646306.345543.15630@i38g2000prf.googlegroups.com>`
- **In-Reply-To:** `<ff4jb5$pck$1@reader1.panix.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com>`

```
On Oct 17, 10:06 pm, docdw...@panix.com () wrote:
> In article <1192606433.159320.283...@i38g2000prf.googlegroups.com>,
>
…[16 more quoted lines elided]…
> consider to be 'formed by experiences other than mine'.

There was no evidence that Rene's opinion was formed by any experience
at all.

In fact he was probably confused. MF Index files may be 'messed up' if
they are simultaneously updated by both 16 bit and 32 bit programs as
these may have different locking strategies for the index blocks. This
is independent of whether they were created by 16 bit or 32 bit
programs, or whether they were 'converted' or 'recreated' or just used
as is.

So Rene's warning is incorrect.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-17T20:47:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rxuRi.162945$Lx1.153723@fe05.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com>`

```
DD,
  I am not certain that I would have used the word "uninformed" but rather 
MIS-informed (or "poor memory")  As I have said in a number of notes, Micro 
Focus documents support for what this person claims will produce messed up 
files. Therefore, I would happily play a game of "I doubt it" with this 
information.  If there were such cases, then I believe that MF would accept this 
as a "product bug" and fix it - and that such cases would have caused much more 
noise than this one person's memory.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-18T09:21:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ff78io$n72$1@reader1.panix.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com>`

```
In article <rxuRi.162945$Lx1.153723@fe05.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>DD,
>  I am not certain that I would have used the word "uninformed" but rather 
>MIS-informed (or "poor memory")

Receiving information, Mr Klein, or using memory are matters of experience... 
no evidence of that, now is there?  Simple sort that I am, my approach to 
such differences is to request further information... but that's just my way.

DD
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-18T09:08:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192723718.011319.268330@q5g2000prf.googlegroups.com>`
- **In-Reply-To:** `<rxuRi.162945$Lx1.153723@fe05.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com>`

```
> DD,
>   I am not certain that I would have used the word "uninformed" but rather
…[5 more quoted lines elided]…
> noise than this one person's memory.

Eventually everyone's doubting about this experience I had. In fact
Microfocus would not even agree it will mess up the indexed (.IDX)
file but rather issue a new patch and that is it. I do not know if it
is fixed though because when I raised this issue with them I already
did "all" of my conversion to a 32bit ISAM files, so what the heck.

Nonetheless this concern of 16bit to 32bit ISAM file should NOT be
taken lightly. Below link will somehow lit a light about it, it should
work.

http://supportline.microfocus.com/mf_kb_display.asp?kbnumber=7727
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-18T17:54:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A5NRi.170765$Lx1.153873@fe05.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com> <1192723718.011319.268330@q5g2000prf.googlegroups.com>`

```
So when you say that MF issued a patch, you are confirming that MF *does* 
support the use (for all types of file access) of 16-bit Indexed files with 
32-bit products.  When a user reported a problem, they accepted it as a problem 
and produce what they thought was the solution. (and that KB article is from 
2003 - so apparently there haven't been any other reports of problems for the 
last 4 years).
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-18T17:56:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w7NRi.156252$zt4.81301@fe08.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com> <1192723718.011319.268330@q5g2000prf.googlegroups.com> <A5NRi.170765$Lx1.153873@fe05.news.easynews.com>`

```
Oh, and I should have added, that KB article reported a FS=39 - so it wouldn't 
have "corrupted" the file at all.  The OPEN would have failed before any I/O 
could have occurred.

Sounds pretty safe to me!!!
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-18T11:09:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192730970.324128.158790@i13g2000prf.googlegroups.com>`
- **In-Reply-To:** `<1192723718.011319.268330@q5g2000prf.googlegroups.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com> <1192723718.011319.268330@q5g2000prf.googlegroups.com>`

```
On Oct 19, 5:08 am, Rene_Surop <infodynamics...@yahoo.com> wrote:
> > DD,
> >   I am not certain that I would have used the word "uninformed" but rather
…[17 more quoted lines elided]…
> http://supportline.microfocus.com/mf_kb_display.asp?kbnumber=7727

That reference is to 'Visual COBOL' which is not the same product as
Microfocus 15bit/Microsoft Cobol which became Server Express. While
Visual COBOL was bought by MicroFocus and suppported by them it does
not use the file systems of the MF products and so any problems are
unrelated to the topic.

In any case it does not indicate that the ISAM index is 'messed up'.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-18T18:27:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NANRi.198228$vo5.59085@fe04.news.easynews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com> <rxuRi.162945$Lx1.153723@fe05.news.easynews.com> <1192723718.011319.268330@q5g2000prf.googlegroups.com> <1192730970.324128.158790@i13g2000prf.googlegroups.com>`

```
Good catch Richard.  I misread the article and thought it was talking about (MF) 
"VisOC" - not (mbp) Visual COBOL.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-18T09:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ff78bb$mvv$1@reader1.panix.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com>`

```
In article <1192646306.345543.15630@i38g2000prf.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Oct 17, 10:06 pm, docdw...@panix.com () wrote:
>> In article <1192606433.159320.283...@i38g2000prf.googlegroups.com>,
…[20 more quoted lines elided]…
>at all.

I don't believe stating my consideration to have been formed solely by 
evidence, Mr Plinston... is there no room for aesthetics in your life?

>
>In fact he was probably confused.

Perhaps he might respond to this on his own, if he sees fit... or perhaps you 
might want to generate the analysis which caused you to establish this as a 
probable function.  Feel free to use both sides of the posting.

DD
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 7)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-18T07:38:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192718299.896702.133570@i38g2000prf.googlegroups.com>`
- **In-Reply-To:** `<1192646306.345543.15630@i38g2000prf.googlegroups.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <ff4jb5$pck$1@reader1.panix.com> <1192646306.345543.15630@i38g2000prf.googlegroups.com>`

```
> In fact he was probably confused. MF Index files may be 'messed up' if
> they are simultaneously updated by both 16 bit and 32 bit programs as
…[5 more quoted lines elided]…
> So Rene's warning is incorrect.

Not at all confused.

Based from my first hand conversion experience, for small (less than
4Mb) ISAM datafiles that doesn't need for an updating (write/
rewrite)... you may use the new 32bit compiled Cobol programs for read-
only. But considering the given requirements, this option is not
adviseable. Better go for a "full" ISAM datafile conversion for future
purposes. Surely, it will mess up you indexed (.IDX) files.

Yes, I did advise based on experience.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-17T05:08:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jalRi.4741$E7.4531@bignews3.bellsouth.net>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> ...
> Certainly there are 'Winprinters' that are useless, but as these are
> designed for casual home use they are of no consequence to business
> users. ...

I don't know about the rest of the world, but about 77% of the workforce
in the U.S. are employed by companies with 20 or fewer employees. Big
business therefore employees less than 1/4 of the workers. Companies buy
computers and printers according to the number of employees who use
them. It is well known that small companies often buy low end products to
save money. Therefore, I find your comments "uninformed." ;-)
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-17T10:21:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13hca2p1ajumg75@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com>`

```
Richard wrote:
>>
>> Moving back to your deployment platform, it is very clear to me that
…[5 more quoted lines elided]…
> you comment to be uninformed.

I recall one chap who testified before Congress regarding the "monopoly" 
status of Microsoft. To him, Windows was a godsend.

He testified (paraphrasing):

"We write high-end application software. We had a room as big as an airplane 
hanger full of printers. Every time we made a modification to our software, 
we had to test it with several hundred devices. Every time a new printer hit 
the market, we had to buy one to make sure our software was compatible. All 
that went away with our Windows version. Now we just hand the data to the 
operating system and concentrate on our application."

It's in the Congressional Record, so it must be true...

But even Windows is not immune. On the Vista newsgroups, there is an 
occassional hand-wringing by some chap with Vista and a piece of antiquated 
junk (usually a scanner, gaming device, or obscure video board) for which 
drivers are not available.

>
> Certainly there are 'Winprinters' that are useless, but as these are
> designed for casual home use they are of no consequence to business
> users.

How so? If they were useless, who would buy them? We've got one here (it 
cost $69) that we use to print CDs (another $60 for the bulk ink 
reservoirs).
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T11:28:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192645734.533093.200160@e34g2000pro.googlegroups.com>`
- **In-Reply-To:** `<13hca2p1ajumg75@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com>`

```
On Oct 18, 4:21 am, "HeyBub" <heybubNOS...@gmail.com> wrote:
> Richard wrote:
>
…[20 more quoted lines elided]…
> It's in the Congressional Record, so it must be true...

That was what, ten years ago, haven't you caught up since then ?

It was also not about Linux, but may have been DOS where the program
had to worry about outputting the correct stream of bytes for the
printer.

CUPS on Linux or Unix has drivers for as many printers as Vista does,
or maybe even more.

> But even Windows is not immune. On the Vista newsgroups, there is an
> occassional hand-wringing by some chap with Vista and a piece of antiquated
…[9 more quoted lines elided]…
> reservoirs).

There are, in fact, many WinPrinters that can be driven directly by
CUPS, such as by OKI or HP where filters are available to do this with
one directly connected. Otherwise they can be on a Windows client and
accessed via Samba or JetDirect or ...
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T11:52:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192647142.941868.248070@i13g2000prf.googlegroups.com>`
- **In-Reply-To:** `<13hca2p1ajumg75@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com>`

```

On Oct 18, 4:21 am, "HeyBub" <heybubNOS...@gmail.com> wrote:

> But even Windows is not immune. On the Vista newsgroups, there is an
> occassional hand-wringing by some chap with Vista and a piece of antiquated
> junk (usually a scanner, gaming device, or obscure video board) for which
> drivers are not available.

It is not just 'ancient junk' but many newer devices have no Vista
drivers. And not just 'obscure' ones, some HP printers (even
WinPrinters) have no drivers for Vista.

"""Dell 540 	Photo Printer 	There is no Windows Vista printer driver
available for this product. For more information on usage limitations
for a 540 printer running Windows Vista, refer to the following
Knowledge Base Article: "Usage limitations for a Dell Photo Printer
540 running Microsoft� Windows Vista�." Article ID: 309259
Dell J740 	Color Inkjet 	There is no Windows Vista printer driver
available for this product."""

""" Lexmark P6210 (All In One Printer) - No Drivers For Vista Yet"""

"""No HP Drivers for the color laser 4550 or the laserjet 1000 series
for VISTA.. what joy"""
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-17T14:23:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FitRi.5169$E7.34@bignews3.bellsouth.net>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
>
> It is not just 'ancient junk' but many newer devices have no Vista
…[14 more quoted lines elided]…
> for VISTA.. what joy"""

All I have to say to that is, what maniac at Microsoft decided to break
the Windows XP printer drivers in Vista?
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-17T14:32:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1192656772.007001.107820@e34g2000pro.googlegroups.com>`
- **In-Reply-To:** `<FitRi.5169$E7.34@bignews3.bellsouth.net>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net>`

```
On Oct 18, 8:23 am, "Judson McClendon" <ju...@sunvaley0.com> wrote:
> "Richard" <rip...@Azonic.co.nz> wrote:
>
…[18 more quoted lines elided]…
> the Windows XP printer drivers in Vista?

A cynic may note that end users are not 'Microsoft's Customers', those
are the OEMs and manufacturers. To keep their customers happy MS
needed to ensure that computer buyers needed to spend much more money
on higher spec equipment and replacement peripherals, otherwise with
the generally falling prices and MS wanting more money for Vista it
will be an even higher proportion of the total revenue being skimmed
off by MS and lower profit margins for the rest.

I just put together a simple Windows box for a client and with OEM XP
Pro not only was this the most expensive single component, it was
twice that of the next expensive (the dual core CPU). Obviously the
Dells and Gateway get much better prices than I do, but it must seem
to them that they could make better profit selling Linux machines at
half the price (due to lower spec requirements as well as lower
software cost).

Now that Dell is selling Linux openly they are already pushing the
printer and graphics card suppliers to write better drivers. Still, my
Nvidia GPU works fine.

OTOH it may be that Directx 10.1 will break many allegedly Vista
compatible graphics cards.

"""Here's the thing. DX10 hardware - such as the GeForce 8800 or the
Radeon 2900 - won't work with the new 10.1 features. The 0.1 revision
requires completely new hardware for support, thus royally cheesing
off many gamers who paid top whack for their new hardware over the
last few months on the basis of future game compatibility."""
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-17T20:16:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k4adh39ljcbcr420en0oq2v6866lqedmh9@4ax.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net>`

```
On Wed, 17 Oct 2007 14:23:28 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Richard" <riplin@Azonic.co.nz> wrote:
>>
…[18 more quoted lines elided]…
>the Windows XP printer drivers in Vista?

Vista (x64) requires kernal-mode drivers to have a digital signature. XP allowed unsigned
drivers. A kernel-mode program can do ANYthing, including modify the operating system.
Even worse, it can give you a clear (unencrypted) copy of DRM material, from which you
could make pirated copies. Oh the horror. 

Hacking your computer is one thing; copying Shrek II cannot and will not be tolerated.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** bill@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2007-10-18T13:58:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5np739Fj9cnmU1@mid.individual.net>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net>`

```
In article <FitRi.5169$E7.34@bignews3.bellsouth.net>,
	"Judson McClendon" <judmc@sunvaley0.com> writes:
> "Richard" <riplin@Azonic.co.nz> wrote:
>>
…[18 more quoted lines elided]…
> the Windows XP printer drivers in Vista?

It isn't printer drivers.  There are more differences than similarities
between XP and Vista.  for example, the whole GINA method was changed.
(Actually, one has to wonder if this is a matter of change or just the
fact that one is not based on the other beyond conceptualy.)

bill
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 8)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-10-22T19:52:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RpSdnelhT8Z6zoDanZ2dnUVZ_umlnZ2d@comcast.com>`
- **In-Reply-To:** `<FitRi.5169$E7.34@bignews3.bellsouth.net>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net>`

```
Judson McClendon wrote:
> All I have to say to that is, what maniac at Microsoft decided to break
> the Windows XP printer drivers in Vista?

Vista requires signing - no more of this "I know it's unsigned, but 
install it anyway."  (You can turn that off, but that affects the entire 
OS, not just that driver.)  There's also now a push for vendors to 
support 64-bit drivers - I tried XP-64 and removed it because there were 
no drivers.  Lack of a video driver in Vista 64-bit is why Ubuntu is on 
this computer now.  When we got my wife's new computer (Dual AMD 64, 
Vista 64-bit), Kodak had no drivers for their photo printer.

It's a conscious decision, because drivers now must respond to remote 
revocation.  Steve Gibson (the SpinRite guy) does a podcast called 
Security Now, and when Vista was about to drop, he did two shows on the 
differences and "new" features of drivers.  It's on http://www.twit.tv , 
from back in January I believe.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 9)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-10-23T13:18:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193170725.055603.247310@v23g2000prn.googlegroups.com>`
- **In-Reply-To:** `<RpSdnelhT8Z6zoDanZ2dnUVZ_umlnZ2d@comcast.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net> <RpSdnelhT8Z6zoDanZ2dnUVZ_umlnZ2d@comcast.com>`

```
On Oct 23, 2:52 pm, LX-i <lxi0...@netscape.net> wrote:
> Judson McClendon wrote:

> It's a conscious decision, because drivers now must respond to remote
> revocation.

Microsoft wants to be able to turn your computer into a brick.

Think of how this will increase their revenue. Every year MS can brick
your computer so that you have to go out and buy a whole new system.

http://slashdot.org/articles/07/10/23/1255235.shtml
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 10)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-23T16:02:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13hsobfmcr1le08@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net> <RpSdnelhT8Z6zoDanZ2dnUVZ_umlnZ2d@comcast.com> <1193170725.055603.247310@v23g2000prn.googlegroups.com>`

```
Richard wrote:
> On Oct 23, 2:52 pm, LX-i <lxi0...@netscape.net> wrote:
>> Judson McClendon wrote:
…[9 more quoted lines elided]…
> http://slashdot.org/articles/07/10/23/1255235.shtml

Maybe so, but it's a MICROSOFT brick and therefore a good brick.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-10-23T20:13:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382dnas9JK_cN4PanZ2dnUVZ_jqdnZ2d@comcast.com>`
- **In-Reply-To:** `<1193170725.055603.247310@v23g2000prn.googlegroups.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <1192499904.272716.5990@v23g2000prn.googlegroups.com> <471482db@news.orcon.net.nz> <1192591222.043970.265630@v29g2000prd.googlegroups.com> <1192606433.159320.283290@i38g2000prf.googlegroups.com> <13hca2p1ajumg75@news.supernews.com> <1192647142.941868.248070@i13g2000prf.googlegroups.com> <FitRi.5169$E7.34@bignews3.bellsouth.net> <RpSdnelhT8Z6zoDanZ2dnUVZ_umlnZ2d@comcast.com> <1193170725.055603.247310@v23g2000prn.googlegroups.com>`

```
Richard wrote:
> On Oct 23, 2:52 pm, LX-i <lxi0...@netscape.net> wrote:
> 
…[3 more quoted lines elided]…
> Microsoft wants to be able to turn your computer into a brick.

I don't think that's the case...  :)

> Think of how this will increase their revenue. Every year MS can brick
> your computer so that you have to go out and buy a whole new system.
> 
> http://slashdot.org/articles/07/10/23/1255235.shtml

This is the whole thing with "activation" that Microsoft had to come up 
with to try to defeat pirates.  You've got 3 days to get the thing 
re-activated (which you don't have to pay for - you just call them (or 
maybe e-mail, I don't know) and tell them what happened).

What I was talking about was an HD driver that is flawed, so as to 
deliver unencrypted HD content.  That's what "driver revocation" is 
supposed to cover.

Doesn't bother me too much - they could revoke every driver tomorrow, 
and my Ubuntu box would keep chuggin' along...  :)
```

#### ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-16T00:54:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz>`

```
On Tue, 16 Oct 2007 11:32:09 +1300, "news" <greg@primesoft.co.nz> wrote:

>I'm looking for comment on any issues I may encounter in a conversion for 
>Microsoft COBOL V5 (Which was licenced off Micro Focus) and Version 5 of Net 
…[8 more quoted lines elided]…
>There are between 500,000 and a million lines of code (Is that large?)

Yes, that's large.

>There are about 100 installations of the 16 bit version of the system.
>Companys using it range from NZ$400M turnover to $100K turnover (What New 
…[10 more quoted lines elided]…
>but not fully tested)

If you have one program with 100,000 lines of code, you have serious structural problems
that need to be remedied before attempting 3-6 below. 

>I now have to assess cost of several logical phases. i.e. assess the min and 
>max cost possible for each phase - This is where any issues I need to 
…[10 more quoted lines elided]…
>would no longer get these symptoms.

Very easy. It's just a recompilation. You don't need phases. 

Converting data files is just a reorg. You don't need to change data elements in your
records. 

>2.    Write a module to replace ASSIGN PRINTER to handle printed output.

Many printer drivers that can do what you want without changing source code.

3. Refactor programs to reasonable size, one function per callable program. Separate user
interface from application logic. 

>7.    Port to a relational database (Probably Postgres)  for easier 3rd 
>party reporting.

I would make this 4. First, move file IO into data layers. Second, design the database ..
properly (normalized), NOT one table per indexed file. Third, rewrite data layers to read
the database and return 'logical views' matching indexed files one for one. 

Having done 1, 3 and 4, you have a foundation to build on.

>3.    Write a web interface using Net Express and hopefully AJAX to replace 
>the screen I/O of the current version. Duplication of look and feel of 
>exsisting interface envisagaged. Compile as a .Net application.

Easier than you think .. AFTER user interface is separated from business logic.

>4.    Port to Linux using MONO (.NET framework for Linux)

Why? Unix GUI isn't as good as Windows.

>5.    Revisit the user interface (3.) altering bigger sections of underlying 
>business logic to enable us to produce a "prettier" more flexible interface. 
>Possible conversion of some code to Object orientated code.

People will tell you to do the user interface with Java oriented tools 

>6.    Alter Code to handle security for system to run as a web application 
>in a bureau environment.5. & 6. may occur simultaneously.

Do it yourself security is almost always third rate. Security should be outside
application code, primarily in the database. That's one reason why you first need a
database.

>Progammer Strategy
>
…[7 more quoted lines elided]…
>and remote control of RDP sessions, personally.

You overlooked testing, which will be more expensive than coding. You overlooked design,
as well. 

>Anyone interested at this level is welcome to make contact. Please be aware 
>that without support of the userbase that this project will be all over 
>within the next 6-8weeks as I won't have justified the purchase of the 
>development tools.

Show them mockups of pretty GUI screens with searchable lists and reports as spreadsheets.
They'll fall in love.
```

##### ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** "news" <greg@primesoft.co.nz>
- **Date:** 2007-10-16T23:09:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47148ec3$1@news.orcon.net.nz>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com...
> On Tue, 16 Oct 2007 11:32:09 +1300, "news" <greg@primesoft.co.nz> wrote:
>
…[14 more quoted lines elided]…
> Yes, that's large.
Hmmm, thats what I Thought. I guess 20 odd years of coding makes for a bit 
of a mammoth conversion task.
>
>>There are about 100 installations of the 16 bit version of the system.
…[16 more quoted lines elided]…
> that need to be remedied before attempting 3-6 below
The suite is made up of over 200 executables which draw on over 600 copybook 
files for reusable code.
I'm hoping a complete restructure isn't in order or this project won't fly.
>
>>I now have to assess cost of several logical phases. i.e. assess the min 
…[25 more quoted lines elided]…
> code.
My goal is if it prints from windows it also prints from my programs. 
However as I want to port it to linux it will have to take this into account 
in design.
>
> 3. Refactor programs to reasonable size, one function per callable 
> program. Separate user
> interface from application logic.
See above this may already be the case.
>
>>7.    Port to a relational database (Probably Postgres)  for easier 3rd
…[14 more quoted lines elided]…
>>exsisting interface envisagaged. Compile as a .Net application.
Possibly, but I need the users to get something in a timely fashion with a 
low risk of introducing bugs. This strategy would seemingly suck a lot of 
cash on testing before I could get the new code generating any new revenue.
>
> Easier than you think .. AFTER user interface is separated from business 
…[4 more quoted lines elided]…
> Why? Unix GUI isn't as good as Windows.

Because Linux has a big chunk of the server market. E-commerce is expanding, 
If I can provide the reliabilty and stability of a COBOL based financial 
system for e-commerce systems to write to directly I believe there will be a 
market for it.I can provide poit of sale through to Balance Sheet on one box 
with one core business logic.
I don't ever intend to design a non-webform version of this software. I 
intend to leapfrog that technology and never offer it to the market at all. 
As far as I'm aware, the browsers available for linux are in many ways 
superior to those in windows, particularly in security. At the end of the 
day whilst everyone likes "Pretty" most serious business people will opt for 
solid and functional when trusting their financial transactions to a 
computer system.

>
>>5.    Revisit the user interface (3.) altering bigger sections of 
…[5 more quoted lines elided]…
> People will tell you to do the user interface with Java oriented tools
AJAX is a java orientated tool. I'm yet to figure if I can get it to work 
with Net Express
>
>>6.    Alter Code to handle security for system to run as a web application
…[6 more quoted lines elided]…
> database.
This step was not necessarily to be coded using COBOL. My thoughts were more 
based around Linux and is ability to secure the ISAM data files as part of 
the registration process of signing up to the web service. This may or may 
not be done via COBOL. The code I envisaged would simply look to a different 
directory for the datafiles depending on which user was logged in.
>
>>Progammer Strategy
…[12 more quoted lines elided]…
> as well.
Typically I do that bit and pay myself stuff all. :(
>
>>Anyone interested at this level is welcome to make contact. Please be 
…[7 more quoted lines elided]…
> They'll fall in love.

They are so used to the console interface that many have threatened me with 
death if I change it. :)
We are talking of Java enabled Cellphones sending XML data to the linux 
server (I mentioned earlier) to load Payroll transactions and automated SMS 
messaging from that server to communicate job locations and descriptions 
organising casual remote workers. That seemingly has them excited if not in 
love! Can't really be done without new tools!

Thanks for taking the time to reply you have given me a bit more to think 
about.
>
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-16T07:37:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13h9c4vc165qvc2@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com> <47148ec3$1@news.orcon.net.nz>`

```
news wrote:
>>
>>> 2.    Write a module to replace ASSIGN PRINTER to handle printed
…[6 more quoted lines elided]…
> account in design.

Good God, why? One of the benefits of moving to Windows was many of our 
compatibilty problems disappeared. We no longer care what kind of printer or 
modem or whatever is connected; we build a print line and hand it to Windows 
to sort out.

Linux has about 1/100 of the drivers for hardware that Windows has. Hardware 
vendors often don't even bother with Linux drivers.

Users don't want to have to hire a 17-year old computer nerd to keep their 
system running. If you try to peddle a commercial system based on Linux, you 
automatically double the amount of service calls you can expect to receive.

If you want to piss around for your own enjoyment fiddling with Linux, 
that's okay. But if you try to inflict Linux on a user, you're doomed. 
DOOMED, I say.

(The fact that I own a wheelbarrow full of Micros~1 stock has no bearing on 
this assessment.)



>>> 3.    Write a web interface using Net Express and hopefully AJAX to
>>> replace
…[25 more quoted lines elided]…
> financial transactions to a computer system.

Nonsense. Linux does have a recognizable share of the server market and will 
continue to grow. Right now, it's about 25% (according to PC week), but 
that's a smallish minority of the server market. Might as well be writing 
code for the Macintosh.

In my view, betting the company on Open Sores operating systems is an 
unnecessary gamble.


Other thoughts:

1. Moving to a GUI system will probably throw a big twist in the way you 
design your programs. Some programs will be junked entirely and re-written 
from scratch. This is because many things are SO much easier in Windows, 
you'll say "I gotta have me some of that!" Perhaps many existing modules 
dealing with various hunks of hardware (printers, modems, scanners, etc.) 
will be scrapped because all those functions are now the responsibility of 
the OS.

2. You'll find that calling on the OS to perform many tasks is a godsend. 
Giant sections of exiting code will be tossed in the can and replaced with 
one call to an API.

3. The logic of your programs will change. Many events will be occuring 
simultaneously (updating a file, mouse movements, button pushes...) all 
coming in at random times and you'll have to re-think your logic from 
sequential processing to event-driven control. Once you get past the 
barrier, it's automatic, BUT a straight sequential processing stream can get 
terribly confused when the user taps the "Pause" button.

4. The features you can offer will increase dramatically. One example: In 
our system, a clerk records a special order for a customer. This special 
order percolates through the system and eventually a box arrives from the 
vendor. As the employee is checking in the shipment, the system 
automatically sends an email to the original customer telling him his order 
has arrived! Sending an email via DOS would be like pulling teeth; in 
Windows, it's trivial.

You will need a programmer versed in Visual Basic. You will need to re-learn 
installation tools for your software. You will have to shop for Active-X 
add-in controls.

It won't be easy, but what's art without suffering.
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-10-16T12:12:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tk6Ri.280$f06.275@newsfe14.lga>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com> <47148ec3$1@news.orcon.net.nz> <13h9c4vc165qvc2@news.supernews.com>`

```

HeyBub <heybubNOSPAM@gmail.com> wrote in message
news:13h9c4vc165qvc2@news.supernews.com...

>
> 3. The logic of your programs will change. Many events will be occuring
…[3 more quoted lines elided]…
> barrier, it's automatic, BUT a straight sequential processing stream can
get
> terribly confused when the user taps the "Pause" button.
>


You know, this is something of a programming "urban myth".  Event-oriented
programming isn't something absolutely and "if-and-only-if" associated with
GUI programming.  If "News"'s systems are screen-driven then he's doing
event-oriented (EO) already.   Even if you have only the display & accept
verbs available you can do a crude rendition of EO.  All that's needed is to
write your program so as to assume something independent to handle the
screen-io functions (which all modern Cobol implementations provide); pass
on a message or a screen to the handler, set switches so you know where you
were and what you were doing in the program, then wait for something to come
back.  Your programming action will then depend on what you get and what
switches were set.  You certainly CAN program so as to have events happen in
a strict sequence in this environment - but so can you in any GUI
environment.

As well, many of the possible actions a user may take concern the screen but
not the underlying program.  I've yet to come across a situation where the
underlying program has to know about the window being resized or moved, for
instance; or about the mouse being moved.  That's the business of the screen
handler.  All the program needs to worry is about the data that gets sent to
it (including button pushes or scrolling selections or whatever).

I've been doing this sort of programming for eons.  Older followers of this
group that worked with Univac gear may remember TMS that ran on OS/4.  That
certainly qualified as EO - character-oriented green screens and 2400 baud
lines and all!

So: the PAUSE button: please give me an example of its use in a data-entry
screen!

Cheers
PL
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 5)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-16T15:47:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ha8ris55j51ee@news.supernews.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com> <47148ec3$1@news.orcon.net.nz> <13h9c4vc165qvc2@news.supernews.com> <tk6Ri.280$f06.275@newsfe14.lga>`

```
tlmfru wrote:
> HeyBub <heybubNOSPAM@gmail.com> wrote in message
> news:13h9c4vc165qvc2@news.supernews.com...
…[41 more quoted lines elided]…
> data-entry screen!

It's not an urban myth. It's not even a programming myth. In a screen full 
of controls, when one is selected, that's an "event." Another event may be 
selected that modifies the first event.

Say:
Exiting a field triggers data evaluation logic. Meanwhile, the cursor 
proceeds to the next field. The data validation logic on the first field 
detects and error and informs the user. After the user acknowledges the 
error condition, focus is returned to the first field. This triggers a lost 
focus event on the second field which triggers the data validation logic for 
the second field and so on...

Unless the programmer knows how these events are being aligned, much hair 
will be pulled.

There's dozens of these "gotchas" that batch programmers, even CICS 
programmers, are not familiar with.

As to an example of PAUSE being used in a data-entry screen, how about a 
look-up feature that finds millions of records?
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

_(reply depth: 6)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-10-16T20:07:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nidRi.423$uk.139@newsfe21.lga>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com> <47148ec3$1@news.orcon.net.nz> <13h9c4vc165qvc2@news.supernews.com> <tk6Ri.280$f06.275@newsfe14.lga> <13ha8ris55j51ee@news.supernews.com>`

```

HeyBub <heybubNOSPAM@gmail.com> wrote in message
news:13ha8ris55j51ee@news.supernews.com...
> tlmfru wrote:
> > HeyBub <heybubNOSPAM@gmail.com> wrote in message
…[31 more quoted lines elided]…
>

<snip>

> Say:
> Exiting a field triggers data evaluation logic. Meanwhile, the cursor
> proceeds to the next field. The data validation logic on the first field
> detects and error and informs the user. After the user acknowledges the
> error condition, focus is returned to the first field. This triggers a
lost
> focus event on the second field which triggers the data validation logic
for
> the second field and so on...
>
…[9 more quoted lines elided]…
>

No, no, Hey, you're missing my point.  I'm quite aware of this and other
situations and have gone along with the "best practice" rules whether I
liked them or not.  (My absolute non-favourite was that enabling a field in
one GUI environment would generate a lost-focus event for ALL previous
buttons, fields, etc., on the screen).  I was trying to demonstrate that
"event-oriented" and "GUI" are not the same thing, and that you don't
require the latter to do the former.

If the lookup finds millions of records - well, every one I've ever worked
with had a maximum number that it would display at once - and had a cancel
button.

PL
```

###### ↳ ↳ ↳ Re: Stategy for (Large?) 16bit COBOL code conversion to Net Express

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-17T00:05:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q3vah3hrlbj5vf0j624lb6rssujbhqutat@4ax.com>`
- **References:** `<4713eb53$1@news.orcon.net.nz> <7hh8h358vkj137oeocabhvd5ausrqp2kgj@4ax.com> <47148ec3$1@news.orcon.net.nz>`

```
On Tue, 16 Oct 2007 23:09:26 +1300, "news" <greg@primesoft.co.nz> wrote:

>
>"Robert" <no@e.mail> wrote in message 
…[40 more quoted lines elided]…
>files for reusable code.

Now the average program size is down to 4,000 lines, which is high-average for programs
written in the 1980s. That's not horrible, like 100,000 lines, but is still too big.

When they say reusable code, they mean procedural code, not data structures. Outside OO,
reusable code is written as callable functions. 

>I'm hoping a complete restructure isn't in order or this project won't fly.

No, just repackaging. Package logical chunks of code as callable programs, with special
attention of file IO and user interface. Those are the programs you're going to rewrite as
database and GUI, respectively. 

>>>I now have to assess cost of several logical phases. i.e. assess the min 
>>>and
…[27 more quoted lines elided]…
>in design.

Windows' printer interfaces are much more sophisticated then Unix's. It is very common to
have the business logic on Unix and the user interface on Windows. A printer is as much a
user interface device as a screen. Middleware ties the front and back ends together. Well
known examples are WebSphere, J2EE, JBoss, TIBCO, Weblogic and Struts. If you like .net,
use ADO.

Do not try to do it yourself with first generation approaches like RPC, or even Samba or
NFS. 

>> 3. Refactor programs to reasonable size, one function per callable 
>> program. Separate user
…[30 more quoted lines elided]…
>Because Linux has a big chunk of the server market. 

You mean Unix, not Linux. That's true, but Unix is seldom used for user interface (except
on Apple). I work on very large Unix servers for F-100 companies, and I've never seen KDE
or GNOME used to interface with human beings, only with developers. :) The GUI world used
to be owned by Windows, is now owned by Web pages written with Java tools such as J2EE.

>E-commerce is expanding, 
>If I can provide the reliabilty and stability of a COBOL based financial 
>system for e-commerce systems to write to directly I believe there will be a 
>market for it.I can provide poit of sale through to Balance Sheet on one box 
>with one core business logic.

There are many BAD point of sale systems in the world, fewer than a dozen good ones. 

I've seen elegant integrated systems that start with a balance sheet, let you drill down
to accounts receivable, down to customers, down to invoices, down to line items ... all
threaded together with a unified audit trail such as a keyrec number. It looks good in
demos, but the real measure of utility is in the gritty details.

>I don't ever intend to design a non-webform version of this software. I 
>intend to leapfrog that technology and never offer it to the market at all. 
…[4 more quoted lines elided]…
>computer system.

Well said. By the same token, they don't judge a system by its browser security, either.
Leave that to magazines. 

>>>5.    Revisit the user interface (3.) altering bigger sections of 
>>>underlying
…[20 more quoted lines elided]…
>directory for the datafiles depending on which user was logged in.

ISAM data files!! Be serious. A schema is the database equivalent of a directory; a table
is equivalent to a file. Databases have security not only at those two levels, but also at
the individual field within a record. Some users can see salaries, others cannot. Some can
update salaries, others cannot. With security in the database, rather than application
code, no one can bypass it by using general purpose tools nor by writing a program.

>>>Progammer Strategy
>>>
…[12 more quoted lines elided]…
>Typically I do that bit and pay myself stuff all. :(

Development plans emphasize the things a company is good at and/or believes important, and
deemphasize the others. The development plan DOES NOT CHANGE REALITY. By reducing testing
to a single line item and giving it a small time/money budget doesn't reduce the need for
testing, it means you'll deliver a poorly tested system. Some companies go the other way.
They spend 90% of their time and money on planning, process control and testing, while
sweeping development under the rug. They wind up with software that's technically weak,
but well documented. 

Where do you want the errors to be? They will be found wherever you 'saved money' or
couldn't be bothered. If you want high-level design errors, design on the back of an
envelope. 

>>>Anyone interested at this level is welcome to make contact. Please be 
>>>aware
…[14 more quoted lines elided]…
>love! Can't really be done without new tools!

Apparently you think CCXML and VoiceXML is the best or only way to communicate with mobile
users. 

Generally, there are two competing network technologies: telephony and computer (IP). The
XML ones originated in the telephony side (bet you didn't know that). As a result, they
depend on centralized control (SS7, telco switches) and metered pay per use, because
that's how telephone people think.

Competing technologies from the computer side are SIP/RTP and I.323. That's how VoIP
phones work. At a low level they're carried as UDP packets, usually on the internet or
VPN. Both can send text messages, voice and video to any COMPUTER, telephone or IP-capable
speaker or screen. Your users do have computers. The phone company doesn't want you
talking to computers. 

An emerging technology, independent of those those two, is Jabber/XMPP, which is pure
internet. Google has added significant functionality to the Standard with its own flavor,
called Jingle. Don't laugh. Google is serious, and we know they'll own the world in 20
years. Google offers a FREE library that can dance circles around SIP/RTP, talking over
the FREE internet. 

When the telephone company salesman tells you "XML will do for voice what HTML did for
screens" he's just selling phone services. The computer-based approaches are more
liberating.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
