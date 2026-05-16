[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# need help...!

_5 messages · 5 participants · 1998-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### need help...!

- **From:** Quan Ngo <le_spaceBoy@usa.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36385DC2.C799703E@usa.net>`

```
hi,

this is the data I use as input from a file...

06155267NOVA SCOTIA GOVERNMENT   CNDBG45320250012567
08119978POTATO COMPANY P.E.I.            CNDCS01230090102299
12183390THE YANKEE DOODLE                 USAGL98761000003679
14154433NATIONAL DEFENSE                    CNDBG45320500012567

and this is how the output comes out...

day  order #    client name
country  product #   quantity   unit price
06   5267N?   VA SCOTIA GOVERNMENT   CN     DBG       453202
500      $12,567.0
80   978PO4   ATO COMPANY P.E.I.          CDN     CS0        123009
010      $22,99.12
01   90THE0   YANKEE DOODLE             USAG      L98
761000      003      $67,91.40
19   3NATI?   NAL DEFENSE                 CNDBG      453
205000      125      $67,17.01

it seems like the data is sort of shifted to the left...
I have no idea why it's doing that.

can anyone help me...!
```

#### ↳ Re: need help...!

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71attb$2l9$1@news.megsinet.net>`
- **References:** `<36385DC2.C799703E@usa.net>`

```
I think what you're saying is that the FIRST record is read correctly, but subsequent records are shifting to the left. This would imply that you are reading in one less character than the file actually has. So, if the record length is 80, you might be reading in 79 bytes. 

The first thing I would check is for Line-feed/Carriage-return problems. Depending on your environment, your file may have one extra character or two extra characters at the end of each line.

Try the LINE SEQUENTIAL option and see if things change.

- Darius Cooper

    Quan Ngo wrote in message <36385DC2.C799703E@usa.net>...
    hi, 
    this is the data I use as input from a file... 

    06155267NOVA SCOTIA GOVERNMENT   CNDBG45320250012567 
    08119978POTATO COMPANY P.E.I.            CNDCS01230090102299 
    12183390THE YANKEE DOODLE                 USAGL98761000003679 
    14154433NATIONAL DEFENSE                    CNDBG45320500012567 

    and this is how the output comes out... 

    day  order #    client name                                        country  product #   quantity   unit price 
    06   5267N?   VA SCOTIA GOVERNMENT   CN     DBG       453202      500      $12,567.0 
    80   978PO4   ATO COMPANY P.E.I.          CDN     CS0        123009      010      $22,99.12 
    01   90THE0   YANKEE DOODLE             USAG      L98         761000      003      $67,91.40 
    19   3NATI?   NAL DEFENSE                 CNDBG      453         205000      125      $67,17.01 

    it seems like the data is sort of shifted to the left... 
    I have no idea why it's doing that. 

    can anyone help me...!
```

#### ↳ Re: need help...!

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981029031210.24005.00000789@ng-fd1.aol.com>`
- **References:** `<36385DC2.C799703E@usa.net>`

```
At the very least your input data is one character shorter than your internal
record length definition.  On line one you are getting one extra character from
the next line, on line two you are picking up two characters from the next
(third line), on line three, three extra characters from the next line (fourth
line).

But you are pulling a rabit out of the hat when you get your COBOL to display
something like
  $12,567.0
on one line and then
   $22,99.12
on the next.  You may be deserving a reward for that. It is a bizarritude for
sure.

That dollar amount field in unit price column is getting disrupted by the
presence of the carriage return (or carriage return plus line feed). If only
you could see it before it is munged into abstentia by the edited field
function, it might look something like this.

    $12,567.[CR]0
    $22,99[CR].12
    $67,9[CR]1.40
    $67,[CR]17.01


It is a fair guess that you have atleast one more record in the input which, in
fact, commences with the value 1701 (you did not show that record but our all
seeing eyes can see beyond the net right into your datafile - that happens
close to holloween). That is a guess, but it is unlikely that the next four
ciphers would be legible if they were garbage (statistically speaking, you
understand).

There is a technique for getting COBOL on PCs to chop the carriage return  out
of the buffer before handing it to you. You ought to just look up the file
definition and OPEN verb specification in your manual.
Be patient, you'll find the part you need buried somewhere in the description
of processing on sequential files.

It is clear from your output that you are defining the record one byte too
long, when including the CR. Your actual working area needs to be two shorter
then it is. Add one back in if you can't fathom how to get rid of the CR.

Your Order # column is looking something like this, compensting for the current
strangeness, ([SP] means a single space).

  read        printed
5267NO      5267N?
978POT       978PO4 
90THE[SP]  90THE0   
3NATIO      3NATI? 

Input ASCII   displays as
----------------   -------------
 alpha-O         ?                 (79 as 63: x4F as x3F)
 alpha-T          numeric-4  (84 as 52: x54 as x34)
 space             numeric-0  (32 as 48: x20 as x30)
 alpha-O         ?                 (79 as 63: x4F as x3F)

(my sincerest apologies if that does not display well on you mail reader
screen).

So the issue here is really just the high order nibble of the low order byte. 

In a COBOL definition S9(n) field, that nibble carries the sign. So an
intermediate field or the detail field within the print line has a PIC S9(5)
defintion.

COBOL is friendly, it allows you to move character data to a numeric field. If
the target numeric has a sign, the compiler forces the sign to positive

4 -> 3
5 -> 3
2 -> 3
4 -> 3

Noice that in contrast, the higher order decimal positions do not have their
sign zone coerced to x3z. So the nonumic data in those 9-field positons do not
get mangled. It is good to learn this lesson. In display fields this is ugly,
but it such a field were used for calculation the results could cause the
program to halt, or worse proceed forward with undefines results.

Generally, do not use signed fields on output, unless you code SIGN IS SEPARATE
CHARACTER.

Your program is not paying any attention to the third position of the input
record. And in a related matter, the day figure does not make sense,are you
showing us what is actually on the file and printout

The inconsistencies

seems
like
read -> displayed
06   -> 06
81   -> 80
18   -> 01
54   -> 19

In the four input lines you present, there is no '80' sequence.  So you either
misled us a bit, or you have a non-trivial program weakness in the handling of
the 'day' information.

Do you ever move a zero, inproperly, TO the INPUT record area?

Perhaps your day field is three bytes long, but you are only looking at the
first two bytes, or else an intermediate field is two bytes.

Did you lift this code and report directly form the program and run? Or did you
retype a portion of it. (The result seems to imply record 080 and a record 170
are present, but not listed).

Some of this is guess work (maybe most of it), but can't do much more until you
post the code. Hope this is atleast some help.

Best Wishes,









Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: need help...!

- **From:** davidafish@my-dejanews.com
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<719vnh$32c$1@nnrp1.dejanews.com>`
- **References:** `<36385DC2.C799703E@usa.net>`

```
What does your record layout look like? What type of data file is this?  What
is the source of the data?  Please provide more information for analysis.

In article <36385DC2.C799703E@usa.net>,
  Quan Ngo <le_spaceBoy@usa.net> wrote:

>
> --------------6D5E1DD45B78A5207A9F165F
…[28 more quoted lines elided]…
> can anyone help me...!

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: need help...!

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<718mqh$1dg_001@news.netdirect.net>`
- **References:** `<36385DC2.C799703E@usa.net>`

```
In article <36385DC2.C799703E@usa.net>, Quan Ngo <le_spaceBoy@usa.net> wrote:
+
+
+hi,
+
+this is the data I use as input from a file...
+
+06155267NOVA SCOTIA GOVERNMENT   CNDBG45320250012567
+08119978POTATO COMPANY P.E.I.            CNDCS01230090102299
+12183390THE YANKEE DOODLE                 USAGL98761000003679
+14154433NATIONAL DEFENSE                    CNDBG45320500012567
+
+and this is how the output comes out...
+
+day  order #    client name
+country  product #   quantity   unit price
+06   5267N?   VA SCOTIA GOVERNMENT   CN     DBG       453202
+500      $12,567.0
+80   978PO4   ATO COMPANY P.E.I.          CDN     CS0        123009
+010      $22,99.12
+01   90THE0   YANKEE DOODLE             USAG      L98
+761000      003      $67,91.40
+19   3NATI?   NAL DEFENSE                 CNDBG      453
+205000      125      $67,17.01
+
+it seems like the data is sort of shifted to the left...
+I have no idea why it's doing that.
+
+can anyone help me...!
+
Not unless you post your source code, too. Without seeing your
record descriptions and the code that moves data from the input
record to the output record, the only thing anyone can tell you 
is that your program has a mistake in it somewhere.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
