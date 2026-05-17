[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Standardization; Factories

_2 messages · 1 participant · 1998-04_

---

### Standardization; Factories

- **From:** "ralf laemmel" <ua-author-13874780@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<353E2841.799B@informatik.uni-rostock.de>`

```

Hi all,

Another question concerning a design decision
in the committee draft (COBOL standard).

When a class program is loaded, the factory object
is automatically created. Does a programmer have
a way to code statements which are executed when the
class program is loaded? Such statements would do
some initialization of the factory object.

As far as I can see in the standard, the answer is "NO".
I want to state that there should be support.

I think it is not possible in Standard COBOL,
because there is no anonymous procedure division.
There are only the factory methods. In contrast,
by the way, some variants of MF COBOL support a separate
PROCEDURE DIVISION doing the thing I am interested in.

Why do I think it is necessary?
Well, I always can do some initialization of the
factory object by a special factory method.

Of course, such an approach puts burden on the programmer who
must be aware of the fact that the factory needs to
be initialized. Moreover, such an explicit initialization
is not orthogonal to the way instance objects are created
and initialized. Here, I can override NEW, but I can't do that
for factories.

Note, to make sense a separate data division is
needed as well or the factory data must be
visible at least.

I hope I didn't overlook anything.
I appreciate any comment.
Ralf

+=======================================================================+
| Ralf Laemmel
|
…[15 more quoted lines elided]…
|
+-----------------------------------------------------------------------+
| M. Marcotty: "... the metalanguage of a formal definition must not
|
| become a language known to only the priests of the cult ..."
|
+-----------------------------------------------------------------------+
| Don't miss the Language Development Laboratory Home Page at
|
| http://www.informatik.uni-rostock.de/FB/Praktik/psuet/ldl/
|
+=======================================================================+
```

#### ↳ Re: Standardization; Factories

- **From:** "ralf laemmel" <ua-author-13874780@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e171bc36cd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<353E2841.799B@informatik.uni-rostock.de>`
- **References:** `<353E2841.799B@informatik.uni-rostock.de>`

```

› I hope I didn't overlook anything.
› I appreciate any comment.
› Ralf

Maybe, I should mention another trick myself.
I can use a factory data item initialized by
a VALUE clause to model the fact if initialization
was performed or not. Every class method invocation
must then check this data item and possibly force
the initialization.

That is a real trick.
Still, I miss orthogonality.
Moreover, the operational semantics
of such a delayed initialization is
quite different to the initialization
at class loading time.

Consequently, it seems quite convenient
to me to add a method to the Base class
which is responsible for initialization,
say a method which is called by default
at class loading time. This factory method
would be similar in intent to NEW (at the
object instance level).

Bye,
Ralf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
