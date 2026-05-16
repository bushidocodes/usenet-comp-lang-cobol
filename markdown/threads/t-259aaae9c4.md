[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Input File (READ)

_1 message · 1 participant · 1999-10_

---

### RE: Input File (READ)

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-10-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E47B36D9946CD311995000A0C9EA3E9256B6BA@voyager.okc.disa.mil>`

```
The filling is usually done for a read into, the )! of the FD generally
points directly into the I/O buffer....

-----Original Message-----
From: Paulo Vieira [mailto:pvieira@emporsoft.pt]
Sent: Saturday, October 23, 1999 6:13 AM
To: comp.lang.cobol@list.deja.com
Subject: Re: Input File (READ)


 Message from the Deja.com forum: 
 comp.lang.cobol
 Your subscription is set to individual email delivery


Jerry P <bismail@bisusa.com> wrote in message
news:DC8Q3.479$Lm1.28301@typhoon01.swbell.net...
[snip...]
> Rule: When an input record is shorter than the maximum
> defined record length, the program fills the remainder of
> record definition with spaces.
>

Im my experience, when reading a line sequential file with a record
definition of (say) 1 to 510 chars, all I get is the actual data until the
end-of-record indicator (LF or CR+LF). The ramaining bytes stay untouched,
presumably with the result of the previsous read. Therefore I consider a
good practice to initialize the bigger record definition prior to read the
file.

Runtime/Compiler : R/M Cobol 6.09

Paulo Vieira, Emporsoft





 _____________________________________________________________
 Deja.com: Before you buy.
 http://www.deja.com/
 * To modify or remove your subscription, go to
 http://www.deja.com/edit_sub.xp?group=comp.lang.cobol
 * Read this thread at
 http://www.deja.com/thread/%3C7us5bt%24b68%241%40duke.telepac.pt%3E


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
