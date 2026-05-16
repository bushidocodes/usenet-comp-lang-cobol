[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol - Data Exception (Conversion Data).

_6 messages · 5 participants · 2000-04_

---

### Re: Cobol - Data Exception (Conversion Data).

- **From:** "Eileen Preston" <epreston@lear.com>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM>`

```


>>> Peter E. C. Dashwood 04/01 8:53 pm >>>
 
Sorry, but I couldn't let this go...

docdwarf@clark.net wrote in message ...
>In article <8bng6o$11p$1@news.flashnet.it>,
>Gianluigi Angotti <giangol@tin.it> wrote:


>...A check which would work across all platforms I know of is:
>
…[9 more quoted lines elided]…
>DD
This almost certainly WON'T work across all platforms. (I'd be surprised if
it worked on ANY platform, and it is certainly NOT a solution to the
underlying problem).

It is predicated on the (I believe false) hope that moving an invalid packed
field to a non-packed target will NOT cause a data exception. In other
words, an 0C7 can only be raised during a PACK operation. (Maybe someone in
the NG who has access to a mainframe can confirm or deny whether this is the
current situation...?)


This will not work on a mainframe.  If DATO-NUM is invalid data (packed or not packed) there will be a sock seven (S0C7 data exception on a mainframe).

Also asking if a PIC X field is numeric will give a false answer IF the field is signed because a sign always is alpha in a PIC X field so doing the numeric check on ARE-TEST won't work on a signed field or if DATO-NUM was packed.

I've gotten enough calls in the gawd awful hours of the morning on this :D.


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itfoesgp6sn4o31k97onh283gfjvmkdmtc@4ax.com>`
- **References:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM>`

```
On Wed, 05 Apr 2000 15:40:08 -0400 "Eileen Preston" <epreston@lear.com> wrote:

:>>>> Peter E. C. Dashwood 04/01 8:53 pm >>>
 
:>Sorry, but I couldn't let this go...

:>docdwarf@clark.net wrote in message ...
:>>In article <8bng6o$11p$1@news.flashnet.it>,
:>>Gianluigi Angotti <giangol@tin.it> wrote:


:>>...A check which would work across all platforms I know of is:

:>>05  AREA-TEST     PIC X(5).
:>>05  AREA-TEST-NUM REDEFINES AREA-TEST PIC 9(5).

:>>...

:>>MOVE DATO-NUM TO AREA-TEST-NUM.
:>>IF AREA-TEST NOT NUMERIC
:>>    DISPLAY 'TUTTI DI FROMAGGIO!'.

:>This almost certainly WON'T work across all platforms. (I'd be surprised if
:>it worked on ANY platform, and it is certainly NOT a solution to the
:>underlying problem).

In which platform will a NUMERIC class test as above incorrectly succeed or
fail?

I think this must, by definition, work.

:>It is predicated on the (I believe false) hope that moving an invalid packed
:>field to a non-packed target will NOT cause a data exception.             

One cannot guarantee that such a move WILL fail.

It may fail, but it may not.

:>                                                              In other
:>words, an 0C7 can only be raised during a PACK operation. (Maybe someone in
:>the NG who has access to a mainframe can confirm or deny whether this is the
:>current situation...?)

And 0C7 CANNOT be raised during a pack operation.

Neither PACK nor UNPK require numeric operands.

:>This will not work on a mainframe.  If DATO-NUM is invalid data (packed or 
:>not packed) there will be a sock seven (S0C7 data exception on a mainframe).

Why?

How can a NUMERIC class test cause a numeric data exception? 

Makes the class test kind of useless, doesn't it?

:>Also asking if a PIC X field is numeric will give a false answer IF the field 
:>is signed because a sign always is alpha in a PIC X field so doing the numeric 
:>check on ARE-TEST won't work on a signed field or if DATO-NUM was packed.

Why do you consider that to be false?

It is a valid number.

:>I've gotten enough calls in the gawd awful hours of the morning on this :D.

I would like to see your example of a NUMERIC class test causing an 0C7.

Any such situation would be a bug in the compiler.
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nxSG4.16398$0o4.107844@iad-read.news.verio.net>`
- **References:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM>`

```
- note - I cannot tell where the quoting leaves off and the new text
begins so I re-quoted everything. -

In article <s8eb5e6f.072@UTAEMAIL.UTA.COM>,
Eileen Preston <epreston@lear.com> wrote:
>
>
…[36 more quoted lines elided]…
>I've gotten enough calls in the gawd awful hours of the morning on this :D.

Ms Preston... as I posted for Mr Dashwood, and have gotten no response, so
I will refer you to:

<http://x44.deja.com/[ST_rn=ps]/getdoc.xp?AN=606091440&search=thread&CONTEXT=954987552.337969155&HIT_CONTEXT=954987552.337969155&hitnum=15>

... in which 'that which will not work' is shown to compile, run and give
an accurate result.

DD
```

#### ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ciahm$77u$1@hermes.enternet.co.nz>`
- **References:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM>`

```
Thanks Eileen,

You confirmed what I suspected. I'll check out the dwarf's PMAP, but I think
there is a general consensus that this is NOT the way to do it...

Even if it does work (and DD seems sure it does) I still don't like it as a
"solution".

Your point about the CLASS test is also well taken and jogged my memory back
to the days of punched cards when we validated numeric input fields by
reading them into Alphanumeric fields and using the CLASS  AND SIGN tests as
follows:

if INPUT-FIELD is NUMERIC
              AND
   INPUT-FIELD IS POSITIVE
....
(Note no use of implied subjects ...this was banned on most installations in
New Zealand in the 60s as contributing to "unreadable code"...)



Pete.

Eileen Preston wrote in message ...
>>>> Peter E. C. Dashwood 04/01 8:53 pm >>>
>
…[16 more quoted lines elided]…
>>DD

>This will not work on a mainframe.  If DATO-NUM is invalid data (packed or
not packed) there will be a sock seven (S0C7 data exception on a mainframe).
>
>Also asking if a PIC X field is numeric will give a false answer IF the
field is signed because a sign always is alpha in a PIC X field so doing the
numeric check on ARE-TEST won't work on a signed field or if DATO-NUM was
packed.
>
>I've gotten enough calls in the gawd awful hours of the morning on this :D.
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cidb5$6r2$1@slb3.atl.mindspring.net>`
- **References:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM> <8ciahm$77u$1@hermes.enternet.co.nz>`

```
Most of the recent thread have shown the Procedure Division - but not the
data division related to this thread.  Let me show a couple of DIFFERENT
examples that came up earlier - and explain why they might have lead to
"confusion".

First, I *firmly* believe that *no* IBM compiler has ever (or ever will)
issue a S0C7 on an "IF NUMERIC" class test.  HOWEVER, there are some cases
that after performing this test on a "related" field, a S0C7 will/might
occur.

for the original question:

Assume:
  01  Group1.
        05  NumField-S   Pic S9(03) Packed-Decimal. (or on IBM S/390 Comp-3).
        05  NumField-N   Pic    9(03) Packed-Decimal.

If you do an
   If Group1 Numeric
class test, this absolutely, definitely, will *not* test whether or not
either NumField does or does not include numeric data.   I believe that
(although it is NON-standard - because the Standard doesn't allow a Numeric
test against a group item with elementary SIGNED fields) that IBM might
actually compile this - but it would not test whether the elementary item was
or was not a "valid" numeric PACKED field.

The other question concerned when moving a numeric data item to or from
another might cause a S0C7.  My memory is (at least with OS/VS COBOL - and
some settings of NUMPROC in the newer compilers) that SOME moves from/to
numeric fields include a "ZAP" (for sign repair) as well as a PACK/UNPACK.
If this is true, it would not be the PACK/UNPACK that gets the S0C7, but the
ZAP (zero and add packed). However, to the COBOL program it WOULD appear that
the MOVE created the S0C7.
```

##### ↳ ↳ Re: Cobol - Data Exception (Conversion Data).

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<unaH4.16472$0o4.108695@iad-read.news.verio.net>`
- **References:** `<s8eb5e6f.072@UTAEMAIL.UTA.COM> <8ciahm$77u$1@hermes.enternet.co.nz>`

```
In article <8ciahm$77u$1@hermes.enternet.co.nz>,
Peter E. C. Dashwood <dashwood@enternet.co.nz> wrote:
>Thanks Eileen,
>
…[4 more quoted lines elided]…
>"solution".

What actually *works*, Mr dashwood, and what one 'likes' are not always
the same... or what's a MOVE CORRESPONDING for?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
