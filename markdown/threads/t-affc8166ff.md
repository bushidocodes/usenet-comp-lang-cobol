[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO-Cobol compiler directive problem

_2 messages · 1 participant · 2000-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Object-oriented COBOL`](../topics.md#oo)

---

### OO-Cobol compiler directive problem

- **From:** Herwig Huener <Herwig.Huener@mch6.siemens.de>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol,ger.ct
- **Message-ID:** `<396F2F63.2BDE1DAE@mch6.siemens.de>`

```
2000-07-14 17:15:00 MEST

Hi,

At this time, I am implementing a small
part of the new OO-Cobol, namely the
compiler-directing facility. (This is
paid work and no hobby.)

Consider this:

       >> define oops as 17
       >> define oops as parameter override
       ...

The *intent* of these lines is to have a
compiler-variable oops with the value
17, unless another value is provided from
the operating system environment.
To my mind, these lines should be equivalent
to:

       >> define oops as parameter
       >> if oops is not defined
       >> define oops as 17
       >> end-if
       ...

Unfortunately, the CD 1.8 states:

   7.2.9.3 General rules
   ...
   5) If the PARAMETER phrase is specified, the
   value referenced by compilation-variable-name-1
   is obtained from the operating environment by
   an implementor-defined method. If no value is
   made available from the operating environment,
   compilation-variable-name-1 is not defined.
   ...

I interpret that if the "parameter" or
"parameter override" phrase is given and the
operating environment does not provide a value,
an already existing compiler-variable shall
disappear.

In that case, a default-value mechanism cannot
implemented as shown in the first example above.

Is this really the intent of the standard? I
would prefer that the effect of

       >> define oops as parameter

or

       >> define oops as parameter override

in the absence of an externally provided value
should leave any possibly already existing
compiler-variable oops untouched and
unchanged. The wording of the Standard should
be:

                              ... If no value is
   made available from the operating environment,
   the define ... parameter directive shall have
   no effect.
   ...

Any comments?
```

#### ↳ Re: OO-Cobol compiler directive problem

- **From:** Herwig Huener <Herwig.Huener@mch6.siemens.de>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol,ger.ct
- **Message-ID:** `<3972C8CE.E7204AF1@mch6.siemens.de>`
- **References:** `<396F2F63.2BDE1DAE@mch6.siemens.de>`

```
2000-07-17 10:47:59 MESZ

Herwig Huener wrote:
>
> ...
>

Thanks for the many responses which I found
in my Inbox today. I think I will implement
the issue as "... shall disappear" because
of the convincing argument that there are
two ways of expressing the same intent.

However, one ist always prepared for changes
when implementing a not yet completely
defined language. We had the same problem
when we made an Ada-83 compiler - eons
ago.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
