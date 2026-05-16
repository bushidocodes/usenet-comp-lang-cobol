[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM OSVS reference modification

_4 messages · 3 participants · 2004-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### IBM OSVS reference modification

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-24T22:04:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com>`

```
When a program is compiled by Micro Focus with the OSVS option on,
reference modification is accepted in most places but not in
conditionals.

Valid: MOVE A(1:1) TO B

Invalid: IF A(1:1) = '1' ...

Where did IBM get this notion? Is it simply a bug?
```

#### ↳ Re: IBM OSVS reference modification

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-11-24T20:48:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-1D28CE.20484624112004@knology.usenetserver.com>`
- **References:** `<n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com>`

```
In article <n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com>,
 Robert Wagner <spamblocker-robert@wagner.net> wrote:

> When a program is compiled by Micro Focus with the OSVS option on,
> reference modification is accepted in most places but not in
…[6 more quoted lines elided]…
> Where did IBM get this notion? Is it simply a bug?

I'm not sure what the OSVS option is supposed to emulate -- but that 
notation in conditionals works in the recently shipping (last 10 years 
or so) compilers.
```

#### ↳ Re: IBM OSVS reference modification

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-26T00:17:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Cupd.5121167$ic1.479672@news.easynews.com>`
- **References:** `<n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com>`

```
The OSVS compiler directive is a "dialect" directive that ONLY (or very 
close to only)  impacts reserverd words .

To  determine if SYNTAX is correct for emulating IBM's OS/VS COBOL compiler, 
use the FLAG(OSVS) directive.

"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message 
news:n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com...
> When a program is compiled by Micro Focus with the OSVS option on,
> reference modification is accepted in most places but not in
…[6 more quoted lines elided]…
> Where did IBM get this notion? Is it simply a bug?
```

##### ↳ ↳ Re: IBM OSVS reference modification

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-26T04:54:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdddq05mbk0k8oedsm3s3r367s0n7f996g@4ax.com>`
- **References:** `<n51aq0146huh06ajafv639cmjmkh8dl76s@4ax.com> <0Cupd.5121167$ic1.479672@news.easynews.com>`

```
Thanks for the research. The option I used was $SET OSVS, not
FLAG(OSVS). The compiler does what the manual says, here:

http://supportline.microfocus.com/supportline/documentation/books/sx40sp1/lhpdf608.htm#0002


On Fri, 26 Nov 2004 00:17:00 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>The OSVS compiler directive is a "dialect" directive that ONLY (or very 
>close to only)  impacts reserverd words .
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
