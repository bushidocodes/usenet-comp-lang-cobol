[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using the nearest EXIT

_5 messages · 5 participants · 1995-08_

---

### Using the nearest EXIT

- **From:** "tea..." <ua-author-17087727@usenetarchives.gap>
- **Date:** 1995-08-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<421372$3j@uucp.intac.com>`

```
Hi,

For a program I am doing for class, I needed a way to get out of a called
routine back to the calling routine. On a hunch I used EXIT and it worked.
The question is: it seems from the books I have here that EXIT is used in
the context of EXIT PROGRAM to leave a subprogram to go back to the calling
program. Is EXIT actually used in the case when there is only one program
and I want to go from sub-routine to calling routine, or is there another
more acceptable way of doing this (short of the dreaded GO TO).

Thanx,

Bennett
```

#### ↳ Re: Using the nearest EXIT

- **From:** "jst..." <ua-author-17087635@usenetarchives.gap>
- **Date:** 1995-08-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa7fbb03ed-p2@usenetarchives.gap>`
- **In-Reply-To:** `<421372$3j@uucp.intac.com>`
- **References:** `<421372$3j@uucp.intac.com>`

```
›   tea··.@in··c.com (Bennett Ruda) writes:
›  Hi,
…[7 more quoted lines elided]…
›  more acceptable way of doing this (short of the dreaded GO TO).


I think the best way to do this is to use a GOBACK.
```

#### ↳ Re: Using the nearest EXIT

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-08-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa7fbb03ed-p3@usenetarchives.gap>`
- **In-Reply-To:** `<421372$3j@uucp.intac.com>`
- **References:** `<421372$3j@uucp.intac.com>`

```
In article <421372$3.··.@uuc··c.com>
tea··.@in··c.com (Bennett Ruda) writes:

› 
› Hi,
…[8 more quoted lines elided]…
› 
I've noticed that it depends on what computer you use COBOL.
I have seen exit by itself only used for perform thru's, as in:

Perform g0000-get-down thru g0000-exit.

g0000-get-down.
IF ws-feeling-mean
go to g0000-exit.

g0000-exit.
exit.
Even though there is a branch to g0000-exit, control returns to the para
which did the perform thru...
And exit program is the way to return to a calling program. However,
goback is an IBM extension that can be used on IBM.


So in the called program returning to the caller:

....
EXIT PRogram.

or
goback.

But goback doesn't work on other machines.
It used to be that stop run was the way to stop the main program.
But if it is an IMS program, you were supposed to use goback,
since "your program" was a subroutine to IMS....



Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

#### ↳ Re: Using the nearest EXIT

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-08-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa7fbb03ed-p4@usenetarchives.gap>`
- **In-Reply-To:** `<421372$3j@uucp.intac.com>`
- **References:** `<421372$3j@uucp.intac.com>`

```
tea··.@in··c.com (Bennett Ruda) wrote:

› Hi,
 
› For a program I am doing for class, I needed a way to get out of a called
› routine back to the calling routine. On a hunch I used EXIT and it worked.
…[4 more quoted lines elided]…
› more acceptable way of doing this (short of the dreaded GO TO).

Well, on the Unisys A Series machines you can use the EXIT PERFORM statement.
This statement functions like a "return" in procedural languages. I think it is
great. You can write code that has less go to's and less paragraphs. We use this
statement in many of our programs. Here is an example

PERFORM para-1 THRU para-1-exit.
:
:
para-1.

:
IF return-value THEN
EXIT PERFORM.
:
:
para-1-exit.
EXIT.

Or you can use:

PERFORM WITH TEST AFTER
VARYING my-counter FROM 1 BY 1 UNTIL 100

:
:
IF counter = 70 AND file1-eof THEN
EXIT PERFORM
END-IF
:
:
END PERFORM.

This syntax, I think, will be in the COBOL97 standard. I think it has been
submitted but not approved. Can someone confirm this for me please.

› Thanx,
 
› Bennett
 
 
› --
› Bennett J. Ruda              || "The World exists only because of
› Former teacher               || the innocent breath of schoolchildren"
› Whose credo remains the same || From the Talmud
› tea··.@in··c.com            || Masechet Shabbat 119b


------------------------------------------------------
Gordon DeGrandis Gor··.@pi··g.be
Contraste Europe S.A. Brussels, Belgium
These are my opinions.
-------------------------------------------------------
Never tell people how to do things. Tell them what to do
and they will surprise you with their ingenuity.
- General George S. Patton
```

##### ↳ ↳ Re: Using the nearest EXIT

- **From:** "bob dombroski" <ua-author-17087774@usenetarchives.gap>
- **Date:** 1995-08-31T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa7fbb03ed-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa7fbb03ed-p4@usenetarchives.gap>`
- **References:** `<421372$3j@uucp.intac.com> <gap-aa7fbb03ed-p4@usenetarchives.gap>`

```
I agree with Gordon.

Although there are ways to avoid this situation, exit perform works fine
(even though you've created an implicit GOTO
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
