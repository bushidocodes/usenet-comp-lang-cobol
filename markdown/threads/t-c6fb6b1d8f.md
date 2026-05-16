[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL (zOS) and Unicode

_9 messages · 8 participants · 2005-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL (zOS) and Unicode

- **From:** "Bertram" <bfj.geiger@tiscali.de>
- **Date:** 2005-02-03T11:39:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
Is there a possibility to convert the e.g. html-notation of unicode like 
&#12345; to a "normal" cobol structure like PIC N(...) and can COBOL convert 
it back?

Whow does COBOL store data in PIC N if the unicode needs more than 2 bytes?
```

#### ↳ Re: COBOL (zOS) and Unicode

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-02-03T10:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Q9q71beflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
.    On  03.02.05
  wrote  bfj.geiger@tiscali.de (Bertram)
     on  /COMP/LANG/COBOL
     in  ctsv2d$1il0$1@ulysses.news.tiscali.de
  about  COBOL (zOS) and Unicode


bg> Whow does COBOL store data in PIC N if the unicode needs more than 2
bg> bytes?

   Unicode normally is represented in 32 bits, but there are  
transformation functions to represent it in 16 bits (UTF-16) and 8  
bits (UTF-8), even 7 bits (UTF-7).

   I would think that your compiler can be directed to use the one or  
the other.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er kann die Tinte nicht halten, und wenn es ihm ankommt, jemand zu besudeln, so besudelt er sich gemeiniglich am meisten. -G.C.Lichtenberg
```

#### ↳ Re: COBOL (zOS) and Unicode

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-02-03T07:30:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZHpMd.40934$8j3.22848@fe40.usenetserver.com>`
- **In-Reply-To:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
Bertram wrote:
> Is there a possibility to convert the e.g. html-notation of unicode like 
> &#12345; to a "normal" cobol structure like PIC N(...) and can COBOL convert 
> it back?

You can look at Function Char - strip off the &#, and it'll give you the 
character.  I'm not sure how high up those codes go, though, and whether 
it only supports ASCII output, or Unicode.  It would be where I would 
start, though.  :)
```

##### ↳ ↳ Re: COBOL (zOS) and Unicode

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2005-02-03T20:38:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20050203153821.14317.00000361@mb-m10.aol.com>`
- **References:** `<ZHpMd.40934$8j3.22848@fe40.usenetserver.com>`

```
LX-i lxi0007 writes ...

>Bertram wrote:
>> Is there a possibility to convert the e.g. html-notation of unicode like 
>> &#12345; to a "normal" cobol structure like PIC N(...) and can COBOL
>convert 
>> it back?

Hmm. Strange, I can't seem to find the original
post in this thread.

>
>You can look at Function Char - strip off the &#, and it'll give you the 
…[3 more quoted lines elided]…
>

Enterprise COBOL on z/OS supports the National
data type, which is also called UTF-16. The intrinsic
functions NATIONAL-OF and DISPLAY-OF convert
between classic DISPLAY (EBCDIC) characters 
and Unicode characters. The intrinsic functions
CHAR and ORD can convert between character
values and integer values but only between 1
and 256.

If your notation is encountered in XML, however,
the XML-PARSE statement might be able to help
you.

Be aware that Unicode can be encoded in three
formats:

UTF-32 - 4 bytes per character
UTF-16 - 2 bytes per character, except some
               values use 2 2-byte characters
               (called surrogate characters),
              which is how Unicode can support
              more than 64K characters
UTF-8 - 1, or 2, or 3, or 4 bytes per character

Enterprise COBOL supports UTF-16 (except for
surrogate pairs) and UTF-8 (to some degree).

<ad>
For details and hands-on practice, consider our one-day course "Enterprise
COBOL Update II: Unicode and XML Support".

Course description here:
http://www.trainersfriend.com/COBOL_Courses/d705descr.htm

which contains a link to the detailed topical outline.
</ad>

Kind regards,



-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: COBOL (zOS) and Unicode

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-02-03T09:04:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C87094.09040103022005@knology.usenetserver.com>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
In article <ctsv2d$1il0$1@ulysses.news.tiscali.de>,
 "Bertram" <bfj.geiger@tiscali.de> wrote:

> Is there a possibility to convert the e.g. html-notation of unicode like 
> &#12345; to a "normal" cobol structure like PIC N(...) and can COBOL convert 
> it back?
> 
> Whow does COBOL store data in PIC N if the unicode needs more than 2 bytes?

You might want to look at the new TRANSLATE instructions.  There is a 
translate-two-to-one that would let you convert a string of hex digits 
into a string of the same byte values.

But you would need a bit of assembler to pull it off.
```

##### ↳ ↳ Re: COBOL (zOS) and Unicode

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2005-02-03T15:34:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36fcqfF51citnU1@uni-berlin.de>`
- **In-Reply-To:** `<joe_zitzelberger-C87094.09040103022005@knology.usenetserver.com>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de> <joe_zitzelberger-C87094.09040103022005@knology.usenetserver.com>`

```
Top posted with nothing in the attached message.

Unicode is UTF-16 which is a proper subset of ISO-10646 which can be 1, 
2, or 4 bytes IIRC.  I don't' think HTML notation is Unicode although 
the character set used to express the notation may be Unicode where each 
character in &#12345 is 16 bytes for a total of 112 bytes.
Joe Zitzelberger wrote:

> In article <ctsv2d$1il0$1@ulysses.news.tiscali.de>,
>  "Bertram" <bfj.geiger@tiscali.de> wrote:
…[14 more quoted lines elided]…
>
```

#### ↳ Re: COBOL (zOS) and Unicode

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-03T20:34:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KVvMd.990947$f47.169520@news.easynews.com>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
The NSYNBMOL compiler option impacts whether or not PIC N data (without a USAGE 
clause) is treated as
  - "traditional" IBM DBCS
     or
  - UTF-16 (Unicode / ISO-10646)

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/2.4.32

the NATIONAL-OF and DISPLAY-OF functions convert PIC N to X and vice versa (with 
an optional CCSID specification).  See:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR20/7.1.20
    and
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR20/7.1.36

    and some example code at:
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/1.7.3.5

NOTE WELL:
  The IBM DISPLAY-OF function is NOT conforming to the definition provided in 
the '02 ANSI/ISO Standard - as it doesn't provide the optional "default" bad 
conversion character.
```

#### ↳ Re: COBOL (zOS) and Unicode

- **From:** "Schroeder" <jfriedman@nc.rr.com>
- **Date:** 2005-02-04T19:32:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35QMd.54381$dt3.5196509@twister.southeast.rr.com>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de>`

```
This topic came up in conversation with a friend of mine recently as well. I 
think the confusion is that some Unicode characters require more than a 
single UTF-8 or UTF-16 character position to hold them (when converting from 
UTF-32 down to UTF-16 or UTF-8). So if you have a PIC N(1) field in COBOL, 
if that is supposed to hold a national character, clearly there are some 
characters that won't fit.

My understanding is that COBOL gets around this by letting the implementor 
define whether UTF-16 or UTF-8 is being used and as such only characters 
which fit in a single character position would ever be supported by that 
implementation. I don't think the 02 Standard allowed for UTF-32 as a native 
implementation (I would have to dig it up to check). So within a purely 
COBOL world, there shouldn't be a problem as no offending characters (in 
theory) could ever get in.

But I think this user brings up a potential problem when reading XML or some 
other data which potentially includes national characters which might 
require multiple character positions to represent one glyph. If you MOVE 
such a character to a PIC N field, it might not fit.

I don't remember if the 02 Standard has some sort of exception condition 
defined for that case, but if not there probably should be. What do you 
think?



Jeff Friedman



"Bertram" <bfj.geiger@tiscali.de> wrote in message 
news:ctsv2d$1il0$1@ulysses.news.tiscali.de...
> Is there a possibility to convert the e.g. html-notation of unicode like 
> &#12345; to a "normal" cobol structure like PIC N(...) and can COBOL 
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL (zOS) and Unicode

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-04T22:21:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gzSMd.834092$B07.117707@news.easynews.com>`
- **References:** `<ctsv2d$1il0$1@ulysses.news.tiscali.de> <35QMd.54381$dt3.5196509@twister.southeast.rr.com>`

```
z/OS (Enterprise COBOL) versus ANSI/ISO 2002 COBOL are quite different issues. 
(Enterprise COBOL does NOT claim to support '02 "internationalization" 
features - and in fact its DISPLAY-OF feature is incompatile with the '02 
Standard - which defines a different 2nd argument).

The '02 Standard is ABSOLUTELY clear that "USAGE NATIONAL" (and the 
implementor's "native national character set) *may* be ISO-10646 (or Unicode) 
but NEED NOT be.  If it is Unicode and/or 10646, then it may be any UTF format.

Enterprise COBOL *does* claim to support UTF-16 but I can find no evidence that 
it supports UTF-8.  It *does* support the previous IBM DBCS format which is 
"similar" to UTF-8 - but is certainly NOT identical.

I *beleive* that the current Entprrise COBOL supports both
  PIC N Usage Display-1
     and
  PIC N Usage National

within the same program  and would allow "MOVE" statements between the 2.  I 
*know* that it supports multiple CCSID values in both the CODEPAGE compiler 
option and the DIDSPLAY_OF and NATIONAL-OF intrinsic functions.

Finally, the SPECIAL-NAMES paragraph in the '02 Standard (see page 175) supports

    LOCALE [ locale-name-2 ]
    NATIVE
    UCS-4
    UTF-8
    UTF-16
    code-name-2

Therefore, I beleive (but won't swear to it) that all of those character 
repertories can be (semi-) supported within the same '02 conforming program 
(depending upon "processor dependent" implementations).  Other than "LOCALE" - I 
do *not* think this impacts the meaning of PIC N data items.  Page 317 of the 
'02 Standard states,

"Each symbol 'N' represents a national character position that shall contain a 
character from the computer's national character set".

I *beleive* the '02 Standard is written "assuming" (requiring?) a SINGLE 
"computer's national character set" (which may be UTF/UCS- ???  - or "full ISO 
10646/Unicode - or something else.  Therefore, how you "convert" (handle) mixed 
values is dependent upon the computer's national character set "rules".

NOTE WELL:
  I am semi-weak on "all of this" - so I am more than willing to admit that 
anything stated above MAY be in error.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
