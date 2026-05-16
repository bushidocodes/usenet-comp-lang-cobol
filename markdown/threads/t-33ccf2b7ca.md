[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "invalid" source code (END-IF, Next Sentence, and missing periods)

_3 messages · 2 participants · 2001-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-06T18:38:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kemcktsi7ovea0in13apv98ivrcu40mmun@4ax.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <ZtO07.30484$J91.1061302@bgtnsc06-news.ops.worldnet.att.net>`

```
On Thu, 05 Jul 2001 00:25:29 GMT, "Russell Styles" <rwstyles@worldnet.att.net>
wrote:

>
>"Terry Heinze" <terryheinze@prodigy.net> wrote in message
…[24 more quoted lines elided]…
>warnings.

Or you can just use GOBACK in either case (main program or called program).

Of course, this assumes that GOBACK is available for your compiler...

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

#### ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-09T20:33:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A06EC.2DC642D3@Azonic.co.nz>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <ZtO07.30484$J91.1061302@bgtnsc06-news.ops.worldnet.att.net> <kemcktsi7ovea0in13apv98ivrcu40mmun@4ax.com>`

```
Frank Swarbrick wrote:

> Is that right?  I concidered your approach, and threw it out.  What if there are
> 30 fields to validate?  Can you honesty say you would continue your code as show
…[4 more quoted lines elided]…
> avoiding goto's, exit paragraph, etc.

Just perform each validation but from the last to the first:

     PERFORM Validate-field-30
     PERFORM Validate-field-29
     ....
     PERFORM Validate-field-1

The error message will be set for each invalid field but the result will
be that of the 'first' error message (ie the one with the lowest number
here).
```

##### ↳ ↳ Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-09T18:55:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A5275.8A27CCCB@sprynet.com>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <ZtO07.30484$J91.1061302@bgtnsc06-news.ops.worldnet.att.net> <kemcktsi7ovea0in13apv98ivrcu40mmun@4ax.com> <3B4A06EC.2DC642D3@Azonic.co.nz>`

```
Richard Plinston wrote:
> 
> Frank Swarbrick wrote:
…[18 more quoted lines elided]…
> here).

My point, once again, is to totally avoid validating later fields if any
earlier ones are invalid.  (See previous message for justification.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
