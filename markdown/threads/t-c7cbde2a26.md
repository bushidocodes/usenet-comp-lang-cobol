[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Free IBM machine accounts for COBOL programming?

_5 messages · 4 participants · 2020-03_

---

### Free IBM machine accounts for COBOL programming?

- **From:** "roland" <ua-author-4387559@usenetarchives.gap>
- **Date:** 2020-03-04T19:58:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com>`

```
All,

As a result of a "discussion" in another group I got into playing with COBOL again and started writing "The Minimum You Need to Know About GnuCOBOL." If any of you have read one or more books in that series

theminimumyouneedtoknow.com

you know that they aren't like mass market books just regurgitating the manuals with a couple of trivial examples thrown in. What I want to focus on in this book is COBOL != COBOL != COBOL. I will most likely reprise my lottery tracking system from this book

https://www.theminimumyouneedtoknow.com/app_book.html

but I also want to focus on the platform specific differences. I've thrown out my DS-10 Alpha running OpenVMS, but there are places I can get a VMS account. I also wanted to include versions of the same programs on an IBM platform. In particular it would be cool if the IBM system also had PostgreSQL installed because that is the closest I can think of to a production database that could be running on all computers.

At any rate, if someone knows of places one can sign up for a basic "student" level account that would be great. I especially want to do some detailed analysis of the COMP-3 differences with GnuCOBOL, IBM COBOL, and DEC/VAX/VMS COBOL. I might even dribble in a CICS version of the screen programs.

Thanks,
```

#### ↳ Re: Free IBM machine accounts for COBOL programming?

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2020-03-04T20:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7cbde2a26-p2@usenetarchives.gap>`
- **In-Reply-To:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com>`
- **References:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com>`

```
In article <70dd4e97-178b-4ae1-9a1b-a31··d@goo··s.com>,
seasoned_geek wrote:

[snip]

› What I want to
› focus on in this book is COBOL != COBOL != COBOL.

Best of luck, old boy; there are hiring managers who don't know this.

DD
```

##### ↳ ↳ Re: Free IBM machine accounts for COBOL programming?

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-03-05T09:54:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7cbde2a26-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c7cbde2a26-p2@usenetarchives.gap>`
- **References:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com> <gap-c7cbde2a26-p2@usenetarchives.gap>`

```
On 3/4/20 8:52 PM, doc··f@pa··x.com wrote:
› In article <70dd4e97-178b-4ae1-9a1b-a31··d@goo··s.com>,
› seasoned_geek   wrote:
…[9 more quoted lines elided]…
› 

I have moved COBOL programs from a number of systems to
GnuCOBOL. About the only thing I ever find needing
modification are SELECT Statements because of the numerous
ways to name and refer to files. GnuCOBOL handles it quite
nicely.

bill
```

###### ↳ ↳ ↳ Re: Free IBM machine accounts for COBOL programming?

- **From:** "roland" <ua-author-4387559@usenetarchives.gap>
- **Date:** 2020-03-06T15:48:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7cbde2a26-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c7cbde2a26-p3@usenetarchives.gap>`
- **References:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com> <gap-c7cbde2a26-p2@usenetarchives.gap> <gap-c7cbde2a26-p3@usenetarchives.gap>`

```
On Thursday, March 5, 2020 at 8:54:32 AM UTC-6, Bill Gunshannon wrote:
› On 3/4/20 8:52 PM,  wrote:
›› In article ,
…[18 more quoted lines elided]…
› bill

Going FROM some system to GnuCOBOL works well, especially if you don't have any OOP COBOL and are staying on the same platform. Having said that, I will be focusing more on complex calculation throughput and database interaction. I will also be focusing on the YABU implementation.

Most importantly the wide range of functions/extensions GnuCOBOL has which cannot be used if you want to move FROM GnuCOBOL to another platform's COBOL. It seems GnuCOBOL took pains to implement many of MOFO and ACCUCOBOL's extensions, but those extensions don't play everywhere. I really want to beat on the COMP-3 calculations where temporaries will be created within COMPUTE statements. The Decimal standard isn't fixed point and that introduces issues when some big numbers are involved.
```

###### ↳ ↳ ↳ Re: Free IBM machine accounts for COBOL programming?

_(reply depth: 4)_

- **From:** "wlfraed" <ua-author-2301228@usenetarchives.gap>
- **Date:** 2020-03-13T18:56:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c7cbde2a26-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c7cbde2a26-p4@usenetarchives.gap>`
- **References:** `<70dd4e97-178b-4ae1-9a1b-a311b100e20d@googlegroups.com> <gap-c7cbde2a26-p2@usenetarchives.gap> <gap-c7cbde2a26-p3@usenetarchives.gap> <gap-c7cbde2a26-p4@usenetarchives.gap>`

```
On Fri, 6 Mar 2020 12:48:06 -0800 (PST), seasoned_geek
declaimed the following:

› Going FROM some system to GnuCOBOL works well, especially if you don't have any OOP COBOL and are staying on the same platform. Having said that, I will be focusing more on complex calculation throughput and database interaction. I will also be focusing on the YABU implementation.
›
› Most importantly the wide range of functions/extensions GnuCOBOL has which cannot be used if you want to move FROM GnuCOBOL to another platform's COBOL. It seems GnuCOBOL took pains to implement many of MOFO and ACCUCOBOL's extensions, but those extensions don't play everywhere. I really want to beat on the COMP-3 calculations where temporaries will be created within COMPUTE statements. The Decimal standard isn't fixed point and that introduces issues when some big numbers are involved.

Any possibility you can make use of the Raincode COBOL Legacy compiler?
Yeah -- it runs on Windows, but is supposed to be aimed at a "no port" port
from mainframe compilers.

They just released a new version of the compiler -- the COBOL is
documented to be "free" (PL/1 and ASM need licenses).

Unfortunately, I've not been able to get it to create a usable EXE* (it
builds the EXE, but that then fails with a missing DLL; even though the DLL
is in the PATH). I have managed to get it to compile to a DLL (the default
behavior) which one executes using a "runner" program. The documentation is
also not the clearest around with regards to defining the data file
connections.


* I'm sure v3.x -- 2017 -- built working executables, but 4.0.x doesn't.
OTOH, 4.x has the Visual Studio integration which appears to work with the
community edition of VS2019; v3.x wouldn't integrate with community
version. Haven't figured out how to get the data files to be found by the
VS "runner" (again -- builds DLLs, not stand-alones).


	Wulfraed                 Dennis Lee Bieber         AF6VN
	wlf··d@ix.··m.com    http://wlfraed.microdiversity.freeddns.org/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
