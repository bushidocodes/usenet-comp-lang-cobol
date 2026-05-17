[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Debugg to C subprogram

_2 messages · 2 participants · 1997-01_

---

### Debugg to C subprogram

- **From:** "marcela godoy" <ua-author-17071734@usenetarchives.gap>
- **Date:** 1997-01-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32ED74C5.6BB1@tandem.cl>`

```

I am using microfocus V.3.2., my programs call C subprograms and if I
make debug with animator of MF occurs the next error when call c
subprogram : "CALLED PROGRAM FILE NOT FOUND IN DRIVE/DIRECTORY ERROR
173" and cann't continue execution, then, Can I execute the C subprogram
and not obtain the error 173 in the debugg of the principal program?

thanks in progress.
mgo··.@tan··m.cl
```

#### ↳ Re: Debugg to C subprogram

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-01-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0be87bb48b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32ED74C5.6BB1@tandem.cl>`
- **References:** `<32ED74C5.6BB1@tandem.cl>`

```

Marcela Godoy wrote:
› 
› I am using microfocus V.3.2., my programs call C subprograms and if I
…[3 more quoted lines elided]…
›  and not obtain the error 173 in the debugg of the principal program?

Hi.

This is most likely because the runtime system which is executing your
program
under the Animator can't "see" your C functions. If they are in a DLL,
then
a statement such as 'SET p-ptr TO ENTRY "CFUNCS.DLL"' at the start of
your
.int code should make them visible (where p-ptr is declared as USAGE
PROCEDURE-POINTER and "CFUNCS.DLL" is the name of your DLL).
The reason this is probably happening automatically outside of the
Animator is
that you are most likely using a special trigger program to run your
application
which loads the DLL at startup. The Animator trigger program will not
know this
is necessary.

One other thing to bear in mind is that on 16-bit products, the DLL in
question
will not load using this method if there is no function in the DLL with
the same
name as the DLL itself. However, on 32-bit products the DLL will load
correctly
and all the entrypoints will be visible.

If this is no help, then please explain how your C functions are
packaged and
how you normally run the program without using Animator.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
