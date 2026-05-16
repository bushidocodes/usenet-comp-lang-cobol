[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Status 9/060 with MF-COBOL

_3 messages · 2 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### File Status 9/060 with MF-COBOL

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6YQ03.37$_c.34@news.megsinet.net>`

```
Has anyone ever got a 9/060 code with MF-COBOL? If you did, and you figured
out what was causing it, I'd like to know.

According to the MF-COBOL documentation, there is no such extended code as
"060".

- Darius
```

#### ↳ Re: File Status 9/060 with MF-COBOL

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-pvIIUdoumvXG@Dwight_Miller.iix.com>`
- **References:** `<6YQ03.37$_c.34@news.megsinet.net>`

```
On Thu, 20 May 1999 09:56:21, "Darius Cooper" 
<Darius_cooper@Bigfoot.com> wrote:

> Has anyone ever got a 9/060 code with MF-COBOL? If you did, and you figured
> out what was causing it, I'd like to know.
> 
> According to the MF-COBOL documentation, there is no such extended code as
> "060".

This isn't going to be much help, but I *HAVE* seen this before - 
reported at a client site.  I think it had to do with running Window 
95 as a client to Netware 3.12 or 4.1.  I think we had to have them 
install the Novell Client/32 drivers instead of using the default 
Window 95 Novell drivers.  It only happened on networks where SOME 
clients were DOS and some were Windows 95.

Does this sound like your situation?

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: File Status 9/060 with MF-COBOL

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9_Z03.9$UA.216@news.megsinet.net>`
- **References:** `<6YQ03.37$_c.34@news.megsinet.net> <Jl0PnHJ5PvPd-pn2-pvIIUdoumvXG@Dwight_Miller.iix.com>`

```
Thank you for the reply.
My application is on AIX.
MF-COBOL says that there isn't such a code, and that our DECODING of the
extended error-code is incorrect.
Since this error came up at two client sites, but does not happen when we
run the app. in-house, we are unable to animate it and see the error-code.

Thanks again,

- Darius


Thane Hubbell wrote in message ...
>On Thu, 20 May 1999 09:56:21, "Darius Cooper"
><Darius_cooper@Bigfoot.com> wrote:
>
>> Has anyone ever got a 9/060 code with MF-COBOL? If you did, and you
figured
>> out what was causing it, I'd like to know.
>>
>> According to the MF-COBOL documentation, there is no such extended code
as
>> "060".
>
…[15 more quoted lines elided]…
>http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
