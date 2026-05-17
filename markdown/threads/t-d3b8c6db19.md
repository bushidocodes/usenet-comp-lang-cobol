[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DataGeneral to RM COBOL help

_3 messages · 2 participants · 1996-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### DataGeneral to RM COBOL help

- **From:** "rag..." <ua-author-654840@usenetarchives.gap>
- **Date:** 1996-06-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4q6vk7$94t@interport.net>`

```


I have a new project to port DG ICobol and VS/Cobol to a PC platform.

I previously did this with ICobol to MF Cobol.


Will RM handle the source code as is (it SHOULD be in the 85 extentions)
and more importantly...

I have data as sequential files on the PC - in a record is the structure
of COMP data standard or should I convert everything to display. Also is
sign location going to be a problem, ie. is S999V99 the same in what I
have exported as it will be in RM?

Post here or EMAIL...


thanks!
                                            Kevin Danzig
      rag··.@int··t.net               ----------------
```

#### ↳ Re: DataGeneral to RM COBOL help

- **From:** "uwe baemayr" <ua-author-6588910@usenetarchives.gap>
- **Date:** 1996-06-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3b8c6db19-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4q6vk7$94t@interport.net>`
- **References:** `<4q6vk7$94t@interport.net>`

```

Kevin:

You wrote:

› I have a new project to port DG ICobol and VS/Cobol to a PC platform.
› 
…[8 more quoted lines elided]…
› have exported as it will be in RM?

Source programs from I-COBOL (or any other dialect) will compile cleanly
in RM/COBOL-85 if they don't use any DG extensions that are not part of
the ANSI 1985 standard. Some DG extensions, like the SCREEN SECTION, are
part of the 85 standard.

Data currently stored in some other form of COBOL will need to be
converted to ASCII text files, in display format. Signs should be stored
separately (leading or trailing). An RM/COBOL-85 program could then read
those files as ORGANIZATION LINE SEQUENTIAL and create new indexed files
in our format.

RM/COBOL-85 assumes combined trailing signs for numeric fields. There
are two ways to make our runtime use separate fields: 1) Specify SIGN
LEADING SEPARATE or SIGN TRAILING SEPARATE next to the PICture clause for
the field. 2) Use the RM/COBOL-85 compiler parameter S which forces that
particular program to assume all signed fields have trailing separate
signs.

I hope this helps...

› Post here or EMAIL...

Did both.

------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Ryan McFarland Corporation | or: jea··.@ccw··s.edu |
| -- a division of Liant Software | Compuserve: 74774,47 / GO LIANT |
------------------------------------------------------------------------
```

##### ↳ ↳ Re: DataGeneral to RM COBOL help

- **From:** "rag..." <ua-author-654840@usenetarchives.gap>
- **Date:** 1996-06-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d3b8c6db19-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d3b8c6db19-p2@usenetarchives.gap>`
- **References:** `<4q6vk7$94t@interport.net> <gap-d3b8c6db19-p2@usenetarchives.gap>`

```

In <31C··.@li··t.com> Uwe Baemayr writes:

› Data currently stored in some other form of COBOL will need to be 
› converted to ASCII text files, in display format.  Signs should be stored
› separately (leading or trailing).  An RM/COBOL-85 program could then read
› those files as ORGANIZATION LINE SEQUENTIAL and create new indexed files
› in our format.

this is a real pain... but I'll only have to do it thrice on each file
(and there are only a dozen and a half). But why line sequential as
opposed to simple sequential files (with ton(s) of comp data these
records are over 600 characters in three of the files)


› RM/COBOL-85 assumes combined trailing signs for numeric fields.  There
› are two ways to make our runtime use separate fields: 1) Specify SIGN
…[3 more quoted lines elided]…
› signs.

If I knew what DG's sign format was it probably still wouldn't help, you
didn't answer regarding the 'standard' of COMP data (simply binary).

› I hope this helps...
 
›› Post here or EMAIL...
 
› Did both.

Thanks!

                                            Kevin Danzig
      rag··.@int··t.net               ----------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
