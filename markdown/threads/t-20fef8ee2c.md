[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol (Move field using <corresponding> syntax) question

_15 messages · 9 participants · 2005-01_

---

### Cobol (Move field using <corresponding> syntax) question

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-16T01:23:46+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csbi13$4gk$1@mawar.singnet.com.sg>`

```
Hi,
I had a question and appreciate someone out there could help advise. Thanks 
in advance :-)

Actually, need to process an input file, extract the full record(based on 
condition) and output it to a flat file.
However, for all PACKED input field, need to output as ALHANUMERIC into the 
output file.

As the input file has a lot of fields, I was wondering if there is a way in 
which we can move the all the input file
fields to the output files without having to use the syntax <MOVE> to move 
each of the input field to the output field.

Heard that there is a syntax which can do that. It's something called 
<CORRESPONDING>

1) Can someone enlightented how this syntax can be used and how to code 
(Appreciate if can show an example) ?

2) In addition, does the above (1) syntax work if the input field is a 
PACKED and for the output field, I want it
    to be APLHA ?

Thanks in advance :-)
```

#### ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2005-01-15T17:57:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg>`

```
Example:

01  Input-Record.
        05  Input-Field-one                 pic s9(06)        comp-3.
        05  Input-field-two                  pic s9(06).
        05  Input-Field-three               pic  x(09).
01  Output-Record.
        05  Input-Field-one                 pic  x(06).
        05  Input-Field-two                 pic  x(06).
        05  Input-Field-three               pic  x(09).

Procedure Division.
        Move Corr Input-Record to Output-Record.
        ---- or ----
        Move Corresponding Input-Record to Output-Record.

But, it has some additional restrictions/nuances:
. You can/will get warning messages for all respective fields with no
    correspondence.
. Every field that you handle individually must now be qualified. Ex:
    Move 6 to Input-Field-one of Output-Record.
    This can be a PITA, but can be overcome by duplicate/redundant
    definitions. But, that also exposes the possibility of mismatched
    "duplicate/redundant" definitions.
. Probably more issues....

This is a basic example. Any/all syntax should be checked, and any
operation(s) should be tested/reviewed. I haven't used this in a long
time.

I'm sure others here will offer additions.

Thanks,

Gary Walker




"Rick" <leng1@bigfoot.com> wrote in message
news:csbi13$4gk$1@mawar.singnet.com.sg...
> Hi,
> I had a question and appreciate someone out there could help advise.
Thanks
> in advance :-)
>
> Actually, need to process an input file, extract the full record(based on
> condition) and output it to a flat file.
> However, for all PACKED input field, need to output as ALHANUMERIC into
the
> output file.
>
> As the input file has a lot of fields, I was wondering if there is a way
in
> which we can move the all the input file
> fields to the output files without having to use the syntax <MOVE> to move
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-01-15T21:46:40+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<coriu0h988gft177mpqr38o7mof2hs4qr7@4ax.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com>`

```
On Sat, 15 Jan 2005 17:57:08 GMT "The Family" <lgvwalk@swbell.net> wrote:

:>Example:

:>01  Input-Record.
:>        05  Input-Field-one                 pic s9(06)        comp-3.
:>        05  Input-field-two                  pic s9(06).
:>        05  Input-Field-three               pic  x(09).
:>01  Output-Record.
:>        05  Input-Field-one                 pic  x(06).
:>        05  Input-Field-two                 pic  x(06).
:>        05  Input-Field-three               pic  x(09).

:>Procedure Division.
:>        Move Corr Input-Record to Output-Record.
:>        ---- or ----
:>        Move Corresponding Input-Record to Output-Record.

:>But, it has some additional restrictions/nuances:
:>. You can/will get warning messages for all respective fields with no
:>    correspondence.

Is that how it works nowadays?

I don't remember error messages for unpaired fields.
```

###### ↳ ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-01-15T20:07:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oitiu0hbp7qcdgl7sq1ti2qig6u4mhe42n@4ax.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com> <coriu0h988gft177mpqr38o7mof2hs4qr7@4ax.com>`

```
On Sat, 15 Jan 2005 21:46:40 +0200, Binyamin Dissen
<postingid@dissensoftware.com> wrote:

>On Sat, 15 Jan 2005 17:57:08 GMT "The Family" <lgvwalk@swbell.net> wrote:
>
…[22 more quoted lines elided]…
>I don't remember error messages for unpaired fields.
Some compilers will issue an warning if NO match is found. COBOL/400
is one of them, and can also print a list of the matched fields
(compiler option) on the program listing.
Others may also do that.

RM/COBOL dos not issue any warning/error, and does not print the
matched fields.
Acucobol issues a warning but does not print matched fields either.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

_(reply depth: 4)_

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2005-01-15T13:20:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1105824045.207125.6970@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<oitiu0hbp7qcdgl7sq1ti2qig6u4mhe42n@4ax.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com> <coriu0h988gft177mpqr38o7mof2hs4qr7@4ax.com> <oitiu0hbp7qcdgl7sq1ti2qig6u4mhe42n@4ax.com>`

```
Message snipped
Frederico Fonseca and others wrote:

> >I don't remember error messages for unpaired fields.
> Some compilers will issue an warning if NO match is found. COBOL/400
…[13 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com

None of the COBOL standards have required or even suggested the issuing
of warning messages for mismatches.  There are many valid situations
where a full correspondance would be inappropriate.

As a thought, there may be a utility available that would do the job
quite simply without the need for a COBOL program at all.  DFSORT for
IBM mainframes would be a likely candidate and I think there are
several other such programs for other operating systems.  Though, if
you also wanted or needed to do validation, then COBOL would be a very
good choice.

Robert
Robert
```

###### ↳ ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2005-01-16T00:35:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oFiGd.15160$wi2.14275@newssvr11.news.prodigy.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com> <coriu0h988gft177mpqr38o7mof2hs4qr7@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
news:coriu0h988gft177mpqr38o7mof2hs4qr7@4ax.com...
> On Sat, 15 Jan 2005 17:57:08 GMT "The Family" <lgvwalk@swbell.net> wrote:
>
…[23 more quoted lines elided]…
>

Well, I guess it depends on the compiler, but the last time I used
corresponding(Q1,2004) on IBM Cobol/VSE, I seem to recall
some warnings. I could be wrong, or the warnings could have been
related to another condition of the corresponding option.

So, I'll concede that warning may/may not occur.

Thanks,

Gary Walker



> --
> Binyamin Dissen <bdissen@dissensoftware.com>
…[9 more quoted lines elided]…
> especially those from irresponsible companies.
```

##### ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-16T06:56:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9O-YX1aPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com>`

```
.    On  15.01.05
  wrote  lgvwalk@swbell.net (The Family)
     on  /COMP/LANG/COBOL
     in  UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com
  about  Re: Cobol (Move field using <corresponding> syntax) question


TF> . You can/will get warning messages for all respective fields with no
TF>     correspondence.

   It is probably not a "Warning", but a "Remark", since there is no  
danger to be warned about.

   I just checked the manual of Unisys' old ACOB ('74), which may  
issue diagnostics of class "R", i.e. Remark, indicating the line  
numbers of the matching subordinate data time pairs.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Der Amerikaner, der den Kolumbus zuerst entdeckte, machte eine bï¿½se Entdeckung. -G.C.Lichtenberg
```

##### ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-17T08:14:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csgo88$ikm$1@si05.rsvl.unisys.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com>`

```

"The Family" <lgvwalk@swbell.net> wrote in message
news:UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com...
> Example:
>
…[13 more quoted lines elided]…
>
I'd be a whole lot more comfortable if Input-field-one and Input-field-2
were described as numeric.  While there are rules in the standard that cover
the MOVE from PIC S9(6) to PIC X(6), they represent a number of exceptions
(the sign isn't MOVEd, for example), and ensuring that the results are
intuitive is better served by a numeric destination whose descriptions
explicitly match the desired results.

PICTURE 9(6) USAGE DISPLAY produces results compatible with PIC X(6); those
results just happen to be restricted to the set of numeric digits.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-17T17:24:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sxSGd.911360$lR6.137732@news.easynews.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com> <csgo88$ikm$1@si05.rsvl.unisys.com>`

```
Actually, my guess is that even though the original request was for an 
"alphanumeric" output field, that probably a numeric-edited field would work 
best, e.g.

  Pic  +9(6).

(and Pic +9(6).99  - type pictures if any input would be of that type).

It is just a guess, but it normally when doing this type of "conversion" that is 
the type of output that is desired.
```

###### ↳ ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "The Family" <lgvwalk@swbell.net>
- **Date:** 2005-01-17T17:37:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yJSGd.2811$2e7.1234@newssvr12.news.prodigy.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <UPcGd.14555$wi2.6604@newssvr11.news.prodigy.com> <csgo88$ikm$1@si05.rsvl.unisys.com>`

```

Yeah, it's just an example. But, you're right, typically a positively
sign move like this, using the number +123456, would produce
"12345F" as output. Then, someone would deduce that "F" was
merely "C6", and they'd fix it.

Error, or not, the point to the OP was that the MC will merely
function as the many single move's it replaces. But, the oversight
you mention, was not intentional.

Thanks,

Gary Walker


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:csgo88$ikm$1@si05.rsvl.unisys.com...
>
> "The Family" <lgvwalk@swbell.net> wrote in message
…[18 more quoted lines elided]…
> were described as numeric.  While there are rules in the standard that
cover
> the MOVE from PIC S9(6) to PIC X(6), they represent a number of exceptions
> (the sign isn't MOVEd, for example), and ensuring that the results are
…[3 more quoted lines elided]…
> PICTURE 9(6) USAGE DISPLAY produces results compatible with PIC X(6);
those
> results just happen to be restricted to the set of numeric digits.
>
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-01-15T17:57:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l0miu0hkdldhda703o7hf901hl3o8k1eie@4ax.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg>`

```
On Sun, 16 Jan 2005 01:23:46 +0800, "Rick" <leng1@bigfoot.com> wrote:

>Hi,
>I had a question and appreciate someone out there could help advise. Thanks 
…[16 more quoted lines elided]…
>(Appreciate if can show an example) ?
01 g1.
   05 var1 pic x(10) value "abcdef".
   05 var2 pic S9(9)V99 comp-3 value -12345.99.

01 G2
   05 var2-txt pic x(10) value "  var2=".
   05 var2 pic S9(9)V99 sign leading separate.
   05 var1-txt pic x(10) value "  var1=".
   05 var1 pic x(10).

...
  move corr g1 to g2
  display g2

output = "  var2=   -00001234599  var1=   abcdef"
>
>2) In addition, does the above (1) syntax work if the input field is a 
>PACKED and for the output field, I want it
>    to be APLHA ?
If you do as per example you may not need it to be alpha.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** Howard Abrams <habrams@charter.net>
- **Date:** 2005-01-15T13:35:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41E98C91.4070201@charter.net>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg>`

```
Not knowing what machine you are running on, I can suggest that the 
"corresponding" move should work for at least part of what you need.  It 
will move from packed to unpacked on IBM mainframe Cobol as long as you 
define the pic correctly.  Once you have it unpacked, your only problem 
will be to verify the sign on the receiving field. For instance, "PIC 
S9(5) COMP-3" to "PIC 9(5)" will unpack the field, but you may need to 
clean up the implied positive or negative sign with another program.
Rick wrote:
> Hi,
> I had a question and appreciate someone out there could help advise. Thanks 
…[25 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-16T06:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9O-XOQo9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <41E98C91.4070201@charter.net>`

```
.    On  15.01.05
  wrote  habrams@charter.net (Howard Abrams)
     on  /COMP/LANG/COBOL
     in  41E98C91.4070201@charter.net
  about  Re: Cobol (Move field using <corresponding> syntax) question


HA> to verify the sign on the receiving field. For instance, "PIC
HA> S9(5) COMP-3" to "PIC 9(5)" will unpack the field, but you may need
HA> to clean up the implied positive or negative sign with another
HA> program.

   Why another program? Just define the receiving variable also with a  
sign, i.e. not PIC 9(5) but PIC S9(5).


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Hinlï¿½nglicher Stoff zum Stillschweigen. -G.C.Lichtenberg
```

#### ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-16T20:27:46+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csdk4q$ld4$1@reader01.singnet.com.sg>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg>`

```
Hi,
Thanks all for the advice given  :-)

By the way, my concern now is that if my o/p file declaration "length" is 
different from
my i/p file "length", will the syntax "corresponding" still work as when I 
o/p, I need
to unpack those i/p field that were declare as pack to o/p as alphan, 
something
like o/p as 0000123456.88+   . From here, length declaration will definitely 
be different.

In addition, the input file has a lot of fields inside and if use the syntax 
MOVE to move
the input field 1 by 1 to the o/p field, coding will be long and 
inefficient.

Hope the syntax <corresponding> will address my 2 concern above.





"Rick" <leng1@bigfoot.com> wrote in message 
news:csbi13$4gk$1@mawar.singnet.com.sg...
> Hi,
> I had a question and appreciate someone out there could help advise. 
…[25 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol (Move field using <corresponding> syntax) question

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-01-16T15:01:44+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9pku0l9jbshj5bphp13rv3o2pjp5j26d8@4ax.com>`
- **References:** `<csbi13$4gk$1@mawar.singnet.com.sg> <csdk4q$ld4$1@reader01.singnet.com.sg>`

```
On Sun, 16 Jan 2005 20:27:46 +0800 "Rick" <leng1@bigfoot.com> wrote:

:>By the way, my concern now is that if my o/p file declaration "length" is 
:>different from
:>my i/p file "length", will the syntax "corresponding" still work as when I 
:>o/p, I need
:>to unpack those i/p field that were declare as pack to o/p as alphan, 
:>something
:>like o/p as 0000123456.88+   . From here, length declaration will definitely 
:>be different.

MOVE CORRESPONDING is simply a shortcut way to specify a MOVE for each field
that is in both records. It will follow the rules for simple MOVE, including
converting packed to display, truncating/padding, etc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
