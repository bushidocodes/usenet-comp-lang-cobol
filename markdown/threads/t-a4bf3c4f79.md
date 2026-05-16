[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Various "debuggin" tools (for IBM mainframe development)

_3 messages · 3 participants · 2005-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Various "debuggin" tools (for IBM mainframe development)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-04T05:50:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0iIe.820839$ub.287481@fe07.news.easynews.com>`

```
As a follow-up on another thread, let me state that I did work for Micro Focus 
(until I went on long term disability - about a decade ago).  However, I worked 
for ADS the originator of the Xpediter family of products before that - and did 
both training and systems programming for a "major utility" using IBM mainframe 
COBOL and tools before that.  During much of my "mainframe support" time, I was 
also active in GUIDE (COBOL project) and currently am the requirements 
coordinator for both the LNGC (where COBOL, LE, and PL/I live) and APEN project 
(where Debug Tool, Fault Analyzer, etc live).

I personally (not getting paid by anyone these days) think that almost every 
type of "development" tool (at least for IBM mainframe development) has PROs and 
CONs.  One of the things that I think (but won't swear to it) that is relatively 
different about the IBM mainframe COBOL environment and the COBOL environment 
elsewhere and other language development environments is the HUGE number 
(historic and current) of "3rd party" and "add-on" products for debugging 
(static and dynamic), optimizing,  etc.  Chuck can certainly correct me if he 
know of lots for Unisys - and others certainly may know of tools for HP, Dec 
(when they existed), etc.

My first experience with (IBM) mainframe COBOL was with OS/VS COBOL (although I 
did later have some contact with ANS COBOL V2 - thru V4).  Almost EVERY shop 
that I ever dealt with "owned" the CAPEX (then CA-Optimizer) add-on product to 
improve performance for that compiler.  Additional common tools included:
  Abend-Aid (static debugging)
  Dumper (then File-Aid) - test data generation
  Xpediter, Intertest, ViaTest, etc for interactive debugging
  TESTCOB (then COBTEST, then CODE/370, then Debug Tool) from IBM for 
interactive debugging - but all "add-on" products
  BTS (IMS interactive and batch debugging)
  CEDF (CICS interactive debugging)
     and many, MANY, more

Realia (then CA-Realia) was initially (as far as I could ever tell - but I could 
be mistaken on this) was primarily for IBM mainframe development.  Although 
Micro Focus *started* out for non-IBM mainframe development, by the time of 
"COBOL'/2" and "Workbench" this was a majority of their revenue source.  Fujitsu 
actually GOT the source code for OS/VS COBOL and (initial releases) of VS COBOL 
II - because of the "odd" IBM/Fujitsu deals and separation contracts.

The following just the BEGINNING of some of the issues that I tell people to 
think about when considering a testing and development plan.  (Those considering 
MOVING from an IBM mainframe to another *production* environment have - IMHO - 
another set of issues to consider).

Is testing with IBM product's and compilers *THE* solution to all your 
problems/issues?
    GOOD
Certainly using the same compiler for testing and production saves many problems
Using "test files" (and databases) on the mainframe itself often solves problems 
too.
Their "remote debugging" tools have come along way from their original releases

   BAD
IBM no longer supports any debugging tools for OS/VS COBOL code (unlike, 
Xpediter, Intertest, Micro Focus, etc)
IBM *requires* TEST and NOOPT for their interactive debugging tools (which is 
rarely what is used in production, so you STILL have to recompile and re-test 
before production)
IBM's workstation products (VisualAge COBOL and WSED) don't support mixed 
Assembler & COBOL - very common in many/most mainframe shops.  (They also don't 
support CMPR2 - but isn't a big deal for most shops today)
Do you have the mainframe "power" to have dedicated test regions, TSO sessions 
running interactive debuggers, etc (some shops do - some don't)

   ***

Is using a 3rd party mainframe interactive tool the "ultimate solution"?
   GOOD
- I think that the Xpediter family of products provides an excellent "common 
look and feel" for debugging complex ILC applications with most combinations of 
languages, databases, transaction processors, etc
 - Xpediter provides at least SOME debugging support for "OPT" code.
 -Ease of installation and use have improved with each release.  (Still not 
"self-evident" to those who don't get sufficient training - from what I hear).
 - As far as I know (and hear) all the other "major" 3rd party vendors have 
similar advantages over IBM itself - but also have disadvantages (listed below)

  BAD
- Again, you need adequate mainframe resources
- 3rd party vendors are ALWAYS "behind" when IBM introduces new releases (such 
as CICS TS V3.1 - and Enterprise COBOL V3.4)
 - Some 3rd party products require "hooks" into the system that Auditors would 
DIE if they really understood
 - PRICE !!! (Which is worse? Compuware or CA?  I think they compete for this 
<G>

    ***

Are 3rd party "Workstation" development tools the "silver bullet" that will 
solve all your development problems?
   GOOD
- No (or minimal) mainframe resources required
- No "waiting" for SysGens or other changes to "test systems" (no chance of 
bringing down an entire test region)
- Continued support for OS/VS COBOL and better support for Assembler (on the 
Workstation) than IBM itself
- Much improved (over years ago) access to test data ON the mainframe while 
doing development on the Workstation

  BAD
- Again, 3rd party products are always behind mainframe releases
- Every programmer needs to be a "mini-SysProg" to set up individual systems (or 
"projects" need them for server-centric development platforms
 - "Big" clients (and squeaky wheels) get all the attention (in my experience) 
and what they ask for to be enhanced is what gets enhanced
 - PRICE  (How many workstation development stations can you buy for the cost of 
a new testing mainframe LPAR?)

   *********

Bottom-Line:
  Although I have a lot of experience (and history) with both mainframe and 
workstation products targeted at the IBM mainframe developer, I have yet to see 
a SINGLE product that "solves" all the problems of development (and which 
doesn't need some improvements).  However, I (personally) like to see criticism 
and comments based on what vendors are doing (and not doing) today - and not 
based on what did (or didn't) work 5, 10, or 20 years ago.

It is remarkable (to me) how many GREAT tools there are to make life "easy" (or 
at least easier) for IBM mainframe COBOL (and other language) application 
programmers - especially when I compare these to the tools for some other 
environments that I know about.  However, anyone considering a new product (or a 
change in products) really does need to hear both the good and the bad about the 
products in question.
```

#### ↳ Re: Various "debuggin" tools (for IBM mainframe development)

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T06:47:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9SiIe.49939$t43.38986@tornado.tampabay.rr.com>`
- **References:** `<c0iIe.820839$ub.287481@fe07.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:c0iIe.820839$ub.287481@fe07.news.easynews.com...
> BAD
> IBM *requires* TEST and NOOPT for their interactive debugging tools (which 
> is rarely what is used in production, so you STILL have to recompile and 
> re-test before production)

Is there an issue with this ? You can use TEST(NONE,SYM,SEPARATE)

Dynamic Debug does not put hooks into your source but inserts them at run 
time so you can test with the compile option TEST(NONE) - you do need the 
Authorized Debug facility and be authorized to use it to debug but I think 
you can debug _without_ going through a recompile stage directly in 
production environments.  The debug information is all kept separate so it 
does not affect the object size.

Not sure on the NOOPT but I think it's only disabled when the test option is 
not NONE.

Am I missing something?

JCE
```

#### ↳ Re: Various "debuggin" tools (for IBM mainframe development)

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-04T07:57:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dctadg$143q$1@si05.rsvl.unisys.com>`
- **References:** `<c0iIe.820839$ub.287481@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:c0iIe.820839$ub.287481@fe07.news.easynews.com...

> One of the things that I think (but won't swear to it) that is relatively
> different about the IBM mainframe COBOL environment and the COBOL
environment
> elsewhere and other language development environments is the HUGE number
> (historic and current) of "3rd party" and "add-on" products for debugging
> (static and dynamic), optimizing,  etc.  Chuck can certainly correct me if
he
> know of lots for Unisys - ...

No, you're quite right, Bill.  The internals of Unisys MCP compilers, the
object code generated by them, and even the (specified and defined) format
of an object code file can change absolutely without notice from release to
release so long as the system software recognizes the change.  Unisys
supports only those compilers that Unisys compiles and ships.  I do not
believe it is cost-effective for outside vendors to modify the compilers to
produce different object code to accommodate debugging tools.

Unisys continues to support the Debug Module in COBOL, but most users have
found TADS (Test And Debug System) preferable and more powerful (it's
available for the shared-technology languages COBOL85, Pascal83 and C, as
well as the older monolithic compilers for COBOL74, Fortran77, and all four
ALGOL-based languages).  TADS also has hooks into CANDE (Command and Edit
Language, the original Burroughs Large System on-line editing tool), EDITOR
(a more powerful, but still green-screen editing/debugging environment) and
Programmer's Workbench (the latest Windows-based development environment,
with interfaces to both MCP and TADS).  TADS also relies on explicit and
continued response and intervention provided directly by the MCP itself.

In fact, one of the reasons we continue to develop such tools in-house is
precisely that it *is* impractical for outside vendors to keep up with the
relatively rapid evolution of the specifics of code file formation that
comes from the very close cooperation among the developers of the operating
system, the compilers and the hardware that has been a hallmark of this
particular architecture since the introduction of the Burroughs B5000.

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
