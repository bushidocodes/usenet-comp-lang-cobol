[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help ! Stuck with a Report Program.

_4 messages · 3 participants · 1998-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help ! Stuck with a Report Program.

- **From:** "ganesh kudva" <ua-author-13908158@usenetarchives.gap>
- **Date:** 1998-07-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de>`

```
Hello,

I have a problem with my Report Writing Program (TSO), on mainframe. I use
COBOL MVS. It is simple TSO File Processing.

I write a record into a file, by this statement.
WRITE Asatz FROM Zeile4.

Where Asatz -- X(80) and Zeile4 -- X(80). The output Report File has a
Record length of 80.

but when I see the Report file later, it has a blank line for everyline of
valid record printed. i.e., if there are five valid report lines, there
are totally 10 lines in the Report a blank line preceding every valid
report line.

Can anybody help ?

Thanks in Advance,
Ganesh Kudva.
```

#### ↳ Re: Help ! Stuck with a Report Program.

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-07-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c3f8616bab-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de>`
- **References:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de>`

```

Ganesh Kudva wrote in message
<01bdb147$9acc0c20$410··.@Amp··h.de>...
› Hello,
› 
…[12 more quoted lines elided]…
› report line.


Is the write statement you showed us, the ONLY one?
Check if you have another. Do you ever move spaces to Zeile4?
More info is needed...
```

##### ↳ ↳ Re: Help ! Stuck with a Report Program.

- **From:** "ganesh kudva" <ua-author-13908158@usenetarchives.gap>
- **Date:** 1998-07-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c3f8616bab-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c3f8616bab-p2@usenetarchives.gap>`
- **References:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de> <gap-c3f8616bab-p2@usenetarchives.gap>`

```
The statements are like this ...

MOVE Ws-Tele-Tbl (Counter) TO Ws-Temp-Data.
MOVE Spaces TO Zeile4.
MOVE Corresponding Ws-Temp-Data
TO Zeile4.


WRITE Asatz FROM Zeile4.


These set of statements are in a loop, till all the records in the table
Ws-Tele-Tbl are written in to the file.

Zeile4 has 80 Chars, and is like

01 Zeile.
05 Filler X(02).
05 Country X(10).
05 ........... ........


Thanks,
Ganesh Kudva.

Leif Svalgaard wrote in article
<35a··.@new··m.net>...
›
›
…[3 more quoted lines elided]…
›
```

#### ↳ Re: Help ! Stuck with a Report Program.

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-07-16T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c3f8616bab-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de>`
- **References:** `<01bdb147$9acc0c20$410394ad@Amp-Ganesh.ban.bosch.de>`

```
In article <01bdb147$9acc0c20$410··.@Amp··h.de>, "Ganesh Kudva"
writes:

› e., if there are five valid report lines, there
› are totally 10 lines in the Report a blank line preceding every valid
› report line.

My first guess would be that somewhere the carriage control character has not
be accounted for and the printout of the file is assuming that the first
position of the record is the ASA carriage control character (DCB=RECFM=FA or
FBA) and it has a zero in it, which is being interpreted as double-space
(advance two lines before printing). If the first character is not intended to
be carriage control, make sure the DD (or the TSO equivalent) is using
DCB=RECFM=F or FB.

You are describing this as a "report file", which often implies something
destined for a printer, which then implies that there is carriage control. In
such cases, in COBOL/MVS,VM,VSE one normally uses an AFTER ADVANCING clause in
the WRITE statement. If the 80 bytes are suppose to be printable positions, one
can use the ADV option, which would tell the compiler to allocate a carriage
control character in front of the 80 bytes one has defined for the record in
the FD. The records would then be 81 bytes long (the one carriage control
character plus the 80 printable positions defined as the record in the FD).

Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
