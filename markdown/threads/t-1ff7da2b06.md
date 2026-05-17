[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Realia 5.0 and screenio.lib

_7 messages · 6 participants · 1996-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Realia 5.0 and screenio.lib

- **From:** "emi..." <ua-author-17086441@usenetarchives.gap>
- **Date:** 1996-08-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4v6fdm$arj@tron.sci.fi>`

```

Dll's made with realia 5.0 can be called from modules made with other
languages as VB or C. Ok, let's begin to use this version of CA's
compiler. But for it's text-based screen handler (Screenio) there is
no new library (Screenio.lib), last good one is based on Realia 4.2 and
won't work with new compiled programs.

Does anybody have same problem and know some solution?

Friendly

Harri Ljungdell
Helsinki, FIN
```

#### ↳ Re: Realia 5.0 and screenio.lib

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-08-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4v6fdm$arj@tron.sci.fi>`
- **References:** `<4v6fdm$arj@tron.sci.fi>`

```

In article <4v6fdm$a.··.@tro··i.fi>, emi··.@s··.fi says...
› 
› Dll's made with realia 5.0 can be called from modules made with other   
…[13 more quoted lines elided]…
› 


Forgot to mention that the updrade diskette Norcom (Screenio V2.3) sent
me had two directories: one for CA-Realia Cobol 4.2 and one for 5.0.
The libraries needed for linking are in those directories.

mike dodas
```

#### ↳ Re: Realia 5.0 and screenio.lib

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1996-08-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4v6fdm$arj@tron.sci.fi>`
- **References:** `<4v6fdm$arj@tron.sci.fi>`

```

emi··.@s··.fi (emikron) wrote:

› Dll's made with realia 5.0 can be called from modules made with other	
› languages as VB or C. Ok, let's begin to use this version of CA's
› compiler. But for it's text-based screen handler (Screenio) there is	
› no new library (Screenio.lib), last good one is based on Realia 4.2 and
› won't work with new compiled programs.	
 
› Does anybody have same problem and know some solution?		
 
› Friendly	
 
› Harri Ljungdell	
› Helsinki, FIN
›  

Harri:

We have a screen handler which works with version 5 of CA-Realia
COBOL, called COBOL spII. It is availabel for both MS-DOS text mode
systems and Windows GUI systems. Screen definitions and screen
handling source code (ANSI standard COBOL CALL's) are 100% transparent
between character environments and GUI environments.

You can also download an evaluation copy of the software from our home
page.

Access the Flexus COBOL Page at http://www.flexus.com


Bob Wolfe, flexus
rtw··.@fle··s.com
Check out The Flexus COBOL Page at: http://www.flexus.com
```

#### ↳ Re: Realia 5.0 and screenio.lib

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-08-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4v6fdm$arj@tron.sci.fi>`
- **References:** `<4v6fdm$arj@tron.sci.fi>`

```

In article <4v6fdm$a.··.@tro··i.fi>, emi··.@s··.fi says...
› 
› Dll's made with realia 5.0 can be called from modules made with other   
…[13 more quoted lines elided]…
› 

Harri:

I'm not sure what kind of problem you are having, but I believe
CA-Realia 5.0 Cobol requires Version 2.3 of Screen/IO. This is the
version I have used with 5.0.

P.S. - Your post sounds like 5.0 has been generally available for
quite some time. I just recently received a letter to
upgrade to 5.0, although I was a beta-tester for 5.0.

mike dodas
Salt Lake City, UT--USA
```

##### ↳ ↳ Re: Realia 5.0 and screenio.lib

- **From:** "ande..." <ua-author-17072691@usenetarchives.gap>
- **Date:** 1996-08-19T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1ff7da2b06-p4@usenetarchives.gap>`
- **References:** `<4v6fdm$arj@tron.sci.fi> <gap-1ff7da2b06-p4@usenetarchives.gap>`

```

On 19 Aug 1996 21:09:51 GMT, mi··.@u··.com (Michael Dodas) wrote:

>In article <4v6fdm$a.··.@tro··i.fi>, emi··.@s··.fi says...
>>
…[24 more quoted lines elided]…
> upgrade to 5.0, although I was a beta-tester for 5.0.

Mike and Harri:

Check with us at NORCOM for a new lib for screenio
We may even have it on our web page
http://www.alaska.net/â€¾norcom



______________________________
John Andersen
Juneau, Alaska
```

#### ↳ Re: Realia 5.0 and screenio.lib

- **From:** "kevin j. hansen" <ua-author-17072510@usenetarchives.gap>
- **Date:** 1996-08-21T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4v6fdm$arj@tron.sci.fi>`
- **References:** `<4v6fdm$arj@tron.sci.fi>`

```

emikron wrote:
› But for it's text-based screen handler (Screenio) there is
› no new library (Screenio.lib), last good one is based on Realia 4.2 and
…[3 more quoted lines elided]…
› Harri:

NORCOM distributed a library for Realia 5.0 with the 2.3 upgrade we sent out in
April, I believe. Our records show that we sent it to you for the copy which
was under maintenance. The library is in a subdirectory on the upgrade
diskette.

FWIW, we're also making good progress on a native Windows version of Screenio.

Kevin
```

#### ↳ Re: Realia 5.0 and screenio.lib

- **From:** "a000..." <ua-author-990456@usenetarchives.gap>
- **Date:** 1996-08-30T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1ff7da2b06-p7@usenetarchives.gap>`
- **In-Reply-To:** `<4v6fdm$arj@tron.sci.fi>`
- **References:** `<4v6fdm$arj@tron.sci.fi>`

```

You might try giving C.A. a call or check out their BBS and download
the new version .

emi··.@s··.fi (emikron) wrote:

› Dll's made with realia 5.0 can be called from modules made with other	
› languages as VB or C. Ok, let's begin to use this version of CA's
› compiler. But for it's text-based screen handler (Screenio) there is	
› no new library (Screenio.lib), last good one is based on Realia 4.2 and
› won't work with new compiled programs.	
 
› Does anybody have same problem and know some solution?		
 
› Friendly	
 
› Harri Ljungdell	
› Helsinki, FIN
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
