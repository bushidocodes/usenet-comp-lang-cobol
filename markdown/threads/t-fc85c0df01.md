[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copy replacing

_10 messages · 6 participants · 1999-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Copy replacing

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38307ECF.B5AFE62@NOSPAMhome.com>`

```
Sometimes we need to convert a file from an old format to a new one. 
The standard procedure is to create a new copy member for the new file
format, changing as few field names as possible, as they will be used
in  the programs using it.

So we have
01   MY-FILE-NAME.
     05   TT-FIELD-1     PIC X(05).
     05   TT-FIELD-2     PIC X(20).
      etc

This is when we would like to use a COPY REPLACING TT- BY TTOLD- for the
conversion program, but we end up making a copy of the copy member and
editing that REPLACING by hand.

Are we going to have a more direct way of doing this simple editing
function ?
```

#### ↳ Re: Copy replacing

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com>`

```
It already exists in modern versions of Cobol.

In article <38307ECF.B5AFE62@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes
>Sometimes we need to convert a file from an old format to a new one. 
>The standard procedure is to create a new copy member for the new file
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Copy replacing

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80rtug$csc$1@starburst.uk.insnet.net>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk>`

```
Yes but not very usefully for existing code.

You have to define the replaceable part as something like (TT) I think i.e..
01 MY-FILE-NAME.
     05  (TT)-FIELD-1   PIC X(05).
     05  (TT)-FIELD-2   PIC X(20).

You ALWAYS have to use COPY REPLACING.
E.g. either
    REPLACING ==(TT)== BY ==TT==
or
    REPLACING ==(TT)== BY ==TTOLD==

However I think it is worthwhile if you can change all places where the copy
book is used.   I wish we could have found the time.

Rick


Alistair Maclean <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk...
> It already exists in modern versions of Cobol.
>
…[27 more quoted lines elided]…
> People are like teabags - you have to put them in to hot water before you
find
> out how strong they are.
```

###### ↳ ↳ ↳ Re: Copy replacing

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38319719.C07BC329@NOSPAMhome.com>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk> <80rtug$csc$1@starburst.uk.insnet.net>`

```
That has been my experience exactly.  You can DESIGN your copy member
from the beginning to use COPY REPLACING effectively.  But simple
editing of existing copy members in your program doesn't work well. 
Maybe Alistair has had a different experience (with a different
compiler) than we have.

Rick Price wrote:
> 
> Yes but not very usefully for existing code.
…[50 more quoted lines elided]…
> > out how strong they are.
```

###### ↳ ↳ ↳ Re: Copy replacing

_(reply depth: 4)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsPC9AAjTqM4Ew5K@ld50macca.demon.co.uk>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk> <80rtug$csc$1@starburst.uk.insnet.net> <38319719.C07BC329@NOSPAMhome.com>`

```
No. It's just bad luck if you are trying to reverse engineer your
layouts. But as reverse engineering only affects the next compilation
why not go ahead on a compile by compile basis rather than globally?

In article <38319719.C07BC329@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes
>That has been my experience exactly.  You can DESIGN your copy member
>from the beginning to use COPY REPLACING effectively.  But simple
…[57 more quoted lines elided]…
>> > out how strong they are.
```

###### ↳ ↳ ↳ Re: Copy replacing

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3832B9FA.94E32097@NOSPAMhome.com>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <jQGMiKAHpWM4Ew9s@ld50macca.demon.co.uk> <80rtug$csc$1@starburst.uk.insnet.net> <38319719.C07BC329@NOSPAMhome.com> <bsPC9AAjTqM4Ew5K@ld50macca.demon.co.uk>`

```
I just copied the copy member into my source and edited it.  My post
wasn't on how to program the code, but on what I see as a weakness in
the COPY REPLACING command.  I wondered if that had been addressed for
the future.

Alistair Maclean wrote:
> 
> No. It's just bad luck if you are trying to reverse engineer your
…[73 more quoted lines elided]…
> out how strong they are.
```

#### ↳ Re: Copy replacing

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsb%3.2298$Di3.24915@news2.mia>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com>`

```
So do this:

 01   MY-FILE-NAME.
      05   :TT:-FIELD-1     PIC X(05).
      05   :TT:-FIELD-2     PIC X(20).

COPY whatever REPLACING ==:TT:== BY ==TTOLD==.
COPY whatever REPLACING ==:TT:== BY ==TT==.


Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:38307ECF.B5AFE62@NOSPAMhome.com...
> Sometimes we need to convert a file from an old format to a new one.
> The standard procedure is to create a new copy member for the new file
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Copy replacing

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3842BFAB.681A08AF@NOSPAMhome.com>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <bsb%3.2298$Di3.24915@news2.mia>`

```
I won't change an existing copy member, breaking scores of existing
programs, so that I can use it a bit differently in my new program.

However, I can wish that it were designed for REPLACING in the first
place.  Too bad that is necessary.

James King wrote:
> 
> So do this:
…[27 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Copy replacing

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3843B94E.3C331936@zip.com.au>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <bsb%3.2298$Di3.24915@news2.mia> <3842BFAB.681A08AF@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> I won't change an existing copy member, breaking scores of existing
…[4 more quoted lines elided]…
> 

Too bad you cannot apply a default substitution that can be overridden
by the program only if required.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Copy replacing

- **From:** wmklein@my-deja.com
- **Date:** 1999-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<820nq2$g38$1@nnrp1.deja.com>`
- **References:** `<38307ECF.B5AFE62@NOSPAMhome.com> <bsb%3.2298$Di3.24915@news2.mia> <3842BFAB.681A08AF@NOSPAMhome.com>`

```
Check your compiler to see if your vendor ALREADY supports syntax that
will be STANDARD in the next COBOL Standard.  (I know that Micro Focus
does - but don't personally know of any other that does it already.)

Look for the "leading" and "trailing" options in the COPY/REPLACING (and
REPLACE) statements - that "officially" support partial word replacement
- without planning on it when you create your original COPY member.

Note:  If your vendor does not support this already, you might want to
find out their method of doing an "official" enhancement request - such
as IBM has via the SHARE user group or via the support channel "REQUEST"
feature.

This probably won't help you with your immediate requirement - but MIGHT
be faster than waiting for your vendor to provide a fully conforming
compiler - for the next Standard.

In article <3842BFAB.681A08AF@NOSPAMhome.com>,
  Please, do, not, e-mail, replies, post, them!! wrote:
> I won't change an existing copy member, breaking scores of existing
> programs, so that I can use it a bit differently in my new program.
…[17 more quoted lines elided]…
> > > Sometimes we need to convert a file from an old format to a new
one.
> > > The standard procedure is to create a new copy member for the new
file
> > > format, changing as few field names as possible, as they will be
used
> > > in  the programs using it.
> > >
…[6 more quoted lines elided]…
> > > This is when we would like to use a COPY REPLACING TT- BY TTOLD-
for the
> > > conversion program, but we end up making a copy of the copy member
and
> > > editing that REPLACING by hand.
> > >
> > > Are we going to have a more direct way of doing this simple
editing
> > > func


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
