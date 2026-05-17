[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF screen displays problem

_5 messages · 2 participants · 1995-05_

---

### MF screen displays problem

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-05-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3qfv9m$s1b@wrdis02.robins.af.mil>`

```
We are having a problem with screens generated in MF.

The following example will only show the _last_ value (10)
in the output field, even when stepped through.

Yet the same code without the blank screen will show an incrementing
value, although it is the value from the previous display, ie, if
sub=02, then 01 will be displayed.

The blank screen obviously has some side effects that I don't
understand, and the screens appear to be buffered.

Would someone please enlighten me?

Thanks


IDENTIFICATION DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.

01 G-002 PIC XX.

01 sub pic 99.
01 sub2 pic 9999.

SCREEN SECTION.

01 G-TEST.
02 BLANK SCREEN.
02 LINE 1 COL 1 VALUE "sample screen".
02 LINE 6 COL 1 VALUE "output field [ ]".
02 LINE 6 COL 15 PIC XX USING G-002.
PROCEDURE DIVISION.
DISPLAY G-TEST.
perform 100-loop varying sub from 1 by 1 until sub > 10.
STOP RUN.

100-loop.

move sub to g-002.
display g-test.
perform 110-wait varying sub2 from 1 by 1 until sub2 > 1000.

110-wait.
exit.

Jon R. Wilson
jwi··.@b85··f.mil
```

#### ↳ Re: MF screen displays problem

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-05-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5f9babf7d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3qfv9m$s1b@wrdis02.robins.af.mil>`
- **References:** `<3qfv9m$s1b@wrdis02.robins.af.mil>`

```
In article <3qfv9m$s.··.@wrd··f.mil>, jwi··.@b85··f.mil
says...
›
› The following example will only show the _last_ value (10)
› in the output field, even when stepped through.

I stepped this through using text animator and using anim2 under NT and
got it updating the field on each display.

›
› Yet the same code without the blank screen will show an incrementing
› value, although it is the value from the previous display, ie, if
› sub=02, then 01 will be displayed.

didn't get this at all. What version and what machine/CPU/OS were you
using?

› 
› 
…[28 more quoted lines elided]…
› exit.                                                        

Not the best way to do a wait as it's CPU speed and load dependant as
well as graphics card speed dependant. ACCEPTing from TIME would be more
accurate. Why use a delay loop though? it just hogs the CPU slowing other
processes down.

Shaun
```

##### ↳ ↳ Re: MF screen displays problem

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-05-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5f9babf7d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5f9babf7d-p2@usenetarchives.gap>`
- **References:** `<3qfv9m$s1b@wrdis02.robins.af.mil> <gap-f5f9babf7d-p2@usenetarchives.gap>`

```
s.··.@mfl··o.uk (Shaun C. Murray) wrote:

› In article <3qfv9m$s.··.@wrd··f.mil>, jwi··.@b85··f.mil 
› says...
›› 
›› The following example will only show the _last_ value (10)
›› in the output field, even when stepped through.
 
› I stepped this through using text animator and using anim2 under NT and 
› got it updating the field on each display.
 
›› 
›› Yet the same code without the blank screen will show an incrementing
›› value, although it is the value from the previous display, ie, if 
›› sub=02, then 01 will be displayed.
 
› didn't get this at all. What version and what machine/CPU/OS were you 
› using?

MF workbench 3.2.43, animator version 2 version 7.8.01, 486 DX 33 PC
DOS 6.21 running under Windows 3.1

›› 
›› 
…[28 more quoted lines elided]…
›› exit.                                                        
 
› Not the best way to do a wait as it's CPU speed and load dependant as 
› well as graphics card speed dependant. ACCEPTing from TIME would be more 
› accurate. Why use a delay loop though? it just hogs the CPU slowing other 
› processes down.

It was just a sample. I needed to slow it down enough to verify that
the numbers were not just flashing by when running at full speed.
This is not the production code that demonstrated the problem, just a
simple recreation of it.

(I'll remember that I'm being graded next time :-)

Jon Wilson
```

###### ↳ ↳ ↳ Re: MF screen displays problem

- **From:** "jwi..." <ua-author-17071930@usenetarchives.gap>
- **Date:** 1995-05-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5f9babf7d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5f9babf7d-p3@usenetarchives.gap>`
- **References:** `<3qfv9m$s1b@wrdis02.robins.af.mil> <gap-f5f9babf7d-p2@usenetarchives.gap> <gap-f5f9babf7d-p3@usenetarchives.gap>`

```
› s.··.@mfl··o.uk (Shaun C. Murray) wrote:
 
››› The following example will only show the _last_ value (10)
››› in the output field, even when stepped through.
 
›› I stepped this through using text animator and using anim2 under NT and 
›› got it updating the field on each display.

Since you said it works under NT, I tried a few other things...

Amazingly enough, the same code works properly using the DOS tools
instead of Windows. It also works properly on a Sun.

So, now that we've narrowed it down, how do I get around it?


Jon R. Wilson
jwi··.@b85··f.mil
```

###### ↳ ↳ ↳ Re: MF screen displays problem

_(reply depth: 4)_

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-05-31T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5f9babf7d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5f9babf7d-p4@usenetarchives.gap>`
- **References:** `<3qfv9m$s1b@wrdis02.robins.af.mil> <gap-f5f9babf7d-p2@usenetarchives.gap> <gap-f5f9babf7d-p3@usenetarchives.gap> <gap-f5f9babf7d-p4@usenetarchives.gap>`

```
In article <3qicrq$h.··.@wrd··f.mil>, jwi··.@b85··f.mil
says...
› Amazingly enough, the same code works properly using the DOS tools
› instead of Windows. It also works properly on a Sun.
›
› So, now that we've narrowed it down, how do I get around it?

Just tried it on Windows now. It does go wrong somehow. I'll raise a PDR
(Product Discrepancy Report) and mail you the PDR#. Get in touch with
your support rep and quote that number at him.

As to working around it, I don't rightly know how without a major
investigation. I'll leave that to the ADIS/Panels 2 guys.

Shaun
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
