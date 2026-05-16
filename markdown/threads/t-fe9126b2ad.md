[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Close with disp ?

_5 messages · 3 participants · 2004-04_

---

### Close with disp ?

- **From:** "Ron S" <SpamStopper@NoSpam.Org>
- **Date:** 2004-04-05T16:46:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kPidnT8JnsQ3TuzdRVn_vQ@giganews.com>`

```
I was converting a 35 year old OS Cobol program to
Enterprise Cobol today. All the CLOSE statements in
this program had CLOSE file-name WITH DISP. I don't
happen to have a 35 year old manual and this is not
 valid for Enterprise Cobol. Does anyone remember
what CLOSE WITH DISP was supposed to do?
```

#### ↳ Re: Close with disp ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-05T22:20:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dZkcc.17055$lt2.5031@newsread1.news.pas.earthlink.net>`
- **References:** `<kPidnT8JnsQ3TuzdRVn_vQ@giganews.com>`

```
Page 443 of the OS/VS COBOL program says that "CLOSE WITH DISP" means to use
whatever is on the DISP parameter of the JCL - so it sounds like you can just
remove it and things should work "as expected".
```

##### ↳ ↳ Re: Close with disp ?

- **From:** "Ron S" <SpamStopper@NoSpam.Org>
- **Date:** 2004-04-05T20:32:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A5KdnXrEpO9Vle_dRVn_vA@giganews.com>`
- **References:** `<kPidnT8JnsQ3TuzdRVn_vQ@giganews.com> <dZkcc.17055$lt2.5031@newsread1.news.pas.earthlink.net>`

```
> Page 443 of the OS/VS COBOL program says that "CLOSE WITH DISP" means to use
> whatever is on the DISP parameter of the JCL - so it sounds like you can just
> remove it and things should work "as expected".
>

Thanks. I did remove it and all was well but I was just curious as to what its
purpose was years ago. Not much, it would seem.
```

###### ↳ ↳ ↳ Re: Close with disp ?

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-04-05T22:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LApcc.17059$wq4.867538@news20.bellglobal.com>`
- **In-Reply-To:** `<A5KdnXrEpO9Vle_dRVn_vA@giganews.com>`
- **References:** `<kPidnT8JnsQ3TuzdRVn_vQ@giganews.com> <dZkcc.17055$lt2.5031@newsread1.news.pas.earthlink.net> <A5KdnXrEpO9Vle_dRVn_vA@giganews.com>`

```
Ron S wrote:
>>Page 443 of the OS/VS COBOL program says that "CLOSE WITH DISP" means to use
>>whatever is on the DISP parameter of the JCL - so it sounds like you can just
…[7 more quoted lines elided]…
> 
A wag ... close with rewind vs close with dismount type of thing at the 
JCL level?

Donald
```

###### ↳ ↳ ↳ Re: Close with disp ?

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-04-05T22:39:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iGpcc.17065$wq4.870329@news20.bellglobal.com>`
- **In-Reply-To:** `<A5KdnXrEpO9Vle_dRVn_vA@giganews.com>`
- **References:** `<kPidnT8JnsQ3TuzdRVn_vQ@giganews.com> <dZkcc.17055$lt2.5031@newsread1.news.pas.earthlink.net> <A5KdnXrEpO9Vle_dRVn_vA@giganews.com>`

```
Ron S wrote:
>>Page 443 of the OS/VS COBOL program says that "CLOSE WITH DISP" means to use
>>whatever is on the DISP parameter of the JCL - so it sounds like you can just
…[7 more quoted lines elided]…
> 

As a PS to that, it is too bad that some of those old tape methods left 
Cobol.  They would work very well for things like CD"s and DVD's on a 
PC, for example. With properly working label records and mount dismount 
close commands, someone could actually do proper backup of data without 
leaving Cobol. The Rewritable DVD is quite a neat device.  I think it 
will be arround for a while, at least as a prototype.

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
