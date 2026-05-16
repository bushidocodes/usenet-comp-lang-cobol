[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Redundant code sections.

_5 messages · 5 participants · 2003-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Redundant code sections.

- **From:** knuckles_doa@hotmail.com (We need more power captain)
- **Date:** 2003-10-08T02:01:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fc35a4e.0310080101.8f4e718@posting.google.com>`

```
Hi all,

does anyone know of a utility to search through source code  (Tandem
COBOL in this case) and locate all the redundant sections  (i.e
sections that have no corresponding PERFORM).  It would need to find
redundant sections if they're called from a redundant section also.

I could write a utility but lifes short enough already and I expect
someone has done a good one already.  

The aim of this is to make the code more readable and maintainable.

I have 1300 programs to do.

Thanks in advance.

Yaz
```

#### ↳ Re: Redundant code sections.

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-10-08T17:55:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031008135516.18927.00000391@mb-m15.aol.com>`
- **References:** `<8fc35a4e.0310080101.8f4e718@posting.google.com>`

```

knuckles_doa@hotmail.com  (We need more power captain)
Date: 10/8/03 4:01 AM EST
Message-id: <8fc35a4e.0310080101.8f4e718@posting.google.com>

asks...

<<
does anyone know of a utility to search through source code  (Tandem
COBOL in this case) and locate all the redundant sections  (i.e
sections that have no corresponding PERFORM).  It would need to find
redundant sections if they're called from a redundant section also.

>>


If all else fails you can usually use the compiler itself to do shallow
analysis.  Most compilers atleast list the line numbers where procedures are
referenced. A procedure with no references
_MAY_ be redundant. 

This approach is possibly dangerous as it 
does not account for perform thru ranges, nor
fallthrus.

You might want to reconsider your basic plan however.  Just an opinion. But the
portion of code, even in long term legacy systems that is
actually 'redundant' in the sense of having no internal references at all is
usually rather small.

Many segments of code become useless with time as the possibilities related to
that function
stop occuring as requirements change, ... but rarely do people go in and change
the code to stop executing. That is a notion relative to what I have seen, and
you may have a real different situation.

But honestly, in your 1300 programs how much is really obsolete? The danger of
hacking away at that code do not balance the likely gain of readability that
you indicate motivates you. Just an opinion, ;-).

Does your compiler list the line numbers of code or data where it is
referenced? Do you feel that is reliable enough in the cases where there is not
reference? Do you have enough examples
(with 1300 programs you should) to see that a compiler might not indicate
fallthrus or perform thrus in the cross reference? 

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Redundant code sections.

- **From:** "Ira Baxter" <idbaxter@semdesigns.com>
- **Date:** 2003-10-10T11:44:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f86dfc1$1@giga.realtime.net>`
- **References:** `<8fc35a4e.0310080101.8f4e718@posting.google.com>`

```
"We need more power captain" <knuckles_doa@hotmail.com> wrote in message
news:8fc35a4e.0310080101.8f4e718@posting.google.com...

> does anyone know of a utility to search through source code  (Tandem
> COBOL in this case) and locate all the redundant sections  (i.e
> sections that have no corresponding PERFORM).

"Redundant" usually means "unnecessary duplication".
(We have a tool that does this; see CloneDR at our website
if you have more interest).

From your description, I think you are interested in finding "dead" code,
that is, code that cannot ever be executed.  We have a tool
that does this (and rips it out, too) for Java, but not presently
for COBOL.

 >It would need to find
> redundant sections if they're called from a redundant section also.
>
> I could write a utility but lifes short enough already and I expect
> someone has done a good one already.

I would think that good cross reference would be the easy place
to start.   Any section that is defined but not referenced is a candidate
for removal.

> The aim of this is to make the code more readable and maintainable.
>
> I have 1300 programs to do.

This scale suggests that perhaps you really don't want to do this manually.
At 30 minutes cleanup editing per file, assuming you don't make
any mistakes, this is roughly 4 months of work.  And... you'll make
mistakes.

If you are serious about doing this, you probably want to use an
automated tool.
```

#### ↳ Re: Redundant code sections.

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-10-14T11:58:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmgkgq$a9g$1@hyperion.microfocus.com>`
- **References:** `<8fc35a4e.0310080101.8f4e718@posting.google.com>`

```
Try Revolve from Micro Focus.

http://www.microfocus.com/products/revolve/

"We need more power captain" <knuckles_doa@hotmail.com> wrote in message
news:8fc35a4e.0310080101.8f4e718@posting.google.com...
> Hi all,
>
…[15 more quoted lines elided]…
>
```

#### ↳ Re: Redundant code sections.

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-10-14T14:15:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bmh0ea$i49$2@news.utelfla.com>`
- **References:** `<8fc35a4e.0310080101.8f4e718@posting.google.com>`

```
We need more power captain <knuckles_doa@hotmail.com> wrote:

: does anyone know of a utility to search through source code  (Tandem
: COBOL in this case) and locate all the redundant sections  (i.e
: sections that have no corresponding PERFORM).  It would need to find
: redundant sections if they're called from a redundant section also.

Perhaps I am misunderstanding something, but doesn't the compile report
have a listing of where each of the paragraphs is called via PERFORM?

Failing that, it seems like it'd be easy enough to use the editor to search
for paragraph names that are not PERFORMed and go from there.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
