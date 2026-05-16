[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus position on the "Standardized" OO Collection Class Technical Report

_18 messages · 7 participants · 2006-07_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Compilers and vendors`](../topics.md#compilers) · [`Object-oriented COBOL`](../topics.md#oo)

---

### Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-27T08:22:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`

```
I thought some of you in this forum might be interested in a document just 
posted to the (public) J4 website.  See:

     http://www.cobolstandard.info/j4/files/06-0076.doc
```

#### ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-27T16:11:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EA5yg.244380$iF6.77276@pd7tw2no>`
- **In-Reply-To:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`

```
William M. Klein wrote:
> I thought some of you in this forum might be interested in a document just 
> posted to the (public) J4 website.  See:
> 
>      http://www.cobolstandard.info/j4/files/06-0076.doc
> 
Excellent !

Existing users can stick with existing M/F Collection classes, at least 
until such time in an upgrade, that M/F might drop them (???); or 
alternatively go the dotNet route.

Can only wonder why your statement wasn't made earlier by Micro Focus.

Jimmy
```

#### ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** Fredrick.Underwood.Devrie@gmail.com
- **Date:** 2006-07-27T10:34:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154021658.148982.275810@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`

```

William M. Klein wrote:
> I thought some of you in this forum might be interested in a document just
> posted to the (public) J4 website.  See:
…[5 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

Having read this paper and others available on this web site, I find
your submission to be quite, well, I want to say STUPID but I'll just
say very short sighted.

First, the document doesn't really talk about anything other than your
threat, your desire to kill this Technical Report, which as I
understand it, Micro Focus as a company is free to ignore.  Nothing is
binding in a Technical Report.  There is no way for J4 to proces this
paper and there was no reason to submit it other than to cause
controversy and contention.  Posting it to this group leads to
confusion, futher controversy and well, sadly it shines a negative
light on you and the company you represent.  It's like publically
calling a duel.  How uncivilized.

Second - without the Collection Class Library standardized, there is no
portablility amongst compilers (which may well be Micro Focus' intended
goal, locking you into their solution) as to this interface with OTHER
OO languages.

Short sighted and stupid.  If this really is an official Micro Focus
position, I would hope that Micro Focus wakes up and realizes that
instead of attracting customers with this stand they are driving them
away.
```

##### ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-27T18:29:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PB7yg.142247$vu2.103997@fe05.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com>`

```
If you are a strong supporter of COBOL portability, then I assume you are aware 
that there are NO implementations of either the current ANSI or ISO COBOL 
Standard.  Not know which vendor's or vendors'  compiler you are currently 
using, I am forced to ask if YOU (or your company) have asked your vendor to 
provide a conforming compiler?  Also, do you currently compile using "standard 
conforming" flagging.

My experience (both when working for a vendor, working as a member of the user 
group of another vendor, and from years watching this forum) is that actual 
COBOL programmers do NOT code "conforming" COBOL source code, so that 
"portability" via standardization simply doesn't exist.

  ***

As far as the reason for this specific paper, J4 *will* be voting on the TR next 
week (which by the way as stated in another submission is actually a "Technical 
Specification" rather than a "Technical Report" according to current ISO usage). 
Therefore, this paper was intended to provide advanced warning of the action 
that Micro Focus will be taking at the meeting.  Personally, from previous 
standards-group work, I find getting advanced warning useful.  If you have 
worked on some other committee, you may not have found this useful, but I have 
never heard that on J4.

As far as this being "short-sighted,"  Micro Focus has found that the amount of 
current COBOL-only OO applications is virtually nil.  OO COBOL on Windows, Unix, 
and Linux tends to exist in "mixed language" applications.  Therefore, as stated 
in the paper, MF will continue to work on improving support for such 
inter-operability, but will NOT try and enhance COBOL-only (RESTRICTED to COBOL) 
tools (for OO).

It should be noted that IBM, for example, currently only supports OO COBOL (on 
z/OS) in a "Java" environment.  As Java DOES include "collection classes" - the 
need for COBOL-only interfaces is non-existent.  In fact, trying to force COBOL 
semantics on mixed COBOL/Java is counter-productive (for their customers).

 ***

Finally, it is my expectation that there is a pretty good chance that J4 *will* 
forward the Collection Classes document to ISO for national body vote at their 
meeting next week.  If you think the current specification is a GOOD thing for 
COBOL, then I would suggest that you make certain that your national standards 
body is aware of your view.  It is (partially) to alert members of this forum to 
the upcoming international vote and its issues that I posted my original note.

The other reason, is that my past impression of this newsgroup is that many 
(certainly  NOT all) members did NOT think the current J4 specification was the 
correct way to go.
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** Fredrick.Underwood.Devrie@gmail.com
- **Date:** 2006-07-27T12:07:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154027265.476636.184240@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<PB7yg.142247$vu2.103997@fe05.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com>`

```

William M. Klein wrote:

> My experience (both when working for a vendor, working as a member of the user
> group of another vendor, and from years watching this forum) is that actual
> COBOL programmers do NOT code "conforming" COBOL source code, so that
> "portability" via standardization simply doesn't exist.
>

Your experience is obviously limited.  I have ported many systems
across multiple platforms and vendors with minimal change.  This is
quite a bogus argument.  It is partially because of standardization and
conforming compilers that this is possible, and that COBOL is the
success story that it is.  I am even aware of systems developed with MF
COBOL but deployed with a different vendor COBOL (with ZERO source code
changes) in order to avoid paying out of sight run time fees.

> As far as this being "short-sighted,"  Micro Focus has found that the amount of
> current COBOL-only OO applications is virtually nil.  OO COBOL on Windows, Unix,
…[3 more quoted lines elided]…
> tools (for OO).

This is such a spurious argument it makes me laugh.  Of COURSE there
are few OO only COBOL programs in MF Experience.  They don't have a
conforming implementation of the standard so there cannot be any
programs that are OO only.  It's like arguing against developing a
hydrogen powered car because you have never developed a hydrogen
powered car.  MF obviously wants the standard to be whatever THEY have
developed and not a REAL standard.  I am aware that MF has OO
extensions.  Compared to the COBOL standard, they are, well - just
aweful.  Their ISO2000 directive that allows comforning syntax is sadly
incomplete and if it WERE then it would be possible to write full OO
COBOL programs and who knows ... if there were a way to do it maybe
they would encouter users using it!
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-27T20:10:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f59yg.151261$Rg2.10872@fe07.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com>`

```
I agree that COBOL programs are portable - and that this is one of the 
advantages of COBOL.  However, I do NOT agree that portable COBOL programs are 
"standard conforming".  (Consider COMP-3, GOBACK,  USAGE POINTER and so many 
other EXTENSIONS that are widely used).

Your assumption that my primary experience is mostly with Micro Focus is simply 
WRONG.  If you are a frequent reader of this forum, I think you wouldn't have 
thought that, but that is only an assumption on my part.

Again, tell me what vendor you are using and I will know to what extent it 
"conforms" to the CURRENT ANSI and/or ISO Standard.  It is true that Micro Focus 
doesn't, but as I indicate elsewhere, there is NO vendor (or freeware) that 
does.  In fact, to the best of my knowledge, the Micro Focus implementation of 
OO is the closest to the current Standard of any currently available for 
Windows, Unix, or Linux.

The point is that existing customers of ALL COBOL vendors have not provided 
sufficient business cases to the vendors for them to provide conforming 
compilers.  Vendors meet REAL customers needs, not "standards".

Vendors do (have and will continue to) provide compilers supporting portable 
COBOL source code.  I see little or no evidence that any customers actually 
want/need or that vendors are soon going to provide conforming compilers.

P.S.  There was some need/business cases for compilers conforming to the '85 
ANSI/ISO Standard - but that is 20 years ago.  Those compilers are still in use 
(and being developed and enhanced).

Again, did you ever try compiling ANY of your "portable" (or ported) COBOL 
source code with "conformance flagging" turned on?  If so, was it conforming?

Finally, Micro Focus is committed to providing "mixed COBOL/Java" and "mixed 
COBOL/C++" and "mixed COBOL/C#" PORTABLE object oriented support.  If that was 
what the current ANSI Collection Classes "promised," then I think Micro Focus 
would support it.  However, that is exactly what this proposal STOPS from 
happening - as it forces the application to use COBOL-specific semantics in what 
is usually a multi-language environment.
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 5)_

- **From:** Fredrick.Underwood.Devrie@gmail.com
- **Date:** 2006-07-27T14:29:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154035740.484705.322500@s13g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<f59yg.151261$Rg2.10872@fe07.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com>`

```

William M. Klein wrote:

> Your assumption that my primary experience is mostly with Micro Focus is simply
> WRONG.  If you are a frequent reader of this forum, I think you wouldn't have
> thought that, but that is only an assumption on my part.

Kind Sir, I never assumed any such thing and challenge you to show
where I indicated such in my messages.  Your assumptions are what they
are.

>
> Again, tell me what vendor you are using and I will know to what extent it
…[5 more quoted lines elided]…
>

This is not related to the issue at hand.  Micro Focus wanting to kill
a feature that is vitally necessary for development of Object Oriented
programs in COBOL.

> Finally, Micro Focus is committed to providing "mixed COBOL/Java" and "mixed
> COBOL/C++" and "mixed COBOL/C#" PORTABLE object oriented support.  If that was
…[3 more quoted lines elided]…
> is usually a multi-language environment.

Your "usually a multi-language environment" argument is erroneous.  C++
does not USUALLY interact with Java.  Java doesn't USUALLY (ever?)
interact with C#, etc.  COBOL seems to be the only place such mixing
seems to be necessary and this MAY be largely because one cannot use
any native syntax in COBOL to use collections of objects -- something
vital to OO programming.

This mixed language support does not allow one to collect COBOL only
objects.  Killing the feature does nothing to enable Micro Focus to
create these extensions as they desire.  It does, however,
unnecessarily strip COBOL of a needed feature for OO programming.  This
is negativism toward COBOL - which as I understand it, is Micro Focus'
bread and butter.  It seems like cutting off one's nose to spite one's
face.  

THUS it is short sighted and well... stupid.
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-27T22:24:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72byg.152074$Rg2.76522@fe07.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154035740.484705.322500@s13g2000cwa.googlegroups.com>`

```
<Fredrick.Underwood.Devrie@gmail.com> wrote in message 
news:1154035740.484705.322500@s13g2000cwa.googlegroups.com...
>

(previous messages snipped)

It seems as if you and I aren't communicating very well.  Please DO communicate 
your views on providing a Standard COBOL Collection Class specification to your 
national standards body and any and all COBOL vendors that you deal with.

I want to correct one thing from an earlier post

You statted,

" Of COURSE there are few OO only COBOL programs in MF Experience.  They don't 
have a conforming implementation of the standard so there cannot be any programs 
that are OO only."

Micro Focus *does* have an OO implementation that conforms to the current 
ANSI/ISO definition.  They also provide collection classes (as an extension to 
the current ANSI/ISO COBOL OO specification - as there is no current 
specification for this.)

Even WITH these classes, Micro Focus has determined that most (certainly not 
all) COBOL programmers developing COBOL OO applications WANT to use existing 
class libraries that are NOT language specific (e.g. the .NET class libraries).

You still haven't answered (that I have seen) which vendor or vendors compilers 
you are using and whether you use their conformance flagging features. If so, do 
your programs actually NOT use any extensions?  (I am certain that some such 
programs exist in the world, but I don't think they are very common.)

COBOLsource code portabity is and will continue to be important.  Previous 
experience (of most programmers that I have dealt with on Windows, Linux, Unix, 
and IBM platforms, do NOT restrict their portable source code to syntax defined 
in the Standard - but rather to that source code that is commonly implemented. 
These two simply are not now (if they ever were) the same.

Having an ISO specification for a COBOL-specific Collection Class will provide 
just about as much portability as the definition of VALIDATE (included in the 
current Standard) and BIT data types (also in the current standard) and Report 
Writer (required, not optional in the current Standard) and lots of other NOT 
IMPLEMENTED BY MANY vendor features.

  ***

If my original post actually gets you to communicate with your "vendor of 
choice" and/or your "national standards body" - even if it is to disagree wtih 
the Micro Focus position, then I think that is a good thing.  If all you do is 
call this vendor "stupid" for meeting its best information of what its current 
customers WANT, then there is a problem somewhere, and it isn't with Micro 
Focus.
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-27T16:17:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154042276.584592.119660@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<f59yg.151261$Rg2.10872@fe07.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com>`

```
William M. Klein wrote:

> I agree that COBOL programs are portable - and that this is one of the
> advantages of COBOL.  However, I do NOT agree that portable COBOL programs are
> "standard conforming".  (Consider COMP-3, GOBACK,  USAGE POINTER and so many
> other EXTENSIONS that are widely used).

Well, _I_ never use those 3 examples, never have.  The first two are
IBMisms and no use to me.  USAGE POINTER is for C programmers.

> The point is that existing customers of ALL COBOL vendors have not provided
> sufficient business cases to the vendors for them to provide conforming
> compilers.  Vendors meet REAL customers needs, not "standards".

I think that 'business cases' are more important than 'real customer
needs'. It is in the vendors interest to lock in their customers in by
creating features that the customers, or actually the customer's
programmers, will use as if they were real needs.

> Vendors do (have and will continue to) provide compilers supporting portable
> COBOL source code.  I see little or no evidence that any customers actually
> want/need or that vendors are soon going to provide conforming compilers.

Vendors provide the ability to port _to_ their special features from
other vendors. They do not support  'portable source code' in the sense
of 'write it for our compiler and recompile it on someone else's'
(except for example MF targetting mainframe development).

> Finally, Micro Focus is committed to providing "mixed COBOL/Java" and "mixed
> COBOL/C++" and "mixed COBOL/C#" PORTABLE object oriented support.  If that was
…[3 more quoted lines elided]…
> is usually a multi-language environment.

I don't actually see the point of mixed languages.  It sounds nice to
use 'existing skills and logic', but usually it takes more effort to
re-engineer than to just rewrite.
```

###### ↳ ↳ ↳ Portability and porting (was: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-28T00:23:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KNcyg.122880$GD7.23528@fe08.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154042276.584592.119660@i42g2000cwa.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1154042276.584592.119660@i42g2000cwa.googlegroups.com...
> William M. Klein wrote:
>
<snip>
>> Vendors do (have and will continue to) provide compilers supporting portable
>> COBOL source code.  I see little or no evidence that any customers actually
…[6 more quoted lines elided]…
>

Interesting point and one that once upon a time and long ago was a major part of 
my "job".

When I did work for Micro Focus (pre-MERANT) my primary respoonsibility (for 
much of the time) was "IBM Mainframe compatibility".  This was because a large 
portion of MF's revenue at that time was in providing a workstation environment 
for developing applications intended to run on IBM mainframes (and be compiled 
with IBM mainframe compilers) - as you mention above.

This was also the primary revenue source for Realia (pre- CA - if not 
afterwards).  Fujitsu's compiler actually started out as "shared" source code 
with IBM (but the law-suits related to that were well documented).

The history of COBOL and portability is one of "de jure" vs. "de facto" 
standards.  When COBOL was "young and growing", IBM mainframes were a (the?) 
dominant playing field for "business" data processing.  What IBM did (with COBOL 
as with many other things) was OFTEN (not always) "copied" by other vendors - so 
that people COULD "port" their applications (easily) from IBM to their 
environments - regardless of what any Standard did and did not say. Today, there 
is (IMHO) no correspondingly DOMINANT COBOL vendor. (M$ may be considered a 
correspondingly dominant operating system vendor - whether people like them or 
not <G>)

X/Open was a (relatively) early attempt to take EXISTING extensions and create a 
"Standard" that actually provided portabilikty across "open systems" (usually 
Unix or similar environments).  Some of those extensions are still common today, 
others are not, e.g.
 -  Line Sequential files
 - Comp-5 (non-truncated binary and/or operating system specific binary)
 - methods of getting and setting environment variables and program "arguments"
 - even extended Accept/Display (especially with screen section)

Most of those (I think) appeared first as an extension in one vendor's 
implementation and then in multiple vendors implementations then in X/Open.  The 
'02 Standard actually "picked up" both Screen Section and 
File-Sharing/Record-locking FROM the X/Open specification, but made them 
"processor dependent" which is "newspeak" for optional.

My impression (true or false) is that when an implentor provides a "new 
extension" that meets their customers' needs (perceived or real) that other 
vendors DO add similar and usually dentical extensions
  - if their customers also want this type of facility
         and
  - if this vendor wants to provide a "portation facility" FROM (as you 
indicated) the other implementation

The more various implementors provide the "same" extension, the more likely it 
is to become a de facto Standard.

 ***

Bottom-Line:
  Other than providing a "development off-loading platform" (e.g. Micro Focus 
Mainframe Express), you are certainly correct that most (all?) vendors are NOT 
in the business of providing "easy" portation AWAY from their products.  On the 
other hand, my perception is still that vendors DO provide extensions to meet 
the actual "buisness needs" of their current customers (e.g. both Micro Focus 
and IBM XML support/extensions).  If these extensions are truly needed in 
"portable" source code, then multiple vendors will pick them up.  If they are 
not (such as my perception of the COBOL OO Collection Classes - and COBOL 
Standard Arithmetic) then no amount of "standardization" will get vendors to 
provide them
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-27T19:56:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12cio4gg5af1354@news.supernews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154042276.584592.119660@i42g2000cwa.googlegroups.com>`

```
Richard wrote:
>
> I don't actually see the point of mixed languages.  It sounds nice to
> use 'existing skills and logic', but usually it takes more effort to
> re-engineer than to just rewrite.

There are some things you just can't do in COBOL.

Flames, for example.

Or what if, in the middle of a double declining balance computation you 
needed the inverse of a 100x100 matrix? AND needed to compose a ringtone to 
go with it?
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-27T18:59:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154051960.444514.73700@75g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<12cio4gg5af1354@news.supernews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com> <1154027265.476636.184240@m73g2000cwd.googlegroups.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154042276.584592.119660@i42g2000cwa.googlegroups.com> <12cio4gg5af1354@news.supernews.com>`

```

HeyBub wrote:
> Richard wrote:
> > I don't actually see the point of mixed languages.  It sounds nice to
…[9 more quoted lines elided]…
> go with it?

In a rational world it will be known at the program specification stage
that such things are needed and it will be implemented in the most
appropriate language.

Having a 100x100 matrix in Cobol with a need to invert it it may be
more effective to code the inversion in Cobol rather than working out
how to pass that data into a Java class or Fortran array and have it
inverted there.

Alternately if there is part done already in Cobol it may be easier
and/or better to reimplement that code into Java (or Fortran) rather
than attempting to rewrite the Cobol part and some new Java part and
gluing them together.
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-28T09:27:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaclar$5qa$1@reader2.panix.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154042276.584592.119660@i42g2000cwa.googlegroups.com> <12cio4gg5af1354@news.supernews.com>`

```
In article <12cio4gg5af1354@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>Richard wrote:
>>
…[6 more quoted lines elided]…
>Flames, for example.

Hmmmm...  what about -

MOVE 'POOPIE-HEAD'  TO  LAST-POSTERS-DESCRIPTION.
MOVE 'AM NOT! '     TO  STUNNING-REPLY.
MOVE 'ARE SO! '     TO  REPLYS-REJOINDER.

... and so on.

DD
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-28T08:56:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ck5roj9vh9f47@news.supernews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <f59yg.151261$Rg2.10872@fe07.news.easynews.com> <1154042276.584592.119660@i42g2000cwa.googlegroups.com> <12cio4gg5af1354@news.supernews.com> <eaclar$5qa$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <12cio4gg5af1354@news.supernews.com>,
> HeyBub <heybubNOSPAM@gmail.com> wrote:
…[17 more quoted lines elided]…
>

I was thinking about the other kind of flames, like the one's on the 
dentist's (played by Allen Arkin) BMW in "The In-Laws":

Arkin: "There's FLAMES on my car!"
Be-bopper: "Thaz right man. They won't wash off and you can't paint over 
'em."
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-07-28T14:13:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ead622$3hq$1@reader2.panix.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <12cio4gg5af1354@news.supernews.com> <eaclar$5qa$1@reader2.panix.com> <12ck5roj9vh9f47@news.supernews.com>`

```
In article <12ck5roj9vh9f47@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <12cio4gg5af1354@news.supernews.com>,
…[25 more quoted lines elided]…
>'em." 

Hmmmmm... and some people wonder if there are reasons for my saying 'I 
barely know what *I* think, let alone anyone else.'

DD
```

###### ↳ ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-27T13:24:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4isi6qF5a2paU1@individual.net>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com> <PB7yg.142247$vu2.103997@fe05.news.easynews.com>`

```
Just a few IMHO thoughts:
- It would certainly be useful for COBOL to be able to utilize objects and
interfaces created by/for other languages/run-time environments.
- However, *relying* on another language/run-time environment to be present
just to use COBOL seems to me to not be a good thing.

Specifically, I think it's a good thing that IBM Enterprise COBOL has
interoperability with Java.  But I think that requiring java.lang.Object as
the base object for OO COBOL is a very bad idea.  It should be *allowed* but
not *required*.  (Am I mistaken that it is required?)

It seems to me that COBOL collection classes need not be part of the COBOL
standard.  It seems to me that it might be more useful for someone to write
the collection class in standard(!) COBOL and release the source code to the
community.  Vendors could provide these collection classes with their
compiler, if they choose.  But even if they don't one could simply compile
them from source.

Or one could, if such an interface is available, use classes available for
another language/run-time environment.

Seems to me that both options have their good and bad points, and that
neither is perfect.  But to have both options available would give you a
choice on which way to go.

It also seem like it would be idea if other languages could interface
directly with COBOL objects.  I'm not sure how all of this inter-language
interfacing even works right now, so I can't say much more than that. 

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 07/27/06 12:29 PM >>>
If you are a strong supporter of COBOL portability, then I assume you are
aware 
that there are NO implementations of either the current ANSI or ISO COBOL 
Standard.  Not know which vendor's or vendors'  compiler you are currently 
using, I am forced to ask if YOU (or your company) have asked your vendor to

provide a conforming compiler?  Also, do you currently compile using
"standard 
conforming" flagging.

My experience (both when working for a vendor, working as a member of the
user 
group of another vendor, and from years watching this forum) is that actual

COBOL programmers do NOT code "conforming" COBOL source code, so that 
"portability" via standardization simply doesn't exist.

  ***

As far as the reason for this specific paper, J4 *will* be voting on the TR
next 
week (which by the way as stated in another submission is actually a
"Technical 
Specification" rather than a "Technical Report" according to current ISO
usage). 
Therefore, this paper was intended to provide advanced warning of the action

that Micro Focus will be taking at the meeting.  Personally, from previous 
standards-group work, I find getting advanced warning useful.  If you have 
worked on some other committee, you may not have found this useful, but I
have 
never heard that on J4.

As far as this being "short-sighted,"  Micro Focus has found that the amount
of 
current COBOL-only OO applications is virtually nil.  OO COBOL on Windows,
Unix, 
and Linux tends to exist in "mixed language" applications.  Therefore, as
stated 
in the paper, MF will continue to work on improving support for such 
inter-operability, but will NOT try and enhance COBOL-only (RESTRICTED to
COBOL) 
tools (for OO).

It should be noted that IBM, for example, currently only supports OO COBOL
(on 
z/OS) in a "Java" environment.  As Java DOES include "collection classes" -
the 
need for COBOL-only interfaces is non-existent.  In fact, trying to force
COBOL 
semantics on mixed COBOL/Java is counter-productive (for their customers).

 ***

Finally, it is my expectation that there is a pretty good chance that J4
*will* 
forward the Collection Classes document to ISO for national body vote at
their 
meeting next week.  If you think the current specification is a GOOD thing
for 
COBOL, then I would suggest that you make certain that your national
standards 
body is aware of your view.  It is (partially) to alert members of this
forum to 
the upcoming international vote and its issues that I posted my original
note.

The other reason, is that my past impression of this newsgroup is that many

(certainly  NOT all) members did NOT think the current J4 specification was
the 
correct way to go.
```

##### ↳ ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-28T01:57:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<naeyg.251981$IK3.36235@pd7tw1no>`
- **In-Reply-To:** `<1154021658.148982.275810@i42g2000cwa.googlegroups.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com> <1154021658.148982.275810@i42g2000cwa.googlegroups.com>`

```
Fredrick.Underwood.Devrie@gmail.com wrote:
> William M. Klein wrote:
> 
…[7 more quoted lines elided]…
>> wmklein <at> ix.netcom.com

Hey ! Hey ! What's all this haranguing Bill Klein for. Don't shoot the
messenger !

For the record, way beyond retirement age, I have given up on
programming completely, particularly COBOL because it is becoming
prohibitively expensive on PCs. However I am a thousand percent for OO
COBOL and the feature I enjoyed most was Collections/Dictionaries.

Background - Ann Bennett/Wallace representative for IBM on J4 and at the
  time Covenor for WG4 (ISO), which job she is probably reluctantly
volunteering for again, now that Chuck Stevens (Unisys) got laid-off,
credits three people with "giving" COBOL any OO capability - Raymond
Obin who was at the time an M/F employee, somebody from HP and the third
company representative I can't remember.

Back around '93, J4 set up a sub-committee OCTG (Object COBOL Technical
Group). Good move. People who had a genuine interest in pursuing the
topic, even if they weren't all closely familiar with it. Ray Obin
produced a short paperback summarizing their thoughts and current OO
classes are not dramatically different, although there have been minor
refinements made to the syntax. (I'm not referring here to either
Collections or GUIs which were not at that time part of their
objective). Amongst others, in his book Ray acknowledged two M/F
employees at the time, Don Schricker and Bill Klein, who served on the OCTG.

Frankly it's a bloody miracle COBOL ever got any OO at all - just note
all the people in this Newsgroup oozing with enthusiasm !

Four companies took up the challenge, Hitachi, IBM and Micro Focus.
The fourth, Fujitsu followed a while later. IBM had Visual Age closely
tied into OS2 - and as we know that appears to have silently
disappeared. For Fujitsu, Hitachi and Micro Focus to produce
competitive OO compilers versus other languages, they knew they had to
provide two features - GUIs and Collections. They each did this in their
own way. It's always been a mandate of J4 that the COBOL Standard should
not acknowledge different Operating Systems. My thoughts, bad move - and
throws Windows GUI-ing out of the window (no pun intended).

I rile each time I reflect on this. Back around 95/96 Russell Clarke,
(Australia) produced a very DETAILED paper on OO COBOL Collections -
well in excess of 50 pages - I'll take a guess, it took him at least six
months of thought to put it together. I'll admit I didn't comprehend
clearly what his paper was about - and I'm just as certain that 90% of
the J4 membership didn't have a clue either ! Having given it subsequent
thought, the only way to discuss Russell's paper was that it produced
many templates which allowed you to cobble them together to achieve the
particular collection type you required to suit your own needs.

Had he had sufficient time, maybe his ideas might have come across more
clearly if he had taken those templates and produced samples showing what
you could achieve by 'cobbling'.

It appears J4 thought Russell's paper was the best thing since sliced
bread. Without catching their breath they forwarded it to WG4 for comment
- where it got CLOBBERED on some nitty-gritty stuff. "Ooh!", said J4,
"Good try, but let's put it on ice". Meanwhile some of the OO books were
telling us there would be OO Collections around '97 - the authors got
this info from J4 membership.

Back to William Klein. Henry VIII's 'Defender of the Faith", on British
coinage. If there's anybody deserves that awarded in the COBOL world it
is Bill. He served on J4 in a private capacity (picking up the tab for
membership and travel expenses out of his own pocket). He has always
been a staunch promoter of COBOL and no less for OO. He is on record as
writing, "We want OO COBOL (and Collections) to be the best there is".
Having said that, I think I'm correct in stating that Bill is still not
an OO enthusiast - but from his view, if COBOL has to have OO then 'make
it the best'. So far as I am aware he has never made comment one way or
the other that he is for or against Collection classes.

Back to Russell - Thane Hubbell who subsequently represented Fujitsu on
J4 until they quit, set up a discussion group, roughly some 20 of us. So
somewhere around 2000 Bill points us at Russell's document sat on ice.
Even though a couple of us had earlier volunteered to give some input,
we were not advised by the J4 chair that Russell's paper existed. There
was something written in J4 documentation that in due time they would
return to the Collection topic. Bill nudged them, at the same time
pointing us at Russell's paper. I'm quite sure that the J4 team were
delirious that Bill raised this old nugget.

With an interest in Collections I had a deep look at what Russell had
written. For clarification I contacted him but had an out-of-date e-mail
address. So now I sat down and produced something for J4 based on my own
coding using M/F classes. It wasn't a proposal, but a description from a
developer's point of view. (A subtle way of telling the 'non-knowing'
what OO Collections were about).

I consider it absolutely C-R-I-M-I-N-A-L the way Russell's paper was
treated. Having consumed a considerable amount of time in producing his
paper and the currency he was paid in was fresh air. So they just
shelved it. Not that Russell could give a monkies; soon after he
switched completely to Java - as advised to me when he acknowledged my
e-mail, (see next para but one below)..

By no means comprehensive, and perhaps simplistic, I arrived at a
different model from Russell. On reflection, if Russsell's paper had
expanded on his proposed syntax with examples, it might have been a
winner. Lots of classes involved but I think he had all points covered
and conceivably it might have been considerably more flexible than the
Smalltalk model on which Hitachi and Micro Focus based their
collections. (I'm referring to what you called a 'Tutorial Language'
Pete :-) ).

Just about to submit my initial paper, out of the blue comes Russell - he
had picked up my message from his old e-mail address. He made some
useful comments and agreed that he had missed out on not including
SORTED COLLECTIONS. Too late in the day to revamp what I had written I
submitted it to J4 with some of Russell's responses as an appendix. Let
me state again, emphatically, I am no OO expert, just somebody
illustrating the code he produced using existing M/F classes.

Forgotten the timing, when it started, but OO Collections were
'resurrected'. Enthusiastic and the new boy on the block, (the J4 team),
  Thane Hubbell was either asked or volunteered to do the Collection
proposal. Features began to appear, but didn't convey the whole story.
Off the top of my head there are some 30 plus classes in the M/F
Collection hierarchy - things like CharacterArray and Arrays which can be
used independently - e.g. to access the icons in a Treeview you use an
indexed collection held in an Array.

Well he sure took the knife to the M/F structure. Whether at the time
Thane had *actually* coded in either F/J Collections or Java - I don't
know. The net result first go-around was Ordered Collection,
KeyedCollection (aka Dictionary or MAP in Java), with coded examples of
methods. (Note I capitalized SORTED COLLECTIONS above ?). I referenced
Fujitsu on-line manuals but unfortunately examples only show snippets of
code - not complete programs/classes. They sure have a different
philosophy about creating object references compared to M/F. Using the
'Design Pattern' technique read a record from a file into a new
class(object) for that record - now you have an object reference - as
opposed to M/F where objects can certainly be created using aRecordClass
but also the ability, say for collections, to have them as 'text
strings' (ofValues) or displayable elements (ofReferences) to display GUIs.

I'm still waiting for the penny to drop - then eventually bitch, "What
about bloody SORTED COLLECTIONS ?", which from experience were 80% of my
usage. No acknowledgment but then a Sorted Collection class appears
together with an OO Exception Class.

Fed up at this stage and not seeing any apparent input from Micro Focus,
I wrote to Tony Hill the M/F CEO. (He's now gone). As I wrote just
recently his reply, "What do you want me to do ?". I *did* have thoughts
- "Tell J4 to stick their Collection structure where the sun don't shine
!". Whether he passed my comments onto any of his lieutenants, I don't
know. (To be fair, Tony was the CEO and it would be wrong of him to get
involved in the daily nitty-gritty. His prime job was keeping the
shareholders happy - MONEY).

Now back to the J4 Collection Structure. Paraphrase the whole game so
that you have a limited number of classes and down the road you have
'new' problems. (From a Sun Microsystems book, they took two shots at
the Java collection structure to get it right).

Now let's talk the 'real world' using a Procedural W/S Table occurs 'x'
to 'y' depending on 'z'. Can you visualize where such a table would
contain elements for info on Customers, Vendors, Products and say
Weather forecasts. The sensible approach would be four W/S Tables where
you can recognize each individually.

But now J4 has minimal collection classes, so part of the thinking is
'You'd better allow for a collection to hold different types of objects.
What a wacky solution, because you still have to figure out which is
which. Just so happens, Smalltalk and M/F have the class BAG - a
grab-bag. You want to temporarily collect a Customer name, a dozen eggs,
bicycle repair kit, or whatever and you store them as a 'temporary
holding pattern' in a BAG. Logically M/F Collections refer to one type
of object. OK, if you were assembling a p;purchase order (like
Amazon.com) you might have *associated* records, each identified by
(Record) Type, for Customer Name and Address followed by a series of
books or CDs being ordered. Thinking you have done the smart thing by
minimizing the number of class types is not necessarily a good way to go.

PART 2 - The Money World

You and I program to make a living. Hardware and compiler vendors also
want to make money. As Bill has indicated in this Forum, many times, he
is extremely doubtful that compiler only vendors can survive in the long
term - and here we are talking about all the COBOL PC compilers.
(Regrettably Chuck Stevens just got laid off from Unisys - and they are
big iron trying to compete against Big Blue).

You can't do it (PC-wise) just charging developers say $3,500 for their
initial purchase. Say there are 23,000 developers x $3,500  - nice gravy
$80.5 million but that's a one-shot deal. So one way or the other they
get innovative in achieving additional income, and that means
independent developers having to spend more.

DotNet. My understanding is that M/F was initially approached by
Microsoft and turned Bill Gates down, even though they had a good
relationship. Fujitsu jumped into the gap - then quit J4. To be
competitive M/F had to do likewise introducing dotNet with Net Express V
4.0.

As Bill has previously indicated M/F did some pruning probably based on
realistic projections. Firstly Tony Hill left. Then Don Schricker who
was the M/F J4 rep. Little surprising that they would let a key man of
theirs go who has been on J4 almost as a career.

While M/F continuously updates the class structure with each
Fixpack/Upgrade covering OLE, Java etc., nevertheless they ask
themselves how can we reduce our development costs. Well the dotNet
approach is a nice let-out. I don't know whether or not M/F users have
moved in droves to dotNet but I see questions, in the Forum, coming up
more frequently about using the dotNet feature to get at other
languages. Personally I think dotNet is a bit of a death-knell to
PC-COBOL for any vendor. Developers will get the message that by taking
the plunge and getting into other languages they can do all they want.
The next observation is "Why use COBOL at all ?". I know of three
competent OO COBOL programmers who have already arrived at that
conclusion - and they aren't going at dotNet via Net Express !

You use the word STUPID below, so you have in effect already said it. I
wont use the same word back to you - but view what I've written above
and translate your ideas into REAL DOLLARS (OR POUNDS) on behalf of
Micro Focus. I would love it if COBOL had Standard Collections and GUIs
- the latter is definitely never going to happen. Money-wise M/F have
concluded that a revamp of their PROVEN and WORKING Collection structure
just doesn't warrant the cost.

It is NOT as you suggest Bill's position. Having within perhaps the last
month or so discussed his representing them on J4, (Hope they are
picking up the tab for expenses Bill :-) ), he has asked what M/F's
position is on various features not yet implemented. He is the messenger
- passing on their official position; he has no personal axe to grind.

Unlike most of the legalese garbage that occurs in J4 documentation -
Bill's message was clear and precise on behalf of the client he
represents. "Duel ?'. 'Uncivilized ?'. Get real ! Like it or not we live
in a rotten world where gentility has gone by the board. Sadly it's the
bucks that count.


> Having read this paper and others available on this web site, I find
> your submission to be quite, well, I want to say STUPID but I'll just
…[15 more quoted lines elided]…
> OO languages.

What bloody portability ? That went out of the window after COBOL '85.
Have you used M/F support classes. To comply with what you are
suggesting not only would M/F have to revamp every affected class but so
would I, where I AND THEY use pic x(4) comp-5 !
> 
> Short sighted and stupid.  If this really is an official Micro Focus
> position, I would hope that Micro Focus wakes up and realizes that
> instead of attracting customers with this stand they are driving them
> away.

Micro Focus have woken up to the fact that they are not making as much
money as they would wish. Take it this *really* is their official
position. As to losing some customers perhaps - but not the way you are
suggesting - try the dotNet route instead.

A quote from Bill's reply to you :-
.....................................
As far as this being "short-sighted,"  Micro Focus has found that the
amount of
current COBOL-only OO applications is virtually nil.  OO COBOL on
Windows, Unix,
and Linux tends to exist in "mixed language" applications.  Therefore,
as stated
in the paper, MF will continue to work on improving support for such
inter-operability, but will NOT try and enhance COBOL-only (RESTRICTED
to COBOL)
tools (for OO).

It should be noted that IBM, for example, currently only supports OO
COBOL (on
z/OS) in a "Java" environment.  As Java DOES include "collection
classes" - the
need for COBOL-only interfaces is non-existent.  In fact, trying to
force COBOL
semantics on mixed COBOL/Java is counter-productive (for their customers).
....................................

I can only guage by what I see in the M/F Forum. My best guess - in
excess of 90% of people using the Forum depend upon Dialog System -
which has canned templates to handle each of the Windows controls.
Bill's comments kind of cement that observation.

I only know of some five M/F users who truly use OO - and of those two
have gone the dotNet route without using COBOL !

And when it comes to OO, want to run down the list, not sure if I have
them all :-

- Acucorp - niet to date

- CA-Realia - ? Not likely. They will point you at one of their packages
  		other than COBOL

- Fujitsu - yes but also dotNet. They've quit J4. Will be interesting to
		see if they switch to the J4 Collections. Likely because
		of dotNet they will leave their own Collection code
		untouched.

- HP - Probably niet. They quit J4

- IBM - well, via JavaBase

- KOBOL - no mention to date

- Micro Focus - yes but also dotNet

- RM/COBOL - Niet

- Unisys - Niet

- Open Source - Ahhhhhh. Let's gear ourselves to COBOL '85 . It's only
	 21 years-old technology

-----------------------------
Your other message - you are out to lunch.

>>WMK : My experience (both when working for a vendor, working as a 
member of the user
>>group of another vendor, and from years watching this forum) is that 
actual
>>COBOL programmers do NOT code "conforming" COBOL source code, so that
>>"portability" via standardization simply doesn't exist.
…[9 more quoted lines elided]…
> changes) in order to avoid paying out of sight run time fees.

You've got your eyes wide shut on this one. So you've ported to other
COBOLs. How many M/F extensions (and BLOODY USEFUL extensions) did you
chop out to achieve portability. And surely you are referring to
Procedural COBOL, not OO which this is all about. Did you try to port OO
code - what exactly did you do with pic x(4) comp-5, consistently
referenced using GUIs and Collections in M/F ?

Back in Thane's discussion group, Pete Dashwood made reference to pic
9(09) comp-5 a feature of the as yet unpublished Standard, available in
Fujitsu and certainly available in M/F. Seemed Pete made a sensible 
comment so I switched all my programs from  pic x(4) to pic 9(09)comp-5 
- and finished up with an unmitigated disaster - I had to switch the 
programs back to pic x(4) comp-5. (And while the Standard acknowledges 
comp-5, would it have been a big deal to have allowed pic x(4) comp-5 as 
a short-cut ?).

I don't know if I have ever said this as bluntly before - but where M/F 
is concerned, with no proof, I get the impression others on J4 are just 
out to screw them on some of their innovations.

(BTW I *do* like avoiding the runtime fees - but what am I supposed to
do, drop OO to achieve this ?
>
>
>>As far as this being "short-sighted,"  Micro Focus has found that the 
amount of
>>current COBOL-only OO applications is virtually nil.  OO COBOL on 
Windows, Unix,
>>and Linux tends to exist in "mixed language" applications. 
Therefore, as stated
>>in the paper, MF will continue to work on improving support for such
>>inter-operability, but will NOT try and enhance COBOL-only 
(RESTRICTED to COBOL)
>>tools (for OO).
>
…[13 more quoted lines elided]…
>
Got news for you. I used to code SOLELY in OO classes with the exception
of the Procedural Trigger program. As indicated earlier, please bear in
mind the "OO-four" produced OO compilers while J4 sat upon their hands,
way before there was a Standard. Your reference to the ISO2000 directive
is correct - it is purely cosmetic to get the 'look and feel' of the
Repository syntax. No point in belabourig that point, if you want
Repository get N/E V 4.0 onwards.  (The thing to really note about that
Directive is that it was an attempt by M/F to comply with the latest
deliberations from J4. Note the year of the directive 2000 - it took 
until COBOL 2002 before we had the Standard that his directive was aimed 
at, as an interim. Went checking to try and find when the directive was 
first introduced - let's go with '97 (97 to 2000) as opposed to actual 
('97 to 2002).

To check went to Will Price 'Elements of OO ' First Edition, published 
1997. Didn't confirm introduction date for that directive, but in doing 
so turned up this :-

"Figure 10-7 is a hierarchical list of collection classes of the 
Standard collection class library as described in a March 1996 ISO document.

        Collection
           Bag
           Identity-set
             Identity-table
               Identity-dictionary
             Value-set
               Value-table
                   Value-dictionary
               Sorted-set
               Ordered-set
                   Ordered-table
                      Ordered-dictionary
           Ordered-collection
              List
              Queue
              Stack


Without repeating his diagram for the M/F grouping, with name changes, 
it is fairly close.

So who got it right ? (a) J4 who passed the above on to WG4 in '96, 
which M/F fairly closely emulated, or (b) J4 after the year 2000 
dreaming up an entirely new set ?
			
	
As to Micro Focus doing their own thing - based on what were perceived
as firm upcoming J4 changes, M/F added features in advance (Procedural,
not necessarily OO). As Bill pointed out quite a while back, they got
burned on this one; somebody at J4 managed to put a little twist on the
new feature which screwed M/F. Possibly the enhancement may even have
been canceled.

Let me emphasis this is not in support of M/F - they can look after 
their own bailly-wicket. Just my perception of the current state. Yes it 
most certainly is in defence of Bill, who has always been of the frame 
of mind taking an impartial look to get the best out of both Procedural 
and OO COBOL - not that he actually needs defending; he is quite capable 
of doing his own thing. I just don't like to see him inaccurately maligned.

Believe me I am truly pissed off at costs and runtime fees - which 
contributed to my giving up on the programming game !!!!

Jimmy
```

#### ↳ Re: Micro Focus position on the "Standardized" OO Collection Class Technical Report

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-27T11:44:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154025871.905796.55890@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`
- **References:** `<CJ_xg.122869$tQ4.48006@fe01.news.easynews.com>`

```

William M. Klein wrote:

>      http://www.cobolstandard.info/j4/files/06-0076.doc

Don't you think that it is ironic that a standards committee that is
tasked with providing a fully documented, publically available standard
to ISO is using a closed, undocumented, single vendor, single platform,
proprietry format for its communications ?.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
