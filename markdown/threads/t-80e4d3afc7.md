[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress - Email user from a cgi question.

_8 messages · 5 participants · 1998-04_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### NetExpress - Email user from a cgi question.

- **From:** "neil hayes" <ua-author-2495564@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6gfve5$q0s$1@hermes.is.co.za>`

```

Hi all,

I have a Cobol CGI program that accepts data from my htm form, processes it
and accumulates results. I obtained the user's email address during the
session.

How can I email back the results to the user ?

Do I need any special requirements on the NT Server to facilitate this
service ?

So if anyone can point me in the right direction I'd be grateful.

Neil
Ne··.@sys··o.za
```

#### ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "stephen paul gennard" <ua-author-17075398@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6gfve5$q0s$1@hermes.is.co.za>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za>`

```

Hi Neil,

If you were using UNIX, I would suggest using sendmail, however you are
using NT. So what you need is a little tool for send email to SMTP
server.

I have used a public domain program called "blat", which is very
similar in concept to sendmail on unix.

Blat can be found @ http://gepasi.dbs.aber.ac.uk/softw/Blat.html

>From the COBOL program use: either: CBL_EXEC_RUN_UNIT, x"91" fn 35
or the Win32 API CreateProcess to execute blat.

Hope this helps...


Stephen Gennard, Micro Focus Ltd
Unix Development, N.O.W. Products Group,             Email: s.··.@mfl··o.uk

Neil Hayes wrote:
> 
> Hi all,
…[13 more quoted lines elided]…
> Ne··.@sys··o.za
```

#### ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "david sands" <ua-author-2249128@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6gfve5$q0s$1@hermes.is.co.za>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za>`

```

Hi Neil,

There are a couple of options you could look into:-

1) I have seen this done by creating a text file and then feeding into an
email
system by running a batch file (using X"91" function 35) from your
COBOL prog.
This was done on OS/2 using info from a mainframe and feeding this into
cc-mail.
Check out the docs for your email system to see if you can do this.

2) You could use OLE automation if your email system can support it. There
are some
examples with Net Express of using OLE automation with WORD and EXCEL.

3) You could use the MAPI api to send emails. You will needs Exchange or
some other
mail system that supports MAPI. There is documentation in the WIN32
SDK on the
various API calls that are available. You will need to put in a fair
amount of
investigation of the APIs but you can certainly do it. I know of a
couple of people
who have used this method successfully. The WIN 32 SDK is supplied
with Net
Express.

Hope this helps.

David Sands.



Neil Hayes wrote in message <6gfve5$q0s$1.··.@her··o.za>...
› Hi all,
› 
…[15 more quoted lines elided]…
›
```

##### ↳ ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "smb" <ua-author-13098204@usenetarchives.gap>
- **Date:** 1998-04-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-80e4d3afc7-p3@usenetarchives.gap>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za> <gap-80e4d3afc7-p3@usenetarchives.gap>`

```

"David Sands" wrote:
› Hi Neil,
› 
…[18 more quoted lines elided]…
› SDK is supplied with NetExpress.

Hi Neil,

David is right about (2) and (3) - and if you really want to, you can
combine the two and use Active Messaging (OLE automation wrapper of MAPI).

We're in the process of putting together a demo for our User Conference
in May, showing just that - e-mail me if you're interested.

Steve.
MF Development.

› Neil Hayes wrote in message <6gfve5$q0s$1.··.@her··o.za>...
›› Hi all,
…[10 more quoted lines elided]…
›› So if anyone can point me in the right direction I'd be grateful.
```

###### ↳ ↳ ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "don mccollim" <ua-author-17074221@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-80e4d3afc7-p4@usenetarchives.gap>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za> <gap-80e4d3afc7-p3@usenetarchives.gap> <gap-80e4d3afc7-p4@usenetarchives.gap>`

```

I have successfully used ActiveX controls from Dev-Soft which permit easy access
to SMTP from MF NetExpress. They have a demo package available on their Web
Site. I would be willing to give you my source code if it would be helpful.

Steve Biggs wrote:

› "David Sands"  wrote:
›› Hi Neil,
…[47 more quoted lines elided]…
› E-mail replies: please remove all the "x"s from my address.



Steve Biggs wrote:

› "David Sands"  wrote:
›› Hi Neil,
…[47 more quoted lines elided]…
› E-mail replies: please remove all the "x"s from my address.
```

###### ↳ ↳ ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "don mccollim" <ua-author-17074221@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-80e4d3afc7-p4@usenetarchives.gap>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za> <gap-80e4d3afc7-p3@usenetarchives.gap> <gap-80e4d3afc7-p4@usenetarchives.gap>`

```

I have successfully used ActiveX controls from Dev-Soft which permit easy access
to SMTP from MF NetExpress. They have a demo package available on their Web
Site. I would be willing to give you my source code if it would be helpful.


Steve Biggs wrote:

› "David Sands"  wrote:
›› Hi Neil,
…[47 more quoted lines elided]…
› E-mail replies: please remove all the "x"s from my address.
```

###### ↳ ↳ ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "don mccollim" <ua-author-17074221@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-80e4d3afc7-p4@usenetarchives.gap>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za> <gap-80e4d3afc7-p3@usenetarchives.gap> <gap-80e4d3afc7-p4@usenetarchives.gap>`

```

I have successfully used ActiveX controls from a company called Dev-Soft. They
have an evaluation package available on their WEB Page. I would be willing to
send you my source code if it would be helpful.


Steve Biggs wrote:

› "David Sands"  wrote:
›› Hi Neil,
…[47 more quoted lines elided]…
› E-mail replies: please remove all the "x"s from my address.
```

###### ↳ ↳ ↳ Re: NetExpress - Email user from a cgi question.

- **From:** "don mccollim" <ua-author-17074221@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-80e4d3afc7-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-80e4d3afc7-p4@usenetarchives.gap>`
- **References:** `<6gfve5$q0s$1@hermes.is.co.za> <gap-80e4d3afc7-p3@usenetarchives.gap> <gap-80e4d3afc7-p4@usenetarchives.gap>`

```

I have successfully used ActiveX controls from a company called Dev-Soft. They
have an evaluation package available on their WEB Page. I would be willing to
send you my source code if it would be helpful.


Steve Biggs wrote:

› "David Sands"  wrote:
›› Hi Neil,
…[47 more quoted lines elided]…
› E-mail replies: please remove all the "x"s from my address.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
