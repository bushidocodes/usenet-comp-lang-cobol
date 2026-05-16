[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNIX KORN shell/end of record seems to be carriage control and misreads file

_4 messages · 4 participants · 2002-09_

---

### UNIX KORN shell/end of record seems to be carriage control and misreads file

- **From:** morant@dnr.state.wi.us (Tom Morano)
- **Date:** 2002-09-09T06:08:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55066e.0209090508.7a545ee8@posting.google.com>`

```
I'm having a problem reading records from a flat file with UNIX COBOL.
We have just converted to the KORN shell, if that matters.

Say I'm reading a record that is 80 characters long, looking at the
file it looks like a normal record, characters out to byte 80.  When I
read the first record it works fine, reads the 80 characters.  Then I
read the second record, but instead of starting in the first byte of
record 2, it starts with the 81st character of record 1, which seems
to do what a carriage return would do, though it's not visible when I
look at it in a couple of formats.  It also reads characters 1 thru 79
of record 2.   So it's offset by 1 character.
For the third read it reads characters 80 & 81 of record 2, and
characters 1 thru 78 of record 3.  It continues that pattern thru the
rest of the file.

My code worked fine over on VAX alpha server, but this is happening
when running this on UNIX cobol.   Yes, the record lengths match the
FD's and such in the program exactly.

What has worked in some instances is reading it into a SAS program as
80 cahracters, then writing out those 80 characters and an 'x' as a
placeholder in character 81.  Then we adjust the ensuing cobol program
thusly.  The last program we're working on though isn't fooled by
this, and still reads that carriage control character that seems to be
to the right of the last character in the record.

It's a normal read we're doing:
READ MASTER-RECORD INTO TRANSACTION-RECORD-LAYOUT
   AT END
      MOVE 'Y' TO END-OF-MASTER-FILE-SW.

Has anyone else run across this??
```

#### ↳ Re: UNIX KORN shell/end of record seems to be carriage control and misreads file

- **From:** "Paul Barnett" <paul.barnett@microfocus.nospam.com>
- **Date:** 2002-09-09T14:57:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ali9ni$sa3$1@hyperion.microfocus.com>`
- **References:** `<55066e.0209090508.7a545ee8@posting.google.com>`

```
The character in position 81 should be a line-feed character. In Micro Focus
cobol you define the record length as 80 characters but with ORGANIZATION
LINE SEQUENTIAL and then the line-feed is interpreted as end of line.If, you
don't specify LINE-SEQUENTIAL, then chucks of 80 bytes are read from the
file, including the markers. Using the ORGANIZATION entry allows you to
specify which way you want to work. It's up to you how to decide which. I
would suggest LINE SEQUENTIAL from what you say.

Incidentally, on M$ environments, the end of line is shown by both
carriage-return and line-feed.

"Tom Morano" <morant@dnr.state.wi.us> wrote in message
news:55066e.0209090508.7a545ee8@posting.google.com...
> I'm having a problem reading records from a flat file with UNIX COBOL.
> We have just converted to the KORN shell, if that matters.
…[29 more quoted lines elided]…
> Has anyone else run across this??
```

#### ↳ Re: UNIX KORN shell/end of record seems to be carriage control and misreads f...

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2002-09-09T20:17:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020909161701.05562.00000684@mb-fc.aol.com>`
- **References:** `<55066e.0209090508.7a545ee8@posting.google.com>`

```
In article <55066e.0209090508.7a545ee8@posting.google.com>,
morant@dnr.state.wi.us (Tom Morano) writes:

>Say I'm reading a record that is 80 characters long, looking at the
>file it looks like a normal record, characters out to byte 80.  When I
…[8 more quoted lines elided]…
>rest of the file.

This looks suspiciously like a sequential file definition that is reading 
a 'line sequential' file.  One of the 'transitional' things that you have to 
deal with when moving from a Mainframe to a PC based environment.
If you are taking data directly from the original platform the program 
should function as defined, but if you are 'creating' test data on the new
platform in some text editor; you are getting the extra CR character added.
```

#### ↳ Re: UNIX KORN shell/end of record seems to be carriage control and misreads file

- **From:** Doug Robinson <fdr@mytemyke.com>
- **Date:** 2002-09-11T17:43:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2002.09.11.17.43.55.244375.5368@mytemyke.com>`
- **References:** `<55066e.0209090508.7a545ee8@posting.google.com>`

```
On Mon, 09 Sep 2002 09:08:53 -0400, Tom Morano wrote:

> I'm having a problem reading records from a flat file with UNIX COBOL.
> We have just converted to the KORN shell, if that matters.
…[28 more quoted lines elided]…
> Has anyone else run across this??


I don't know what platform you are on, but try an 'apropos hex' and see
what the viewer is for hex.  On my machines of various types I have
hexdump.  From there take a look at the record and see if each record
ends with a c/r + linefeed.  That is a windoze construct and most unix
machines delimit records with just the linefeed.  You wouldn't be copying
files with Samba would you.....just checking.  If so do another apropos
and see the utility that converts wondoze formats to unix and vice versa.
Been there, done that, got the T shirt......fdr
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
