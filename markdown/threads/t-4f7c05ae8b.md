[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The redefines clause & comp-3

_26 messages · 10 participants · 2005-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### The redefines clause & comp-3

- **From:** "ed" <ed.narayan@gmail.com>
- **Date:** 2005-08-08T07:13:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com>`

```
Hi,
I had a couple of questions on standard cobol concepts:

1) Is there a difference between the Redefines clause being specified
at a group level rather than at an elementary level ? For instance I
could have:

01 record.
   05 marker...
   05 rec1.
      10 data1 ...
   05 rec2 redefines rec1.
      10 data2 ...

Lets assume here the data file can have either rec1/rec2 depending on
the value of the "marker" field. This is the normal case of redefines
at this group level.

However if I have redefines at an elementary level
10 data1 Pic xxx.
10 data1new Pic 9(3).

Does data1new always take precedence ? i.e. does the data file only
contain type "data1new" ? or can it also contain type "data1". If it
can contain both types is it reasonable to expect a "marker" field (as
used above) in the data wwhich identifies which type is in use ?


2) Does comp-3 always have a sign indicator in the last 1/2 byte ? i.e.
for example a C/D or an F in the last 1/2 byte. Or can it be that no
such information is there in the last 1/2 byte indicating that the data
is unsigned?

Regards,
ed
```

#### ↳ Re: The redefines clause & comp-3

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-08T15:08:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dAKJe.85772$mC.37224@tornado.tampabay.rr.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com>`

```

"ed" <ed.narayan@gmail.com> wrote in message 
news:1123510409.171687.228790@g49g2000cwa.googlegroups.com...
> Hi,
> I had a couple of questions on standard cobol concepts:
…[3 more quoted lines elided]…
> could have:

From a "usage" standpoint, not that I'm aware of.   It's dictated by what 
you are trying to do.  It's mostly used as in your first example as a record 
"overlay"...some overlays are bigger than others...but it's how you use them 
that's important.

> 01 record.
>   05 marker...
…[11 more quoted lines elided]…
> 10 data1new Pic 9(3).
I assume that data1new redefines data1 and you missed this in error?


> Does data1new always take precedence ? i.e. does the data file only
> contain type "data1new" ? or can it also contain type "data1". If it
> can contain both types is it reasonable to expect a "marker" field (as
> used above) in the data wwhich identifies which type is in use ?
Assuming the above:

There is nothing to take precedence.  Each type merely represents a "view" 
of the same data.
A file contains what it contains, you can then view the data through either 
definition.

Typically it is important to know which data you are using if it becomes 
important later in terms of unsupported operations on data types.

For example we have a lot of the following:
05 WS-2BYTE      PIC 9(04) COMP.
05 WS-2BYTE-X  PIC XX REDEFINES WS-2BYTE.

The two fields here are totally incompatible - but it lets us do some record 
string building with binary data.  It's still just 2 bytes.

Maybe I miss the question?

> 2) Does comp-3 always have a sign indicator in the last 1/2 byte ? i.e.
> for example a C/D or an F in the last 1/2 byte. Or can it be that no
…[4 more quoted lines elided]…
> ed
<the following may not be true for every implementation that exists in the 
world in all languages and dialects.  It is also just an opinion>

The half nibble is reserved for sign whether or not the field is declared as 
signed. That is why when defining packed fields you often see declare the 
extra half byte even if it's not really needed as it exists anyway.   That's 
why you won't often see PIC 9(07) COMP-3 because it's 4 bytes just the same 
as PIC 9(08) COMP-3.....

JCE
```

#### ↳ Re: The redefines clause & comp-3

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-08-08T10:19:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11feu0a78og6p73@news.supernews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com>`

```
ed wrote:
> Hi,
> I had a couple of questions on standard cobol concepts:
…[14 more quoted lines elided]…
> at this group level.

The data file can have either rec1/rec2 WITHOUT regard to the "marker" 
field. Whether the "marker" exists, or is correct, depends on the diligence 
of the programmer.

>
> However if I have redefines at an elementary level
…[6 more quoted lines elided]…
> used above) in the data wwhich identifies which type is in use ?

It can have either. It is not reasonable to always expect a "marker" field.

The REDEFINES determines ONLY how the data name will be treated by the 
compiler at execution time.

Often a REDEFINES is used to facilitate data manipulation.

In your example, to get "bb0" in those three bytes, you can't MOVE 0 TO 
data1new. Likewise, to get "ABC" in those three bytes, you can't MOVE "ABC" 
TO data1new.

>
>
…[3 more quoted lines elided]…
> that the data is unsigned?

There is always a sign indicator.* Unsigned = positive. The nibble can be 
any of FACE - or CAFE if you're into Latte - (indicating positive), the 
other possibilities (BD) indicate negative.

-------
*Rule of the Universe: Every bit is either on or off. This is a corollary to 
the basic rule that "Everything has to be somewhere," as in "Why is this 
here?"
```

##### ↳ ↳ Re: The redefines clause & comp-3

- **From:** "Walter Murray" <wmurray@midtown.net>
- **Date:** 2005-08-08T11:12:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123524913_71@spool6-east.superfeed.net>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote:
 > There is always a sign indicator. Unsigned = positive. The nibble can be
> any of FACE - or CAFE if you're into Latte - (indicating positive), the
> other possibilities (BD) indicate negative.

WARNING:  The rules about what constitutes a valid sign nibble, and how that
nibble is interpreted, are entirely dependent on the implementation.  The
rules given above are not universal.  See your particular compiler's
documentation for details.  (Hint:  You'll probably find this documented
under the USAGE clause.)

Walter

Walter J. Murray



----== Posted via Newsfeeds.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeeds.com The #1 Newsgroup Service in the World! 120,000+ Newsgroups
----= East and West-Coast Server Farms - Total Privacy via Encryption =----
```

###### ↳ ↳ ↳ Re: The redefines clause & comp-3

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T12:34:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8c5m$1n5v$1@si05.rsvl.unisys.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net>`

```

"Walter Murray" <wmurray@midtown.net> wrote in message
news:1123524913_71@spool6-east.superfeed.net...

> WARNING:  The rules about what constitutes a valid sign nibble, and how
that
> nibble is interpreted, are entirely dependent on the implementation.  The
> rules given above are not universal.  See your particular compiler's
> documentation for details.  (Hint:  You'll probably find this documented
> under the USAGE clause.)

Indeed, the very existence of "COMP-3" in the language is dependent on the
implementor; the '68, '74, '85 and '02 standards are silent on the subject
of COMP-anything other than just plain COMPUTATIONAL.   It's not just what
constitutes a "sign nibble" in COMP-3 and how it's interpreted that's
implementor-defined, it's the very meanings of "nibble" and "COMP-3" in the
first place.

    -Chuck Stevens
```

###### ↳ ↳ ↳ COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-08T20:16:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z4PJe.959031$pI6.87695@fe06.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com>`

```
IBM (all platforms and compilers that I know of) have "COMP-3" (as an extension) 
= "Packed-Decimal" (USAGE Packed-Decimal was made Standard  in '85 Standard).

Many implementors "emulated" this for compatibility with IBM (as they did for 
many other IBM extension) in the relatively early days of COBOL.

As Chuck indicates below,  COMP-3 (if supported at all) could be equivalent to 
BINARY, DISPLAY, or NATIONAL or anything else.

Although I (personally) know of some implementations with other USAGES 
equivalent to "Packed-Decimal" - I don't (personally) know of any implementation 
that supports COMP-3 where it is NOT Packed-Decimal.  I would be curious if 
there are some/any.

Other IBM (extension) usages are NOT as universal.
  COMP-1 and COMP-2 are floating point for IBM, but are occasionally other 
usages for other compilers
  COMP-4 isn't universal even across IBM platforms.  (It is Binary on mainframe 
and Packed-Decimal on OS/400)

 For "workstation" compilers, it is common for COMP-5 to be a "native" binary 
(recently adopted by IBM)
More than one vendor has COMP-6 as Packed-Decimal with NO sign-nibble (when no 
"S" in Picture)

   ***

Even for USAGE Packed-Decimal and Binary, the Standard doesn't "dictate" exactly 
how the data is stored - only what "radix" must be used.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T20:42:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8g3l$3ge$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com>`

```

On  8-Aug-2005, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> Even for USAGE Packed-Decimal and Binary, the Standard doesn't "dictate"
> exactly
> how the data is stored - only what "radix" must be used.

It's amusing that we're supposed to switch from COMP-3 to Packed-Decimal because
it sounds as though it is more standard that way, even though that is a fiction.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-08T23:06:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YzRJe.49583$vm2.17077@fe10.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu>`

```
USAGE Packed-Decimal yields "portable source code" ('85 Standard or later)

USAGE COMP-3 doesn't even yield portable source code
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 7)_

- **From:** "ed" <ed.narayan@gmail.com>
- **Date:** 2005-08-08T21:46:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123562767.307242.191450@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<YzRJe.49583$vm2.17077@fe10.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com>`

```
To summarise what I could gather:

1) A redefines means that the data file can contain either the
redefined item OR any of the redefining items. This interpretation is
independent of whether the redefines is used on an elementary (which
has a PIC) item or on a group level item.

2) Comp-3 format has a sign in the last nibble on ibm mainframes but
may not appear on others. No standard seems to exist for the same.

Thanks everyone !
Regards,
ed
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-08-09T08:00:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fha7rh1o9pe66@news.supernews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com>`

```
ed wrote:
> To summarise what I could gather:
>
Not exactly.

> 1) A redefines means that the data file can contain either the
> redefined item OR any of the redefining items. This interpretation is
> independent of whether the redefines is used on an elementary (which
> has a PIC) item or on a group level item.

Of course a REDEFINES area may contain anything, not just what is defined.

>
> 2) Comp-3 format has a sign in the last nibble on ibm mainframes but
> may not appear on others. No standard seems to exist for the same.

COMP-3 will always have a sign somewhere. IBM *IS* the de-facto standard. If 
you understand the IBM standard, you can cope with whatever else is out 
there.

IBM equipment (and surely others), had/has hardware components that actually 
did decimal arithmetic - not just convert a decimal number to binary, 
manipulate the bits in binary, and convert the results back to decimal - 
actual decimal.

PCs, for example, don't do decimal.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-09T16:01:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gr4Ke.19518$Di2.12439@fe02.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:11fha7rh1o9pe66@news.supernews.com...
> ed wrote:

>> 2) Comp-3 format has a sign in the last nibble on ibm mainframes but
>> may not appear on others. No standard seems to exist for the same.
…[3 more quoted lines elided]…
>

and your evidence for this is what?  I know I asked if COMP-3 means something 
other than Packed-Decimal (as an extension) for any other compiler, but I 
certainly would never want to "assume this".  And SEVERAL COBOL compilers *do* 
support "unsigned" packed-decimal formats.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 10)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-08-09T16:18:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fi7c61ov6rt93@news.supernews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com> <Gr4Ke.19518$Di2.12439@fe02.news.easynews.com>`

```
William M. Klein wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
> news:11fha7rh1o9pe66@news.supernews.com...
…[9 more quoted lines elided]…
> and your evidence for this is what?

Experience? I understand, therefore I cope.

> I know I asked if COMP-3 means
> something other than Packed-Decimal (as an extension) for any other
> compiler, but I certainly would never want to "assume this".

Whatever works for you is fine by me.

> And
> SEVERAL COBOL compilers *do* support "unsigned" packed-decimal
> formats.

Not really. Even if declared "unsigned," the compiler nevertheless treats 
the number as positive. And does the bit representation in these off-brand 
compilers you mention differ between an allegedly "unsigned" value and an 
honest value differ?
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 11)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-09T14:50:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123624258.999844.156230@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<11fi7c61ov6rt93@news.supernews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com> <Gr4Ke.19518$Di2.12439@fe02.news.easynews.com> <11fi7c61ov6rt93@news.supernews.com>`

```
> Not really.

No. Really.

> Even if declared "unsigned," the compiler nevertheless
> treats the number as positive.

The number is treated as positive when unsigned, yes.

> And does the bit representation in these off-brand

What do you mean by 'off-brand' ? Is IBM the the only 'on-brand' ?  Is
a Unisys brand compiler on a Unisys machine 'off-brand' ?

> compilers you mention differ between an allegedly
> "unsigned" value and an honest value differ?

Yes. An unsigned may be implemented as having no nibble for the sign
such that 9(8) occupies 8 nibbles, 4 bytes.

> Experience? I understand, therefore I cope.

You should get out more, you understand less than think you do.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 12)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-08-09T21:33:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11fipsahnk2075a@news.supernews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com> <Gr4Ke.19518$Di2.12439@fe02.news.easynews.com> <11fi7c61ov6rt93@news.supernews.com> <1123624258.999844.156230@g49g2000cwa.googlegroups.com>`

```
Richard wrote:
>> Not really.
>
…[10 more quoted lines elided]…
> a Unisys brand compiler on a Unisys machine 'off-brand' ?

I think you've pretty much gotten a grip on the concept.

>
>> compilers you mention differ between an allegedly
…[3 more quoted lines elided]…
> such that 9(8) occupies 8 nibbles, 4 bytes.

Back in my day, there were things that were sacred and thing that were 
profane. The kind of data representation you report is an absurdity. I'm not 
saying it didn't happen, just that it opens the door to ghastly errors. I 
sure as Hell wouldn't let my daughter date one.

>
>> Experience? I understand, therefore I cope.
>
> You should get out more, you understand less than think you do.

Hmmph! I don't need to get out. I have the internet.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-09T15:35:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddbb46$f3g$1@si05.rsvl.unisys.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com> <Gr4Ke.19518$Di2.12439@fe02.news.easynews.com> <11fi7c61ov6rt93@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
news:11fi7c61ov6rt93@news.supernews.com...

> > And
> > SEVERAL COBOL compilers *do* support "unsigned" packed-decimal
> > formats.
>
> Not really.

Yes, really.

> Even if declared "unsigned," the compiler nevertheless treats
> the number as positive.

You're confusing how the data is encoded with how the object code interprets
it.  There is no requirement in the standard that the format of a data item
whose PICTURE character-string does not specify a sign nonetheless must
allocate space for the sign that the programmer has requested not be there.

> And does the bit representation in these off-brand
> compilers you mention differ between an allegedly "unsigned" value and an
> honest value differ?

I think it's highly likely that at least some of your financial transactions
are processed on systems that allocate six (not seven or even eight)
four-bit units, each unit containing a decimal digit, for an item declared
"PICTURE 9(6) PACKED-DECIMAL".   The compiler correctly *understands* such
items as being positive in the *absence* of a sign in both the format and
the data in that format.  Some architectures may require the user to account
for the space occupied by a sign even when the datum in quesion cannot be
negative, but for the life of me I can't imagine why they would continue to
do so.

As to "honest value":  what exactly is dishonest about a representation of a
value that the programmer has expressly stated cannot be negative
nonetheless having the capability of containing a negative value?  Where I
come from, successfully forcing a negative value into an unsigned item
qualifies as data corruption on the part of the programmer!

        -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 9)_

- **From:** epc8@juno.com
- **Date:** 2005-08-09T15:42:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123627348.428565.228260@z14g2000cwz.googlegroups.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <1123562767.307242.191450@z14g2000cwz.googlegroups.com> <11fha7rh1o9pe66@news.supernews.com>`

```
HeyBub wrote:

> IBM equipment (and surely others), had/has hardware components that actually
> did decimal arithmetic - not just convert a decimal number to binary,
> manipulate the bits in binary, and convert the results back to decimal -
> actual decimal.

> PCs, for example, don't do decimal.

Two counter examples. First, the IBM-PC XT/370. :-).

A number of micro-computer CPU chips *do* handle addition and
subtraction of (unsigned) packed BCD (2 digits/byte) - the 8080/Z80,
the 65xx and the 80x86 definitely do. Also the 80x87 chip loads and
stores a form of BCD.

I believe that the original 360s handled packed decimal in microcode
not that dissimilar to the operations provided by today's (and
yesterday's) CPU/FPU chips.

I seem to remember that some versions of Rexx and COBOL on the PC take
advantage of these decimal instructions.

[Just for grins look up Wozniak's ingenious method of converting binary
to packed BCD by shifting successive bits into a BCD accumulator that
is being doubled over and over again.]
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-09T13:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddabhs$58b$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com>`

```

On  8-Aug-2005, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> USAGE Packed-Decimal yields "portable source code" ('85 Standard or later)
>
> USAGE COMP-3 doesn't even yield portable source code

Which means that I can copy a packed-decimal number in a file in one platform
and it will look the same in another platform?

Having the word "packed-decimal" compile in two different platforms doesn't mean
that it describes the same thing.
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs (was: The redefines clause & comp-3

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-09T15:59:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cp4Ke.62130$GX1.5026@fe01.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <dd8g3l$3ge$1@peabody.colorado.edu> <YzRJe.49583$vm2.17077@fe10.news.easynews.com> <ddabhs$58b$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ddabhs$58b$1@peabody.colorado.edu...
>
> On  8-Aug-2005, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
…[6 more quoted lines elided]…
> and it will look the same in another platform?

No, it may or may not (probably will NOT)

>
> Having the word "packed-decimal" compile in two different platforms doesn't 
> mean
> that it describes the same thing.

Yes, but if you have a "convert to portable file" program that takes "native" 
Packed-Decimal and moves it to "Display Sign is Separate" numeric data (along 
with all other "comp-type" data), then that program will be as portable as the 
sending USAGEs are portable (in source code - not internal format).
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs

_(reply depth: 5)_

- **From:** Vincent Danion <vfollowedbyname@scort.com>
- **Date:** 2005-08-09T09:26:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lr45jF13vq4nU1@individual.net>`
- **In-Reply-To:** `<Z4PJe.959031$pI6.87695@fe06.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com>`

```
William M. Klein a ï¿½crit :

>   COMP-4 isn't universal even across IBM platforms.  (It is Binary on mainframe 
> and Packed-Decimal on OS/400)

Are you sure about that ?

I read in "ILE COBOL for AS/400 Programmer's Guide, Version 4", page 151:

"COMP-4 is synonymous with BINARY, and COMP and COMP-3 are synonymous
with PACKED-DECIMAL."

My understanding (regarding IBM compilers) is that:
- COMP-3 always means PACKED-DECIMAL, either on mainframe or on OS/400.
- COMP-4 always means BINARY, either on mainframe or on OS/400.
- However COMP means BINARY on mainframe, but PACKED-DECIMAL on OS/400.

Am I right or not ?
```

###### ↳ ↳ ↳ Re: COMP-? / Extension USAGEs

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-09T15:56:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dm4Ke.66243$vm2.3482@fe10.news.easynews.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <11feu0a78og6p73@news.supernews.com> <1123524913_71@spool6-east.superfeed.net> <dd8c5m$1n5v$1@si05.rsvl.unisys.com> <Z4PJe.959031$pI6.87695@fe06.news.easynews.com> <3lr45jF13vq4nU1@individual.net>`

```
You are right and I was wrong.  (As someone who does NOT use OS/400, I always 
get those two confused).  Thanks for the correction.
```

#### ↳ Re: The redefines clause & comp-3

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T16:01:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd7vlb$o09$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com>`

```

On  8-Aug-2005, "ed" <ed.narayan@gmail.com> wrote:

> 1) Is there a difference between the Redefines clause being specified
> at a group level rather than at an elementary level ? For instance I
> could have:

Not every compiler allows redefines at the 01 level.
```

##### ↳ ↳ Re: The redefines clause & comp-3

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T10:59:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd86i6$1jt9$1@si05.rsvl.unisys.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <dd7vlb$o09$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:dd7vlb$o09$1@peabody.colorado.edu...
>
> On  8-Aug-2005, "ed" <ed.narayan@gmail.com> wrote:
…[5 more quoted lines elided]…
> Not every compiler allows redefines at the 01 level.

Redefines is disallowed at the 01 level *in the File and Communication
sections* by the '74, '85 and '02 standards, but I'd have to say I would
*definitely* be surprised to run across a compiler that prohibited it at the
01 level in Working-Storage, and I'd regard that as grounds for a nastygram
to the vendor!  Redefining an 01-level item in Working-Storage is, as far as
I'm concerned, standard COBOL!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: The redefines clause & comp-3

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-08T18:24:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd880r$scr$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <dd7vlb$o09$1@peabody.colorado.edu> <dd86i6$1jt9$1@si05.rsvl.unisys.com>`

```

On  8-Aug-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> > Not every compiler allows redefines at the 01 level.
>
…[5 more quoted lines elided]…
> I'm concerned, standard COBOL!

My bad.

Since I have never been able to come up with an acceptable reason for this
difference, I just avoid it altogether, especially since we use copymembers and
copy and pasting of file formats between sections.
```

###### ↳ ↳ ↳ Re: The redefines clause & comp-3

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-08-08T12:50:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dd8d2v$1nph$1@si05.rsvl.unisys.com>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <dd7vlb$o09$1@peabody.colorado.edu> <dd86i6$1jt9$1@si05.rsvl.unisys.com> <dd880r$scr$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message
news:dd880r$scr$1@peabody.colorado.edu...

> Since I have never been able to come up with an acceptable reason for this
> difference, I just avoid it altogether, especially since we use
copymembers and
> copy and pasting of file formats between sections.

I know of some vendors that *do* allow Redefines in the File and
Communcation sections, I suspect for the very reasons you cite, but it needs
to be identified as an implentation-defined extension.

I believe the reason the standards disallow Redefines in these contexts is
that in a given FD/SD in the File section, and in a given CD in the
Communication sections, the 01-level items *already* implicitly redefine
each other, specifically as distinct from elsewhere.  Coding the data
descriptions with Redefines in those contexts might might mislead the
programmer into thinking that deleting the clause would turn the records
into separate data spaces; it doesn't.  In that context, they redefine each
other regardless.

The reason may not be acceptable *to you*, but unless you can convincingly
argue that it's *unacceptable to everyone* I don't expect to see this
prohibition lifted for the File Section any time soon (the Communication
Section is marked obsolete in '02 COBOL and won't be in the next standard).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: The redefines clause & comp-3

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-08T14:05:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123535151.336805.250480@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<dd880r$scr$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <dd7vlb$o09$1@peabody.colorado.edu> <dd86i6$1jt9$1@si05.rsvl.unisys.com> <dd880r$scr$1@peabody.colorado.edu>`

```
> Since I have never been able to come up with an acceptable reason for this
> difference,

All records under the same FD are implicit redefines of each other
(they all occupy the same area), but explicit redefines in earlier
versions would have implications about the length of each 01 level. ie
if explicitly redefined they would be the same length and this would be
a problem for writing variable record files.
```

###### ↳ ↳ ↳ Re: The redefines clause & comp-3

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-08-09T13:38:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ddabk0$58c$1@peabody.colorado.edu>`
- **References:** `<1123510409.171687.228790@g49g2000cwa.googlegroups.com> <1123535151.336805.250480@o13g2000cwo.googlegroups.com>`

```

On  8-Aug-2005, "Richard" <riplin@Azonic.co.nz> wrote:

> > Since I have never been able to come up with an acceptable reason for this
> > difference,
…[5 more quoted lines elided]…
> a problem for writing variable record files.

That's what I've read.   My statement stands.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
