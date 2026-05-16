[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# micro focus cobol

_7 messages · 6 participants · 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### micro focus cobol

- **From:** wesleybig <allen.wesley@wakefern.com>
- **Date:** 2003-10-17T11:57:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3493895.1066406225@dbforums.com>`

```

USING NET EXPRESS AND MICROFOCUS COBOL

I WOULD LIKE TO KNOW WHAT PRINTER CONTROL CHARACTERS I CAN INPUT INTO MY
COBOL PROGRAM TO MAKE MY HP PRINTER CONVERT FROM PORTAIT TO LANDSCAPE
AND BACK AGAIN FOR A REPORT.

IN ADDITION I WOULD LIKE TO SET THE PRINTER TO A CONDESED PRINT MODE AND
BACK AGAIN.





HELP!!!
```

#### ↳ Re: micro focus cobol

- **From:** "Russell Styles" <rws0202@comcast.net>
- **Date:** 2003-10-17T14:21:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-OmcnRnI4OGvrg2iU-KYjA@comcast.com>`
- **References:** `<3493895.1066406225@dbforums.com>`

```

"wesleybig" <allen.wesley@wakefern.com> wrote in message
news:3493895.1066406225@dbforums.com...
>
> USING NET EXPRESS AND MICROFOCUS COBOL
…[16 more quoted lines elided]…
> Posted via http://dbforums.com

    Here is a segment from a config file I use.  The format should be
obvious -
-DATA is literal, -XDATA are hexadecimal.  Note that this data will need to
be
sent either from a dos application, or to the raw printer, and requires HP
compatability.

    Also note that upper/lower case IS significant.  Lower case L and "one"
are not the same.
Ditto zero and oh.



RESET-XDATA=1B45
; Use letter size paper
RESET-XDATA=1B
RESET-DATA=&l2A


;*******************************
; Portrait, 6 LINES PER INCH
132-COL-XDATA=1B
132-COL-DATA=&l0o6D
; PC-8 SYMBOL SET
132-COL-XDATA=1B
132-COL-DATA=(10U
; Fixed, 16.67 pitch, height=8.5 points, upright,
; Medium (not light or bold), Line printer
132-COL-XDATA=1B
132-COL-DATA=(s0p16.67h8.5v0s0b0T


; set to 10 pitch Courier PC-8 medium upright
80-COL-XDATA=1B
80-COL-DATA=(10U
80-COL-XDATA=1B
80-COL-DATA=(s0p10.00h12.0v0s0b3T
; PORTRAIT, 6 LINES INCH
80-COL-XDATA=1B
80-COL-DATA=&l0o6D


; Set to landscape
; Use reset to get back to portrait.  Do 132-col 1st !!!!!
SET-TO-LANDSCAPE-XDATA=1B
SET-TO-LANDSCAPE-DATA=&l1O
; 8 lines per inch.
SET-TO-LANDSCAPE-XDATA=1B
SET-TO-LANDSCAPE-DATA=&l8D
```

#### ↳ Re: micro focus cobol

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-10-17T18:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F9036AE.C67CC481@shaw.ca>`
- **References:** `<3493895.1066406225@dbforums.com>`

```


wesleybig wrote:

> USING NET EXPRESS AND MICROFOCUS COBOL
>
…[7 more quoted lines elided]…
> HELP!!!

Several ways you can do it :-

1. Got to know all the control characters applicable to your specific
printer and send the controls for portrait, landscape, condensed, expanded
etc. - a real pain !

2. Third party tools like Flexus SP2, Crystal Reports and a recent one, RPV.

3. Check the on-line help for a list of Micro Focus PC_PRINT routines. There
are samples of PC_PRINTing and other printing features at :-

http://supportline.microfocus.com/examplesandutilities/nesamp.asp

N/E Versions 3 and 4 have same routines, but if you are using V 4.0 there
are some enhancements over V 3.

PS: Also sign up for M/F's Answer Exchange, (a freebie), where you can raise
queries about Net Express, or glean from other developers' questions.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: micro focus cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-10-17T14:33:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0310171333.4e4be75a@posting.google.com>`
- **References:** `<3493895.1066406225@dbforums.com> <3F9036AE.C67CC481@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote 

> 1. Got to know all the control characters applicable to your specific
> printer and send the controls for portrait, landscape, condensed, expanded
> etc. - a real pain !

Also unlikely to work with a Windows program using a Windows print
driver.  Its OK to do this with DOS programs and accessing the port
directly.
```

###### ↳ ↳ ↳ Re: micro focus cobol

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-10-17T23:12:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F9077B2.CCCAD513@shaw.ca>`
- **References:** `<3493895.1066406225@dbforums.com> <3F9036AE.C67CC481@shaw.ca> <217e491a.0310171333.4e4be75a@posting.google.com>`

```


Richard wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote
>
…[6 more quoted lines elided]…
> directly.

Yes Richard - I should have added that. Via Windows it's really only the other
alternatives that apply. Interestingly in the U of Limerick samples there is/are
print program(s) - BUT - they are written to file ! Then you gotta print them
yourself.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: micro focus cobol

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-10-20T12:43:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<usl7pvge8o79aa6aea1r4eupnkgcfnp9jb@4ax.com>`
- **References:** `<3493895.1066406225@dbforums.com> <3F9036AE.C67CC481@shaw.ca>`

```
Jimmy:

Thanks for the mention.  Just a comment.....

OUr sp2 product is designed to produce and control GUI screens for
COBOL programs.  While it is possible to use our Active X add-on to
control a Crystal Reports OCX control, we also have a product which is
designed specifically to support COBOL printing directly to the
Windows Print Manager.

That product is called FormPrint.

One more note....Both sp2 and FormPrint work with our Thin Client
product.  This means you can use FormPrint and Thin Client to send
printed output across the Internet to remote client PC's and obtain
robust printed documents through the Windows Print Manager across the
Internet.

Thanks again for the mention!



"James J. Gavan" <jjgavan@shaw.ca> wrote:

>
>
…[32 more quoted lines elided]…
>Jimmy, Calgary AB


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: micro focus cobol

- **From:** MFDEVP <member27090@dbforums.com>
- **Date:** 2003-10-17T15:19:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3494932.1066418376@dbforums.com>`
- **References:** `<3493895.1066406225@dbforums.com>`

```

We are using the MicroFocus Cobol on CICS application server , and how

this command COBSW=-l0 will improve the system performance?

could anybody please help me to figure out this ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
