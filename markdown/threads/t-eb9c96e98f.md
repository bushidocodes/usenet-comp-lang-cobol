[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie-ish question about PICTURE IS

_3 messages · 3 participants · 2010-10_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Newbie-ish question about PICTURE IS

- **From:** axtens <bruce.axtens@gmail.com>
- **Date:** 2010-10-11T20:15:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d9c17be-24b8-44ed-815f-0fd4ffc1598c@u5g2000prn.googlegroups.com>`

```
The last time I did anything of note with COBOL was in the mid 1980s.
It's been a long long time and I've forgotten more than I ever knew.

That said, can someone explain to me why the REDEFINES in the code
below doesn't hide the leading zeroes, but the MOVE to display-counter
does.

Kind regards,
Bruce.

identification division.
program-id. ztest.
author. Bruce Axtens.
data division.
working-storage section.
01	counters.
	05	counter1	picture is 99.
	88	is-zero value 0.
	05	counter-display redefines counter1 picture is ZZ.
01	display-counter	picture is ZZ.

procedure division.
100-main section.
	perform with test after varying counter1 from 10 by -1 until is-zero
		display counter1 " " with no advancing
		display counter-display " " with no advancing
		move counter1 to display-counter
		display display-counter
	end-perform.
	stop run.
	end-program.


C:\OpenCobol>ztest
10 10 10
09 09  9
08 08  8
07 07  7
06 06  6
05 05  5
04 04  4
03 03  3
02 02  2
01 01  1
00 00
```

#### ↳ Re: Newbie-ish question about PICTURE IS

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2010-10-11T20:53:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4baa074d-e699-4c3f-8670-b39903c1cf96@z28g2000yqh.googlegroups.com>`
- **References:** `<4d9c17be-24b8-44ed-815f-0fd4ffc1598c@u5g2000prn.googlegroups.com>`

```
On Oct 11, 10:15 pm, axtens <bruce.axt...@gmail.com> wrote:
> The last time I did anything of note with COBOL was in the mid 1980s.
> It's been a long long time and I've forgotten more than I ever knew.
…[41 more quoted lines elided]…
> 00 00



Somewhat simplified, the formatting happens when you move data to the
field.  So when you move a new value to counter1, it's formatted as
pic 99 at that time.  The pic ZZ field is only read, and that happens
largely like a character field, so the ZZ in counter-display never has
an opportunity to do anything.
```

##### ↳ ↳ Re: Newbie-ish question about PICTURE IS

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-10-12T05:51:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j5Xso.266870$mN7.3277@en-nntp-08.dc1.easynews.com>`
- **References:** `<4d9c17be-24b8-44ed-815f-0fd4ffc1598c@u5g2000prn.googlegroups.com> <4baa074d-e699-4c3f-8670-b39903c1cf96@z28g2000yqh.googlegroups.com>`

```
<robertwessel2@yahoo.com> wrote in message 
news:4baa074d-e699-4c3f-8670-b39903c1cf96@z28g2000yqh.googlegroups.com...
On Oct 11, 10:15 pm, axtens <bruce.axt...@gmail.com> wrote:
> The last time I did anything of note with COBOL was in the mid 1980s.
> It's been a long long time and I've forgotten more than I ever knew.
…[41 more quoted lines elided]…
> 00 00



.> Somewhat simplified, the formatting happens when you move data to the
> field.  So when you move a new value to counter1, it's formatted as
> pic 99 at that time.  The pic ZZ field is only read, and that happens
> largely like a character field, so the ZZ in counter-display never has
> an opportunity to do anything.

Another way to think about this is to remember that a REDEFINES *never* 
changes the data in a field.  It is just another way of looking at the data 
that is there.  (As well as determining how that data is received and sent)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
