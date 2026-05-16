[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol array editing output

_11 messages · 4 participants · 2003-12_

---

### Re: cobol array editing output

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-10T14:00:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br852g$5id$1@si05.rsvl.unisys.com>`

```

I mistyped.  To Judson McClendon's .

> > However,the compiler must generate code to convert between
> > subscript and offset when a SET or compare is done between integer and
> > index data items.

I responded

> I think you mean integers and index-names in standard-speak.  ...
> The results of comparing a number ... against an index-name
> are undefined.

That should have been

> I think you mean integers and index-names in standard-speak. ...
> The results of comparing a number ... against an index data item
> are undefined.

Index data items -- i.e., items declared USAGE IS INDEX -- are of limited
utility, IMHO.

    -Chuck Stevens
```

#### ↳ Re: cobol array editing output

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-11T07:02:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031211080332.635$tn@news.newsreader.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> Index data items -- i.e., items declared USAGE IS INDEX -- are of limited
> utility, IMHO.

Yes, and even dangerous. Much better to declare additional indexes to
the same table.
```

#### ↳ Re: cobol array editing output

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-12T11:31:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd8f0a8_8@news.athenanews.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:br852g$5id$1@si05.rsvl.unisys.com...
>
> Index data items -- i.e., items declared USAGE IS INDEX -- are of limited
> utility, IMHO.
>
So how would you (efficiently) pass a table and its current reference to a
called subprogram?

Pete.
```

##### ↳ ↳ Re: cobol array editing output

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-11T15:36:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<brav27$27td$1@si05.rsvl.unisys.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com>`

```
I didn't write that they were of *no* utility, I said they were of *limited*
utility.

    -Chuck Stevens

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3fd8f0a8_8@news.athenanews.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
> news:br852g$5id$1@si05.rsvl.unisys.com...
> >
> > Index data items -- i.e., items declared USAGE IS INDEX -- are of
limited
> > utility, IMHO.
> >
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: cobol array editing output

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-12T23:54:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fd99ea9_1@news.athenanews.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:brav27$27td$1@si05.rsvl.unisys.com...
> I didn't write that they were of *no* utility, I said they were of
*limited*
> utility.
>
So how would you (efficiently) pass a table and its current reference to a
called subprogram?

Pete.
```

###### ↳ ↳ ↳ Re: cobol array editing output

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-12-12T08:56:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<brcs0c$id8$1@si05.rsvl.unisys.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3fd99ea9_1@news.athenanews.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
…[9 more quoted lines elided]…
>

I'd probably be inclined to SET a numeric data item to the index-name in the
caller, and pass that to the called subprogram, where I SET the local
index-name to that numeric data item.  .

Since range checks have to be performed on the SET that would occur in the
called subprogram anyway, and presuming that the implementor has provided a
USAGE that corresponds in format to that which would be used for an index,
it seems to me unlikely that the SET of an index-name to an index data item
would differ *significantly* in performance from the SET of an index-name to
a numeric data item.   I see maybe a couple of  math ops difference.  Yes,
there is a difference, but I'm not convinced that difference is likely to be
significant compared to everything else the called program would be expected
to do.  And if all the called subprogram does is a single reference to the
table (or anything else trivial enough to make the couple of math ops
measurable, to say nothing of significant), getting rid of the called
subprogram altogether and doing the work "in situ" would improve performance
even more.

When an index-name is set to the contents of an index data item, and both
the table and the index data item are passed in, there's a presumption that
the index data item *was* properly set to the table to begin with.  No
conversion takes place in this case.  I'm not sure I'm comfortable with that
presumption and its consequences, particularly when the user has turned off
range checking on indices.  I'd prefer to pass in a *subscript* and cause
both the conversion and the range check to occur during the SET that the
called subprogram executes.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: cobol array editing output

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-13T11:08:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fda3cb3_5@news.athenanews.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com> <brcs0c$id8$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:brcs0c$id8$1@si05.rsvl.unisys.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3fd99ea9_1@news.athenanews.com...
…[7 more quoted lines elided]…
> > So how would you (efficiently) pass a table and its current reference to
a
> > called subprogram?
> >
…[3 more quoted lines elided]…
> I'd probably be inclined to SET a numeric data item to the index-name in
the
> caller, and pass that to the called subprogram, where I SET the local
> index-name to that numeric data item.  .
>
> Since range checks have to be performed on the SET that would occur in the
> called subprogram anyway, and presuming that the implementor has provided
a
> USAGE that corresponds in format to that which would be used for an index,
> it seems to me unlikely that the SET of an index-name to an index data
item
> would differ *significantly* in performance from the SET of an index-name
to
> a numeric data item.   I see maybe a couple of  math ops difference.  Yes,
> there is a difference, but I'm not convinced that difference is likely to
be
> significant compared to everything else the called program would be
expected
> to do.  And if all the called subprogram does is a single reference to the
> table (or anything else trivial enough to make the couple of math ops
> measurable, to say nothing of significant), getting rid of the called
> subprogram altogether and doing the work "in situ" would improve
performance
> even more.
>
> When an index-name is set to the contents of an index data item, and both
> the table and the index data item are passed in, there's a presumption
that
> the index data item *was* properly set to the table to begin with.  No
> conversion takes place in this case.  I'm not sure I'm comfortable with
that
> presumption and its consequences, particularly when the user has turned
off
> range checking on indices.  I'd prefer to pass in a *subscript* and cause
> both the conversion and the range check to occur during the SET that the
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: cobol array editing output

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-13T11:11:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fda3d70_5@news.athenanews.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com> <brcs0c$id8$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:brcs0c$id8$1@si05.rsvl.unisys.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3fd99ea9_1@news.athenanews.com...
…[7 more quoted lines elided]…
> > So how would you (efficiently) pass a table and its current reference to
a
> > called subprogram?
> >
…[3 more quoted lines elided]…
> I'd probably be inclined to SET a numeric data item to the index-name in
the
> caller, and pass that to the called subprogram, where I SET the local
> index-name to that numeric data item.  .
>
> Since range checks have to be performed on the SET that would occur in the
> called subprogram anyway, and presuming that the implementor has provided
a
> USAGE that corresponds in format to that which would be used for an index,
> it seems to me unlikely that the SET of an index-name to an index data
item
> would differ *significantly* in performance from the SET of an index-name
to
> a numeric data item.   I see maybe a couple of  math ops difference.  Yes,
> there is a difference, but I'm not convinced that difference is likely to
be
> significant compared to everything else the called program would be
expected
> to do.  And if all the called subprogram does is a single reference to the
> table (or anything else trivial enough to make the couple of math ops
> measurable, to say nothing of significant), getting rid of the called
> subprogram altogether and doing the work "in situ" would improve
performance
> even more.
>
> When an index-name is set to the contents of an index data item, and both
> the table and the index data item are passed in, there's a presumption
that
> the index data item *was* properly set to the table to begin with.  No
> conversion takes place in this case.  I'm not sure I'm comfortable with
that
> presumption and its consequences, particularly when the user has turned
off
> range checking on indices.  I'd prefer to pass in a *subscript* and cause
> both the conversion and the range check to occur during the SET that the
> called subprogram executes.
>
Thank you. A very revealing response.

Not being an adherent of the paranoid programming school, I would (and do)
use an index data item. It is set correctly by the calling program and can
be used with confidence by the called program. That's what they're for.

Pete.

Pete.
```

###### ↳ ↳ ↳ Re: cobol array editing output

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-13T07:50:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031213085204.214$Vh@news.newsreader.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com> <brcs0c$id8$1@si05.rsvl.unisys.com> <3fda3d70_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> Not being an adherent of the paranoid programming school, ...

Ah! But are we being paranoid enough? ;-)
```

###### ↳ ↳ ↳ Set numeric value to INDEX was Re: cobol array editing output

_(reply depth: 5)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-12-12T19:08:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<broiv2$rh5$1@news.eusc.inter.net>`
- **In-Reply-To:** `<brcs0c$id8$1@si05.rsvl.unisys.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com> <brcs0c$id8$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message 
> news:3fd99ea9_1@news.athenanews.com...
…[49 more quoted lines elided]…
> 
The set numeric item to INDEX involves a divide thus would be somewhat
expensive.  Using an USAGE INDEX item means that the set can generate 
simple move or load store combinations rather than using multiply and 
divide.  Of course the penalty on modern systems is far less in the 
overall scheme of things than it was 10 - 15 years ago but it doe add an 
inefficiency in what may be a compute intensive operation depending on 
what the sub-routine is doing (or the caller).
```

###### ↳ ↳ ↳ Re: Set numeric value to INDEX was Re: cobol array editing output

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-17T06:10:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031217071207.273$Km@news.newsreader.com>`
- **References:** `<br852g$5id$1@si05.rsvl.unisys.com> <3fd8f0a8_8@news.athenanews.com> <brav27$27td$1@si05.rsvl.unisys.com> <3fd99ea9_1@news.athenanews.com> <brcs0c$id8$1@si05.rsvl.unisys.com> <broiv2$rh5$1@news.eusc.inter.net>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:
> >
> > Since range checks have to be performed on the SET that would occur
…[8 more quoted lines elided]…
> > expected to do.

I agree. On architectures I am familiar with, the overhead of calling a
procedure or function is considerably greater than a couple of math ops,
not including any other processing the procedure or function does.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
