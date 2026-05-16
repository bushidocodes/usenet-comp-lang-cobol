[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# If you were inventing CoBOL...

_5 messages · 2 participants · 2004-09_

---

### Re: If you were inventing CoBOL...

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-09-09T10:27:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chq3ql$s0o$1@si05.rsvl.unisys.com>`

```
A correction to my response:

Robert Wagner wrote:

> > As a practical matter, the callee need not distinguish between
> > REFERENCE and CONTENT, except modifying CONTENT will not produce
> > expected results.

I responded:

> Yes, that's correct according to the 2002 standard.

Actually, no, that's not.

If a called program modifies a parameter that was passed to it with BY
REFERENCE, the value is modified in the calling program.  A MODIFIED value
in the called program is the expected result.

If a called program modifies a parameter that was passed to it BY CONTENT,
that parameter is *not* modified in the calling program.  An UNMODIFIED
value in the calling program is the expected result.

"Modifying CONTENT" will produce expected results if your expectations of
those results are reasonable.

    -Chuck Stevens
```

#### ↳ Re: If you were inventing CoBOL...

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-09T19:20:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4b1k05ig9p7td27942dserkso614kc8kq@4ax.com>`
- **References:** `<chq3ql$s0o$1@si05.rsvl.unisys.com>`

```
On Thu, 9 Sep 2004 10:27:49 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>A correction to my response:
>
…[21 more quoted lines elided]…
>those results are reasonable.

There is no reason to modify data passed BY CONTENT. If the callee
does so, it has a false expectation that changes are being passed back
to the caller.
```

##### ↳ ↳ Re: If you were inventing CoBOL...

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-09-09T12:25:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chqao7$10eh$1@si05.rsvl.unisys.com>`
- **References:** `<chq3ql$s0o$1@si05.rsvl.unisys.com> <h4b1k05ig9p7td27942dserkso614kc8kq@4ax.com>`

```

"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:h4b1k05ig9p7td27942dserkso614kc8kq@4ax.com...

> There is no reason to modify data passed BY CONTENT.

There isn't?  Forty-five years of ALGOL programs that used parameters as
local variables once they'd examined the value have been Doing It Wrong???

> If the callee does so, it has a false expectation that changes are being
passed back
> to the caller.

No, in fact, it may be with the *correct and specific* expectation that the
changes made to the parameter will *not* be passed back to the caller!
Once the callee has made use of the value as passed from the caller, the
callee can do whatever he wants with the variable *without* fear of damage
upstream!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: If you were inventing CoBOL...

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-09T22:53:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72n1k0llcn2jmf2hcqh551cbqt56l9mg9s@4ax.com>`
- **References:** `<chq3ql$s0o$1@si05.rsvl.unisys.com> <h4b1k05ig9p7td27942dserkso614kc8kq@4ax.com> <chqao7$10eh$1@si05.rsvl.unisys.com>`

```
On Thu, 9 Sep 2004 12:25:58 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
…[5 more quoted lines elided]…
>local variables once they'd examined the value have been Doing It Wrong???

Is memory so expense they can't afford their own local variables?

>> If the callee does so, it has a false expectation that changes are being
>passed back
…[6 more quoted lines elided]…
>upstream!

After finding the value in foo is wrong, I search for all places where
foo is modified. Now, I have to notice whether foo was passed BY
CONTENT? I don't think so.

We potentially had the same problem before. A program could modify an
output record, then never write it. In all the code I've worked with,
I can't recall ever seeing that happen .. at least on purpose. If I
did catch someone doing that, I'd accuse him or her of deceptive
programming and insist it be changed.
```

###### ↳ ↳ ↳ Re: If you were inventing CoBOL...

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-09-09T16:48:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chqq57$1aqt$1@si05.rsvl.unisys.com>`
- **References:** `<chq3ql$s0o$1@si05.rsvl.unisys.com> <h4b1k05ig9p7td27942dserkso614kc8kq@4ax.com> <chqao7$10eh$1@si05.rsvl.unisys.com> <72n1k0llcn2jmf2hcqh551cbqt56l9mg9s@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message
news:72n1k0llcn2jmf2hcqh551cbqt56l9mg9s@4ax.com...

> Is memory so expense they can't afford their own local variables?

They *can*, but they are not obligated to.

> After finding the value in foo is wrong, I search for all places where
> foo is modified. Now, I have to notice whether foo was passed BY
> CONTENT? I don't think so.

No, you don't.  You might have to notice whether it was passed *by
reference*, but it's not gonna be wrong in the caller on account of the
callee if the caller passed it BY CONTENT!  You have to look for the cases
in which it *isn't* passed by content!

> We potentially had the same problem before. A program could modify an
> output record, then never write it. In all the code I've worked with,
> I can't recall ever seeing that happen .. at least on purpose. If I
> did catch someone doing that, I'd accuse him or her of deceptive
> programming and insist it be changed.

Well, ain't we pontifical.  Many is the time I've successfully and correctly
tested a database data-set formatting problem by diddling with the
information in the data set record without ever having opened the data base.
Guess you want the tests to run longer than they have to ...

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
