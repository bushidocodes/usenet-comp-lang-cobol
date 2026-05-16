[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New Wording for EXIT rules.

_3 messages · 3 participants · 2001-06 → 2001-07_

---

### New Wording for EXIT rules.

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-29T23:12:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106292212.366496bb@posting.google.com>`

```
Okay, we all know that the wording for the General Rules for EXIT
PARAGRAPH and EXIT SECTION are awful. I, too, would like to see
something in plain English.  Can the room give us a good one? If so, I
will certainly submit it to J4 as an editorial comment, and if it
really IS better, it will be adopted.  We all know what the statements
really mean, we just want to state the RULES as palinly as possible. 
Since this is a standard, it must be totally unambiguous, and cover
all cases.

I know that Pete Dashwood had a try at it, and it sounded good to me,
but I can't find it now.

Here are the old rules, now LET THE PROCESS BEGIN!
*------------------
10) If an EXIT statement with the PARAGRAPH phrase is executed, the
EXIT statement causes control to be passed
to an implicit CONTINUE statement immediately following the last
statement in the current paragraph.
11) If an EXIT statement with the SECTION phrase is executed, the EXIT
statement causes control to be passed to
an implicit CONTINUE statement immediately following the last
statement in the last paragraph in the current
section.
*------------------

I am curious to see how well this open process works. Pete, the ball
is in your court...

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

#### ↳ Re: New Wording for EXIT rules.

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-07-05T14:50:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i1uqv$1mf$1@news.netmar.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com>`

```
If you are using an EXIT PERFORM, isnt that the same as using a GO TO?

Why not just split the perform up into two paragraphs or simply use a GO TO?

 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

##### ↳ ↳ Re: New Wording for EXIT rules.

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-07-06T17:02:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B45EF11.9133171C@home.com>`
- **References:** `<4145699b.0106292212.366496bb@posting.google.com> <9i1uqv$1mf$1@news.netmar.com>`

```


chammond@lc.cc.il.us wrote:

> If you are using an EXIT PERFORM, isnt that the same as using a GO TO?
>
> Why not just split the perform up into two paragraphs or simply use a GO TO?
>

I suppose a lot depends upon how you are coding, (and bear in mind I only use OO).
Without going all 'tecchie' :-

(1) A 'directive' to GO TO this particular point in the code - a paragraph name

(2) EXIT PERFORM you are going to the next line of code, immediately following the
END-PERFORM. Assuming your in-line perform is contained in a paragraph - the GO TO
construct doesn't work  for you, because you may have other instructions to perform
before quitting the PARAGRAPH (or METHOD).

EXIT-PERFORM, EXIT-METHOD - I like it ! I like it !

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
