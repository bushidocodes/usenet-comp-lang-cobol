[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Shortest possible COBOL program.

_8 messages · 8 participants · 1997-07_

---

### Shortest possible COBOL program.

- **From:** "yam..." <ua-author-17072498@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

According to my IBM manual SC26-4045-05 (VS COBOL II compiler), the
shortest possible program producing output is

ID DIVISION.
PROGRAM-ID. ERRMSG.


-----beg··a@a··.org--- 
#!/bin/perl -sp0777i
$/=unpack('H*',$_);$_=`echo 16dio\U$k"SK$/SM$n\EsN0p[lN*1
lK[d2%Sa2/d0$^Ixp"|dc`;s/\W//g;$_=pack('H*',/((..)*)$/)
-----end_sig_block_end_mail_message---
```

#### ↳ Re: Shortest possible COBOL program.

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

In <5qg2jv$loo$1.··.@vix··c.edu>, yam··.@pra··t.org (William Paul Fiefer) writes:
› According to my IBM manual SC26-4045-05 (VS COBOL II compiler), the
› shortest possible program producing output is
…[4 more quoted lines elided]…
› 

But what you forgot to mention is that the IBM COBOL II compiler
(and other IBM COBOL compilers) use this specific program to dump
the compiler's internal message table.

Compiling this program under COBOL I, COBOL II, COBOL/370 or COBOL for MVS/VM
should result in every error, warning and message possible for that compiler.

Lew Pitcher
Toronto Dominion Bank
```

#### ↳ Re: Shortest possible COBOL program.

- **From:** "james walker" <ua-author-838022@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

actually this is the minimum required to be called a program, and an
excellent way to make a stub program, for testing a called program being
developed elsewhere but not yet quite ready, your functionality can be
chacked by creating a stub program comprised of just these 2 lines!!!!!
____________________
```

#### ↳ Re: Shortest possible COBOL program.

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

On 15 Jul 1997 14:48:31 GMT, yam··.@pra··t.org (William Paul
Fiefer) wrote:

› According to my IBM manual SC26-4045-05 (VS COBOL II compiler), the
› shortest possible program producing output is
…[7 more quoted lines elided]…
› #!/bin/perl -sp0777i$/=unpack('H*',$_);$_=`echo 16dio\U$k"SK$/SM$n\EsN0p[lN*1
 
› lK[d2%Sa2/d0$^Ixp"|dc`;s/\W//g;$_=pack('H*',/((..)*)$/)
› -----end_sig_block_end_mail_message---

Based on a thread I inadvertantly started around a year ago this IS
the shortest legal program. The only thing non-compliant with your
version is the use of ID for IDENTIFICATION. That's an IBM extension.

NOW, I hope that Microsoft doesn't have any spies around because this
looks like the beginning of a great new product. I realize it doesn't
do much yet, but neither does version 1.0 of any MS product.

The way I figure it, we could sell upgrades to 1.1 which has
IDENTIFICATION spelled out so it will compile everywhere, and we could
put an Easter Egg in version 2.0 so the magazines will continue to
feature it months after its introduction...

That gives us at least 2 years to think up a use for it by version
3.0. Naturally it will be a bit bigger by then -- say the install set
will be 4 DVD's and it will require at least 128 MB of memory to run
with 512 MB and dual 500 MHz Alpha processors recommended.

George Trudeau, Town of Falmouth

"Visit our controversial short COBOL program at
http://www.town.falmouth.ma.us/hello.html"
```

#### ↳ Re: Shortest possible COBOL program.

- **From:** "mister b" <ua-author-718841@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

William Paul Fiefer wrote in article
<5qg2jv$loo$1.··.@vix··c.edu>...
› According to my IBM manual SC26-4045-05 (VS COBOL II compiler), the
› shortest possible program producing output is
…[3 more quoted lines elided]…
› 
Compilers I have met require PROCEDURE DIVISION at least. Surely the above
code is not ANSI compliant 8-)
Did it pass syntax on your compiler - many is the time I have met incorrect
syntax in examples with documentation...



Mister B

I do NOT speak for Unisys.
Remove NOSPAM from my address to reply.
```

##### ↳ ↳ Re: Shortest possible COBOL program.

- **From:** "j lenz" <ua-author-17071373@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cc37ac08cf-p5@usenetarchives.gap>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu> <gap-cc37ac08cf-p5@usenetarchives.gap>`

```

Mister B wrote:
› 
› William Paul Fiefer  wrote in article
…[17 more quoted lines elided]…
› Remove NOSPAM from my address to reply.


The above mentioned program simply dumps/prints the COBOL II error
messages.

Joseph Lenz
TTI, Inc.
Fort Worth, TX
```

###### ↳ ↳ ↳ Re: Shortest possible COBOL program.

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-07-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cc37ac08cf-p6@usenetarchives.gap>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu> <gap-cc37ac08cf-p5@usenetarchives.gap> <gap-cc37ac08cf-p6@usenetarchives.gap>`

```

J Lenz wrote:
› 
› Mister B wrote:
…[26 more quoted lines elided]…
› Fort Worth, TX

It compiles clean under microfocus cobol 3.2.....

*****************************************************************
prg··.@ep··x.net
url http://www.epix.net/â€¾prgsdw
*****************************************************************
```

#### ↳ Re: Shortest possible COBOL program.

- **From:** "steven j casey" <ua-author-17071728@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cc37ac08cf-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`
- **References:** `<5qg2jv$loo$1@vixen.cso.uiuc.edu>`

```

I don't know about the shortest, but I have seen the longest.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
