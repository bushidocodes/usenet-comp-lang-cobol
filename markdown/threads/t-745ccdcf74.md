[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Query about Compilation

_2 messages · 2 participants · 1996-11_

---

### Query about Compilation

- **From:** "kumar cs" <ua-author-17086796@usenetarchives.gap>
- **Date:** 1996-11-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<329597AB.1FF1@geocities.com>`

```

Hi,

I'm Kumar, and I'm having a beeg problem with unresolved symbols during
linking in object files to form an executable :-
I'm using MFCOBOL version 3.2.43be on SCO unix 3.2
here is the command line :-

cob -xe "" -d mFFH -D ADIS a.o b.o -o outfile

The following symbols are unresolved :

_end
_return_env

Now I do NOt think these two symbols are part of the two .o files being
linked in - rarther, I found that there is a symbol called "_end" in the
cob compiler itself. I think these symbols are defined within the
compiler
itself, but I can't understand why I'm still getting unresolved symbols
error.

Actually, I have a more general problem...I don't understand what the
above
compilation line is doing - since I have no manuals for mfcobol - this
is
why I'd like some inputs on that , as well as any probable cause for the
errors, if you can guess at it!

Thank you all , please respond by mail too.

Kumar
```

#### ↳ Re: Query about Compilation

- **From:** "tony heffner" <ua-author-6589464@usenetarchives.gap>
- **Date:** 1996-11-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-745ccdcf74-p2@usenetarchives.gap>`
- **In-Reply-To:** `<329597AB.1FF1@geocities.com>`
- **References:** `<329597AB.1FF1@geocities.com>`

```

Kumar CS wrote:

› cob -xe "" -d mFFH -D ADIS a.o b.o -o outfile
› 
…[4 more quoted lines elided]…
› 

It appears you are building a custom runtime system including any
aditional
routine(s) that are in a.o and b.o. These routines will be accessable
to
any cobol programs running under this runtime (outfile). I am not sure
why you are using the -d and -D options. This may be particular to the
SCO platform. -d on HP-UX means to bind this symbol dynamically (at
runtime).
-D does not appear to be valid on HP-UX (Least it is not documented).
Also on HP-UX, in the $COBDIR/src/rts directory there is a file called
mkrts that will build the default runtime. Maybe this also exists on
SCO. Look for it and expand on it to include your objects. This will
also be useful in isolating what your current problem is.

That's about all I can do for ya.

Tony Heffner
ag··.@atl··p.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
