[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Encryption Question

_6 messages · 3 participants · 1998-09_

---

### Encryption Question

- **From:** David Gray <david_m_gray@studio.disney.com>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3600E0DB.18760C0B@studio.disney.com>`

```
Hi all,

Iam writing a DECforms/COBOL screen that will maintain a file containing

amonsgst other things passwords for FTPing to different nodes.

I need to encrypt the password field so that anyone looking at the file
cannot read the password.

The file will be an Indexed RMS and the OS is OpenVMS on an Alpha.

Any ideas greatly appreciated.

Regards,

 David.
```

#### ↳ Re: Encryption Question

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360101ba.0@news1.ibm.net>`
- **References:** `<3600E0DB.18760C0B@studio.disney.com>`

```

David Gray wrote in message <3600E0DB.18760C0B@studio.disney.com>...
>Hi all,
>Iam writing a DECforms/COBOL screen that will maintain a file containing
…[3 more quoted lines elided]…
>Any ideas greatly appreciated.


The ETKPAK package at http://www.etk.com contains a subroutine PWRDPK
(http://www.etk.com/download/etkpak/etkpak.htm#PWRDPK) that produces
an encryption signature of a password. Store the signature in the file. When
the user gives a password, call PWRDPK to get the signature for the
password, compare that to what is in the file, if they don't match, the
password is wrong.
```

##### ↳ ↳ Re: Encryption Question

- **From:** scm@enterprise.net (Shaun C. Murray)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6trgi2$euv$1@news.enterprise.net>`
- **References:** `<3600E0DB.18760C0B@studio.disney.com> <360101ba.0@news1.ibm.net>`

```
In article <360101ba.0@news1.ibm.net>, leif@ibm.net says...
>
>
…[15 more quoted lines elided]…
>

How secure is PWRDPK's encryption routine though?

PGP, http://www.pgp.com or http://www.pgpi.com , or the freely available crypto 
library could also be used to encrypt the file. You would have to call an API 
to decrypt the file before reading it into your COBOL program.

There are a number of commercial packages available though I don't know which 
are available for VMS offhand. I mention this as some companies are 'nervous' 
of free software. Why I don't know as you can bet your bottom the US government 
wouldn't let a commercial entity ship encryption technology outside the US 
without knowing how it works. RSA, http://www.rsa.com , and Baltimore 
http://www.baltimore.ie , being the two I'm familiar with.

The other problem is that some countries don't like encryption. France bans it 
though are coming round to it because the rest of the EU uses it. Certain 
countries also dislike US originated software. eg. Cuba, Russia etc. Use the 
same algorithm but written in Norway and they like you.
```

###### ↳ ↳ ↳ Re: Encryption Question

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360149ba.0@news1.ibm.net>`
- **References:** `<3600E0DB.18760C0B@studio.disney.com> <360101ba.0@news1.ibm.net> <6trgi2$euv$1@news.enterprise.net>`

```

Shaun C. Murray wrote in message <6trgi2$euv$1@news.enterprise.net>...
>>David Gray wrote in message <3600E0DB.18760C0B@studio.disney.com>...
>>>Hi all,
…[8 more quoted lines elided]…
>How secure is PWRDPK's encryption routine though?


It is secure enough to prevent casual snooping. It does not purport to
be in the RSA or PGP league with all the legal problems associated
with that.
```

###### ↳ ↳ ↳ Re: Encryption Question

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36014c66.0@news1.ibm.net>`
- **References:** `<3600E0DB.18760C0B@studio.disney.com> <360101ba.0@news1.ibm.net> <6trgi2$euv$1@news.enterprise.net>`

```
Shaun C. Murray wrote in message <6trgi2$euv$1@news.enterprise.net>...
>In article <360101ba.0@news1.ibm.net>, leif@ibm.net says...
> Certain  countries also dislike US originated software. eg. Cuba, Russia
etc. Use the
>same algorithm but written in Norway and they like you.


PWRDPK is written in Belgium, so on this account we should be OK.
```

#### ↳ Re: Encryption Question

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-u7Ldbek4gZvu@dsm4merlin.iix.com>`
- **References:** `<3600E0DB.18760C0B@studio.disney.com>`

```
On Thu, 17 Sep 1998 10:13:47, David Gray 
<david_m_gray@studio.disney.com> wrote:

> The file will be an Indexed RMS and the OS is OpenVMS on an Alpha.
> 
PGP is available on the Alpha - we use it for file exchange with UUNET
for billing info - you could email munozch@iix.com for some details - 
tell him I sent you

You also might see if Compaq (don't hold your breath) knows anything 
about the  OpenVMS password encryption mechanism that they use being 
available as an API.

=Dwight=
X1=L, X2=L & the domain is phonetic
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
