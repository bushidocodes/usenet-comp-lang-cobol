[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Try this code on for size!!

_7 messages · 6 participants · 1997-02_

---

### Try this code on for size!!

- **From:** "cug..." <ua-author-8920594@usenetarchives.gap>
- **Date:** 1997-02-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<330e7065.14391712@ccinews.ccinet.net>`

```

If anyone can figure this one out and actually walk through it, my hat
is off to them!

Array= 1,3,5,16,4,9,12,3,7,11



Par1

heap-size{a}=length{a}
for L=[length{a}/2]down to 1
do Par2{a,i}


Par2

L=left{i}
R=right{i}
If L<=heap-size{a} and a{L}>a{i}
Then largest= L
else largest=i
If R < = heap-size{a} and a{R} > a{largest}
Then largest = R
If largest <> i
Then exchange[a {i},a{largest}]
Par2{a,largest}
```

#### ↳ Re: Try this code on for size!!

- **From:** "mich..." <ua-author-1003144@usenetarchives.gap>
- **Date:** 1997-02-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<330e7065.14391712@ccinews.ccinet.net>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net>`

```

On Sat, 22 Feb 1997 04:23:19 GMT, cug··.@b··.edu (puddin) wrote:

› If anyone can figure this one out and actually walk through it, my hat
› is off to them!
…[23 more quoted lines elided]…
› 	Par2{a,largest} 

IF THIS-IS-COBOL
THEN-IT-IS-NO-COBOL-I-HAVE-EVER-SEEN
ELSE
WHAT-IS-IT-DOING-IN-THIS-COBOL-NG?
END-IF


P.S. If learning it will make me $100 per hour for the next 3 years,
then I am willing to learn it.


MJL
```

##### ↳ ↳ Re: Try this code on for size!!

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-02-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-df2f388cd9-p2@usenetarchives.gap>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net> <gap-df2f388cd9-p2@usenetarchives.gap>`

```

.mi··.@be··t.com wrote:
.>
.> On Sat, 22 Feb 1997 04:23:19 GMT, cug··.@b··.edu (puddin) wrote:
.>
.> >If anyone can figure this one out and actually walk through it, my
.hat
.> >is off to them!
.> >
.> >Array= 1,3,5,16,4,9,12,3,7,11
.> >
.> >
.> >
.> > Par1
.> >
.> > heap-size{a}=length{a}
.> > for L=[length{a}/2]down to 1
.> > do Par2{a,i}
.> >
.> >
.> > Par2
.> >
.> > L=left{i}
.> > R=right{i}
.> > If L<=heap-size{a} and a{L}>a{i}
.> > Then largest= L
.> > else largest=i
.> > If R < = heap-size{a} and a{R} > a{largest}
.> > Then largest = R
.> > If largest <> i
.> > Then exchange[a {i},a{largest}]
.> > Par2{a,largest}
.>
.> IF THIS-IS-COBOL
.> THEN-IT-IS-NO-COBOL-I-HAVE-EVER-SEEN
.> ELSE
.> WHAT-IS-IT-DOING-IN-THIS-COBOL-NG?
.> END-IF
.>
.> P.S. If learning it will make me $100 per hour for the next 3 years,
.> then I am willing to learn it.
.>
.> MJL


Looks too ugly to learn for me, even for $100 per hour. But since it
would probably take twice as long to deal with than Cobol would, you'd
make twice as much! It really is ungly code, isn't it?

Mike Dodas
```

###### ↳ ↳ ↳ Re: Try this code on for size!!

- **From:** "amos..." <ua-author-17073709@usenetarchives.gap>
- **Date:** 1997-02-22T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-df2f388cd9-p3@usenetarchives.gap>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net> <gap-df2f388cd9-p2@usenetarchives.gap> <gap-df2f388cd9-p3@usenetarchives.gap>`

```

In <330··.@u··.com> Michael Dodas writes:
› 
› .mi··.@be··t.com wrote:
…[48 more quoted lines elided]…
› Mike Dodas

It looks like a binary tree balancing routine written in C psudocode
( I wrote 1 not to long ago)
Why anyone would try to write this in Cobol with the Search all
function avaliable after a sort is unknown to me

Greg Amos just a newbe to programing but learning none the less

amo··.@ix.··m.com
```

###### ↳ ↳ ↳ Re: Try this code on for size!!

_(reply depth: 4)_

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-df2f388cd9-p4@usenetarchives.gap>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net> <gap-df2f388cd9-p2@usenetarchives.gap> <gap-df2f388cd9-p3@usenetarchives.gap> <gap-df2f388cd9-p4@usenetarchives.gap>`

```

Gregory Paul Amos wrote:
› 
› It looks like a binary tree balancing routine written in C psudocode
› ( I wrote 1 not to long ago)
› Why anyone would try to write this in Cobol with the Search all
› function avaliable after a sort is unknown to me

Actually, it is the first part of a heapsort. The heap (array in this case) is already
balanced.


Del.
```

##### ↳ ↳ Re: Try this code on for size!!

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-02-23T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-df2f388cd9-p2@usenetarchives.gap>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net> <gap-df2f388cd9-p2@usenetarchives.gap>`

```

I think the point to the posting was to show how GOOD COBOL is by how easy
it is to follow someone elses code. That, or the person got the wrong news
group.


mic··.@be··t.com wrote in article <330··.@nnt··t.com>...
› On Sat, 22 Feb 1997 04:23:19 GMT, cug··.@b··.edu (puddin) wrote:
› 
…[40 more quoted lines elided]…
›
```

#### ↳ Re: Try this code on for size!!

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df2f388cd9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<330e7065.14391712@ccinews.ccinet.net>`
- **References:** `<330e7065.14391712@ccinews.ccinet.net>`

```

puddin wrote:
›
› If anyone can figure this one out and actually walk through it, my hat
› is off to them!

It is the first half of a heapsort with some errors in it. My guess is that the
algorithm is written in someones personal pseudocode notation.

› Array=    1,3,5,16,4,9,12,3,7,11
› 
›         Par1
› 
 
› Establish a partially ordered tree.  The "for L" should be "for i".
 
›         heap-size{a}=length{a}
›         for L=[length{a}/2]down to 1
›           do Par2{a,i}
› 

While the tree is not partially ordered, push the largest node to the top (NB:
recursion is used).

› Par2
›

"left" and "right" must return the left and right child of the ith node. In the
case of an array data structure, this would be i+1 and i*2, respectively.

› L=left{i}
› R=right{i}

In the resulting partially ordered tree, the value of the ith node should be
greater than the value of either of its children.

›         If L<=heap-size{a} and a{L}>a{i}
›           Then largest= L
…[5 more quoted lines elided]…
›                 Par2{a,largest}



Del.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
