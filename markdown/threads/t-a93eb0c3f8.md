[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Semantics of ADD

_4 messages · 3 participants · 1997-12_

---

### Semantics of ADD

- **From:** "ell e tweedy" <ua-author-12405789@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<348dd236.0@news.cc.umr.edu>`

```


Hello all..

I am thinking about the ADD statment and multiple arguments to it.
Specifically,

ADD a b c TO x y z

The way I would read this is
x = x + a
y = y + b
z = z + c

However, after testing this with the Microfocus compiler we have here
at school, it reads as
x = a + b + c
y = a + b + c
z = a + b + c

which is behaviour I really wouldn't expect.

Does anyone know if this is a specific Microfocus behaviour, or is this
the standard? If it's standard, what do you think is the reasoning
behind it?

Additionally,
ADD a b c TO x y z GIVING p q r
which I don't believe is valid (?) would be a useful construct in my
opinion, for
p = a + x
q = b + y
r = c + z

Ideas, comments?

thanks..
laura
.. Laura Tweedy .. twe··.@u··.edu ..
```

#### ↳ Re: Semantics of ADD

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a93eb0c3f8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<348dd236.0@news.cc.umr.edu>`
- **References:** `<348dd236.0@news.cc.umr.edu>`

```

In article <348··.@new··r.edu>,
ell e tweedy wrote:
› 
›     ADD a b c TO x y z
…[12 more quoted lines elided]…
› which is behaviour I really wouldn't expect.

This is true only if x, y, and z all happen to be zero. The full
behaviour is
x = x + a + b + c
y = y + a + b + c
z = z + a + b + c


› Does anyone know if this is a specific Microfocus behaviour, or is this
› the standard?

This is the standard. The statement

ADD a b c TO x y z

is executed as follows, from left to right:

t = a + b
t = t + c
x = x + t
y = y + t
z = z + t


› If it's standard, what do you think is the reasoning behind it?

MOVE ZERO TO INVOICE-TOTAL.

ADD
INVOICE-LINE1-AMT
INVOICE-LINE2-AMT
...
INVOICE-LINEn-AMT
TO
INVOICE-TOTAL
BATCH-TOTAL
ACCOUNT-TOTAL
GRAND-TOTAL.


Christopher Westbury     You see things; and you say "Why?"
Midtown Associates       But I dream things that never
15 Fallon Place          were; and I say "Why not?"
Cambridge, MA 02138         --"Back To Methuselah" by George Bernard Shaw
```

#### ↳ Re: Semantics of ADD

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-12-09T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a93eb0c3f8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<348dd236.0@news.cc.umr.edu>`
- **References:** `<348dd236.0@news.cc.umr.edu>`

```

In article <348··.@new··r.edu>,
ell e tweedy wrote:
› 
› Additionally,
…[5 more quoted lines elided]…
›     r = c + z

If APL (or its descendant, J) is available at your school, by all means
try it. You will love it! In APL you can apply almost any operator to
almost any n-dimensional structure or slice of a structure. I believe
that APL is far superior to BASIC, Pascal, C, or what-have-you for the
first course in computing.

You are correct that the ADD statement you exhibited is not valid. There
is a conflict between the TO and the GIVING. The simplest form of the
ADD statement is
ADD a TO z

which is executed as
z = z + a

To recap briefly, the left generalization of the first form is
ADD a b c ... TO z

which is executed as
z = z + a + b + c + ...

and the right generalization of the first form is
ADD z TO a b c ...

which is executed as
a = a + z
b = b + z
c = c + z
...

The second form of the ADD statement is
ADD a TO b GIVING z

which is executed as
z = a + b

Notice that b is not modified in the second form even though there is a
TO. The GIVING transfers the modification from b to z. Therefore, TO
has been made optional in this form
ADD a b GIVING z

So, you can have
ADD a b c TO x y z

or you can have
ADD a b c x y z GIVING p q r

but in the second form there is no sensible interpretation when more than
one variable follows the optional TO, since it doesn't do anything
anyway.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: Semantics of ADD

- **From:** "joseph lenz" <ua-author-17071704@usenetarchives.gap>
- **Date:** 1997-12-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a93eb0c3f8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<348dd236.0@news.cc.umr.edu>`
- **References:** `<348dd236.0@news.cc.umr.edu>`

```



ell e tweedy wrote in article
<348··.@new··r.edu>...
› 
› Hello all..
…[37 more quoted lines elided]…
› 

If it makes the code more difficult to read, then don't use it. Make your
code clear and concise, and it will be easier to maintain.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
