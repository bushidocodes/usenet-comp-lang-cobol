[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

_7 messages · 4 participants · 2002-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** "S M Trushell" <strush3@home.com>
- **Date:** 2002-01-08T13:28:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com>`

```
Greetings,

In program READTAB.CBL, I have created and have successfully read a
tab-delimited file(ORG is LINE SEQUENTIAL), straight forward.
I am now trying to parse records from the tab-delimited file.
For each record read, I want to determine number of tabs in that record
using INSPECT:

           INSPECT fd-tab-infile-record
        TALLYING tab-count FOR ALL (**TAB CHAR**)
           DISPLAY 'tab count is  : ' tab-count.

I am unable to find literal value for tab-character (**TAB CHAR**) to use in
this case.
I am using MicroFocus Cobol V3.4.18.

Please advise.

TIA

S M Trushell
```

#### ↳ Re: Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2002-01-08T13:48:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3AF7DA.F5CE0649@rr.com>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com>`

```
The TAB character has a value of 9, which I believe you may specify as
"0x09" in Microfocus (someone please correct me if I'm wrong).  Exact
syntax for expressing hexadecimal value varies among vendors, so I
typically prefer using decimal values, as follows:

01	TAB-CHAR.
	03 filler	pic 99 comp value 9.

This generally works fine, except that some compliers want to store
everything as words rather than bytes and may require a special
directive in order to allow for single-character values.

A greater problem you will encounter is that Microfocus typically
expands tabs into spaces when reading line sequential files.  This was
the topic of an earlier thread about a month or two ago, and
unfortunately there is no *easy* solution.  In the past, I have relied
upon an assembly language routine to read such files.
```

##### ↳ ↳ Re: Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2002-01-09T02:21:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3BA852.D13EF5DA@rr.com>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com> <3C3AF7DA.F5CE0649@rr.com>`

```

> The TAB character has a value of 9, which I believe you may specify as
> "0x09" in Microfocus (someone please correct me if I'm wrong).  Exact
> syntax for expressing hexadecimal value varies among vendors ...

On second thought, I think in Microfocus you would specify the
hex value as:
			pic x value x"09".

Your syntax for the inspect statement itself is correct.
```

##### ↳ ↳ Re: Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-01-09T03:27:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oMO_7.240588$WW.12997901@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com> <3C3AF7DA.F5CE0649@rr.com>`

```

"leclaire" <leclaire@rr.com> wrote in message
news:3C3AF7DA.F5CE0649@rr.com...
> The TAB character has a value of 9, which I believe you may specify as
> "0x09" in Microfocus (someone please correct me if I'm wrong).  Exact
…[14 more quoted lines elided]…
> upon an assembly language routine to read such files.

    Then they must have mentioned the runtime switch
that allows it to NOT expand tabs.
```

###### ↳ ↳ ↳ Re: Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2002-01-09T03:45:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3BBC26.10912405@rr.com>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com> <3C3AF7DA.F5CE0649@rr.com> <oMO_7.240588$WW.12997901@bgtnsc05-news.ops.worldnet.att.net>`

```

Russell Styles wrote:
> 
> "leclaire" <leclaire@rr.com> wrote in message
…[7 more quoted lines elided]…
> that allows it to NOT expand tabs.

As I recall, the only reference made at that time with any certainty 
was that the (-T) switch, or the comparable runtime call, was that
they only affected tab expansion on WRITE operations, not on READ.

As always, I could be wrong but that's what I remember of the thread.
```

###### ↳ ↳ ↳ Re: Q: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-01-10T05:25:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TA9%7.242860$WW.13105290@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com> <3C3AF7DA.F5CE0649@rr.com> <oMO_7.240588$WW.12997901@bgtnsc05-news.ops.worldnet.att.net> <3C3BBC26.10912405@rr.com>`

```

"leclaire" <leclaire@rr.com> wrote in message
news:3C3BBC26.10912405@rr.com...
>
> Russell Styles wrote:
…[15 more quoted lines elided]…
> As always, I could be wrong but that's what I remember of the thread.

    I stand (sit) corrected.  I looked at the documentation this time
(what a concept).
```

#### ↳ Re: Performing INSPECT on Tab-delimited File in MFCOBOL V3.4.18

- **From:** "JerryMouse" <jerrymouse@invalid.com>
- **Date:** 2002-01-09T16:11:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wYZ_7.590358$8q.47603505@bin2.nnrp.aus1.giganews.com>`
- **References:** `<_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com>`

```

"S M Trushell" <strush3@home.com> wrote in message
news:_tC_7.326661$ez.46822820@news1.rdc1.nj.home.com...
> Greetings,
>
…[9 more quoted lines elided]…
>

Try:

TALLYING tab-count FOR ALL X'09'

However, this fails for consecutive occurances of the tab character.

It is left as an exercise for the reader to discover why. (Hint: the command
would fail for the same reason if you were looking for "A" - it has nought
to do with tab.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
