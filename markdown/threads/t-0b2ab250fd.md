[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Subroutines

_1 message · 1 participant · 2001-02_

---

### Re: Subroutines

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-08T07:55:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A82510B.98FC4FD9@Azonic.co.nz>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qik6$11ua$1@news.hitter.net> <95qvp3$rp8$1@nnrp1.deja.com>`

```
Stefan Meyer wrote:
> 
> Sorry no. The is defined as indexed with access dynamic. The main-prog
> opens the file ReadOnly (cause it doesn't make any updates) and the
> subprog needs the file opened I/O (cause it will do some updates).

It is possible to have the file open as I-O and then _not_ do any
updates (gasp, shock, horror).  
The only difference is the locking.  Use MANUAL locking and only WITH
LOCK when a record is required for updating.  Or use WITH NO LOCK and/or
WITH IGNORE LOCK.

Alternately keep track of current open status and CLOSE/OPEN as
appropriate.  That is have a flag 'Open-mode' that is initailly space. 
When the routine is called with a function 'read' then open the file
INPUT and set the flag to, say, 'R'.  If a function (part of linkage) or
'read for update' arrives and the flag is 'R' then CLOSE and OPEN I-O
before reading and set the flag to 'U'.  If the flag is of the correct
mode then there is no need to CLOSE and reOPEN.
 
> > [...]
> > >Sorry if my intention to ask for subroutines was/is not clear.
…[6 more quoted lines elided]…
> That's what I expected.

Get over it.  You have been obsessed with trying to get two subroutines
instead of actually trying to solve the problem.

In fact how would having two instances of the _same_ subroutine help ? 
They would still need code to OPEN INPUT or OPEN I-O as appropriate, it
would still need to be told which is required (or was it going to be a
psychic routine that _knew_ what was required ?).

Just OPEN the file I-O and use manual locking.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
