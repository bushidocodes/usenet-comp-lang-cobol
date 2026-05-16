[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Logic for missing END-xxx statement syntax

_5 messages · 4 participants · 2006-06_

---

### Logic for missing END-xxx statement syntax

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-06-27T11:14:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7qst8$oq8$01$1@news.t-online.com>`

```
Why has the standard never looked at consistent END-xxx
for statements ?
eg, Why isn't there (following is incomplete) -
END-CANCEL
END-CLOSE
END-INITIALIZE
END-OPEN
END-SORT
etc.

Roger
```

#### ↳ Re: Logic for missing END-xxx statement syntax

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-06-27T09:17:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12a2c2oo7pq9i81@corp.supernews.com>`
- **References:** `<e7qst8$oq8$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e7qst8$oq8$01$1@news.t-online.com...
> Why has the standard never looked at consistent END-xxx
> for statements ?
…[6 more quoted lines elided]…
> etc.

These scope terminators are unncessary. Some on
J4 have expressed a desire to avoid the unncessary;
however, any imlementor could add these as an
extension (though I have doubts that many programmers
would actually use them, even if they were available).
```

#### ↳ Re: Logic for missing END-xxx statement syntax

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-06-27T08:03:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gke2a29947fum99f5a25ithrn0up3dl55g@4ax.com>`
- **References:** `<e7qst8$oq8$01$1@news.t-online.com>`

```
On Tue, 27 Jun 2006 11:14:12 +0200, "Roger While" <simrw@sim-basis.de>
wrote:

>Why has the standard never looked at consistent END-xxx
>for statements ?
…[6 more quoted lines elided]…
>etc.

Show me examples where these would be useful.
```

#### ↳ Re: Logic for missing END-xxx statement syntax

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-06-27T12:27:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151436459.543293.214870@p79g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<e7qst8$oq8$01$1@news.t-online.com>`
- **References:** `<e7qst8$oq8$01$1@news.t-online.com>`

```

Roger While wrote:
> Why has the standard never looked at consistent END-xxx
> for statements ?
…[5 more quoted lines elided]…
> END-SORT

It is consistent in that there is a scope terminator available for
every conditional statement to make it imperitive. The statements you
mention cannot be conditional. Where the use of a statement that could
be conditional but does not include any of the phrases that would make
it so then the scope terminator should not be used.

So:         ADD 1 TO X END-ADD

should be an error.  The terminator is only used when it is
conditional:

              ADD 1 TO X ON SIZE ERROR dosomething END-ADD

as there is no conditional clause for CANCEL then there can be no use
for END-CANCEL. etc.

Consider:

              ADD 1 TO X
                      ON SIZE ERROR
                              ADD 1 TO Error-Count
              END-ADD

Which ADD do you scope terminate ?
```

##### ↳ ↳ Re: Logic for missing END-xxx statement syntax

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-06-27T13:35:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qs13a2hhnu2ocq24p8kvtm8hhs2ud46iiu@4ax.com>`
- **References:** `<e7qst8$oq8$01$1@news.t-online.com> <1151436459.543293.214870@p79g2000cwp.googlegroups.com>`

```
On 27 Jun 2006 12:27:39 -0700, "Richard" <riplin@Azonic.co.nz> wrote:

>should be an error.  The terminator is only used when it is
>conditional:
…[13 more quoted lines elided]…
>Which ADD do you scope terminate ?

Hmmm, you just came up with an argument for END-ADD without a
conditional, so that I can code for Joe NewProgrammer with a pair of
END-ADDs.    On the other hand, in-line performs are closer to a
universal standard here.    Which work for people such as myself who
end sentences with periods.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
