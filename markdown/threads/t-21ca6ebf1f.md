[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL & Powerbuilder - 32bit

_2 messages · 2 participants · 1997-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL & Powerbuilder - 32bit

- **From:** "mhe..." <ua-author-17073513@usenetarchives.gap>
- **Date:** 1997-12-08T09:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<881591871.31299@dejanews.com>`

```

I'm trying to get 32bit Powerbuilder on NT to call a 32bit MF COBOL DLL
function.

I get an error message: Error Number 42 (Invalid stack pointer on return
from function call).

I've tried all different calling conventions including pascal. I've
created a very small function for testing that simply has one integer as
the argument and have varied the argument types on the Powerbuilder side
from int to long to make sure that I'm not mixing up argument size.

I can call this same COBOL DLL function successfully from another 4GL I
have (ESL NT).

My question is: Has anybody ever done this before?

I'm thinking about a C++ wrapper at this point, but would prefer not to
have to.

Thanks,
Mike Henry

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: MF COBOL & Powerbuilder - 32bit

- **From:** "jo..." <ua-author-17071890@usenetarchives.gap>
- **Date:** 1997-12-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-21ca6ebf1f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<881591871.31299@dejanews.com>`
- **References:** `<881591871.31299@dejanews.com>`

```

mhe··.@se··s.com wrote:

› I'm trying to get 32bit Powerbuilder on NT to call a 32bit MF COBOL DLL
› function.
 
› I get an error message: Error Number 42 (Invalid stack pointer on return
› from function call).
 
› I've tried all different calling conventions including pascal. I've
› created a very small function for testing that simply has one integer as
› the argument and have varied the argument types on the Powerbuilder side
› from int to long to make sure that I'm not mixing up argument size.

If it's not the calling convention possibly it's the way the argument
is passed. ie. 'by reference' or 'by value'

I've pasted a piece out of the Powerbuilder Help:

------start of quote-------------------------------------------------
In PowerBuilder, you can define external C functions that expect
arguments to be passed by reference or by value. When you pass an
argument by reference, the C function receives a pointer to the
argument and you can change the contents of the argument and return
the changed contents to PowerBuilder. When you pass the argument by
value, the C function receives a local copy of the argument and can
change the contents of the local copy. The changes affect only the
local copy, the contents of the original argument are unchanged. The
syntax for an argument that is passed by reference is:

ref datatype arg

Note PowerBuilder supports passing FAR pointers only. Therefore,
the pointer in the C function must have the FAR qualifier as shown in
the following examples.

---------------------end of quote ------------------------------------


John
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
