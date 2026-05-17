[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Make makefile dependency tree

_3 messages · 3 participants · 1996-07_

---

### Make makefile dependency tree

- **From:** "10004..." <ua-author-13444638@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4tn5vj$hpr$1@mhadf.production.compuserve.com>`

```

Does anyone know a good package (freeware) to scan existing MF
Cobol application and automaticaly build a makefile? A package
able to scan the source code and build the dependency tree of all
called programs and procedure, of all included files and generate
a kind of report (or better the makefile).

Thanks for information

Alain Reymond
```

#### ↳ Re: Make makefile dependency tree

- **From:** "crookie" <ua-author-17071740@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba02d8ce5e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4tn5vj$hpr$1@mhadf.production.compuserve.com>`
- **References:** `<4tn5vj$hpr$1@mhadf.production.compuserve.com>`

```

it ain't free, but this is a standard feature of Micro Focus Visual
Object COBOL for Win95/NT.

www.microfocus.com/win95.html
Crookie
g.··.@mic··s.com

> Alain REYMOND <100··.@Com··e.COM> wrote in article
<4tn5vj$hpr$1.··.@mha··e.com>...
> Does anyone know a good package (freeware) to scan existing MF 
> Cobol application and automaticaly build a makefile? A package 
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Make makefile dependency tree

- **From:** "joan colley" <ua-author-15559010@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba02d8ce5e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ba02d8ce5e-p2@usenetarchives.gap>`
- **References:** `<4tn5vj$hpr$1@mhadf.production.compuserve.com> <gap-ba02d8ce5e-p2@usenetarchives.gap>`

```

Crookie wrote:
› 
› it ain't free, but this is a standard feature of Micro Focus Visual
…[18 more quoted lines elided]…
›› 


Crookie,

How do you handle dynamically named calls to sub modules?

Alain,

I have written a set of tools (which are not mine to give away). But here is the method.

The first tool (written in Cobol) parses the Cobol code looking for "copy" and for
"call" statements. I had to teach it to ignore some statements because the "call" is
not always the first word on a line, and both "call" and "copy" may be contained within
display statements.

I had to do some special handling for the dynamically named calls where the name of the
module is assembled from a linkage variable.

The two files output from this are then sorted uniquely. The "call" file is parsed by a
'c' program which does some recursive processing and generates a list of mains and subs
by run unit.

I then wrote a 'c' program which was originally written in 'awk' until I needed to check
whether a file was a symbolic link or a physical file (the dev region is symbolically
linked file by file to qa which is symbolically linked file by file to prd to save lots
of disk space). This program uses the 'copy' list and the run unit list to build a
standard Unix make file.

There are 5500 cobol modules in the system and 8000 copy books. The 'call and copy'
files take about 1 hour to build and in prd the makefile takes about 2 minutes to build
and about 1 hour to run plus the compile time.


As you can see - all things are possible, some take longer to create.


Good Luck,

Joan.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
