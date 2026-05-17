[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Content of pointer.

_8 messages · 5 participants · 1998-03_

---

### Content of pointer.

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1998-03-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<350FCED7.2D1CAB90@yahoo.com>`

```
Hi.

I need to retrieve the content of an address pointed to by a pointer.

How do I do this ??

Is there something called
"move content of pointer to var" or
"move value of pointer to var" ??

I use NetExpress 2.0 from MicroFocus.

Tommy Nilsen
tom··.@ya··o.com
```

#### ↳ Re: Content of pointer.

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p2@usenetarchives.gap>`
- **In-Reply-To:** `<350FCED7.2D1CAB90@yahoo.com>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com>`

```



tommy nilsen wrote in message <350··.@ya··o.com>...
› Hi.
› 
…[12 more quoted lines elided]…
› 


Why exactly do you need to "retrieve" it (what are you doing with it)? If
you just want to store the address in another USAGE POINTER data item, then
just use

Set new-pointer to original-pointer

Chance are that anything else that you might really want to do with your
pointer can be done with the SET verb. The only thing you are going to have
trouble with is if what you want to do is display the actual "physical"
address somehow. This will require that you understand exactly how your
computer stores pointers (for example a 16-bit Intel pointer has no
relationship to an IBM mainframe pointer). Then you will need to do a
REDEFINES and play around with what you get.
```

#### ↳ Re: Content of pointer.

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-17T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p3@usenetarchives.gap>`
- **In-Reply-To:** `<350FCED7.2D1CAB90@yahoo.com>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com>`

```

tommy nilsen wrote:
› 
› Hi.
…[7 more quoted lines elided]…
› "move value of pointer to var" ??

01 my-fld.
05 my-fld-9 pic s9(8) comp.
05 my-fld-ptr pointer.

refer to my-fld-9 when you wish to get the actual address in the
pointer...
```

##### ↳ ↳ Re: Content of pointer.

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-17T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e4fc9ecd86-p3@usenetarchives.gap>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com> <gap-e4fc9ecd86-p3@usenetarchives.gap>`

```



Joe Zitzelberger wrote in message <351··.@not··s.com>...
› tommy nilsen wrote:
›› 
…[15 more quoted lines elided]…
› pointer...

Today seems to be POINTER and portability day.

Please ONLY use the method listed above if you are running on an IBM
Mainframe system or another system that HAPPENS to store its pointers this
way. Try this on an Intel 16-bit system (for example) and the garbage you
will get will make the "mind boggle".
```

###### ↳ ↳ ↳ Re: Content of pointer.

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e4fc9ecd86-p4@usenetarchives.gap>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com> <gap-e4fc9ecd86-p3@usenetarchives.gap> <gap-e4fc9ecd86-p4@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Joe Zitzelberger wrote in message <351··.@not··s.com>...
…[16 more quoted lines elided]…
› will get will make the "mind boggle".

I wouldn't say garbage, you just have to adjust for the strange byte
order on intel machines and size of the pointers. Also the segmentation
model on 16-bit Intels would mess you up some...but you could do

01 my-fld
03 near.
05 my-fld-near-9 pic s9(4) comp.
05 my-fld-near-ptr pointer redefines my-fld-near-9.
05 pic xx.
03 far redefines near.
05 my-fld-far-9 pic s9(8) comp.
05 my-fld-far-ptr pointer redefines my-fld-far-9.
03 strange-byte-order redefines far.
05 low-low-byte pic x.
05 low-high-byte pic x.
05 high-low-byte pic x.
05 high-high-byte pic x.

Of course, you could go with the flat model, in which case it will work
as previously advertised.....

But how exactly does one make a pointer 'Portable' accross different
memory models???
```

###### ↳ ↳ ↳ Re: Content of pointer.

_(reply depth: 4)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e4fc9ecd86-p5@usenetarchives.gap>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com> <gap-e4fc9ecd86-p3@usenetarchives.gap> <gap-e4fc9ecd86-p4@usenetarchives.gap> <gap-e4fc9ecd86-p5@usenetarchives.gap>`

```


Joe Zitzelberger wrote in message <351··.@not··s.com>...
› William M. Klein wrote:
›› 
›› Joe Zitzelberger wrote in message <351··.@not··s.com>...
 
 
›   >much snippage<
› But how exactly does one make a pointer 'Portable' accross different
› memory models???

Fairly easily (and even easier once the draft Standard takes affect). To
make things "portable", simply define the item as USAGE POINTER and always
use the SET verb to use and modify its values. If you never try and
REDEFINE it and play with its internals, your code should be quite portable
across platforms and compilers.
```

#### ↳ Re: Content of pointer.

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p7@usenetarchives.gap>`
- **In-Reply-To:** `<350FCED7.2D1CAB90@yahoo.com>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com>`

```

tommy nilsen wrote:
›
› Hi.
…[4 more quoted lines elided]…
›

Easy...

On Intel (your) platform

01 MyPointer POINTER.
01 MyPtrValue REDEFINES MyPointer
PIC 9(8) COMP-5.

On IBM platform

01 MyPointer POINTER.
01 MyPtrValue REDEFINES MyPointer
PIC 9(8) COMP.

Then you can add/subtract to/from MyPtrValue, and try whatever to make
your program crash... :-)


****
/Geir
```

##### ↳ ↳ Re: Content of pointer.

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4fc9ecd86-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e4fc9ecd86-p7@usenetarchives.gap>`
- **References:** `<350FCED7.2D1CAB90@yahoo.com> <gap-e4fc9ecd86-p7@usenetarchives.gap>`

```

[Answers are correct for Micro Focus COBOL. I don't know offhand which
of the things I have used are extentions.]

Geir Knaplund wrote:
›
› tommy nilsen wrote:
…[3 more quoted lines elided]…
›› I need to retrieve the content of an address pointed to by a pointer.

This isn't too clear to me. Do you mean you have a POINTER to some
DATA or a POINTER to a POINTER (an address) to some DATA ?
Anyway, the solution is basically the same.

Assume the following data definitions:

WORKING-STORAGE SECTION.
01 MyPointer USAGE POINTER. *> Assume this contains your "base" pointer.
LINKAGE SECTION.
01 MyPointer2 USAGE POINTER.
01 MyData PIC X.

In the first case (a pointer to some data), to get at the data:

SET ADDRESS OF MyData TO MyPointer
DISPLAY MyData

In the second case (a pointer to a pointer to some data):

SET ADDRESS OF MyPointer2 TO MyPointer
SET ADDRESS OF MyData TO MyPointer2
DISPLAY MyData

Of course, in either case, MyData could be a whole record structure
(possibly containing other embedded pointers which you can "follow"
using the same technique).

›› How do I do this ??
›› 
…[13 more quoted lines elided]…
›                         PIC 9(8) COMP.

This lets him discover the ADDRESS that the pointer holds, but not
get at the data that the pointer points to.

› Then you can add/subtract to/from MyPtrValue, and try whatever to make
› your program crash... :-)

You can do that with the pointer directly using "SET ptr [UP/DOWN]"
syntax. No need to redefine it with COMP-5 items (which is a bit
dodgy when you start to consider 64-bit pointers).
If you know your pointer points into an array, for instance, you can
write "SET ptr UP BY LENGTH OF array-record" to point it at the next
element in the array (assuming "array-record" is defined carefully to
be the correct size including padding bytes if the array has
oringinated from another language).

BTW:
COMP-5 is defined to mean "Native order", not "Reverse (Intel) order".
Therefore, you do not need to change the source from COMP-5 to COMP
when switching CPU's.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
