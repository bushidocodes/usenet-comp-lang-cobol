[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Odd code

_7 messages · 6 participants · 1998-02_

---

### Odd code

- **From:** "ejones" <ua-author-2564830@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd3826$effeae40$5050b6cc@ernestjo>`

```

Here is some code that I found in a program today. It is very interesting.
FOr years now I have thought about writting a book about strange/funny
code I have seen.

This is actual code. I did not make this up.


PERFORM E2C54-GET-DATA-51.
...
...
...

E2C54-GET-DATA-51 SECTION.
E2C54-GET-DATA-51-010.
MOVE ZEROS TO I
MOVE ZEROS TO J.
MOVE ZEROS TO K.
MOVE 0 TO L.
IF L = ZEROS
GO TO E2C54-GET-DATA-51-310.
MOVE 0 TO L.
IF L = ZEROS
GO TO E2C54-GET-DATA-51-210.

E2C54-GET-DATA-51-110.
ADD 1 TO I
END-ADD.
IF I GREATER 0
MOVE ZEROS TO I
GO TO E2C54-GET-DATA-51-EXIT.

E2C54-GET-DATA-51-210.
ADD 1 TO J
END-ADD.
IF J GREATER 0
MOVE ZEROS TO J
GO TO E2C54-GET-DATA-51-110.

E2C54-GET-DATA-51-310.
ADD 1 TO K
END-ADD.
IF K GREATER 05
MOVE ZEROS TO K
GO TO E2C54-GET-DATA-51-210.
MOVE SPACES TO E2C54-OPTION-1-TO-5-LIT (K).
MOVE SPACES TO E2C54-MM-RCDR-OPT-CD (K).
MOVE SPACES TO E2C54-OPTION-DESC-LIT (K).
MOVE SPACES TO E2C54-MM-OPT-DESC (K).
GO TO E2C54-GET-DATA-51-310.

E2C54-GET-DATA-51-EXIT. EXIT.

E2C54-SEND-SCREEN SECTION.
E2C54-SEND-SCREEN-010.
```

#### ↳ Re: Odd code

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd3826$effeae40$5050b6cc@ernestjo>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo>`

```

ejones wrote:
›
› Here is some code that I found in a program today. It is very interesting.

[I had to snip the code so that my news server would let me post.
If you missed it, try to retrieve it from the original article. It
must be seen to be believed.]

If I'm not mistaken, this entire masterpiece is equivalent to the
following (minus any typos):

E2C54-GET-DATA-51 SECTION.
*
PERFORM VARYING K FROM 1 BY 1
UNTIL K > 5
MOVE SPACES TO E2C54-OPTION-1-TO-5-LIT (K)
E2C54-MM-RCDR-OPT-CD (K)
E2C54-OPTION-DESC-LIT (K)
E2C54-MM-OPT-DESC (K)
END-PERFORM.
*
MOVE ZERO TO I
J
K
L.
*
E2C54-SEND-SCREEN SECTION.
E2C54-SEND-SCREEN-010.

I'm assuming:

1. All variables are disjoint -- i.e. they do not overlap each other
in memory, by REDEFINES or any other means;

2. No code outside of the section directly invokes any of the
paragraphs within the section.

The MOVE ZERO could probably be omitted, because the rest of the
program probably doesn't depend on the values which are left in I,
J, K, or L.

Is there any known reason why anyone would code such a demented
mess just to initialize a table? Perhaps it was inspired by the
Obfuscated C Contest.

Michael C. Kasten mc··.@swb··l.net
http://home.swbell.net/mck9/cobol/cobol.html
```

##### ↳ ↳ Re: Odd code

- **From:** "news" <ua-author-13363@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb8abdc7e-p2@usenetarchives.gap>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo> <gap-ceb8abdc7e-p2@usenetarchives.gap>`

```

I beleive that this code was written by someone who knew better than the
person to whom he/she
reported. This is the type of code that makes for some unworthy job
security.

Michael C. Kasten wrote in article
<34E··.@swb··l.net>...
› ejones wrote:
›› 
…[46 more quoted lines elided]…
›
```

#### ↳ Re: Odd code

- **From:** "rrp..." <ua-author-13513217@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bd3826$effeae40$5050b6cc@ernestjo>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo>`

```

ejones wrote:
› 
› Here is some code that I found in a program today.  It is very interesting.
…[17 more quoted lines elided]…
›         GO TO E2C54-GET-DATA-51-310.
 
›     MOVE 0 TO L.
›     IF L = ZEROS
…[31 more quoted lines elided]…
› E2C54-SEND-SCREEN-010.

Wow. This code must have been altered over the years; otherwise, the
programmer was clueless.
```

##### ↳ ↳ Re: Odd code

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb8abdc7e-p4@usenetarchives.gap>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo> <gap-ceb8abdc7e-p4@usenetarchives.gap>`

```

rrp··.@i··.net wrote:
› 
› ejones wrote:
…[57 more quoted lines elided]…
› programmer was clueless.

Looks like it was produced by some manner of utility or run through a
structuring engine, maybe?

DD
```

###### ↳ ↳ ↳ Re: Odd code

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb8abdc7e-p5@usenetarchives.gap>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo> <gap-ceb8abdc7e-p4@usenetarchives.gap> <gap-ceb8abdc7e-p5@usenetarchives.gap>`

```

The Goobers wrote:
› rrp··.@i··.net wrote:
›› 
…[62 more quoted lines elided]…
› structuring engine, maybe?

I agree, DD. Boys and Girls, when the boss starts talking '4GL', this is
the kind of slop you can expect to be working with.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: Odd code

- **From:** "ejones" <ua-author-2564830@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ceb8abdc7e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ceb8abdc7e-p4@usenetarchives.gap>`
- **References:** `<01bd3826$effeae40$5050b6cc@ernestjo> <gap-ceb8abdc7e-p4@usenetarchives.gap>`

```

Forgot to put in my first post. The system that this program was in was
installed in 1993! However, I think it was developed with Knowledgeware
and then manually modified.

rrp··.@i··.net wrote in article <34E··.@i··.net>...
› ejones wrote:
›› 
…[3 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
