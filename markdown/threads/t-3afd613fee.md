[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP conversion to decimal using MicroFocus Netexpress COBOL

_4 messages · 4 participants · 2003-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COMP conversion to decimal using MicroFocus Netexpress COBOL

- **From:** "David Thomas" <d.m.thomas@swan.ac.uk>
- **Date:** 2003-01-30T17:25:25
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1bn11$glb$1@news.swman.net.uk>`

```
Got a peculiar one here.

I'm extracting some salary data from a payroll system running on VMS with
MicroFocus COBOL.

We are migrating the system to a Windows/Intel platform and have to extract
the data from the system on the VMS system to the new server.

Running a simple COBOL program to extract basic ID detail and salary from
our VMS version of the payroll system, I can extract the data perfectly.

In the FD section, the salary in the master table is defined as 'S9(7)V99
COMP', and when output it's defined as 'ZZZZZZZZ9.99'. On VMS it works
fine - all amounts returned normally.

If I run the same COBOL code against the new Windows version, the salary is
not converted properly - all amounts are returned as '538976288'.

Not just the salary but any amount using 'S9(7)V99 COMP'.

'S9(4) COMP' amounts are fine - would this indicate a problem with 'S9(7)V99
COMP' which (I think) is 4 bytes as opposed to 2 bytes for 'S9(4) COMP'?



Any information for a humble COBOL dummy, would be gratefully received.



Thanks.
```

#### ↳ Re: COMP conversion to decimal using MicroFocus Netexpress COBOL

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-30T13:25:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v3iqrsruipc3a6@corp.supernews.com>`
- **References:** `<b1bn11$glb$1@news.swman.net.uk>`

```
The value '538976288' is equal to x"20202020".
The field contains ASCII spaces!


David Thomas <d.m.thomas@swan.ac.uk> wrote in message
news:b1bn11$glb$1@news.swman.net.uk...
> Got a peculiar one here.
>
…[3 more quoted lines elided]…
> We are migrating the system to a Windows/Intel platform and have to
extract
> the data from the system on the VMS system to the new server.
>
…[7 more quoted lines elided]…
> If I run the same COBOL code against the new Windows version, the salary
is
> not converted properly - all amounts are returned as '538976288'.
>
> Not just the salary but any amount using 'S9(7)V99 COMP'.
>
> 'S9(4) COMP' amounts are fine - would this indicate a problem with
'S9(7)V99
> COMP' which (I think) is 4 bytes as opposed to 2 bytes for 'S9(4) COMP'?
>
…[9 more quoted lines elided]…
>
```

#### ↳ Re: COMP conversion to decimal using MicroFocus Netexpress COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-01-30T13:24:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1bu5k$fjq$1@slb4.atl.mindspring.net>`
- **References:** `<b1bn11$glb$1@news.swman.net.uk>`

```
Check your setting of the Micro Focus "byte-mode" directive.  It may be that
VMS supports only half-word/whole-word binary fields - but you have set your
Micro Focus environment to support 1, 2, 3, & 4 byte binaries.  This may
cause your "entire" FD to map incorrectly.
```

#### ↳ Re: COMP conversion to decimal using MicroFocus Netexpress COBOL

- **From:** James Johnson <saildot.maryland@verizon.net>
- **Date:** 2003-01-31T01:26:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4bnj3vcf7vvolgr81sde3ojfabpd482jhr@4ax.com>`
- **References:** `<b1bn11$glb$1@news.swman.net.uk>`

```
We have had a problem where if it is defined as S9(5)V2 and the input file has
special characters in that field!@#$%^&*(), instead of error with a type
missmatch it takes the last digit of the octal ascii value for that character
and keeps on happily processing. This is just the latest bug involving numeric
handling we have found on this conversion project.  This is on a Sun Solaris
system.  My impression is MF needs to do some more QC on its compilers.  Chasing
compiler bugs is getting very old.

JJ

On Thu, 30 Jan 2003 17:25:25 -0000, "David Thomas" <d.m.thomas@swan.ac.uk>
wrote:

>Got a peculiar one here.
>
…[29 more quoted lines elided]…
>

James Johnson
remove the dot from after sail in email address to reply
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
