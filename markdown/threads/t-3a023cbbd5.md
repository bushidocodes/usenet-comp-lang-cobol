[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Misc comments on GOTO, packed data, and flowcharts

_2 messages · 2 participants · 2000-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Misc comments on GOTO, packed data, and flowcharts

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392C627C.75AF2674@istar.ca>`
- **References:** `<8g50aa$sj@netaxs.com> <8g7p5k014l0@enews4.newsguy.com>`

```
>From a performance point of view on a modern compiler, presence of a GO
TO will probably disrupt PERFORM optimization because the control flow
isn't guaranteed. PERFORM optimization on the COBOL II compilers and
later for the MVS, VSE and VM operating systems on S390 computers
includes generating PERFORM statements that don't reset the EXIT or
implied exit to fall through to the next paragraph and in some cases
replacing the PERFORM statement with the code from the paragraph being
performed so that no branching is done.  In this case where a GO TO exit
paragraph would be used, the more optimal code would be IF NOT
exit-condition PERFORM rest-of-process.  The code in rest-of-process may
well be moved to immediately follow the IF NOT exit-condition (or an
ELSE statement) so that there is not an extra transfer of control.

In general if my IF statements start nesting too deeply I split off the
inner nestings to a separate paragraph because there is zero to minimal
overhead in doing so.

Clark Morris, CFM Technical Programming Services Inc. cfmtech@istar.ca 

Jeff Baynard wrote:
> 
> I agree 100%.
…[18 more quoted lines elided]…
> > break apart a complex IF/ELSE with multiple nestings is not easy.
```

#### ↳ Re: Misc comments on GOTO, packed data, and flowcharts

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d48X4.105$Gh.12107@typhoon.austin.rr.com>`
- **References:** `<8g50aa$sj@netaxs.com> <8g7p5k014l0@enews4.newsguy.com> <392C627C.75AF2674@istar.ca>`

```
Clark F. Morris, Jr. <cfmtech@istar.ca> wrote in
> In general if my IF statements start nesting too deeply I split off the
> inner nestings to a separate paragraph because there is zero to minimal
> overhead in doing so.

an additional benefit is that you get a free comment as to what the
statement is doing (if you use a meaningful name for the paragraph).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
