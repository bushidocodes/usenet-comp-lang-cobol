[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# define for pathway server

_2 messages · 2 participants · 2004-10_

---

### define for pathway server

- **From:** Tom <nomail@pleaseno.invalid>
- **Date:** 2004-10-06T23:01:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9l8m0h32k88khf11t1prs4a1g7mfjgp5v@4ax.com>`

```
Is there any way to make a define known to a serverprocess other than
through the serverclass-definition ? 

I want the define to be available to all serverclasses in all pathways
of an application. 

I know a definename is normally resolved in the structure of a
filename. Is it possible to have it resolved to a text longer than 8
chars (what i get using the class map define, stripping the last part
of it). i need this to know to what serverclass I need to go to.  

Exploitation doesn't want to deal with params for this, though it's
probably the best way to reolve this, only you need to specify this
with every serverclass in every pathway.


regards,

Tom
```

#### ↳ Re: define for pathway server

- **From:** Jeff Lanam <jeff-dot-lanam@hp-dot-com-not.net>
- **Date:** 2004-10-07T19:47:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<657bm0dcvdhgmh56c84ab024615mb1vrc4@4ax.com>`
- **References:** `<b9l8m0h32k88khf11t1prs4a1g7mfjgp5v@4ax.com>`

```
On Wed, 06 Oct 2004 23:01:24 +0200, Tom <nomail@pleaseno.invalid>
wrote:

>Is there any way to make a define known to a serverprocess other than
>through the serverclass-definition ? 
…[11 more quoted lines elided]…
>with every serverclass in every pathway.

I assume you are talking about HP NonStop Kernal (aka Tandem).
You would be better off asking this question in comp.sys.tandem;
this really isn't a question about COBOL.  There are a lot of people
over there who can help you.  (Sorry I'm not one of them--I don't know
Pathway.)


Jeff Lanam     HP NonStop COBOL Project  INCITS/J4
NonStop Enterprise Division
Hewlett-Packard
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
