[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu PowerForm error messages

_2 messages · 2 participants · 2004-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu PowerForm error messages

- **From:** "CarSalesman" <nikonut@yahoo.com>
- **Date:** 2004-12-19T15:21:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32m66cF3mnuj7U1@individual.net>`

```
I've been using PowerForm for about 5 to 10 years (can't remember - has it
been out that long?).  In using the PowerCobol debugger, you sometimes get
an error message that is along the lines of

JMP0320I-I [PID.....]INPUT/OUTPUT ERROR. STM=WRITE. FILE=finance.prt 
"ERRCD=9062"

This doesn't correspond to the error codes given in the PowerForm Run Time 
Guide, but
I seem to remember that the "90" and "62" relate to tables somewhere in the 
Fujitsu Cobol
documentation.

I've had this error in years past, and can't remember what it means.  I've 
searched the
documentation, but can't seem to find the information.

Can anyone tell me what the error means, or even better, point me to the 
pages in the docs
where its explained?  That way, I won't have to go looking for help next 
time!

don
```

#### ↳ Re: Fujitsu PowerForm error messages

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-20T11:00:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32mc0jF3n6uvtU1@individual.net>`
- **References:** `<32m66cF3mnuj7U1@individual.net>`

```

"CarSalesman" <nikonut@yahoo.com> wrote in message
news:32m66cF3mnuj7U1@individual.net...
> I've been using PowerForm for about 5 to 10 years (can't remember - has it
> been out that long?).  In using the PowerCobol debugger, you sometimes get
…[7 more quoted lines elided]…
> I seem to remember that the "90" and "62" relate to tables somewhere in
the
> Fujitsu Cobol
> documentation.
…[11 more quoted lines elided]…
>

Reproduced from page 33 of the "Introduction to PowerForm Manual"...

"When using PowerFORM you may encounter errors that refer
you to the PowerFORM RTS help. This file is located in the
PowerFORM software folder and is called "Pformapi.hlp". It has
an appendix "Trouble Analysis and Recovery" that documents
the detail codes returned by the PowerFORM RTS. Usually these
codes are communicated in the form "90nn" - the help file only
lists the last two digits "nn"."

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
