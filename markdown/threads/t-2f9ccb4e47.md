[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A fat finger mistake

_16 messages · 6 participants · 2018-04_

---

### A fat finger mistake

- **From:** "ronald.s.draper" <ua-author-14501841@usenetarchives.gap>
- **Date:** 2018-04-28T01:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com>`

```
Editted a program the other day that looked like:

Perform a-routine.

And ended up with the following line:

Perform perform a-routine.

Compiler issued no warnings.

It created a great loop.

I kind of expected to see a warning that part of perform syntax was missing.

Just wondering who else fat fingered a perfect loop.

Ron
```

#### ↳ Re: A fat finger mistake

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-28T04:08:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p2@usenetarchives.gap>`
- **In-Reply-To:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com>`

```
On 28/04/2018 5:42 PM, ron··r@gm··l.com wrote:
› Editted a program the other day that looked like:
› 
…[15 more quoted lines elided]…
› 

What compiler and version of COBOL was this, Ron?

Pete.

I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: A fat finger mistake

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-28T09:36:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p2@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap>`

```
On 04/28/2018 04:08 AM, pete dashwood wrote:
› On 28/04/2018 5:42 PM, ron··r@gm··l.com wrote:
›› Editted a program the other day that looked like:
…[20 more quoted lines elided]…
› 

Not GNU COBOL which immediately barfed on that line. :-)

bill
```

###### ↳ ↳ ↳ Re: A fat finger mistake

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-04-28T13:18:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p3@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap>`

```
On Saturday, April 28, 2018 at 9:37:00 AM UTC-4, Bill Gunshannon wrote:
› On 04/28/2018 04:08 AM, pete dashwood wrote:
›› On 28/04/2018 5:42 PM, ron··.@gm··l.com wrote:
…[23 more quoted lines elided]…
› Not GNU COBOL which immediately barfed on that line.  :-)

Then GNU COBOL is broken. ;)

It shouldn't 'barf' until it encounters a separator period,
at which time it should report that an END-PERFORM is missing.

In other words,

perform perform a-routine
*> several lines of code
end-perform
.

is valid. Leaving out the 'end-perform' is the error.

Micro Focus did, and may still, allow 'perform' without 'end-perform'.
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-28T15:50:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p4@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap>`

```
On 04/28/2018 01:18 PM, Rick Smith wrote:
› On Saturday, April 28, 2018 at 9:37:00 AM UTC-4, Bill Gunshannon wrote:
›› On 04/28/2018 04:08 AM, pete dashwood wrote:
…[16 more quoted lines elided]…
›››› 
 
››››   Just wondering who else fat fingered a perfect loop.
›››› 
…[23 more quoted lines elided]…
› 

Oops. I left off the end perform and he did complain abut that.
I'll try again.

My trest had only one line of code after the perform and a period
so I didn't include the end-perform. I'll add to it and test again.

bill
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 5)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-04-28T16:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p5@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap>`

```
On Saturday, April 28, 2018 at 3:50:09 PM UTC-4, Bill Gunshannon wrote:
› On 04/28/2018 01:18 PM, Rick Smith wrote:
›› On Saturday, April 28, 2018 at 9:37:00 AM UTC-4, Bill Gunshannon wrote:
…[50 more quoted lines elided]…
› so I didn't include the end-perform.  I'll add to it and test again.

Also, have a look at Gary's Guides
< https://open-cobol.sourceforge.io/guides/GnuCOBOL%202.2%20NOV2017%20Programmers%20Guide%20(US%20Letter).pdf >, page 436. That shows ' [ END-PERFORM ] ', that is, optional. Unless testing the program for conformance to the standard, GNU COBOL should not require the END-PERFORM. Either that or amend the manual.

This is what i am talking about for conformance testing.
-----
* Micro Focus COBOL Version 3.2.50 ... 28-Apr-18 15:14 Page 1
...
1$set ans85 flag"ans85" flagas"s"
2 identification division.
3 program-id. p-test.
4 data division.
5 working-storage section.
6 1 n binary pic 9(4) value 0.
7 procedure division.
8 begin.
9 perform perform a-routine
10 add 1 to n
11 add 1 to n
12 add 1 to n
13 add 1 to n
14 add 1 to n
15 add 1 to n
16 add 1 to n
17 add 1 to n
18 add 1 to n
19* end-perform
20 .
* 584-S***** ( 0)**
** In-line PERFORM statement not terminated by END-PERFORM
21 stop run
22 .
23 a-routine.
24
25 end program p-test.
* Micro Focus COBOL Version 3.2.50 L2.5 revision 000
* Last message on page: 1
*
* Total Messages: 1
* Unrecoverable : 0 Severe : 1
* Errors : 0 Warnings: 0
* Informational : 0 Flags : 0
* Data: 500 Code: 120
-----

Remove the comment for 'end-perform' and program compiles without error.
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 6)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-28T17:23:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p6@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap> <gap-2f9ccb4e47-p6@usenetarchives.gap>`

```
On 04/28/2018 04:41 PM, Rick Smith wrote:
› On Saturday, April 28, 2018 at 3:50:09 PM UTC-4, Bill Gunshannon wrote:
›› On 04/28/2018 01:18 PM, Rick Smith wrote:
…[98 more quoted lines elided]…
› 

And, at least under GUN COBOL runs correctly, too. As long as
the end-perform is there the two performs constitute a valid
COBOL statement.

bill
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 5)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2018-04-29T09:57:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p5@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap>`

```
Hello Rick!

Answering a msg of , from Rick Smith to All:

Running the same with GC v3.0rc using cobc -x test1.cbl -Wall -t test1.lst

gives me a clean comile as the listing shows:
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 6)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-29T10:53:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p8@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap> <gap-2f9ccb4e47-p8@usenetarchives.gap>`

```
On 04/29/2018 09:57 AM, Vince Coen wrote:
› Hello Rick!
› 
…[5 more quoted lines elided]…
› 


There is no bug in the statement. With the end-perform to
dis-disambiguate the statement it is perfectly valid and makes
perfect sense. Now, whether or not it does what the author
intended is another matter, but not COBOL related. :-)

bill
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-04-29T22:46:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p8@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap> <gap-2f9ccb4e47-p8@usenetarchives.gap>`

```
On Sunday, April 29, 2018 at 10:09:29 AM UTC-4, Vince Coen wrote:

< snip >

› So it appears to be ignoring the double perform, a bug or a feature:)

How about neither!

With respect to COBOL 85, wrapping code inside a PERFORM ... END-PERFORM
has absolutely no effect on execution. Furthermore, there were no
statements that could affect the flow of control. With no effect, no bug
and no feature!

With the addition of EXIT PERFORM in COBOL 2002, there was now a means
to affect flow of control. This may be used to the same effect as,

in C

do {
...
if (condition_1) break;
...
} while (0);

in COBOL

perform
...
if condition-1
exit perform
end-if
...
end-perform

Whether that is of value is up to the programmer.

The alternatives for the same purpose are:

perform

perform 1 time

move 0 to data-name-1
perform test after until data-name-1 = 0

The last because the standard does not allow ' 0 = 0 '.
"A relation condition shall contain at least one reference to an
operand that is not a literal." [COBOL 2002]

I think that is about all than can be said!
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 7)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-04-30T02:46:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p10@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p5@usenetarchives.gap> <gap-2f9ccb4e47-p8@usenetarchives.gap> <gap-2f9ccb4e47-p10@usenetarchives.gap>`

```
On Sunday, April 29, 2018 at 10:47:00 PM UTC-4, Rick Smith wrote:

< snip >

Oops!

› perform 1 time

Should be

perform 1 times
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-04-29T00:45:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p4@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap>`

```
On 29/04/2018 5:18 AM, Rick Smith wrote:
› On Saturday, April 28, 2018 at 9:37:00 AM UTC-4, Bill Gunshannon wrote:
›› On 04/28/2018 04:08 AM, pete dashwood wrote:
…[41 more quoted lines elided]…
› 
Applause and kudos to Rick Smith. (I hope you'll be around here for
years to come, Rick. You have consistently over the years shown us
levels of COBOL most people don't ever see.)

This is a case in point. First to realize that the doubled Perform is
fine, provided there is a scope delimiter or terminator.

Throughout my own career and since they became available, I have always
used scope delimiters and encouraged others to do likewise. Leaving them
off is laziness and, as the above shows, it CAN be dangerous laziness.

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 5)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2018-04-29T08:44:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p12@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p12@usenetarchives.gap>`

```
On Sunday, April 29, 2018 at 12:45:38 AM UTC-4, pete dashwood wrote:

< snip >

› [...] First to realize that the doubled Perform is
› fine, provided there is a scope delimiter or terminator.

I have known about

perform
imperative-statement
end-perform

for maybe 15 to 20 years, but I never found occasion to use it. In effect,
the answer was waiting a very long time for the question!
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 6)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-29T09:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p13@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p4@usenetarchives.gap> <gap-2f9ccb4e47-p12@usenetarchives.gap> <gap-2f9ccb4e47-p13@usenetarchives.gap>`

```
On 04/29/2018 08:44 AM, Rick Smith wrote:
› On Sunday, April 29, 2018 at 12:45:38 AM UTC-4, pete dashwood wrote:
› 
…[13 more quoted lines elided]…
› 

I think the point is that until the introduction of in-line performs
the scope delimiter was not necessary as there was no way to write
an ambiguous PERFORM. The double PERFORM would have been flagged as
an error. I still have Ryan-Mcfarland (ANSI 74 and ANSI 85) running
on a number of systems here. Maybe I will try it just to see how it
flags the error.

bill
```

###### ↳ ↳ ↳ Re: A fat finger mistake

- **From:** "nworth" <ua-author-6588740@usenetarchives.gap>
- **Date:** 2018-04-29T16:59:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p3@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap>`

```
Bill Gunshannon wrote:
› On 04/28/2018 04:08 AM, pete dashwood wrote:
›› On 28/04/2018 5:42 PM, ron··r@gm··l.com wrote:
…[26 more quoted lines elided]…
› 
Even if it accepts the PERFORM without END PERFORM. it shouldn't result
in an infinite loop, unless maybe there is a looping GO TO before the
sentence terminating period. Syntactic problems and confusion like this
is why END PERFORM is now required by the standard.
```

###### ↳ ↳ ↳ Re: A fat finger mistake

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2018-04-29T17:11:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f9ccb4e47-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f9ccb4e47-p15@usenetarchives.gap>`
- **References:** `<d9e4d3da-ea70-49ec-be29-66a7e905c25e@googlegroups.com> <gap-2f9ccb4e47-p2@usenetarchives.gap> <gap-2f9ccb4e47-p3@usenetarchives.gap> <gap-2f9ccb4e47-p15@usenetarchives.gap>`

```
On 04/29/2018 04:59 PM, Norman Worth wrote:
› Bill Gunshannon wrote:
›› On 04/28/2018 04:08 AM, pete dashwood wrote:
…[31 more quoted lines elided]…
› is why END PERFORM is now required by the standard.

GNU COBOL does not go into an infinite loop and a display
inserted at the end shows it worked exactly as it should.

bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
