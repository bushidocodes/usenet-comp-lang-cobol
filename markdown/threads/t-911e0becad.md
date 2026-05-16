[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copy replacing - Procedure Division

_7 messages · 6 participants · 2004-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Copy replacing - Procedure Division

- **From:** avijayshankar@coolgoose.com (Vijay Shankar)
- **Date:** 2004-02-19T18:35:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4232178f.0402191835.6f402dd4@posting.google.com>`

```
Iam using a Common copybook in a cobol program and using copy replacing
statement to reuse the copybook.

Iam getting a compile time error with the following message

IGYPS2010-E   Procedure-name "PRT08-WA3-EXIT" was found in area "B"
followed by a period or section.  The procedure-name was processed as if
found in area "A".

My copybook looks like this

  (**)-WA3-EXIT.
      EXIT.

I use COPY GENRPPRT REPLACING ==(**)== BY ==PRT08==.

My (**)- starts in Area A in the copybook. After replacing it moves to area
B.

Could somebody throw some light into this problem ?? Any help will be
appreciated

thanks
Vijay
```

#### ↳ Re: Copy replacing - Procedure Division

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-02-20T06:21:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com>`

```
"Obscure" rule in the ANSI/ISO Standard.  You will need to place your COPY
statement in the A-Margin in order to get the "inserted" text there.
Unfortunately, if you have additional lines that should be in the B-Margin, this
may not work.

Happily this "goes" away with the ISO 2002 Standard, but for an IBM mainframe
compiler, you may have PROBLEMS inserting COPY members with both A- and B-margin
source in it.
```

##### ↳ ↳ Re: Copy replacing - Procedure Division

- **From:** avijayshankar@coolgoose.com (Vijay Shankar)
- **Date:** 2004-02-20T05:33:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4232178f.0402200533.19d1b5c6@posting.google.com>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com> <WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>`

```
Thanks.. I had the same hunch and you confirmed it..
I kinda' figured a work-around by having by "key field" appear in area
B for the paragraph headings and i could compile the program

I used PRINT(**)-WA3-EXIT so that the "(**)" string is pushed to area
B

thanks again for your response




"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>...
> "Obscure" rule in the ANSI/ISO Standard.  You will need to place your COPY
> statement in the A-Margin in order to get the "inserted" text there.
…[35 more quoted lines elided]…
> > Vijay
```

##### ↳ ↳ Re: Copy replacing - Procedure Division

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-02-20T15:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c157eh$t1e$1@peabody.colorado.edu>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com> <WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>`

```

On 19-Feb-2004, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> "Obscure" rule in the ANSI/ISO Standard.  You will need to place your COPY
> statement in the A-Margin in order to get the "inserted" text there.
…[7 more quoted lines elided]…
> source in it.

I have no problems with "01  " in the "A" margin of copy replacing commands.   I
have never tried replacing part of a paragraph name.
```

##### ↳ ↳ Re: Copy replacing - Procedure Division

- **From:** Colin Campbell <cmcampb@adelphia.net_remove_this>
- **Date:** 2004-02-20T11:36:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RktZb.4$e3.3@dfw-service2.ext.ray.com>`
- **In-Reply-To:** `<WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com> <WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net>`

```
William M. Klein wrote:
> "Obscure" rule in the ANSI/ISO Standard.  You will need to place your COPY
> statement in the A-Margin in order to get the "inserted" text there.
…[6 more quoted lines elided]…
> 
Actually, you can code just the "BY" phrase in Margin A.  For example:
8   12
     COPY XYZ REPLACING =='X'== BY
==PRE-==.

If you have multiple replacings coded in the COPY statement, only the 
phrases requiring the output to be in Margin A need to be coded in Margin A.
```

###### ↳ ↳ ↳ Re: Copy replacing - Procedure Division

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-02-20T12:49:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c15rsk$2dpa$1@si05.rsvl.unisys.com>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com> <WHhZb.1035$yZ1.530@newsread2.news.pas.earthlink.net> <RktZb.4$e3.3@dfw-service2.ext.ray.com>`

```

"Colin Campbell" <cmcampb@adelphia.net_remove_this> wrote in message
news:RktZb.4$e3.3@dfw-service2.ext.ray.com...

> Actually, you can code just the "BY" phrase in Margin A.  For example:
> 8   12
…[4 more quoted lines elided]…
> phrases requiring the output to be in Margin A need to be coded in Margin
A.

For ANSI-85 COBOL:

There are actually two rules at work here.

The first is that the entirety of the replacement text logically replaces
the entirety of the COPY statement (whether or not the REPLACING phrase is
specified).  That means if the first thing in the library text needs to be
in Area A, the COPY statement should be in Area A.  (ANSI X3.23-1985 page
XII-3, 2.4 The COPY Statement, General Rule 2.

The second is that a replaced text-word begins in the same area in the
resulting program that it occupies in the COPY statement, whereas an
identifier, literal or word that is replaced begins in the same area as the
original text in the library.  (Ibid., page XII-4, General Rule 9).

As Bill said, that all went away in the '02 standard because Area A and Area
B were replaced by a single "program-text area".

     -Chuck Stevens
```

#### ↳ Re: Copy replacing - Procedure Division

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-02-20T08:16:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kfKdnW3Tecc3i6vdRVn-tA@giganews.com>`
- **References:** `<4232178f.0402191835.6f402dd4@posting.google.com>`

```
Vijay Shankar wrote:
> Iam using a Common copybook in a cobol program and using copy
> replacing statement to reuse the copybook.
…[18 more quoted lines elided]…
> appreciated

Off the wall suggestion: Compile the procedure division "copybook"
separately and statically link to your programs. Add "Object-Oriented
Programming" to your resume.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
