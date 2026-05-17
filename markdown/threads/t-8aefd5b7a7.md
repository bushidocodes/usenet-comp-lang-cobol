[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DISPLAY problem (cont'd)

_3 messages · 3 participants · 1995-05_

---

### DISPLAY problem (cont'd)

- **From:** "don..." <ua-author-17087601@usenetarchives.gap>
- **Date:** 1995-05-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3p7r49$9bn@inforamp.net>`

```
I have seen situations where the source appears correct and the complier
wrong, but the source is acutally in error.

Is the DISPLAY part of a conditional (ie IF, PERFORM, etc) ?
If so, two possibilities I have encountered:

1) There is a continuation character of some sort in column 72? It may look
like some other part of a valid statement.

2) Is there a period within the DISPLAY, ie it may appear to be within
quotes but isn't?


Terry Doner 
Senior Systems Consultant 
Toronto Dominion Bank 
don··.@tdb··k.ca
```

#### ↳ Re: DISPLAY problem (cont'd)

- **From:** "francesco carollo" <ua-author-16120105@usenetarchives.gap>
- **Date:** 1995-05-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aefd5b7a7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3p7r49$9bn@inforamp.net>`
- **References:** `<3p7r49$9bn@inforamp.net>`

```
Hi Terry. Thanks for the suggestions however I had checked that already.
Someone a while back suggested that the DISPLAY problem was only the
symptom of a bad addressing problem. I've verified the linkage section
more than once with no luck. Anyone out there have any other ideas as
to how an addressing problem could occur?

I'm getting desperate. I'm even thinking of calling IBM on this one :-)
Any help will be greatly appreciated (i.e. H E L P !!!!!0
See ya
FC
In article <3p7r49$9.··.@inf··p.net> don··.@tdb··k.ca writes:
› I have seen situations where the source appears correct and the complier
› wrong, but the source is acutally in error.
…[17 more quoted lines elided]…
› .

Francesco
bb··.@mus··l.ca
```

##### ↳ ↳ Re: DISPLAY problem (cont'd)

- **From:** "pgraham" <ua-author-32034507@usenetarchives.gap>
- **Date:** 1995-05-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aefd5b7a7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8aefd5b7a7-p2@usenetarchives.gap>`
- **References:** `<3p7r49$9bn@inforamp.net> <gap-8aefd5b7a7-p2@usenetarchives.gap>`

```
Francesco Carollo writes:

› Hi Terry. Thanks for the suggestions however I had checked that already.
› Someone a while back suggested that the DISPLAY problem was only the
› symptom of a bad addressing problem. I've verified the linkage section
› more than once with no luck. Anyone out there have any other ideas as
› to how an addressing problem could occur?
 
› I'm getting desperate. I'm even thinking of calling IBM on this one :-)
› Any help will be greatly appreciated (i.e. H E L P !!!!!0
…[3 more quoted lines elided]…
›  bb··j@mus··l.ca

I throw this out only as a wild suggestion. Some years ago, with Realia Cobol
for the PC I found that regularly when I DISPLAYed more than one item with a
single statement that various errors would appear in the program (memory
prevents me fro being more specific). I now make it a rule to move the
individual items into a template and display this single item. No Problem
then. I never tracked down the cause, just live with the work-around.

Maybe this will trigger a solution!

Phil
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
