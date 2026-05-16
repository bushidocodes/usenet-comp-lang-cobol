[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Meaning of "Duplicate public name"

_4 messages · 3 participants · 2000-08_

---

### Meaning of "Duplicate public name"

- **From:** rezeerf@my-deja.com
- **Date:** 2000-08-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ntra0$7aq$1@nnrp1.deja.com>`

```
Hi,

hope someone can answer me this:

I'm using NetExpress 3.1 and on doing my release-build i get the
following error messages:

Rebuilding         RELEASE\Rt.exe

ERROR: (5) Duplicate public name :  RELEASE\RTAUSK99.OBJ(_RTAUSK45)
ERROR: (5) Duplicate public name :  RELEASE\RTKONTR.OBJ(_RTKONTR)
ERROR: (5) Duplicate public name :  RELEASE\RTMENVER.OBJ(_RTMENBAU)
ERROR: (5) Duplicate public name :  RELEASE\rtsegta4.OBJ(_RTSEGTAB)
ERROR: (5) Duplicate public name :  RELEASE\RTSEGTAB.OBJ(_RTSEGTAB)
ERROR: (5) Duplicate public name :  RELEASE\RTUNBAR7.OBJ(_RTUNBAR3)
ERROR: (5) Duplicate public name :  RELEASE\RTUNBAR8.OBJ(_RTUNBAR2)
ERROR: (5) Duplicate public name :  RELEASE\RTUNBAR9.OBJ(_RTUNBAR2)

All the buildings of the given files in the project are whithout errors,
only during release-build i get the ones above.
I've looke in the online reference at the error-messages and thought i
could be caused by duplicate filenames or write-protection - but,
nothing like that.

Thank you in advance for any suggestions,

alex


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Meaning of "Duplicate public name"

- **From:** Danial Clarke <danial.clarke@merant.com>
- **Date:** 2000-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39A3A63D.98A736CD@merant.com>`
- **References:** `<8ntra0$7aq$1@nnrp1.deja.com>`

```
The easy one is the last error - you appear to have the entry point
'RTUNBAR2' defined in more than one file.

When you compile a module to as a .OBJ it will have public symbols for all
the entry-points. You'll always get an entry-point with the same name as the
file, plus you'll get one with the name defined in the PROGRAM-ID clause,
and then one for each 'ENTRY "..."' statement. For example if I have a file
called 'FRED.CBL' as follows:

    IDENTIFICATION DIVISION.
    PROGRAM-ID. JIM.

    PROCEDURE DIVISION.
    ENTRY "HARRY".
    STOP RUN.

If I compile this to .OBJ the module will have three entry-points; 'FRED',
'JIM' and 'HARRY'. (You can see the public symbols if you specify the -V
option to CBLLINK).

Since your filenames are all different you need to check the PROGRAM-ID
clauses, and any 'ENTRY' statements.

Hope this helps,


Dan.

rezeerf@my-deja.com wrote:

> Hi,
>
…[27 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Meaning of "Duplicate public name"

- **From:** rezeerf@my-deja.com
- **Date:** 2000-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8o5hoi$5fu$1@nnrp1.deja.com>`
- **References:** `<8ntra0$7aq$1@nnrp1.deja.com> <39A3A63D.98A736CD@merant.com>`

```
In article <39A3A63D.98A736CD@merant.com>,
  Danial Clarke <danial.clarke@merant.com> wrote:

<snip>
> Since your filenames are all different you need to check the
PROGRAM-ID
> clauses, and any 'ENTRY' statements.
>
> Hope this helps,
>
> Dan.

Thanx, that was exactly what caused the errors !

alex


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Meaning of "Duplicate public name"

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-23T02:34:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39A33801.A800F448@home.com>`
- **References:** `<8ntra0$7aq$1@nnrp1.deja.com>`

```


rezeerf@my-deja.com wrote:
> 
> Hi,
…[8 more quoted lines elided]…
> ERROR: (5) Duplicate public name :  RELEASE\RTAUSK99.OBJ(_RTAUSK45)

I can't guarantee that this is the same - but I had a similar problem
back in May when rebuilding a cut-down version of my application to an
executable, (using Version 3.0).

You can delete, (Remove from Project), from the IDE both in the
'application tree' left-hand side, and from the alphabetical list of
source on the right-hand side. Although I deleted under DEBUG mode, when
I did a REBUILD ALL under RELEASE mode, I got a similar problem to
yours. Within RELEASE mode delete those source (objects) 'hanging loose'
in the tree and it worked.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
