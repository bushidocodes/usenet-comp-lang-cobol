[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Needed for Sharing Memory Between Processes

_4 messages · 4 participants · 1997-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help Needed for Sharing Memory Between Processes

- **From:** "stanley layson" <ua-author-17073627@usenetarchives.gap>
- **Date:** 1997-05-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc5fe6$403d3080$575e3681@stanley>`

```

I'm working on a project using MicroFocus COBOL which is going to be
ported to both the UNIX and NT OS environments. I needed a way to
serialize the generation of sequence numbers which will be used as keys for
SQL Tables. I don't want to use SELECT MAX() because of performance issues
or make use of a Sequence Number table because of locking issues.

I thought of using a shared memory area which will be accessed by processes
and tried to implement it using CBL_PUT_SHMEM but it only allows sharing
between run units and does not allow sharing between two process. The MF
Cobol in HP has an example of using semaphores, etc. but I'm looking for
another solution which would be more portable between NT and UNIX flavors.


TIA.
```

#### ↳ Re: Help Needed for Sharing Memory Between Processes

- **From:** "doug miller" <ua-author-95539@usenetarchives.gap>
- **Date:** 1997-05-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26b58c5ecb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5fe6$403d3080$575e3681@stanley>`
- **References:** `<01bc5fe6$403d3080$575e3681@stanley>`

```

"Stanley Layson" wrote:
› I'm working on a  project using MicroFocus COBOL which is going to be
› ported to both the UNIX and NT OS environments.  I needed a way to
…[4 more quoted lines elided]…
› I thought of using a shared memory area which will be accessed by processes

This won't eliminate the locking issues encountered with a table. You still have
the same synchronization problem of one process attempting to read a shared
resource while another is updating it (or vice versa). The only difference is that
the processes are contending for access to a file in one case, and to an area
in memory in the other.
```

#### ↳ Re: Help Needed for Sharing Memory Between Processes

- **From:** "sail..." <ua-author-6589447@usenetarchives.gap>
- **Date:** 1997-05-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26b58c5ecb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5fe6$403d3080$575e3681@stanley>`
- **References:** `<01bc5fe6$403d3080$575e3681@stanley>`

```

"Stanley Layson" wrote:

› I'm working on a  project using MicroFocus COBOL which is going to be
› ported to both the UNIX and NT OS environments.  I needed a way to
› serialize the generation of sequence numbers which will be used as keys for
› SQL Tables.  I don't want to use SELECT MAX() because of performance issues
› or make use of a Sequence Number table because of locking issues.  
 
› I thought of using a shared memory area which will be accessed by processes
› and tried to implement it using CBL_PUT_SHMEM but it only allows sharing
› between run units and does not allow sharing between two process.  The MF
› Cobol in HP has an example of using semaphores, etc.  but I'm looking for
› another solution which would be more portable between NT and UNIX flavors. 


Stan, I may be about to make a total ass of myself in public, but I think the
problem is simple. Create a stack as a simple file. Usually there is only one
number on the stack, the next sequence number. Since your using programs will
lock the stack file, take the number off of it, and write it back after
incrimenting it by one, there is no chance that two processes will get the same
number. It will work in any OS environment.

Now here is a little twist that I use. From time to time a program will take
the next sequence number from the file, incriment the number, write it back to
the file, unlock the file AND THEN the user will abandon the record. There
would be a hole in your sequence. Many times this is unimportant, but I do not
like holes in what should be sequences. Here is the trick. You push the
abandoned number back onto the stack file. The next program wishing a sequence
number will take that next number, use it, and NOT write it back. The sequences
may not be the exact order, but an abandoned sequence will be used as soon as
possible.

I hope this helps, or maybe I do not understand your problem. With respect.
Bob

.
Robert Schuldenfrei
S. I. Inc.
32 Ridley Road
Dedham, MA 02026
Voice: (617) 329-4828
FAX: (617) 329-1696
E-Mail: b.··.@s-i··c.com
WWW: http://www.tiac.net/users/tangaroa/index.html
```

##### ↳ ↳ Re: Help Needed for Sharing Memory Between Processes

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-05-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26b58c5ecb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-26b58c5ecb-p3@usenetarchives.gap>`
- **References:** `<01bc5fe6$403d3080$575e3681@stanley> <gap-26b58c5ecb-p3@usenetarchives.gap>`

```

In article <5lb00m$d.··.@new··c.net>
› sai··.@ti··c.net "Robert Schuldenfrei" writes:
› "Stanley Layson"  wrote:
…[5 more quoted lines elided]…
› and write it back after incrimenting it by one...

True, if you use a file the runtime system (or operating system)
will take care of process interlocking for you. Some operating
systems will even co-ordinate the update of a shared file in
shared memory (buffers, cache etc) so it will run quickly.

Otherwise, you can use this 4-stage process in shared memory:

1. ASK FOR CONTROL
Wait until the 'semaphore' variable is zero; then
Write your own unique number (process id) into the semaphore
2. SEE IF YOU GOT CONTROL
Read the semaphore (someone else might also have changed it)
If it is NOT your own unique number, restart at step 1
3. EXECUTE PROTECTED CODE
Eg read & update the sequence number, preferably quickly
(Beware of interrupts and recursive routines)
4. RELEASE CONTROL
Write zero into the semaphore variable to release it.

There are more levels of sophistication if needed, eg variable
retry delay (based on the unique number) to avoid processor races.

Best of luck!
Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
