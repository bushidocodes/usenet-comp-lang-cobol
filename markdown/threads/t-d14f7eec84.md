[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Crystal Reports Engine & COBOL

_6 messages · 4 participants · 1998-10 → 1998-11_

---

### Crystal Reports Engine & COBOL

- **From:** swolfson1@my-dejanews.com
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71aq93$cio$1@nnrp1.dejanews.com>`

```
I would like to use the Crystal Reports Engine API with Acucobol.  Does anyone
have routines for calling the engine from any COBOL that they are willing to
share?

Many thanks

Steve Wolfson

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Crystal Reports Engine & COBOL

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3639DCA7.512F659C@IMN.nl>`
- **References:** `<71aq93$cio$1@nnrp1.dejanews.com>`

```
Our approach: Write a little Vis.Basic program containing the Crystal Reports'
ActiveX and call that program from COBOL, passing the wanted report as a (string)
parameter. We ourself have the VB program ask the user (by modal dialog) if they
want a screen preview or direct hardcopy (dialog screen with 2-option
radiobutton-set and OK/Cancel push buttons). But first, before the preview/print
dialog screen, the passed report name is checked if it needs specific user entered
data, f.e. a customer number, reporting period a.s.o. If needed, a report-specific
screen is showed first to enable this data be entered. After that the standard
dialog appears.

I'll see if out (still under development) program source may be shared with you,
and for that purpose I'll CC this reply to my collegue:

    Paul, would you mail the VBasic source to swolfson1@my-dejanews.com ?

swolfson1@my-dejanews.com wrote:

> I would like to use the Crystal Reports Engine API with Acucobol.  Does anyone
> have routines for calling the engine from any COBOL that they are willing to
…[7 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Crystal Reports Engine & COBOL

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-wCr9eJHwwjcb@Dwight_Miller.iix.com>`
- **References:** `<71aq93$cio$1@nnrp1.dejanews.com> <3639DCA7.512F659C@IMN.nl>`

```
On Fri, 30 Oct 1998 15:35:04, "COBOL Frog (Huib Klink)" 
<H.Klink@IMN.nl> wrote:

>> > I would like to use the Crystal Reports Engine API with Acucobol.
 Does anyone
> > have routines for calling the engine from any COBOL that they are willing to
> > share?
…[4 more quoted lines elided]…
> 

I did not see the original posting - my news server is not doing so 
well in that respect - but Fujitsu COBOL works (reportedly) with 
Crystal Reports.

I have not tried it, but it comes bundled into the 3.0 COBOL starter 
kit.
```

###### ↳ ↳ ↳ Re: Crystal Reports Engine & COBOL

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363E1EFD.BD659D65@IMN.nl>`
- **References:** `<71aq93$cio$1@nnrp1.dejanews.com> <3639DCA7.512F659C@IMN.nl> <Jl0PnHJ5PvPd-pn2-wCr9eJHwwjcb@Dwight_Miller.iix.com>`

```
Sorry Thane/Steve, forgot to mention:

Our approach via visual basic is because we use NetExpress COBOL (Micro Focus),
which can't use (so am I told) the Crystal Reports ActiveX.

Frog, jumped fast

Thane Hubbell wrote:
8<

> I did not see the original posting - my news server is not doing so
> well in that respect - but Fujitsu COBOL works (reportedly) with
> Crystal Reports.
```

#### ↳ Re: Crystal Reports Engine & COBOL

- **From:** MJHOPKI@ertltoys.com
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72q6b4$6u2$1@nnrp1.dejanews.com>`
- **References:** `<71aq93$cio$1@nnrp1.dejanews.com>`

```
I have such a routine.  It is actually fairly simple code and does not require
ActiveX or VB.  It is done completely with Acucobol and Crystal. There is a
minor difference between 16-bit and 32-bit platforms.

I am interested in finding out how much interest there is in such routines
running under Acucobol.  If anyone is interested then contact me.

In article <71aq93$cio$1@nnrp1.dejanews.com>,
  swolfson1@my-dejanews.com wrote:
> I would like to use the Crystal Reports Engine API with Acucobol.  Does anyone
> have routines for calling the engine from any COBOL that they are willing to
…[8 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: Crystal Reports Engine & COBOL

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3651675E.768B77D5@IMN.nl>`
- **References:** `<71aq93$cio$1@nnrp1.dejanews.com> <72q6b4$6u2$1@nnrp1.dejanews.com>`

```
I *am* interested. Please share your code with me and others.

The COBOL Frog

MJHOPKI@ertltoys.com wrote:

> I have such a routine.

Author means COBOL talking with Crystal Reports

>  It is actually fairly simple code and does not require
> ActiveX or VB.  It is done completely with Acucobol and Crystal. There is a
…[3 more quoted lines elided]…
> running under Acucobol.  If anyone is interested then contact me.

8< rest
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
