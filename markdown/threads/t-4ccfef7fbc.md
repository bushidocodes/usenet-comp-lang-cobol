[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Numval

_15 messages · 8 participants · 2004-04_

---

### Numval

- **From:** RPHILISTINE@UNITECHSYS.COM (Ralph)
- **Date:** 2004-04-22T06:29:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Hi,

I am having an accuracy problem with the numval function.  This is a
clip from my debugger:

10 IGELEMVALNUM0                   PIC S9(18) COMP-3   ADDR 	008F9DF8 
 	    VALUE 	> 	+106896201177201599      	<
10 IIP-IGELEMVALTEXT-TEXT          PIC X(256)          ADDR 	008A59C4 
 OCCURRENCE 	( 	   1 	)
 	    VALUE 	> 	+106896201177201605                                
...
   COMPUTE IGELEMVALNUM0 =                                           
   FUNCTION NUMVAL (IIP-IGELEMVALTEXT-TEXT(IGELEM-IDX))              

As you can see from the results of my compute statement, I am getting
a value that is off by 6. My thoughts are that it's due to the size of
the variable since my other tests have been successful with the numval
conversion.  Has there been any documentation that speaks to this
apparent bug with the numval function? Has anyone seen this before?
Any help would be greatly appreciated.
```

#### ↳ Re: Numval

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-22T18:49:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HsUhc.7138$e4.1032@newsread2.news.pas.earthlink.net>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
What compiler?  Have you contacted the vendor?

FYI - I remember that ONE vendor actually used "floating point" for their
original NumVal implementation.  (Unfortunately, the Intrinsic Function
amendment was NOT clear that NumVal should give an "exact" value).  I have NOT
heard of this problem recently, but it could be your problem.
```

##### ↳ ↳ Re: Numval

- **From:** RPHILISTINE@UNITECHSYS.COM (Ralph)
- **Date:** 2004-04-22T15:11:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47fa0497.0404221411.6d8b41bc@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <HsUhc.7138$e4.1032@newsread2.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<HsUhc.7138$e4.1032@newsread2.news.pas.earthlink.net>...
> What compiler?  Have you contacted the vendor?
> 
…[29 more quoted lines elided]…
> > Any help would be greatly appreciated.

Thanks for the reply.  I will ask my systems administrator about the
compiler version.  It seems to work as documented when the text string
is 17 bytes.  It's always that 18th byte that throws a wrench into
things.
```

###### ↳ ↳ ↳ Re: Numval

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2004-04-22T23:08:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfYhc.11635$_o3.378612@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <HsUhc.7138$e4.1032@newsread2.news.pas.earthlink.net> <47fa0497.0404221411.6d8b41bc@posting.google.com>`

```

> > "Ralph" <RPHILISTINE@UNITECHSYS.COM> wrote in message
> > news:47fa0497.0404220529.12a6de47@posting.google.com...
…[19 more quoted lines elided]…
> > > Any help would be greatly appreciated.

What do you get if you remove the COMP-3 ?

What do you get if you change to PIC S9(19) COMP-3
to eliminate the slack byte ?
```

###### ↳ ↳ ↳ Re: Numval

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-22T23:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7AYhc.5550$eZ5.4482@newsread1.news.pas.earthlink.net>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <HsUhc.7138$e4.1032@newsread2.news.pas.earthlink.net> <47fa0497.0404221411.6d8b41bc@posting.google.com> <UfYhc.11635$_o3.378612@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:UfYhc.11635$_o3.378612@bgtnsc05-news.ops.worldnet.att.net...
<snip>
> What do you get if you remove the COMP-3 ?
>
> What do you get if you change to PIC S9(19) COMP-3
> to eliminate the slack byte ?
>

FYI - for those of you not on a compiler that allows for greater than 18 digits,
there are some that DO allow more (as an extension to the '85 Standard).  The
2002 Standard allows for up to 31 digits.
```

#### ↳ Re: Numval

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-04-22T16:35:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kdidnTDw5b8spxXdRVn-jw@giganews.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Ralph wrote:
> Hi,
>
…[17 more quoted lines elided]…
> Any help would be greatly appreciated.

"OCCURRENCE(  1)"  ???

Try this:
PERFORM VARYING I FROM 1 BY 1 UNTIL I > BIG-NUMBER
   IF I NOT = FUNCTION NUMVAL(I)
       DISPLAY 'EEK!"
   END-IF
END-PERFORM

Or something similar.
```

#### ↳ Re: Numval

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2004-04-22T15:25:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cDXhc.19$DB.4@dfw-service2.ext.ray.com>`
- **In-Reply-To:** `<47fa0497.0404220529.12a6de47@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Ralph wrote:
> Hi,
> 
…[17 more quoted lines elided]…
> Any help would be greatly appreciated.

I ran your test using OS/390 V2R10 and Enterprise COBOL, using targets 
which were Display, Binary, and Packed-Decimal, all PIC S9(18).  Here 
are the results:
INPUT-FIELD    = 106896201177201605
AFTER COMPUTE:
NUMVAL-DISPLAY = 10689620117720159I.
NUMVAL-BINARY  = 0106896201177201600.
NUMVAL-PACKED  = 106896201177201599.

Looks broken to me!

With 17 input digits, and 18 digit targets, I got correct answers:
INPUT-FLD2     = 10689620117720160
AFTER COMPUTE:
NUMVAL-DISPLAY2= 01068962011772016:.
NUMVAL-BINARY2 = 0010689620117720160.
NUMVAL-PACKED2 = 010689620117720160.
```

##### ↳ ↳ Re: Numval

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-22T23:28:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uyYhc.5549$eZ5.5116@newsread1.news.pas.earthlink.net>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <cDXhc.19$DB.4@dfw-service2.ext.ray.com>`

```
Colin,
   Can we say "PMR"????  (Let me know if you have any problems getting IBM to
accept this as "APARABLE".)

P.S.  As long as you are using Enterprise COBOL - did you try this with both
ARITH(EXTEND) and "COMPAT"?  It should NOT make any difference, but it might
anyway <G>
```

###### ↳ ↳ ↳ Re: Numval

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2004-04-22T20:42:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mIOdnZ29VIkvDRXdRVn-sA@adelphia.com>`
- **In-Reply-To:** `<uyYhc.5549$eZ5.5116@newsread1.news.pas.earthlink.net>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <cDXhc.19$DB.4@dfw-service2.ext.ray.com> <uyYhc.5549$eZ5.5116@newsread1.news.pas.earthlink.net>`

```
William M. Klein wrote:

>Colin,
>   Can we say "PMR"????  (Let me know if you have any problems getting IBM to
…[7 more quoted lines elided]…
>
Bill,
I'll give that a shot tomorrow, along with any other arithmetic related 
option changes I can see that might affect things.
Colin
```

#### ↳ Re: Numval

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-04-22T20:18:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<108grotec067231@corp.supernews.com>`
- **In-Reply-To:** `<47fa0497.0404220529.12a6de47@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Ralph wrote:
> Hi,
> 
…[17 more quoted lines elided]…
> Any help would be greatly appreciated.

Could the sign along with the 18 digits be causing this?  I'm not quite 
sure how that's addressed in the COBOL 85 standard.  If you don't need a 
signed variable, try dropping that and see if you get accurate results. 
  If you do, and that's acceptable, you've fixed it.  If you don't, or 
you do but that's not acceptable, I'd contact the vendor to get their 
take on it.  Maybe you've uncovered a seam - I did that just today on my 
compiler.  :)
```

##### ↳ ↳ Re: Numval

- **From:** RPHILISTINE@UNITECHSYS.COM (Ralph)
- **Date:** 2004-04-23T06:36:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47fa0497.0404230536.5b6e4168@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <108grotec067231@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote in message news:<108grotec067231@corp.supernews.com>...
> Ralph wrote:
> > Hi,
…[38 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I have tried it without the sign and without the comp-3.  I am still
waiting for a reply from my systems programmer as to the nature of the
compiler.  But changing compilers during the QA process is not exactly
something I can do.  Right now I am coding a work around for instances
where the field is greater than 17 bytes.  Thanks to all for your
replies they were very helpful.  At least I know I'm not going crazy.
```

###### ↳ ↳ ↳ Re: Numval

- **From:** docdwarf@panix.com
- **Date:** 2004-04-23T09:59:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6b7f4$d6j$1@panix5.panix.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <108grotec067231@corp.supernews.com> <47fa0497.0404230536.5b6e4168@posting.google.com>`

```
In article <47fa0497.0404230536.5b6e4168@posting.google.com>,
Ralph <RPHILISTINE@UNITECHSYS.COM> wrote:

[snip]

>Thanks to all for your
>replies they were very helpful.  At least I know I'm not going crazy.

Well... at least you know that in this instance there are others who 
report seeing the same, or similar things.

DD
```

###### ↳ ↳ ↳ Re: Numval

- **From:** Gus <GusPod@optOFFline.XXXX.net>
- **Date:** 2004-04-23T17:58:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<APcic.108571$_g4.25757073@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<47fa0497.0404230536.5b6e4168@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com> <108grotec067231@corp.supernews.com> <47fa0497.0404230536.5b6e4168@posting.google.com>`

```
Ralph wrote:
> LX-i <lxi0007@netscape.net> wrote in message news:<108grotec067231@corp.supernews.com>...

(snip)

> I have tried it without the sign and without the comp-3.  I am still
> waiting for a reply from my systems programmer as to the nature of the
…[3 more quoted lines elided]…
> replies they were very helpful.  At least I know I'm not going crazy.

Independent variables.  ;)
```

#### ↳ Re: Numval

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-04-23T08:46:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BuKdnQc6ObWtgxTdRVn-jw@giganews.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Ralph wrote:
> Hi,
>
…[17 more quoted lines elided]…
> Any help would be greatly appreciated.

Hmm.

For what it's worth, the Fujitsu compiler for the PC returns the correct
value.
```

#### ↳ Re: Numval

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2004-04-23T11:50:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Adic.7$0O2.6@dfw-service2.ext.ray.com>`
- **In-Reply-To:** `<47fa0497.0404220529.12a6de47@posting.google.com>`
- **References:** `<47fa0497.0404220529.12a6de47@posting.google.com>`

```
Ralph wrote:
> Hi,
> 
…[17 more quoted lines elided]…
> Any help would be greatly appreciated.

Ralph,
I ran again on Friday morning.  I'm using the IBM compiler "Enterprise 
COBOL for z/OS and OS/390 V3R2" on an OS/390 V2R10 system.  For this 
compile, I used the option ARITH(EXTEND), and this time, I got the 
correct results for the 18-digit case:
INPUT-FIELD    = 106896201177201605
AFTER COMPUTE:
NUMVAL-DISPLAY = 10689620117720160E.
NUMVAL-BINARY  = 0106896201177201605.
NUMVAL-PACKED  = 106896201177201605.
 

INPUT-FLD2     = 10689620117720160
AFTER COMPUTE:
NUMVAL-DISPLAY2= 01068962011772016:.
NUMVAL-BINARY2 = 0010689620117720160.
NUMVAL-PACKED2 = 010689620117720160.

By the way, if you are running on an IBM mainframe, you can answer the 
question of "what compiler am I using" simply by looking at the first 
line of your listing.  The product name and product number appear there, 
as well as sometimes an indicator of the maintenance level.  You don't 
need to ask a systems programmer for this information.
Example:
1PP 5655-G53 IBM Enterprise COBOL for z/OS and OS/390 3.2.0

Colin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
