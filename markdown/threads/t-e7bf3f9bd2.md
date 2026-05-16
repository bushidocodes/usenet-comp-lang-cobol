[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# call cobol from pl/i using pointers

_4 messages · 4 participants · 2004-07_

---

### call cobol from pl/i using pointers

- **From:** piero.crincoli@infoconsulting.it (Piero Crincoli)
- **Date:** 2004-07-29T02:31:18-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<60905137.0407290131.c4b9854@posting.google.com>`

```
I have to write a cobol routine called from pl/i.

In pl/i I have:

pointer1=addr(area1)
pointer2=addr(area2)
call routine(pointer1, pointer2, variable1, variable2).

What about cobol program? Is the following correct?

linkage section.
  01 pointer1
  01 area1
  01 pointer2
  01 area2
  01 variable1
  01 variable2

procedure division using pointer1, pointer2, variable1, variable2.
  set address of area1 to pointer1
  set address of area2 to pointer2   
  ...

thanks   piero
```

#### ↳ Re: call cobol from pl/i using pointers

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-29T10:42:15+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<4108d424.155882015@news.optonline.net>`
- **References:** `<60905137.0407290131.c4b9854@posting.google.com>`

```
piero.crincoli@infoconsulting.it (Piero Crincoli) wrote:

>I have to write a cobol routine called from pl/i.
>
…[18 more quoted lines elided]…
>  set address of area2 to pointer2   

Yes, it appears to be correct.
```

#### ↳ Re: call cobol from pl/i using pointers

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-07-29T13:13:17+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<NJ6Oc.1900$cK.207@newsread2.news.pas.earthlink.net>`
- **References:** `<60905137.0407290131.c4b9854@posting.google.com>`

```
If you are running in a (supported) IBM mainframe environment, then I would
suggest you review the chapter

  " Chapter 11.  Communicating between COBOL and PL/I "

In the ILC (Inter-Language Call) manual at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA4120/CCONTENTS

This will answer this (and a variety of other) questions.

If you are NOT running on an IBM mainframe, then the answer to your question is
"probably - but not necessarily"
```

#### ↳ Re: call cobol from pl/i using pointers

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-07-29T13:43:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040729094325.29660.00002349@mb-m16.aol.com>`
- **References:** `<60905137.0407290131.c4b9854@posting.google.com>`

```
Piero Crincoli writes ...

>I have to write a cobol routine called from pl/i.
>
…[18 more quoted lines elided]…
>  set address of area2 to pointer2  

Looks good to me on a cursory inspection. But you haven't told us the compilers
nor the operating system - there may be some differences that are important
based on your context.

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
