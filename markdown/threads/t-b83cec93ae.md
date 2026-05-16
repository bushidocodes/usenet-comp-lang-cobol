[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comparing a boolean value with a constant

_6 messages · 4 participants · 2002-01_

---

### Comparing a boolean value with a constant

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-07T09:56:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201070956.235585e@posting.google.com>`

```
Hi,

I have a boolean variable 
01 HAS_VAL PIC 9 VALUE 0.

when I compare this with 0(IF HAS_VAL IS EQUAL TO 0) it fails. If I
add a COMP to the definition the comparision works. But, I can't add
the COMP. Is there a way to compare the two ??

Would help if I could get some comments on the same.

Thanks and Regards,
M Shetty
```

#### ↳ Re: Comparing a boolean value with a constant

- **From:** Greg Ferro <gferro@sprynet.com>
- **Date:** 2002-01-07T13:36:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C39F8D8.48429C0C@sprynet.com>`
- **References:** `<bfbb8fd4.0201070956.235585e@posting.google.com>`

```
You are comparing an alphanumeric value to a numeric literal.

Either make the literal an alphanumeric literal by enclosing it in
single quotes or change the definition of your boolean variable, e.g.:

    01  BOOLEAN-VARIABLES.
          05  HAS-VAL  PIC 9  COMP VALUE 0.

A level 01 definition is by definition a group variable and therefore
character.

mshetty wrote:

> Hi,
>
…[10 more quoted lines elided]…
> M Shetty
```

##### ↳ ↳ Re: Comparing a boolean value with a constant

- **From:** "JerryMouse" <jerrymouse@invalid.com>
- **Date:** 2002-01-07T20:37:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nGn_7.188679$m05.15954833@bin5.nnrp.aus1.giganews.com>`
- **References:** `<bfbb8fd4.0201070956.235585e@posting.google.com> <3C39F8D8.48429C0C@sprynet.com>`

```

"Greg Ferro" <gferro@sprynet.com> wrote in message
news:3C39F8D8.48429C0C@sprynet.com...
> You are comparing an alphanumeric value to a numeric literal.
>
…[7 more quoted lines elided]…
> character.

A GROUP ITEM is an item having subordinate entries; An ELEMENTARY item is on
with no subordinate entries. The level number of either is irrelevant. A
GROUP item (remember, that's one that has subordinate entries and - by
implication - no associated PICTURE clause) is treated as alphanumeric. But
that's not the case here.
>
> mshetty wrote:
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Comparing a boolean value with a constant

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-01-08T15:45:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duE_7.51751$wa.3507999@bin6.nnrp.aus1.giganews.com>`
- **References:** `<bfbb8fd4.0201070956.235585e@posting.google.com> <3C39F8D8.48429C0C@sprynet.com>`

```

On  7-Jan-2002, Greg Ferro <gferro@sprynet.com> wrote:

>     01  BOOLEAN-VARIABLES.
>           05  HAS-VAL  PIC 9  COMP VALUE 0.
>
> A level 01 definition is by definition a group variable and therefore
> character.

A level 01 definition can be a group variable, but doesn't have to be one. 
In this case it is one.
A group variable can often be treated as character, but there are some
differences.  In this case, treat it as character.
```

#### ↳ Re: Comparing a boolean value with a constant

- **From:** "JerryMouse" <jerrymouse@invalid.com>
- **Date:** 2002-01-07T20:41:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OJn_7.564588$8q.45943299@bin2.nnrp.aus1.giganews.com>`
- **References:** `<bfbb8fd4.0201070956.235585e@posting.google.com>`

```

"mshetty" <mshetty@mail.com> wrote in message
news:bfbb8fd4.0201070956.235585e@posting.google.com...
> Hi,
>
…[5 more quoted lines elided]…
> the COMP. Is there a way to compare the two ??

Works for me. Is there something you're leaving out?

I assume by 'it fails,' you mean during execution, not at compile time. And
how does it fail? As an aside, if you 'can't add the COMP' how do you know
if the comparison works when you do 'add the COMP?'
```

##### ↳ ↳ Re: Comparing a boolean value with a constant

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-10T19:00:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201101900.61fde17@posting.google.com>`
- **References:** `<bfbb8fd4.0201070956.235585e@posting.google.com> <OJn_7.564588$8q.45943299@bin2.nnrp.aus1.giganews.com>`

```
"JerryMouse" <jerrymouse@invalid.com> wrote in message news:<OJn_7.564588$8q.45943299@bin2.nnrp.aus1.giganews.com>...
> "mshetty" <mshetty@mail.com> wrote in message
> news:bfbb8fd4.0201070956.235585e@posting.google.com...
…[13 more quoted lines elided]…
> if the comparison works when you do 'add the COMP?'

Actually I can add it but, I shouldn't be adding it because the CORBA
specification does contain COMP.

Thanks and Regards,
mshetty
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
