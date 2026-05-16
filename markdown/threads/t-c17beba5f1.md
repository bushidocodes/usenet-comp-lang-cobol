[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Computer Statement Usage

_3 messages · 2 participants · 2004-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Computer Statement Usage

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-10-12T09:47:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckh1rr$1unj$1@si05.rsvl.unisys.com>`
- **References:** `<IUY8d.8620$Pd2.7721@news02.roc.ny> <35Z8d.2192085$ic1.223442@news.easynews.com> <8a2d426e.0410062107.51f6c06c@posting.google.com> <ck4cvo$2hn5$1@si05.rsvl.unisys.com> <8a2d426e.0410091643.138c08c3@posting.google.com> <cke9db$35f$1@si05.rsvl.unisys.com> <8a2d426e.0410120803.57ee92fe@posting.google.com>`

```
OK, then, my problem is that I don't see the value, in a Unisys MCP
environment, of changing
    COMPUTE F = (A/B) * C.
to
    COMPUTE F = (A/B) * C + SEE-NOTE-ABOVE.

What is it that the user is supposed to gain *in the general case*?   I
certainly don't see an advantage *in our case*.    All I see is,
paraphrasing what an automotive-buff friend once commented about the
engineering style of a particular manufacturer, "a maximally-complicated
solution to a nonexistent problem".

*As I see it* the "problem" only exists when the expression is evaluated in
a certain way.  If the expression is evaluated in a different way, the "one
size fits all" solution not only might not fit (as I believe is the case in
our environment), it might even precipitate worse precision problems through
the scaling process than the original code, and it is almost guaranteed to
degrade performance.

You wrote "Does anybody see a downside?  I'd appreciate your feedback."

I have replied "Yes" (more than once) to the question, and find the response
"apparently not" to the assertion appropriate.

    -Chuck Stevens
```

#### ↳ Re: Computer Statement Usage

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-10-12T22:22:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0410122122.127b36dd@posting.google.com>`
- **References:** `<IUY8d.8620$Pd2.7721@news02.roc.ny> <35Z8d.2192085$ic1.223442@news.easynews.com> <8a2d426e.0410062107.51f6c06c@posting.google.com> <ck4cvo$2hn5$1@si05.rsvl.unisys.com> <8a2d426e.0410091643.138c08c3@posting.google.com> <cke9db$35f$1@si05.rsvl.unisys.com> <8a2d426e.0410120803.57ee92fe@posting.google.com> <ckh1rr$1unj$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:<ckh1rr$1unj$1@si05.rsvl.unisys.com>...
> OK, then, my problem is that I don't see the value, in a Unisys MCP
> environment, of changing
…[8 more quoted lines elided]…
> solution to a nonexistent problem".

Oh yeah, I forgot to mention not to use the solution if your compiler
doesn't produce the problem in the first place. Silly me.
> 
> *As I see it* the "problem" only exists when the expression is evaluated in
…[9 more quoted lines elided]…
> "apparently not" to the assertion appropriate.

The solution was NOT proposed as a solution to those compiler
environments that haven't experienced the problem.
> 

>     -Chuck Stevens
```

##### ↳ ↳ Re: Computer Statement Usage

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-10-13T09:25:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckjkul$m2q$1@si05.rsvl.unisys.com>`
- **References:** `<IUY8d.8620$Pd2.7721@news02.roc.ny> <35Z8d.2192085$ic1.223442@news.easynews.com> <8a2d426e.0410062107.51f6c06c@posting.google.com> <ck4cvo$2hn5$1@si05.rsvl.unisys.com> <8a2d426e.0410091643.138c08c3@posting.google.com> <cke9db$35f$1@si05.rsvl.unisys.com> <8a2d426e.0410120803.57ee92fe@posting.google.com> <ckh1rr$1unj$1@si05.rsvl.unisys.com> <8a2d426e.0410122122.127b36dd@posting.google.com>`

```

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0410122122.127b36dd@posting.google.com...

> The solution was NOT proposed as a solution to those compiler
> environments that haven't experienced the problem.

Well, part of my problem is that it looks to me like the only compilers that
I'd expect to experience the problem in this case are those whose authors
seem to have been blissfully unaware that multiplication is inherently
commutative, something I was taught long before I ever saw a computer or a
compiler!

Guess my point is:  Why is this the *user's* problem to solve?  I'd be
yelling at the vendor if I had to go through gyrations like that!

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
