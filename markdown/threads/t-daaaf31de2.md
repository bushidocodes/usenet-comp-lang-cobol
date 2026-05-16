[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie: Fujitsu Compiling Question

_3 messages · 3 participants · 2000-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Newbie: Fujitsu Compiling Question

- **From:** zoopra@my-deja.com
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<863ihi$esp$1@nnrp1.deja.com>`

```
I am new to COBOL for about 5 months now (after taking a course at
school) and I was pleased to find a Fujitsu COBOL V3 for free (college
student bank account) and I have a question on the compiling.  Is there
any possible way to compile my program with the needed DLL's?  I am
running my program on a seperate computer and it is asking for about 10
DLL's that I need to transfer over to the other computer.  Is there a
while to compile all these together?  Also, with this get rid of the
Runtime Environment Setup when I start the program?

Thanks in Advanced!

Scott Bowling


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Newbie: Fujitsu Compiling Question

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XrHx8GA0edh4EwAz@ld50macca.demon.co.uk>`
- **References:** `<863ihi$esp$1@nnrp1.deja.com>`

```
I think that if you read the licence agreement (by which you sell your
soul to Bill Gates merely by handling it) you will see that you are
licenced only to run the application on the machine with the free
compiler installed. I tried to do as you have done and found the list of
dll, etc., exceeded 10 and the instructions for setting up an RTS  (run
time system) on other machines was incomplete in it's listing of
required files. I gave up and re-wrote the (beautifully structured IMHO
;-) code into MF Cobol and created an exe that way. The MF Cobol exe
does not need a RTS to be set up. 

In article <863ihi$esp$1@nnrp1.deja.com>, zoopra@my-deja.com writes
>I am new to COBOL for about 5 months now (after taking a course at
>school) and I was pleased to find a Fujitsu COBOL V3 for free (college
…[13 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: Newbie: Fujitsu Compiling Question

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000119195739.02746.00000240@nso-fp.aol.com>`
- **References:** `<863ihi$esp$1@nnrp1.deja.com>`

```
In article <863ihi$esp$1@nnrp1.deja.com>, zoopra@my-deja.com writes:

>school) and I was pleased to find a Fujitsu COBOL V3 for free (college
>student bank account) and I have a question on the compiling.  Is there
…[5 more quoted lines elided]…
>

I belive that if you use the getting started guide, it points to all the
DLLs that need to be copied to another machine for use of your new EXE.
The trick is placing all the DLL's in a directory that exists on your PATH
statement.   Unfortunately, there are some 5-8M of DLL's that need to be
copied for the RTS.   As for the Run-Time Environment setup,
you should be able to edit the COBOL85.CBR file and add 

[yourpgm]
@WinCloseMsg=OFF
@EnvSetWindow=UNUSE

to the parameter list for your program.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
