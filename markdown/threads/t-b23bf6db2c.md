[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trimming spaces and appending...

_3 messages · 3 participants · 1997-09_

---

### Trimming spaces and appending...

- **From:** "eric schlene" <ua-author-2960622@usenetarchives.gap>
- **Date:** 1997-09-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34269AFC.9C2CF40D@FREH-01.ADPC.PURDUE.EDU>`

```

I'm a COBOL newbie...so I apologize right up front.

Does anyone have any sample code that can do the following in COBOLII?
I need to take 10 75char text fields, trim out all preceeding and
trailing spaces, and append them sequentially into a single 750
character text field.

I really don't want to ftp the data out and do it on the desktop. I'd
like to prove it can be done in COBOL.

Thanks in advance!

Eric

Also, if there's a good source for COBOL sample code on the web...PLEASE
point me to it. I can't find anything!
-----------------------------------------------------------
"I said rum and Coke on the rocks... | Eric Schlene,
not run the boat on the rocks!" | esc··.@pur··e.edu
- Joe Hazelwood | 765/496-2933
```

#### ↳ Re: Trimming spaces and appending...

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1997-09-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b23bf6db2c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34269AFC.9C2CF40D@FREH-01.ADPC.PURDUE.EDU>`
- **References:** `<34269AFC.9C2CF40D@FREH-01.ADPC.PURDUE.EDU>`

```

Eric Schlene wrote:
› 
› I'm a COBOL newbie...so I apologize right up front.
…[4 more quoted lines elided]…
› character text field.

Let me get this straight... you have 10 fields:

01 flda pic x(75) value ' this '.
01 fldb pic x(75) value ' is '.
01 fldc pic x(75) value ' what '.
01 fldd pic x(75) value ' you'.
01 flde pic x(75) value 'got? '.
etc. to fldj -

and you want target-fld pic x(750) to show 'thisiswhatyougot?' ... or
something like this?

DD
```

#### ↳ Re: Trimming spaces and appending...

- **From:** "alex romaniuk" <ua-author-5783842@usenetarchives.gap>
- **Date:** 1997-09-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b23bf6db2c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34269AFC.9C2CF40D@FREH-01.ADPC.PURDUE.EDU>`
- **References:** `<34269AFC.9C2CF40D@FREH-01.ADPC.PURDUE.EDU>`

```

Eric Schlene wrote:
› 
› I'm a COBOL newbie...so I apologize right up front.
…[18 more quoted lines elided]…
›                               - Joe Hazelwood | 765/496-2933

On VAX Cobol code would be something like this (Without system STR$
calls):

Define in WORKING-STORAGE SECTION

01 TrimPtr PIC 9(4) COMP.
01 StuffPtr PIC 9(4) COMP.
01 Ptr1 PIC 9(4) COMP.
01 Ptr2 PIC 9(4) COMP.
in PROCEDURE

MOVE SPACES TO
MOVE 1 TO StuffPtr
PERFORM VARYING Ptr1 FROM 1 BY 1 UNTIL Ptr1 > 10

* Trim proc goes here
MOVE ZERO TO TrimPtr
PERFORM VARYING Ptr2 FROM 10 BY -1 UNTIL Ptr2 = ZERO OR
TrimPtr NOT= ZERO
IF (Ptr1)(Ptr2:1) NOT= SPACES
MOVE Ptr2 TO TrimPtr
END-IF
END-PERFORM
* Now TrimPtr point to our last char in
MOVE (Ptr1)(1:TrimPtr) TO (StuffPtr:TrimPtr)
ADD TrimPtr TO StuffPtr
END-PERFORM

So If you have array of 10 times 75 chars looking like this:
1. A
2. B
3. CDE
4. F
5. G
6. H
7. IJK
8. L
9. M
10.N

Field of 750 chars would look like this: "ABCDEFGHIJKLMN" and StuffPtr
will point to position after "N"


This program is not tested anywhere, I just wrote it down right now
!!!!!

Alex
*******************************************************************
E-Mail address: ale··.@cn··t.si
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
