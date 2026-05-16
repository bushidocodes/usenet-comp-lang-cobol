[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Web Service

_4 messages · 2 participants · 2007-09_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Web Service

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-09-25T05:49:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190724569.754533.223370@k79g2000hse.googlegroups.com>`

```
Tried several web services in my Cobol (microfocus) program using an
example URL link as below;

http://myxml.thisissample/serverside.WSDL

and it works all the time. The server-side (SOAP) WSDL file will do
the thing for me. But just lately a friend of mine ask if I could do
the same for a .NET framework server that has the below URL;

http://myxml.thisissample/serverside.ASMX

Considering I passed the "required" function with fields or parameters
in my Cobol program, and INVOKE the url with "asmx" extension, will it
produce the same output as my wsdl file?
```

#### ↳ Re: Web Service

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-09-27T19:34:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190946864.180826.22940@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1190724569.754533.223370@k79g2000hse.googlegroups.com>`
- **References:** `<1190724569.754533.223370@k79g2000hse.googlegroups.com>`

```
Just to rephrase my query above, it may not be clear.

I usually invoke SOAP (Web service) using WSDL file extension, now a
friend of mine says that they have a .NET platform server that uses
ASMX file extension instead.

Do not know exactly how ASMX works, search the internet about it and
it tells me it is the same technology as WSDL SOAP but the problem is
how to access ASMX. Would it be the same as the WSDL file extension?

And another thing, what is the maximum data (in length/bytes) that can
be pass to a WSDL?

Reference topic here: Web Service (Retouch)
```

##### ↳ ↳ Re: Web Service

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-28T07:43:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uF6Li.67235$Y7.10525@bignews3.bellsouth.net>`
- **References:** `<1190724569.754533.223370@k79g2000hse.googlegroups.com> <1190946864.180826.22940@d55g2000hsg.googlegroups.com>`

```
"Rene_Surop" <infodynamics_ph@yahoo.com> wrote:
> Just to rephrase my query above, it may not be clear.
>
…[11 more quoted lines elided]…
> Reference topic here: Web Service (Retouch)

I'm not a .NET guru, but I have done some web service applications with
Visual Studio 2005. ASMX is simply the web service extension for ASP.NET
web service pages, as ASPX is the extension for ASP.NET web pages. You
still use WSDL, SOAP and XML in the same way. Other than the "ASPX" in
the web service URL, I don't think a web service client would know the
difference. Hope this helps.
```

###### ↳ ↳ ↳ Re: Web Service

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-09-28T19:32:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1191033173.750387.195040@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<uF6Li.67235$Y7.10525@bignews3.bellsouth.net>`
- **References:** `<1190724569.754533.223370@k79g2000hse.googlegroups.com> <1190946864.180826.22940@d55g2000hsg.googlegroups.com> <uF6Li.67235$Y7.10525@bignews3.bellsouth.net>`

```
Thanks Judson.

Im going to  try executing my Cobol code anyhow by invoking an "ASMX"
file extension instead of the usual WSDL url file that I'm using. I
wont change Cobol codes for the meantime.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
