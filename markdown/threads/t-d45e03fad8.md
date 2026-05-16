[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please help me out!

_7 messages · 7 participants · 1999-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Please help me out!

- **From:** Charlie Ting <cting2@learn.senecac.on.ca>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3817E299.2BCDA80A@learn.senecac.on.ca>`

```
I'm new to COBOL...I wrote a simple program...but I got an error
message..it goes like this.. STATISTICS: HIGHEST SEVERITY CODE=I,
PROGRAM UNIT=1

I don't know what this represents...please help me..thanks..
```

#### ↳ Re: Please help me out!

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kV6S3.689$DM3.10267@news4.mia>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca>`

```
SEVERITY CODES ARE:
(I)nformational     FYI, may mean nothing, such as can't code values in FD /
CD  (Ret-code 2)
(W)arning            means might be a problem, take a look for sure
(Ret-code 4)
(E)rror                  means you mad a boo-boo, better see what you need
to fix as compiler
                             can't guarantee program will run
(Ret-code 8)
(S)evere              No way can I even compile this mess!
(Ret-code 12 or 16)

an I is fairly common in productoin programs due to use of copybooks.


Charlie Ting wrote in message <3817E299.2BCDA80A@learn.senecac.on.ca>...
>I'm new to COBOL...I wrote a simple program...but I got an error
>message..it goes like this.. STATISTICS: HIGHEST SEVERITY CODE=I,
…[4 more quoted lines elided]…
>
```

#### ↳ Re: Please help me out!

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38184182.67429404@news1.attglobal.net>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca>`

```
On Thu, 28 Oct 1999 01:43:53 -0400, Charlie Ting
<cting2@learn.senecac.on.ca> wrote:

>I'm new to COBOL...I wrote a simple program...but I got an error
>message..it goes like this.. STATISTICS: HIGHEST SEVERITY CODE=I,
…[3 more quoted lines elided]…
>

The severity codes (I can tell you are using Fujitsu) are, in order of
Severity - I, W, S, E (C is possible, but I've not see it yet with
Fujitsu).

This is NOT from the Fujitsu docs, this is what I understand these to
really mean:

I - Informational - No real errors
W - Compiled, linkabke, but with some Warning message
S - Syntax error, but may still be linkable - some assumptions were
made by the compiler.
E - Error - not linkable, Error in compile.

Hope that helps - The I just means you have no errors and you can
continue to the link.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Please help me out!

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381848FE.DFF264E3@zip.com.au>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca>`

```
Charlie Ting wrote:
> 
> I'm new to COBOL...I wrote a simple program...but I got an error
…[3 more quoted lines elided]…
> I don't know what this represents...please help me..thanks..

This means that you have some informational messages.

You have done well no errors, no warnings.

Now on to testing,
Ken
```

##### ↳ ↳ Re: Please help me out!

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38185908.EA16CDAF@NOSPAMhome.com>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca> <381848FE.DFF264E3@zip.com.au>`

```
Ken Foskey wrote:
> 
> Charlie Ting wrote:
…[12 more quoted lines elided]…
> Ken

But, first READ your informational messages.  Usually you don't care
about them, but occasionally they are significant to your needs.
```

###### ↳ ↳ ↳ Re: Please help me out!

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rJ3S3.346$iS.19179@viper>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca> <381848FE.DFF264E3@zip.com.au> <38185908.EA16CDAF@NOSPAMhome.com>`

```
>But, first READ your informational messages.  Usually you don't care
>about them, but occasionally they are significant to your needs.

Always verify the Informational and Warning mesages will not affect the
logic in your programs. These do typically refer to logic errors, such as
Wrning about never executing a paragraph. Or Warning about redefining a
larger field, thus not processing the entire width of the field.

The only Informational error I can remember off the top of my head, is the
Fast Sort option enabled/disabled for a SORT file.
```

###### ↳ ↳ ↳ Re: Please help me out!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wq5S3.754$hp5.26937@dfiatx1-snr1.gtei.net>`
- **References:** `<3817E299.2BCDA80A@learn.senecac.on.ca> <381848FE.DFF264E3@zip.com.au> <38185908.EA16CDAF@NOSPAMhome.com>`

```
Howard Brazee wrote in message <38185908.EA16CDAF@NOSPAMhome.com>...
>>
>
>But, first READ your informational messages.  Usually you don't care
>about them, but occasionally they are significant to your needs.

The "informational message" I always look for is the one in IBM COBOL/390
(it was also in VS COBOL II) that says, "the code from line 123 to 456 could
never be executed and therefore was discarded."

That usually means I have a misplaced period or scope terminator, which is
always worth finding before running the program.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
