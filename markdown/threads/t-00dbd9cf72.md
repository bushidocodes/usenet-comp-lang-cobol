[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing Dynamically Allocated files ?

_2 messages · 2 participants · 1999-10_

---

### Accessing Dynamically Allocated files ?

- **From:** "Carl Holme" <carl.holme@ukgateway.net>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tqto6$8pg$1@lure.pipex.net>`

```
I am trying to write a IBM MF Batch COBOL program that will dynamically
allocate files, and then be able to either read from or write to them.

I know that you can allocate and assign a DD Name to it using the TSO
Services. But I don't know how to then reference the file within the code.
The problem is the parameters for the file, will be read in as a parameter,
therefore are variable.

The difficult part is - having allocated the file, and assigned the DD Name,
then trying to reference the DD Name without it being hard coded and defined
correctly in the File Section.

I'm wondering if this kind of request is something that would be done via an
Assembler routine?

Has anybody any suggestions?
```

#### ↳ Re: Accessing Dynamically Allocated files ?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3801DB07.3464A596@zip.com.au>`
- **References:** `<7tqto6$8pg$1@lure.pipex.net>`

```
Carl Holme wrote:
> 
> I am trying to write a IBM MF Batch COBOL program that will
…[15 more quoted lines elided]…
> Has anybody any suggestions?

There was some mention of record contains zero characters and block
contains zero characters and the largest possible record length
solving this problem.

Have not done it just read about it here.  Maybe an expert will chip
in on this one.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
