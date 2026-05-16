[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# free(string)

_3 messages · 1 participant · 2002-06 → 2002-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### free(string)

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2002-06-29T16:49:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afl6r4$cqq$1@nntp2-cm.news.eni.net>`

```
I am trying to determine the windows APi equivalent to the free(string) line
of code that follows...My app interfaces with a C program that is allocating
a string...I do not have the source code the module that allocates the
string...My cobol module is a callback for the main C module)...What I get
from the C module is an address...i set the address of a linkage section 01
level to that address and can reference the data just fine...BUT...

The string needs to be freed by my app, not the C Lang program that
allocates the string...They supply a sample app that simply does
free(string)...But I am unable to translate that into an windows API call...

                char *string;

                        free(string);

Please copy any response to this to my email account...My news reader does
not seem to like this group for some reason...it displays new messages every
now and then at best...
```

#### ↳ Re: free(string)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-30T10:59:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ewBT8.13202$ry2.11595@nwrddc02.gnilink.net>`
- **References:** `<afl6r4$cqq$1@nntp2-cm.news.eni.net>`

```
free is the complement to malloc; and the particular method used by malloc
is compiler-dependent.

malloc returns a pointer to a block of memory; the compiler may do this with
either one of (at least) two methods:

GlobalAlloc (GMEM_FIXED||(any other atributes), size) , which is
complelmented by calling GlobalFree
or
GlobalLock(GlobalAlloc(any attributes other than GMEM_FIXED), size)), which
is complemented by GlobalUnlock followed by GlobalFree. In this case, you
need to get the global handle from the pointer using GlobalHandle

MSDN says GlobalUnlock has no effect on memory allocated with the GMEM_FIXED
attribute; so it would appear you would be safe to always use the second
method, even if  GlobalUnlock  has no effect.

The more 'modern' (and according to MSDN, now recommended method) Windows
method of allocating memory and obtaining a pointer is HeapAlloc;  if your
compiler users this API, you free the memory with HeapFree.

If you can read the C program's import table you may be able to figure out
exactly which method the C program uses; but if ambuguity remains, you might
just end up writing test code to figure out how the C program is obtaining
that pointer it passes to your program.

If GlobalFree (pointer value) returns non-zero, then it has returned a
handle to the object, and you have to repeat the operation.

Easier way to know: specify which C compiler and version you are using, and
ask this same question in a 'c' newsgroup. Chances are someone there will
know how the particular compiler works.

I do not edit email addresses and I believe
"**Ken**Mullins**@**mindspring.com** remove **'s" is not your real email
address, so this is posted to the newsgroup only.

MCM



Ken Mullins <**Ken**Mullins**@**mindspring.com** remove **'s> wrote in
message news:afl6r4$cqq$1@nntp2-cm.news.eni.net...
> I am trying to determine the windows APi equivalent to the free(string)
line
> of code that follows...My app interfaces with a C program that is
allocating
> a string...I do not have the source code the module that allocates the
> string...My cobol module is a callback for the main C module)...What I get
> from the C module is an address...i set the address of a linkage section
01
> level to that address and can reference the data just fine...BUT...
>
> The string needs to be freed by my app, not the C Lang program that
> allocates the string...They supply a sample app that simply does
> free(string)...But I am unable to translate that into an windows API
call...
>
>                 char *string;
>
>                         free(string);
>
```

##### ↳ ↳ Re: free(string)

- **From:** "Ken Mullins" <kenmullins**REMOVE**@mindspring.com>
- **Date:** 2002-07-01T09:03:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afpjuq$a0l$1@slb0.atl.mindspring.net>`
- **References:** `<afl6r4$cqq$1@nntp2-cm.news.eni.net> <ewBT8.13202$ry2.11595@nwrddc02.gnilink.net>`

```
I went the GlobalHandle, GlobalUnlock, and GlobalFree route...Seems to work
ok...Return code from GlobalFree is 0, which is suppose to indicate
success...

The assistance is much appreciated...

kenmullins
newnan, ga USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
