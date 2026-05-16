[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Misc comments on GOTO, packed data, and flowcharts

_2 messages · 2 participants · 2000-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Misc comments on GOTO, packed data, and flowcharts

- **From:** hancock4@bbs.cpcn.com (Lisa nor Jeff)
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g50aa$sj@netaxs.com>`

```
I have found that having a mid paragraph GO TO that heads to the
paragraph exit statement makes for much simpler and easier to understand
code than otherwise adding nested IF/ELSEs.

I don't know about the "rules" of "structured programming", but having a
GO TO  to the exit is fine with me for drop through conditions, indeed
IMHO is a superior coding method.  This is based on years of experience.

Frankly, I never cared much for purists who demanded 100% no GOTOs and
created other logic to accomodate.  It will work and may meet the
"rules", but I think it makes things more complex because trying to
break apart a complex IF/ELSE with multiple nestings is not easy.
```

#### ↳ Re: Misc comments on GOTO, packed data, and flowcharts

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39293560.F6E41545@cusys.edu>`
- **References:** `<8g50aa$sj@netaxs.com>`

```
Lisa nor Jeff wrote:
> 
> I have found that having a mid paragraph GO TO that heads to the
> paragraph exit statement makes for much simpler and easier to understand
> code than otherwise adding nested IF/ELSEs.

Quite a few shops agree with you, making that the standard.  And I agree
that if the programmers haven't been trained in structured methodology,
and if the code is not structured correctly, this has advantages.

The advantage will go away with the next release of COBOL which will
contain an EXIT PARAGRAPH command.

> Frankly, I never cared much for purists who demanded 100% no GOTOs and
> created other logic to accomodate.  It will work and may meet the
> "rules", but I think it makes things more complex because trying to
> break apart a complex IF/ELSE with multiple nestings is not easy.

The advantages I mentioned above arise from people not having to change
their way of thinking.  Removing GOTOs without designing in a structured
manner certainly can make code more complex.  Of course, I am responding
with the same type of arguments that OO people respond when I praise the
simplicity of structured over OO %).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
