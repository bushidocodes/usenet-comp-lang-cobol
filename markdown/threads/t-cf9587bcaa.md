[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I print without advancing a line?

_4 messages · 3 participants · 1999-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: How do I print without advancing a line?

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37137CDC.37C@compaq.com>`
- **References:** `<kGEQ2.11372$Jc7.532271@news2.giganews.com> <3713375d.128923218@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On Tue, 13 Apr 1999 11:05:41 +0100, "Jim" <jimyt@REMOVEMEyahoo.com>
…[10 more quoted lines elided]…
> Write Print-Line with No Advancing.

The WITH NO ADVANCING phrase is for DISPLAY, not WRITE. "WRITE 
whatever BEFORE ADVANCING 0" works if the implementation is conforming 
- that is, if it knows that you are writing to a printer.  Nobody 
should have to worry about escape sequences.  You should realize that 
when you specify "WRITE whatever" and have no ADVANCING clause, the 
default is "WRITE whatever AFTER ADVANCING 1 LINE".  For that reason, 
many people make the very first WRITE after the OPEN a "WRITE whatever 
BEFORE ADVANCING 0" so you don't get a blank line as the first one.  
That may be your problem.
```

#### ↳ Re: How do I print without advancing a line?

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1tvQXhh#GA.366@nih2naad.prod2.compuserve.com>`
- **References:** `<kGEQ2.11372$Jc7.532271@news2.giganews.com> <3713375d.128923218@news1.ibm.net> <37137CDC.37C@compaq.com>`

```
There could also be some interaction with compile options (e.g. Adv/NoAdv),
depending on your environment. The presence/absence of Advancing clauses
may determine a default which overrides the installation default, but
actual selected options (e.g. via parm or control statements) may override
that.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: How do I print without advancing a line?

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OxKkRXhh#GA.309@nih2naad.prod2.compuserve.com>`
- **References:** `<kGEQ2.11372$Jc7.532271@news2.giganews.com> <3713375d.128923218@news1.ibm.net> <37137CDC.37C@compaq.com>`

```
Also if not using Advancing and if using control characters, + means
overprint.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: How do I print without advancing a line?

- **From:** John Piggott <John_Piggott@compuserve.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3715133E.392B@compuserve.com>`
- **References:** `<kGEQ2.11372$Jc7.532271@news2.giganews.com> <3713375d.128923218@news1.ibm.net> <37137CDC.37C@compaq.com>`

```
Alternatively, use report writer to write your line. All the 
implementations I know allow:

    LINE PLUS 0  (or LINE PLUS ZERO)
  
> Thane Hubbell wrote:
> >
…[28 more quoted lines elided]…
> No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
