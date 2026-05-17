[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 98/38 errors on RM/Cobol-85 Indexed datafiles

_5 messages · 4 participants · 1995-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### 98/38 errors on RM/Cobol-85 Indexed datafiles

- **From:** "paul oldham" <ua-author-17087690@usenetarchives.gap>
- **Date:** 1995-06-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<803028648snz@bizanal.demon.co.uk>`

```

We've got a customer who's recently moved his application from an
i486 SCO Xenix based system to a Pentium SCO Unix based system.
He moved the runtime over (5.10) onto the new box.

He's now getting intermittent 98/38 errors reading indexed files.
These seem to occur primarily when he's reading a lot of records
sequentially. The manual is less than helpful: 98 says "If the error
occurs when the file is being read, it may be a disk read error
which goes away when the operation is retried", and the only
reference I've got for the sub-code says "Buffer invalid or record
not found".

Unix itself is reporting no errors on the console. He has 12Mb of
memory and the error happens when he's the only user on the
system, so he's not running out of memory. I've checked his kernel
parameters with another user with a similar setup who's not having
problems, I've got him to run fsck, I've run recover1 on the
files. All of which has failed to make this go away.

Anyone got any other ideas?


-----------------------------------------------------------------------
Paul Oldham        | "Always park in the shade"  | Tel: +44 1252 860090
Yateley, Hants, UK |                 G Graveline | Fax: +44 1252 861756
-----------------------------------------------------------------------
```

#### ↳ Re: 98/38 errors on RM/Cobol-85 Indexed datafiles

- **From:** "anthony beissner" <ua-author-6589405@usenetarchives.gap>
- **Date:** 1995-06-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-97dfba3d8c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<803028648snz@bizanal.demon.co.uk>`
- **References:** `<803028648snz@bizanal.demon.co.uk>`

```
Paul Oldham wrote:
› 
› We've got a customer who's recently moved his application from an 
…[3 more quoted lines elided]…
› He's now getting intermittent 98/38 errors reading indexed files. 



Support questions like this are best addressed to our support staff. In London they
can be reached at +44 171 799 2434. Questions can also be directed to
sup··.@li··t.com.

Without having any more information than what was in the original message, I would
suggest that your customer run the recover1 utility on the file. This might repair
the corruption.

===========================================================================
I have nothing witty to say.        |                     ant··.@li··t.com
===========================================================================
```

#### ↳ Re: 98/38 errors on RM/Cobol-85 Indexed datafiles

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-97dfba3d8c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<803028648snz@bizanal.demon.co.uk>`
- **References:** `<803028648snz@bizanal.demon.co.uk>`

```
Paul Oldham (pa··.@biz··o.uk) wrote:

: We've got a customer who's recently moved his application from an
: i486 SCO Xenix based system to a Pentium SCO Unix based system.
: He moved the runtime over (5.10) onto the new box.

: He's now getting intermittent 98/38 errors reading indexed files.
: These seem to occur primarily when he's reading a lot of records
: sequentially. The manual is less than helpful: 98 says "If the error
: occurs when the file is being read, it may be a disk read error
: which goes away when the operation is retried", and the only
: reference I've got for the sub-code says "Buffer invalid or record
: not found".

: Unix itself is reporting no errors on the console. He has 12Mb of
: memory and the error happens when he's the only user on the
: system, so he's not running out of memory. I've checked his kernel
: parameters with another user with a similar setup who's not having
: problems, I've got him to run fsck, I've run recover1 on the
: files. All of which has failed to make this go away.

: Anyone got any other ideas?

: --

: -----------------------------------------------------------------------
: Paul Oldham | "Always park in the shade" | Tel: +44 1252 860090
: Yateley, Hants, UK | G Graveline | Fax: +44 1252 861756
: -----------------------------------------------------------------------

This would make some sense if he is doing some writing. Depending on if
the COBOL is setup under UNIX to update files on demand or whenever could
affect this.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

#### ↳ Re: 98/38 errors on RM/Cobol-85 Indexed datafiles

- **From:** "paul oldham" <ua-author-17087690@usenetarchives.gap>
- **Date:** 1995-06-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-97dfba3d8c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<803028648snz@bizanal.demon.co.uk>`
- **References:** `<803028648snz@bizanal.demon.co.uk>`

```

In article <803··.@biz··o.uk> I wrote:

› We've got a customer who's recently moved his application from an 
› i486 SCO Xenix based system to a Pentium SCO Unix based system. 
…[4 more quoted lines elided]…
› sequentially.

If anyone is interested we appear to have fixed this problem by
rewriting each file where the error occurred record by record into
another file. This was done at the suggestion of SMB who had had
similar problems. They suspect that in some conditions recover1
doesn't do a perfect recover (but says it has). Many thanks to
them.


Paul Oldham    "Some people wish that Usenet were a democracy. Many people 
Yateley             pretend that it is. Both groups are sadly deluded."
Hampshire, UK                           -- Zen and the Art of the Internet
```

##### ↳ ↳ Re: 98/38 errors on RM/Cobol-85 Indexed datafiles

- **From:** "jea..." <ua-author-11185568@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-97dfba3d8c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-97dfba3d8c-p4@usenetarchives.gap>`
- **References:** `<803028648snz@bizanal.demon.co.uk> <gap-97dfba3d8c-p4@usenetarchives.gap>`

```
In <803··.@biz··o.uk>, Paul Oldham
writes:

› If anyone is interested we appear to have fixed this problem by
› rewriting each file where the error occurred record by record into
…[3 more quoted lines elided]…
› them.

This suggests that the files had defects in their internal block
structures which continually caused recurrences of the 98,38 errors.
RECOVER1 only rebuilds index blocks, not data blocks. None of this
explains why the errors would only occur on a Pentium-based system
unless the files were somehow damaged during the transfer process.

If the bad files aren't too big (and still exist), you may want to
consider submitting them to Liant's UK office for analysis (they'll most
likely forward them here to Austin). It might also be interesting to
run the V6 RECOVER1 utility on the files, as it peforms additional error
checking. However, this version also won't rebuild the data blocks. I
think you certainly took the right approach, but the mystery remains.

---------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Principal Programmer | or: jea··.@ccw··s.edu |
| Ryan McFarland Corp/Liant Software | Compuserve: 74774,47 / GO LIANT |
---------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
