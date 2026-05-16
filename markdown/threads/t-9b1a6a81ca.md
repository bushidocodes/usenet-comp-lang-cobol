[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol & web

_3 messages · 3 participants · 1999-04_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### cobol & web

- **From:** "Vyacheslav Danovich" <vdanovich@empireone.net>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W3pR2.1222$fl5.206241826@dca1-nnrp1.news.digex.net>`

```
I've got an existing multiple file program written in AcuCobol 4.0.  Is
there any way to put in on the web?
```

#### ↳ Re: cobol & web

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f58mh$3g5$1@news.cerf.net>`
- **References:** `<W3pR2.1222$fl5.206241826@dca1-nnrp1.news.digex.net>`

```
Vyacheslav Danovich wrote in message ...
>I've got an existing multiple file program written in AcuCobol 4.0.  Is
>there any way to put in on the web?

Acucobol has plugin capability for browsers. See www.acucorp.com for
details.

Cheesle
```

#### ↳ Re: cobol & web

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371744f1.5819911@news.enter.net>`
- **References:** `<W3pR2.1222$fl5.206241826@dca1-nnrp1.news.digex.net>`

```
"Vyacheslav Danovich" <vdanovich@empireone.net> wrote:

>I've got an existing multiple file program written in AcuCobol 4.0.  Is
>there any way to put in on the web?
>
>

Vyacheslav:

Do you want to put it "on the web" or do you want to put it "on the
Internet?"  I know this question sounds a bit strange, but there
really is a difference.

In our efforts to place a COBOL user interface "on the web" we ran
into so many problems...not with the COBOL, but with using a world
wide browser as a user interface mechanism.  To put it bluntly...world
wide web browsers as commercial application user interface
environments really stink.

Sometimes it IS necessary to use a web based "front end" for your
application.  My personal "rule of thumb" is that when you want to
reach millions of people with your application, then going with a web
browser interface is probably the way to go...BUT if you have a
specific group of people you want to have access to your application,
then you really should look at other methods of "front ending" your
COBOL application.

It is possible to run your COBOL application as a "thin client"
application across TCP/IP which means that you are running it NOT
through a web server/web browser environment, but bypassing the entire
web and running it in a much MORE native and much less interpretive
manner.

You avoid the instabilities and massive overhead of web browsers as
well as the lack of control of end users installing the beta version
of the latest and greatest browser.

Although we provide thin client enabling tools for COBOL, we are by no
means the only ones who do this.  I think that Acucobol can provide
you with thin client tools and you can also write your own thin client
"front end" to your COBOL application using products such as Visual
Basic or Delphi.

I just wanteed to hop up on the old soapbox and get people to start
thinking about the fact that just because you want to run an
application across the Internet, does NOT necessarily mean you have to
use the world wide web to do so.



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
