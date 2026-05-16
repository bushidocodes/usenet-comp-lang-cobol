[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF NE3.1 RTS 9/199 Network Error

_2 messages · 2 participants · 2003-05 → 2003-06_

---

### MF NE3.1 RTS 9/199 Network Error

- **From:** pepe@gmx.com (Pepe)
- **Date:** 2003-05-30T15:39:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cb2e24f.0305301439.47f3eec8@posting.google.com>`

```
Hi,

we recently have some problems with MF COBOL file access.
A new installation uses both workstation and server based on W2K SP3. 
The COBOL part of the program is compiled with NetExpress 3.1 no SP.
The files access is done with "normal extfh" .
It sometimes happens now, that the complete file access (read, write)
for all opened files stops. It is also not possible, to open files
again. Even restarting the program often does not help if there are
more users accessing the files on the share.
COBOL reports an 9/199 error. Calling GetLastError directly after the
file access only leads to "an unexpected network error occured". There
is nothing written to any event logs of Windows.
I thought of problems with OpLocks, but disabling them did not solve
the problem.
Needless to say that similar installations with the same program are
working since years.

Perhaps some of you already had similar problems and could give me a
clue on where to lay stress on my investigations.

Regards,
Pepe
```

#### ↳ Re: MF NE3.1 RTS 9/199 Network Error

- **From:** "Gael Wilson" <gael.wilson@microfocus.uk.com>
- **Date:** 2003-06-02T10:33:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbf5dg$t44$1@hyperion.microfocus.com>`
- **References:** `<7cb2e24f.0305301439.47f3eec8@posting.google.com>`

```
Pepe,

As you found, the file status error is returned as a direct result of a
system level error being returned from the file APIs indicating that some
sort of network error occurred. That being the case, check whether there are
any updates available for the network drivers you are using as that can have
a major bearing on this sort of problem.

Note that if you had applied the Net Express service pack you would have got
a 9/209 error which would given you a better idea of what the problem was
without having to call GetLastError directly.

"Pepe" <pepe@gmx.com> wrote in message
news:7cb2e24f.0305301439.47f3eec8@posting.google.com...
> Hi,
>
> COBOL reports an 9/199 error. Calling GetLastError directly after the
> file access only leads to "an unexpected network error occured".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
