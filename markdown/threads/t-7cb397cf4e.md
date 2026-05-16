[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Kobol

_7 messages · 7 participants · 2002-12_

---

### Kobol

- **From:** vaclav snajdr <vsn@snajdr.de>
- **Date:** 2002-12-28T17:40:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E0DD3ED.4EE1BF64@snajdr.de>`

```
There is a product with this name from "www.thekompany.com",
an IDE and Cobol compiler what ranslate cobol code
to C++.
Has somebody practical experience with this product and can
give a status?
Thanks.
```

#### ↳ Re: Kobol

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-28T19:03:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021228140300.13293.00000365@mb-fr.aol.com>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de>`

```
I have purchased a copy of KOBOL but not used it yet as got busy on other
stuff.
  Let me know if you need any further information /documentation etc.
   RonGlaz6@aol.com
```

#### ↳ Re: Kobol

- **From:** "Fim W���stberg" <fim.wastberg@fimator.se>
- **Date:** 2002-12-28T23:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92qP9.3132$FF4.190414@newsb.telia.net>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de>`

```

"vaclav snajdr" <vsn@snajdr.de> skrev i meddelandet
news:3E0DD3ED.4EE1BF64@snajdr.de...
> There is a product with this name from "www.thekompany.com",
> an IDE and Cobol compiler what ranslate cobol code
…[3 more quoted lines elided]…
> Thanks.

Not so easy to compile and link from command prompt.
You must use the IDE and the editor is not so good.

Fim W�stberg
```

##### ↳ ↳ Re: Kobol

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2002-12-28T21:03:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0212282103.7663b515@posting.google.com>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de> <92qP9.3132$FF4.190414@newsb.telia.net>`

```
"Fim W stberg" <fim.wastberg@fimator.se> wrote in message news:<92qP9.3132$FF4.190414@newsb.telia.net>...
> "vaclav snajdr" <vsn@snajdr.de> skrev i meddelandet
> news:3E0DD3ED.4EE1BF64@snajdr.de...
…[10 more quoted lines elided]…
> Fim Wï¿½stberg

Kobol translates COBOL to C, then uses gcc to compile the C. Setting
things up from the command line is not that bad if you are familiar
with gcc. Also the IDE echoes its command lines into an output window.

Here's the outline of what works under Windows (95) to compile a
single source file:

1. install cygwin to c:\cygwin
2. add c:\cygwin\bin to the path
3. copy these files to the working directory from Kobol

cob2c.exe
cobol2gcc.h
libcompsuppwin32.a
cygwin1.dll

4. add the source file + batch files
5. translate the source text to line-feed delimited text
6. set the "prog" environment variable to the program base name, e.g.
foo
7. execute c1.bat, c2.bat and l.bat

c1.bat:
cob2c -M %prog%.cbl

c2.bat:
g++ -c -Ic:/cygwin/usr/include -Ic:/cygwin/usr/include/g++-3
-o %prog%.o %prog%.cc

l.bat:
g++ -s -o %prog% %prog%.o -L. -lcompsuppwin32 -Lc:/cygwin/lib
-Lc:/cygwin/lib/w32api

Note: c2.bat and l.bat contain a single line of text each

the switches do the following

M = set MAIN file
c = compile only
I = include directory
o = output file
s = strip debug info from exe
L = link to libraries in
l = link to library

c1: foo.cbl -> foo.cc + *.h
c2: foo.o   -> foo.o
l:  foo.o   -> foo.exe
```

#### ↳ Re: Kobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-29T07:24:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E0EA32C.AF0F5365@Azonic.co.nz>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de>`

```
vaclav snajdr wrote:
> 
> There is a product with this name from "www.thekompany.com",
…[4 more quoted lines elided]…
> Thanks.

It seems to work OK, but has no mechanism for locking records or for
using SQL, which means that it is strictly single user and thus only for
simpler tasks and learning.
```

#### ↳ Re: Kobol

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2002-12-30T00:19:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KH0x0LAmE5D+EwI1@ld50macca.demon.co.uk>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de>`

```
So somebody took my suggestion of changing the C in Cobol into a K, in
order to make it appear kool to the peeps, seriously. Do I have any
copyright on the name?

In article <3E0DD3ED.4EE1BF64@snajdr.de>, vaclav snajdr <vsn@snajdr.de>
writes
>There is a product with this name from "www.thekompany.com",
>an IDE and Cobol compiler what ranslate cobol code
…[3 more quoted lines elided]…
>Thanks.
```

##### ↳ ↳ Re: Kobol

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-30T13:17:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0IXP9.4211$qU5.3178656@newssrv26.news.prodigy.com>`
- **References:** `<3E0DD3ED.4EE1BF64@snajdr.de> <KH0x0LAmE5D+EwI1@ld50macca.demon.co.uk>`

```
"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:KH0x0LAmE5D+EwI1@ld50macca.demon.co.uk...
> So somebody took my suggestion of changing the C in Cobol into a K, in
> order to make it appear kool to the peeps, seriously. Do I have any
> copyright on the name?

No, because a brand name is not copyrightable.

You might have a claim on a trademark IF... your first public use of the
term identified KOBOL as a trademark AND you used "KOBOL(tm)" as an
adjective.

If used as a noun, it might qualify as a service mark, if you had offered it
as a service under that brand name.

But I don't believe any of these conditions exist, so instead of "C," "TM"
or "SM" the only acronym or abbreviation which applies is "SOL."

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
