[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Correct answer

_5 messages · 3 participants · 1999-03_

---

### Correct answer

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<921867294.22071.0.nnrp-03.9e98b131@news.demon.co.uk>`

```
I don't know if any one else agrees but I think it would be nice and also
good manners if users who raise a query acknowledged which answers worked.

I sometimes follow a thread and am really no wiser at the end than I was at
the beginning.  This is especially true if I first try to look for a
solution to an allready  discussed problem via dejanews.

I don't know if we can set up a standard reply code showing valid answers.

Regards

Rick
```

#### ↳ Re: Correct answer

- **From:** Stu Talbot <stubtalb@globalnet.co.uk>
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F41888.FE890122@globalnet.co.uk>`
- **References:** `<921867294.22071.0.nnrp-03.9e98b131@news.demon.co.uk>`

```
Sounds good.

Rick Price wrote:

> I don't know if any one else agrees but I think it would be nice and also
> good manners if users who raise a query acknowledged which answers worked.
…[9 more quoted lines elided]…
> Rick
```

#### ↳ Re: Correct answer

- **From:** Stu Talbot <stubtalb@globalnet.co.uk>
- **Date:** 1999-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F418FA.8BA2C245@globalnet.co.uk>`
- **References:** `<921867294.22071.0.nnrp-03.9e98b131@news.demon.co.uk>`

```
Might need to have several "Alternatives" as to ,
most efficient/fastest
most "stylish"
Compiler compliant
etc.
What do you think?

Rick Price wrote:

> I don't know if any one else agrees but I think it would be nice and also
> good manners if users who raise a query acknowledged which answers worked.
…[9 more quoted lines elided]…
> Rick
```

##### ↳ ↳ Re: Correct answer

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<922095245.1883.0.nnrp-08.9e98b131@news.demon.co.uk>`
- **References:** `<921867294.22071.0.nnrp-03.9e98b131@news.demon.co.uk> <36F418FA.8BA2C245@globalnet.co.uk>`

```
I was just thinking of a simple two letter code that could be used in a
search.   The difficulty is in thinking of a letter combination that you
don't often find in text.

However just having a reply giving the solution would be enough.

Stu Talbot wrote in message <36F418FA.8BA2C245@globalnet.co.uk>...
>Might need to have several "Alternatives" as to ,
>most efficient/fastest
…[8 more quoted lines elided]…
>> good manners if users who raise a query acknowledged which answers
worked.
>>
>> I sometimes follow a thread and am really no wiser at the end than I was
at
>> the beginning.  This is especially true if I first try to look for a
>> solution to an allready  discussed problem via dejanews.
>>
>> I don't know if we can set up a standard reply code showing valid
answers.
>>
>> Regards
>>
>> Rick
>
```

#### ↳ CA : Finding optional COMP-3 fields.

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F661D9.48A1BD05@ASPMnetdoor.com>`
- **References:** `<921867294.22071.0.nnrp-03.9e98b131@news.demon.co.uk>`

```


Rick Price wrote:

> I don't know if any one else agrees but I think it would be nice and also
> good manners if users who raise a query acknowledged which answers worked.

Looks like you might be talkin' to me.

When I asked about finding optional COMP-3 fields a few weeks ago (changing the
compiler was not an option), I moved the data in question to a long COMP-6
field (unsigned packed), then to numeric display items, redefined as an array.
We checked specific bytes for x"3C" (ASCII platform) and the rest for the
numeric class test.

> I don't know if we can set up a standard reply code showing valid answers.

Would CA work?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
