[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 85 and Linking

_5 messages · 5 participants · 1996-01_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### COBOL 85 and Linking

- **From:** "ak..." <ua-author-15198638@usenetarchives.gap>
- **Date:** 1996-01-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dmc5v$3a0@news-e1a.megaweb.com>`

```
I would like to know if there is a way to Link COBOL programs to
others computer languages such as PASCAL or C++??

Akil
```

#### ↳ Re: COBOL 85 and Linking

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-01-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da72cdd435-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4dmc5v$3a0@news-e1a.megaweb.com>`
- **References:** `<4dmc5v$3a0@news-e1a.megaweb.com>`

```
What environment. The environment is usually the big issue. Some support
cross language linking / calling, some do not.

An example is the most current IBM big iron environment called LE/370,
which supports mixes of (at least) assembler, COBOL, FORTRAN, PL/I, C,
C++.
```

#### ↳ Re: COBOL 85 and Linking

- **From:** "rbo..." <ua-author-17086166@usenetarchives.gap>
- **Date:** 1996-01-23T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da72cdd435-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4dmc5v$3a0@news-e1a.megaweb.com>`
- **References:** `<4dmc5v$3a0@news-e1a.megaweb.com>`

```


>I would like to know if there is a way to Link COBOL programs to
>others computer languages such as PASCAL or C++??
>Akil

I believe that most compilers use a CALL statement. Exactly how it will
work with another program, if it will, depends on how each one expects
the parameters to be passed.

--Ray B.
```

##### ↳ ↳ Re: COBOL 85 and Linking

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-01-25T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da72cdd435-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-da72cdd435-p3@usenetarchives.gap>`
- **References:** `<4dmc5v$3a0@news-e1a.megaweb.com> <gap-da72cdd435-p3@usenetarchives.gap>`

```
RBO··.@del··i.com wrote:

›  >I would like to know if there is a way to Link COBOL programs to
›   >others computer languages such as PASCAL or C++??
›   >Akil
 
›   I believe that most compilers use a CALL statement.  Exactly how it will 
›   work with another program, if it will, depends on how each one expects 
›   the parameters to be passed.

I'm assuming you're compiling on mainframes. I don't know about
Pascal programs, but C call infomation may be acquired from the book
"Advanced MVS JCL Examples" by James G. Janossy. I've done
COBOL-FORTRAN calls and there are some things to watch out for.

Passing data between COBOL and FORTRAN requires numerics be COMP-2 in
COBOL and REAL in FORTRAN. Each of the COBOL COMP-2s must be a
level-77 item. The order of data in the CALL must be exactly the same
in both the COBOL and FORTRAN programs. Use the FORTRAN keyword
SUBROUTINE when compiling the FORTRAN program. You must include the
parameters "NODYN,NORES" in the COBOL compiler to static-link the two
programs together (FORTRAN cannot be dynamic-linked, even among
themselves). Include in the linkage-editor both the COBOL and FORTRAN
run-time libraries in the SYSLIB DDNAME.

Example for a COBOL and VS FORTRAN run-time library names:
//SYSLIB DD DSN=SYS4.COBVS.VSCLLIB,DISP=SHR
DD DSN=SYS4.FORTVS.V2.VSF2FORT,DISP=SHR

This resolves the external cross-references between the two programs.

Then run the COBOL program as you would normally.

If the above is too confusing to understand, post here and I'll post
my source code that I use to calculate the distance between two points
given their latitude and longitude. I draw the data from a area-code
VSAM file.

Boyce Williams
"Don't flame you, don't flame me, flame the guy behind the tree."
```

#### ↳ Re: COBOL 85 and Linking

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-01-24T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da72cdd435-p5@usenetarchives.gap>`
- **In-Reply-To:** `<4dmc5v$3a0@news-e1a.megaweb.com>`
- **References:** `<4dmc5v$3a0@news-e1a.megaweb.com>`

```
ak··.@g··.com (Kwame Akil) wrote:

› I would like to know if there is a way to Link COBOL programs to
› others computer languages such as PASCAL or C++??
 
› Akil

Depends on the COBOL. Biggest problem is heap management.
Some COBOL's have their own memory management.

Check the publisher of the Pascal/C++ to see if they have a COBOL.

Realia was early Latice compat
Micro$oft has guidelines in their COBOL (Microfocus)

JR

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
