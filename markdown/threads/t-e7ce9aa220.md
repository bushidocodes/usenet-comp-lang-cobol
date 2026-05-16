[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL NT gnt/int

_4 messages · 4 participants · 1998-11 → 1998-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL NT gnt/int

- **From:** formula_ffo@my-dejanews.com
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73uc1n$971$1@nnrp1.dejanews.com>`

```
I have a problem running .gnt files on NT 4.0, but I don't experience the same
problem when I use intermediate code file (.INT)files.

Does anybody know why programs run as .int files and not as .gnt files?

I use Micro Focus Workbench v4.0.07

Frank

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: MF COBOL NT gnt/int

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662C81E.EE116827@bdssoftware.com>`
- **References:** `<73uc1n$971$1@nnrp1.dejanews.com>`

```
.gnt files are more or less native code and run much quicker than .int
code which is interpreted.  Other than that, sorry but I'm not currently
using NT with MF COBOL and can't help you any more.

formula_ffo@my-dejanews.com wrote:
> 
> I have a problem running .gnt files on NT 4.0, but I don't experience the same
…[9 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: MF COBOL NT gnt/int

- **From:** "Stephen Thomas" <thomass@logica.com>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be1d4f$d2836180$0b47ea9e@GDLPPC04.logica.co.uk>`
- **References:** `<73uc1n$971$1@nnrp1.dejanews.com>`

```
You don't say the nature of the problem you are running into.  Any specific
error messages?

But one thought that occurs to me ...

Were they compiled on NT with the 32bit Workbench you are now using, or
were they compiled with the 16bit compiler?   INTs produced by the 16bit
compiler would continue to run under the 32bit runtime but the GNTs would
not.  This is because GNTs are native code, geared to the platform - or at
least the chipset - on which they were compiled.  INTs are, up to a point,
platform independent.  So an INT compiled under DOS would run under, say,
Solaris.  Assuming that the program does not request any DOS specific
services, of course :)
```

#### ↳ Re: MF COBOL NT gnt/int

- **From:** g1dlc@Radix.Net (David L. Craig)
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<743n47$935$1@saltmine.radix.net>`
- **References:** `<73uc1n$971$1@nnrp1.dejanews.com>`

```
In article <73uc1n$971$1@nnrp1.dejanews.com>,
 <formula_ffo@my-dejanews.com> wrote:
>I have a problem running .gnt files on NT 4.0, but I don't experience the same
>problem when I use intermediate code file (.INT)files.
…[3 more quoted lines elided]…
>I use Micro Focus Workbench v4.0.07

If it runs as an int but breaks as a gnt then you almost
always have an NGC (Native Code Generator) bug.  Often only
one processor type's NGC has the problem.  Micro Focus
insists you isolate the problem and build a small demo
program before they accept the bug report.  I have spent
days doing this kind of thing, inserting DISPLAYs until I
find the point where the gnt goes south.  Occasionally
inserting the DISPLAY makes the problem go away, or subtly
modifying the statement that is failing.  I think code
optimizations and odd instruction pipelining / register
changing interactions are responsible.  It must be tough
being an NGC maintainer.

Get the latest version of the NGC before you start
this process.  Maybe the bug is fixed already.  If not,
Micro Focus will be more interested in assisting you
with your problem.

You probably can't wait for them to get around to fixing
your bug, so work with the failing statement until the
problem stops occuring.  Breaking up COMPUTE statements is
often efficacious, as are insertions of unnecessary MOVE
statements or changing USAGE clauses of involved
variables.  Find something that works and then put a
comment in the code explaining why it's there.

Good luck.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
