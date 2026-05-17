[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Serial files

_3 messages · 2 participants · 1998-05_

---

### Serial files

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k4dsc$6il$1@news.igs.net>`

```

Here is an interesting one for all you old timers. I am
using Liant Cobol under Windows95, but this should
apply to all COBOL's.

The code has to read data coming in from RS-232-C
interfaces. It is coming from scales, barcode readers,
etc., that send an ASCII stream terminated. That is,
the data looks exactly like a line sequential file.

In the past, I have always done this in assembler, as
subroutines. I want to do it in pure Cobol, and can
ALMOST do exactly what I want.

I define a file as line sequential, and assign it to a
comport. I open it, and read. I get the data correctly.
The problem is that there is no end of file, and no way
of getting out of the READ statement if there is no data.

The test code (that works) is as follows.

open test-file.
read test-file at end move "y" to end-flag.
close test-file.

The open statement always" seems to work, and always
returns a status "00". The read hangs until I put a bar code
through, and then gets the data into the test-file record, without
taking the "at end" path. The close works. Looks good, but
I need a time out. Like what if the scale data is not there or the
cable is off. In that case, the program hangs on the read.

What it looks like is happening is that the input buffer is cleared
on input, and the next reading from the device always gets read.
The end path is never taken unless a CNTR Z is sent (which the
device will never send). The problem, then, is that I do not WANT
to do a read unless there is data ready. The code should be
something like:

OPEN FILE.
perform READ_THE_RECORD UNTIL
record-is-read or timeout-occurs.
CLOSE FILE.

READ-THE-RECORD.
if (a record exists)
read next (etc.)
else
(check for timeout etc.).

Any ideas on how to do this without cheating by going
into Assembler?
```

#### ↳ Re: Serial files

- **From:** "fujitsu software corporation" <ua-author-6588898@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5aa4a3c8b4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6k4dsc$6il$1@news.igs.net>`
- **References:** `<6k4dsc$6il$1@news.igs.net>`

```

Donald,

You can fully support all RS-232 devices with Fujitsu COBOL and MarshallSoft
Serial communications libraries for Windows 95/NT.

You can get the FREE unrestricted Fujitsu COBOL Starter Set at
www.adtools.com

For more information on MarshallSoft see www.marshallsoft.com

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX: (408) 428-0600
Email: co··.@adt··s.com
Web: www.adtools.com


Donald Tees wrote in message <6k4dsc$6il$1.··.@new··s.net>...
› Here is an interesting one for all you old timers.  I am
› using Liant Cobol under Windows95, but this should
…[53 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Serial files

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5aa4a3c8b4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5aa4a3c8b4-p2@usenetarchives.gap>`
- **References:** `<6k4dsc$6il$1@news.igs.net> <gap-5aa4a3c8b4-p2@usenetarchives.gap>`

```

› You can fully support all RS-232 devices with Fujitsu COBOL and
› MarshallSoft
› Serial communications libraries for Windows 95/NT.

Thank you.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
