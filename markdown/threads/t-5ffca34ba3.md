[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling programs

_5 messages · 2 participants · 1999-11_

---

### Calling programs

- **From:** ba600@FreeNet.Carleton.CA (Mike Kenzie)
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80k5ci$h07@freenet-news.carleton.ca>`

```

Well I couldn' get the fujitsu cobol loaded so I'm using an old realia
compiler.  My win 3.1 disks are all bad (3 sets!)

I created a program to read a indexed file.

I would like to be able to call this program from another.

Do I have to link them?  I've done this before with I/O routines and do
not recall linking them, is this a REALIA thing?
```

#### ↳ Re: Calling programs

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991113173226.26112.00000436@ngol02.aol.com>`
- **References:** `<80k5ci$h07@freenet-news.carleton.ca>`

```
In article <80k5ci$h07@freenet-news.carleton.ca>, ba600@FreeNet.Carleton.CA
(Mike Kenzie) writes:

>
>Well I couldn' get the fujitsu cobol loaded so I'm using an old realia
…[8 more quoted lines elided]…
>

What problems did you have with Fujitsu COBOL vs 3.0?

As for linking sub programs, you will need to first recompile as a SUB 
vs MAIN then LINK to DLL vs EXE. the resulting LIB, EXP, DLL can be
linked with the new MAIN that calls your sub-program for indexed file 
handling.   Depending on whether you use Dynamic or Static linking,
will determine whether it is necessary to include the DLL's LIB in the
Link process for the Main program.

Hope that this helps.
```

##### ↳ ↳ Re: Calling programs

- **From:** ba600@FreeNet.Carleton.CA (Mike Kenzie)
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80mmmk$e8d@freenet-news.carleton.ca>`
- **References:** `<80k5ci$h07@freenet-news.carleton.ca> <19991113173226.26112.00000436@ngol02.aol.com>`

```

Sff5ky (sff5ky@aol.comxxx123) writes:
> In article <80k5ci$h07@freenet-news.carleton.ca>, ba600@FreeNet.Carleton.CA
> (Mike Kenzie) writes:
…[13 more quoted lines elided]…
> What problems did you have with Fujitsu COBOL vs 3.0?

I  can run it from my NT box, but I need it to run on an older DOS
machine, and it won't run under DOS. 


> 
> As for linking sub programs, you will need to first recompile as a SUB 
…[4 more quoted lines elided]…
> Link process for the Main program.

IT was the dynamic/static trouble initially, removed the quotes and it
blew up on memory troubles trying to add 1 record to the file.

The goal was to have a file that could be called from another or run
directly from batch file.
```

###### ↳ ↳ ↳ Re: Calling programs

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991114193633.26391.00000702@ngol03.aol.com>`
- **References:** `<80mmmk$e8d@freenet-news.carleton.ca>`

```
In article <80mmmk$e8d@freenet-news.carleton.ca>, ba600@FreeNet.Carleton.CA
(Mike Kenzie) writes:

>> 
>> What problems did you have with Fujitsu COBOL vs 3.0?
…[4 more quoted lines elided]…
>

That may be because the vs 3.0 compiler is not a 16-bit compiler.
Unfortunately, I think that the only way to get the 16-bit compiler
from Fujitsu, is on the old 3.0 demo disks that had vs 2.0 as an 
alternate compiler.  There are some more restrictions on program
size  and maybe some of the newer standards.
```

###### ↳ ↳ ↳ Re: Calling programs

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991114193634.26391.00000703@ngol03.aol.com>`
- **References:** `<80mmmk$e8d@freenet-news.carleton.ca>`

```
In article <80mmmk$e8d@freenet-news.carleton.ca>, ba600@FreeNet.Carleton.CA
(Mike Kenzie) writes:

> Link process for the Main program.
>
…[5 more quoted lines elided]…
>

Using quotes around the program name makes the call a static link.
removing the quotes should make it a dynamic call.  I am not sure of
why switching to a dynamic call would cause the system to blow up.
Make sure that the DLL has some way of keeping track of whether it 
is the first call and proper setup operations are handled.
I doubt that you would be able to run the DLL standalone from the DOS Prompt.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
