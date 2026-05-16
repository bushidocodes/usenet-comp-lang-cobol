[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetCOBOL "Release Candidate" available

_5 messages · 3 participants · 2002-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### NetCOBOL "Release Candidate" available

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-20T16:56:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a519to$np3$1@slb3.atl.mindspring.net>`

```
Good news & Bad News

 >>> Good News

The Fujitsu "Release Candidate" of their "NetCOBOL for .NET" product is now
available.

To get (download) the "release candidate" and to get more information about
this product, go to:

  http://www.adtools.com/dotnet/index.html

>>> Medium News

This product *requires* that you have the final (NOW released) version of
Visual Studio.  This is available from a variety of places (Microsoft can
direct you to retailers from their web site).  HOWEVER, this is NOT cheap
!!!

OTOH, they (Microsoft) do plan on providing a 60-day trial version (for
shipping costs).  The Fujitsu site has a "pointer" to this site (where you
can "reserve" a copy now).

>>> Bad News  (in MY personal opinion)

Do read the "NetCOBOL for .NET Limitations" section of their "Fujitsu
NetCOBOL for .NET" document.  To give you an idea of why it "scares" me,
here is what I see in that section,

"The following are limitations in this version of Fujitsu COBOL for .NET

 - Print files (ASSIGN TO PRINTER) are not supported. If you want to use
print files we recommend that you compile your print programs using Fujitsu
COBOL V6 and call this unmanaged code from your NetCOBOL for .NET managed
code. See Interacting with Other Languages .

 - The SCREEN SECTION is not supported. Your NetCOBOL for .NET applications
should use WinForms or WebForms for interfacing with your users.

 - SORT/MERGE is not supported. As with print files compile your SORT/MERGE
programs with the Windows COBOL compiler (e.g. Fujitsu COBOL V6) and call
the unmanaged code from your NetCOBOL for .NET managed code. See Interacting
with Other Languages.

 - The COBOL REPORT WRITER module is not supported.

 - Nested programs are not supported.

 - Pointer data items (USAGE POINTER) are not supported.

 - TYPEDEF STRONG is not supported.

 - ENTRY statements are not supported. Code that relies on ENTRY points
should be restructured so that each separate ENTRY point becomes a method.

 - ALTER statements are not supported. ALTER was declared obsolete in the
1985 COBOL standard.

 - A GO TO statement without a procedure name (used as the target of an
ALTER statement) is not supported.

 - The "STOP literal" statement, which would display a message to an
operator and pause execution pending a response, is not supported.

 - Exception handling in .NET has some differences to standard OO COBOL
exception handling. .Net exceptions continue to be propagated up the call
chain until a matching exception handler is found. In standard OO COBOL the
handler needs to be defined in the source unit in which the exception is
raised.

 - NetCOBOL for .NET only supports the COBOL file system. It does not
support other file systems such as the external file system, or Btrieve.

 - You cannot build assemblies within the Visual Studio .NET IDE. This is a
VS .NET limitation not a COBOL limitation."
```

#### ↳ Re: NetCOBOL "Release Candidate" available

- **From:** "Lee Unterreiner" <flu@nospam.flu-ent.com>
- **Date:** 2002-02-20T17:01:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a51gus$60k$1@slb6.atl.mindspring.net>`
- **References:** `<a519to$np3$1@slb3.atl.mindspring.net>`

```
A couple of comments on Bill's comments:

According to Fujitsu ...

- Outputting directly to a printer (and Report Writer?) will be supported
'as soon as possible'.

- Other file systems are still supported via the traditional CALL interface

- Embedded SQL is supported as is the new ADO+

Lee
```

#### ↳ Re: NetCOBOL "Release Candidate" available

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-02-21T19:10:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C75461A.4F41E52E@Azonic.co.nz>`
- **References:** `<a519to$np3$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Do read the "NetCOBOL for .NET Limitations" section of their "Fujitsu
…[3 more quoted lines elided]…
> "The following are limitations in this version of Fujitsu COBOL for .NET

It has been pointed out elsewhere that the .NET CLR is 'multi-language'
only as far as the other languages work like C#.  Many of the languages
supported by the CLR have been mangled so that they are 'C# with another
syntax'.
```

##### ↳ ↳ Re: NetCOBOL "Release Candidate" available

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-02-21T07:03:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a52r7g$elc$1@slb7.atl.mindspring.net>`
- **References:** `<a519to$np3$1@slb3.atl.mindspring.net> <3C75461A.4F41E52E@Azonic.co.nz>`

```
Richard,
  It is my understanding (and I could prove to be wrong) that despite what I
(personally) see as SERIOUS deficiencies in this "release candidate" - that
Fujitsu *does* intend to provide a "full feature" NetCOBOL "relatively
soon".

I used to think that they intended to provide a full ANSI'85 high-level
compiler - but from reading what they say about a number of the REQUIRED
features from the '85 Standard (that are marked as OBSOLETE), my "best
guess" is that they are aiming at a compiler that will include all (most?)
of the draft (expected to be final at the end of this year) 200x Standard.

Again, with my limited understanding, the CLR does place "constraints" on
the "object code" that a compiler produces, but I know of none that it
"really" places on syntax/semantics.

On the other hand, (again with my limited knowledge) I can imagine that
ENTRY statements and nested programs (for example) might well be a
"challenge" to implement.  Similarly, there are some DEFINITE requirements
in .NET for "memory protection" so USAGE POINTER may be "easier said than
done" - but I would expect to see it in a "relatively" early release of
NetCOBOL.
```

##### ↳ ↳ Re: NetCOBOL "Release Candidate" available

- **From:** "Lee Unterreiner" <flu@nospam.flu-ent.com>
- **Date:** 2002-02-21T15:22:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a53vif$ps1$1@slb2.atl.mindspring.net>`
- **References:** `<a519to$np3$1@slb3.atl.mindspring.net> <3C75461A.4F41E52E@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote  :
>
> It has been pointed out elsewhere that the .NET CLR is 'multi-language'
> only as far as the other languages work like C#.  Many of the languages
> supported by the CLR have been mangled so that they are 'C# with another
> syntax'.

Richard,

If you aren't using an OO language .NET does not have much to offer.

Betrand Meyer says in his video course that C# is a syntatical
representation of the CLR semantics.  Sort of a high-level assembler for the
CLR.  But its only one such.  So is OO COBOL or Eiffel with minor additions,
VB with some big changes, C++ with some subtractions.

To degree one's favorite language supports OO (mine is REAL close).  Right
now Fujitsu is the only option for COBOL.  If  .NET is going to be as big as
Bill says (and he would know) then we need the other vendors to give us some
choices.

Lee
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
