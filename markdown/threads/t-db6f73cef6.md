[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating PDS members from a batch program

_4 messages · 4 participants · 1998-10_

---

### Creating PDS members from a batch program

- **From:** don_weigend@email.com (Donald Weigend)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1104_907704981@hen.arinet.com>`

```
Greetings All,

Does anyone have any COBOL code examples that create members in a PDS as output. I would like to enhance a 
program that generates JCL for several batch jobs. This program currently stores all the JCL together in a single 
sequential file, I then have to split these jobs up manually. I would appreciate any help anyone can give.

Donald Weigend
SPR Inc.
```

#### ↳ Re: Creating PDS members from a batch program

- **From:** "Paul M. Dorfman" <pdorfma@ucs.att.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361A8C52.B33DE2E3@ucs.att.com>`
- **References:** `<1104_907704981@hen.arinet.com>`

```
Donald Weigend wrote:
> 
> Greetings All,
…[6 more quoted lines elided]…
> SPR Inc.

Donald,

Others may point you in the right direction as to how to do it strictly
in COBOL (it is going to be tricky, to say at least). However, if you
are lucky to have the SAS System installed at your site, check the
procedures PDS, PDSCOPY, and SOURCE. With these, you can do everything
you need and a lot more (including creating inputs for IBM utes, if
necesary). Since these procs are MVS-specific, they are not listed in
the SAS Procedures Guide, but rather in the SAS Companion for the MVS
Environment. The text is amply supplied with examples, so it will not
take you long to get it up and running, even if you have never heard of
SAS before. By the way, the SOURCE procedure is quite useful in
producing a file listing of PDS members with all the satellite
information (almost exactly the way you can see it in 3.4).

Good luck.

Kind regards, Paul.
```

#### ↳ Re: Creating PDS members from a batch program

- **From:** PPP <ABCDE@ddd.ddd.com>
- **Date:** 1998-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361EC7F2.B3D@ddd.ddd.com>`
- **References:** `<1104_907704981@hen.arinet.com>`

```
Donald Weigend wrote:
> 
> Greetings All,
…[6 more quoted lines elided]…
> SPR Inc.

I've a rather stupid method which may be usefull to you.
The material I need are
A PDS
2 program, 
	PGM A your utility program,
	PGM B my program.
2 JCL, 
	JCL B - to run PGM B and submit the JCL A 
	JCL A - your JCL to execute PGM A but the DD statement are replaced by
symbol.
 e.g. //OUT1     DD DSN=PROJECT1.TASK1.LIB(&S),DISP=SHR 

Details

PGM B will need to accept the member name of the resulting "report"
either from the input card are stored in an DSN.
Then PGM B will read to JCL A and replace the symbol(&M) with the member
name.
Finally PGM B will output the formatted JCL A to "internal reader".

When you want to run JCL A, simply submit JCL B.

Hope you can understand what I written.
```

##### ↳ ↳ Re: Creating PDS members from a batch program

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdf5ec$cac8b4c0$c58c3398@us0071826>`
- **References:** `<1104_907704981@hen.arinet.com> <361EC7F2.B3D@ddd.ddd.com>`

```
IEBUPDTE

PPP <ABCDE@ddd.ddd.com> wrote in article <361EC7F2.B3D@ddd.ddd.com>...
| Donald Weigend wrote:
| > 
| > Greetings All,
| > 
| > Does anyone have any COBOL code examples that create members in a PDS
as output. I would like to enhance a
| > program that generates JCL for several batch jobs. This program
currently stores all the JCL together in a single
| > sequential file, I then have to split these jobs up manually. I would
appreciate any help anyone can give.
| > 
| > Donald Weigend
…[25 more quoted lines elided]…
|
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
