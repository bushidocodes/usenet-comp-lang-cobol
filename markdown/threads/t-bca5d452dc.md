[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help required

_8 messages · 5 participants · 1998-11 → 1998-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help required

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b1d8d.3699473@nntp.ix.netcom.com>`

```
I got the following errors in cobol. can anyone explain them to me, in
human terms?

000190 PROCEDURE DIVISION.
000200 DECLARATIVES.
000210     COPY "DECL.CUSTOMER".
000220     COPY "DECL.DESC".
000230 END DECLARATIVES.
000240 MAIN SECTION.
000250 FIRST-PARA.
000260     OPEN I-O CUSTOMER.
       SCREEN.    <- first error
           DISPLAY "DO YOU WANT TO CONTINUE ? [Y or N] " 
                LINE 5 POSITION 12.
           ACCEPT TYPX LINE 5 POSITION 47.
           IF TYPX = "N" GO TO EOJ.
           IF TYPX NOT = "Y" GO TO SCREEN. <- second set of errors
000270 MAIN-LOOP.

area A should be blank, verb expected SCREEN FOUND
(thats referring to the screen goto i think)

procedure nam required, verb expected SCREEN found



gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: help required

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YfF62.221$7a.139@news1.atlantic.net>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com>`

```
SCREEN is a reserved word in your compiler.
Normally as SCREEN SECTION.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >

G Moore wrote in message <365b1d8d.3699473@nntp.ix.netcom.com>...
>I got the following errors in cobol. can anyone explain them to me, in
>human terms?
>
[...]
>000260     OPEN I-O CUSTOMER.
>       SCREEN.    <- first error
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ Re: help required

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b6c95.710674@nntp.ix.netcom.com>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com> <YfF62.221$7a.139@news1.atlantic.net>`

```
On Tue, 24 Nov 1998 16:10:42 -0500, "Rick Smith"
<ricksmith@aiservices.com> wrote:

>SCREEN is a reserved word in your compiler.
>Normally as SCREEN SECTION.
>-------------------------------
>Rick Smith
>e-mail: < ricksmith@aiservices.com >

thanks.


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: help required

- **From:** Ralph Jones <leclay@ibm.net>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365B312C.C6E386AB@ibm.net>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com>`

```
Screen is a reserved word for many compilers, you cannot use it as a para.
name.

G Moore wrote:

> I got the following errors in cobol. can anyone explain them to me, in
> human terms?
…[22 more quoted lines elided]…
> gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: help required

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73h1n0$iil$1@news.igs.net>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com>`

```
Try removing the tab, and putting in spaces at the start
of the line.  You have the first part of the code in one
format (1-6 a number, 7 a space, then area A) then
the line with the error starts in column four(it should
be 8).  It is also a reserved word, so illegal as a
paragraph name.

G Moore wrote in message <365b1d8d.3699473@nntp.ix.netcom.com>...
>I got the following errors in cobol. can anyone explain them to me, in
>human terms?
…[24 more quoted lines elided]…
>gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: help required

- **From:** Lookin'@You.2 (WDS)
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36634032.4089660@news1.frb.gov>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com>`

```
On Tue, 24 Nov 1998 20:59:51 GMT, gvwmoore@ix.netcom.com wrote:

>I got the following errors in cobol. can anyone explain them to me, in
>human terms?
…[20 more quoted lines elided]…
>procedure nam required, verb expected SCREEN found

Your compiler probably considers SCREEN to be a reserved word.  Try
changing that paragraph name to something else.
```

##### ↳ ↳ (relatively) new reserved words

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3666F57C.D28E98BE@home.com>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com> <36634032.4089660@news1.frb.gov>`

```
> Your compiler probably considers SCREEN to be a reserved word.  Try
> changing that paragraph name to something else.

I long ago got in the habit of using the prefix MY- in front of real
words such as SCREEN.  This habit has followed me from language to
language and has saved me from problems such as this.
```

##### ↳ ↳ Re: help required

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ebnh$7vh$1@news.igs.net>`
- **References:** `<365b1d8d.3699473@nntp.ix.netcom.com> <36634032.4089660@news1.frb.gov>`

```
Fujitsu is very fussy about columns. The line right after 260
has a TAB rather than 8 spaces in from of it, from where
you cut and pasted from another program.  Go into the text
editor, and type 8 SPACES before it and your problem
will go away.

And yes, I agree that an editor that cannot figure out TABS
is as Mickey mouse as hell.

WDS wrote in message <36634032.4089660@news1.frb.gov>...
>On Tue, 24 Nov 1998 20:59:51 GMT, gvwmoore@ix.netcom.com wrote:
>
…[29 more quoted lines elided]…
>-------------------Decoy@Spammer.Trasher----------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
