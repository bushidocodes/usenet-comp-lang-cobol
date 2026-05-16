[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VA COBOL on Win32, calling external DLLs

_8 messages · 4 participants · 2003-08_

---

### VA COBOL on Win32, calling external DLLs

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-08-21T12:54:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca>`

```
I'm having a hella time trying to CALL functions in external DLLs from 
IBM's Visual Age for COBOL on Win32.  I've read a variety of sometimes 
conflicting examples, and none seem to work for me.

Note that I'm _not_ creating a DLL from COBOL code, nor am I calling my 
own DLLs written in some other langage.  I'm interesting in running 
functions in things like user32.dll or wsock32.dll.

Anybody spare a clue?  An known working example of loading the DLL into 
memory, and accessing a function appreciated.

-- cm
```

#### ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-21T20:49:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fa1b.5424$sV.652@newsread1.news.atl.earthlink.net>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca>`

```
I don't have an  answer but you MIGHT get a better reply in the

   ibm.software.cobol

forum.
```

##### ↳ ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-08-22T11:25:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pBq1b.60288$PD3.4621138@nnrp1.uunet.ca>`
- **In-Reply-To:** `<8fa1b.5424$sV.652@newsread1.news.atl.earthlink.net>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca> <8fa1b.5424$sV.652@newsread1.news.atl.earthlink.net>`

```
William M. Klein wrote:

> I don't have an  answer but you MIGHT get a better reply in the
> 
…[3 more quoted lines elided]…
> 
Unfortunately, my newsfeed does not carry this newsgroup.  Looks like 
Google Groups doesn't carry it, either.
```

###### ↳ ↳ ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-08-22T11:35:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bi5k9u$5bd9a$1@ID-184804.news.uni-berlin.de>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca> <8fa1b.5424$sV.652@newsread1.news.atl.earthlink.net> <pBq1b.60288$PD3.4621138@nnrp1.uunet.ca>`

```
clvrmnky<clvrmnky@coldmail.com.invalid> 08/22/03 09:25AM >>>
>William M. Klein wrote:
>
…[7 more quoted lines elided]…
>Google Groups doesn't carry it, either.

Connect your newsreader to news.software.ibm.com.  No authentication
necessary, IIRC.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: VA COBOL on Win32, calling external DLLs

_(reply depth: 4)_

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-08-22T15:25:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n6u1b.60418$PD3.4622063@nnrp1.uunet.ca>`
- **In-Reply-To:** `<bi5k9u$5bd9a$1@ID-184804.news.uni-berlin.de>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca> <8fa1b.5424$sV.652@newsread1.news.atl.earthlink.net> <pBq1b.60288$PD3.4621138@nnrp1.uunet.ca> <bi5k9u$5bd9a$1@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick wrote:

> clvrmnky<clvrmnky@coldmail.com.invalid> 08/22/03 09:25AM >>>
[...]
>>Unfortunately, my newsfeed does not carry this newsgroup.  Looks like 
>>Google Groups doesn't carry it, either.
…[3 more quoted lines elided]…
> necessary, IIRC.

Thanks.  I was poking around for the server name, with no luck.  I'll 
refer VA COBOL specifics to there from now on.
```

#### ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** "Al Shannon" <shannon@allover.com>
- **Date:** 2003-08-22T00:04:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f45c0bc$1_2@corp.newsgroups.com>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca>`

```
As I recall, you simply make static calls to the functions you're interested
in using standard call linkage.  It's equivalent to calling C functions from
your COBOL program.  Link with the import library.  You don't explicitly
load the DLL.  You should be able to find the details in the programming
guide for calling functions written in C.  See:

   http://www-3.ibm.com/software/awdtools/cobol/va/library/

Al...

"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:xP61b.59893$PD3.4615912@nnrp1.uunet.ca...
> I'm having a hella time trying to CALL functions in external DLLs from
> IBM's Visual Age for COBOL on Win32.  I've read a variety of sometimes
…[10 more quoted lines elided]…
>




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 100,000 Newsgroups - 19 Different Servers! =-----
```

##### ↳ ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-08-22T11:38:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TNq1b.60297$PD3.4621228@nnrp1.uunet.ca>`
- **In-Reply-To:** `<3f45c0bc$1_2@corp.newsgroups.com>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca> <3f45c0bc$1_2@corp.newsgroups.com>`

```
Al Shannon wrote:

> As I recall, you simply make static calls to the functions you're interested
> in using standard call linkage.  It's equivalent to calling C functions from
…[4 more quoted lines elided]…
>    http://www-3.ibm.com/software/awdtools/cobol/va/library/

I've been using this programming guide as a reference.  There are 
examples for calling your own C functions, but none for calling 
arbitrary functions in DLLs that you haven't coded.  That is, for DLLs 
where you do not have the import library to link with.

Or perhaps I misunderstand your meaning?

There must be a way to call external public functions from 
self-registering DLLs.  My eyes are not finding it in this guide.

-- cm
```

#### ↳ Re: VA COBOL on Win32, calling external DLLs

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-08-22T13:17:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Aes1b.60353$PD3.4621563@nnrp1.uunet.ca>`
- **In-Reply-To:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca>`
- **References:** `<xP61b.59893$PD3.4615912@nnrp1.uunet.ca>`

```
clvrmnky wrote:

> I'm having a hella time trying to CALL functions in external DLLs from 
> IBM's Visual Age for COBOL on Win32.  I've read a variety of sometimes 
…[8 more quoted lines elided]…
> 
To _partially_ answer my own question, the idea is to defer linking with 
the DYNAM compiler option (-qdynam for cob2) and CALL the DLL as a 
literal or identifier.  The runtime stuff will look for the DLL in the 
standard search path, and will append ".dll" to the call identifier.

So far, so good.  I still have to find a way, if there is one, of 
calling a particular entry point within the DLL.  Passing and return 
values or references are contingent on this, as well.  I've heard rumors 
that VA COBOL allows only one entry point per DLL; the entry point is 
the name of the DLL.

Does this jibe with the VA COBOL experience out there?

-- cm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
