[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF net express

_13 messages · 5 participants · 2000-09_

---

### MF net express

- **From:** "Gandalf" <nhaire@bigfoot.com>
- **Date:** 2000-09-11T02:22:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bc32a1@news.server.worldonline.co.uk>`

```
Any idea where I can DL this from?
I am using MF personal at the moment but it does not produce EXE files, I
have used the brilliant Fujitsu compiler but it did not like one of my sort
programs, I got the error message "SORT-MERGE FILE CAN ONLY SPECIFY
FILE-IDENTIFIER IN ASSIGN CLAUSE". MF personal compiled the prog OK !!
Thanks
Nigel
```

#### ↳ Re: MF net express

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-09-11T01:35:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000910213531.19879.00000679@nso-cu.aol.com>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk>`

```
In article <39bc32a1@news.server.worldonline.co.uk>, "Gandalf"
<nhaire@bigfoot.com> writes:

>have used the brilliant Fujitsu compiler but it did not like one of my sort
>programs, I got the error message "SORT-MERGE FILE CAN ONLY SPECIFY
>FILE-IDENTIFIER IN ASSIGN CLAUSE". MF personal compiled the prog OK !!
>Thanks

What was your SELECT/SD/SORT syntax?
Maybe with a minor change or two it would be compatible 
to compile under either system.
```

#### ↳ Re: MF net express

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-10T22:27:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8phjft$giv$1@slb0.atl.mindspring.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk>`

```
To get your program to compile with Fujitsu,
 Change your Select/Assign statement associated with your SD to something
like

  Select SortFile Assign to Fujitsu-has-a-bug.
        instead of
   Select SortFile Assign to "ANSI-Allows.This".

(This "bug" in Fujitsu is fixed in later versions of their compiler)
```

##### ↳ ↳ Re: MF net express

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-11T03:54:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bc5733.5392202@207.126.101.100>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net>`

```
fujitsu-has-a-bug won't work.  It has to be 8 characters or less.

I use 

Assign Sort-Work to Whatever.



On Sun, 10 Sep 2000 22:27:38 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>To get your program to compile with Fujitsu,
> Change your Select/Assign statement associated with your SD to something
…[23 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF net express

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-11T12:40:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pijrv$t0i$1@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100>`

```
My experience has been that file names can be longer than eight
characters, as long as they do not contain spaces.  For example I created
a demonstration program for my COBOL students using the name:

	FALL2000-DATADIVDEMOFinal.COB

I compiled, linked, and executed the file using the steps found in "TY
COBOL in 24 Hours" (i.e. I did not create a project).  

Floyd Johnson

Thane Hubbell (thaneH@softwaresimple.com) wrote:
: fujitsu-has-a-bug won't work.  It has to be 8 characters or less.

: I use 

: Assign Sort-Work to Whatever.



: On Sun, 10 Sep 2000 22:27:38 -0500, "William M. Klein"
: <wmklein@nospam.ix.netcom.com> wrote:

: >To get your program to compile with Fujitsu,
: > Change your Select/Assign statement associated with your SD to something
: >like
: >
: >  Select SortFile Assign to Fujitsu-has-a-bug.
: >        instead of
: >   Select SortFile Assign to "ANSI-Allows.This".
: >
: >(This "bug" in Fujitsu is fixed in later versions of their compiler)
: >
: >--
: >Bill Klein
: >    wmklein <at> ix dot netcom dot com
: >"Gandalf" <nhaire@bigfoot.com> wrote in message
: >news:39bc32a1@news.server.worldonline.co.uk...
: >> Any idea where I can DL this from?
: >> I am using MF personal at the moment but it does not produce EXE files, I
: >> have used the brilliant Fujitsu compiler but it did not like one of my sort
: >> programs, I got the error message "SORT-MERGE FILE CAN ONLY SPECIFY
: >> FILE-IDENTIFIER IN ASSIGN CLAUSE". MF personal compiled the prog OK !!
: >> Thanks
: >> Nigel
: >>
: >>
: >
: >

: ---
: Try a better search engine:  http://www.google.com
: My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF net express

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-11T15:25:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bcf94c.46896220@207.126.101.100>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net>`

```
You are correct in general, but the assign of a sort work file (if you
don't want an error message) has to be 8 characters or less with
Fujitsu COBOL.

On 11 Sep 2000 12:40:31 GMT, floydj@netins.net (Floyd Johnson) wrote:

>My experience has been that file names can be longer than eight
>characters, as long as they do not contain spaces.  For example I created
…[64 more quoted lines elided]…
>+-----------------------------------------------------------+

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF net express

_(reply depth: 5)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-11T17:41:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pj5fv$948$1@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100>`

```
Are other uses of virtual file names similarly limited? or just the sort
work file?

Floyd Johnson 

Thane Hubbell (thaneH@softwaresimple.com) wrote:
: You are correct in general, but the assign of a sort work file (if you
: don't want an error message) has to be 8 characters or less with
: Fujitsu COBOL.
```

###### ↳ ↳ ↳ Fujitsu sort work file assign, was.. NetExpress

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-11T23:39:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bd6af0.516522@207.126.101.100>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100> <8pj5fv$948$1@ins21.netins.net>`

```
I'm learning all kinds of things this week.

First  - bill is right - the later versions issue an I level message
if you use a value in quotes.

Floyd is right - you can use more than 8 character names.

I am right - the name has to be 8 characters or less?  How can that
be?  Well, if I use "Whatever" it works fine.  If I use "Whatever1" i
get an error message that states:


JMN2948I-E  20  CHARACTER WHICH CONSTRUCTS FILE-IDENTIFIER IS INVALID.
OR NAME OF FILE-IDENTIFIER EXCEEDS 8 CHARACTERS. 
            NAME OF FILE-IDENTIFIER IS ASSUMED TO BE VALID. IF THE
NAME EXCEEDS 8 CHARACTERS,FIRST 8 CHARACTERS IS 
            ASSUMED TO BE VALID.


I'm looking into this now.

On 11 Sep 2000 17:41:19 GMT, floydj@netins.net (Floyd Johnson) wrote:

>Are other uses of virtual file names similarly limited? or just the sort
>work file?
…[20 more quoted lines elided]…
>+-----------------------------------------------------------+

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Fujitsu sort work file assign, was.. NetExpress

_(reply depth: 7)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-12T12:47:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pl8lv$pnj$2@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100> <8pj5fv$948$1@ins21.netins.net> <39bd6af0.516522@207.126.101.100>`

```
Late, yesterday afternoon,I sent the following note to Thane as an
e-mail.  Since he replied to the group, I thought it might be helpful to
see the original message.

======================================================

Thane:

I am still confused (I think).  The code from your book (see page 288)
uses file names which are longer than eight characters.  They don't seem
to generate error messages ( though I just tried the first one).  Am I
at the right page of the book?  Is it something that is inconsistent in
Fujitsu (i.e. works sometimes, but not always).  Or was it an error that
was introduced after version 3.0 (which we are using)?

I am following this up because I fast approaching this material in our
course.  I know that every language implementation has its quirk, I just
feel more comfortable if I know what they are and how they work.

Floyd Johnson

=======================================================

Thane Hubbell (thaneH@softwaresimple.com) wrote:
: I'm learning all kinds of things this week.

: First  - bill is right - the later versions issue an I level message
: if you use a value in quotes.

: Floyd is right - you can use more than 8 character names.

: I am right - the name has to be 8 characters or less?  How can that
: be?  Well, if I use "Whatever" it works fine.  If I use "Whatever1" i
: get an error message that states:


: JMN2948I-E  20  CHARACTER WHICH CONSTRUCTS FILE-IDENTIFIER IS INVALID.
: OR NAME OF FILE-IDENTIFIER EXCEEDS 8 CHARACTERS. 
:             NAME OF FILE-IDENTIFIER IS ASSUMED TO BE VALID. IF THE
: NAME EXCEEDS 8 CHARACTERS,FIRST 8 CHARACTERS IS 
:             ASSUMED TO BE VALID.


: I'm looking into this now.

: On 11 Sep 2000 17:41:19 GMT, floydj@netins.net (Floyd Johnson) wrote:

: >Are other uses of virtual file names similarly limited? or just the sort
: >work file?
: >
: >Floyd Johnson 
: >
: >Thane Hubbell (thaneH@softwaresimple.com) wrote:
: >: You are correct in general, but the assign of a sort work file (if you
: >: don't want an error message) has to be 8 characters or less with
: >: Fujitsu COBOL.
: >
: >--
: >--
: >+-----------------------------------------------------------+
: >|                      Floyd H. Johnson                     |
: >+-----------------------------+-----------------------------+    
: >| Voice  : (716) 594 - 0942   | 87 Parkway Drive            |
: >| E-Mail : floydj@netins.net  | North Chili, NY  14514      |
: >+-----------------------------+-----------------------------+
: >|                 http://bounce.to/Roberts                  |
: >+-----------------------------------------------------------+
: >| If you think you understand Him,                          |
: >|               then you really do not know HIM !!          |
: >+-----------------------------------------------------------+

: ---
: Try a better search engine:  http://www.google.com
: My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Fujitsu sort work file assign, was.. NetExpress

_(reply depth: 7)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-12T12:51:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pl8s0$pnj$4@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100> <8pj5fv$948$1@ins21.netins.net> <39bd6af0.516522@207.126.101.100>`

```
I sent the following note to Thane as an e-mail.  Since he replied to
the group, I thought it might be helpful to see the message.

=====================================================

Thane:

I am still confused (I think).  The code from your book (see page 288)
uses file names which are longer than eight characters.  They don't seem
to generate error messages ( though I just tried the first one).  Am I
at the right page of the book?  Is it something that is inconsistent in
Fujitsu (i.e. works sometimes, but not always).  Or was it an error that
was introduced after version 3.0 (which we are using)?  

I am following this up because I fast approaching this material in our
course.  I know that every language implementation has its quirk, I just
feel more comfortable if I know what they are and how they work.

Floyd Johnson

======================================================

Thane Hubbell (thaneH@softwaresimple.com) wrote:
: I'm learning all kinds of things this week.

: First  - bill is right - the later versions issue an I level message
: if you use a value in quotes.

: Floyd is right - you can use more than 8 character names.

: I am right - the name has to be 8 characters or less?  How can that
: be?  Well, if I use "Whatever" it works fine.  If I use "Whatever1" i
: get an error message that states:


: JMN2948I-E  20  CHARACTER WHICH CONSTRUCTS FILE-IDENTIFIER IS INVALID.
: OR NAME OF FILE-IDENTIFIER EXCEEDS 8 CHARACTERS. 
:             NAME OF FILE-IDENTIFIER IS ASSUMED TO BE VALID. IF THE
: NAME EXCEEDS 8 CHARACTERS,FIRST 8 CHARACTERS IS 
:             ASSUMED TO BE VALID.


: I'm looking into this now.

: On 11 Sep 2000 17:41:19 GMT, floydj@netins.net (Floyd Johnson) wrote:

: >Are other uses of virtual file names similarly limited? or just the sort
: >work file?
: >
: >Floyd Johnson 
: >
: >Thane Hubbell (thaneH@softwaresimple.com) wrote:
: >: You are correct in general, but the assign of a sort work file (if you
: >: don't want an error message) has to be 8 characters or less with
: >: Fujitsu COBOL.
: >
: >--
: >--
: >+-----------------------------------------------------------+
: >|                      Floyd H. Johnson                     |
: >+-----------------------------+-----------------------------+    
: >| Voice  : (716) 594 - 0942   | 87 Parkway Drive            |
: >| E-Mail : floydj@netins.net  | North Chili, NY  14514      |
: >+-----------------------------+-----------------------------+
: >|                 http://bounce.to/Roberts                  |
: >+-----------------------------------------------------------+
: >| If you think you understand Him,                          |
: >|               then you really do not know HIM !!          |
: >+-----------------------------------------------------------+

: ---
: Try a better search engine:  http://www.google.com
: My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Fujitsu sort work file assign, was.. NetExpress

_(reply depth: 7)_

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-12T12:52:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pl8us$pnj$6@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100> <8pj5fv$948$1@ins21.netins.net> <39bd6af0.516522@207.126.101.100>`

```
I sent the following note to Thane as an e-mail.  Since he replied to
the group, I thought it might be helpful to see the message.

==============================================

Thane:

I am still confused (I think).  The code from your book (see page 288)
uses file names which are longer than eight characters.  They don't seem
to generate error messages (though I just tried the first one).  Am I
at the right page of the book?  Is it something that is inconsistent in
Fujitsu (i.e. works sometimes, but not always).  Or was it an error that
was introduced after version 3.0 (which we are using)?  

I am following this up because I am fast approaching this material in our
course.  I know that every language implementation has its quirk, I just
feel more comfortable if I know what they are and how they work.

Floyd Johnson

==============================================

Thane Hubbell (thaneH@softwaresimple.com) wrote:
: I'm learning all kinds of things this week.

: First  - bill is right - the later versions issue an I level message
: if you use a value in quotes.

: Floyd is right - you can use more than 8 character names.

: I am right - the name has to be 8 characters or less?  How can that
: be?  Well, if I use "Whatever" it works fine.  If I use "Whatever1" i
: get an error message that states:


: JMN2948I-E  20  CHARACTER WHICH CONSTRUCTS FILE-IDENTIFIER IS INVALID.
: OR NAME OF FILE-IDENTIFIER EXCEEDS 8 CHARACTERS. 
:             NAME OF FILE-IDENTIFIER IS ASSUMED TO BE VALID. IF THE
: NAME EXCEEDS 8 CHARACTERS,FIRST 8 CHARACTERS IS 
:             ASSUMED TO BE VALID.


: I'm looking into this now.

: On 11 Sep 2000 17:41:19 GMT, floydj@netins.net (Floyd Johnson) wrote:

: >Are other uses of virtual file names similarly limited? or just the sort
: >work file?
: >
: >Floyd Johnson 
: >
: >Thane Hubbell (thaneH@softwaresimple.com) wrote:
: >: You are correct in general, but the assign of a sort work file (if you
: >: don't want an error message) has to be 8 characters or less with
: >: Fujitsu COBOL.
: >
: >--
: >--
: >+-----------------------------------------------------------+
: >|                      Floyd H. Johnson                     |
: >+-----------------------------+-----------------------------+    
: >| Voice  : (716) 594 - 0942   | 87 Parkway Drive            |
: >| E-Mail : floydj@netins.net  | North Chili, NY  14514      |
: >+-----------------------------+-----------------------------+
: >|                 http://bounce.to/Roberts                  |
: >+-----------------------------------------------------------+
: >| If you think you understand Him,                          |
: >|               then you really do not know HIM !!          |
: >+-----------------------------------------------------------+

: ---
: Try a better search engine:  http://www.google.com
: My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF net express

_(reply depth: 5)_

- **From:** Floyd Johnson <floydj@netins.net>
- **Date:** 2000-09-12T08:14:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39BE1E38.34E319B0@netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100> <8pijrv$t0i$1@ins21.netins.net> <39bcf94c.46896220@207.126.101.100>`

```
I sent the following note to Thane as an e-mail.  Since he replied to
the group, I thought it might be helpful to see the message.

Thane:

I am still confused (I think).  The code from your book (see page 288)
uses file names which are longer than eight characters.  They don't seem
to generate error messages ( though I just tried the first one).  Am I
at the right page of the book?  Is it something that is inconsistent in
Fujitsu (i.e. works sometimes, but not always).  Or was it an error that
was introduced after version 3.0 (which we are using)?  

I am following this up because I fast approaching this material in our
course.  I know that every language implementation has its quirk, I just
feel more comfortable if I know what they are and how they work.

Floyd Johnson


Thane Hubbell wrote:
> 
> You are correct in general, but the assign of a sort work file (if you
…[75 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MF net express

- **From:** floydj@netins.net (Floyd Johnson)
- **Date:** 2000-09-11T12:43:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pik1p$t0i$3@ins21.netins.net>`
- **References:** `<39bc32a1@news.server.worldonline.co.uk> <8phjft$giv$1@slb0.atl.mindspring.net> <39bc5733.5392202@207.126.101.100>`

```
My experience has been that Fujitsu file names can be longer than eight
characters, as long as they do not contain spaces.  For example I created
a demonstration program for my COBOL students using the name:

        FALL2000-DATADIVDEMOFinal.COB

I compiled, linked, and executed the file using the steps found in "TY
COBOL in 24 Hours" (i.e. I did not create a project).

Have I been lucky - or is something else going on?

Floyd Johnson


Thane Hubbell (thaneH@softwaresimple.com) wrote:
: fujitsu-has-a-bug won't work.  It has to be 8 characters or less.

: I use 

: Assign Sort-Work to Whatever.



: On Sun, 10 Sep 2000 22:27:38 -0500, "William M. Klein"
: <wmklein@nospam.ix.netcom.com> wrote:

: >To get your program to compile with Fujitsu,
: > Change your Select/Assign statement associated with your SD to something
: >like
: >
: >  Select SortFile Assign to Fujitsu-has-a-bug.
: >        instead of
: >   Select SortFile Assign to "ANSI-Allows.This".
: >
: >(This "bug" in Fujitsu is fixed in later versions of their compiler)
: >
: >--
: >Bill Klein
: >    wmklein <at> ix dot netcom dot com
: >"Gandalf" <nhaire@bigfoot.com> wrote in message
: >news:39bc32a1@news.server.worldonline.co.uk...
: >> Any idea where I can DL this from?
: >> I am using MF personal at the moment but it does not produce EXE files, I
: >> have used the brilliant Fujitsu compiler but it did not like one of my sort
: >> programs, I got the error message "SORT-MERGE FILE CAN ONLY SPECIFY
: >> FILE-IDENTIFIER IN ASSIGN CLAUSE". MF personal compiled the prog OK !!
: >> Thanks
: >> Nigel
: >>
: >>
: >
: >

: ---
: Try a better search engine:  http://www.google.com
: My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
