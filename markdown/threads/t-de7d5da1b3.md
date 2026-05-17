[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Abend U1020 On File Read

_2 messages · 2 participants · 1996-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Abend U1020 On File Read

- **From:** "len richardson" <ua-author-17086358@usenetarchives.gap>
- **Date:** 1996-09-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<322D2A61.7CFE@ix.netcom.com>`

```

I've got a problem with a VS COBOL II program that abends with a U1020.
It issues message IGZ020I with a FILE STATUS return code of 46. The code
seems simple and straightforward: I perform a paragraph (thru an exit)
that reads a file into a working storage area. AT END I set a switch.
Also, one of the records in the file must have a certain value. My
performed paragraph uses both the switch and the value to stop the
reading of the file.
The funny thing is the value is found and the program continues
processing until end-of-job (GOBACK), but then abends with a U1020.

If anyone has encountered this, please help. Thanx.

Len


perform read-file
thru read-file-exit
until value-found
or eof-switch.

read-file.
read MYFILE into MYDATA-VALUE-REC
at end
move 'y' to eof-switch-ind.
read-file-exit. exit.
```

#### ↳ Re: Abend U1020 On File Read

- **From:** "haluk okur" <ua-author-1144603@usenetarchives.gap>
- **Date:** 1996-09-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-de7d5da1b3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<322D2A61.7CFE@ix.netcom.com>`
- **References:** `<322D2A61.7CFE@ix.netcom.com>`

```

Len Richardson wrote:

› I've got a problem with a VS COBOL II program that abends with a U1020.
› It issues message IGZ020I with a FILE STATUS return code of 46. The code
…[21 more quoted lines elided]…
›         read-file-exit. exit.

If this is the real code, I mean if there are no other lines between the
PERFORM statement and READ-FILE paragraph, the code simply "falls thru"
into the READ-FILE paragraph. The result is a READ-NEXT-after-END-OF-FILE
situation which yields in return code 46 (=no current record).

Hope this helps.
----------
Haluk Okur / SIMKO A.S. (Siemens in Turkiye)
e-mail: sp··.@s··.de __o
Tel : +90 (216) 389-5940, ext 4563 -\<,
Fax : +90 (216) 306-2548 ___(*)/(*)___
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
