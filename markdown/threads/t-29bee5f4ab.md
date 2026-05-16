[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Numeric Edited Fields

_16 messages · 10 participants · 2001-08_

---

### Numeric Edited Fields

- **From:** "Stephan Wiesner" <stephan@stephanwiesner.de>
- **Date:** 2001-08-11T11:08:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
I read that I can edit numeric fields like this:
01 myNumber Pic ZZZ.

Doesn't work with Acucobol, though :-(
I get ' VALUE type error'

Anyone knows how to do it?

Stephan
```

#### ↳ Re: Numeric Edited Fields

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-08-11T14:35:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
On Sat, 11 Aug 2001 11:08:31 +0200, Stephan Wiesner wrote:

>I read that I can edit numeric fields like this:
>01 myNumber Pic ZZZ.
…[8 more quoted lines elided]…
>
Try PIC ZZ9 BLANK WHEN ZERO.


Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

##### ↳ ↳ Re: Numeric Edited Fields

- **From:** "Stephan Wiesner" <stephan@stephanwiesner.de>
- **Date:** 2001-08-11T15:55:27+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l3dfb$sld$07$1@news.t-online.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es>`

```
No, does work, but after that the variable isn't numeric.
Thought Z means that the '0' are suppressed. Doesn't make sense if I don't
have a numeric value, does it?

Stephan


"Willem Clements" <willem@horizontes-informatica.com> schrieb im Newsbeitrag
news:jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es...
> On Sat, 11 Aug 2001 11:08:31 +0200, Stephan Wiesner wrote:
>
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-08-11T17:04:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.ghx9790.pminews@news.wanadoo.es>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es> <9l3dfb$sld$07$1@news.t-online.com>`

```
On Sat, 11 Aug 2001 15:55:27 +0200, Stephan Wiesner wrote:

>No, does work, but after that the variable isn't numeric.
>Thought Z means that the '0' are suppressed. Doesn't make sense if I don't
…[4 more quoted lines elided]…
>
A numeric edited field is not anymore numeric but alphanumeric. Once edited
it can contain blanks, decimal points, commas, plus and minus signs and
currency signs.



Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

_(reply depth: 4)_

- **From:** "Stephan Wiesner" <stephan@stephanwiesner.de>
- **Date:** 2001-08-11T17:22:19+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l3ii5$172$05$1@news.t-online.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es> <9l3dfb$sld$07$1@news.t-online.com> <jvyyrzubevmbagrfvasbezngvpnpbz.ghx9790.pminews@news.wanadoo.es>`

```
So, I work with my normal numeric variables and if I want to display them, i
have to move them to a formated variable first?
Well, at least now it works, although in quite a curious way...

Thanks for the help!
Stephan



> A numeric edited field is not anymore numeric but alphanumeric. Once
edited
> it can contain blanks, decimal points, commas, plus and minus signs and
> currency signs.
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-08-12T13:16:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xkvd7.6987$NJ6.28517@www.newsranger.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <jvyyrzubevmbagrfvasbezngvpnpbz.ghx2b50.pminews@news.wanadoo.es> <9l3dfb$sld$07$1@news.t-online.com>`

```
Actually, the value never is numeric - it's always "numeric edited" which is a
different animal.  There's nothing wrong with using ZZZ as the destination for a
MOVE, a GIVING or a COMPUTE.

In article <9l3dfb$sld$07$1@news.t-online.com>, Stephan Wiesner says...
>
>No, does work, but after that the variable isn't numeric.
…[31 more quoted lines elided]…
>
```

#### ↳ Re: Numeric Edited Fields

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2001-08-11T09:38:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l3g16$257$1@suaar1ac.prod.compuserve.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
There is no reason this line should not compile.
Please post the whole program so we can what you are really doing.
```

##### ↳ ↳ Re: Numeric Edited Fields

- **From:** "Stephan Wiesner" <stephan@stephanwiesner.de>
- **Date:** 2001-08-11T16:45:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l3gdr$6mc$00$1@news.t-online.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <9l3g16$257$1@suaar1ac.prod.compuserve.com>`

```
Okay, here it goes.
The compiler says:
E:\Project1\Source\Hello.cbl, line 32: HMH is not numeric
Hello.acu - 1 Error(s), 0 Warning(s)




       identification division.
       program-id. zins3.

       environment division.

       configuration section.

       special-names.
           decimal-point is comma.
       input-output section.

       data division.
      * aus nem file

       working-storage section.
      * interne variablen
        01 strings.
           03 vorname  pic X(25).
           03 nachname pic X(25).
        01 zahlen.
           03 gehalt   pic 9(4)v9(2) value 100,0.
           03 zuschlag pic 9(2)      value 0.
           03 hmh      PIC ZZ9 BLANK WHEN ZERO.
        01 arrays.
           03 tage Pic X(20) Occurs 7 Times Indexed by Table-Index.



        procedure division.
        main.
           compute gehalt = gehalt + hmh
           display gehalt
           display
           accept omitted
           exit program.
           stop run.
           .










"Ron" <NoSoy@swbell.net> schrieb im Newsbeitrag
news:9l3g16$257$1@suaar1ac.prod.compuserve.com...
> There is no reason this line should not compile.
> Please post the whole program so we can what you are really doing.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-08-11T16:16:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GTcd7.6260$NJ6.27832@www.newsranger.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <9l3g16$257$1@suaar1ac.prod.compuserve.com> <9l3gdr$6mc$00$1@news.t-online.com>`

```
Hi Stephen,

A few things:

Your hmh cannot be used in a calculation because it it is not a pure numeric
field. Create a numeric field and perform the calc on that field. Move it to the
num ed field when you're ready to display it. 

Your hmh does not contain a  value, nor is one moved to it. You can include a
VALUE clause to the data def or move the value to it.

Numeric edited fields are used for display (or print) purposes, so numeric data
should be moved to them just before display. Any calculations s/b performed on
the numeric version of the field; when display is required, then the numeric
field s/b moved to the numeric edited field first. 

Regards, Jack.


n article <9l3gdr$6mc$00$1@news.t-online.com>, Stephan Wiesner says...
>
>Okay, here it goes.
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-08-12T13:19:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Invd7.6989$NJ6.28447@www.newsranger.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <9l3g16$257$1@suaar1ac.prod.compuserve.com> <9l3gdr$6mc$00$1@news.t-online.com>`

```
Since hmh is never displayed - simply make it pic 999 and it will work.  It is
being used as a source field for the ADD which is not allowed.


In article <9l3gdr$6mc$00$1@news.t-online.com>, Stephan Wiesner says...
>
>Okay, here it goes.
…[63 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Numeric Edited Fields

- **From:** "Solar Systems" <solar@conterra.com>
- **Date:** 2001-08-12T10:34:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b76932f@news.conterra.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <9l3g16$257$1@suaar1ac.prod.compuserve.com> <9l3gdr$6mc$00$1@news.t-online.com>`

```
Move some numeric value to HMH before the compute...


"Stephan Wiesner" <stephan@stephanwiesner.de> wrote in message
news:9l3gdr$6mc$00$1@news.t-online.com...
> Okay, here it goes.
> The compiler says:
> E:\Project1\Source\Hello.cbl, line 32: HMH is not numeric
> Hello.acu - 1 Error(s), 0 Warning(s)
```

#### ↳ Re: Numeric Edited Fields

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2001-08-11T14:53:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JFbd7.74057$oh1.28830922@news2.rdc2.tx.home.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
Hmm...     maybe this will work?   the ZZZ really should work.... maybe it's
just that compiler.  If you figure it out post cause I'm curious.
Mike


01 myNumber PIC Z(3) VALUE ZERO.



"Stephan Wiesner" <stephan@stephanwiesner.de> wrote in message
news:9l2slb$2gb$03$1@news.t-online.com...
> I read that I can edit numeric fields like this:
> 01 myNumber Pic ZZZ.
…[8 more quoted lines elided]…
>
```

#### ↳ Re: Numeric Edited Fields

- **From:** christer.o.jonsson@home.se (Christer O. Jönsson)
- **Date:** 2001-08-11T12:50:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d46942c6.0108111150.5acdf8f8@posting.google.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
"Stephan Wiesner" <stephan@stephanwiesner.de> wrote in message news:<9l2slb$2gb$03$1@news.t-online.com>...
> I read that I can edit numeric fields like this:
> 01 myNumber Pic ZZZ.
…[6 more quoted lines elided]…
> Stephan

Hi

Your problem is't the picture ZZZ it's that you try to do calculation
on it, the Z picture is for display/printing and only semi numeric and
can't be used for calculation. You have too have a pic 999 for the
calculation and later move the result into the ZZZ picture.

//Christer O. Jonsson
```

#### ↳ Re: Numeric Edited Fields

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-08-11T16:45:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l4936$rhq$1@slb7.atl.mindspring.net>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```
A number of replies have talked about the fact that you can't use
numeric-edited fields in computations.  I did want to add one additional bit
of information on this.  It is possible to NOT explicitly move a numeric
edited field to a numeric field to use it in an arithmetic expression *IF*
you use the NumVal intrinsic function (which is probably NOT something that
a new COBOL student would come across).  The following is perfectly valid
(conforming) source code - assuming you have a compiler that supports the
latest ANSI/ISO Standard.

01  NumField-1   Pic S99v99   Value Zero.
01  NumEd-2      Pic  +999,999.99   Value Zero.
01  NumEd-3      Pic   zzz                 Value Zero.
   ...
*  do something to get non-zero values into NumEd-2.

Compute NumEd-3 NumField-1 = (Function NumVal (NumEd-2)  + 123.4) / 100
  On Size Error
         Display "something"
  Not On Size Error
         Display "something else"
 End-Compute

This shows that a numeric-edited field can ALWAYS be the receiving item of a
COMPUTE statement - and that it can also be used as a "sending" field when
it is used in the NumVal intrinsic function.

Having said this, it is OFTEN (possibly usually) appropriate to keep "two"
copies of numeric fields - one edited and one not.  Whether this is
appropriate depends on the application logic needed for your program.
```

##### ↳ ↳ Re: Numeric Edited Fields

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-08-11T18:22:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0108111722.71cd312e@posting.google.com>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com> <9l4936$rhq$1@slb7.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote 
> 
> 01  NumField-1   Pic S99v99   Value Zero.
…[15 more quoted lines elided]…
> 

*------------------

Bill, that's a REALLY NICE example...  I have had far too little
opportunity to use intrinsic functions at my client sites, and I
appreciate seeing exactly how they can be used in business.

Stephen
```

#### ↳ Re: Numeric Edited Fields

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-08-13T15:43:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9l8she$6i5$1@peabody.colorado.edu>`
- **References:** `<9l2slb$2gb$03$1@news.t-online.com>`

```

On 11-Aug-2001, "Stephan Wiesner" <stephan@stephanwiesner.de> wrote:

> I read that I can edit numeric fields like this:
> 01 myNumber Pic ZZZ.
…[6 more quoted lines elided]…
> Stephan

You can move a number to that field before it prints.  Is that what you want
to do?   I suspect you're talking about input, in which case you need to
edit by hand or use a function call.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
