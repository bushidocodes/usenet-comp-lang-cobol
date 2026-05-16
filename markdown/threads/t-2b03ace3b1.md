[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress 3.1 Socket call and Connect to ODBC database

_2 messages · 2 participants · 2001-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### NetExpress 3.1 Socket call and Connect to ODBC database

- **From:** dcantua@co.la.ca.us (Daniel G. Cantua)
- **Date:** 2001-09-12T16:35:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cca870b.0109121535.30c41b66@posting.google.com>`

```
Help.  My program needs to connect to a DB2 database using an ODBC
connection.  It also must be a server receiving Berketly Sock call
from another machine.  The process is as follows.

   Connect to database using ODBC.
   Initialize Socket
   Bind Socket
   Listen for Socket
   Accept Socket when connected
   Wait for Message
   Receiver Message
   Process Message
   Send Response
   Wait for next Message
   If connect is lost go back to Listen for Socket

This works fine in animate.  But when I run at the command line it
give me a memory out of bounds error right after I connect to
database.  It is running on a WinNt 4.0 workstation.  I use the
command line compiles.  Any help will be taken.  It will have to run
using just the MicroFocus runtimes.

Daniel G. Cantua
Los Angeles County - ISD
```

#### ↳ Re: NetExpress 3.1 Socket call and Connect to ODBC database

- **From:** graham@olympic.co.uk (graham)
- **Date:** 2001-09-18T00:20:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a02b0a1.0109172320.6ebea19@posting.google.com>`
- **References:** `<6cca870b.0109121535.30c41b66@posting.google.com>`

```
When you say that it works when Animated can you clarify? Do you mean
when the whole thing was invoked by Animating? How are the two
situations different? Have you established whether the error (is it rt
error 114) occurs in your code or a library module?

The, sorry, obvious reply is that you aren't running indentical code
and that the Animator environment is different from the other
environment. Have you checked the many setup options in NetExpress for
differences between the animator and non-animator environments? The
most likely (?!?!) cause is some uninitialised pointer or array
subscript which is given a zero value in Animator but just picks up
some any old rubbish value that just happened to be there otherwise...

graham 
Olympic Computers 

dcantua@co.la.ca.us (Daniel G. Cantua) wrote in message news:<6cca870b.0109121535.30c41b66@posting.google.com>...
> Help.  My program needs to connect to a DB2 database using an ODBC
> connection.  It also must be a server receiving Berketly Sock call
…[21 more quoted lines elided]…
> Los Angeles County - ISD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
