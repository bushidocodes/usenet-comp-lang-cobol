[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Listings and COPY/REPLACING

_2 messages · 2 participants · 1998-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Listings and COPY/REPLACING

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<69v7rb$qsb@sjx-ixn1.ix.netcom.com>`

```

I am having a discussion with some members of the J4 COBOL committee about
listings of source code with COPY/REPLACING. Although I have seen some
others, I primarily know the IBM and Micro Focus COBOL products. Therefore,
I am interested in knowing what other products do with this. Can you answer
the following and tell me exactly what compiler you are talking about (I
would like to get as many answers as possible):

When you get a listing of source code that includes a COPY/REPLACING
statement, does the listing show:

QUESTION !

A) The original source code before the REPLACING was done
B) The source code with REPLACING done
C) Both the original source code and the replaced source code
D) There is a compiler (or other) option that lets you select which
type of code
you see

QUESTION 2

Regardless of what your current (or past) compiler does (did), if
you were trying to design a new "user-friendly" compiler, which of the
options above would you like to see in the listing?

* * * * * * * * * * * * * * *

P.S. Both as a programmer and as a (previous) employee of a compiler vendor,
I really HATE the COPY/REPLACING option. I know there are times that it
works great and seems to meet a real business need. However, it is a BEAR
to try and debug and often to maintain. No matter how long I have worked
with the COBOL Standard and various compilers, the rules still confuse me in
places.

Therefore, please do not reply to this thread with why (or why not) you
think COPY/REPLACING is a good thing. If you want to start that discussion,
please start you own thread and I will be happy to join the ranting and
raving there.
```

#### ↳ Re: Listings and COPY/REPLACING

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-01-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cd9318ec6f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<69v7rb$qsb@sjx-ixn1.ix.netcom.com>`
- **References:** `<69v7rb$qsb@sjx-ixn1.ix.netcom.com>`

```

William M. Klein wrote:
›
› I am having a discussion with some members of the J4 COBOL committee bout
› listings of source code with COPY/REPLACING.

Last I heard (in 1981), J4 considered the source listing was beyond the
staandard's scope.

› When you get a listing of source code that includes a COPY/REPLACING
› statement, does the listing show:
…[8 more quoted lines elided]…
›             you  see
 
› I've only ever seen A.
 
›     QUESTION 2
› 
›         Regardless of what your current (or past) compiler does (did), if
› you were trying to design a new "user-friendly" compiler, which of the
› options above would you like to see in the listing?

I don't want a listing, I want an editor with interactive
cross-reference, error files, code listings, etc. I do expect an
interactive cross-reference to use the effective name. I get most of
this functionality from the Unisys A Series System Editor. When you use
the cross-reference to go to a line with a replaced word on it, the
Editor just goes to the beginning of the line, it doesn't find the right
token.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
