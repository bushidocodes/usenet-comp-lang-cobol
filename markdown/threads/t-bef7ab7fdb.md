[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Searching Tables

_2 messages · 2 participants · 1999-09_

---

### Re: Searching Tables

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF5B25.51993BB9@zip.com.au>`
- **References:** `<37ED8B5B.5DD67199@home.com> <37ee4b57.122921762@news2.ibm.net> <37EE7DFC.3F71B6A1@home.com>`

```
"James J. Gavan" wrote:
> 
> Volker Bandke wrote:
…[25 more quoted lines elided]…
> Jimmy, Calgary AB

I prefer the search statement.  Adding the index is really a small
price to pay especially since you need to define a subscript anyway
and there is a performance benefit for the index in most cases.

The other thing is the implicit bounds checking performed by search
with OCCURS DEPENDING ON tables.  I have experienced too many errors
with turning debugging (such as SSRANGE in MVS).

This is one of the selling points of Cobol.  The main trap is having
to set the index to 1 before you start with 'standard' search but not
with search all.  This is useful for locating multiple occurrences of
the same key in the same table but causes many hours of debugging. 
(Must write this into the inspection guide for Cobol).

Junior programmer challenge:  How do you find the first key entry from
a table where the ordered key is duplicated multiple times using a
search all.

Ken
```

#### ↳ Re: Searching Tables

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EFA8A3.8261AB94@home.com>`
- **References:** `<37ED8B5B.5DD67199@home.com> <37ee4b57.122921762@news2.ibm.net> <37EE7DFC.3F71B6A1@home.com> <37EF5B25.51993BB9@zip.com.au>`

```
Ken Foskey wrote:
> 
> "James J. Gavan" wrote:
…[47 more quoted lines elided]…
> Ken

Thanks Thane, Volker and Ken,

I was mulling over this one this morning as I was having my first cuppa.

In response to Volker's first query "Why haven't you considered....".
Good question, with a simple answer. Never had the luxury of going to
school to learn COBOL; taught myself out of necessity to earn a living.
May not be the most efficient coder, but with a systems background -
I'll not be modest - I can put a good design together. In some respects,
that's perhaps an advantage over 'tweeking' at code to save
milli/microseconds.

For Volker's information - dare I say it - my end-user is a German
perfectionist <G>, highly respected in his field, and was invited by
Chevron to lecture to their plant managers on Non-Destructive Testing.
So we are constantly playing a game, me trying to anticipate the next
short-cut he might look for in my design, and he, always coming back,
with another neat twist to automate his data entry even further -
sometimes frustrating for me, but also fun -  keeps this old guy
mentally alert.

Nevertheless, as I would say to anybody who cares to ask, unashamedly
'steal' other peoples code if you find their technique clearer/more
efficient than what you have been doing.

Volker has indicated he teaches COBOL - so any comment on the following. 
Seems to me the academic world should be a good resource for us
bread-and-butter guys. A big ZIP in Calgary. Probably the major centre
for computing in Canada because of the oil/gas, and I have no idea, but
there could be in excess of 1,000 COBOL programmers chugging away on
those mainframes.

We have a University and Tech Institute, both with glitzy web-sites.
Seeking general background on collections/dictionaries, (I know they
have OO courses), posted an e-mail to a likely candidate at the two
institutions. Got zippo back - not even a polite acknowledgement.

Some 5 years ago phoned the COBOL department of another Tech College
with separate queries some two years apart. Both times got the same
Chinese instructor, (no, I'm not being racist, I recognised his Hong
Kong accent). On both occasions he was extremely defensive and both
times started the conversation with "Why are you phoning me, you should
be phoning your instructor". Absolutely aghast that somebody from the
real world was asking for his advice. Both occasions he got off the
phone as quickly as possible.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
