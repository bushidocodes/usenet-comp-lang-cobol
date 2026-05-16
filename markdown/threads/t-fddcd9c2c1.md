[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is the length of a picture string always equal to the length of the string DISPLAYed?

_17 messages · 7 participants · 2006-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-14T21:31:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s_rIf.1245$n67.995@edtnps89>`

```
    The context here is writing a tool to perform analysis on COBOL source 
code. Assume that when I load the source code into memory, I do some 
preprocessing so that picture strings like "X(6)" never occurs. For example, 
perhaps I will always expand repeat-factors so in some earlier stage so that 
the later analysis stages see "XXXXXX" instead of "X(6)".

    Suppose you have a picture string like "$$,$$9.99" which contains 9 
characters. Regardless of what data the item with this picture string 
contains, when I try to DISPLAY it, the output displayed always consists of 
9 characters as well, e.g. "  $128.00", where the space character is 
inserted to pad the output string to the correct length.

    Is this always true (assuming the COBOL compiler complies with the 85 
standard), or does there exist a picture string that one could write where 
the length of the output does not match the length of the string?  Again, 
recall that the picture strings will never, at this point, contain 
repeat-factors, so although "X(6)" is technically a picture string of length 
4, the analysis module will actually see "XXXXXX", which is a picture string 
of length 6, and its naive(?) algorithm of assuming that the picture length 
is equal to the output length, and concluding that the output will be of 
length 6 is correct.

    - Oliver
```

#### ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-14T14:41:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89>`

```
On Tue, 14 Feb 2006 21:31:04 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>    Is this always true (assuming the COBOL compiler complies with the 85 
>standard), or does there exist a picture string that one could write where 
…[6 more quoted lines elided]…
>length 6 is correct.

Why is it important that the picture is XXXXXX instead of X(6)?    The
answer in either case is the same.    It is always true.   We have to
jump through hoops to compress our output for export to programs that
expect delimited data.
```

##### ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-14T21:52:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gisIf.1249$n67.564@edtnps89>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com...
>
> Why is it important that the picture is XXXXXX instead of X(6)?

    Because the string "X(6)" has 4 characters in it ('X', '(', '6', and 
')'), and yet it will produce an output of length 6, which will cause the 
naive formula of "length of output = length of picture string" to fail.

    - Oliver
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-14T14:59:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com> <gisIf.1249$n67.564@edtnps89>`

```
On Tue, 14 Feb 2006 21:52:12 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>> Why is it important that the picture is XXXXXX instead of X(6)?
>
>    Because the string "X(6)" has 4 characters in it ('X', '(', '6', and 
>')'), and yet it will produce an output of length 6, which will cause the 
>naive formula of "length of output = length of picture string" to fail.

Then S9999v99 also fails.
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

_(reply depth: 4)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-14T22:16:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9FsIf.1252$n67.399@edtnps89>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com> <gisIf.1249$n67.564@edtnps89> <ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com...
> On Tue, 14 Feb 2006 21:52:12 GMT, "Oliver Wong" <owong@castortech.com>
> wrote:
…[7 more quoted lines elided]…
> Then S9999v99 also fails.

    Indeed it does. Thanks, this is exactly the kind of answer I was looking 
for, and I now know that I need to refine my algorithm a bit. Is there 
anything else that acts like 'V' in this manner?

    - Oliver
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-14T22:24:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xMsIf.11475$6Q3.4281@fe07.news.easynews.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com> <gisIf.1249$n67.564@edtnps89> <ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com> <9FsIf.1252$n67.399@edtnps89>`

```
S may or may not fail. (Some compilers show an "over-punch" and others show the 
sign separately on a DISPLAY)

What a specific compiler does with P is another question.

Remember (extension) usages like COMP-1 and COMP-2 with NO picture clause.

I think (but an not certain) that some compilers will show "slack" bits/bytes - 
when SYNC or OCCURS causes these to "exist".

Note particluarly GR(1) of the DISPLAY statement in the '02 Standard (and this 
has ALWAYS been true)

"Any conversion of data required between literal-1 or the data item referenced 
by identifier-1 and the hardware device is defined by the implementor."

The bottom-line is that this is NOT "portable" behavior (nor does it need to 
be - to be ANSI/ISO conforming)
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-15T10:33:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dsv01c$6kb$1@reader2.panix.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <gisIf.1249$n67.564@edtnps89> <ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com> <9FsIf.1252$n67.399@edtnps89>`

```
In article <9FsIf.1252$n67.399@edtnps89>,
Oliver Wong <owong@castortech.com> wrote:
>
>"Howard Brazee" <howard@brazee.net> wrote in message 
…[14 more quoted lines elided]…
>anything else that acts like 'V' in this manner?

I'm not sure if it 'acts like 'V' in this manner'... but how about 
something like:

01  FLD1     PIC X(500)    VALUE SPACES.
01  STRTPOS  PIC 9(4) COMP VALUE 0.
01  LNGTH    PIC 9(4) COMP VALUE 0

...
IF condition
    MOVE    stuff   TO FLD1
    COMPUTE STRTPOS =  (computation01)
    COMPUTE LNGTH   =  (computation02)
    DISPLAY FLD1(STRTPOS:LNGTH)
END-IF.

DD
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-15T07:03:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62d6v1dfs6oj8q3l59h25ctkfgjm5htir7@4ax.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <6ij4v11u3rbh1dn38oebo64c2nkrasb5it@4ax.com> <gisIf.1249$n67.564@edtnps89> <ulk4v1h7igot6d4h91eolmahqiikc72co4@4ax.com> <9FsIf.1252$n67.399@edtnps89>`

```
On Tue, 14 Feb 2006 22:16:37 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>> Then S9999v99 also fails.
>
>    Indeed it does. Thanks, this is exactly the kind of answer I was looking 
>for, and I now know that I need to refine my algorithm a bit. Is there 
>anything else that acts like 'V' in this manner?

Here's some real code:

 01  PASSED-DBCONV-RECORD.                                      
     02  PASSED-DBCONV-DISPLAY-DBKEY.                           
      03  PASSED-DBCONV-PAGE     PIC X(08).                     
      03  PASSED-DBCONV-PAGE-N   REDEFINES PASSED-DBCONV-PAGE   
                                                                
                                 PIC 9(08).                     
      03  PASSED-DBCONV-DASH     PIC X(01).                     
      03  PASSED-DBCONV-POS      PIC X(03).                     
      03  PASSED-DBCONV-POS-N    REDEFINES PASSED-DBCONV-POS    
                                                                
                                 PIC 9(03).                     
     02  PASSED-DBCONV-X.                                       
      03  FILLER                 PIC X(4).                      
      03  PASSED-DBCONV-DBKEY    PIC S9(08) COMP.
```

#### ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-14T15:09:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dstnvd$db3$1@si05.rsvl.unisys.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89>`

```

"Oliver Wong" <owong@castortech.com> wrote in message 
news:s_rIf.1245$n67.995@edtnps89...

>    Is this always true (assuming the COBOL compiler complies with the 85 
> standard), or does there exist a picture string that one could write where 
> the length of the output does not match the length of the string?

No, it is not always true.

Certainly for "P" the answer is "no", and the same is true for "V" (which 
never occupies space in the datum).

Whether "S" takes up a character or not is dependent both on the presence or 
absence of the SIGN SEPARATE clause and how the implementor represents signs 
in that particular USAGE.

And in '02 COBOL, whether a currency-sign in the datum and a currency-symbol 
in the PICTURE clause occupy the same space is dependent on whether they're 
the same length.  You can declare, say, "L" as the currency SYMBOL denoting, 
say, "GBP", and use "L" as a floating insertion editing symbol.  In this 
case I'd suggest, presuming all the other characters in the PICTURE have a 
one-to-one correspondence to the datum, the datum will be two characters 
longer than the PICTURE.

So I would suggest that presuming it is Universally and Eternally True that 
the PICTURE character string is the same length as the USAGE DISPLAY datum 
it descrkbes is a presumption likely to get you into a fair amount of hot 
water.

    -Chuck Stevens
```

##### ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-02-15T13:45:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gGIf.48157$dW3.25422@newssvr21.news.prodigy.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <dstnvd$db3$1@si05.rsvl.unisys.com>`

```
2/15/06

While not a factor at the elementary item level (where the PICTURE and USAGE
clauses are found) , the size of a group item can vary based on an OCCURS
DEPENDING ON and the presence/absence of an ODOSLIDE-like compiler
directive.

Hmm, come to think of it, USAGE can occur at the group-item level, affecting
all the elementary items therein. But this sounds like the only usage in
which you are interested is DISPLAY.

I have some old software available free at the flexus Download page at
http://www.flexus.com/download.html  which might help:

COBDATA.ZIP contains a tutorial on COBOL data types which gives the storage
requirements for most of the PICTURE/USAGE combinations available (both text
and - I believe - rich text).

COBFD.ZIP includes a piece of MS-DOS software which will scan a copylib or
source file and produce a report file (text) showing the size of every
elementary item found, right next to its PICTURE and USAGE. Maybe that would
help you identify other circumstances in which "actual-size NOT EQUAL
number-of-chars-in-picture"  (WARNING: This is really old; first posted in
1994, I have been threatening to update it since only about 1995).

MCM
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T14:14:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wHGIf.3042$_62.820@edtnps90>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <dstnvd$db3$1@si05.rsvl.unisys.com> <3gGIf.48157$dW3.25422@newssvr21.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:3gGIf.48157$dW3.25422@newssvr21.news.prodigy.com...
> I have some old software available free at the flexus Download page at
> http://www.flexus.com/download.html  which might help:
…[5 more quoted lines elided]…
> and - I believe - rich text).

    Thanks, this tutorial in particular will probably be very helpful to me.

    - Oliver
```

#### ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T14:14:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3HGIf.3041$_62.2182@edtnps90>`
- **References:** `<s_rIf.1245$n67.995@edtnps89>`

```
    Thanks everyone; it sounds like I still have a lot to learn about COBOL.

    So it sounds like the bottom line is that the length of the displayed 
string is compiler-dependent, and there isn't much I can do to make any real 
predictions about what the output might be in the most general cases.

    I was initially interested in trying to find picture strings which 
describe the format of group elements. For example:

01 GroupA
  02 ElementB PIC X(4)
  02 ElementC PIC X(10)

    I could say that GroupA is "like" a PIC X(14), but I can see now that 
there are several cases where it won't be possible to do this.

    - Oliver
```

##### ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-15T07:14:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dsvggl$1fb8$1@si05.rsvl.unisys.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <3HGIf.3041$_62.2182@edtnps90>`

```
Historically group items have been treated as alphanumeric data items large 
enough to contain the aggregate lengths of the elementary items within them. 
In order to figure out how long a group is, it is necessary to figure out 
how long each elementary item is, and also to take into account any slack 
bits that might result from implementation-defined alignment and 
synchronization requirements.

So yes, to figure out how long a group item is you have to figure out how 
long the data spaces occupied by its subordinate elementary items are, and 
that's not simply a matter of counting characters in the PICTURE 
character-string.   That's not opinion, that's the result of a fair amount 
of  experience in COBOL compiler development and support, more specifically, 
working with data-declaration-entry parsers in general and PICTURE clause 
parsers in particular.

        -Chuck Stevens

<top post, no more below>


"Oliver Wong" <owong@castortech.com> wrote in message 
news:3HGIf.3041$_62.2182@edtnps90...
>    Thanks everyone; it sounds like I still have a lot to learn about 
> COBOL.
…[15 more quoted lines elided]…
>    - Oliver
```

#### ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-02-15T14:00:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11v722an520rv72@news.supernews.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89>`

```
Oliver Wong wrote:
>    The context here is writing a tool to perform analysis on COBOL
> source code. Assume that when I load the source code into memory, I
…[20 more quoted lines elided]…
>    - Oliver

Surely you don't mean to decompose PIC X(30000) into PIC XXXXXXXX...... 
(pant, pant, whew!) XXX.

I don't know what the limit on the size of a picture string is, but I'm 
pretty sure it's less than 30,000 characters!
```

##### ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-15T20:16:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S_LIf.3106$_62.2327@edtnps90>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <11v722an520rv72@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:11v722an520rv72@news.supernews.com...
> Oliver Wong wrote:
>>    The context here is writing a tool to perform analysis on COBOL
…[10 more quoted lines elided]…
> pretty sure it's less than 30,000 characters!

    When emulating the behaviour of a typical compiler, I don't actually 
place a limitation on the size of a picture string, so the decomposition 
would indeed happen as you described.

    I'm not concerned with checking the validity of the COBOL source code 
I'm going to be processing, but merely of being to do analysis on COBOL 
source code which is already known to be valid.

    - Oliver
```

##### ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-15T12:28:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt02t7$1qde$1@si05.rsvl.unisys.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <11v722an520rv72@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:11v722an520rv72@news.supernews.com...

> Surely you don't mean to decompose PIC X(30000) into PIC XXXXXXXX...... 
> (pant, pant, whew!) XXX.
>
> I don't know what the limit on the size of a picture string is, but I'm 
> pretty sure it's less than 30,000 characters!

It was 30 characters up through the '85 standard; it was increased to 50 in 
'02.

For numeric data items, the '74 and '85 standards limited the number of 
significant digits described by the the PICTURE character-string to the 
range 1 through 18; the '02 standard increased the upper limit requirement 
to 31.

The maximum size of an elementary alphanumeric data item isn't specified; 
however, the practical upper limit for '85 COBOL is represented by a PICTURE 
character string containing a leading "X(", twenty-seven instantiations of 
the character "9", and a trailing ")".  The corresponding '02 data item 
could have forty-seven instantiations of "9" between the parens.  Both 
represent data items that are rather larger than the strings describing them 
in the PICTURE clause.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Is the length of a picture string always equal to the length of the string DISPLAYed?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-15T20:46:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QqMIf.59285$Ak4.27882@fe09.news.easynews.com>`
- **References:** `<s_rIf.1245$n67.995@edtnps89> <11v722an520rv72@news.supernews.com> <dt02t7$1qde$1@si05.rsvl.unisys.com>`

```
It may be worth noting (given what Oliver has stated previously) that there are 
compilers with the following extensions:

1) Picture clauses LONGER than that allowed in the Standards ('85 or '02)

2) Numeric items longer than 18 (or 31) digits.

What Chuck states is true for the Standard - but certainly NOT true for all 
implementations (i.e. larger, not smaller values are allowed)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
