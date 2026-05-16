[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WRITE ADVANCING

_26 messages · 13 participants · 2009-09_

---

### WRITE ADVANCING

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-09-17T05:56:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>`

```
OK,
  Let's go back to COBOL and the days of "line printers" or their equivalent <G>

This is a follow-up on ongoing thread in the OC forum.

There is a question about what happens (should happen) in the case of a program 
that combines WRITER AFTER ADVANCING with WRITE BEFORE ADVANCING to the same 
file.

I thought that there used to be some warnings about this, i.e. that "results may 
be unpredictable or at least undesirable" if you mixed these two.  However, I 
can't find any. (Standard or user documentation)

Does anyone know of any "official" warnings about this?

I may be thinking of combining the (old) IBM extension "WRITE AFTER POSITIONING" 
with "WRITE AFTER ADVANCING" - but I don't know.
```

#### ↳ Re: WRITE ADVANCING

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-17T13:31:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tdms$lcf$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>`

```
In article <EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>OK,
>  Let's go back to COBOL and the days of "line printers" or their equivalent <G>
…[5 more quoted lines elided]…
>file.

I do not recall ever using WRITE BEFORE ADVANCING... the only grounds for 
doing so that come to mind would be for emphasis or underlining or the 
like, in which case I was taught to use WRITE AFTER ADVANCING 0.

[SNIP]

>I may be thinking of combining the (old) IBM extension "WRITE AFTER
>POSITIONING" 
>with "WRITE AFTER ADVANCING" - but I don't know.

That (AFTER POSITIONING), as my admittedly porous memory has it, dealt 
with defining the first character of a print file (DCB=FBA, etc) and 
specifically addressing it with one of the arcane control-codes because 
the programmer did not want to deal with SPECIAL-NAMES.

According to 
<http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGYM1101/4.4?SHELF=&DT=19930312152044&CASE=> 
the WRITE AFTER POSITIONING statement was not supported under VS COBOL 
II... but that was only twenty or so years ago so it might be called 
'moderately recent'.

DD
```

##### ↳ ↳ Re: WRITE ADVANCING

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-17T08:38:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rci4b556svl020dh37qeqjjkse225nu2so@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com>`

```
On Thu, 17 Sep 2009 13:31:08 +0000 (UTC), docdwarf@panix.com () wrote:

>That (AFTER POSITIONING), as my admittedly porous memory has it, dealt 
>with defining the first character of a print file (DCB=FBA, etc) and 
>specifically addressing it with one of the arcane control-codes because 
>the programmer did not want to deal with SPECIAL-NAMES.

My AFTER POSITIONING experience was to match the paper tapes that were
placed in the printers for various forms.
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-09-17T11:38:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s7l4b5lh3a56ejhe1m7tmaigvqdncqmg7v@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <rci4b556svl020dh37qeqjjkse225nu2so@4ax.com>`

```
On Thu, 17 Sep 2009 08:38:02 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Thu, 17 Sep 2009 13:31:08 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[6 more quoted lines elided]…
>placed in the printers for various forms.

My memory says it was used to skip either a number of lines or to a
particular channel.  For example, if you said WRITE PRINT-REC AFTER
POSITIONING 0 , it would double space.  If you said ....AFTER
POSITIONING +, it would suppress spacing.  If 1 through 9 were used,
it would skip to channel 1 through 9 respectively.  Or if you used A,
B or C, it would skip to channel 10, 11, or 12 respectively.

However, if you add the word LINES after the integers (0, 1, 2, 3)
you'd get an eject, single space, double space, triple space
respectively.

Furthermore, if you were writing to an IBM 1442 and said .....AFTER
POSITIONING V (or W), it would select pocket 1 (or 2).

Regards,
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-17T09:51:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<llm4b5pafa1ree6oombcsgmbn7g3u4024f@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <rci4b556svl020dh37qeqjjkse225nu2so@4ax.com> <s7l4b5lh3a56ejhe1m7tmaigvqdncqmg7v@4ax.com>`

```
On Thu, 17 Sep 2009 11:38:40 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>My memory says it was used to skip either a number of lines or to a
>particular channel.  For example, if you said WRITE PRINT-REC AFTER
…[10 more quoted lines elided]…
>POSITIONING V (or W), it would select pocket 1 (or 2).

You've jogged similar memories for me.

Speaking of memory, I certainly don't remember many of my earliest
SELECT ASSIGN statements, as even back then, I never actually *wrote*
those from scratch.
```

##### ↳ ↳ Re: WRITE ADVANCING

- **From:** Charlie <foxgrove@shaw.ca>
- **Date:** 2009-09-17T12:19:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9950f8d-bcc2-4181-8664-2af0c957f558@i4g2000prm.googlegroups.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com>`

```
[SNIP]
>
> I do not recall ever using WRITE BEFORE ADVANCING... the only grounds for
…[4 more quoted lines elided]…
>

Back in the day... Honeywell 120....  We always tried to use BEFORE
ADVANCING and avoided AFTER ADVANCING.  Printing was directly to the
printer.  With BEFORE your line would print during one rotation of the
print drum and then the paper would feed.  Control returned to your
program while the paper was moving.  With AFTER the paper would move,
then the line would print with control returned to you program after
the line started printing.  Paper movement was relatively slow,
compared to a single drum rotation.  Using BEFORE was much quicker as
your program could proceed while the paper was moving.
```

##### ↳ ↳ Re: WRITE ADVANCING

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2009-09-18T00:47:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com>`
- **In-Reply-To:** `<h8tdms$lcf$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> (snip) 
> That (AFTER POSITIONING), as my admittedly porous memory has it, dealt 
…[11 more quoted lines elided]…
> 

Wow!  Thanks for posting that link.

I was amazed at all the differences between OS/VS COBOL and VS COBOL II, 
and that most of them were features I never used or situations I never 
encountered.  I certainly was not aware of them at the time.  How did we 
ever manage the conversion?
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

- **From:** PatH <phall@certcoinc.com>
- **Date:** 2009-09-18T04:46:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<711f0d79-110d-4ee2-8904-09fbc02166db@l34g2000vba.googlegroups.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com>`

```

>
> Wow!  Thanks for posting that link.
…[6 more quoted lines elided]…
> --http://arnold.trembley.home.att.net/


When we converted to COBOL for VSE/ESA  I thought things would be much
worse.  Turns out I was not very imaginative in my use of some of the
more exotic parts of COBOL so the conversion was relatively easy.
Guess there is something to be said for 'meat and potatoes' coding.

PatH
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-18T13:42:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h902oa$t66$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com> <711f0d79-110d-4ee2-8904-09fbc02166db@l34g2000vba.googlegroups.com>`

```
In article <711f0d79-110d-4ee2-8904-09fbc02166db@l34g2000vba.googlegroups.com>,
PatH  <phall@certcoinc.com> wrote:

[snip]

>Guess there is something to be said for 'meat and potatoes' coding.

There is something to be said for 'Look, Ma, I'm a Programmer!' coding... 
but the language might not be suited for a Family Newsgroup.

(I ran across a fellow who discovered the 66 RENAMES and suddenly found 
uses for it Absolutely Everywhere... in 1996.  His misuse of it in the 
LINKAGE SECTION started to cause *my* programs to blow up; when I 
attempted a Friendly Discussion About Coding Consistency he said that we 
should 'step out into the parking lot' and settle this.

Note to non-native speakers - an offer to exit a building for a 
discussion, eg 'You want to step outside and say that?', is, in the United 
States of America, a colloquialism which quite often is a prelude to a 
physical confrontation.  When it is made by a man who stands six inches 
taller and weighs a good fifty pounds more than I then I conclude, rightly 
or wrongly, that the Marquis of Queensbury's Rules should not apply to my 
response.)

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 5)_

- **From:** PatH <phall@certcoinc.com>
- **Date:** 2009-09-18T07:03:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55436040-a16f-4a43-9e1e-76b6462974b9@a6g2000vbp.googlegroups.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com> <711f0d79-110d-4ee2-8904-09fbc02166db@l34g2000vba.googlegroups.com> <h902oa$t66$1@reader1.panix.com>`

```
On Sep 18, 8:42 am, docdw...@panix.com () wrote:
> In article <711f0d79-110d-4ee2-8904-09fbc0216...@l34g2000vba.googlegroups.com>,
>
…[7 more quoted lines elided]…
> but the language might not be suited for a Family Newsgroup.


Ahh shouldn't that be 'Look, Ma, I'm a Programmer!  YeeHaa!!'  LOL

PatH
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-18T13:28:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h901u5$4jo$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tdms$lcf$1@reader1.panix.com> <w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com>`

```
In article <w6OdnR0gqN9Cgy7XnZ2dnUVZ_s-dnZ2d@giganews.com>,
Arnold Trembley  <arnold.trembley@att.net> wrote:
>docdwarf@panix.com wrote:

[snip]

>> According to 
>>
…[5 more quoted lines elided]…
>Wow!  Thanks for posting that link.

Shucks... t'warn't nothin'.  A page I find *really* useful is 
http://publib.boulder.ibm.com/cgi-bin/bookmgr/LIBRARY .

>
>I was amazed at all the differences between OS/VS COBOL and VS COBOL II, 
>and that most of them were features I never used or situations I never 
>encountered.  I certainly was not aware of them at the time.  How did we 
>ever manage the conversion?

I'm not sure about 'we'... but many places I worked (usual caveat about 
'sick shops' applies) ignored it.  They ran OS/VS COBOL as much as they 
could and when they Absolutely Had To their 'conversion strategy' 
consisted of 'programs that need compiling will now use IGYCRCTL, anything 
else will remain untouched'...

... until they started to run into conflicts between the lower-level 
subroutines (ILB0 vs IGZY) and programs that had been running just 
fine for years began blowing up with S0C4s on READs.

From what I saw... places really didn't make serious efforts to shift away 
from OLDBOL until Y2K remediation began.

DD
```

#### ↳ Re: WRITE ADVANCING

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-09-17T13:44:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tefk$ous$1@news.eternal-september.org>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>`

```
In article <EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
>OK,
>  Let's go back to COBOL and the days of "line printers" or their equivalent
…[6 more quoted lines elided]…
>file.

What happens, or should happen, is that the compiler issues a diagnostic, and 
produces no object file. You mean there are compilers that permit this??
>
>I thought that there used to be some warnings about this, i.e. that "results  may 
…[3 more quoted lines elided]…
>Does anyone know of any "official" warnings about this?

Tandem COBOL won't compile it. 
Honeywell GCOS/8 COBOL won't compile it.
Neither would IBM DOS/VSE COBOL, IIRC.
```

##### ↳ ↳ Re: WRITE ADVANCING

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-17T14:22:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tgnl$qm0$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tefk$ous$1@news.eternal-september.org>`

```
In article <h8tefk$ous$1@news.eternal-september.org>,
Doug Miller <spambait@milmac.com> wrote:
>In article <EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>, "William
>M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

[snip]

>>Does anyone know of any "official" warnings about this?
>
>Tandem COBOL won't compile it. 
>Honeywell GCOS/8 COBOL won't compile it.
>Neither would IBM DOS/VSE COBOL, IIRC.

Code:

IF TKNO-CNT > ZERO                                 
    MOVE TKNO-CNT TO FT1-TOTAL                           
    WRITE LEAVE-RCD FROM FOOTER-1 AFTER ADVANCING 2 LINES
END-IF                                                   
IF TKNO-CNT < ZERO                                 
    MOVE TKNO-CNT TO FT1-TOTAL                           
    WRITE LEAVE-RCD FROM FOOTER-1 AFTER BEFORE           
      ADVANCING 2 LINES
END-IF

Compiled with G53 IBM Enterprise COBOL for z/OS  3.4.1.

Compile RC = 12, message:

IGYPS2106-S   "BEFORE" was found in the "WRITE" statement.  It was not 
allowed in this context.  The statement was discarded.

Conclusion: sounds kind of 'official' aye.

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-09-17T11:56:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GStsm.180386$O23.92961@newsfe11.iad>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tefk$ous$1@news.eternal-september.org> <h8tgnl$qm0$1@reader1.panix.com>`

```
Oooooh, Doc.  "AFTER BEFORE ADVANCING"!

I can't see what the problem is here.  You can't bollix the printer - it'll
do what you say, mixing befores & afters with equinamity.  I have very
rarely used "before" - AFAICR it was to handle headings in special forms
situations - but I've never encountered a situation (or a compiler) which
objected to using both in the same file.

Enlighten me, please!

PL

<docdwarf@panix.com> wrote in message news:h8tgnl$qm0$1@reader1.panix.com...
> In article <h8tefk$ous$1@news.eternal-september.org>,
> Doug Miller <spambait@milmac.com> wrote:
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-17T17:12:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tqlu$rmq$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tefk$ous$1@news.eternal-september.org> <h8tgnl$qm0$1@reader1.panix.com> <GStsm.180386$O23.92961@newsfe11.iad>`

```
In article <GStsm.180386$O23.92961@newsfe11.iad>, tlmfru <lacey@mts.net> wrote:
>Oooooh, Doc.  "AFTER BEFORE ADVANCING"!

Wahoo, Mr Lacy... no wonder there was a bit of trouble (and no wonder why 
I post code so another set of eyes can debug).

Let me try that one again:

Compiling with G53 IBM Enterprise COBOL for z/OS  3.4.1 :

code:

IF TKNO-CNT GREATER ZERO                                
    MOVE TKNO-CNT TO FT1-TOTAL                          
    WRITE LEAVE-RCD FROM FOOTER-1 AFTER ADVANCING 2 LINE
END-IF                                                  
IF TKNO-CNT GREATER ZERO                                
    MOVE TKNO-CNT TO FT1-TOTAL                          
    WRITE LEAVE-RCD FROM FOOTER-1                       
      BEFORE ADVANCING 2 LINES                          
END-IF                                                  

Log message for COMP step:

UIDCP511 COMP - STEP WAS EXECUTED - COND CODE 0000

End of compile listing messages:

* Statistics for COBOL program TESTPROG:                     
*    Source records = 2270                                   
*    Data Division statements = 1649                         
*    Procedure Division statements = 239                     
End of compilation 1,  progam TESTPROG,  highest severity 0.
Return code 0                                                

Conclusion: the compiler returns no error for a combination of 'AFTER 
ADVANCING' and 'BEFORE ADVANCING' when coded in this manner.

Thanks again, Mr Lacy.

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 5)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2009-09-26T23:04:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9m6l5$e79$1@theodyn.ncf.ca>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tefk$ous$1@news.eternal-september.org> <h8tgnl$qm0$1@reader1.panix.com> <GStsm.180386$O23.92961@newsfe11.iad> <h8tqlu$rmq$1@reader1.panix.com>`

```
 (docdwarf@panix.com) writes:
> In article <GStsm.180386$O23.92961@newsfe11.iad>, tlmfru <lacey@mts.net> wrote:
>>Oooooh, Doc.  "AFTER BEFORE ADVANCING"!
…[38 more quoted lines elided]…
> DD

But the BEFORE text will overwrite the line of AFTER text, even
if MIXING BEFORE and AFTER works "as expected".

That may be what the programmer intended, but would a different
person maintaining the code spot that immediately?

Some vendors seem set against mixing and matching. I'd call it bad
style, but expect it to work. I haven't seen a Honeywell compiler
since 1980, but I do recall that HIS GCOS 4js had a 100% overhead
for WRITE AFTER. I'd always write long reports to disk or tape so
that they could be reprinted if the printer mangled them or of a
page got lost in the mail. I found long HIS COBOL 74 reports took
up twice as much space and printed slowly. Browsing the files
revealed that it generated pairs of print records for WRITE AFTER.
The first record would have the requested paper movement command
followed by a second reord with a null slew and the text data. The
impact printer speed seemed noticeably slower than WRITE BEFORE
output.

When we converted from HIS COBOL 74 to IBM's COBOL 68 some folks
spent a lot of time convering WRITE BEFORE to WRITE AFTER. My
recollection is that if your print files were FBM or VBM
there wasn't much difference. IBM had Machine Control Codes
for both BEFORE and AFTER.

I led the migration to VS COBOL II at our data center in the late
1980s, and don't recall any issue with either BEFORE or AFTER
not being supported. There were enough of both that I would
have expected it to come up. We did leave it till late, perhaps
it was an issue with earlier releases of VS COBOL II.

How common is/was WRITE BEFORE? With impact printers in the 1980s
our site had programmers go to what seem like a lot of trouble
to code a few programs to print then slew, squeezing  a few %
faster speed out of the line printers for particularly long 
reports. In general it seemed more complex to code the programs
for doing that.
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-28T13:30:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9qdpm$ijb$2@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <GStsm.180386$O23.92961@newsfe11.iad> <h8tqlu$rmq$1@reader1.panix.com> <h9m6l5$e79$1@theodyn.ncf.ca>`

```
In article <h9m6l5$e79$1@theodyn.ncf.ca>,
Kelly Bert Manning <bo774@FreeNet.Carleton.CA> wrote:
> (docdwarf@panix.com) writes:


>> Wahoo, Mr Lacy... no wonder there was a bit of trouble (and no wonder why 
>> I post code so another set of eyes can debug).
…[31 more quoted lines elided]…
>> ADVANCING' and 'BEFORE ADVANCING' when coded in this manner.

[snip]

>But the BEFORE text will overwrite the line of AFTER text, even
>if MIXING BEFORE and AFTER works "as expected".

More research would have to be done to see the results of mixing AFTERs 
and BEFOREs prior to my coming to a conclusion about that, Mr Manning.  My 
concern was merely 'will it compile?', not 'what will be the printed 
results.'

(durned programmers and their precision and all that, I know)

>
>That may be what the programmer intended, but would a different
>person maintaining the code spot that immediately?

My experience is limited, granted... but I have never, to the best of my 
porous recollection, had to maintain a BEFORE ADVANCING statement and have 
written, in my own code, *only* AFTERs... makes life a bit easier, I'd 
say.

>
>Some vendors seem set against mixing and matching. I'd call it bad
>style, but expect it to work. I haven't seen a Honeywell compiler
>since 1980, but I do recall that HIS GCOS 4js had a 100% overhead
>for WRITE AFTER.

This may well have been the case... and it also may be that things have 
changed a bit in the intervening three decades or so.

[snip]

>When we converted from HIS COBOL 74 to IBM's COBOL 68 some folks
>spent a lot of time convering WRITE BEFORE to WRITE AFTER.

This is odd... I wonder what the rationale would have been to devote 
resources, both human and machine, to converting to what you've described 
as a less-efficient method.  Maybe that's why I never went Management.

[snip]

>How common is/was WRITE BEFORE?

As stated above, from my experience, both maintaining and developing, 0% 
BEFORE and 100% AFTER.

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-28T10:34:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sbp1c591mrpg7234g31lmtdlcnks03eutq@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <GStsm.180386$O23.92961@newsfe11.iad> <h8tqlu$rmq$1@reader1.panix.com> <h9m6l5$e79$1@theodyn.ncf.ca> <h9qdpm$ijb$2@reader1.panix.com>`

```
On Mon, 28 Sep 2009 13:30:30 +0000 (UTC), docdwarf@panix.com () wrote:

>As stated above, from my experience, both maintaining and developing, 0% 
>BEFORE and 100% AFTER.

How about Report Writer?
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-28T17:30:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9qrrv$p9c$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h9m6l5$e79$1@theodyn.ncf.ca> <h9qdpm$ijb$2@reader1.panix.com> <sbp1c591mrpg7234g31lmtdlcnks03eutq@4ax.com>`

```
In article <sbp1c591mrpg7234g31lmtdlcnks03eutq@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 28 Sep 2009 13:30:30 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[3 more quoted lines elided]…
>How about Report Writer?

0% Report Writer.

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-09-28T22:36:50-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cvo2c5lj4o7cb914bkuaofg7surd1qehp5@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <GStsm.180386$O23.92961@newsfe11.iad> <h8tqlu$rmq$1@reader1.panix.com> <h9m6l5$e79$1@theodyn.ncf.ca> <h9qdpm$ijb$2@reader1.panix.com>`

```
On Mon, 28 Sep 2009 13:30:30 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <h9m6l5$e79$1@theodyn.ncf.ca>,
>Kelly Bert Manning <bo774@FreeNet.Carleton.CA> wrote:
…[82 more quoted lines elided]…
>BEFORE and 100% AFTER.

I used WRITE BEFORE on the RCA 301 and was surprised by the WRITE
AFTER when I started with the IBM 360 on DOS.  What was of minor
interest was that the printer command codes used in the CCWs were
print and advance or WRITE BEFORE.  My recollection of the gory
details is not great but a posting from the Green card of the time
could refresh my memory. 
>
>DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-09-18T11:43:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aNOsm.129375$nL7.115746@newsfe18.iad>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tefk$ous$1@news.eternal-september.org> <h8tgnl$qm0$1@reader1.panix.com> <GStsm.180386$O23.92961@newsfe11.iad>`

```

tlmfru <lacey@mts.net> wrote in message
news:GStsm.180386$O23.92961@newsfe11.iad...
> Oooooh, Doc.  "AFTER BEFORE ADVANCING"!
>
> I can't see what the problem is here.  You can't bollix the printer -
it'll
> do what you say, mixing befores & afters with equinamity.  I have very
> rarely used "before" - AFAICR it was to handle headings in special forms
…[6 more quoted lines elided]…
>

I should add that after reflecting, I remember that I wrote one program
using "before" exclusively, just to annoy a programmer on the staff who
positively broke out in warts if anyone used an "inefficient" method, of
anything.  He went berserk!   It was a weekly program that produced one page
of output so it really didn't matter.  Oooh that was fun.

PL
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-18T17:01:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h90edg$f88$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tgnl$qm0$1@reader1.panix.com> <GStsm.180386$O23.92961@newsfe11.iad> <aNOsm.129375$nL7.115746@newsfe18.iad>`

```
In article <aNOsm.129375$nL7.115746@newsfe18.iad>,
tlmfru <lacey@mts.net> wrote:

[snip]

>I should add that after reflecting, I remember that I wrote one program
>using "before" exclusively, just to annoy a programmer on the staff who
>positively broke out in warts if anyone used an "inefficient" method, of
>anything.  He went berserk!   It was a weekly program that produced one page
>of output so it really didn't matter.  Oooh that was fun.

Leaving aside the all-too-human enjoyment of occaisionally inflicting bits 
of petty sadism on Those Who Really Deserve It... this caused me to think 
about two things:

1) If Mr Efficiency was so concerned maybe it was time to compile with a 
PMAP and ask to see where additional costs were being incurred, calculate 
these costs per run and then compare those costs to the costs of 
re-coding, re-testing and implementing to Prod something more efficient.  
(As you mentioned, a weekly job with one page of output)

2) I was taught that - in most cases, there are exceptions to every rule, 
including this one - that writing a report to disk and then printing the 
dataset with a utility (eg, IEBGENER) would, in the long run, prove to be 
cheaper than re-running the report when delivery-clerk misdirected a copy 
or a Corner-Office Idiot lost it and blithely ordered 'Oh, just re-run the 
job'... ESPECIALLY when it was a job that updated things.

DD
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-18T11:37:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34h7b5lii27u2siqtmg81g29j9ko2ced7g@4ax.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <h8tgnl$qm0$1@reader1.panix.com> <GStsm.180386$O23.92961@newsfe11.iad> <aNOsm.129375$nL7.115746@newsfe18.iad> <h90edg$f88$1@reader1.panix.com>`

```
On Fri, 18 Sep 2009 17:01:36 +0000 (UTC), docdwarf@panix.com () wrote:

>1) If Mr Efficiency was so concerned maybe it was time to compile with a 
>PMAP and ask to see where additional costs were being incurred, calculate 
…[9 more quoted lines elided]…
>job'... ESPECIALLY when it was a job that updated things.

A very good point.   Analyzing the program for efficiency is not
sufficient.   The program is just part of the process of getting data
to (and/or from) those who need the data.   Including delivery-clerk
mishaps into the analysis isn't easy to put a number on - but it's
real life.
```

###### ↳ ↳ ↳ Re: WRITE ADVANCING

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-18T17:45:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h90h0n$rv5$1@reader1.panix.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com> <aNOsm.129375$nL7.115746@newsfe18.iad> <h90edg$f88$1@reader1.panix.com> <34h7b5lii27u2siqtmg81g29j9ko2ced7g@4ax.com>`

```
In article <34h7b5lii27u2siqtmg81g29j9ko2ced7g@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>Analyzing the program for efficiency is not
>sufficient.   The program is just part of the process of getting data
>to (and/or from) those who need the data.   Including delivery-clerk
>mishaps into the analysis isn't easy to put a number on - but it's
>real life.

I don't know about this 'real life' stuff... but I've shops where a 
Corner-Office Idiot didn't get a report, barked 'run the job again'... and 
all the inventory-reductions got double-posted.

DD
```

#### ↳ Re: WRITE ADVANCING

- **From:** "Damian J. Thomas" <damian.thomas@unisys.com>
- **Date:** 2009-09-17T11:27:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h8tv1m$1lm3$1@si05.rsvl.unisys.com>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message 
news:EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com...
> There is a question about what happens (should happen) in the case of a 
> program that combines WRITER AFTER ADVANCING with WRITE BEFORE ADVANCING 
> to the same file.

With the Unisys MCP COBOL74 and COBOL85 compilers,
WRITE AFTER ADVANCING and WRITE BEFORE ADVANCING are both allowed 
separately.
Mixing BEFORE and AFTER in the same WRITE statement is not allowed.

Damian Thomas
(I do not speak for my employer.  These are my opinions only.)
```

#### ↳ Re: WRITE ADVANCING

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2009-09-19T14:43:04
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1253367784@f1.n250.z2.fidonet.ftn>`
- **References:** `<EBosm.28421$GS3.19497@en-nntp-07.dc1.easynews.com>`

```
Hello William!

17 Sep 09 11:56, William M. Klein wrote to All:

 WMK> There is a question about what happens (should happen) in the case of
 WMK> a program that combines WRITER AFTER ADVANCING with WRITE BEFORE
 WMK> ADVANCING to the same file.

In a stack of program/modules rewritten for OC I have both during production 
of the page headings depending if it is page one i.e., issuing a write 
printline after page will waste one sheet of paper despite it being at topo of 
form when using a laser or inkjet type printer. So I issue write before's on 
page one and replace 'before page' with 'before 1' during the first 2 lines of 
the headings. line 3 to whatever then reverts to standad eg write after having 
printed a blank line to sync up the two styles.

This works well, as one would expect.  You might well be referring to 
'positioning' for which I do not recall using let alone having problems with 
but there again I don't remember too much of the early 60's and Cobol 
programming.

Its hard enough going from one room to another and trying to remember why :)

[And that is not so much a joke]

Vince
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
