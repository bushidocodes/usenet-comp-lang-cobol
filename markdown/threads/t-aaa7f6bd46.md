[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Code Pic 9 item

_8 messages · 5 participants · 2002-06 → 2002-07_

---

### Code Pic 9 item

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-24T22:47:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d17db43@news.mhogaming.com>`

```
Can I code a numeric item where the screen will have spaces and not zeros, I
would like the screen item to show up empty and accept user input.
```

#### ↳ Re: Code Pic 9 item

- **From:** "Topcoder" <No@Spam.Com>
- **Date:** 2002-06-25T04:44:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3d17db43@news.mhogaming.com>`

```

Joseph Ostreicher wrote in message <3d17db43@news.mhogaming.com>...
>Can I code a numeric item where the screen will have spaces and not zeros, I
>would like the screen item to show up empty and accept user input.


Sure.  Use the clause BLANK ZERO.
```

##### ↳ ↳ Re: Code Pic 9 item

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-25T01:06:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d17fbe9$1@news.mhogaming.com>`
- **References:** `<3d17db43@news.mhogaming.com> <pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net>`

```
oh right i forgot about that, BLANK ZERO in the edited field, i used z in
the screen item, which i guess does the same job.

Thanks
"Topcoder" <No@Spam.Com> wrote in message
news:pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net...
>
> Joseph Ostreicher wrote in message <3d17db43@news.mhogaming.com>...
> >Can I code a numeric item where the screen will have spaces and not
zeros, I
> >would like the screen item to show up empty and accept user input.
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Code Pic 9 item

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-25T01:32:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d180212$1@news.mhogaming.com>`
- **References:** `<3d17db43@news.mhogaming.com> <pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net>`

```
Actually the BLANK ZERO doesn't work for me, can you show how to put it in
the Second-Term Clause using following cods

 @OPTIONS MAIN
 IDENTIFICATION DIVISION.
 PROGRAM-ID. UNSTRINGG.
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SOURCE-COMPUTER. IBM-PC.
 OBJECT-COMPUTER. IBM-PC.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01 EXPRESSION-IN       PIC x(10) VALUE SPACES.
 01 FIRST-TERM          PIC 9(5)  VALUE zero.
 01 SECOND-TERM         PIC 9(5)  VALUE  zero.
 01 OPERATION           PIC X     VALUE SPACE.
 01 UNSTRING-POINTER       PIC 9(2)  value zero.
 01 Total               pic 9(5) value zero.

 SCREEN SECTION.
 01 MAIN BLANK SCREEN foreground-color 6 background-color 3.
     03 line 1 column 34 value "String Test" underline, reverse-video.
     03 LINE 3 COLUMN 1 VALUE "Enter Expression".
     03 line 3 column 19 pic x(10) using expression-in.
     03 line 5 column 1 value "First-Term".
     03 line 5 column 13 pic z(5) using First-Term.
     03 line 6 column 1 value "Second-Term".
     03 line 6 column 13 pic 9(5) using Second-Term.
     03 line 7 column 1 value "Operation".
     03 line 7 column 13 pic x from Operation.
     03 line 8 column 1 value "Unstring-pointer".
     03 line 8 column 20 pic 9(2) using unstring-pointer.
     03 line 9 column 1 value "Total".
     03 line 9 column 13 pic z(5) from Total.
 procedure division.
 unstringg-start.
     display main
     accept main
     unstring expression-in delimited by "+" or "."  or "*"  or "/" into
first-term delimiter in
     operation count in unstring-pointer
     end-unstring
     add 2 to unstring-pointer
     unstring expression-in delimited by "=" into second-term pointer
unstring-pointer
     end-unstring
     add first-term second-term giving total.
     display main


"Topcoder" <No@Spam.Com> wrote in message
news:pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net...
>
> Joseph Ostreicher wrote in message <3d17db43@news.mhogaming.com>...
> >Can I code a numeric item where the screen will have spaces and not
zeros, I
> >would like the screen item to show up empty and accept user input.
>
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Code Pic 9 item

- **From:** J M Pittman <jjmpittmaniiii@mindspring.com>
- **Date:** 2002-07-01T21:14:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D212898.5090808@mindspring.com>`
- **References:** `<3d17db43@news.mhogaming.com> <pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net> <3d180212$1@news.mhogaming.com>`

```
Try:  03 line 6 column 13 pic 9(5)blank zero using Second-Term.



Joseph Ostreicher wrote:

>Actually the BLANK ZERO doesn't work for me, can you show how to put it in
>the Second-Term Clause using following cods
…[65 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Code Pic 9 item

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-06-25T12:06:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36AADEA38525E5D3.4B036CB7FCA0F47E.C78A9D56A2E7133F@lp.airnews.net>`
- **References:** `<3d17db43@news.mhogaming.com> <pySR8.59735$UT.4096732@bgtnsc05-news.ops.worldnet.att.net>`

```
On Tue, 25 Jun 2002 04:44:05 GMT, "Topcoder" <No@Spam.Com> enlightened
us:

>
>Joseph Ostreicher wrote in message <3d17db43@news.mhogaming.com>...
…[6 more quoted lines elided]…
>

While using the BLANK ZERO clause will work, so will a PIC Z which is
more practical for a one byte field.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #101:

Your file was so big.
It might be very useful.
But now it is gone.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Code Pic 9 item

- **From:** "Joseph Ostreicher" <josephos@hotmail.com>
- **Date:** 2002-06-25T00:47:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d17f7a0@news.mhogaming.com>`
- **References:** `<3d17db43@news.mhogaming.com>`

```
Nevermind...

"Joseph Ostreicher" <josephos@hotmail.com> wrote in message
news:3d17db43@news.mhogaming.com...
> Can I code a numeric item where the screen will have spaces and not zeros,
I
> would like the screen item to show up empty and accept user input.
>
>
>
>
```

#### ↳ Re: Code Pic 9 item

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-06-25T05:57:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af9e76$nsv$1@slb2.atl.mindspring.net>`
- **References:** `<3d17db43@news.mhogaming.com>`

```
Try using reference modification to clear the PIC 9 item.

03 WS-ITEM PIC 9(08).

MOVE SPACES TO WS-ITEM (1:LENGTH OF WS-ITEM).

The compiler will treat it as if it were PIC X(08).

HTH....

Bill

"Joseph Ostreicher" <josephos@hotmail.com> wrote in message
news:3d17db43@news.mhogaming.com...
> Can I code a numeric item where the screen will have spaces and not zeros,
I
> would like the screen item to show up empty and accept user input.
>
>
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
