[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Meets JAVA

_5 messages · 4 participants · 2003-10_

---

### COBOL Meets JAVA

- **From:** mossjm@wideopenwest.com (QCBLSRC)
- **Date:** 2003-10-19T09:36:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3473e5fa.0310190836.5e5d4c3f@posting.google.com>`

```
An excerpt from a conversation I had with one of my COBOL programmers
who is learning Java.

Manager: Java web programming is alot different than COBOL.  You have
alot to learn.  >>> Conversation turns to record processing >>

Programmer: So, how do you write a record in Java?

Manager: You don't.  You have to do it field by field with an SQL
statement.

Programmer: That's fucked!

Manager: ROFLMAO
```

#### ↳ Re: COBOL Meets JAVA

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-10-19T17:38:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-5E9B17.17384119102003@corp.supernews.com>`
- **References:** `<3473e5fa.0310190836.5e5d4c3f@posting.google.com>`

```
In article <3473e5fa.0310190836.5e5d4c3f@posting.google.com>,
 mossjm@wideopenwest.com (QCBLSRC) wrote:

> An excerpt from a conversation I had with one of my COBOL programmers
> who is learning Java.
…[11 more quoted lines elided]…
> Manager: ROFLMAO

Errrr, I hate to point out, but all the Streams subclasses support the 
ability to write a byte array (record).  

And any object that implements the interface to serialize itself can 
become a byte array quite easily.

So an alternative answer might have been:

      myStream.write( myObject.Serialize );
```

##### ↳ ↳ Re: COBOL Meets JAVA

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-10-19T23:42:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031019194203.13842.00001108@mb-m29.aol.com>`
- **References:** `<joe_zitzelberger-5E9B17.17384119102003@corp.supernews.com>`

```
Joe Zitzelberger joe_zitzelberger@nospam.com 
Date: 10/19/03 4:38 PM EST
Message-id: <joe_zitzelberger-5E9B17.17384119102003@corp.supernews.com>

writes an excellent, and conscise response to a rufian ...

<<

So an alternative answer might have been:

      myStream.write( myObject.Serialize );

>>

Also, arrays are objects, too. So with proper coding you can read a whole file
of objects into memory with one invocation, and after manipulating the heck out
of it (including inserting or deleting members, you can write the whole thing
back out, with merely one more invocation. OOP tools are definitely absolutely
amazing, they definitely automate the technician.

With proper encoding of the objects as serializable, the whole concept of the
read loop, and the write loop are gone ... that saves money in development and
maintenance. You need decent designers to engage this stuff.

So, ... the question becomes, ... do we have the foundation classes in COBOL
compiler packages from major vendors that will support serious automation of
the technicians in COBOL yet. Or do managers have to turn to Java for
efficiency in the management of the labor resource, ... still?

Joe, I cannot believe how polite you were to 
the OT.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: COBOL Meets JAVA

- **From:** mossjm@wideopenwest.com (QCBLSRC)
- **Date:** 2003-10-19T20:43:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3473e5fa.0310191943.23c59ca8@posting.google.com>`
- **References:** `<3473e5fa.0310190836.5e5d4c3f@posting.google.com> <joe_zitzelberger-5E9B17.17384119102003@corp.supernews.com>`

```
Joe,

I stand corrected in application.
I was referring to using a JDBC connection to a DB2/400 database.
In this scenario, there is no way to use a "write" statement.
However, your suggestion is true for text files.

John
```

#### ↳ Re: COBOL Meets JAVA

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-10-21T10:46:18+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn2v3m$9k3$1@hyperion.microfocus.com>`
- **References:** `<3473e5fa.0310190836.5e5d4c3f@posting.google.com>`

```
Call a COBOL program to do it for you.

With Micro Focus Net Express and Server Express this is relatively straight
forward.

Paul
www.microfocus.com

"QCBLSRC" <mossjm@wideopenwest.com> wrote in message
news:3473e5fa.0310190836.5e5d4c3f@posting.google.com...
> An excerpt from a conversation I had with one of my COBOL programmers
> who is learning Java.
…[11 more quoted lines elided]…
> Manager: ROFLMAO
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
