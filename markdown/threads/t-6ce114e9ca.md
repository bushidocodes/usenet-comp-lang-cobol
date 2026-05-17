[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help to printout contents of af Multi Line Entry Field - Dialog (f...@lr.dk)

_2 messages · 2 participants · 1996-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help to printout contents of af Multi Line Entry Field - Dialog (f...@lr.dk)

- **From:** "hhh" <ua-author-39160@usenetarchives.gap>
- **Date:** 1996-10-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbbceb$386992c0$0a03010a@FEK.LR.DK>`

```

1. Field is for exempel defined as 01 TXT PIC x(100)
2. Each line can have 15 char
3. Text is:

Fernando
Kvistgaard
Lille Elstedvej
33

Entry is defined with the options Ord wrap
after "Fernando" there is 7 spaces
after "Kvistgaard" there is 5 spaces
after "Lille...." there is 0 spaces
after "33" there is 13 spaces

but

TXT-string has "Fernando Kvistgaard Lille Elstedvej 33"

How can one output the text as it is in the screen?

Thanks to who will help me

Fernando Kvistgaard
```

#### ↳ Re: Help to printout contents of af Multi Line Entry Field - Dialog (f...@lr.dk)

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-10-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ce114e9ca-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbbceb$386992c0$0a03010a@FEK.LR.DK>`
- **References:** `<01bbbceb$386992c0$0a03010a@FEK.LR.DK>`

```

hhh wrote:
[snip]
› TXT-string has "Fernando Kvistgaard Lille Elstedvej 33"
›
› How can one output the text as it is in the screen?
›

Hi.

You probably want to split the PIC X(100) into several individual variables
and then print each one seperately. I suggest looking at the UNSTRING verb.

Alternatively, you might want to note the location of the various start and
end points of the strings you want to extract from the PIC X(100) and display
each segment individually. In this case I suggest looking at using a
combination of INSPECT and subseqent DISPLAY/MOVE etc using reference
modification.

The details for how you want to UNSTRING or INSPECT your input string will
depend on just how flexible you are as to the contents of that string.

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
