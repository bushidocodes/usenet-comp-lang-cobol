[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# micro focus personal cobol

_17 messages · 10 participants · 2001-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### micro focus personal cobol

- **From:** "Dave Krajcar" <raider@pacifier.com>
- **Date:** 2001-10-23T17:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
Hi...here's hoping one of you can shed some light on this.

I have a field with a picture clause of S9(17).  The value is
0000000000001234E.  When I try to use that field, I get an error saying that
there is an illegal digit in the numeric field.  I'm using Micro Focus
Personal Cobol.  I tried several flavors of the usage clause (comp-1, 2 etc)
and get syntax on them.  I tried the "sign is trailing" and that had no
effect.  What am I missing here?

Thanks!
-D
```

#### ↳ Re: micro focus personal cobol

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-23T18:52:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD5BE2E.6804D21C@home.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```


Dave Krajcar wrote:

> Hi...here's hoping one of you can shed some light on this.
>
…[8 more quoted lines elided]…
> -D

Dave,

As opposed to us guessing - to get an accurate answer - post the source code for
the program. Presumably you are using Personal COBOL with Windows ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: micro focus personal cobol

- **From:** "Dave Krajcar" <raider@pacifier.com>
- **Date:** 2001-10-23T21:15:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u5lB7.43945$Zb.21368497@news1.sttln1.wa.home.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <3BD5BE2E.6804D21C@home.com>`

```
OK, code posted in another message.  Yes, it is personal cobol for windows.

-D
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3BD5BE2E.6804D21C@home.com...
>
>
…[5 more quoted lines elided]…
> > 0000000000001234E.  When I try to use that field, I get an error saying
that
> > there is an illegal digit in the numeric field.  I'm using Micro Focus
> > Personal Cobol.  I tried several flavors of the usage clause (comp-1, 2
etc)
> > and get syntax on them.  I tried the "sign is trailing" and that had no
> > effect.  What am I missing here?
…[6 more quoted lines elided]…
> As opposed to us guessing - to get an accurate answer - post the source
code for
> the program. Presumably you are using Personal COBOL with Windows ?
>
> Jimmy, Calgary AB
>
>
```

#### ↳ Re: micro focus personal cobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-23T19:03:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fajB7.1527$0c6.233930@paloalto-snr1.gtei.net>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
Dave Krajcar <raider@pacifier.com> wrote in message
news:l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com...
> Hi...here's hoping one of you can shed some light on this.
>
> I have a field with a picture clause of S9(17).  The value is
> 0000000000001234E.  When I try to use that field, I get an error saying
that
> there is an illegal digit in the numeric field.  I'm using Micro Focus
> Personal Cobol.  I tried several flavors of the usage clause (comp-1, 2
etc)
> and get syntax on them.  I tried the "sign is trailing" and that had no
> effect.  What am I missing here?
>

Just guessing here, but the "E" does not appear to be valid numeric digit.

MCM
```

##### ↳ ↳ Re: micro focus personal cobol

- **From:** Colin Campbell <cmcampb@ibm.net>
- **Date:** 2001-10-23T13:42:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD5D62B.B86C066A@ibm.net>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net>`

```
If the data came from the mainframe, the "E" represents a digit "5" with a
positive (+) sign.

I haven't used MicroFocus COBOL for awhile,  However, if you are processing it
with an unsigned PICture, or with certain (unremembered) processing options, I
think MicroFocus COBOL might decide it is invalid.  Also, if you are working
in ASCII, not EBCDIC, I don't know whether the "E" is valid as a "signed,
positive 5".

Michael Mattias wrote:

> Dave Krajcar <raider@pacifier.com> wrote in message
> news:l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com...
…[14 more quoted lines elided]…
> MCM
```

###### ↳ ↳ ↳ Re: micro focus personal cobol

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-24T15:17:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r6lv7$gff$1@peabody.colorado.edu>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net> <3BD5D62B.B86C066A@ibm.net>`

```

On 23-Oct-2001, Colin Campbell <cmcampb@ibm.net> wrote:

> If the data came from the mainframe, the "E" represents a digit "5" with a
> positive (+) sign.
…[8 more quoted lines elided]…
> positive 5".

If you can decode the value by hand, you can always write a routine to
decode it.   Pass values with signed positive, signed negative, and unsigned
numbers to determine the code if you don't know it already.  Then write a
routine to look at this last digit, convert it, and save the sign.
```

##### ↳ ↳ Re: micro focus personal cobol

- **From:** "Dave Krajcar" <raider@pacifier.com>
- **Date:** 2001-10-23T21:08:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T_kB7.43942$Zb.21360701@news1.sttln1.wa.home.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net>`

```
Michael.

"E" should be a valid signed digit and represents +5.

It has been suggested that I post the code which I will do in another
message.

Thanks!
-D
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:fajB7.1527$0c6.233930@paloalto-snr1.gtei.net...
> Dave Krajcar <raider@pacifier.com> wrote in message
> news:l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com...
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: micro focus personal cobol

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2001-10-24T10:09:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N$athHAbVo17Ewea@ld50macca.demon.co.uk>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net> <T_kB7.43942$Zb.21360701@news1.sttln1.wa.home.com>`

```
In article <T_kB7.43942$Zb.21360701@news1.sttln1.wa.home.com>, Dave
Krajcar <raider@pacifier.com> writes
>Michael.
>
>"E" should be a valid signed digit and represents +5.
>
Just a guess. I believe that E as a sign is an, as now, unsupported
feature of certain mainframe Cobols and MicroFocus Cobol (whoops should
have been all CAPS) probably does not support that feature. 
```

###### ↳ ↳ ↳ Re: micro focus personal cobol

_(reply depth: 4)_

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-24T09:19:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r6il2$qdo$1@suaar1ac.prod.compuserve.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net> <T_kB7.43942$Zb.21360701@news1.sttln1.wa.home.com> <N$athHAbVo17Ewea@ld50macca.demon.co.uk>`

```
"E" as sign in this context is standard zoned decimal.
Use the SIGN"EBCDIC" compiler directive and micro-focus will
interpret the sign according to mainframe zoned decimal format.

$set sign"ebcdic"
       identification division.
       program-id. cobtest.
       environment division.
       data division.
       working-storage section.
       01  abc  pic S9(3).
       procedure division.
           move 555 to abc.
           goback.

After execution the value in abc is '55E'. This is what you want,
is it not? With sign"ascii" (the default) the value in abc is
'555'.
```

###### ↳ ↳ ↳ Re: micro focus personal cobol

_(reply depth: 5)_

- **From:** "Dave Krajcar" <raider@pacifier.com>
- **Date:** 2001-10-24T16:48:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<shCB7.45642$Zb.22770877@news1.sttln1.wa.home.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <fajB7.1527$0c6.233930@paloalto-snr1.gtei.net> <T_kB7.43942$Zb.21360701@news1.sttln1.wa.home.com> <N$athHAbVo17Ewea@ld50macca.demon.co.uk> <9r6il2$qdo$1@suaar1ac.prod.compuserve.com>`

```
Ron....you are right on the money!

That fixed the problem...my hat's off to you!
-D

"Ron" <Ron@NoSpamForMe.Com> wrote in message
news:9r6il2$qdo$1@suaar1ac.prod.compuserve.com...
> "E" as sign in this context is standard zoned decimal.
> Use the SIGN"EBCDIC" compiler directive and micro-focus will
…[17 more quoted lines elided]…
>
```

#### ↳ Re: micro focus personal cobol

- **From:** "Dave Krajcar" <raider@pacifier.com>
- **Date:** 2001-10-23T21:13:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4lB7.43944$Zb.21367712@news1.sttln1.wa.home.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
It was suggested that I post the code in question.  I have simplified it to do nothing but display the number.  See below...

From the data division, file section:

       01  CARDHOLDER-DET    REDEFINES CCS-RECORD.                      COMPANY 000087
           05  RECORD-TYPE          PIC  X(001).                        COMPANY 000088
               88 CARDHOLDER-DETAIL VALUE "6".                          COMPANY 000089
           05  COMPNAY-NUMBER       PIC  X(009).                        COMPANY 000090
           05  TRAN-CODE            PIC  9(004).                        COMPANY 000091
           05  POSTING-DATE         PIC  9(008).                        COMPANY 000092
           05  TRAN-DATE            PIC  9(008).                        COMPANY 000093
           05  TRAN-AMOUNT-AREA.                                        COMPANY 000093
               07  TRAN-AMOUNT      PIC S9(017).                        COMPANY 000094
           05  MERCHANT-NAME        PIC  X(025).                        COMPANY 000095

From the procedure division:

       2000-process.
           perform 2100-read-data.
           perform 2200-driver
               until at-end-of-input.
      *
      *
       2100-read-data.
           read input-data-file
           at end
               set at-end-of-input to true.
      *
      *
       2200-driver.
           if cardholder-record
               display cardholder-ID-num
                   "  "
                   cardholder-name
                   "  "
                   gl-number
                       in cardholder-rec.
           if cardholder-detail
               display "----->" tran-amount
               "<-----".
           perform 2100-read-data.

If I change the above display from tran-amount to 
tran-amount-area, my resulting display is
  ----->0000000000001234E<-----
If I try it as is, I get an illegal character in numeric field
message (error 163). The "E" should be valid as it is the sign
digit and represents a value of +5.

Thanks!
-d


"Dave Krajcar" <raider@pacifier.com> wrote in message news:l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com...
> Hi...here's hoping one of you can shed some light on this.
> 
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: micro focus personal cobol

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-23T16:52:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r4oq3$i3t$1@suaar1ac.prod.compuserve.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <e4lB7.43944$Zb.21367712@news1.sttln1.wa.home.com>`

```
Are you getting this data from an OS/390 system originally in EBCDIC?
If so, use the SIGN EBCDIC compiler directive to recognize EBCDIC
signed data. Starting in column 7 of the very first line of the
program before Identification Division put [$set sign"ebcdic"]
without the brackets of course.
```

#### ↳ Re: micro focus personal cobol

- **From:** "Bill" <suppehovet@att.net>
- **Date:** 2001-10-23T23:20:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HWmB7.80438$WW.4182548@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
it is indeed a positive five converted from an EBCDIC system

here is what I have seen before
A is 1
B is 2   etc....

J is negative 1
K is negative 2   etc......

all you need to do is a inspect statement...
INSPECT QTY-FIELD REPLACING ALL "A" BY "1"
assuming you can redefine your qty field as a alphabetic so the replace
works
as for the negative qty's....I would inspect and tally a indicator for all
negative numbers
I don't know how to change a "J" to a negative 1.....maybe someone else here
does




Dave Krajcar wrote in message ...
>Hi...here's hoping one of you can shed some light on this.
>
>I have a field with a picture clause of S9(17).  The value is
>0000000000001234E.  When I try to use that field, I get an error saying
that
>there is an illegal digit in the numeric field.  I'm using Micro Focus
>Personal Cobol.  I tried several flavors of the usage clause (comp-1, 2
etc)
>and get syntax on them.  I tried the "sign is trailing" and that had no
>effect.  What am I missing here?
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: micro focus personal cobol

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-24T15:21:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r6m59$ghe$1@peabody.colorado.edu>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <HWmB7.80438$WW.4182548@bgtnsc05-news.ops.worldnet.att.net>`

```

On 23-Oct-2001, "Bill" <suppehovet@att.net> wrote:

> here is what I have seen before
> A is 1
…[3 more quoted lines elided]…
> K is negative 2   etc......

I have hand written on my green card that +0 is [ and -0 is ]
```

#### ↳ Re: micro focus personal cobol

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-24T20:27:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FuFB7.41741$ev2.49934@www.newsranger.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
On Tue, 23 Oct 2001 17:48:01 GMT, in article
<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>, Dave Krajcar stated 
>
>Hi...here's hoping one of you can shed some light on this.
…[10 more quoted lines elided]…
>

If you have a COBOL Reference look up External and Internal Floating Decimal
Point usage.  It is different than a fixed decimal point. S9(17) is fixed.  I
don't know the maximum number of places out a decimal point can go for a fixed
field (For your compiler), but you may want to look it up.
>

Internal
05  COMPUTE-RESULT            USAGE COMP-1 VALUE 06.23E-24

comes from an example in my book for a field with a set value.

External
05 COMPUTE-RESULT             -9V9(9)E-99.

I have never had to use this so I cant give an example.
```

##### ↳ ↳ Re: Microfocus Sign Overpunch

- **From:** leclaire <leclair@rr.com>
- **Date:** 2001-10-25T12:18:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD80274.8B24415B@rr.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com> <FuFB7.41741$ev2.49934@www.newsranger.com>`

```

  To allow Microfocus to interpret Sign Overpunch ASCII numeric data,
there is a compiler directive you must include either when compiling or
as the first line of source code:

      $Set sign"ebcdic"
       Identification Division.
       Program-ID. etc.
      *Program uses Sign Overpunch ASCII numeric data

  All your programs will then be able to use the data from your other
system, but be aware that the directive affects ALL signed numeric data
used by your program.

-Rob
```

#### ↳ Re: micro focus personal cobol

- **From:** leclaire <leclair@rr.com>
- **Date:** 2001-10-25T12:19:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD802B5.E8F9E7C6@rr.com>`
- **References:** `<l3iB7.43611$Zb.21170392@news1.sttln1.wa.home.com>`

```
  To allow Microfocus to interpret Sign Overpunch ASCII numeric data,
there is a compiler directive you must include either when compiling or
as the first line of source code:

      $Set sign"ebcdic"
       Identification Division.
       Program-ID. etc.
      *Program uses Sign Overpunch ASCII numeric data

  All your programs will then be able to use the data from your other
system, but be aware that the directive affects ALL signed numeric data
used by your program.

-Rob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
