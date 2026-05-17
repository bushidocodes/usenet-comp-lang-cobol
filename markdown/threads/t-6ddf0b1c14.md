[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micofocus COBOL (win) run time error 166

_4 messages · 4 participants · 1997-04_

---

### Micofocus COBOL (win) run time error 166

- **From:** "jackson" <ua-author-576846@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ies9k$qp9@news.inforamp.net>`

```

I am currently getting run time error 166 when running
Powerbuilder/Powerbridge and microfocus cobol(win).

I wonder if anybody has any idea about this run time error.

Thanks in advance....

Jackson
```

#### ↳ Re: Micofocus COBOL (win) run time error 166

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-04-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ddf0b1c14-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5ies9k$qp9@news.inforamp.net>`
- **References:** `<5ies9k$qp9@news.inforamp.net>`

```

In article <5ies9k$q.··.@new··p.net> srd··.@tdb··k.ca "Jackson" writes:
› I am currently getting run time error 166 when running
› Powerbuilder/Powerbridge and microfocus cobol(win).
› I wonder if anybody has any idea about this run time error.

Try: "Recursive COBOL Call is illegal"

This might happen, for example, if a menu program Call-s an
application program which then uses CALL (instead of Exit Program)
to get back to the menu.

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

##### ↳ ↳ Re: Micofocus COBOL (win) run time error 166

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-04-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ddf0b1c14-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6ddf0b1c14-p2@usenetarchives.gap>`
- **References:** `<5ies9k$qp9@news.inforamp.net> <gap-6ddf0b1c14-p2@usenetarchives.gap>`

```

R Ross-Langley wrote:
› 
› In article <5ies9k$q.··.@new··p.net> srd··.@tdb··k.ca "Jackson" writes:
…[8 more quoted lines elided]…
› to get back to the menu.

Another possibility is that you are CALLing a subprogram and passing
a PROCEDURE-POINTER to a callback entry point which is in the CALLing
program - this will cause a 166 error when the CALLed program/function
calls the callback.
In this case, either split out the callback stuff into a seperate
module or (if that's not desirable or possible, probably due to it
needing to access the working-storage of the original caller) simply
make the calling program recursive. The manuals tell you how.

Cheers,
Kev.
```

#### ↳ Re: Micofocus COBOL (win) run time error 166

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-04-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ddf0b1c14-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5ies9k$qp9@news.inforamp.net>`
- **References:** `<5ies9k$qp9@news.inforamp.net>`

```

In article <5ies9k$q.··.@new··p.net>, "Jackson" wrote:
› I am currently getting run time error 166 when running
› Powerbuilder/Powerbridge and microfocus cobol(win).	
…[5 more quoted lines elided]…
› Jackson

My MF manual says runtime error 166 is an illegal recursive call. That would
mean that you have a program A which calls Program B which calls Program A (or
one of its entry points). Or possibly Program A calls itself or one of its
own entry points. You can have recursive programs in MF Cobol but you have to
have a LOCAL STORAGE section in Program A (and Program B if it is also call
again by A).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
