[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sections vs Paragraphs

_3 messages · 3 participants · 1999-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Sections vs Paragraphs

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3713483C.CFEF94F@NOSPAMhome.com>`
- **References:** `<371255EA.7E1F6A4F@NOSPAMhome.com> <19990412183800.02097.00002057@ng115.aol.com>`

```
Twymer wrote:
> 
> I would agree wholeheartedly, except that I have just spent twom months
…[8 more quoted lines elided]…
> TW

Perform through seems to me to be even worse than sections.  I prefer no
drop throughs at all for readibilitiy and maintainability.  Maybe after
the next standard is out, more people will agree with me.
```

#### ↳ Re: Sections vs Paragraphs

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7evk49$7jp$1@news.cerf.net>`
- **References:** `<371255EA.7E1F6A4F@NOSPAMhome.com> <19990412183800.02097.00002057@ng115.aol.com> <3713483C.CFEF94F@NOSPAMhome.com>`

```
Howard Brazee wrote in message <3713483C.CFEF94F@NOSPAMhome.com>...
>Perform through seems to me to be even worse than sections.  I prefer no
>drop throughs at all for readibilitiy and maintainability.  Maybe after
>the next standard is out, more people will agree with me.

Perform through is a statement I cannot with my best will see why were
implemented. If one wishes to make a cobol program impossible to understand,
that's it!

Cheesle
```

##### ↳ ↳ Re: Sections vs Paragraphs

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u1zlJmhh#GA.349@nih2naad.prod2.compuserve.com>`
- **References:** `<371255EA.7E1F6A4F@NOSPAMhome.com> <19990412183800.02097.00002057@ng115.aol.com> <3713483C.CFEF94F@NOSPAMhome.com> <7evk49$7jp$1@news.cerf.net>`

```
Yes, that's a large part of the problem. The problem is that, unlike every
other programming language (I think), in Cobol the execution-time behavior
of a paragraph is not entirely specified/controlled by the paragraph
itself, it's not really a closed procedure per se - it varies depending on
the whim of the referring code, e.g. whether goto, fall thru, perform,
perform thru, etc. This problem is eliminated by standardizing on only one
way to reach any label (except the initial start), and the best one to
choose obviously is Perform without Thru.

I'm not talking about flags or values input to the procedure having an
effect on its internal flow, that's OK. But the code as a whole should do
the same thing for any given set of input values. With multiple ways to
reach the code and different behavior for them, Cobol severely blew it.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!


Cheesle wrote in message <7evk49$7jp$1@news.cerf.net>...

>Perform through is a statement I cannot with my best will see why were
>implemented. If one wishes to make a cobol program impossible to
understand,
>that's it!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
