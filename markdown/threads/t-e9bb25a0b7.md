[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New learning website for COBOL in the making

_15 messages · 9 participants · 2012-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### New learning website for COBOL in the making

- **From:** Christopher Bahn <cbbahn@gmail.com>
- **Date:** 2012-11-11T01:49:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`

```
Hi everybody,

I just beginning learning COBOL and want to help me and others with example source code for studying. Therefore, I set up a website which shall contain a small database with code: https://sites.google.com/site/cobolcode/

Any code "donation" (not meant in a transfer of copy rights, but showing at the homepage) would be highly appreciated. Thanks a lot!

Kind regards,

Christopher
```

#### ↳ Re: New learning website for COBOL in the making

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2012-11-11T11:56:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L7KdnRkSfrs6RQLNnZ2dnUVZ_tqdnZ2d@earthlink.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`

```

"Christopher Bahn" <cbbahn@gmail.com> wrote in message 
news:b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com...
> Hi everybody,
>
…[10 more quoted lines elided]…
> Christopher

The short program at your link looks like Java.  How does that help anyone 
learn COBOL?
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Christopher Bahn <cbbahn@gmail.com>
- **Date:** 2012-11-12T06:29:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<799c1ac0-b88e-4bfd-a403-6cc39b9d32af@googlegroups.com>`
- **In-Reply-To:** `<L7KdnRkSfrs6RQLNnZ2dnUVZ_tqdnZ2d@earthlink.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <L7KdnRkSfrs6RQLNnZ2dnUVZ_tqdnZ2d@earthlink.com>`

```
Am Sonntag, 11. November 2012 17:56:08 UTC+1 schrieb Charles Hottel:
> "Christopher Bahn" <cbbahn@gmail.com> wrote in message 
> 
…[32 more quoted lines elided]…
> learn COBOL?

That is true, but it is meant only as illustration of "source code".
```

#### ↳ Re: New learning website for COBOL in the making

- **From:** Luuk <luuk@invalid.lan>
- **Date:** 2012-11-11T18:24:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rj35n9-gd5.ln1@luuk.invalid.lan>`
- **In-Reply-To:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`

```
On 11-11-2012 10:49, Christopher Bahn wrote:
> Hi everybody,
>
…[7 more quoted lines elided]…
>

As Charles said, it looks like Java,
so maybe you should heve use Google,
because than you would have found:
http://groups.engin.umd.umich.edu/CIS/course.des/cis400/cobol/hworld.html

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.     HELLOWORLD.
000300
000400*
000500 ENVIRONMENT DIVISION.
000600 CONFIGURATION SECTION.
000700 SOURCE-COMPUTER. RM-COBOL.
000800 OBJECT-COMPUTER. RM-COBOL.
000900
001000 DATA DIVISION.
001100 FILE SECTION.
001200
100000 PROCEDURE DIVISION.
100100
100200 MAIN-LOGIC SECTION.
100300 BEGIN.
100400     DISPLAY " " LINE 1 POSITION 1 ERASE EOS.
100500     DISPLAY "Hello world!" LINE 15 POSITION 10.
100600     STOP RUN.
100700 MAIN-LOGIC-EXIT.
100800     EXIT.

and is 'hello world' not the standard first program that anyone wants to 
write when he (or she) is learning a 'new' language ?
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Anonymous <nobody@remailer.paranoici.org>
- **Date:** 2012-11-12T13:19:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fca69f60120d6f459bd57cad3040a29e@remailer.paranoici.org>`
- **References:** `<rj35n9-gd5.ln1@luuk.invalid.lan>`

```
Luuk <luuk@invalid.lan> wrote:

> and is 'hello world' not the standard first program that anyone wants to 
> write when he (or she) is learning a 'new' language ?

No, it is not, especially not in this case since COBOL came out in 1959 and
"Hello, World!" didn't come out until K&R in 1978.

Do the math!

>
```

###### ↳ ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Luuk <luuk@invalid.lan>
- **Date:** 2012-11-12T20:16:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1iu7n9-7li.ln1@luuk.invalid.lan>`
- **In-Reply-To:** `<fca69f60120d6f459bd57cad3040a29e@remailer.paranoici.org>`
- **References:** `<rj35n9-gd5.ln1@luuk.invalid.lan> <fca69f60120d6f459bd57cad3040a29e@remailer.paranoici.org>`

```
On 12-11-2012 14:19, Anonymous wrote:
> Luuk <luuk@invalid.lan> wrote:
>
…[9 more quoted lines elided]…
>

Can i borrow someone's calculator?

;)
```

###### ↳ ↳ ↳ Re: New learning website for COBOL in the making

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-11-13T13:06:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jfCdnXvncvvOBz_NnZ2dnUVZ_rSdnZ2d@earthlink.com>`
- **References:** `<rj35n9-gd5.ln1@luuk.invalid.lan> <fca69f60120d6f459bd57cad3040a29e@remailer.paranoici.org> <1iu7n9-7li.ln1@luuk.invalid.lan>`

```
Luuk wrote:
> On 12-11-2012 14:19, Anonymous wrote:
>> Luuk <luuk@invalid.lan> wrote:
…[13 more quoted lines elided]…
>

You could write a program ...
```

###### ↳ ↳ ↳ Re: New learning website for COBOL in the making

_(reply depth: 5)_

- **From:** Luuk <luuk@invalid.lan>
- **Date:** 2012-11-13T21:01:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dhlan9-vsv.ln1@luuk.invalid.lan>`
- **In-Reply-To:** `<jfCdnXvncvvOBz_NnZ2dnUVZ_rSdnZ2d@earthlink.com>`
- **References:** `<rj35n9-gd5.ln1@luuk.invalid.lan> <fca69f60120d6f459bd57cad3040a29e@remailer.paranoici.org> <1iu7n9-7li.ln1@luuk.invalid.lan> <jfCdnXvncvvOBz_NnZ2dnUVZ_rSdnZ2d@earthlink.com>`

```
On 13-11-2012 20:06, HeyBub wrote:
> Luuk wrote:
>> On 12-11-2012 14:19, Anonymous wrote:
…[18 more quoted lines elided]…
>

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.     HELLOWORLD.
000300
000400*
000500 ENVIRONMENT DIVISION.
000600 CONFIGURATION SECTION.
000700 SOURCE-COMPUTER. RM-COBOL.
000800 OBJECT-COMPUTER. RM-COBOL.
000900
001000 DATA DIVISION.
001100 FILE SECTION.
001200
100000 PROCEDURE DIVISION.
100100
100200 MAIN-LOGIC SECTION.
100300 BEGIN.
100400     DISPLAY " " LINE 1 POSITION 1 ERASE EOS.
100500     DISPLAY "What time  has past between 1959 and 1978:", 	100600 
         1978-1959 .
100700     STOP RUN.
100800 MAIN-LOGIC-EXIT.
100900     EXIT.


But my coding skills are a bit...... not used for some time...
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-11-13T15:31:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c93ca2d-164c-4fb5-a2e6-faa4cf856099@googlegroups.com>`
- **In-Reply-To:** `<rj35n9-gd5.ln1@luuk.invalid.lan>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <rj35n9-gd5.ln1@luuk.invalid.lan>`

```
On Sunday, November 11, 2012 12:30:02 PM UTC-5, Luuk wrote:

[snip]

> 000100 IDENTIFICATION DIVISION.
> 000200 PROGRAM-ID.     HELLOWORLD.
…[18 more quoted lines elided]…
> 100800     EXIT.

FYI, the minimum program conforming to the COBOL 85 standard is:
-----
       identification division.
       program-id. hello.
       procedure division.
       begin.
           display "Hello world!".
-----

For COBOL 2002, it is (or should be):
-----
       program-id. hello.
       procedure division.
           display "Hello world!".
-----
```

###### ↳ ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Christopher Bahn <cbbahn@gmail.com>
- **Date:** 2012-11-20T05:31:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<755d6795-7a17-464a-85fe-0fb1f1db4300@googlegroups.com>`
- **In-Reply-To:** `<0c93ca2d-164c-4fb5-a2e6-faa4cf856099@googlegroups.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <rj35n9-gd5.ln1@luuk.invalid.lan> <0c93ca2d-164c-4fb5-a2e6-faa4cf856099@googlegroups.com>`

```
Am Mittwoch, 14. November 2012 00:31:13 UTC+1 schrieb Rick Smith:
> On Sunday, November 11, 2012 12:30:02 PM UTC-5, Luuk wrote:
> 
…[78 more quoted lines elided]…
> -----

Thanks!
```

#### ↳ Re: New learning website for COBOL in the making

- **From:** TruthSlave <TS@home.com>
- **Date:** 2012-11-18T20:53:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k8bhrq$s85$2@speranza.aioe.org>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`

```
On 11/11/12 09:49, Christopher Bahn wrote:
> Hi everybody,
>
…[10 more quoted lines elided]…
> Christopher


Back in the day i wrote a COBOL compiler for a now obscure platform, the 
amiga. I ported the program to linux but never got around to
publishing it.

It came with a number of reasonable programming examples, if you're
interested you could have those in a zip.
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-11-19T10:27:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vtjka89a0njuch9a9n5hflk18m48nkhjm6@4ax.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <k8bhrq$s85$2@speranza.aioe.org>`

```
On Sun, 18 Nov 2012 20:53:18 +0000, TruthSlave <TS@home.com> wrote:

>On 11/11/12 09:49, Christopher Bahn wrote:
>> Hi everybody,
…[17 more quoted lines elided]…
>

Too bad the Amiga is now obscure.  It was far better than Windows or
Apple but had a bunch of knuckleheads as CEOs.


>It came with a number of reasonable programming examples, if you're
>interested you could have those in a zip.

Regards,
-- 

          ////
         (o o)
-oOO--(_)--OOo-
  
"After eating an entire bull, a mountain lion felt so good he started 
roaring. He kept it up until a hunter came along and shot him... The moral: 
When you're full of bull, keep your mouth shut."
--Will Rogers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Christopher Bahn <cbbahn@gmail.com>
- **Date:** 2012-11-20T05:30:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb57059a-567d-4562-85f1-2b9487847599@googlegroups.com>`
- **In-Reply-To:** `<k8bhrq$s85$2@speranza.aioe.org>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <k8bhrq$s85$2@speranza.aioe.org>`

```
Am Sonntag, 18. November 2012 21:53:20 UTC+1 schrieb TruthSlave:
> On 11/11/12 09:49, Christopher Bahn wrote:
> 
…[40 more quoted lines elided]…
> interested you could have those in a zip.

Hi,

that would be great: christopher.bahn@aol.com
```

#### ↳ Re: New learning website for COBOL in the making

- **From:** quasar.chunawalla@gmail.com
- **Date:** 2012-11-19T22:48:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be06a56a-50db-4eef-94b2-ea4bd0dfdbf8@googlegroups.com>`
- **In-Reply-To:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com>`

```
Christopher, 

I would advise you to always use a Monospace font, while displaying Cobol Code Samples on your site.

Thank you very much,

Quasar Chunawala

On Sunday, November 11, 2012 3:19:05 PM UTC+5:30, Christopher Bahn wrote:
> Hi everybody,
> 
…[14 more quoted lines elided]…
> Christopher
```

##### ↳ ↳ Re: New learning website for COBOL in the making

- **From:** Christopher Bahn <cbbahn@gmail.com>
- **Date:** 2012-11-20T05:30:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33bd8497-627f-4060-9654-9553a094e2be@googlegroups.com>`
- **In-Reply-To:** `<be06a56a-50db-4eef-94b2-ea4bd0dfdbf8@googlegroups.com>`
- **References:** `<b8117739-d5ce-4041-90ca-98dc5e729a14@googlegroups.com> <be06a56a-50db-4eef-94b2-ea4bd0dfdbf8@googlegroups.com>`

```
Am Dienstag, 20. November 2012 07:48:58 UTC+1 schrieb quasar.c...@gmail.com:
> Christopher, 
> 
…[48 more quoted lines elided]…
> > Christopher

Thanks for the hint!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
