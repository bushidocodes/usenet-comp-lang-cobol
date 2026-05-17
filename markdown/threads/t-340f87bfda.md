[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mf cobol and pointers

_5 messages · 4 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Mf cobol and pointers

- **From:** "sver..." <ua-author-8015530@usenetarchives.gap>
- **Date:** 1998-03-12T05:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e8db4$4j5$1@nnrp1.dejanews.com>`

```

Question :

I have a structure :

01 test-struct.
05 param1 pic x(10).
05 param2 pic x(10).


application 1 fills this structure (actually it fills a (DB2) SQLDA structure
but this structure is just a test-case) and then passes a pointer to this
structure to application 2.

Now, given that the 2nd app only has a pointer to this structure, how can I
read the individual fields param1 and param2 from this structure ? Is there a
way to redefine the pointer to the above structure ?

Any help is appreciated,
Simon Verzijl
Devote

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Mf cobol and pointers

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-340f87bfda-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6e8db4$4j5$1@nnrp1.dejanews.com>`
- **References:** `<6e8db4$4j5$1@nnrp1.dejanews.com>`

```


sve··.@hot··l.com wrote in message <6e8db4$4j5$1.··.@nnr··s.com>...
› Question :
› 
…[22 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading

Let's say that the called program gets a pointer as the only passed field,
Then you would code

Linkage Section.
01 Passed-Pointer Usage Pointer.
01 Linkage-Section-Reference-to-test-struct.
05 param1 pic x(10).
05 param2 pic x(10).
Procedure Division Using Passed-Pointer
Linkage-Section-Reference-to-test-struct.

Set Address of Linkage-Section-Reference-to-test-struct
to Passed-Pointer.

And then you will have addressability to the original group and subfields
from the subprogram's Linkage Section. (and actually you could define the
group field anyway you want in the subprogram)

P.S. Note that the calling program only passes one parameter, but the
subprogram declares TWO 01-levels in both the Linkage Section and the
PROCEDURE DIVISION USING statements. (This violates the normal rules, but is
how this works.)
```

##### ↳ ↳ Re: Mf cobol and pointers

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-340f87bfda-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-340f87bfda-p2@usenetarchives.gap>`
- **References:** `<6e8db4$4j5$1@nnrp1.dejanews.com> <gap-340f87bfda-p2@usenetarchives.gap>`

```

William M. Klein wrote:

› Let's say that the called program gets a pointer as the only passed field,
› Then you would code
…[19 more quoted lines elided]…
› how this works.)

What is the violation? TWO in linkage? Or the difference between number of args
between calling and called prog?

I thought for sure that the 01-lever did not need to be in the using phrase. The
compiler sees two separate 01 levels and allocates for each a BLL cell (or
equivalent, I don't know the MF jargon for this). The set address then fills the
bll for the 2nd 01-level.

Anyway this is an extension! Implementation may very among vendors. In the next
standard this will be possible. Including a test for presence/absence. (IF ...
OMITTED (how negative of the committee, IF INCLUDED/PRESENT sounds much more
positive))

The Frog
```

###### ↳ ↳ ↳ Re: Mf cobol and pointers

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-340f87bfda-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-340f87bfda-p3@usenetarchives.gap>`
- **References:** `<6e8db4$4j5$1@nnrp1.dejanews.com> <gap-340f87bfda-p2@usenetarchives.gap> <gap-340f87bfda-p3@usenetarchives.gap>`

```



Cobol Frog (Huib Klink) wrote in message <350··.@I··.nl>...
.much snippage<
› 
› What is the violation? TWO in linkage? Or the difference between number of
…[9 more quoted lines elided]…
› 
It is definitely an extension (violation of the Standard and the USUAL way
of coding even with extensions) to have the number of parameters passed
differ (especially be LESS) from the number in the PROCEDURE DIVISION USING
phrase.

As for not putting the second 01-level in the USING phrase, this does work
(sometimes) but not always. It is particularly bad if you have any ENTRY
USING statements (another extension allowed by both IBM and MF. You must be
used to IBM as you mention BLL-cells.) If you omit the second 01-level in
the USING, this will work sometimes, but not always - if you put it there,
it will ALWAYS work.
```

###### ↳ ↳ ↳ Re: Mf cobol and pointers

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-340f87bfda-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-340f87bfda-p3@usenetarchives.gap>`
- **References:** `<6e8db4$4j5$1@nnrp1.dejanews.com> <gap-340f87bfda-p2@usenetarchives.gap> <gap-340f87bfda-p3@usenetarchives.gap>`

```

Cobol Frog (Huib Klink) wrote:
› 
› William M. Klein wrote:
…[13 more quoted lines elided]…
››               to Passed-Pointer.

Why don't you just use the pointer like it was intended?

linkage section.
01 passed-pointer usage pointer.
01 l-s-r-t-t-s.....

procedure division using passed-pointer.

set address of linkage-section-referenced-to-test-struct to
passed-pointer

the you have full addressability and everything without the cryptic
headache. And no calling
program will ever make the mistake of doing:

call the-prog using
address of some-item
some-item
end-call

when they should just do:

call the-prog using address of some-item end-call
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
