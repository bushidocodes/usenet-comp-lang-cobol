[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# number of days between dates

_76 messages · 24 participants · 2001-01 → 2001-02_

---

### Re: number of days between dates

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-01-04T08:14:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A54304E.EFC47152@worldnet.att.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net>`

```
mangogrower wrote:
> 
> The way I learned it and according to Pope Gregory who created the Gregorian
…[15 more quoted lines elided]…
>                         is LEAP-YEAR.

Don't forget "else is NOT Leap-year".

Actually, someone whose name I forgot posted a more simple and clever
algorithm in comp.lang.cobol a couple of years ago.

05  YEAR-YYYY        PIC 9(04) USAGE IS DISPLAY.
05  YEAR-CCYY        REDEFINES YEAR-YYYY.
    10  YEAR-CC      PIC 9(02) USAGE IS DISPLAY.
    10  YEAR-YY      PIC 9(02) USAGE IS DISPLAY.

IF YEAR-YY EQUAL ZERO
    DIVIDE YEAR-CC BY 4 GIVING USELESS-JUNK REMAINDER LEAP-YEAR-TEST
ELSE
    DIVIDE YEAR-YY BY 4 GIVING USELESS-JUNK REMAINDER LEAP-YEAR-TEST
END-IF

IF LEAP-YEAR-TEST EQUAL ZERO
    MOVE 'Y' TO LEAP-YEAR-FLAG
ELSE
    MOVE 'N' TO LEAP-YEAR-FLAG
END-IF

Notice we now have only ONE divide statement and two IF statements,
while the direct approach has THREE divide statements and THREE IF
statements to determine that 2001 is not a leap year.  I believe this
approach results in more efficient code and correctly implements the
4-year rule, the 100-year rule, and the 400-year rule.  It should work
until they have to correct the calendar for more drift, probably in 1200
years or so.
```

#### ↳ Re: number of days between dates

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-04T09:22:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A54A330.8BFB87F0@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net>`

```
>     DIVIDE YEAR-CC BY 4 GIVING USELESS-JUNK REMAINDER LEAP-YEAR-TEST

The main thing to be learned by this problem is that the code above works the same
in all environments.  No compiler options are needed, no worrying about how
fractions are handled.  No worrying whether some future maintenance programmer
will know how fractions are handled.

When someone walks through the code, plugging in values, he doesn't have to pull
out a manual to verify what happens with intermediate values within a compute
statement.  He doesn't have to check to see what compiler options were used.  He
doesn't have to worry about someone making a completely separate maintenance
change which breaks his code when compiled with different options.
```

#### ↳ Re: number of days between dates

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-07T13:08:06+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<938dom$1q0$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net>`

```

Arnold Trembley wrote in message <3A54304E.EFC47152@worldnet.att.net>...
<Snipped>
>Actually, someone whose name I forgot posted a more simple and clever
>algorithm in comp.lang.cobol a couple of years ago.
…[16 more quoted lines elided]…
>END-IF


I like this solution very much. It will run on just about ANY machine and
compiler options are not going to make any difference to it.

However, it is NOT a good example of  modern COBOL code and, as there are a
number of new COBOL programmers who frequent this forum I suggest it be
amended as follows:

01   year-yyyy.
       12  year-cc pic 99.
       12  year-yy pic 99.
[there is no need for the redefinition, and usage defaults to DISPLAY...]

01   leap-year-flag  pic x value space.
        88 its-a-leap-year    value '1'.
        88 its-NOT-a-leap-year value '0'.

01  leap-year-test pic 9.
       88 no-remainder  value zero.

01  useless-junk    pic 99.

...

if year-yy = zero
   divide year-cc by 4
               giving useless-junk
               remainder leap-year-test
else
   divide year-yy by 4
               giving useless-junk
               remainder leap-year-test
end-if

if no-remainder
   set its-a-leap-year to TRUE
else
   set its-NOT-a-leap-year to TRUE
end-if

if its-a-leap-year
      [etc....]

[Please, please, newbies, resist the urge to set flags to 'Y' or 'N'. Use 88
levels; that's what they're for. COBOL is intended to be a Self-Documenting
Language... Besides, it is arrogant to assume the whole world uses "Yes" and
"No"  (it doesn't) and, in terms of pure logic, "1" and "0" are better
Boolean representations of a truth value.)

Unfortunately, not all implementations of COBOL allow a value to be set to
FALSE, so it is necessary to provide for both TRUE and FALSE with 88 levels,
then set the required one to TRUE, as shown above.

Also, where your environment supports it, use lower case ("there's no need
to SHOUT") as it is easier on the eyes than Upper Case.]

Pete.
```

##### ↳ ↳ Re: number of days between dates

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-07T02:31:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz>`

```

"Peter E. C. Dashwood" <dashwood@enternet.co.nz

For a contrary view:

> [Please, please, newbies, resist the urge to set flags to 'Y' or
'N'. Use 88
> levels; that's what they're for. COBOL is intended to be a
Self-Documenting
> Language... Besides, it is arrogant to assume the whole world uses
"Yes" and
> "No"  (it doesn't) and, in terms of pure logic, "1" and "0" are
better
> Boolean representations of a truth value.)

Please, please, newbies, use "Y" or "N" as flag values (or "YES" and
"NO" or "YA" and "NEIN" or "YEP" and "NOPE"). Zero and 1 are
ambigious, have no relation to reality, mean nothing in ordinary
discourse ("Are you ready for lunch?" "One!"), and only pendantic
fuddie-duddies care whether they are the true members of the Boolean
Tribe.
>
> Unfortunately, not all implementations of COBOL allow a value to be
set to
> FALSE, so it is necessary to provide for both TRUE and FALSE with 88
levels,
> then set the required one to TRUE, as shown above.

There you are. See, not even COBOL has much use for the artificial
constructs of 0 and 1 (or is it -1 and 0, or -1 and +1, or 0 and
non-zero, I forget).

>
> Also, where your environment supports it, use lower case ("there's
no need
> to SHOUT") as it is easier on the eyes than Upper Case.]

Also, except in literals and comments, use ALL CAPS when writing COBOL
code. The name COBOL is in caps and the code was meant to be written
that way. By using caps you are guaranteed cross-compiler / platform
compatibility. Programs are easier to digest. Mistakes are easier to
find. Listings in teeny type are easier to read. Caps in code are much
easier on older eyes.
```

###### ↳ ↳ ↳ Upper/Mixed-case source code (was: number of days between dates

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-06T20:54:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<938lnh$lp4$1@slb7.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
"Jerry P" <jerryp@bisusa.com> wrote in message
news:QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net...
>
 <snip>
>
> Also, except in literals and comments, use ALL CAPS when writing COBOL
…[6 more quoted lines elided]…
>

Just a personal opinion,
  If you are using a COBOL (yes, it is COBOL not Cobol) compiler that does
NOT support mixed-case source code, then

A) Make certain that you are being PAID a lot of money to work with
something that was out-of-date 15 years ago <G>

  or

B) Get a new compiler !!!

Mixed case source code is ENTIRELY portable to any compiler that supports
the '85 ANSI Standard.  It is only "old" (pre-85, i.e. '74 or '68) Standard
compilers that cannot "happily" support mixed case source code.

P.S.  I am visually impaired (which is how/why I am on long term disability)
and find "mixed case" to be MUCH easier to read and process than all
upper-case.  (Unless I do want to SHOUT - which sometimes I do.)
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** "Russell Styles" <RWSTYLES01@CS.COM>
- **Date:** 2001-01-07T00:09:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<938tn1$hn8$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
    Let's be honest - if the original programmer spoke
German (or whatever), then the chances are that
most of the comments and data names are
going to be gibberish to you.  The fact that they
use something other than "Y" to mean YES or ON
is the least of your problems.

    So far as using 0 and 1, which is yes and which is no.  Why?


"Jerry P" <jerryp@bisusa.com> wrote in message
news:QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net...
>
> "Peter E. C. Dashwood" <dashwood@enternet.co.nz
…[3 more quoted lines elided]…
> > [Please, please, newbies, resist the urge to set flags to 'Y'
or
> 'N'. Use 88
> > levels; that's what they're for. COBOL is intended to be a
> Self-Documenting
> > Language... Besides, it is arrogant to assume the whole world
uses
> "Yes" and
> > "No"  (it doesn't) and, in terms of pure logic, "1" and "0"
are
> better
> > Boolean representations of a truth value.)
>
> Please, please, newbies, use "Y" or "N" as flag values (or
"YES" and
> "NO" or "YA" and "NEIN" or "YEP" and "NOPE"). Zero and 1 are
> ambigious, have no relation to reality, mean nothing in
ordinary
> discourse ("Are you ready for lunch?" "One!"), and only
pendantic
> fuddie-duddies care whether they are the true members of the
Boolean
> Tribe.
> >
> > Unfortunately, not all implementations of COBOL allow a value
to be
> set to
> > FALSE, so it is necessary to provide for both TRUE and FALSE
with 88
> levels,
> > then set the required one to TRUE, as shown above.
>
> There you are. See, not even COBOL has much use for the
artificial
> constructs of 0 and 1 (or is it -1 and 0, or -1 and +1, or 0
and
> non-zero, I forget).
>
> >
> > Also, where your environment supports it, use lower case
("there's
> no need
> > to SHOUT") as it is easier on the eyes than Upper Case.]
>
> Also, except in literals and comments, use ALL CAPS when
writing COBOL
> code. The name COBOL is in caps and the code was meant to be
written
> that way. By using caps you are guaranteed cross-compiler /
platform
> compatibility. Programs are easier to digest. Mistakes are
easier to
> find. Listings in teeny type are easier to read. Caps in code
are much
> easier on older eyes.
>
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-01-09T09:04:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OLF66.1569$gN3.82849@news1.atl>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <938tn1$hn8$1@sshuraab-i-1.production.compuserve.com>`

```
"Russell Styles" <RWSTYLES01@CS.COM> wrote:
>     Let's be honest - if the original programmer spoke
> German (or whatever), then the chances are that
…[5 more quoted lines elided]…
>     So far as using 0 and 1, which is yes and which is no.  Why?

0 is nothing, 1 is something.  Take a wild guess which is which. ;-)
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-01-07T13:53:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ux_56.6065$m01.647693@dfiatx1-snr1.gtei.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
Jerry P <jerryp@bisusa.com> wrote in message
news:QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net...
>
> Also, except in literals and comments, use ALL CAPS when writing COBOL
> code. The name COBOL is in caps and the code was meant to be written
> that way.

If you mean edit with "caps on" for everything, I must disagree.

What I do is write the COBOL code in upper-case, and comments in mixed case.
Very easy to isolate code from comments!


 COOL-PARAGRAPH.
* INPUT: FOO
* OUTPUT: BAR.
* Conditions: FOO must be set to the number of angels which can dance on the
head of a pin.

    MOVE 2 TO BAZ
    COMPUTE DOG = CAT + 1
* adjust pets for leap year
     IF FUNCTION MOD (ZEBRA,4) GREATER 0
         SUBTRACT 6 FROM GAZELLE
     END-IF
     CONTINUE.



 By using caps you are guaranteed cross-compiler / platform
> compatibility. Programs are easier to digest. Mistakes are easier to
> find. Listings in teeny type are easier to read. Caps in code are much
> easier on older eyes.
>
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-07T15:35:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a588c8e.44049797@news1.attglobal.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <ux_56.6065$m01.647693@dfiatx1-snr1.gtei.net>`

```
I work in a system without change control.  I work on code that is
mostly upper case.  I use all lower case for my edits.  Makes it easy
to see what I did.

On Sun, 07 Jan 2001 13:53:30 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Jerry P <jerryp@bisusa.com> wrote in message
>news:QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net...
…[34 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-07T19:18:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mi366.15974$zH4.777876@newsread1.prod.itd.earthlink.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <ux_56.6065$m01.647693@dfiatx1-snr1.gtei.net>`

```

"Michael Mattias" <michael.mattias@gte.net

> >
> > Also, except in literals and comments, use ALL CAPS when writing
COBOL
> > code. The name COBOL is in caps and the code was meant to be
written
> > that way.
>
> If you mean edit with "caps on" for everything, I must disagree.

Nah. I said "literals and COMMENTS" (excuse the CAPS). You and I are
in substantial agreement.

>
> What I do is write the COBOL code in upper-case, and comments in
mixed case.
> Very easy to isolate code from comments!

Outstanding! Damn, you're good.

>
>
…[3 more quoted lines elided]…
> * Conditions: FOO must be set to the number of angels which can
dance on the
> head of a pin.
>
…[6 more quoted lines elided]…
>      CONTINUE.

In your example, note the asterisk in (presumably) column 7. What I've
started doing is adding a ">" in column 8 so that I'll be ready when
C2FF (Comment to Free Form) changeover occurs. I know it's almost 100
years off, but it pays to be prepared.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-01-08T14:03:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vMj66.327$PT.74603@dfiatx1-snr1.gtei.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <ux_56.6065$m01.647693@dfiatx1-snr1.gtei.net> <mi366.15974$zH4.777876@newsread1.prod.itd.earthlink.net>`

```
Jerry P <jerryp@bisusa.com> wrote in message
news:mi366.15974$zH4.777876@newsread1.prod.itd.earthlink.net...
>
> "Michael Mattias" <michael.mattias@gte.net
…[12 more quoted lines elided]…
>

DUH. I guess I better learn how to read.

>
> Outstanding! Damn, you're good.

And you, sir, are perspicacious.

MCM
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2001-01-08T12:04:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A59ACB5.4090801@optonline.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
Jerry P wrote:

> "Peter E. C. Dashwood" <dashwood@enternet.co.nz
> 
…[23 more quoted lines elided]…
> "NO" or "YA" and "NEIN" or "YEP" and "NOPE").

"YA" ist ein joke, nicht? "Yes", in German is "JA", as anyone who read 
WW II comic books could tell you. Back to ones & zeros, where "1" = true 
& "0" = false. No ambiguity there, Nazis or Bolsheviks.

LiamD (not a Nazi, but I play one on TV)
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-01-08T14:03:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vMj66.328$PT.74450@dfiatx1-snr1.gtei.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59ACB5.4090801@optonline.net>`

```
Liam Devlin <liamddd@optonline.net> wrote in message
news:3A59ACB5.4090801@optonline.net...
> >
> > Please, please, newbies, use "Y" or "N" as flag values (or "YES" and
> > "NO" or "YA" and "NEIN" or "YEP" and "NOPE").
>
> "YA" ist ein joke, nicht? "Yes", in German is "JA",...

Peter was not using German.

"YA" is "Chicagoan" (or maybe it's "Pittsburghian" or "Milwaukese")

MCM
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-08T14:11:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CUj66.8360$Sl.438333@iad-read.news.verio.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59ACB5.4090801@optonline.net>`

```
In article <3A59ACB5.4090801@optonline.net>,
Liam Devlin  <LiamD@optoffline.not> wrote:

[snippage]

>LiamD (not a Nazi, but I play one on TV)

Really?  When you do, who wins?

(this is smilar to 'Last night the high-school band played Beethoven.
Beethoven lost.')

DD
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-08T07:12:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A59CADF.AFC5671E@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
Jerry P wrote:

> Please, please, newbies, use "Y" or "N" as flag values (or "YES" and
> "NO" or "YA" and "NEIN" or "YEP" and "NOPE"). Zero and 1 are
…[3 more quoted lines elided]…
> Tribe.

Quite often YES or NO are just as ambiguous as ONE or TWO, depending on
what the flag is supposed to represent.  (And I don't mean where the
switch might be "MALE" or "FEMALE").

The question is:   Do people code a switch with values such as "FOUND" or
"NOT FOUND"?  Or do they find that to be too wordy?  With 88 level SET
commands these can be invisible.

Boy, I wish I had a SET MY-SWITCH TO FALSE ability!!
```

###### ↳ ↳ ↳ SET TO FALSE (was: number of days between dates

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-08T09:49:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93cnfd$vgd$1@slb7.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:3A59CADF.AFC5671E@brazee.net...
> Jerry P wrote:
>
<snip>
>
> The question is:   Do people code a switch with values such as "FOUND" or
…[4 more quoted lines elided]…
>

I believe that Howard is aware of this (already) - but for those reading
this note who are NOT yet aware of it,
 The "SET TO FALSE" facility *is* included in the draft of the next
revision - and is implemented by some (not all) existing compilers as an
"extension".

And before anyone asks (again) - it requires a new phrase (WHEN FALSE) in
the 88-level, so there is no "question/problem" with what value is used when
setting a "switch/flag" to FALSE.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 5)_

- **From:** Jeff Baynard <jeffbaynard@home.com>
- **Date:** 2001-01-09T01:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B67FD1C3.2D0%jeffbaynard@home.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net>`

```
SET xxx TO FALSE seems like a nice construct.  Should be worth using.

This is like a religious war.  'Y' and 'N' are just as good as NOT-EOF and
EOF.  I, however, do not like the 0 and 1 bit, but to each his own.

The bottom line is, when coding, try to adhere to shop standards.  If more
programmers use the SET construct, then by all means use it.  If most
programmers use 'Y' and 'N', then by all means use that.  Ask your lead if
you don't know.  A program should not switch back and forth between these
constructs; it should adhere to one convention throughout the entire source.
This makes 'hidden secrets' less likely.

Jeff

in article 93cnfd$vgd$1@slb7.atl.mindspring.net, William M. Klein at
wmklein@ix.netcom.com wrote on 1/8/01 10:49 AM:

> 
> I believe that Howard is aware of this (already) - but for those reading
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-01-09T12:50:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NOD66.779$LB4.42808@dfiatx1-snr1.gtei.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com>`

```
Jeff Baynard <jeffbaynard@home.com> wrote in message
news:B67FD1C3.2D0%jeffbaynard@home.com...
> The bottom line is, when coding, try to adhere to shop standards.  If more
> programmers use the SET construct, then by all means use it.


Perhaps; but do not give up trying to bring those shop standards out of the
Carter Administration!!

MCM
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-09T12:21:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5B64D6.4BAE9DA9@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <NOD66.779$LB4.42808@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:

> Perhaps; but do not give up trying to bring those shop standards out of the
> Carter Administration!!

No problem there - much of our code was ANSI 68 recently migrated (without style
changes) to work with Y2K.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 6)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-01-10T19:11:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93j18s$8ohg$1@newssvr06-en0.news.prodigy.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com>`

```
    I can't recall if anyone has made this point yet, but the decision to
use Y/N, 1/0, HV/LV is completely irrelevant if one uses SET statements and
condition names.  If you'll notice, you can change the values of the
condition names from Y to 1 and N to 0, for instance, without touching any
PROCEDURE DIVISION statement.  Meaningful condition names seems to me the
most readable/maintainable.

To reply, remove extra "r" in e-mail address.
....Terry


----- Original Message -----
From: "Jeff Baynard" <jeffbaynard@home.com>
Newsgroups: comp.lang.cobol
Sent: Monday, January 08, 2001 7:21 PM
Subject: Re: SET TO FALSE (was: number of days between dates


> SET xxx TO FALSE seems like a nice construct.  Should be worth using.
>
…[7 more quoted lines elided]…
> constructs; it should adhere to one convention throughout the entire
source.
> This makes 'hidden secrets' less likely.
>
> Jeff
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-11T21:05:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93js34$k18$3@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com>`

```

Terry Heinze wrote in message
<93j18s$8ohg$1@newssvr06-en0.news.prodigy.com>...
>    I can't recall if anyone has made this point yet, but the decision to
>use Y/N, 1/0, HV/LV is completely irrelevant if one uses SET statements and
>condition names.

Yes Terry, you are completely right and I have attempted to make this point
on at least 3 occasions during this thread.

Unfortunately, people tend to hear what they want to hear...<G>

Pete.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-12T07:27:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5EB1FE.4D9E1C66@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz>`

```
> Terry Heinze wrote in message
> >    I can't recall if anyone has made this point yet, but the decision to
> >use Y/N, 1/0, HV/LV is completely irrelevant if one uses SET statements and
> >condition names.

There is no need to use SET and 88 levels to acheive this.  The same
isolation from actual values can be done using a couple of ordinary
variables (probably in a copy book) or 78 levels.

       01   Is-True                 PIC X VALUE "Y".   (or whatever you
want)
       01   Is-Not-True             PIC X VALUE "N".


        MOVE Is-True        TO EOF-Flag
        ....

        IF ( EOF-Flag = Is-True )
            .....


I dislike 88 levels and SETs because they make it hard to find all
references to the flag using grep or text searches.  Using 88 levels and
SET does not make the program 'more modern', only more difficult to
maintain (IMHO).
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-11T12:58:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93kvm3$n7b$1@slb3.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz>`

```
Just another personal opinion, if you are using "grep or text searches" to
do program maintenance, then I suggest that you look at some "more modern"
tools - as well as some more modern language constructs.

*Many* Mainframe and Workstation tools allow you to find where data is
actually used and modified in a program without resorting to "is the same
data-name used" technology.

The use of "is-true" type constants seems pretty "error-prone" to me (if you
are still using grep and text searches) because I *assume* that you test
multiple fields in the same program against this same "value".  Therefore
(and yes grep can do this - but most text searches cannot) you need to
search for references to the same field and the same test value.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-12T09:23:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5ECD1C.31FCB416@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz> <93kvm3$n7b$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Just another personal opinion, if you are using "grep or text searches" to
> do program maintenance, then I suggest that you look at some "more modern"
> tools -

> as well as some more modern language constructs.

Condition names (88 levels) aren't 'more modern', they are from the
1960s.  Perhaps you hadn't noticed them until recently   ;-)

The kludge of misappropriating the SET verb was to solve the problem
inherent in condition names in that it was necessary to repeat the
actual literal value when a MOVE was used.  eg:

          05 Transaction-Type       PIC "X".
             88  Opening-Balance    VALUE "A".
             88  Payment-received   VALUE "P".
             ...

          MOVE "A"        TO Transaction-Type
          ...
          IF ( Opening-Balance )
              ...

This can be avoided completely be using fixed literals (there used to be
a CONSTANTS SECTION for these) or 78 levels (or equivalent).

          05  Opening-Balance      PIC X VALUE "A".
          05  Payment-received     PIC X VALUE "P".
          .....

        MOVE Opening-Balance       TO Transaction-Type
        .....
        IF ( Transaction-Type = Payment-Received )
            ....


There is no need for 88 levels or SET TO TRUE/FALSE.  There is no need
to think of these as 'modern'.


> *Many* Mainframe and Workstation tools allow you to find where data is
> actually used and modified in a program without resorting to "is the same
> data-name used" technology.

I often want to find where a data item is used across a whole system,
not just in one program.  Keeping ideas from the '60s (Condition names)
out of the program makes 'data-name used technology' appropriate.
 
> The use of "is-true" type constants seems pretty "error-prone" to me (if you

What is 'error-prone' or not is primarily dependant on what one is used
to, and what one has trained oneself to be aware of.

> are still using grep and text searches) because I *assume* that you test
> multiple fields in the same program against this same "value". 

Yes, unlike 88 levels the same value can be used giving a uniform usage.

> Therefore
> (and yes grep can do this - but most text searches cannot)

Then I must have one of the 'more modern' tools, because I can.

> you need to
> search for references to the same field and the same test value.

I usually want to search for _all_ usage of a variable, ie those places
where it is changed or tested.  With 88 levels I would have to search
for the flag variable name and each of the 88 level names.  This can be
simplified by using a structured naming such as:

      01   Transaction-EOF-Flag        PIC X.
           88  Transaction-EOF-Flag-TRUE    VALUE "1".
           88  Transaction-EOF-Flag-FALSE   VALUE "0".

In fact this is superfluous as the SET ... FALSE will remove the need
for the ..-FALSE 88 level and the variable need not have a name. 
However, in general (in my experience), there is often little textural
resemblence between the flag variable name and the 88 level(s). One
program may have:

      01   EOF-Flag        PIC "X".
           88  Transactions-finished  VALUE "Y".
           88  More-Transactions      VALUE SPACE.


       MOVE SPACE    TO EOF-Flag

       READ ....  
               AT END SET Transactions-finished   TO TRUE
               ...       	

       IF ( More-Transactions )
            ...

Which, of course, is simply poor style, but typical.




> > I dislike 88 levels and SETs because they make it hard to find all
> > references to the flag using grep or text searches.  Using 88 levels and
> > SET does not make the program 'more modern', only more difficult to
> > maintain (IMHO).
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 11)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-12T12:19:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93li4v$mu3$2@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz> <93kvm3$n7b$1@slb3.atl.mindspring.net> <3A5ECD1C.31FCB416@Azonic.co.nz>`

```

Richard Plinston wrote in message <3A5ECD1C.31FCB416@Azonic.co.nz>...
>
>There is no need for 88 levels or SET TO TRUE/FALSE.  There is no need
…[10 more quoted lines elided]…
>
Well, there is certainly no need for YOU to use 88 levels and SET. Your
opinion is not going to be changed by reasoned argument.

As you mentioned elsewhere, it is a question of what you are used to.

However, if you believe that "ideas from the '60s" should be kept out of
COBOL, we wouldn't have much of a Language left.

The point is that it doesn't matter when an idea was first postulated, what
matters is whether it is still true or not.

I believe that condition-names are just as pertinent in COBOL today as they
have always been. You don't. That's OK.

Both of us can go off and develop code and solve application problems. The
only difficulty which arises is when someone else has to maintain our code.

And that's where the whole question of "style" (which is necessarily based
on opinion) arises.

There is no right or wrong here, only opinion. I f you work in the same
environment for many years, or on your own, then you will develop a sytyle
that suits that environment.

If you find yourself working on many different platforms and sites (maybe as
a contractor) you will be exposed to many different influences, which will
in turn modify your opinions about things, with a resulting change of style.

It is noticeable that your particular style has already been influenced by
exposure to other languages. (Mine probably has too, but it is not as
noticeable...<G>) There is nothing wrong with that, AS LONG as other people
have no difficulty with the code you write.

Actually, Richard, I appreciate the fact that you were the ONLY person in
this forum who raised an issue on the code I posted. (Dislike of condition
names used, and why you disliked it). Everyone else got sidetracked into
their own personal preferences for switch settings, etc.

While we are never going to agree on the use of condition names, at least we
can agree to disagree.

Pete.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-12T17:43:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5F4250.F9952681@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz> <93kvm3$n7b$1@slb3.atl.mindspring.net> <3A5ECD1C.31FCB416@Azonic.co.nz> <93li4v$mu3$2@hermes.enternet.co.nz>`

```
Peter E. C. Dashwood wrote:
> 
> However, if you believe that "ideas from the '60s" should be kept out of
> COBOL, we wouldn't have much of a Language left.

I wasn't arguing for excluding "ideas from the 60s", I was arguing that
condition names aren't "more modern".

There are, in fact, several "ideas from the 60s" which I would certainly
suggest be excluded, fortunately many of them are by the majority.

> Both of us can go off and develop code and solve application problems. The
> only difficulty which arises is when someone else has to maintain our code.

Or, more importantly, when I have to modify someone else's code,
_no_one_ will have difficulty with _my_ code       double  ;-)

> There is no right or wrong here, only opinion. I f you work in the same
> environment for many years, or on your own, then you will develop a sytyle
> that suits that environment.

Well, of course, 'developing a style' does imply actively trying new
techniques and learning from others, including from other languages.

> If you find yourself working on many different platforms and sites (maybe as
> a contractor) you will be exposed to many different influences, which will
> in turn modify your opinions about things, with a resulting change of style.

Yes, I do.  

> While we are never going to agree on the use of condition names, at least we
> can agree to disagree.

Yes, of course, I will agree that you have found condition names to make
some code easier to maintain as long as you agree that I have found some
code where the condition names and SETs made it harder to maintain.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-12T11:58:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93li4t$mu3$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz>`

```

Richard Plinston wrote in message <3A5EB1FE.4D9E1C66@Azonic.co.nz>...
>
>There is no need to use SET and 88 levels to acheive this.  The same
…[18 more quoted lines elided]…
>maintain (IMHO).

Well, Richard, your opinion is as valuable as anyone else's.

I would strongly disagree with the above for the following reasons:

(All of the following is simply opinion. Readers can draw their own
conclusions...)

1. The code you arrive at:

>        IF ( EOF-Flag = Is-True )

is contrived and ugly. (And it smacks of C or VB influence, where "Is.."
Functions abound.)

Compare it with:  IF Finished... (This is English, and looks like a COBOL
solution).

It further causes confusion with the COBOL language elements, TRUE and
FALSE. My original post here was aimed at newcomers; the less confusion, the
better.

I understand your reason for doing it, and your point regarding greps and
text searches for the switch or flag references is a valid one, but only
because COBOL does not currently implement SET ....FALSE  in all
implementations.

If COBOL can SET ...TRUE  and SET... FALSE, then there is no need to ever
reference the flag or switch (in fact, it can be declared as FILLER and
never referenceable) so there would be no need to search for references to
it.

Consider this:

77    filler   pic x.
         88     Finished         value [whatever you prefer; it really
doesn't matter...]


Then, in code....


Read whatever
      at end
           set Finished to TRUE
      NOT  at end
           set Finished to FALSE
End-read

if Finished....

or

if NOT finished

I contend that this is more readable and "elegant" than contriving
"Is-False" values.

There is no longer any requirement to grep or text search for the actual
flag or switch as it can NEVER be referenced anyway...

2. You suggest using a 78 level. Sadly this is an implementor extension of
COBOL and is not defined in the Standard Language. (It is possible that the
committee is looking at it for the next standard, but I'm sure Bill Klein
will tell us if this is the case. In the meantime, it is only available from
Merant AFAIK.)

3. I would not argue that using SET makes the program more modern (although
SET is a RELATIVE newcomer to COBOL ...like 20 years as opposed to 40 years
<G>) but I certainly would argue that using it makes the program more
difficult to maintain; it doesn't. Quite the contrary, in fact.

Pete.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-12T17:44:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5F4299.8FAFE8AC@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <93js34$k18$3@hermes.enternet.co.nz> <3A5EB1FE.4D9E1C66@Azonic.co.nz> <93li4t$mu3$1@hermes.enternet.co.nz>`

```
Peter E. C. Dashwood wrote:

> >I dislike 88 levels and SETs because they make it hard to find all
> >references to the flag using grep or text searches.  Using 88 levels and
…[3 more quoted lines elided]…
> Well, Richard, your opinion is as valuable as anyone else's.
 
> 1. The code you arrive at:
> >        IF ( EOF-Flag = Is-True )
> is contrived and ugly. (And it smacks of C or VB influence, where "Is.."
> Functions abound.)

All code that one is unused to is 'contrived and ugly'.  I use upper
case reserved words, mixed case user words, parentheses around
conditions and vertically align MOVE .. TO blocks .  This may be found
to be ugly by those who use all-upper or all-lower, or other.

> Compare it with:  IF Finished... (This is English, and looks like a COBOL
> solution).

Actually it is not very good English, there is no subject.  Now if you
had something along the lines of:

        If transaction-data is finished
        then ...

where 'transaction-data' was the 'eof flag' and 'finished' is a class
with a single value equal to the constant moved to this on end of file,
then this may be better English.  Whether it is 'better' Cobol is a
matter of opinion.

> It further causes confusion with the COBOL language elements, TRUE and
> FALSE. My original post here was aimed at newcomers; the less confusion, the
> better.

I wasn't necessarily suggesting that 'Is-True' be adopted as a standard,
you could choose your own names, only that I prefer this style.  In fact
I have used C-TRUE and C-FALSE in Windows programming (but it might be
too C like for everyone's taste).

> I understand your reason for doing it, and your point regarding greps and
> text searches for the switch or flag references is a valid one, but only
> because COBOL does not currently implement SET ....FALSE  in all
> implementations.

> If COBOL can SET ...TRUE  and SET... FALSE, then there is no need to ever
> reference the flag or switch (in fact, it can be declared as FILLER and
> never referenceable) so there would be no need to search for references to
> it.

Well, exactly.  When Cobol can actually do as you propose then it may be
worth adopting.  In the meantime I suspect that new users will be
confused by future features that were not covered in their courses and
may not be available in their compiler because they haven't set the
MF(x) switch.
 
> if Finished....
> or
> if NOT finished

> I contend that this is more readable and "elegant" than contriving
> "Is-False" values.

Probably because you are used to the contrivence of 'Finished'.  It also
doesn't specify _what_ is finished.  In typical programs there are
several items that may have a 'finished' status.
 
> 2. You suggest using a 78 level. Sadly this is an implementor extension of
> COBOL and is not defined in the Standard Language. 

And yet your proposal of SET .. FALSE is also currently an extension and
not in the Standard Language which is in use.

In fact I had proposed, and had examplified, them as normal standard
variables and had offered '78 or equivalent' only as an option.  A
symbolic constant will also do nicely, and is standard.

> 3. I would not argue that using SET makes the program more modern (although
> SET is a RELATIVE newcomer to COBOL ...like 20 years as opposed to 40 years
> <G>) but I certainly would argue that using it makes the program more
> difficult to maintain; it doesn't. Quite the contrary, in fact.

In general I avoid such contrivences as 'EOF Flags' and thus find little
use for 88 levels and SET. I usually have something along the lines of:

         MOVE Master-Key    TO Trans-Key
         START Transaction .. INVALID KEY MOVE HIGH-VALUES TO Trans-Key
         PERFORM
             UNTIL Trans-Master-Key NOT = Master-Key

             READ ... NEXT 
                 AT END MOVE HIGH-VALUES TO Trans-Key
                 NOT AT END
                 IF ( file staus check here )
                 ELSE
                 IF ( Trans-Master-Key = Master-Key 
                  AND other things to look for
                    )
         ....

But then most of my systems are primarily interactive and an
'End-of-File' is equivalent to reading beyond the required data and does
not indicate 'Finished' in any overall way.

Perhaps the association of 'difficult to maintain' is only incidental to
the use of 88 levels and SETs and their use is a symptom of the problem
and not a primary cause.

That is: the use of 88 and flags for such things as end of file
conditions may indicate that the code is less structured than it could
be.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-11T07:09:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5DBEAC.535DB7DC@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com>`

```


Terry Heinze wrote:

>     I can't recall if anyone has made this point yet, but the decision to
> use Y/N, 1/0, HV/LV is completely irrelevant if one uses SET statements and
> condition names.  If you'll notice, you can change the values of the
> condition names from Y to 1 and N to 0, for instance, without touching any
> PROCEDURE DIVISION statement.

Unless you're debugging.  Hmm, I still debug with displays and dumps.  Do
on-line debuggers show 88 levels, or do you need to reference the source to see
which 88 levels are set?


> Meaningful condition names seems to me the
> most readable/maintainable.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-11T08:41:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93kgmu$vdm$1@nntp9.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <3A5DBEAC.535DB7DC@brazee.net>`

```
GOOD interactive debuggers allow you to "play with" 88-levels (set, test,
display the current Truth/Falsity, etc)

Certainly when I worked for ADS (prior to Centura prior to Compuware),
Xpediter did

Certainly when I worked for Micro Focus (prior to MERANT), Animator (GUI and
"traditional") did.
```

###### ↳ ↳ ↳ Re: SET TO FALSE (was: number of days between dates

_(reply depth: 8)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2001-01-12T06:07:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5E9F06.70709@optonline.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <3A5DBEAC.535DB7DC@brazee.net>`

```
Howard Brazee wrote:

> 
> Terry Heinze wrote:
…[11 more quoted lines elided]…
> which 88 levels are set?

Xpediter shows the 88-level values so you can see if the test is true or 
false.

As long as I'm posting, someone mentioned that a switch could be defined 
as filler, which it could. But that would make it impossible to use the 
default value for the data type, e.g., zero for PIC 9, as the False, 
without also using the Value clause.

I like to set my switches up in their own 01 level and Initialize 
All-Switches in my initialization paragraph. This way I'm certain 
everything is tidy at the start, besides, I do think the name of the 
switch (or flag) should aid to understanding the switch's purpose.

LiamD
```

###### ↳ ↳ ↳ INITIALIZE enhancements (was: SET TO FALSE (was: number of days between dates

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-12T00:45:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93m961$mr2$1@slb1.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <3A5DBEAC.535DB7DC@brazee.net> <3A5E9F06.70709@optonline.net>`

```
And yet another plug for the "maybe in our life time" next revision of
COBOL.  There are a *number* of enhancements in the draft Standard to the
INITIALIZE statement. One of them is to explicitly request INITIALIZE
"filler" fields - another is to initialize a field to whatever is in its
value clause.  Hence (in the NEXT COBOL Standard)

Given:

 01 All-Switches.
      05        Value "Y".
         88 First-Time Value "Y"
              when false "N".
     05        Value "1"
          88 Count-1   Value "1" "5" thru "9"
              when False Value "4".
          88  Count-2   Value "2".

You can then have a Procedure Division statement of

  Initialize All-Switches with Filler All to Value

which would be EQUIVALENT to coding
   Set First-Time Count-1 to True

Either statement will set both the switches to what their original value
clauses specified.

P.S.  Notice that you do NOT need a Picture clause when you have a Value
clause for an alphanumeric field - unless you want to have the Picture
"larger" than the Value clause. (Both of these fields would be Pic X(01)
because they have one-byte value clauses)

P.P.S.  Of course INITIALIZE without the new phrases works the same way it
does in the '85 Standard - so there are no compatibility problems for
existing code.
```

###### ↳ ↳ ↳ Re: INITIALIZE enhancements (was: SET TO FALSE (was: number of days between dates

_(reply depth: 10)_

- **From:** "mangogrower" <mangogrower@telocity.co>
- **Date:** 2001-02-07T21:50:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DKng6.62177$Ch.11626652@newsrump.sjc.telocity.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <3A59CADF.AFC5671E@brazee.net> <93cnfd$vgd$1@slb7.atl.mindspring.net> <B67FD1C3.2D0%jeffbaynard@home.com> <93j18s$8ohg$1@newssvr06-en0.news.prodigy.com> <3A5DBEAC.535DB7DC@brazee.net> <3A5E9F06.70709@optonline.net> <93m961$mr2$1@slb1.atl.mindspring.net>`

```
Now those are (Y|1|J|S) somethings I've wanted a LONG time Bill.

Something Like:

INITIALIZE MY-DATA TO INITIALVALUES. (would init all data items including
FILLER)

or INITIALIZE MY-DATA  WITHFILLER

PLUG, plug,plug.


And for my two pfennigs worth,
The original -Date- routine cited does not work.

when working with CCYYMMDD  (Or any CCYYxxxxx dates)
you MUST divide by 400  FIRST.

Otherwise you get 1900 and 2100 and 2200 as leap years and they are not.

I LOVE 88s/condition names.  I've programmed (professionally) in
COBOL/COBOLII,
Assembler, 'C', Basic/VB, and Delphi (plus other 'packages').
On the IBM Mainframe, VIASOFT (one of the very best COBOL tools) supports
'88' display / mods when used as a filler at the item name.

I PREFER all switches to be 'YES' or 'NO ' because 1) they stand out in
memory
2) I'm not doing math on them.

BTW Peter, why is it easier to 'grep' for WS-SOME-SWITCH-NAME
compared to FATAL-ERROR-UPDATING-SOME-MASTER ?

Quite often you find code like this:

                if .....
                            if .....
                                    MOVE 'Y'       TO
                                          WS-SOME-SWITCH
                            (OR )
                                    IF WS-SOME-SWITCH   =
                                        'Y'


you don't know what is being done unless you request enough 'before/after'
lines to print


PS.  I think if we're coding 'COBOL', we can be certain its a DIGITAL
computer
as opposed to an ANALOG computer - that would be something that understands
+5 Volts!

If everyone always agreed, the world would be pretty boring!

William M. Klein <wmklein@ix.netcom.com> wrote in message
news:93m961$mr2$1@slb1.atl.mindspring.net...
> And yet another plug for the "maybe in our life time" next revision of
> COBOL.  There are a *number* of enhancements in the draft Standard to the
…[53 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-01-09T09:03:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FKF66.1568$gN3.82804@news1.atl>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net>`

```
"Jerry P" <jerryp@bisusa.com> wrote:
>
> Zero and 1 are ambigious, have no relation to reality, mean nothing
> in ordinary discourse ("Are you ready for lunch?" "One!"), and only
> pendantic fuddie-duddies care whether they are the true members of
> the Boolean Tribe.

Pardon, Jerry, but I must take issue with the above statement. :-)
If the audience were the population in general, I would agree.  But
any programmer who could not instantly recognize 0=no and 1=yes in
such a situation, I would not want working for me.

I agree that using "Y"/"N" or particularly "YES"/"NO" is clearer. :-)
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-09T15:32:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y9G66.8490$Sl.448203@iad-read.news.verio.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl>`

```
In article <FKF66.1568$gN3.82804@news1.atl>,
Judson McClendon <judmc@bellsouth.net> wrote:
>"Jerry P" <jerryp@bisusa.com> wrote:
>>
…[8 more quoted lines elided]…
>such a situation, I would not want working for me.

Mr McClendon, you could you make such an error?  Zero is round,
continuous, infinite in itsself; these are qualities of affirmation, not
negation.  A one, on the other hand, is broken and (literally!) solitary;
these are characteristics which must be changed to be affirmative, just as
a one must be changed to a zero to be 'yes'.

Now if you'll excuse me... there are Matters of State to be attended to by
*this* King of England.

DD
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-09T09:32:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5B3D1A.97DF40BB@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net>`

```
NA wrote:

> Mr McClendon, you could you make such an error?  Zero is round,
> continuous, infinite in itsself; these are qualities of affirmation, not
> negation.  A one, on the other hand, is broken and (literally!) solitary;
> these are characteristics which must be changed to be affirmative, just as
> a one must be changed to a zero to be 'yes'.

The IBM switches with a I or O didn't seem natural to me.  Partly this is
because it wasn't a one or an I, but a vertical line.   It looked like
I=closed, O=open.  But then we have to translate this to on or off.

Still, without the FALSE clause 88 level descriptions aren't always as clear
or logical as I would like:

05 SW-STUDENT-FOUND-SWITCH    pic x     value "N".
     88   SW-STUDENT-FOUND                          Value "Y".
     88   SW-STUDENT-NOT-FOUND                Value "N".

Set SW-STUDENT-NOT-FOUND to true...
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2001-01-09T23:28:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E8N66.23578$_G5.3161709@typhoon.nyroc.rr.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <3A5B3D1A.97DF40BB@brazee.net>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:3A5B3D1A.97DF40BB@brazee.net...
>
> The IBM switches with a I or O didn't seem natural to me.  Partly this is
> because it wasn't a one or an I, but a vertical line.   It looked like
> I=closed, O=open.  But then we have to translate this to on or off.
>
It took me years to figure the on/off switch labling I=on, O=off, but I
finally did (on my own): Think of a pipe coming out of the page with a round
pivoting disk inside. If the disk is pivoted on edge (I), the contents of
the pipe can flow (on). If the disk is pivoted the other way (O), the pipe
is blocked (off).
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-13T11:45:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93q1bh$9ot$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <3A5B3D1A.97DF40BB@brazee.net>`

```
Howard Brazee wrote in message <3A5B3D1A.97DF40BB@brazee.net>...
>NA wrote:
>
…[3 more quoted lines elided]…
>> these are characteristics which must be changed to be affirmative, just
as
>> a one must be changed to a zero to be 'yes'.
>
…[4 more quoted lines elided]…
>Still, without the FALSE clause 88 level descriptions aren't always as
clear
>or logical as I would like:
>
…[4 more quoted lines elided]…
>Set SW-STUDENT-NOT-FOUND to true...


I think the whole thing an insidious plot.  We are going to back to
hieroglyphics after centuries of evolving perfectly good alphabets, The
damned younger generation just will *not* take the time to learn to read,
and everything has to be presented to them as little picture before they can
use it.  Pretty soon, we will be back to toggling ones and zeros on the
operator's console.  An nefarious plot to waste all our hard fought
knowledge.  A blight upon intellect I tell you ...
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-09T13:30:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net>`

```
On Tue, 09 Jan 2001 15:32:08 GMT, docdwarf@clark.net (  NA)
enlightened us:

>In article <FKF66.1568$gN3.82804@news1.atl>,
>Judson McClendon <judmc@bellsouth.net> wrote:
…[21 more quoted lines elided]…
>DD

The Earl of Obfuscation would like to report (or retort..take your
pick) to the King of England thusly:

Zero is round, continuous, infinite in itsself; therefore one asks
oneself, "Does it End?"  The answer, of course, is NO.

A One is broken and solitary; again one asks oneself, "Does it End?"
The answer, of course, is YES.

Hence, 0 = NO, 1 = Yes

The preceeding stated without every resorting to that binary stuff!

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

In the beginning, God created earth and rested. 
Then God created man and rested. 
Then God created woman. 
Since then, neither God nor man has rested.



Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-09T19:07:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jkJ66.8522$Sl.449712@iad-read.news.verio.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>`

```
In article <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>,
SkippyPB  <swiegand@neo.rr.com.nospam> wrote:
>On Tue, 09 Jan 2001 15:32:08 GMT, docdwarf@clark.net (  NA)
>enlightened us:
…[37 more quoted lines elided]…
>The preceeding stated without every resorting to that binary stuff!

No wonder you only made it to Earl... to make King ya gots to know stuff
like 'Truth is Eternal, that which is Eternal does Not End, of this We are
Positive'... hence 0 = Yes.

Likewise, One is the Lonliest Number and that the King does not need A
Loan, No!... hence 1 = No.

DD
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-10T12:37:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<98682222D947394C.2BF07E6C3FC843D9.DBBFCFCF644E843B@lp.airnews.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net> <jkJ66.8522$Sl.449712@iad-read.news.verio.net>`

```
On Tue, 09 Jan 2001 19:07:59 GMT, docdwarf@clark.net (  NA)
enlightened us:

>In article <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>,
>SkippyPB  <swiegand@neo.rr.com.nospam> wrote:
…[48 more quoted lines elided]…
>DD

The Earl (it was the only thing available!) bows before the supreme
obfuscating King's brilliance :)

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

In the beginning, God created earth and rested. 
Then God created man and rested. 
Then God created woman. 
Since then, neither God nor man has rested.



Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-01-10T19:49:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1376.8712$Sl.459296@iad-read.news.verio.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net> <jkJ66.8522$Sl.449712@iad-read.news.verio.net> <98682222D947394C.2BF07E6C3FC843D9.DBBFCFCF644E843B@lp.airnews.net>`

```
In article <98682222D947394C.2BF07E6C3FC843D9.DBBFCFCF644E843B@lp.airnews.net>,
SkippyPB  <swiegand@neo.rr.com.nospam> wrote:
>On Tue, 09 Jan 2001 19:07:59 GMT, docdwarf@clark.net (  NA)
>enlightened us:
…[54 more quoted lines elided]…
>obfuscating King's brilliance :)

Pfoo, you'se jes' easily impressed.

DD
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-09T15:08:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93fqtk$ieo$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>`

```

SkippyPB wrote in message
<03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net>...
>On Tue, 09 Jan 2001 15:32:08 GMT, docdwarf@clark.net (  NA)
>enlightened us:
…[38 more quoted lines elided]…
>

One and zero?  True and False? What is this stuff?  I thought this was about
COBOL.  Show me a picture clause.  How do you write a cheque for true?  The
opposite of 1 is lost.  My roommate told me that playing cards last night,
so it must be true.
```

###### ↳ ↳ ↳ Ture/False - 0/1 (was: number of days between dates

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-09T15:55:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93g1bp$4q1$1@nntp9.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net> <93fqtk$ieo$1@news.igs.net>`

```
"donald tees" <donald@willmack.com> wrote in message
news:93fqtk$ieo$1@news.igs.net...
>

> >
>
> One and zero?  True and False? What is this stuff?  I thought this was
about
> COBOL.  Show me a picture clause.  How do you write a cheque for true?
The
> opposite of 1 is lost.  My roommate told me that playing cards last night,
> so it must be true.
>
>

Well, in the draft Standard - how about:

  01 Bool1   Pic 1.
  01  Bool2  Pic 1(8)  Value B"01010101".

and then in your Procedure Division,

  If Bool1 B-and Bool2 Zero
     Display "This must mean something to someone !!!"
 End-If

Or even (if I recall correctly)

Evaluate Bool1 Also Bool2
  When True also False
      Display "Would you call THIS self-documenting???"
End-Evaluate
```

###### ↳ ↳ ↳ Re: Ture/False - 0/1 (was: number of days between dates

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-10T04:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a5be770.263956757@news1.attglobal.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <Y9G66.8490$Sl.448203@iad-read.news.verio.net> <03BB182A99F7C5FF.5BEC8948605378E6.E648911CB7C69865@lp.airnews.net> <93fqtk$ieo$1@news.igs.net> <93g1bp$4q1$1@nntp9.atl.mindspring.net>`

```
Awe... come on... 

01  Flag Boolean value false.

(Not sure this is valid, but it sure should be!)

or

01  Flag Boolean.

code.....

Set Flag to False

If Flag ....
Else ...

Set Flag to True

Etc.. WHO CARES what's inside it?  FOO or BAR it doesn't matter..



On Tue, 9 Jan 2001 15:55:14 -0600, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>"donald tees" <donald@willmack.com> wrote in message
>news:93fqtk$ieo$1@news.igs.net...
…[37 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-10T04:40:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl>`

```

"Judson McClendon" <judmc@bellsouth.net> wrote in message
news:FKF66.1568$gN3.82804@news1.atl...
> "Jerry P" <jerryp@bisusa.com> wrote:
> >
> > Zero and 1 are ambigious, have no relation to reality, mean
nothing
> > in ordinary discourse ("Are you ready for lunch?" "One!"), and
only
> > pendantic fuddie-duddies care whether they are the true members of
> > the Boolean Tribe.
…[4 more quoted lines elided]…
> such a situation, I would not want working for me.

Oops. According to the citizenship rules of the Boolean Tribe, 0=False
and Not Zero = True. So if you had a programmer who asserted that two
was true...

As an aside, this means that +1 and -1 are identical and +1 -1 = 0.
But I was told that two positives never equal a false. To which I
respond, "Yeah, sure."
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-11T02:14:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93hpc2$gh0$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net>`

```

Jerry P wrote in message
<2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net>...

>> > pendantic fuddie-duddies care whether they are the true members of
>> > the Boolean Tribe.
…[4 more quoted lines elided]…
>> such a situation, I would not want working for me.



>Oops. According to the citizenship rules of the Boolean Tribe, 0=False
>and Not Zero = True. So if you had a programmer who asserted that two
…[4 more quoted lines elided]…
>respond, "Yeah, sure."


Having lived with the tribe  for many years now, and studied their habits
(especially the curious property that some of them always tell the truth,
some of them always lie and some of them sometimes lie OR tell the truth) I
can tell you that to members of the tribe, 1 is NOT a "number" (it is a
symbol for the truth or falsity of a proposition).

The concept of "two" is beyond the experience of the tribe members so a
programmer who asserted that "two was true" would be tried for heresy (ONLY
'1' or 'NOT 0' can be TRUE), ritually slaughtered, and eaten by the older
members of the Tribe (the pedantic fuddy-duddies) as a warning to the young
'uns...

The Tribe's Religion is mystical in the extreme and revolves around an
Algebra based on the two symbols described above.

Although this is a true 'Algebra' (it has commutative and associative
properties, and Multiplicative and Additive Identities, even though
'Addition' and 'Multiplication'  (in the Arithmetic sense) are NOT defined
for it...!!), it cannot be used to perform operations such as you describe:
+1-1=0 or +1=-1

Instead, the defined operations are AND and OR. It also has special rules
regarding "negation" (De Morgan's Laws) which should very quickly persuade
you that the idea of 'NOT' being 'NEGATIVE' is just as meaningless as the
idea of 'TRUE' being 'POSITIVE'.

The Creed says: 1 OR 0 = 1
                              1 AND 0 = 0
                         NOT (1 OR 0) = NOT 1 AND NOT 0  [De Morgan 1]
                         NOT (1 AND 0) = NOT 1 OR  NOT 0 [De Morgan 2]
                         NOT 1 = 0
                         NOT 0 = 1
And that's ALL it says (note NO arithmetic signs...)

It is many years now since I lived with the Tribe, but the understanding I
acquired there has been inextricably embroidered into the fabric of my
Programs, and they are better for it...

But then again... I could be lying...<G>

Pete.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-10T09:19:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93hqrm$m4j$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz>`

```
Peter, Peter, Peter.  You have been corrupted by all these weirdo
languages designed for computers with small regard for the programmer.
You need to get back into a language designed for People
that *use* Computers (like Cobol).

I stopped using zero and one to mean "true" and "false" way
back when I discovered that it was hardware dependent.  Yes
indeed, some chips use positive logic, and some use negative
logic.  So "true" really should mean +5 Volts when fastened to
a device, but often means 0 Volts.

I use "T" for true, and "F" for false.  I use "Y" for yes, and "N" for no.
ON, and Off are problematic, I agree, but can be mapped to either
of the others by an 88 level.

Zero and One should only be used at the assembler level, and
even then they should be mapped at the macro level.

Peter E. C. Dashwood wrote in message
<93hpc2$gh0$1@hermes.enternet.co.nz>...
>
>Jerry P wrote in message
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-11T12:03:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93iri0$ij1$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net>`

```

donald tees wrote in message <93hqrm$m4j$1@news.igs.net>...
>Peter, Peter, Peter.  You have been corrupted by all these weirdo
>languages designed for computers with small regard for the programmer.
>You need to get back into a language designed for People
>that *use* Computers (like Cobol).
>
Well, I have certainly been corrupted... (But not by computer
polyglot...<G>)

As for getting back into COBOL; I have never been out of it.

>>>
>I stopped using zero and one to mean "true" and "false" way
…[10 more quoted lines elided]…
>even then they should be mapped at the macro level.
<<<
er...I believe that mapping the values to an 88 level is exactly what I
recommended.

So, I take it you have no issue with the code sample?

(You know very well, Donald, how rarely I post code samples ANYWHERE... On
this occasion, I believe it was warranted. Nobody so far has commented in
any way on the code. Instead, the thread has wandered into a delightful
discussion on what everybody's preferences are... That's OK too, but it
doesn't address the issue.)

Nobody, least of all me, is disagreeing with your right to use whatever you
want. My original statement was, THAT IN A BOOLEAN CONTEXT 1 and 0 make the
most sense. (As Boolean Algebra is defined around these two symbols, I can't
see what all the fuss is about.) My personal preference is not to use YES
and NO because I have worked in countries where these values are not the
accepted affirmative and negative.

No matter where you work, at some time you will probably need a "finished
processing" switch (for example).

Let's say you are working in a country where Spanish is the first
Language...

Don't you think it is a tad insensitive, even discourteous and disrespectful
to the indigenous programmers who will maintain your code after you leave if
you
code:

if end-switch = "Y"

when you could've coded:

if todos-finitos... or  if finished

???

OK, now consider these 3 examples:

77  end-switch pic x.
       88 finished          value "Y".
       88 NOT-finished value "N".

77  end-switch pic x.
       88 finished           value "1".
       88 NOT-finished  value "0".

77  end-switch pic x.
       88 finished           value "B".
       88 NOT-finished  value "Z".


The first one says: "I am an English speaking programmer and you guys better
deal  with it.."
 The second one says: "Let's use the international language of Mathematics
to communicate in a spirit of co-operation."
The last one says: "Is it time for my medication, yet?"

ALL of them will work, and, as far as the computer programming is concerned,
can be argued to be equally valid. However, life is not just about computer
programming, and working together as part of a team in exotic locations
needs all the facilitation it can get.

Besides, I am by nature, polite and generally considerate (but then
again...I could be lying <G>)

Pete.








>Peter E. C. Dashwood wrote in message
><93hpc2$gh0$1@hermes.enternet.co.nz>...
…[25 more quoted lines elided]…
>>some of them always lie and some of them sometimes lie OR tell the truth)
I
>>can tell you that to members of the tribe, 1 is NOT a "number" (it is a
>>symbol for the truth or falsity of a proposition).
>>
>>The concept of "two" is beyond the experience of the tribe members so a
>>programmer who asserted that "two was true" would be tried for heresy
(ONLY
>>'1' or 'NOT 0' can be TRUE), ritually slaughtered, and eaten by the older
>>members of the Tribe (the pedantic fuddy-duddies) as a warning to the
young
>>'uns...
>>
…[6 more quoted lines elided]…
>>for it...!!), it cannot be used to perform operations such as you
describe:
>>+1-1=0 or +1=-1
>>
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-10T18:00:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93it2b$296$1@slb7.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz>`

```
Peter -
  Somehow, when you are writing a source program using the words "If" "Move"
"Value" (not to mention such "oddities" as "Pic" meaning "Picture") -
assuming that "Yes" and "No" (or "True and False") are "acceptable"  - in
fact TRUE and FALSE are already part of the "required" language (e.g.
EVALUATE).

Therefore, it seems to me that

01    Pic X(05) Value "False".  *> with no data-name
    88 End-Of-File  Value "True"
        when set to False "False".

seems "more" self-documenting than using "1" and "0".  (Personally, I might
still use "Y" and "N" - or "yes" and "no" - or "T" and "F" - depending on my
"mood")

P.S.  Is this speaking to your point or not?  I certainly DO agree with the
use of 88-levels and Set to TRUE/FALSE.  I also use (as above) mixed case
when creating source code.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-11T21:01:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93js33$k18$2@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <93it2b$296$1@slb7.atl.mindspring.net>`

```

William M. Klein wrote in message <93it2b$296$1@slb7.atl.mindspring.net>...
>Peter -
>  Somehow, when you are writing a source program using the words "If"
"Move"
>"Value" (not to mention such "oddities" as "Pic" meaning "Picture") -
>assuming that "Yes" and "No" (or "True and False") are "acceptable"  - in
…[8 more quoted lines elided]…
>
That's interesting, Bill.


I'm not sure that all platforms will support 'when set to False "False"',
but you'd know more about that than I do.

I have to say that personally, even if it IS supported, I wouldn't do do
what you outlined above.

Why not? Because I believe it is confusing. (especially to newcomers, and
they were the people I was originally addressing.)

However, your point that the Language already supports TRUE and FALSE is
well taken, and I believe we have no real issues here.

Pete.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-10T19:36:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93iv06$ans$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz>`

```
Peter E. C. Dashwood wrote in message
<93iri0$ij1$1@hermes.enternet.co.nz>...

>er...I believe that mapping the values to an 88 level is exactly what I
>recommended.
>
>So, I take it you have no issue with the code sample?

This is Usenet.  How dare you bring up facts?
;<)

>
>(You know very well, Donald, how rarely I post code samples ANYWHERE... On
…[4 more quoted lines elided]…
>

Quite.

>Nobody, least of all me, is disagreeing with your right to use whatever you
>want. My original statement was, THAT IN A BOOLEAN CONTEXT 1 and 0 make the
>most sense. (As Boolean Algebra is defined around these two symbols, I
can't
>see what all the fuss is about.) My personal preference is not to use YES
>and NO because I have worked in countries where these values are not the
…[8 more quoted lines elided]…
>Don't you think it is a tad insensitive, even discourteous and
disrespectful
>to the indigenous programmers who will maintain your code after you leave
if
>you
>code:
…[24 more quoted lines elided]…
>The first one says: "I am an English speaking programmer and you guys
better
>deal  with it.."
> The second one says: "Let's use the international language of Mathematics
…[3 more quoted lines elided]…
>ALL of them will work, and, as far as the computer programming is
concerned,
>can be argued to be equally valid. However, life is not just about computer
>programming, and working together as part of a team in exotic locations
…[6 more quoted lines elided]…
>

I am not really polite nor considerate when I write code ... but then I
write it for myself, not for anybody else.

It *is* an interesting question.  How do you reconcile human languages with
computer source code, if the requirement is for several different human
languages are involved.  I quite agree that the assumption of English is
rude.  Nevertheless, coding in Spanish, or German, or any other language is
just as restrictive.  Perhaps every data name in the source object should
have a language property, but then we would need an OOP compiler instead of
a structured compiler that can compile OOP syntax.

I do not see any solution that really works, with perhaps the exception of
the one used by the RC church for years.  Do it all in Latin.

Pax
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 9)_

- **From:** mike__c@my-deja.com
- **Date:** 2001-01-11T13:40:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93kd4i$6o$1@nnrp1.deja.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <93iv06$ans$1@news.igs.net>`

```
In article <93iv06$ans$1@news.igs.net>,
  "donald tees" <donald@willmack.com> wrote:
>
> I am not really polite nor considerate when I write code ... but then
I
> write it for myself, not for anybody else.
>
> It *is* an interesting question.  How do you reconcile human languages
with
> computer source code, if the requirement is for several different
human
> languages are involved.  I quite agree that the assumption of English
is
> rude.  Nevertheless, coding in Spanish, or German, or any other
language is
> just as restrictive.  Perhaps every data name in the source object
should
> have a language property, but then we would need an OOP compiler
instead of
> a structured compiler that can compile OOP syntax.
>
> I do not see any solution that really works, with perhaps the
exception of
> the one used by the RC church for years.  Do it all in Latin.
>
> Pax
>
>

At the moment I'm maintaining code for a German company. Variable names,
comments, etc. are all in German and I don't speak the lingo. I'm sure
a German speaker would say the code was self documenting, but it makes
little sense to me. I just follow the logic through the program and get
a translation whenever I need to insert a comment or variable name. One
good thing I've found is that I haven't been led astray by out of date
comments which tell you what a paragraph did back in the 80s, or by
spurious variable names that have an 88 level set to TRUE where you
expect a FALSE and vv.

0/1, T/F, Y/N, J/N, etc. don't make much of a difference when you see:
77  aaaaaaaaaa           pic x.
       88 bbbbb          value "0".
       88 ccccc          value "1".


Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2001-01-11T03:10:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Du976.12820$fO.567159@typhoon.austin.rr.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz>`

```

Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote
> Don't you think it is a tad insensitive, even discourteous and
disrespectful
> to the indigenous programmers who will maintain your code after you leave
if
> you code:
> if end-switch = "Y"
> when you could've coded:
> if todos-finitos... or  if finished
> ?

best would be:  si est� acabado
The mixing of IF and TODOS-FINITOS is terrible.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-11T20:50:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93js31$k18$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <Du976.12820$fO.567159@typhoon.austin.rr.com>`

```

Leif Svalgaard wrote in message ...
>
>Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote
…[12 more quoted lines elided]…
>
Hahaha!

I totally agree, Leif.

Now we can all go off and talk about Spanish, German, and French COBOL
compilers. Native Language versions of COBOL have been around for years. I
have worked with the French and German compilers (purely as an
exercise...not for serious work...and it was many years ago.)

There IS a conflict in using COBOL with non-English Language, because the
verbs are all in English.

You would need a Spanish COBOL compiler to accept:

'si estï¿½ acabado'

and even then, I doubt that it would support the verb "to be" (esta).

Amazingly, (at least, I found it amazing) the foreign programmers I have
come across are happier working with standard "English" COBOL than they are
with a Native Language version. (Maybe because it is more likely to have the
latest patches and fixes applied to it...?...I dunno)

The best I can do, as a vistor to their country and their site, is respect
their standards, and try not to appear arrogant about the use of English. I
never forget that they are speaking English to accommodate me. This is
reflected in my code.

Pete.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-01-11T07:04:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5DBD86.A8274964@brazee.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz>`

```


"Peter E. C. Dashwood" wrote:

> Let's say you are working in a country where Spanish is the first
> Language...
…[32 more quoted lines elided]…
> The last one says: "Is it time for my medication, yet?"

While CoBOL is based upon English, I have no problem in using Spanish words in
code intended to be maintained by Spanish speakers.   It is simple enough to
replace "Y" with "S".  But changing the switch value doesn't change the fact
that you named your variables "finished" and "NOT-finished".  Your first
statement has not changed.

If you switch from business speak to math speak in the switch values - your
variable names are still English, so you haven't changed your "I am an English
speaking programmer and you guys better deal  with it.." inference.

CoBOL isn't a math language.  It is a business language.  Use the terms and
values used by business.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-11T11:56:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B46C5365BD2DB722.7008AD6A28797E6F.D4361A492A0D633C@lp.airnews.net>`
- **References:** `<9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net>`

```
On Thu, 11 Jan 2001 07:04:55 -0700, Howard Brazee <howard@brazee.net>
enlightened us:

>
>
…[49 more quoted lines elided]…
>values used by business.

I don't want to nitpik here Howard, but Cobol is an English business
language.  As Peter has pointed out, Math (and it's symbols) is much
more universal than English even though English is the preferred
business language.

I've worked in countries (Thailand, Indonesia, etc.) where even the
Arabic alphabet is unfamiliar.  Many programmers can't speak English
and some can't even read it.  They learned the Cobol verbs the way you
or I would learn Assembler mnemonics.  So in many cases having a
switch that equats to Y for yes or N for N is a struggle for them to
understand wheras 0 and/or 1 is not.  As Peter pointed out, you need
to be mindful of your audience.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

In the beginning, God created earth and rested. 
Then God created man and rested. 
Then God created woman. 
Since then, neither God nor man has rested.



Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-01-11T14:30:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YJo76.71$BQ6.2403@news4.atl>`
- **References:** `<9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net> <B46C5365BD2DB722.7008AD6A28797E6F.D4361A492A0D633C@lp.airnews.net>`

```
"SkippyPB" <swiegand@neo.rr.com.nospam> wrote:
>
> I've worked in countries (Thailand, Indonesia, etc.) where even the
> Arabic alphabet is unfamiliar.  Many programmers can't speak English
> and some can't even read it.  They learned the Cobol verbs the way you
> or I would learn Assembler mnemonics.

I'm being picky Steve, but I think you mean the 'Roman Alphabet' and
Arabic numerals.  Thank God the West picked the best of both!  ;-)
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 11)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-12T12:36:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37738AD5F4A324D3.6C0CA49DE9FEC2EB.D54E0D1057A746F0@lp.airnews.net>`
- **References:** `<3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net> <B46C5365BD2DB722.7008AD6A28797E6F.D4361A492A0D633C@lp.airnews.net> <YJo76.71$BQ6.2403@news4.atl>`

```
On Thu, 11 Jan 2001 14:30:48 -0600, "Judson McClendon"
<judmc@bellsouth.net> enlightened us:

>"SkippyPB" <swiegand@neo.rr.com.nospam> wrote:
>>
…[6 more quoted lines elided]…
>Arabic numerals.  Thank God the West picked the best of both!  ;-)

Yes of course you are correct Judson.  Got my terms confused.  Seems
to be a common things these days.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

In the beginning, God created earth and rested. 
Then God created man and rested. 
Then God created woman. 
Since then, neither God nor man has rested.



Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-12T12:41:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93li52$mu3$4@hermes.enternet.co.nz>`
- **References:** `<9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net> <B46C5365BD2DB722.7008AD6A28797E6F.D4361A492A0D633C@lp.airnews.net>`

```

SkippyPB wrote in message ...

>I don't want to nitpik here Howard, but Cobol is an English business
>language.  As Peter has pointed out, Math (and it's symbols) is much
…[10 more quoted lines elided]…
>
Thanks, Steve.

I have nothing to add; you have said it all more concisely and eloquently
than I did <G>.

Pete.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-12T12:39:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93li50$mu3$3@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net>`

```

Howard Brazee wrote in message <3A5DBD86.A8274964@brazee.net>...
>

>While CoBOL is based upon English, I have no problem in using Spanish words
in
>code intended to be maintained by Spanish speakers.   It is simple enough
to
>replace "Y" with "S".  But changing the switch value doesn't change the
fact
>that you named your variables "finished" and "NOT-finished".  Your first
>statement has not changed.
>
>If you switch from business speak to math speak in the switch values - your
>variable names are still English, so you haven't changed your "I am an
English
>speaking programmer and you guys better deal  with it.." inference.
>
No issue here, Howard. I was simply trying to make a point using a
light-hearted example. Had I put everything in Spanish, the intended
audience would not have understood it... (actually, I DID replace "finished"
with "todos-finitos" which I figured most people would have no difficulty
with. Then Leif beat me up because it was "horrible"!...<G>)

The real point is to be sensitive to foreign speakers, if you are working
with them.

(Hey, it's only common courtesy, after all....)


>CoBOL isn't a math language.  It is a business language.  Use the terms and
>values used by business.
>
Yes, it isn't a math language, but the symbols of Mathematics are more
universally familiar than the symbols of any given spoken language.

I'm not using Math notation because I think COBOL should be Maths oriented;
I'm doing it because it makes sense and because my intended audience
(foreign speaking programmers) can see that at least I made the effort to
use something we can ALL relate to...(Surprisingly, I have had programmers
remark on it and they DO notice...)

I agree that the Business terms are more important... (I went to a lot of
trouble in Spain to learn the terms pertinent to the business...to this day
I think of "Treasury Bonds" as "Bonos de Tresoradios"...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 10)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-01-12T12:42:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A0DF7C2AC9AF9A4.1CCDACC5C80F9EA7.60C817A7641C09B3@lp.airnews.net>`
- **References:** `<9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl> <2JR66.2917$b25.111926@newsread2.prod.itd.earthlink.net> <93hpc2$gh0$1@hermes.enternet.co.nz> <93hqrm$m4j$1@news.igs.net> <93iri0$ij1$1@hermes.enternet.co.nz> <3A5DBD86.A8274964@brazee.net> <93li50$mu3$3@hermes.enternet.co.nz>`

```
On Fri, 12 Jan 2001 12:39:10 +1300, "Peter E. C. Dashwood"
<dashwood@enternet.co.nz> enlightened us:

>
>Howard Brazee wrote in message <3A5DBD86.A8274964@brazee.net>...
…[44 more quoted lines elided]…
>Pete.

Just as an add on to what Peter has stated, the suite of software that
my employer sells has been totally converted into Spanish.  We found
when we started doing business in Mexico and later South America that
the programmers were having real difficulties with our English usage
in Cobol programs.  So we hired some multi-lingual folks and converted
all screen and report literals to Spanish, all data names (as much as
possible) to Spanish and anything else that made sense to convert.  We
did not convert our Assembler programs because they're not English
anyway :)

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

In the beginning, God created earth and rested. 
Then God created man and rested. 
Then God created woman. 
Since then, neither God nor man has rested.



Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-14T09:59:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A617883.53FAC1E6@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <QxQ56.11135$Ps.465781@newsread2.prod.itd.earthlink.net> <FKF66.1568$gN3.82804@news1.atl>`

```
> "Jerry P" <jerryp@bisusa.com> wrote:
> >
…[3 more quoted lines elided]…
> > the Boolean Tribe.

Zero and 1 do indeed have a very strong relationship to reality, the
reality of how computers actually work.  Most computers have AND, OR,
XOR, NOT and NAND gates which are exactly how many forms of logic work.

In many languages the complex conditional tests that are coded in the
source language are processed at the lowest level directly be the
machine instructions to arrive at true or false results.  To ensure that
this works correctly in all cases many languages use 0 to mean false
(none, empty, null, not set, off) and any other value to mean true
(occupied, full, set, on).

If you cannot relate this to the realities that you do know of, then
perhaps you should expand the set of realities in which you operate.
```

##### ↳ ↳ Re: number of days between dates

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-08T07:09:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A5967AD.2724D2B0@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz>`

```
> However, it is NOT a good example of  modern COBOL code and, as there are a
> number of new COBOL programmers who frequent this forum I suggest it be
> amended as follows:
>
>       [etc....]


> [Please, please, newbies, resist the urge to set flags to 'Y' or 'N'. Use 88
> levels; that's what they're for. COBOL is intended to be a Self-Documenting
> Language... Besides, it is arrogant to assume the whole world uses "Yes" and
> "No"  (it doesn't) and, in terms of pure logic, "1" and "0" are better
> Boolean representations of a truth value.)

I dislike SET verbs and 88 levels.  One major problem is that they make
it difficult to find all use of a flag variable using text search or
greps.  It is often necessary to do several searches on each 88 name.

I don't see that use of SET makes the code 'more modern', it has been in
the language for decades.


> Unfortunately, not all implementations of COBOL allow a value to be set to
> FALSE, so it is necessary to provide for both TRUE and FALSE with 88 levels,
…[3 more quoted lines elided]…
> to SHOUT") as it is easier on the eyes than Upper Case.]

You have simply traded 'all upper' to 'all lower'.  While 'all upper'
may look archaic and C uses 'all lower', this (IMHO) does not improve
its readability or make it 'more modern'.  After all, while Cobol is 40
years old, C is 30 and C++ is 20 years old.

I prefer to have all the reserved words in upper case and others in
proper case (first letter and prefixes capitalised).  ie Modula-2
style.  This is easy to arrange with my editor as I have most of the
reseverved words available with 2 key-strokes and they are in upper
case.

What is most readable depends entirely on what one is used to reading. 
If someone has only seen 'all upper' then they will have great
difficulty relating to 'all lower', and vv.
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-07T15:31:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93ajgs$mpi$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz>`

```
Richard Plinston wrote in message <3A5967AD.2724D2B0@Azonic.co.nz>...
>
>What is most readable depends entirely on what one is used to reading.
>If someone has only seen 'all upper' then they will have great
>difficulty relating to 'all lower', and vv.

I agree.  A lot of it is simple habit.  I have found myself, lately, using
upper
case for standard Cobol, but lower case for OOP properties.  It works for
me.
```

###### ↳ ↳ ↳ Re: number of days between dates

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2001-01-08T01:44:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a5919c6.2444248@nntp.sprynet.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz>`

```
On Mon, 08 Jan 2001 07:09:33 +0000, Richard Plinston <riplin@Azonic.co.nz>
wrote:

>> However, it is NOT a good example of  modern COBOL code and, as there are a
>> number of new COBOL programmers who frequent this forum I suggest it be
…[16 more quoted lines elided]…
>the language for decades.

I like 88-levels because it's easier to tell what something means.  "MOVE 9 TO
COMMAND" doesn't mean much, where as SET COMMAND-DELETE TO TRUE" does.  However,
I totally understand your point.  One thing I like about C is enumerated types.
I haven't used C in ages, but if I recall correctly you can do something like:

enum {command-delete=9, command-add=8, command-replace=7} command;

Then you say "command = command-delete".  That would be the same as "command =
7" (moving 7 to a variable named 'command').

This way you can easily search for your variable by name, and yet have value
assignments that are easy to read.

Oh well...
Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-01-14T16:23:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93t54l$sj4$1@news.igs.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com>`

```

"Frank Swarbrick" <infocat@sprynet.com> wrote in message
news:3a5919c6.2444248@nntp.sprynet.com...
> On Mon, 08 Jan 2001 07:09:33 +0000, Richard Plinston <riplin@Azonic.co.nz>
> wrote:
>
> >> However, it is NOT a good example of  modern COBOL code and, as there
are a
> >> number of new COBOL programmers who frequent this forum I suggest it be
> >> amended as follows:
…[4 more quoted lines elided]…
> >> [Please, please, newbies, resist the urge to set flags to 'Y' or 'N'.
Use 88
> >> levels; that's what they're for. COBOL is intended to be a
Self-Documenting
> >> Language... Besides, it is arrogant to assume the whole world uses
"Yes" and
> >> "No"  (it doesn't) and, in terms of pure logic, "1" and "0" are better
> >> Boolean representations of a truth value.)
…[8 more quoted lines elided]…
> I like 88-levels because it's easier to tell what something means.  "MOVE
9 TO
> COMMAND" doesn't mean much, where as SET COMMAND-DELETE TO TRUE" does.
However,
> I totally understand your point.  One thing I like about C is enumerated
types.
> I haven't used C in ages, but if I recall correctly you can do something
like:
>
> enum {command-delete=9, command-add=8, command-replace=7} command;
>
> Then you say "command = command-delete".  That would be the same as
"command =
> 7" (moving 7 to a variable named 'command').
>
> This way you can easily search for your variable by name, and yet have
value
> assignments that are easy to read.
>
> Oh well...
> Frank Swarbrick

You can do the exact same thing in Cobol, and not use 88's at all. The 88
level and the SET verb are just a convenience, most of making code easy to
read is just a matter of thinking about it for thirty seconds.  There are no
"right and wrong" ways.  Just readable ways and obscure ways.

        01 commands                    picture x.
        01 read-command    picture x value "r".
        01 write-command    picture x value "w".

    move read-command to commands.
    perform do-the-command.

    if commands is equal to read-command
            etc.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-15T16:40:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A6327F5.1ED9DD79@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com>`

```
Frank Swarbrick wrote:
> >
> >I dislike SET verbs and 88 levels.  One major problem is that they make
> >it difficult to find all use of a flag variable using text search or
> >greps.  It is often necessary to do several searches on each 88 name.

> I like 88-levels because it's easier to tell what something means.  "MOVE 9 TO
> COMMAND" doesn't mean much, where as SET COMMAND-DELETE TO TRUE" does.  However,
…[9 more quoted lines elided]…
> assignments that are easy to read.

Exactly, it is not hard to do this exact thing in Cobol.  

      01  Command-Values.
          03  Cammand-Delete        PIC 9 VALUE 9.
          03  Command-Add           PIC 9 VALUE 8.
          03  .....

          MOVE Command-Delete     TO Command

Or use 78s or Symbolic literals or equivalent.

No 88 levels or SETs are required.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-14T21:44:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93trl4$mqo$1@slb7.atl.mindspring.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3A6327F5.1ED9DD79@Azonic.co.nz...
> Frank Swarbrick wrote:
> > >
 <snip>
>
> Or use 78s or Symbolic literals or equivalent.
>
> No 88 levels or SETs are required.

Use of 78-levels (not 77-levels) is QUITE implementor-specific (and is not
part of the ANSI/ISO Standard - and *may* go away in the future when the
"CONSTANT" attribute is added to Standard COBOL).
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** "TJ Dombrowski" <keldin@earthlink.not>
- **Date:** 2001-01-15T05:54:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1gw86.29991$U4.860523@newsread1.prod.itd.earthlink.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz>`

```
One of the easier ways to subtract dates is to convert to Julian like
2001014 for Jan 14 2001
and subtract them.   other wise you will have to deal with does the month
have 28,29,30, or 31 days and such
which is much harder.


"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3A6327F5.1ED9DD79@Azonic.co.nz...
> Frank Swarbrick wrote:
> > >
…[4 more quoted lines elided]…
> > I like 88-levels because it's easier to tell what something means.
"MOVE 9 TO
> > COMMAND" doesn't mean much, where as SET COMMAND-DELETE TO TRUE" does.
However,
> > I totally understand your point.  One thing I like about C is enumerated
types.
> > I haven't used C in ages, but if I recall correctly you can do something
like:
> >
> > enum {command-delete=9, command-add=8, command-replace=7} command;
> >
> > Then you say "command = command-delete".  That would be the same as
"command =
> > 7" (moving 7 to a variable named 'command').
> >
> > This way you can easily search for your variable by name, and yet have
value
> > assignments that are easy to read.
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-15T06:53:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i7x86.19897$ag.637994@newsread2.prod.itd.earthlink.net>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz> <1gw86.29991$U4.860523@newsread1.prod.itd.earthlink.net>`

```

"TJ Dombrowski" <keldin@earthlink.not> wrote in message
news:1gw86.29991$U4.860523@newsread1.prod.itd.earthlink.net...
> One of the easier ways to subtract dates is to convert to Julian
like
> 2001014 for Jan 14 2001
> and subtract them.   other wise you will have to deal with does the
month
> have 28,29,30, or 31 days and such
> which is much harder.

Huh?

How you gonna convert to Julian without using 28 - 31? (absent
functions, of course)
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 7)_

- **From:** "Timothy" <timhillock@home.com>
- **Date:** 2001-01-26T00:42:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uJ3c6.244197$59.61403237@news3.rdc1.on.home.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz> <1gw86.29991$U4.860523@newsread1.prod.itd.earthlink.net> <i7x86.19897$ag.637994@newsread2.prod.itd.earthlink.net>`

```

Jerry P <jerryp@bisusa.com> wrote in message
news:i7x86.19897$ag.637994@newsread2.prod.itd.earthlink.net...
>
> "TJ Dombrowski" <keldin@earthlink.not> wrote in message
…[15 more quoted lines elided]…
>
 Jerry,  TJ means the 28, 29, 30 and 31 are the number of days in a given
month.  Converting to a Julian date means that the math will be more simple
to work out.   For each day/date in the normal calendar, there is a
corresponding number in the Julian format, as per following examples:

    Jan 1 - Day 1
    Jan 2 - Day 2
    Jan 3 - Day 3
    .....etc.......
    Jan 30 - Day 30
    Jan 31 - Day 31
    Feb 1 - Day 32
    Feb 2 - Day 33
    .......etc............
    Feb 26 - Day 57
    Feb 27 - Day 58
    Feb 28 - Day 59
                                Feb 29 - Day 60  (Leap year)
    Mar 1 - Day 60 ...............- Day 61
    Mar 2 - Day 61 ...............- Day 62
    Mar 3 - Day 62 ...............- Day 63
           .etc..............................
    Dec 30 - Day 363 ...........- Day 364
    Dec 30 - Day 364 ...........- Day 365
    Dec 31 - Day 365 ...........- Day 366


Tim
Day 25 of the 21st Century and 3rd Millenniun.
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 8)_

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2001-01-26T11:14:42
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94rmc3$leg$1@venus.telepac.pt>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz> <1gw86.29991$U4.860523@newsread1.prod.itd.earthlink.net> <i7x86.19897$ag.637994@newsread2.prod.itd.earthlink.net> <uJ3c6.244197$59.61403237@news3.rdc1.on.home.com>`

```
The information given bellow, although widely used, seems a bit inacurate to
me.
For a complete and very well written description of Julian Day calculations,
see Calendar FAQ by Claus Toreding (http://www.pauahtun.org/CalendarFAQ/)


"Timothy" <timhillock@home.com> wrote in message
news:uJ3c6.244197$59.61403237@news3.rdc1.on.home.com...
>
> Jerry P <jerryp@bisusa.com> wrote in message
…[20 more quoted lines elided]…
> month.  Converting to a Julian date means that the math will be more
simple
> to work out.   For each day/date in the normal calendar, there is a
> corresponding number in the Julian format, as per following examples:
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 5)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2001-01-15T19:28:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a634de8.5032339@nntp.sprynet.com>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz>`

```
On Mon, 15 Jan 2001 16:40:21 +0000, Richard Plinston <riplin@Azonic.co.nz>
wrote:

>Frank Swarbrick wrote:
>> >
…[28 more quoted lines elided]…
>No 88 levels or SETs are required.

Seems to me that would take up working-storage unnecessarily.  Setting 88-levels
would only make an entry into the literal pool, and only if that particular
88-level is used.

Of course, maybe the optimizer would get rid of not used 03-levels, but then
again maybe not.  

Also, in the case of C enumerated types I don't think you can set the variable
to a value of anything other than the specified enumerated types.

Anyway, no big deal.  I'm only stating my personal bias/preference.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: number of days between dates

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-16T10:56:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A6428C8.7DC31226@Azonic.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz> <3A5967AD.2724D2B0@Azonic.co.nz> <3a5919c6.2444248@nntp.sprynet.com> <3A6327F5.1ED9DD79@Azonic.co.nz> <3a634de8.5032339@nntp.sprynet.com>`

```
Frank Swarbrick wrote:
> >>
> >> This way you can easily search for your variable by name, and yet have value
…[8 more quoted lines elided]…
> 88-level is used.

Yes of course, that is why I suggested the alternatives (where available
and suitable) of 78s or equivalents or of symbolic constants.

Using a literal value in code _may_ (depending on compiler) create a new
entry in the literal pool for each usage.  So:

	AT END MOVE "Y"		TO EoF
	..
	IF ( EoF = "Y" )

may indeed cost 2 literal table entries.  Whereas use of a descriptive
variable with this value will not create any literal table entry but
will have a variable declaration.  Thus the variables will save space
compared to using literals.

Whether an 88 level generates a separate literal entry for each usage or
uses some other mechanism depends on how the implementation has been
done.  for example it may be that a particular compiler could convert:

        SET EoF-Detected TO TRUE
  into  MOVE "Y"      TO EoF-Flag

and then compile this code giving a new literal table entry for each
reference.		

Which code 'wastes' more space is not a simple matter of asserting that
one or the other will.


> Also, in the case of C enumerated types I don't think you can set the variable
> to a value of anything other than the specified enumerated types.

Yes of course, that is why I suggested the alternatives (where available
and suitable) of 78s or equivalents or of symbolic constants.

Decades ago I used a compiler that had a 'CONSTANTS SECTION' that
prevented changing the values of the decalrations within it.

> Anyway, no big deal.  I'm only stating my personal bias/preference.
```

##### ↳ ↳ Re: number of days between dates

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2001-01-10T13:46:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93hlco$gb1$1@hermes.enternet.co.nz>`
- **References:** `<bQJ46.4569$jo.56099329@tomcat.sk.sympatico.ca> <3a538214$0$57191$272ea4a1@news.execpc.com> <ZHL46.4584$jo.52232273@tomcat.sk.sympatico.ca> <9304tj$92n$1@slb1.atl.mindspring.net> <aTQ46.1354$Er.229814@newsrump.sjc.telocity.net> <3A54304E.EFC47152@worldnet.att.net> <938dom$1q0$1@hermes.enternet.co.nz>`

```
Well,

That certainly evoked some passionate responses.

I had no idea you guys cared so much...<G>

It was interesting that while many of you, quite properly, disputed my
opinions, nobody actually said they didn't like the suggested code.

Actually, I don't care what people use as flag and switch values...as long
as it is documented with an 88 level so that it is never referenced. I would
agree that coding:

if switch = '1' ...

is every bit as bad as coding:

if switch = 'Y' ...

or coding:

if switch = [anything else]

None of it tells us anything about the purpose of switch.

As for Upper/Lower case, again, my personal preference is for Mixed and a
number of studies support this view, but, hey, if you prefer something else,
good.

One of the problems is that when people first start out in COBOL (and my
message was aimed at newcomers) there is no way of knowing what is good
style or what isn't, and why.

Style is necessarily based on opinion and this will differ.

My opinion is based on 35 years of using the Language on all kinds of
platforms and environments all over the planet...so I feel qualified to
offer an opinion.

However, what is offered is just that: an opinion. (albeit, an informed one)

I will gladly give the reasons which caused me to reach this opinion, but it
is no more valid than anybody else's and you will notice that the code I
posted was "suggested".

Now, anybody like to change the "suggested" code?

Further comments below...


Peter E. C. Dashwood wrote in message
<938dom$1q0$1@hermes.enternet.co.nz>...

>Arnold Trembley wrote in message <3A54304E.EFC47152@worldnet.att.net>...
><Snipped>
…[20 more quoted lines elided]…
>
I like this solution very much. It will run on just about ANY machine and
compiler options are not going to make any difference to it.

However, it is NOT a good example of  modern COBOL code and, as there are a
number of new COBOL programmers who frequent this forum I suggest it be
amended as follows:

01   year-yyyy.
       12  year-cc pic 99.
       12  year-yy pic 99.
[there is no need for the redefinition, and usage defaults to DISPLAY...]

01   leap-year-flag  pic x value space.
        88 its-a-leap-year    value '1'.
        88 its-NOT-a-leap-year value '0'.

01  leap-year-test pic 9.
       88 no-remainder  value zero.

01  useless-junk    pic 99.

...

if year-yy = zero
   divide year-cc by 4
               giving useless-junk
               remainder leap-year-test
else
   divide year-yy by 4
              giving useless-junk
               remainder leap-year-test
end-if
if no-remainder
   set its-a-leap-year to TRUE
else
   set its-NOT-a-leap-year to TRUE
end-if

if its-a-leap-year
      [etc....]


I shall now annotate the opinions expressed below...[annotation in square
brackets]
>>>
"Please, please, newbies, resist the urge to set flags to 'Y' or 'N'. Use 88
levels; that's what they're for. "

[This should be updated to say "resist the urge to TEST flags with 'Y or
'N'". The values can be anything you feel comfortable with]


COBOL is intended to be a Self-Documenting
Language... Besides, it is arrogant to assume the whole world uses "Yes" and
"No"  (it doesn't) and, in terms of pure logic, "1" and "0" are better
Boolean representations of a truth value.)

[This cannot be argued, as anyone who has studied Boolean Algebra and
Propositional Calculus will understand. You CAN represent values with
ANYTHING, but it is then no longer Boolean (George Boole based his Algebra
on a Binary system, using 1 and 0. Despite the Poison Dwarf's attempt to
muddy the water, 1 is TRUE and 0 is FALSE. (Sorry, Doc, it's defined that
way and is therefore axiomatic, SO LONG as you want to call it
"Boolean"...<G> I also realise that you may well decide not to do so, in
which case whatever you want is OK...<G>))]

Unfortunately, not all implementations of COBOL allow a value to be set to
FALSE, so it is necessary to provide for both TRUE and FALSE with 88 levels,
then set the required one to TRUE, as shown above.

[No comment. Bill Klein might like to comment on where the COBOL standard is
with Set ...to FALSE?]

Also, where your environment supports it, use lower case ("there's no need
to SHOUT") as it is easier on the eyes than Upper Case.
[However, if you are working on a site or in an environment where this is
not the norm, adhere to what is usual.]

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
