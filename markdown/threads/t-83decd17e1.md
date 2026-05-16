[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Move text to num problem

_5 messages · 4 participants · 2007-01_

---

### Move text to num problem

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2007-01-03T13:19:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2007.01.03.20.19.38.644379@starband.net>`

```
I am having a problem and it does not seem to make sense to me because I
didn't THINK there should be a difference.
 
Consider the following:
pp 5655-G53 IBM Enterprise COBOL for z/OS and OS/390 3.2.0

01  Buffer-Text.
  05  interim stuff
  05  Buffer-Text-48-52.
    10  Buffer-Text-40-50   Pic x(3).
    10  Filler              Pic x(2).
  05  trailing stuff of 80 byte "card"
 
01  Variables.
  05  stuff
  05  No-9  Pic 9(9).
  05  more stuff

If version = 115
  Move Buffer-Text-48-52 to No-9
  ...
Else
  Move Buffer-Text-48-50 to No-9
  ...
End-if.

Now the move with the elementary item works "correctly" and fills
in the zeros in the zoned numeric, but the move of the group item does not.

Test1 the incoming data is version 115 and 48-52 is 00004
and No-9 ends up with '00004    '
 
Test2 the incoming data is version 110 and 48-50 is 004 (48-52 is '004 L')
and No-9 ends up with '000000004'

It seems to me that group item -48-52 should be treated the same as PIC
x(5) and should populate No-9 correctly.  If this is the case I will
contact IBM and gripe.

Thanks, 
Chris
Senior Software Engineer, CA, inc
Always remember, you are unique...just like everyone else.
```

#### ↳ Re: Move text to num problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-01-03T20:31:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<doUmh.208590$jO5.196868@fe06.news.easynews.com>`
- **References:** `<pan.2007.01.03.20.19.38.644379@starband.net>`

```
From,
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR31/6.2.24.6

" group move is treated as though it were an alphanumeric-to-alphanumeric 
elementary move ..."

while from
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR31/6.2.24.2

(for elementary moves)

"When the receiving field is:  ...
    Numeric or numeric-edited: ...

  When the category of the sending item is alphanumeric,  alphanumeric-edited, 
national, or national-edited, the data is moved  as if the sending item were 
described as an unsigned integer. "
```

##### ↳ ↳ Re: Move text to num problem

- **From:** Christopher Pomasl <pomasl-NOSpam@starband.net>
- **Date:** 2007-01-03T14:15:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2007.01.03.21.15.02.689103@starband.net>`
- **References:** `<pan.2007.01.03.20.19.38.644379@starband.net> <doUmh.208590$jO5.196868@fe06.news.easynews.com>`

```
#@$^$^#%&#&

I was afraid of that.
How does this compare to what the COBOL spec states?  Or does it?

Thanks for looking that up for me (or at least knowing where it was).  I
guess I need to further refine my redefines.

Chris

On Wed, 03 Jan 2007 20:31:05 +0000, William M. Klein wrote:

> From,
>    http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR31/6.2.24.6
…[14 more quoted lines elided]…
> described as an unsigned integer. "
```

#### ↳ Re: Move text to num problem

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-01-03T13:50:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<na4op2t9norhoqfei90vbul54tc1aqd77b@4ax.com>`
- **References:** `<pan.2007.01.03.20.19.38.644379@starband.net>`

```
On Wed, 03 Jan 2007 13:19:41 -0700, Christopher Pomasl
<pomasl-NOSpam@starband.net> wrote:

>It seems to me that group item -48-52 should be treated the same as PIC
>x(5) and should populate No-9 correctly.  If this is the case I will
>contact IBM and gripe.

I have been fooled by this as well.   Group items aren't quite the
same as alphabetic items.   Obviously you can do a redefine though.
```

#### ↳ Re: Move text to num problem

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2007-01-03T21:23:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-NidnRXDDpd1gwHYnZ2dnUVZ8qeknZ2d@pipex.net>`
- **In-Reply-To:** `<pan.2007.01.03.20.19.38.644379@starband.net>`
- **References:** `<pan.2007.01.03.20.19.38.644379@starband.net>`

```
Top post:

'Interesting' code. That's all I would say. Interesting.

Regards

Michael

Christopher Pomasl wrote:
> I am having a problem and it does not seem to make sense to me because I
> didn't THINK there should be a difference.
…[46 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
