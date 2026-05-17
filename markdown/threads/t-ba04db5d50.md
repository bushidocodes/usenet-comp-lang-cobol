[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol74 vs cobol85

_2 messages · 2 participants · 1995-10_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Cobol74 vs cobol85

- **From:** "takashi suezawa" <ua-author-17087955@usenetarchives.gap>
- **Date:** 1995-10-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44tva9$dpk@bioko.ifi.unizh.ch>`

```
Hi there

I have a question for those who are programming in cobol74 or cobol 85.
I would like know the differences between cobol74 and cobol85.


thank you for your effort
Takashi
```

#### ↳ Re: Cobol74 vs cobol85

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-10-04T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba04db5d50-p2@usenetarchives.gap>`
- **In-Reply-To:** `<44tva9$dpk@bioko.ifi.unizh.ch>`
- **References:** `<44tva9$dpk@bioko.ifi.unizh.ch>`

```
Well, I won't list all the difference here, because that would take
a manual...

Changes from COBOL 74:

1. Now you can have inline loops:
PERFORM VARYING WS-INDEX FROM 1 BY 1
UNTIL WS-INDEX GREATER WS-TABLE-SIZE
ADD THE-TABLE-NUM( WS-INDEX ) TO WS-ACCUMULATOR
END-PERFORM.

2. The festive evaluate verb (case-like) has been added:
EVALUATE WS-HAMSTER-CAGE
WHEN "GERBILS"
DISPLAY "GERBILS IN CAGE"
WHEN "HAMSTERS"
DISPLAY "YUP, THERE BE A HAMSTER"
WHEN OTHER
DISPLAY "C PROGRAMMER IN CAGE"
END-EVALUATE.
And, there are other forms of Evaluate as well.

3. Moving offsets of bytes from a field.

MOVE WS-HAMSTER-CAGE(1:2) TO FIRST-TWO-BYTES.

4. Scope-delimiters for conditionals...
IF WS-HAMSTER-CAGE = "GERBILS"
DISPLAY "GERBILS IN A CAGE"
ELSE
IF WS-HAMSTER-CAGE = "HAMSTERS"
DISPLAY "HAMSTER PARTY!"
END-IF
END-IF.

5. Festive Not at end phrase in READ statement...

READ GERBILS-FILE
AT END
DISPLAY "NO MORE GERBILS"
NOT AT END
DISPLAY "MORE GERBILS TO COME..."
END-READ.

6. Evil plot by space aliens to make READY TRACE and Exhibit named
no longer usable....


Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
