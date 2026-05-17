[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNSTRING works in program but not in function

_2 messages · 2 participants · 2015-10 → 2015-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### UNSTRING works in program but not in function

- **From:** "bruce.axtens" <ua-author-12894444@usenetarchives.gap>
- **Date:** 2015-10-30T10:59:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30b051fd-55a7-40e4-b6e9-8ac326bb674e@googlegroups.com>`

```
Let's assume I'm a newbie. Given how long it is since I last used COBOL consistently ...

The UNSTRING/STRING in the program works but fails in the function. In the function it doesn't split the string on the value of needle1.

This is MicroFocus COBOL 2.3 under Visual Studio 2015 on Windows 10 Home 64bit.


program-id. Program1 as "GSUB1.Program1".
environment division.
CONFIGURATION SECTION.
repository.
function gsub.
data division.
working-storage section.
01 working.
03 haystack1 value "my dog has fleas".
03 needle1 value "has".
03 needle2 value "had".
03 haystack2 pic x(20) value spaces.
03 lhs-count usage display pic 9(6) value 0.
03 rhs-count usage display pic 9(6) value 0.
01 others.
03 lhs pic x(10).
03 rhs pic x(10).
procedure division.

unstring haystack1 delimited by needle1 into lhs count in lhs-count, rhs count in rhs-count.
string lhs(1:lhs-count), needle2, rhs(1:rhs-count) into haystack2.

display function gsub(haystack1, needle1, needle2).

goback.

end program Program1.

identification division.
function-id. gsub.
data division.
working-storage section.
01 lhs-count pic 9(5) value zero.
01 rhs-count pic 9(5) value zero.
01 lhs pic x(25) value spaces.
01 rhs pic x(25) value spaces.

linkage section.
01 haystack1 pic x(25).
01 needle1 pic x(25).
01 needle2 pic x(25).
01 haystack2 pic x(51).
procedure division using haystack1, needle1, needle2 returning haystack2.

unstring haystack1 delimited by needle1 into lhs count in lhs-count, rhs count in rhs-count.
string lhs(1:lhs-count), needle2, rhs(1:rhs-count) into haystack2.

goback.

end function gsub.


Bruce/bugmagnet
```

#### ↳ Re: UNSTRING works in program but not in function

- **From:** "bwtiffin" <ua-author-14501766@usenetarchives.gap>
- **Date:** 2015-12-01T17:54:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8fbff6bd29-p2@usenetarchives.gap>`
- **In-Reply-To:** `<30b051fd-55a7-40e4-b6e9-8ac326bb674e@googlegroups.com>`
- **References:** `<30b051fd-55a7-40e4-b6e9-8ac326bb674e@googlegroups.com>`

```
On Friday, October 30, 2015 at 10:59:16 AM UTC-4, Bruce Axtens wrote:
› Let's assume I'm a newbie. Given how long it is since I last used COBOL consistently ...
› 
…[57 more quoted lines elided]…
› Bruce/bugmagnet

Late response:

The data being passed to linkage is shorter than the picture. You'll get garbage in.

haystack1 has "my dogs has fleasxxxxxxxxxxxx..."
Needle1 in the gsub function will have "hasxxxxxxxxxxxxxxxxxx..." so the unstring won't work as expected.

I didn't try this with Micro Focus, but

linkage section.
01 haystack1 pic x any length.
01 needle1 pic x any length.
01 needle2 pic x any length.
01 haystack2 pic x(51).

worked under GnuCOBOL 2. The identifiers in the function pick up the proper lengths from the function caller and cut out the garbage.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
