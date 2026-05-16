[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL to Java Conversion

_5 messages · 5 participants · 2003-09_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### COBOL to Java Conversion

- **From:** "RGonzalez" <rgonzalez@f3rsolutions.com.removethis>
- **Date:** 2003-09-26T04:23:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>`

```
Hello,

Is there any businesses that perform COBOL to Java conversions?
Does anyone know what their going rates are (more or less)?


Thanks
__________________________
R.Gonzalez
F3RSolutions.com
```

#### ↳ Re: COBOL to Java Conversion

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-09-26T12:24:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XdWcb.82413$Lnr1.22975@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>`

```
Corporola Inc. performs COBOL to Java conversions.
The rate is flexible based on size of code or fearutes needed.
Check out http://www.corporola.com

Thomas Li
Corporola Inc.


"RGonzalez" <rgonzalez@f3rsolutions.com.removethis> wrote in message
news:ybPcb.30593$Ci5.680950@twister.tampabay.rr.com...
> Hello,
>
…[9 more quoted lines elided]…
>
```

#### ↳ Re: COBOL to Java Conversion

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-26T13:33:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309261233.725e5777@posting.google.com>`
- **References:** `<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>`

```
"RGonzalez" <rgonzalez@f3rsolutions.com.removethis> wrote

> Is there any businesses that perform COBOL to Java conversions?
> Does anyone know what their going rates are (more or less)?

You say 'conversion' rather than 'reimplementation'.  Any code that is
converted is likely to retain much of the structure and style of the
original.  The programs won't be 'Java programs', but will be 'Cobol
programs in the syntax of Java'.  In order to produce the same results
they will have to emulate Cobol's semantics.

From working with Fortran and Cobol programs converted to C I would
suggest that the results would need programmers who are fluent in both
Cobol (for the style and semantics) and Java (for the syntax).  If
such people were actually available then they could be employed much
more productively working on the Cobol code.

There are, however, Cobol to Java translators which will produce Java
executables from Cobol source code.  If, for example, you want to
write Cobol to run in a Java VM in WebSphere then this may be viable -
just don't even look at the java code.
```

#### ↳ Re: COBOL to Java Conversion

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2003-09-27T02:56:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L%6db.10909$oa4.6910@twister.nyroc.rr.com>`
- **References:** `<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>`

```
Check on Relativity (www.relativity.com). I doubt their services come cheap
but they utilize a tool that assists in reengineering COBOL to java rather
than doing a rote translation of it.

"RGonzalez" <rgonzalez@f3rsolutions.com.removethis> wrote in message
news:ybPcb.30593$Ci5.680950@twister.tampabay.rr.com...
> Hello,
>
…[9 more quoted lines elided]…
>
```

#### ↳ Re: COBOL to Java Conversion

- **From:** bsulliv@legacyj.com (Brian Sullivan)
- **Date:** 2003-09-28T21:51:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8041505.0309282051.6cbe7d4a@posting.google.com>`
- **References:** `<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>`

```
"RGonzalez" <rgonzalez@f3rsolutions.com.removethis> wrote in message news:<ybPcb.30593$Ci5.680950@twister.tampabay.rr.com>...
> Hello,
> 
…[6 more quoted lines elided]…
> F3RSolutions.com

Hello,

Check out LegacyJ (http://www.legacyj.com) for PERCobol.

It's not COBOL to Java conversion, but rather compiling COBOL to work
in the Java environment with extremely simple integration between the
two.  We believe there's a number of accuracy, performance, and
maintainance tradeoffs in translation, so we encourage people to keep
the code in COBOL source for maintainance so we can have accuracy and
continue to upgrade our compiler/runtime's performance over time.

There's a download available for evaluation.  The IDE is Eclipse,
allowing both COBOL and Java development.  If wanting to do new work
in Java, check out the Cobol calling Java and Java calling Cobol
samples in particular.  With our LTP product, even CICS API code is
now supported directly as EJBs.

Every Cobol program is an object, so calling:

PROGRAM-ID. MYCOBOL.
DATA DIVISION.
LINKAGE SECTION.
01 A PIC X(10).
01 B PIC 9(3).
01 C PIC 9(5)V99 COMP-2.
PROCEDURE DIVISION USING A B C.

is as direct as:

mycobol instance=new mycobol();
instance.call(null,new Object[] {"Hello",new Integer(123),new
Double(456.78)});

(Note, multiple instances of the same Cobol program are permitted,
with each 'context' following standard COBOL-85 calling rules, so
technologies such as servlets and EJBs do work as expected.  Beware
any Java translation that makes data static, it's a dead-end.)

And calling from Cobol into Java is just as simple as implementing a
class with one method, call.  Each parameter implements a Datatype
interface with methods such as toInt, toText, toDouble, etc. for
direct usage of elementary types, and getElements() for breaking down
groups and tables.

Objects are supported directly from Cobol, so the following is valid
(using custom C"" class literals for brevity):

INVOKE C"java.lang.Thread" "sleep" USING BY VALUE 1000

(Or you could use one of the numerous extensions, such as DELAY 1.0
from Tandem syntax.)

Regards,
Brian Sullivan
LegacyJ Corp.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
