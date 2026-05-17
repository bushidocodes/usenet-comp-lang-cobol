[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Omit Leading Zeroes

_7 messages · 4 participants · 1996-06_

---

### Omit Leading Zeroes

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-06-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4pnbdt$8l7@nnrp1.news.primenet.com>`

```

In Micro Focus COBOL, I want to "string" some values into a destination
record without including leading zeroes. I've got literally millions of
these records (for bulk copying into a database).

For example, string "1," delimited by size, SOME-NAME delimited by space,
"," delimited by size, THAT-NUMBER delimited by size, "," ...

If SOME-NAME contains "FOO " and THAT-NUMBER is pic 9(8) with a
value of 12, I'll still get: 1,FOO,00000012, ...

How can I get 1,FOO,12, ... ? Over several million records, that's
a lot of bytes saved.

I know how to edit THAT-NUMBER byte by byte into another variable
which will end up with a value of "12 " and then I could use that as
the source of a "string ... delimited space", but it seems like so much
more work than should be needed for such a straightforward and common
operation. Of course I could go to the C library, but that would be a
cop-out. ;-)

So what simple method am I missing here?

dd--
Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

#### ↳ Re: Omit Leading Zeroes

- **From:** "ggra..." <ua-author-12492810@usenetarchives.gap>
- **Date:** 1996-06-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4pnbdt$8l7@nnrp1.news.primenet.com>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com>`

```

In article <4pnbdt$8.··.@nnr··t.com> you wrote:
: In Micro Focus COBOL, I want to "string" some values into a destination
: record without including leading zeroes. I've got literally millions of
: these records (for bulk copying into a database).
:
: For example, string "1," delimited by size, SOME-NAME delimited by space,
: "," delimited by size, THAT-NUMBER delimited by size, "," ...
:
: If SOME-NAME contains "FOO " and THAT-NUMBER is pic 9(8) with a
: value of 12, I'll still get: 1,FOO,00000012, ...
:
: How can I get 1,FOO,12, ... ? Over several million records, that's
: a lot of bytes saved.
:
: I know how to edit THAT-NUMBER byte by byte into another variable
: which will end up with a value of "12 " and then I could use that as
: the source of a "string ... delimited space", but it seems like so much
: more work than should be needed for such a straightforward and common
: operation. Of course I could go to the C library, but that would be a
: cop-out. ;-)
:
: So what simple method am I missing here?
:
: dd--
: Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner

Try (untested):

move 0 to t
inspect THAT-NUMBER tallying i for leading zero
string "1," delimited by size
SOME-NAME delimited by space
"," delimited by size
THAT-NUMBER(i) delimited by size
"," ...
into foo

I think that should do the trick.

Greg
//
Greg Granger
egr··.@na··o.net
```

##### ↳ ↳ Re: Omit Leading Zeroes

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1996-06-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c29cdcb850-p2@usenetarchives.gap>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com> <gap-c29cdcb850-p2@usenetarchives.gap>`

```



› ggr··.@na··o.net (G. O. Granger) wrote in article
› <4pnljj$k.··.@cas··o.net>...
 
›  move 0 to t
›  inspect THAT-NUMBER tallying i for leading zero
…[7 more quoted lines elided]…
› I think that should do the trick.

Not quite.

move 1 to i
inspect THAT-NUMBER tallying i for leading zero
if THAT-NUMBER = zero then subtract 1 from i
string "1," delimited by size
SOME-NAME delimited by space
"," delimited by size
THAT-NUMBER(i:) delimited by size
"," delimited by size
...
into FOO.

Reference modification is denoted by the (start:length) syntax. The
variable start designates the first (counting from the left) character
position to be moved and the variable length designates a count of
characters. In the above example, the variable i is calculated to
indicated the first nonzero character position, or the last zero in the
case when that-number contains only zero. When length is omitted as in
the example, all remaining characters are moved.

Hope this works for you.

Tom Morrison, T.M··.@li··t.com
Relativity (div. Liant Software)
512-719-7019  FAX:512-719-7070  WWW: http://www.liant.com/
```

###### ↳ ↳ ↳ Re: Omit Leading Zeroes

- **From:** "ggra..." <ua-author-12492810@usenetarchives.gap>
- **Date:** 1996-06-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c29cdcb850-p3@usenetarchives.gap>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com> <gap-c29cdcb850-p2@usenetarchives.gap> <gap-c29cdcb850-p3@usenetarchives.gap>`

```

Tom Morrison (t.m··.@li··t.com) wrote:
: > ggr··.@na··o.net (G. O. Granger) wrote in article
: <4pnljj$k.··.@cas··o.net>...
:
: > move 0 to t
: >...
: > string "1," delimited by size
: Not quite.
:
: move 1 to i
: inspect THAT-NUMBER tallying i for leading zero
: if THAT-NUMBER = zero then subtract 1 from i
: string "1," delimited by size
: SOME-NAME delimited by space
: "," delimited by size
: THAT-NUMBER(i:) delimited by size
: "," delimited by size
: ...
: into FOO.
:
: Reference modification is denoted by the (start:length) syntax. The
: variable start designates the first (counting from the left) character
: position to be moved and the variable length designates a count of
: characters. In the above example, the variable i is calculated to
: indicated the first nonzero character position, or the last zero in the
: case when that-number contains only zero. When length is omitted as in
: the example, all remaining characters are moved.
:
: Hope this works for you.

Oops quite right ... I did say it was untested ;-)
Thanks,
Greg
//
Greg Granger
ggr··.@na··o.net
```

###### ↳ ↳ ↳ Re: Omit Leading Zeroes

_(reply depth: 4)_

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-06-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c29cdcb850-p4@usenetarchives.gap>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com> <gap-c29cdcb850-p2@usenetarchives.gap> <gap-c29cdcb850-p3@usenetarchives.gap> <gap-c29cdcb850-p4@usenetarchives.gap>`

```

G. O. Granger wrote:
: Tom Morrison (t.m··.@li··t.com) wrote:
: : > ggr··.@na··o.net (G. O. Granger) wrote in article

Thanks. I guess the answer is:

1. COBOL simply falls flat on its face in this area.
There is no equivalent to the 'sprintf' with a %d format,
that can be used in the otherwise very powerful STRING command.

DON NELSON and others involved in standards development:
please consider "OMITTING LEADING " as a feature in the
STRING command!

2. Greg's INSPECT solution (as corrected by Tom, or just
bypassing and stuffing literal "0 " if the source is zero,
of as Greg offered it if you "know it'll NEVER be zero",
is the cleanest we can get it for now.

I've adopted that solution, packaged as shown below.
In this case I chose to save a source variable from which I could do
a STRING ... delimited spaces, rather than saving the OFFSET value
for the numeric variable.

So the code I'm using reads pretty cleanly:

call LJ-NUM using NUM-VAR, STRING-VAR

...and later, ...
unstring ... STRING-VAR delimited spaces, ...

--- begin boring detail section ---

In case anyone cares, the LJ-NUM nested subprogram has:

In the LINKAGE:
77 NUMERIC-VALUE pic 9(8).
77 STRING-SOURCE pic x(9).
In WORKING storage:
77 OFFSET pic 99 comp.

. . . if NUMERIC-VALUE = zero
move "0 " to STRING-SOURCE ("0" is OK but less clear...)
else
move 1 to OFFSET
inspect NUMERIC-VALUE tallying OFFSET for leading zero
* ### MOVE will store left justified with trailing spaces...
move NUMERIC-VALUE(OFFSET:) to STRING-SOURCE
end-if

This works out especially nicely because that subprogram is actually
doing some other stuff for me too.

Thanks again,

Victor Odhner, Phoenix AZ http://www.primenet.com/~vodhner
```

#### ↳ Re: Omit Leading Zeroes

- **From:** "kathleen kelley" <ua-author-1957366@usenetarchives.gap>
- **Date:** 1996-06-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4pnbdt$8l7@nnrp1.news.primenet.com>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com>`

```

Victor Odhner wrote:
› 
› In Micro Focus COBOL, I want to "string" some values into a destination
…[22 more quoted lines elided]…
› Victor Odhner,  Phoenix AZ        http://www.primenet.com/~vodhner

Define THAT-NUMBER as Pic Z(8), then delimit by space.
```

##### ↳ ↳ Re: Omit Leading Zeroes

- **From:** "ggra..." <ua-author-12492810@usenetarchives.gap>
- **Date:** 1996-06-12T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c29cdcb850-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c29cdcb850-p6@usenetarchives.gap>`
- **References:** `<4pnbdt$8l7@nnrp1.news.primenet.com> <gap-c29cdcb850-p6@usenetarchives.gap>`

```

Kathleen Kelley (b.··.@mic··e.net) wrote:
: Victor Odhner wrote:
: >
: > In Micro Focus COBOL, I want to "string" some values into a destination
: > record without including leading zeroes. I've got literally millions of
: > these records (for bulk copying into a database).
: >
: > For example, string "1," delimited by size, SOME-NAME delimited by space,
: > "," delimited by size, THAT-NUMBER delimited by size, "," ...
: >
: > If SOME-NAME contains "FOO " and THAT-NUMBER is pic 9(8) with a
: > value of 12, I'll still get: 1,FOO,00000012, ...
: >
: > How can I get 1,FOO,12, ... ? Over several million records, that's
: > a lot of bytes saved.
: >
: > I know how to edit THAT-NUMBER byte by byte into another variable
: > which will end up with a value of "12 " and then I could use that as
: > the source of a "string ... delimited space", but it seems like so much
: > more work than should be needed for such a straightforward and common
: > operation. Of course I could go to the C library, but that would be a
: > cop-out. ;-)
: >
: > So what simple method am I missing here?
: >
: > dd--
: > Victor Odhner, Phoenix AZ http://www.primenet.com/â€¾vodhner
:
: Define THAT-NUMBER as Pic Z(8), then delimit by space.

I'm afraid that will not give him quite what he wants, consider:

working-storage section.
01 i pic 9(8) value 12.
01 j pic zzzzzzz9.
01 s pic x(70) value spaces.

procedure division.
move i to j
string "|" delimited by size
j delimited by space
"|" delimited by size
into s
display s

This will display "||", not "|12|" because the string command will delimit
by space and the leading spaces will cause an empty string value to be
returned.

As well as the inspect solution (which I suspect is the fastest you could
also use the unstring command) ... I suspect this is what you might have
been thinking about:
working-storage section.
01 i pic 9(8) value 12.
01 j pic zzzzzzz9.
01 s pic x(70) value spaces.
01 s1 pic x(70) value spaces.
01 s2 pic x(70) value spaces.

procedure division.
move i to j
move j to s
unstring s delimited by all spaces into s1 s2
display s1
display s2
exit program.

In the above s2 will contain the number desired and s1 will contain an empty
string.

Greg

//
Greg Granger
ggr··.@na··o.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
