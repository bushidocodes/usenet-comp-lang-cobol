[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL CGI on Aix with apache

_7 messages · 3 participants · 2001-08_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### COBOL CGI on Aix with apache

- **From:** "Jack" <keziah.jones@caramail.com>
- **Date:** 2001-08-06T11:03:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr>`

```
I'm now porting an AS/400 CGI in COBOL to an AIX server.
So, I'm looking for ressources about making a CGI in COBOL on Unix AIX with
apache.
```

#### ↳ Re: COBOL CGI on Aix with apache

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-07T00:53:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b6e928b_9@goliath.newsgroups.com>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr>`

```
Can you give us some more details as to how the CGI interface is
implemented?

Are you making calls to a COBOL "blind" interface (It doesn't matter whether
it is the Windows CGI or the Standard one) or are you making your own direct
CGI calls to the Unix CGI (using STDIO), or to the Windows CGI using direct
calls...

What COBOL are you using?

More information is required before help can be offered...

Pete.

"Jack" <keziah.jones@caramail.com> wrote in message
news:y0tb7.5927$Yy2.32585@tengri.easynet.fr...
> I'm now porting an AS/400 CGI in COBOL to an AIX server.
> So, I'm looking for ressources about making a CGI in COBOL on Unix AIX
with
> apache.
>
>



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

##### ↳ ↳ Re: COBOL CGI on Aix with apache

- **From:** "Jack" <keziah.jones@caramail.com>
- **Date:** 2001-08-06T15:15:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SIwb7.6668$Yy2.33544@tengri.easynet.fr>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr> <3b6e928b_9@goliath.newsgroups.com>`

```

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> a �crit dans le
message news: 3b6e928b_9@goliath.newsgroups.com...
> Can you give us some more details as to how the CGI interface is
> implemented?
>
On AS/400 our soft use calls those three "procedures" from the system  :

like this :

CALL LINKAGE  IS PROCEDURE "QtmhWrStout"
     USING
                            OUTBUFF
                            OUTBUFFLN
                            QUS-EC
END-CALL.

- QtmhRdStin       - to read the standard
- QtmhWrStout    - to write the HTML
- QtmhGetEnv      - for getting back some informations

> Are you making calls to a COBOL "blind" interface (It doesn't matter
whether
> it is the Windows CGI or the Standard one) or are you making your own
direct
> CGI calls to the Unix CGI (using STDIO), or to the Windows CGI using
direct
> calls...
>
does my first answer is enough ?

> What COBOL are you using?

COBOL Microfocus
```

###### ↳ ↳ ↳ Re: COBOL CGI on Aix with apache

- **From:** Gary_guizio@ci.juneau.ak.us (GaryG)
- **Date:** 2001-08-06T14:34:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf4aea75.0108061334.28d4aebe@posting.google.com>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr> <3b6e928b_9@goliath.newsgroups.com> <SIwb7.6668$Yy2.33544@tengri.easynet.fr>`

```
"Jack" <keziah.jones@caramail.com> wrote in message news:<SIwb7.6668$Yy2.33544@tengri.easynet.fr>...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> a ï¿½crit dans le
> message news: 3b6e928b_9@goliath.newsgroups.com...
…[30 more quoted lines elided]…
> COBOL Microfocus

You can use a product called Cobol-CGIX from England Technical
Services.(www.netins.net/showcase/etsinc) It will accomplish much of
the same thing you are doing on the AS400 but in the AIX environment.
```

###### ↳ ↳ ↳ Re: COBOL CGI on Aix with apache

_(reply depth: 4)_

- **From:** "Jack" <keziah.jones@caramail.com>
- **Date:** 2001-08-07T16:12:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ESb7.6794$Yy2.38015@tengri.easynet.fr>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr> <3b6e928b_9@goliath.newsgroups.com> <SIwb7.6668$Yy2.33544@tengri.easynet.fr> <cf4aea75.0108061334.28d4aebe@posting.google.com>`

```
> You can use a product called Cobol-CGIX from England Technical
> Services.(www.netins.net/showcase/etsinc) It will accomplish much of
> the same thing you are doing on the AS400 but in the AIX environment.

Thank you for these informations.

Any informations about the prices ?
COBOL-CGI and COBOL-CGIX
```

###### ↳ ↳ ↳ Re: COBOL CGI on Aix with apache

_(reply depth: 5)_

- **From:** gary_guizio@ci.juneau.ak.us (GaryG)
- **Date:** 2001-08-07T12:30:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f96d0295.0108071130.69bd657f@posting.google.com>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr> <3b6e928b_9@goliath.newsgroups.com> <SIwb7.6668$Yy2.33544@tengri.easynet.fr> <cf4aea75.0108061334.28d4aebe@posting.google.com> <9ESb7.6794$Yy2.38015@tengri.easynet.fr>`

```
"Jack" <keziah.jones@caramail.com> wrote in message news:<9ESb7.6794$Yy2.38015@tengri.easynet.fr>...
> > You can use a product called Cobol-CGIX from England Technical
> > Services.(www.netins.net/showcase/etsinc) It will accomplish much of
…[5 more quoted lines elided]…
> COBOL-CGI and COBOL-CGIX

COBOL-CGIX was $1,250.00 in January of 2000. This is for an unlimited use license.
```

###### ↳ ↳ ↳ Re: COBOL CGI on Aix with apache

_(reply depth: 6)_

- **From:** "Jack" <keziah.jones@caramail.com>
- **Date:** 2001-08-08T09:49:17+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b6c7.6813$Yy2.43499@tengri.easynet.fr>`
- **References:** `<y0tb7.5927$Yy2.32585@tengri.easynet.fr> <3b6e928b_9@goliath.newsgroups.com> <SIwb7.6668$Yy2.33544@tengri.easynet.fr> <cf4aea75.0108061334.28d4aebe@posting.google.com> <9ESb7.6794$Yy2.38015@tengri.easynet.fr> <f96d0295.0108071130.69bd657f@posting.google.com>`

```

> COBOL-CGIX was $1,250.00 in January of 2000.  This is for an unlimited use
license.

Thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
