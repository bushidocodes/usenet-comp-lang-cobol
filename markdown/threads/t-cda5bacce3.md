[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# KOBOL

_5 messages · 4 participants · 2004-06 → 2004-07_

---

### KOBOL

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-06-19T02:32:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uBNAc.17667$V57.3262560@news4.srv.hcvlny.cv.net>`

```
I've always said, I'm a slow learner, but better a slow learner than a 
no learner.

Consequentially, today I was forced to look at Kobol.

An on line example is available for the simplest of things. HELLO.

A free evaluation copy can be downloaded for the Windows, 2 ways if I
understand it, and for Linux in various distributions.

Bored to tears with the TV, I looked at the example code in the 
evaluation system. At least that's what I believe it was.

While the code is COBOL, I hope it isn't an example of normal
programming, and wondered if any of you have opinions to
share. I would hate to try to fix a program using that STYLE.
I found the use of COPY so extensive I wonder if anyone reads
these programs.

Warren Simmons
```

#### ↳ Re: KOBOL

- **From:** "KNOCHG" <knochg@wi.rr.com>
- **Date:** 2004-07-02T23:42:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8905d6faded9113fd133cbc0ebc32cc5@localhost.talkaboutprogramming.com>`
- **References:** `<uBNAc.17667$V57.3262560@news4.srv.hcvlny.cv.net>`

```
I
```

#### ↳ Re: KOBOL

- **From:** "KNOCHG" <knochg@wi.rr.com>
- **Date:** 2004-07-03T00:01:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aebd8851bb9a1c16c224c3026a51e716@localhost.talkaboutprogramming.com>`
- **References:** `<uBNAc.17667$V57.3262560@news4.srv.hcvlny.cv.net>`

```
I am sorry you did not find the examples helpful.  Rather than try to teach
COBOL they were intended to allow people to get the nuances of the KOBOL
compiler.  Further, I was in a hurry to get them out and should have spent
more time organizing them for the people using them.   

The use of copy files enables me to use the same code for Microfocus,
Fujitsu, Kobol Windows, and Kobol in Linux. As an example I have a file
"C:\KOBOL\WS\SBP.WS" which contains the working storage for the data
elements of the Special Names Paragraph.  the file "C:\FSC\WS\SBP.WS" 
contains the working storage for the special names paragraph when the code
is compiled under Fujitsu.  

Therefore:  I only need to change the copy statements to allow the code to
compile in any of the 4 types of operating systems.  For Linux I use
"c:/windows/KOBOL/WS/SBP.ws" and copy from the windows drive using SUSE. 
Therefore, a change in a module is carried through to all 4 test
environments.  

KOBOL is able to run almost all examples from SAMS Teach yourself COBOL in
24 hours.  Simply remove the first line and the examples run well.  I use
a .bat file for each program.  Sometimes I will use the IDE therefore the
KOB files can be used to generate files for specifec programs.

The included examples covered how to use copy statements, how to use files
assigned to both disk and to a literal, how to use function keys, the use
of screens, the use of tables, searching, the use of binary, and of course
how to print.  

As I am not a professional programer, perhaps you can help me create
better written examples for KOBOL. Your input would be appreciated both by
me and I am sure the people at TheKompany. 

This is an excellent compiler that has shown itself to be very fast and
does not have the restrictions that the MICROFOCUS compiler that I use
has.

I have used tables exceeding 400 entries, and there does not seem to be
any restriction on the size of the tables. 
The system allows for color on screens, function keys, and basically
everything I need so far.
```

##### ↳ ↳ Re: KOBOL

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-07-03T12:42:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0407031142.6d592147@posting.google.com>`
- **References:** `<uBNAc.17667$V57.3262560@news4.srv.hcvlny.cv.net> <aebd8851bb9a1c16c224c3026a51e716@localhost.talkaboutprogramming.com>`

```
"KNOCHG" <knochg@wi.rr.com> wrote 

> The system allows for color on screens, function keys, and basically
> everything I need so far.

When I last looked there was no file sharing or record locking.  This
means that it stays firmly single user.  I understand that it may
include SQL at some point which would hopefully cater for multi-user
access.
```

###### ↳ ↳ ↳ Re: KOBOL

- **From:** "KNOCHG" <knochg@nospam.wi.rr.com>
- **Date:** 2004-07-03T21:57:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1684e5f9915cff733a0036f49da51f3@localhost.talkaboutprogramming.com>`
- **References:** `<uBNAc.17667$V57.3262560@news4.srv.hcvlny.cv.net> <aebd8851bb9a1c16c224c3026a51e716@localhost.talkaboutprogramming.com> <217e491a.0407031142.6d592147@posting.google.com>`

```
I am not sure if the system can handle multi-user.   I will E-Mail
TheKompany.com and ask Shawn Gordon.  Perhaps you can test it on a
multi-user platform?  Documentation is laking which is unfortunate because
it is a good product.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
