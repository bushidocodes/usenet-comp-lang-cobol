[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Computer Statement Usage

_1 message · 1 participant · 2004-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Computer Statement Usage

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2004-10-13T18:25:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10mrau14cmas99f@corp.supernews.com>`
- **References:** `<IUY8d.8620$Pd2.7721@news02.roc.ny> <yCZ8d.21081$jj2.997385@news20.bellglobal.com> <us89m0proesf23qfn5druc9snmk9nl9n72@4ax.com> <217e491a.0410062301.4f3c7ff8@posting.google.com> <R7Gdner4pp05ovjcRVn-jA@giganews.com> <ck3td7$2778$1@si05.rsvl.unisys.com> <10mqriusnd0dvac@corp.supernews.com> <ckjtcr$rhn$1@si05.rsvl.unisys.com> <10mr4fs562njjd3@corp.supernews.com> <bLgbd.2618771$ic1.269412@news.easynews.com>`

```
Bill, this is no biggie. Mr Stevens mentioned, today, 'that
multiplication is inherently commutative', I recalled an earlier
post concerning 'order of evaluation of conditions', I recalled
the post which mentioned 'rearranging', this led me to 'order
of execution' of arithmetic operations.

Essentially, I was looking at how far down the standard
reaches versus how far up implementor-defined reaches.
You response answered the question.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:bLgbd.2618771$ic1.269412@news.easynews.com...
> Rick,
>    There was (as I recall) an interpretation request and answer for the
'85
> Standard (which I believe applies to NATIVE arithmetic in the '02
Standard).
> The conclusion (NOT in these words) was
>
>   "implementor defined means the implementor may do WHATEVER they want
....
> Although customer reaction PROBABLY requires a 'reasonable' evaluation".
>
…[5 more quoted lines elided]…
> the implementor *must* evaluate A / B first - even in NATIVE arithmetic,
but
> this does NOT mean that they can't take the "precision" of either C or the
> receiving field into consideration when doing the evaluation. FURTHERMORE,
it is
> possible (i.e. conforming - even if not ever done) for the vendor to
ALWAYS
> evaluate "A / B" as "1" and to store the results in a temporary field
which is
> used in the evaluation of  "* C".
>
> The bottom-line (from my perspective) is that *all* arithmetic expressions
in
> the '85 Standard and when ARITHMETIC IS NATIVE is in effect with the '02
> Standard really are TOTALLY implementor defined and that they (the
implementor)
> can do just about ANYTHING they want in this evaluation.
>
…[18 more quoted lines elided]…
> >> > > rearranging the components of an arithmetic expression to cause it
to
> >> > > produce the most precise intermediate results '85 or prior
standards,
> > or
> >> > in
…[26 more quoted lines elided]…
> >> Correct citation, but there's a later reference that makes clear that
it
> >> applies rigorously only to *standard* arithmetic and not *native*
> >> arithmetic.
…[51 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
