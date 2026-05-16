[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DISPLAY Statement Throwing Trash No Matter What

_37 messages · 10 participants · 2009-02 → 2009-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-20T15:21:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnmhp4$95$1@reader1.panix.com>`

```

Platform: Big Blue Mainframe
Compiler: IBM Enterprise COBOL for z/OS  3.4.1

Well... here's a simple one that everyone can join in on!

A program that I deal with does a six-input flat-file match/merge, a bunch 
of processing and generates (among other things) two files for two 
different accounting systems.

Another program in the same jobstream uses those two outputs as inputs and 
'cross-foots' them; it matches the records by employee and then adds up 
different fields from both files into a total.  One of these totals is 
subtracted from the other and the difference should be zero.

Total numbers of employees thusly checked is about 70,000 and - mirable 
dictu! - usually they crossfoot out to zero.  For every run, though, there 
are some records that don't match... sometimes there are reasons for these 
(one accounting system groups categories differently or ignores certain 
fields)... but for each run there's always at least one record that falls 
into the 'I dunno what the problem is but they don't zero out.'

Still with me?  The essence is:

ADD FLD01 OF FILE01
    FLD02 OF FILE01
    FLD03 OF FILE01
...
    FLD99 OF FILE01 GIVING CHECK-TOT01.

ADD FLD01 OF FILE02
    FLD02 OF FILE02
    FLD03 OF FILE02
...
    FLD99 OF FILE02 GIVING CHECK-TOT02.

SUBTRACT CHECK-TOT02 FROM CHECK-TOT01 GIVING DIFF.
IF DIFF NOT = 0
    DISPLAY 'CROSSFOOT ERROR FOR SSN '
             SOC-SEC-NO               
            ' ACCOUNTING NO '                   
            ACCTNG-NO            
            ' SECTION '                    
            SECTION-NO           
            ' AMOUNT IS '             
            DIFF.

(cursory examination of fields, including DIFF, show them as some kind of 
S9(n)V99 COMP-3.)

As things stand now the DISPLAY results in lines like:

CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 SECTION 06920 AMOUNT 
IS 0000000590Q+
CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 SECTION 06955 AMOUNT 
IS 0000000400}+

... et and cetera.  So... for DIFF (PIC S9(9)V99 VALUE +0.) I defined 
DIFF-Z PIC ZZZ,ZZZ,ZZ9.99-. , put in a 'MOVE DIFF TO DIFF-Z' and changed 
the DISPLAY... and now I get

CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 SECTION 06920 AMOUNT 
IS         344+9 
CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 SECTION 06955 
AMOUNT IS          40+0

... and I cannot get it formatted as it should be.  I've tried defining 
DIFF-N PIC S9(9)V99 VALUE +0., MOVE DIFF to DIFF-N, MOVE DIFF-N to 
DIFF-Z... same results: no decimal point and a sign-indicator in the 
middle of the number.  Likewise with ADD 0, DIFF GIVING DIFF-Z, MULTIPLY 
DIFF BY 1 GIVING DIFF-Z and DIVIDE DIFF BY 1 GIVING DIFF-Z... all the 
usual Journeyman's tricks.

This isn't an Urgent Matter... folks have been living with AMOUNT IS 
0000000590Q+ for years... but it doth make me wonder why stuff that I was 
taught in my earliest COBOL courses no longer seems to hold true.  There 
are enough arithmetic operations being done on the data so that 
non-numerics would have caused it to blow up long ago... is there some 
whacky compiler directive I should be redirecting?

Thanks much.

DD
```

#### ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-20T10:57:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eiBnl.214000$zQ4.101913@en-nntp-02.dc1.easynews.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com>`

```
Doc,
  Easy (possibly temporary) fix (as long as you are moving it to a 
numeric-edited field) is
instead of:
  DIFF-Z  PIC ZZZ,ZZZ,ZZ9.99-.
code
  DIFF-Z  Pic ----,---,--9.99.
or better (IMHO)
  DIFF-Z  Pic+ +++,+++,++9.99.

HOWEVER,  there is something else going wrong (I think).  I think there is an 
actual "+" in the middle of the data.  Is there an "IF NUMERIC" test before the 
display?
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-20T17:56:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnmqs2$hpt$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <eiBnl.214000$zQ4.101913@en-nntp-02.dc1.easynews.com>`

```
In article <eiBnl.214000$zQ4.101913@en-nntp-02.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Doc,
>  Easy (possibly temporary) fix (as long as you are moving it to a 
…[4 more quoted lines elided]…
>  DIFF-Z  Pic ----,---,--9.99.

Wow... this cure is worse than the disease; the DISPLAYs (for the same 
data) now show

CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 SECTION 06920 AMOUNT
IS          -5+.
CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 SECTION 06955 AMOUNT 
IS          -4+.

>or better (IMHO)
>  DIFF-Z  Pic+ +++,+++,++9.99.

Changing the 'PIC+' to a simple 'PIC '... again, 'wow', but different.

CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 SECTION 06920 AMOUNT
IS         -59.08
CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 SECTION 06955 AMOUNT 
IS         -40.00

>
>HOWEVER,  there is something else going wrong (I think).

You and me both, B'wana.

>I think there is an 
>actual "+" in the middle of the data.  Is there an "IF NUMERIC" test before the 
>display?

No... but I'll play with it and see.  The original DIFF field is COMP-3 
and the result of a SUBTRACT... GIVING; I just recompiled with LIST and a 
descending into the Temple of Truth ('Kids, Don't Try This At Home!') 
shows this generates

ZAP   520(8,13),568(6,4) 
SP    521(7,13),355(5,3) 
ZAP   576(6,4),522(6,13) 
ZAP   522(6,13),522(6,13)
UNPK  584(11,4),522(6,13)

... and if the data were funny it should S0C7 there.  It'd be a nuisance 
to perform NUMERIC checks on all the fields being used here... but it 
might turn out being less work, all around, than what I'm doing now.

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-02-20T12:40:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9OCnl.213411$9i5.43652@en-nntp-07.dc1.easynews.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <eiBnl.214000$zQ4.101913@en-nntp-02.dc1.easynews.com> <gnmqs2$hpt$1@reader1.panix.com>`

```
Sorry about the Pic+ +, instead of Pic ++ ...

You do want 4 not 3 "+" before the first comma - not that you probably have 
9-digit to the right of the decimal point results.

Does the "40" raise any bells with you?  Any chance that something has gotten a 
"space" in it (e.g. X'40')? (I tried looking at X"59" and X'08' - but they 
aren't very interesting <G>)
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-20T19:17:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnmvjl$jpi$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <eiBnl.214000$zQ4.101913@en-nntp-02.dc1.easynews.com> <gnmqs2$hpt$1@reader1.panix.com> <9OCnl.213411$9i5.43652@en-nntp-07.dc1.easynews.com>`

```
In article <9OCnl.213411$9i5.43652@en-nntp-07.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Sorry about the Pic+ +, instead of Pic ++ ...
>
…[5 more quoted lines elided]…
>aren't very interesting <G>)

Actually... the 40 was a real, genuine 40; I managed to find the records 
that composed it and both contained COMP-3-defined fields with 
X'00(more)2000D', adding up to -40.00.  It is an ugly slog... but hey, it 
is Friday and there's only so much porn-surfing I can do, sometimes I have 
to break it up with work.

Thanks much!

DD
```

#### ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-02-20T12:05:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gjotp415ce9c8i2vnf4387q022d76buera@4ax.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com>`

```
On Fri, 20 Feb 2009 15:21:08 +0000 (UTC), docdwarf@panix.com () wrote:

>
>Platform: Big Blue Mainframe
…[34 more quoted lines elided]…
>SUBTRACT CHECK-TOT02 FROM CHECK-TOT01 GIVING DIFF.

Possible Overflow for either CHECK-TOT01 or CHECK-TOT02 or both?


>IF DIFF NOT = 0
>    DISPLAY 'CROSSFOOT ERROR FOR SSN '
…[43 more quoted lines elided]…
>DD

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"Why is it called lipstick if you can still move your lips?"
-- George Carlin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-20T18:22:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnmsca$gcj$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gjotp415ce9c8i2vnf4387q022d76buera@4ax.com>`

```
In article <gjotp415ce9c8i2vnf4387q022d76buera@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
>On Fri, 20 Feb 2009 15:21:08 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>SUBTRACT CHECK-TOT02 FROM CHECK-TOT01 GIVING DIFF.
>
>Possible Overflow for either CHECK-TOT01 or CHECK-TOT02 or both?

Possible... but *highly* unlikely.  The application is Payroll and 
frequency is bi-weekly; those fields are defined as S9(7)V99 COMP-3 and 
S9(9)V99 COMP-3... and this is not the sort of organisation where 
individuals earn such sums as that.  A run with an ON OVERFLOW DISPLAY 
'!!AIEEE!' yielded nothing.

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-20T18:24:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnmshd$omo$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gjotp415ce9c8i2vnf4387q022d76buera@4ax.com> <gnmsca$gcj$1@reader1.panix.com>`

```
In article <gnmsca$gcj$1@reader1.panix.com>,  <docdwarf@panix.com> wrote:

[snip]

>A run with an ON OVERFLOW DISPLAY 
>'!!AIEEE!' yielded nothing.

Sorry... I coded 'ON SIZE ERROR', not 'ON OVERFLOW'.

DD
```

#### ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-02-20T17:48:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com>`

```
You can only get "Q" and "}" in a USAGE DISPLAY signed numeric var when the 
data are SIGN EBCDIC...

....which occurs of course on EBCDIC machines (which you are on).....

....OR....

When signed (overpunch) display numeric items are transferred (eg FTP) 
between ASCII and EBCDIC machine with some kind of "automatic, you don't 
have to worry about it"  EBCDIC-ASCII conversion (eg when you FTP in ASC 
mode).

While.the numeric digits of such a number are generally converted from ASCII 
to EBCDIC correctly, the overpunch sign character invariably gets screwed 
up.

There should be CHARSET and SIGN compiler directives you can use to deal 
with it  but it's usually easier to just fix 'em yourself with a 
substitution table....

... that is, if you can't get the "transfer process" straightened out by 
following the suggestions I laid out lo these many years ago at:

 http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-23T13:58:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnua1j$j1p$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com>`

```
In article <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>You can only get "Q" and "}" in a USAGE DISPLAY signed numeric var when the 
>data are SIGN EBCDIC...
…[12 more quoted lines elided]…
>up.

Well... given that (according to the first posting) a total of five 
records (out of 77,000+ are throwing 'bad' DISPLAYs and that the data are 
manipulated by a SUBTRACT... GIVING, generating ZAP and AP structures... 
it seems to me, kinda sorta almost, that the transfer method being used (I 
think it is called 'Connect Direct') is not causing the classic 
ASCII-to-ECBDIC 'COMP-3 don't work that way' mess.

This appearance is reinforced by the file of 'good records' being sent to 
a group of Accountants every week... and such folks get notoriously 
fidgety about things like crossfooting... and there's been nary a word 
about problems with the ones that make it across for the past 
year-and-a-half (program last compiled, according to the load module, 
20071127).

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-02-23T08:19:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com> <gnua1j$j1p$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:gnua1j$j1p$1@reader1.panix.com...
> In article <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[15 more quoted lines elided]…
> ASCII-to-ECBDIC 'COMP-3 don't work that way' mess.

I just threw that out there because it is 'a'  cause of similar problems, 
just in case you and I are not the only ones who read this NG.

Don't know about you, but the most I ever expect from a newsgroup when I 
have a problem is "it could be... and here's how you can test if that is the 
case".....  and given that, more things to look at/try can never be a Bad 
Thing.


MCM
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-02-23T08:25:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com>`

```
Oops, forgot...

>>not causing the classic
>> ASCII-to-ECBDIC 'COMP-3 don't work that way' mess

This is NOT about COMP-3 ( 'USAGE BINARY' or 'USAGE PACKED-DECIMAL' 
depending on compiler)...

It is about signed numerics  with USAGE DISPLAY.

MCM


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com...
>
> <docdwarf@panix.com> wrote in message 
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-23T15:02:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnudqs$cqt$3@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com> <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com>`

```
In article <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>Oops, forgot...
>
…[6 more quoted lines elided]…
>It is about signed numerics  with USAGE DISPLAY.

E'en worse... it is about a jumble of signed numerics, compressed data, 
edited numerics and toe of frog... as sources for the DISPLAY statement.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 6)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-02-23T11:15:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vRAol.21897$rb1.2001@newsfe02.iad>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com> <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com> <gnudqs$cqt$3@reader1.panix.com>`

```
I have invariably found that "the problem is somewhere else".  (I'd go so
far as to elevate it to a natural law!)  So whatever logic you THINK is
causing the problem, isn't.

I realize that this is a generalization and therefore of no specific help.
But backing away from the particulars may provide illumination.  Although
you have a nastily complicated problem definition.

Best of luck!

PL

<docdwarf@panix.com> wrote in message news:gnudqs$cqt$3@reader1.panix.com...
> In article <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com>,
> Michael Mattias <mmattias@talsystems.com> wrote:
…[13 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-02-23T14:06:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com> <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad>`

```
tlmfru wrote:
> I have invariably found that "the problem is somewhere else".  (I'd
> go so far as to elevate it to a natural law!)  So whatever logic you
…[5 more quoted lines elided]…
>

Right. There's Heybub's Maxim: "If you look at a problem more than a few 
minutes, the problem is either intractable and beyond human comprehension or 
the problem is trivial."

I've only encountered the first possibility once: my ex-wife.
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-24T00:54:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnvggv$s2i$3@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com>`

```
In article <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>tlmfru wrote:
>> I have invariably found that "the problem is somewhere else".  (I'd
…[10 more quoted lines elided]…
>the problem is trivial."

Someone doesn't seem to remember much mathematics beyond algebra.

>I've only encountered the first possibility once: my ex-wife. 

Have you ever had a dream about hoop-rolling snakes and from that 
generated a whole new theory about how carbon-atoms form compounds?

Never mind the explanation... it'll take more than a few minutes.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-02-24T09:16:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5878q4tglsdonqd9lc7ergob678mvof1hv@4ax.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com> <gnvggv$s2i$3@reader1.panix.com>`

```
On Tue, 24 Feb 2009 00:54:55 +0000 (UTC), docdwarf@panix.com () wrote:

>Someone doesn't seem to remember much mathematics beyond algebra.

For the vast majority of adults, all the math they will use is what us
old timers needed to use slide rules.

Proportion, significant digits, estimating - that's it. Unfortunately,
these skills are very lacking - even laws are passed which are based
upon such failures.
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 10)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-02-25T11:36:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com> <gnvggv$s2i$3@reader1.panix.com> <5878q4tglsdonqd9lc7ergob678mvof1hv@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 24 Feb 2009 00:54:55 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
> upon such failures.

Especially reporters. Statements like "Eighty percent of drivers, however, 
cannot be 'above average'..."
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-02-25T10:54:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ob1bq4pcdnh1e4l60bf09p9ntogeuj5m31@4ax.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com> <gnvggv$s2i$3@reader1.panix.com> <5878q4tglsdonqd9lc7ergob678mvof1hv@4ax.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com>`

```
On Wed, 25 Feb 2009 11:36:57 -0600, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>> Proportion, significant digits, estimating - that's it. Unfortunately,
>> these skills are very lacking - even laws are passed which are based
…[3 more quoted lines elided]…
>cannot be 'above average'..." 

But we can have 80% of incomes "below average", depending on which
definition of "average" we are using.
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 11)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-02-25T14:27:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GQhpl.18638$c45.4295@nlpi065.nbdc.sbc.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com> <gnvggv$s2i$3@reader1.panix.com> <5878q4tglsdonqd9lc7ergob678mvof1hv@4ax.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com...
> Especially reporters. Statements like "Eighty percent of drivers, however, 
> cannot be 'above average'..."

Why not?  In Lake Wobegon, all the children are above average.

MCM
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 12)_

- **From:** jnjsle1@optonline.net
- **Date:** 2009-02-25T15:30:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com> <gnvggv$s2i$3@reader1.panix.com> <5878q4tglsdonqd9lc7ergob678mvof1hv@4ax.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com> <GQhpl.18638$c45.4295@nlpi065.nbdc.sbc.com>`

```
On Feb 25, 3:27 pm, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> "HeyBub" <hey...@NOSPAMgmail.com> wrote in message
>
> news:bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com...


Doc,

Have you looked at the data in the DIFF variable before the display?
Or just redefine it as a PIC X(06) and display that variable.

Use hex on when viewing the sysout to determine if it's a tue comp-3
field.
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-26T13:11:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<go64eg$4l5$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com> <GQhpl.18638$c45.4295@nlpi065.nbdc.sbc.com> <71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com>`

```
In article <71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com>,
 <jnjsle1@optonline.net> wrote:
>On Feb 25, 3:27?pm, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>> "HeyBub" <hey...@NOSPAMgmail.com> wrote in message
…[10 more quoted lines elided]…
>field.

Thanks much for the suggestion... but if you recall the DIFF variable 
contains data which are the result of a series of ADD... GIVING and 
SUBTRACT... GIVING statements.  The compiler/OS/version (IBM Enterprise 
COBOL for z/OS 3.4.1) I am using generates the Assembley statements (using 
the PMAP... errrrr, LIST option) various xP operations (ZAP, AP, SP, etc) 
and these are, in my experience, *exquisitely* sensitive to the 'purity' 
of COMP-3 (packed-decimal) data.

COMP (binary) is another story, entire... many's the time I've had to 
point out that MOVE SPACES TO ENTIRE-REC will put a value of x'4040404040' 
into a COMP field... but COMP-3 is a bit more stringent in its 
requirements.

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 14)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-02-26T09:22:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ysypl.23588$ZP4.13309@nlpi067.nbdc.sbc.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com> <GQhpl.18638$c45.4295@nlpi065.nbdc.sbc.com> <71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com> <go64eg$4l5$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:go64eg$4l5$1@reader1.panix.com...
>
> Thanks much for the suggestion... but if you recall the DIFF variable
…[5 more quoted lines elided]…
> of COMP-3 (packed-decimal) data.

This may sound like grasping at straws, but you could try changing from ADD 
or SUBTRACT  to COMPUTE and/or using the COBOL functions which will provide 
the SUM of table elements.

I never had a problem with ADD, but I do remember some kind of similar 
problem I had with SUBTRACT which was solved by COMPUTEing instead.

MCM
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-26T16:09:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<go6ese$fil$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com> <go64eg$4l5$1@reader1.panix.com> <Ysypl.23588$ZP4.13309@nlpi067.nbdc.sbc.com>`

```
In article <Ysypl.23588$ZP4.13309@nlpi067.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:

[snip]

>I never had a problem with ADD, but I do remember some kind of similar 
>problem I had with SUBTRACT which was solved by COMPUTEing instead.

As was mentioned... the problem I was diddling with put out a DISPLAY that 
went to a SYSOUT dataset which was later read by a different program which 
relied on the numbers being in that whacky format... so fixing one thing 
would cause something downstream to break.  I've sung that song often 
enough that I can do harmony on it... no need to start vocalising now.

As for COMPUTE versus ADD/SUBTRACT/etc... I've looked through a few ASM 
lists and haven't been able to see a difference in generated code for the 
statements.  If there's an example you think might bear further research 
I'd be glad to give it the proverbial whack.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 14)_

- **From:** jnjsle1@optonline.net
- **Date:** 2009-02-28T08:51:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a3b8562-5a5c-4412-b732-e866fe193cf2@41g2000yqf.googlegroups.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <bN2dnWF7T9AkHDjUnZ2dnUVZ_g2WnZ2d@earthlink.com> <GQhpl.18638$c45.4295@nlpi065.nbdc.sbc.com> <71dc7bea-0111-4b3e-a94d-8e4c4f971316@q30g2000vbn.googlegroups.com> <go64eg$4l5$1@reader1.panix.com>`

```
On Feb 26, 8:11 am, docdw...@panix.com () wrote:
> In article <71dc7bea-0111-4b3e-a94d-8e4c4f971...@q30g2000vbn.googlegroups.com>,
>
…[29 more quoted lines elided]…
> DD

Doc,

The + shouldn't appear in a display of a COMM-3 field (does a - appear
for neg #s?).
Something's going on between the calc of the field and its display.
That's why I suggested displaying the native content of the DIFF field
immediately before the display showing the questionable data.

If the data displayed is valid COMP-3, either DISPLAY is
malfunctioning or someone modified the VERB code or special print char
settings are being used or it's enemy action.
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 8)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-02-23T22:04:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jAKol.23368$aZ3.5383@newsfe01.iad>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com> <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad> <svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com>`

```
Beauty!  Let's compile a list of maxims!  I have several: one of which is
"there are no programmer groupies".

PL

HeyBub <heybub@NOSPAMgmail.com> wrote in message
news:svSdnSp-p554nD7UnZ2dnUVZ_oWWnZ2d@earthlink.com...
> tlmfru wrote:
> > I have invariably found that "the problem is somewhere else".  (I'd
…[9 more quoted lines elided]…
> minutes, the problem is either intractable and beyond human comprehension
or
> the problem is trivial."
>
> I've only encountered the first possibility once: my ex-wife.
>
>
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-24T00:51:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnvgae$s2i$2@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <xgyol.12683$8_3.4636@flpi147.ffdc.sbc.com> <gnudqs$cqt$3@reader1.panix.com> <vRAol.21897$rb1.2001@newsfe02.iad>`

```
In article <vRAol.21897$rb1.2001@newsfe02.iad>, tlmfru <lacey@mts.net> wrote:
>I have invariably found that "the problem is somewhere else".  (I'd go so
>far as to elevate it to a natural law!)  So whatever logic you THINK is
…[4 more quoted lines elided]…
>you have a nastily complicated problem definition.

E'en better... I managed to solve the problem and then found out that the 
solution caused another part of the jobstream (which depended on the 'bad 
format' and forced a '+' sign in what I thought were later DISPLAYs) to 
break.

No, you *don't* want to know.

>
>Best of luck!

Thanks much.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-23T15:01:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnudo1$cqt$2@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com> <gnua1j$j1p$1@reader1.panix.com> <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com>`

```
In article <Ebyol.12681$8_3.1952@flpi147.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
>
><docdwarf@panix.com> wrote in message news:gnua1j$j1p$1@reader1.panix.com...

[snip]

>> Well... given that (according to the first posting) a total of five
>> records (out of 77,000+ are throwing 'bad' DISPLAYs and that the data are
…[6 more quoted lines elided]…
>just in case you and I are not the only ones who read this NG.

Oh, a 'for the newbies', eh?  Well... what happens when the Space Aliens 
who are monitoring this group catch on... and begin to corrupt all our 
batch payroll systems?

(ans: 'Nobody will be able to tell the difference anyhow!')

Thanks much... still slogging.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-02-23T12:27:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0u5q4dj6a76phfs6el2nbl15ep9k0bj9i@4ax.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com> <gnua1j$j1p$1@reader1.panix.com>`

```
About 30 years ago, the shop I was working with moved from mainframe
IBM DOS to mainframe IBM OS.    We changed some programs to move
numbers from signed to unsigned numbers and back again before
comparing old data with new.   

Did all of your data come from the same place?  
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-24T01:08:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnvh9f$r2p$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <UoHnl.11029$hc1.1835@flpi150.ffdc.sbc.com> <gnua1j$j1p$1@reader1.panix.com> <c0u5q4dj6a76phfs6el2nbl15ep9k0bj9i@4ax.com>`

```
In article <c0u5q4dj6a76phfs6el2nbl15ep9k0bj9i@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>About 30 years ago, the shop I was working with moved from mainframe
>IBM DOS to mainframe IBM OS.    We changed some programs to move
…[3 more quoted lines elided]…
>Did all of your data come from the same place?  

They did... but what they went through, and were then expected to go 
through, are a bit sticky.

Let me give an example: the front-end system allows an employee to enter a 
sum under Undifferentiated Intoxication Fees (to cover alcohol and, where 
legal without a prescription, Elixer of Terpin Hydrate) and a different 
sum under Undifferentiated Altered States Fees (to cover sexual asphyxia 
and, where legal, small containers of nitrous oxide).  The old back-end 
would then maintain these figures as separate.

The new back-end - online, now, for a mere four years - combines these two 
categories under some obscure Federal Law as Undifferentiated Intoxication 
and Altered States Fees.  The folks at the Help Desk still get calls from 
employees saying that they do not understand why their nitrous oxide 
reimbursement is not showing up in what used to be the Undifferentiated 
Altered States Fees... and what's this about Intoxication?

DD
```

#### ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-02-20T22:01:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-oidnUXzma0W8wLUnZ2dnUVZ_iyWnZ2d@earthlink.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com>`

```
Doc,

0000000590Q+     If DIFF is S9(9)V99  and Q = X'D8'  then this looks like 
minus 00000005908 followed by a plus sign.  What answer are you expecting? 
Where is the plus sign coming from?  If the plus sign is part of the number 
then DIFF must not be S9(9)V99.  X'00000000000000F5F9F0D84E' isn't what I 
would normally expect to see displayed and it won't fit in a S9(9)V99 field 
when packed.   Can you put a routine in to display the hexadecimal values of 
the two numbers and the difference?  I think that if you do that the answer 
will jump out at you and you can use it to check if any other processing is 
somehow corrupting DIFF. What NUMPROC option are you using? You could try 
using a separate DISPLAY to show DIFF.  I assume the total length of the 
output string is not greater that the maximum allowed?

Likewise 0000000400}+    looks like minus 00000004000 followed by a plus 
sign.

Have you tried SIGN LEADING SEPARATE or SIGN TRAILING SEPARATE?

What does working storage look like where this fields are defined i.e. what 
other fields precede/follow them?  It looks like somhow the rightmost two 
bytes are getting corrupted.  Try to think about how this might be possible.

From a later post you said:   X'00(more)2000D', adding up to -40.00  But 
that is not -40.00 it is -20.00  Again what answer are you expecting?

A later post said this is payroll related.  Have you checked that the two 
numbers being subtracted are both positive or zero?  I assume no one gets 
paid a negative amount.

Again from a later post:

Changing the 'PIC+' to a simple 'PIC '... again, 'wow', but different.

                    CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 
SECTION 06920 AMOUNT
                    IS         -59.08
                    CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 
SECTION 06955 AMOUNT
                    IS         -40.00

This looks to me like it could be the right answer.  Since you must think it 
is not the right answer, What is the answer you are expecting?


<docdwarf@panix.com> wrote in message news:gnmhp4$95$1@reader1.panix.com...
>
> Platform: Big Blue Mainframe
…[81 more quoted lines elided]…
>
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-02-23T14:58:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gnudin$cqt$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <-oidnUXzma0W8wLUnZ2dnUVZ_iyWnZ2d@earthlink.com>`

```
In article <-oidnUXzma0W8wLUnZ2dnUVZ_iyWnZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>Doc,
>
>0000000590Q+     If DIFF is S9(9)V99  and Q = X'D8'  then this looks like 
>minus 00000005908 followed by a plus sign.  What answer are you expecting? 

I have no expectations for what is to happen when one DISPLAYs a field 
defined as S9(9)V99 COMP-3... so I'm trying different stuff.

>Where is the plus sign coming from?

The JES SYSOUT.  All I did was copy-n-paste.

>If the plus sign is part of the number 
>then DIFF must not be S9(9)V99.

DIFF is not S9(9)V99.  As you quoted below, from my original presentation 
of the matter, '(cursory examination of fields, including DIFF, show 
them as some kind of S9(n)V99 COMP-3.)

>X'00000000000000F5F9F0D84E' isn't what I 
>would normally expect to see displayed and it won't fit in a S9(9)V99 field 
>when packed.

As was pointed out in another posting, DIFF is the result of a SUBTRACT... 
GIVING, which compiles to ZAP and SP (among other statements); these 
usually exhibit unruly behavior when non-numeric data are present.

>Can you put a routine in to display the hexadecimal values of 
>the two numbers and the difference?  I think that if you do that the answer 
>will jump out at you and you can use it to check if any other processing is 
>somehow corrupting DIFF.

Maybe I'm spending more time avoiding the work (putting in such a hexval 
display) than the actual work would take; I used a spare PIC  
$ZZZ,ZZZ,ZZZ,ZZ9.99- and coded:

MOVE CHECK-TOT01 TO WS-DISP-NUMED-FLD.
DISPLAY ' !! CHECK-TOT01 = ', WS-DISP-NUMED-FLD
MOVE CHECK-TOT02 TO WS-DISP-NUMED-FLD.
DISPLAY ' !! CHECK-TOT02 = ', WS-DISP-NUMED-FLD

SUBTRACT CHECK-TOT02 FROM CHECK-TOT01 GIVING DIFF

...and I got

!! CHECK-TOT01 = $            751.15
!! CHECK-TOT02 = $            810.23
... AMOUNT IS 0000000590Q+ <== this is a DISPLAY of DIFF, S9(9)V99 COMP-3

... and the actual result should be -59.08.  'Q' is x'D8', a reversal of 
X'8D' and that's what I'd expect to find at the end of an S9(9)V99 COMP-3 
field which contained X'00...05908D'.

Where the '+' sign comes from I have no idea.

>What NUMPROC option are you using?

NUMPROC(MIG)

>You could try 
>using a separate DISPLAY to show DIFF.  I assume the total length of the 
>output string is not greater that the maximum allowed?

That assumption is correct... as noted, this is a Payroll application; 
with all the various bonuses, supplements, addenda and payments for 
Miscellaneous Graft and Corruption I severely doubt that anyone in this 
particular organisation is pulling in more than US$5,000,000/wk... we 
ain't Hollywood.

[snip]

>From a later post you said:   X'00(more)2000D', adding up to -40.00  But 
>that is not -40.00 it is -20.00

That posting said, I believe, that there were *two* recs 
containining X'00(more)2000D', adding up to -40.00

>Again what answer are you expecting?

I was expecting X'200D' + X'200D' to add up to X'400D' and to be displayed 
as '-40.00' under the other conditions given... and I was almost right, 
too.

>
>A later post said this is payroll related.  Have you checked that the two 
>numbers being subtracted are both positive or zero?  I assume no one gets 
>paid a negative amount.

See above.  CHECK-TOT01 and CHECK-TOT02 are the results of adding together 
a bunch of S9(n)V99 and yes, in payroll, deductions can be treated as 
negative additions.

Thanks much... still slogging.

DD
```

#### ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** Lew Pitcher <lpitcher@teksavvy.com>
- **Date:** 2009-05-25T18:11:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free>`
- **References:** `<gnmhp4$95$1@reader1.panix.com>`

```
On February 20, 2009 10:21, in comp.lang.cobol, docdwarf@panix.com
(docdwarf@panix.com) wrote:

> 
> Platform: Big Blue Mainframe
…[53 more quoted lines elided]…
> IS 0000000400}+

Short answer:
  Your DISPLAY is erroneously unpacking the COMP-3 sign nybble into a
  character. To fix, move your USAGE IS COMP-3 field to a USAGE IS DISPLAY
  field, and then DISPLAY /that/ field/

Longer explanation:
  In IBM BCD ("PACKED DECIMAL" or "COMP-3") math, values are stored as a
  series of decimal nybbles, followed by a single nybble indicating the sign
  of the value. 0XA, 0XC, and 0XE are negative signs, while 0XB, 0XD, and
  0XF are positive signs. 

  The IBM COBOL "DISPLAY" verb does not properly UNPACK these PACKED DECIMAL
  values. It works for positive input values where the sign nybble is 0xF,
  but fails for other positive values, and any negative value. This is a
  well-known problem; many mainframe programmers have coded around it.

  To use the standard code-around (at least, the one /I/ learned), add
    77  UNPACKED-NUMBER         PIC Z(9)9 USAGE IS DISPLAY.
  to your WORKING-STORAGE, and then change your IF LOGIC TO
        IF DIFF NOT = 0
           MOVE DIFF TO UNPACKED-NUMBER
           DISPLAY 'CROSSFOOT ERROR FOR SSN '
              SOC-SEC-NO
              ' ACCOUNTING NO '
              ACCTNG-NO
              ' SECTION '
              SECTION-NO
              ' AMOUNT IS '
              UNPACKED-NUMBER.

HTH
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-25T17:47:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MdFSl.19295$Tp1.4375@en-nntp-01.dc1.easynews.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free>`

```
Your explanation is correct (sort-of).  You state,

"  The IBM COBOL "DISPLAY" verb does not properly UNPACK these PACKED DECIMAL 
values."

as *IF* the DISPLAY statement is SUPPOSED to unpack the byte with the 
sign-nibble.  Nothing in the ANSI/ISO COBOL Standard requires this (even when 
USAGE PACED-DECIMAL is used rather than COMP-3), this is not conforming and 
defined behavior.

Furthermore, there is nothing in the current (or past) IBM documentation that 
would even HINT that the DISPLAY statement will unpack the final byte.

The simple fact is that what is happening is "well known" and even RELIED upon 
behavior for IBM compilers and the DISPLAY statement - for as leas as long as I 
have known of IBM COBOL.

It is correct, that if you want to see a sign, then you should move this to a 
USAGE DISPLAY field (preferably numeric-edited) and the OP would be happier. 
If, however, you know and understand how the IBM DISPLAY statement works, then 
code (and review your output) accordingly.
```

##### ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-29T16:12:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvp1he$9n3$1@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free>`

```
In article <31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free>,
Lew Pitcher  <lew.pitcher@digitalfreehold.ca> wrote:
>On February 20, 2009 10:21, in comp.lang.cobol, docdwarf@panix.com
>(docdwarf@panix.com) wrote:
…[5 more quoted lines elided]…
>> Well... here's a simple one that everyone can join in on!

[snip]

>> CROSSFOOT ERROR FOR SSN 999999998 ACCOUTING NO 9J53 SECTION 06920 AMOUNT
>> IS 0000000590Q+
>> CROSSFOOT ERROR FOR SSN 999999997 ACCOUTING NO 9J63 SECTION 06955 AMOUNT
>> IS 0000000400}+

>Short answer:
>  Your DISPLAY is erroneously unpacking the COMP-3 sign nybble into a
>  character.

Shorter answer... the fields I was giving were final results from a 
separate program to which intermediate results were being passed... *and* 
this final program forced a +-sign to the end of the number.

In other words... that which was being erroneously unpacked was then being 
further manipulated to show an unnecessary (and, at times, incorrect) 
+-sign.

> To fix, move your USAGE IS COMP-3 field to a USAGE IS DISPLAY
>  field, and then DISPLAY /that/ field/

You mean something like WS-DISP-NUM PIC 99999999.99 SIGN TRAILING?  Did 
that... and things went KERFLOOIE because the second program was relying 
on there being 'bad data' to fix with a forced +-sign.

In other words... not one series of ADDS and MOVES in one program needed 
to be manipulated, two series in two programs... and a few ABENDS later I 
coded a DFSORT to handle the whole mess.  This wasn't for the user - 'The 
program's been doing this since Babbage wrote it, I can live with it' - 
but because I wanted to see what was going on.

It got solved long enough ago that I no longer need sedatives... and the 
nightmares have decreased to a tolerable level.

Thanks much for your time, Mr Pitcher; it is greatly appreciated and I 
hope to be able to return the favo(u)r.

DD
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

- **From:** Lew Pitcher <lpitcher@teksavvy.com>
- **Date:** 2009-05-29T12:20:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1708$4a200b4d$4c0aa020$29873@TEKSAVVY.COM-Free>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free> <gvp1he$9n3$1@reader1.panix.com>`

```
On May 29, 2009 12:12, in comp.lang.cobol, docdwarf@panix.com
(docdwarf@panix.com) wrote:
[snip]
> Thanks much for your time, Mr Pitcher; it is greatly appreciated and I
> hope to be able to return the favo(u)r.

You are most welcome for what little help I gave :-)

Since I'm now retired (after 30+ years in the business), and no longer
actively coding COBOL, it may take some time before there is an opportunity
for you to return the favo(u)r. But, I appreciate the offer.

Luck be with you
```

###### ↳ ↳ ↳ Re: DISPLAY Statement Throwing Trash No Matter What

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-29T16:33:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvp2nu$9n3$2@reader1.panix.com>`
- **References:** `<gnmhp4$95$1@reader1.panix.com> <31697$4a1b1776$4c0aa020$17651@TEKSAVVY.COM-Free> <gvp1he$9n3$1@reader1.panix.com> <e1708$4a200b4d$4c0aa020$29873@TEKSAVVY.COM-Free>`

```
In article <e1708$4a200b4d$4c0aa020$29873@TEKSAVVY.COM-Free>,
Lew Pitcher  <lew.pitcher@digitalfreehold.ca> wrote:
>On May 29, 2009 12:12, in comp.lang.cobol, docdwarf@panix.com
>(docdwarf@panix.com) wrote:
…[8 more quoted lines elided]…
>for you to return the favo(u)r. But, I appreciate the offer.

Oh boy... you mean I got to make a decent, kind, open and generous offer 
that has a snowball's chance of ever getting taken up!  All the form and 
none of the substance... maybe I'll make it to Management yet!

>
>Luck be with you

I think it was Shaw who said 'Each man makes his own luck'... then again, 
how that applies to the fellow walking across the street, traffic light in 
his favor, who is then struck by a drunken driver I'm not quite sure.

Hope for luck in one hand, spit in the other and see which fills up... 
sorry, have to stop now, my keyboard's getting soggy.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
