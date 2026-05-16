[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# command line options for old viscob and vclink commands

_4 messages · 3 participants · 2002-08_

---

### command line options for old viscob and vclink commands

- **From:** bob.webb@cellcom.com (Bob Webb)
- **Date:** 2002-08-12T08:12:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24dcc159.0208120712.5e53d68b@posting.google.com>`

```
I run an old Visual Cobol system on HP-UX.  Does anyone know more
about the viscob and vclink commands than what is printed on the
command line text that follows.  I would greatly appreciate some
descriptions of the command line options.  Are there manuals available
anywhere?

Here is the output from the 'viscob %help' and the bare 'vclink -h'
commands which will show everything that I know and give appropriate
version information for anyone who might be able to help me.

bwebb@devx:~/tenx/source$ viscob %help

 Visual COBOL Compiler
 Version 3.6.08 (HP-UX/HPPA) 
Copyright (C) 1987 to 1996, Micro Focus Technology NV

start:    viscob   [<program>  [<files>  [<options>]]]
program:  name of a COBOL program
files:    <object file> [<listing file> [<directory of the work
file>]]
options:  option sign MS-DOS, DOS-Extender and Windows: '/' - UNIX:
'%'
      acheck  ansi    bc4     bin1    bin6    bs2000  cancel  check  
compb
      compx   cref    debug   dyncall ebcdic  fext    flagmf  float  
fobs
      help    hilf    ibm     icheck  low     map     mfsign  notrunc
ntrext
      nobss   objl    oldsync opt0    omf32   pcheck  pre     ref97  
saa
      sbug    srcl    sts     sync    upre    xdebug  xfloat  xopen  
xpre
      ?
      errlev=<num>  errlim=<num>  lines=<num>  ctrlevel=<num> 
ulevel=<num>
      copy=<copy list>   nokeyword=<name list>    nowarn=<error number
list>
      pars=<file name>   dynlist=<file name>

P006  ####  ERROR OPENING SOURCE FILE :  
 ABNORMAL END 000E/0002: CANCEL INITIATED
bwebb@devx:~/tenx/source$ vclink -h

usage: vclink [-v] [-n] [-d] [-r] [-i arg] [-x lib] [-o file] [-- str]
objs libs

flags: -h        (Help)
       -v        (Turn on verbose mode)
       -n        (Do not strip symbol table from executable)
       -d        (Link VISUAL run-time system (RTS) dynamically)
       -r        (Link VISUAL RTS at this position - default is to
append)
       -i arg    (Use arg as ISAM lib in place of VCISAM - see
example)
       -x lib    (Create dynamic-links to all VISUAL objects in lib -
see info2)
       -o file   (Create an executable named 'file')
       -- string (Pass string directly to cc/ld/cob)

info1: Flags not understood by vclink are passed on to cc/ld/cob.
       To pass a vclink flag to cc/ld/cob, or if a cc/ld/cob flag has
a
       space-separated argument, use the -- option.

info2: The -x option must be used when linking shared-objects or
archives that
       contain VISUAL routines that are to be dynamically-callable.

e.g.   vclink x.o -v -- '-L ..' -lprog -i -lisam
       vclink -o prog x.o -x ../libprog.a -r -lmylib -- -v
```

#### ↳ Re: command line options for old viscob and vclink commands

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-12T10:34:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aj8khi02prd@enews4.newsguy.com>`
- **References:** `<24dcc159.0208120712.5e53d68b@posting.google.com>`

```

"Bob Webb" <bob.webb@cellcom.com> wrote in message
news:24dcc159.0208120712.5e53d68b@posting.google.com...
> I run an old Visual Cobol system on HP-UX.  Does anyone know
more
> about the viscob and vclink commands than what is printed on
the
> command line text that follows.  I would greatly appreciate
some
> descriptions of the command line options.  Are there manuals
available
> anywhere?

That looks like the mbp compiler that was picked up by
MicroFocus.  It's since been discontinued, but you might be
able to score some manuals from MF.  Chris Glazier was the last
contact I knew of there, but did not have many direct
interactions with him.  (That was more than a year ago at this
point as well.)

I have a copy of viscob.hlp -- in windows help file format.  Is
that of use to you?
```

##### ↳ ↳ Re: command line options for old viscob and vclink commands

- **From:** bob.webb@cellcom.com (Bob Webb)
- **Date:** 2002-08-14T05:09:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24dcc159.0208140409.5cfc4bee@posting.google.com>`
- **References:** `<24dcc159.0208120712.5e53d68b@posting.google.com> <aj8khi02prd@enews4.newsguy.com>`

```
Thanks, I received the .hlp file and it was greatly appreciated.

"Grinder" <grinder@no.spam.maam.com> wrote in message news:<aj8khi02prd@enews4.newsguy.com>...
> "Bob Webb" <bob.webb@cellcom.com> wrote in message
> news:24dcc159.0208120712.5e53d68b@posting.google.com...
> > I run an old Visual Cobol system on HP-UX.  Does anyone know

> 
> That looks like the mbp compiler that was picked up by
…[7 more quoted lines elided]…
> that of use to you?
```

###### ↳ ↳ ↳ Re: command line options for old viscob and vclink commands

- **From:** ekky@hanse-box.de (Ekky Panneck)
- **Date:** 2002-08-15T12:52:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1f448c96.0208151152.65dd5771@posting.google.com>`
- **References:** `<24dcc159.0208120712.5e53d68b@posting.google.com> <aj8khi02prd@enews4.newsguy.com> <24dcc159.0208140409.5cfc4bee@posting.google.com>`

```
I got mbp VISCOB for DOS, so I hope options had not changed.
Please let me know exactly what is wanted and will try to 
make a few digis from that pages.

Ekky
 news:<24dcc159.0208140409.5cfc4bee@posting.google.com>...
> Thanks, I received the .hlp file and it was greatly appreciated.
> 
…[14 more quoted lines elided]…
> > that of use to you?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
