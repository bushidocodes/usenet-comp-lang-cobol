[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AS/400 (I Series) Support

_3 messages · 3 participants · 2003-03_

**Topics:** [`AS/400, iSeries, RPG`](../topics.md#as400)

---

### AS/400 (I Series) Support

- **From:** Floyd Johnson <fjohnso5@rochester.rr.com>
- **Date:** 2003-03-04T19:23:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E64FD2B.5050904@rochester.rr.com>`

```
Friends:

Some of you may remember when I wrote last fall about receiving an 
AS/400 as a gift from our college bookstore.  We finally received the 
machine last Christmas and are now planning to deploy it sometime during 
the summer months.

IBM has offered to help us get it "up and running". They understand, 
through the brief contact that we have had with them, that we have the 
hardware but no software.

My anticipated use of the hardware is to support our File Structures 
course (using COBOL) and our upper division DBMS course (using ???).

My question for you - what software to I need to be looking for.  I know 
nothing about the AS/400 - and we will need to build this thing from the 
OS on up to support the above mentioned courses.

Thank you for any hints, hand holding, or suggestions you can provide.
I am a good learner - I spent the last two years installing LINUX for 
the first time and have a reasonably stable network working, though I 
had used UNIX for most of the previous four years.

I suspect that we will get to the same place with the AS/400.  Some 
years ago I was using an IBM 9370 for an extended period of time (alas, 
using FORTRAN), so I have been exposed to the IBM platform to some extent.

Thanks again.

Floyd Johnson
Assistant Professor
     Computer Science
```

#### ↳ Re: AS/400 (I Series) Support

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-03-04T22:21:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<738a6v0959iho4l45a2mk16pbg725je3uo@4ax.com>`
- **References:** `<3E64FD2B.5050904@rochester.rr.com>`

```
On Tue, 04 Mar 2003 19:23:25 GMT, Floyd Johnson
<fjohnso5@rochester.rr.com> wrote:

>
>IBM has offered to help us get it "up and running". They understand, 
>through the brief contact that we have had with them, that we have the 
>hardware but no software.
When they say they will help does that mean that they will supply the
software free of charge or at a very low price, or just help to
install/configure whatever you buy?
If it is free try and get your hand in (at least) the following
WebSphere
COBOL/400 and ILE-COBOL
RPG/400
CL/400 (just mandatory if you whish to do anything usefull)
C/C++ compiler
JAVA Development Kit (the full thing, not just the runtime)
And try and get licenses of Client Access and Personal Comunications
also.
(there may be other things but I don't remember).

>
>My anticipated use of the hardware is to support our File Structures 
>course (using COBOL) and our upper division DBMS course (using ???).
You will get IBM DB2 as a base installation. (not UDB). This may be
enough for what your course requires.

COBOL/400 or ILE-COBOL are both separately licensed, and you may need
to buy a license for either of them. (bear in mind that COBOL/400 does
NOT have all the intrinsic functions that ILE-COBOL has, this just in
case these are part of your course).

Also depending on the operating system version that you can install in
that specific model, you may also be able to install at any time, and
for a period of 70 days any of the development tools available for
that platform which is very handy sometimes. (whether you can do this
more than once I don't know!!)
>
>My question for you - what software to I need to be looking for.  I know 
…[6 more quoted lines elided]…
>had used UNIX for most of the previous four years.
Be very carefull with authorities.
Some "managers" give to much authority because they don't know how to
do things and they get some big surprises sometimes.
Use group authorities as much as possible.
Use Menu/programs with `"owner" authorities, and don't give individual
authorities higher than "*use" unless required. (e.g. you can set a
menu/program (B) with authority to change a file (C), give a user (A)
authority to use that program (B), even though the user may not have
any authority to file (C).
Don't give "*allobj" authorities to anyone 
Use a "security level" of at least 20.

The AS/400 has lots of help in each individual command, but sometimes
it is still not clear what a particular command requires. Old manuals
were great to search, but the new ones requires that you install all
the manuals in the AS400, configure the HTTP server and that Java
runtime is also installed. Try and get some help from IBM in this
area.



Regards

FF
Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: AS/400 (I Series) Support

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-03-04T16:10:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0303041610.7e37febd@posting.google.com>`
- **References:** `<3E64FD2B.5050904@rochester.rr.com>`

```
My AS/400 experience is mostly peripheral - so take this with a chunk
of rock salt ---

As I understand it the AS/400's architecture is build AROUND a built
in Relational database.  It's part of the basic setup.  COBOL is an
EXTRA on the AS/400.

Another top post ends here.

Floyd Johnson <fjohnso5@rochester.rr.com> wrote in message news:<3E64FD2B.5050904@rochester.rr.com>...
> Friends:
> 
…[29 more quoted lines elided]…
>      Computer Science
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
