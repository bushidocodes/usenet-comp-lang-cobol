[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BMS Attributes - by bit...

_5 messages · 4 participants · 2000-09_

---

### BMS Attributes - by bit...

- **From:** Ethan Schultz <ethans@RosebudUSA.com>
- **Date:** 2000-09-05T20:20:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B58DC1.502D8FA2@RosebudUSA.com>`

```
Hi,

does anyone have a breakdown of the bits used for
IBM's BMS ?   I don't need the extended attributes,
just need to know which one's are used for FSET,
PROT/UNPROT, BRT, etc...

Thanks !

Ethan Schultz
Rosebud Mgt Systems
ethans@rosebudusa.com
```

#### ↳ Re: BMS Attributes - by bit...

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-09-06T04:46:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B5CC12.3B0FC6C8@worldnet.att.net>`
- **References:** `<39B58DC1.502D8FA2@RosebudUSA.com>`

```
Ethan Schultz wrote:
> 
> Hi,
…[4 more quoted lines elided]…
> PROT/UNPROT, BRT, etc...

Why not check IBM's site or BookManager? I had the 3270 "green card"
years ago, but it's long since disappeared into documentation heaven.

Bill Lynch
```

##### ↳ ↳ Re: BMS Attributes - by bit...

- **From:** Ethan Schultz <ethans@RosebudUSA.com>
- **Date:** 2000-09-06T07:46:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B62E9C.4D3961D5@RosebudUSA.com>`
- **References:** `<39B58DC1.502D8FA2@RosebudUSA.com> <39B5CC12.3B0FC6C8@worldnet.att.net>`

```
That's an idea...   unfortunately bookmgr (on the web)
didn't have it - and poking through 1000's of page of
support 'tips' on IBM.COM isn't my idea of fun !

I wrote a little pgm to do the byte <> bit conversion
and show me the bits for 'known' attribute values.

I was then able to 'sort out' the translation table myself,
as well as find a 'problem' or two with a few defined
values for attributes that've been coded over the years !


Thanks



William Lynch wrote:

> Ethan Schultz wrote:
> >
…[10 more quoted lines elided]…
> Bill Lynch
```

###### ↳ ↳ ↳ Re: BMS Attributes - by bit...

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-06T11:58:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2AAF5E17A14E72B.28959EFDA3B812E2.45DEB3E851174DB1@lp.airnews.net>`
- **References:** `<39B58DC1.502D8FA2@RosebudUSA.com> <39B5CC12.3B0FC6C8@worldnet.att.net> <39B62E9C.4D3961D5@RosebudUSA.com>`

```
On Wed, 06 Sep 2000 07:46:36 -0400, Ethan Schultz
<ethans@RosebudUSA.com> enlightened us:

>That's an idea...   unfortunately bookmgr (on the web)
>didn't have it - and poking through 1000's of page of
…[30 more quoted lines elided]…
>

Here's the breakdown:

First, visualize a byte as:

X  1  U/P  A/N  D/SPD  Reserved  MDT
0   1    2      3       4  5           6            7

Where the top row is the usage and the bottom row is the bit position
left to right.  The postions are further explained as:

0 = Value determined by contents of bit 2-7

1 = Always a 1

2 = If 0, then Unprotected
      If 1, then Protected

3 = If 0, then Alphameric
      If 1, then Numeric

     Note:  Bits 2 and 3 equal to 11 causes an automatic skip

4 & 5 = If 00, then display/not selector pen detectable
            If 01, then display/selector pen detectable
            If 10, then intensified display/selector pen detectable
            If 11, then Non-display, non-print, non-detectable

6 = Reserved.  Must always be 0

7 = Modified Data Tag:  
      0 = Field has not been modified
      1 = Field has been modified

More notes:  Bits 0 and 1 are not decoded when received by the display
unit (3270).  When transfereing characters to the mainframe (CPU) bit
1 is a 1 and bit 0 is set depending upon the character being
transfered.  All attribute characters are part of the defined
character set.  The default option (bits 2 through 7 all set to 0)
results in an unprotected alphameric, displayed, non detectable field.

Examples:

Unprotected, alphameric, high intensity, detectable, MDT off:

bits 2-7 = 00 1000 (EBCD C8, ASCII 48, Character H)

Protected,  high intensity, detectable, MDT on:

bits 2-7 = 10 1001 (EBCD E9, ASCII 5A, Character Z) 

If you need to know about underlining, blinking etc.  post here and
I'll pass that along.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-

Today's tip for annoying co-workers:
Ask people what gender they are.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

#### ↳ Re: BMS Attributes - by bit...

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-09-06T23:26:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p6jqd$puk$1@nnrp1.deja.com>`
- **References:** `<39B58DC1.502D8FA2@RosebudUSA.com>`

```
In article <39B58DC1.502D8FA2@RosebudUSA.com>,
  ethans@RosebudUSA.com wrote:
> Hi,
>
…[11 more quoted lines elided]…
>

Go to your CICS copylib (for example, it might be called
CICS410.SDFHMAC) and browse member DFHBMSCA. If you can't find it,
write a quick and dirty CICS/COBOL program, copying in DFHBMSCA into WS.

Then, using your handy-dandy PC calculator in scientific mode (or a
hand held calculator if you wish) enter each BMS attribute byte (in
hex) from DFHBMSCA and switch the result mode to BINARY.

I think this will be much easier and you'll be using IBM's definitions.

HTH....

Cheers,

Bill


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
