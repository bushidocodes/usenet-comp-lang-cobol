[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New to COBOL

_10 messages · 6 participants · 1998-09_

---

### New to COBOL

- **From:** bamm.com (BammBamm)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f56079.8843178@n3.idirect.com>`

```
Hello there,
I'm just starting out with COBOL and I'm having problems with string
variables.

Here's my problem. I'd like to know how to eliminate blank spaces in a
string variable.

e.g.         01           LAST-NAME           PIC  X(15).

When I enter a string in the window console such as SMITH and press
ENTER the program waits until I fill in the remaining spaces assigned
to the variable LAST-NAME which is  10. So in order for the program to
continue I'm forced to input SMITH along with any aditional characters
to make up a total of 15  characters.

I am using Fujitsu COBOL 3.0

Thank You in advance.
```

#### ↳ Re: New to COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t444t$klh@sjx-ixn3.ix.netcom.com>`
- **References:** `<35f56079.8843178@n3.idirect.com>`

```

bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
>Hello there,
>I'm just starting out with COBOL and I'm having problems with string
…[15 more quoted lines elided]…
>Thank You in advance.

I won't swear to it, but this sounds like a "bug" in the Fujitsu compiler
that has been reported in this NG before.  Have you tried contacting their
support?
```

##### ↳ ↳ Re: New to COBOL

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tb5t7$bg4$1@nnrp1.dejanews.com>`
- **References:** `<35f56079.8843178@n3.idirect.com> <6t444t$klh@sjx-ixn3.ix.netcom.com>`

```
William -

I don't have much experience w/ Fujitsu; much more w/ Micro Focus; and
haven't worked much with that in a few years now, but could it be simply that
his  screen input field is defined with something like a 'MUSTFILL'
attribute?

- Ed Stevens

In article <6t444t$klh@sjx-ixn3.ix.netcom.com>,
  "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
> bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
…[23 more quoted lines elided]…
>


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: New to COBOL

- **From:** fujitsu_cobol@my-dejanews.com
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t9fv6$32e$1@nnrp1.dejanews.com>`
- **References:** `<35f56079.8843178@n3.idirect.com>`

```
Fujitsu COBOL fully conforms to the ANSI and X/Open COBOL standards with
regards to ACCEPT statements.

Fujitsu COBOL supports the following five types of Screen Accepts:
1.  ACCEPT data-item
2.  ACCEPT data-item FROM CONSOLE
3.  ACCEPT data-item AT LINE number COLUMN number
4.  ACCEPT screen-section

If you do not want to complete fill a field with blanks, then you will want to
use ACCEPT data-item FROM CONSOLE

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX:   (408) 428-0600
Email: cobol@adtools.com
Web:   http://www.adtools.com


In article <35f56079.8843178@n3.idirect.com>,
  bamm.com (BammBamm) wrote:
> Hello there,
> I'm just starting out with COBOL and I'm having problems with string
…[16 more quoted lines elided]…
>


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: New to COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t9rch$b8k@sjx-ixn9.ix.netcom.com>`
- **References:** `<35f56079.8843178@n3.idirect.com> <6t9fv6$32e$1@nnrp1.dejanews.com>`

```
To Fujitsu:
   May I suggest that you run this by Artur Reimann - the Fujitsu
representative to J4?

If your product behaves differently for
    ACCEPT data-name
        versus
    ACCEPT data-name FROM CONSOLE

*and*

you document "from console" as your default input device, then YOU HAVE A
BUG ....
   This most certainly is NOT ANSI conforming.
      (and the X/Open definition for this type of ACCEPT is identical to the
ANSI one)

fujitsu_cobol@my-dejanews.com wrote in message
<6t9fv6$32e$1@nnrp1.dejanews.com>...
>Fujitsu COBOL fully conforms to the ANSI and X/Open COBOL standards with
>regards to ACCEPT statements.
…[7 more quoted lines elided]…
>If you do not want to complete fill a field with blanks, then you will want
to
>use ACCEPT data-item FROM CONSOLE
>
…[32 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: New to COBOL

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298253.70008.23121@kcbbs.gen.nz>`
- **References:** `<6t9fv6$32e$1@nnrp1.dejanews.com>`

```
In message <<6t9fv6$32e$1@nnrp1.dejanews.com>> fujitsu_cobol@my-dejanews.com writes:
> regards to ACCEPT statements.
> 
…[7 more quoted lines elided]…
> use ACCEPT data-item FROM CONSOLE

Items 3 and 4 are implicitly FROM CRT.  In MF the CONSOLE and the
CRT are the same screen, so these can be mixed, though it is
not recommended.  In Fujitsu (AFAIK) CONSOLE and CRT are
different windows, so cannot be mixed.

The real difference between ACCEPT FROM CONSOLE and FROM CRT
is that in the former it is accepting keystrokes while the
latter accepts the content of fields.

The 'data-item' can be preset to have any value and then
keystrokes will change the value character by character
and when the accept is completed it will cntain the 
data as changed (ie the combination of initial value and
keystrokes determined by the rules given to each key).

It is best to have the field displayed before the accept
or by it, so that the user can see the current field
content.
```

#### ↳ Re: New to COBOL

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tc6gn$ru5$1@news.igs.net>`
- **References:** `<35f56079.8843178@n3.idirect.com>`

```

bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
>Hello there,
>I'm just starting out with COBOL and I'm having problems with string
>variables.
>
The console accept display with Fujitsu is very primitive. Use
a screen function instead (you have both a screen and a console).
```

##### ↳ ↳ Re: New to COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tc88o$gv0@dfw-ixnews3.ix.netcom.com>`
- **References:** `<35f56079.8843178@n3.idirect.com> <6tc6gn$ru5$1@news.igs.net>`

```

Donald Tees wrote in message <6tc6gn$ru5$1@news.igs.net>...
>
>bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
…[7 more quoted lines elided]…
>
  But the CONSOLE variation (without AT or a screen-name) is the only ACCEPT
that is ANSI conforming and guaranteed to be portable.
```

###### ↳ ↳ ↳ Re: New to COBOL

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6td49c$n8j$1@news.igs.net>`
- **References:** `<35f56079.8843178@n3.idirect.com> <6tc6gn$ru5$1@news.igs.net> <6tc88o$gv0@dfw-ixnews3.ix.netcom.com>`

```

William M. Klein wrote in message <6tc88o$gv0@dfw-ixnews3.ix.netcom.com>...
>Donald Tees wrote in message <6tc6gn$ru5$1@news.igs.net>...
>>bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
…[3 more quoted lines elided]…
>  But the CONSOLE variation (without AT or a screen-name) is the only
ACCEPT
>that is ANSI conforming and guaranteed to be portable.


Its gotta work on one computer before it gets ported.
```

##### ↳ ↳ Re: New to COBOL

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-WVldYFtOuDQ0@Dwight_Miller.iix.com>`
- **References:** `<35f56079.8843178@n3.idirect.com> <6tc6gn$ru5$1@news.igs.net>`

```
On Fri, 11 Sep 1998 22:01:23, "Donald Tees" <donald@willmack.com> 
wrote:

> 
> bamm.com (BammBamm) wrote in message <35f56079.8843178@n3.idirect.com>...
…[5 more quoted lines elided]…
> a screen function instead (you have both a screen and a console).

With Version 4.0 the console window/icon goes away unless you use it 
in your program.  Very nice - glad to see it happen.  Hated having TWO
items in the task bar with the same name.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
