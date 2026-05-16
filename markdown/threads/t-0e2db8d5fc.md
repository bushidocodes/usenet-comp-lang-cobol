[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Saving Fujitsu Cobol source files

_9 messages · 7 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Saving Fujitsu Cobol source files

- **From:** ironhrse@inav.net (Brad)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b3b78.284973252@news.trxinc.com>`

```
Does anyone know offhand how to save a Cobol source   (just the text)
file in the Fujitsu 3.0  editor.  Whenever I do and then load it up to
the mainframe (TSO) it gets all askew and and told I have "non-Cobol",
I am guessing control characters that I can't characters in my text.
I imagine it's just a matter of one or two simple option but right now
I don't have time to dig through the doc (FINALS you know).

Thanks for the assistance,

Cyndy

cyndyh@hotmail.com

"Resist the Urge to Code"
```

#### ↳ Re: Saving Fujitsu Cobol source files

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b84eb.9434039@news1.ibm.net>`
- **References:** `<365b3b78.284973252@news.trxinc.com>`

```
On Tue, 24 Nov 1998 23:09:21 GMT, ironhrse@inav.net (Brad) wrote:

>Does anyone know offhand how to save a Cobol source   (just the text)
>file in the Fujitsu 3.0  editor.  Whenever I do and then load it up to
…[3 more quoted lines elided]…
>I don't have time to dig through the doc (FINALS you know).

Change your editor VIEW to standard colums and line numbers and that
will aid your transition.
```

##### ↳ ↳ Re: Saving Fujitsu Cobol source files

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7B2B6D8B8B5B1778.293092E1E503F97A.0A004031CBE149C2@library-proxy.airnews.net>`
- **References:** `<365b3b78.284973252@news.trxinc.com> <365b84eb.9434039@news1.ibm.net>`

```
On Wed, 25 Nov 1998 04:35:38 GMT, redsky@ibm.net (Thane Hubbell)
enlightened us:

>On Tue, 24 Nov 1998 23:09:21 GMT, ironhrse@inav.net (Brad) wrote:
>
…[8 more quoted lines elided]…
>will aid your transition.

I don't know about your mainframe environment, but mine doesn't like
lower case letters in the Cobol source, especially if it is on a
command line.  So, you might ensure that all of your Cobol source is
in upper case.

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Today's tip for annoying your relatives over the holidays:
Make beeping noises when you back up.


 Steve
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hql6$31p@dfw-ixnews3.ix.netcom.com>`
- **References:** `<365b3b78.284973252@news.trxinc.com> <365b84eb.9434039@news1.ibm.net> <7B2B6D8B8B5B1778.293092E1E503F97A.0A004031CBE149C2@library-proxy.airnews.net>`

```

SkippyPB wrote in message
   <snip>
>
>I don't know about your mainframe environment, but mine doesn't like
…[3 more quoted lines elided]…
>


I assume you are saying that you don't have an ANSI'85 compiler.  This
feature was made "Standard" over a decade ago!
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

_(reply depth: 4)_

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981126185411.13710.00000932@ng108.aol.com>`
- **References:** `<73hql6$31p@dfw-ixnews3.ix.netcom.com>`

```
>> So, you might ensure that all of your Cobol source is
>> in upper case.

This falls into that same rut some of us old dodgers get cranked
up about.  

I wrote source for so many years in all uppercase that I cannot
bring myself to write it any other way.  All the other programmers
used to laugh and call me names.  Now they just remind me to
change my Depends regularly and otherwise ignore me.

JC Jones.
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

_(reply depth: 5)_

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365E1940.CA431021@mindspring.com>`
- **References:** `<73hql6$31p@dfw-ixnews3.ix.netcom.com> <19981126185411.13710.00000932@ng108.aol.com>`

```
keep on writing it in any case (upper or lower) you damn well please. 
good code is good code regardless of the case, font, or whateverthehell
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

_(reply depth: 5)_

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OPFerMxG#GA.96@upnetnews03>`
- **References:** `<73hql6$31p@dfw-ixnews3.ix.netcom.com> <19981126185411.13710.00000932@ng108.aol.com>`

```

JCJ0347 wrote in message <19981126185411.13710.00000932@ng108.aol.com>...
>>> So, you might ensure that all of your Cobol source is
>>> in upper case.
…[7 more quoted lines elided]…
>change my Depends regularly and otherwise ignore me.


It seems that "go to DEPENDing" takes on a whole new meaning here? <G>


>JC Jones.
>
>
>
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

_(reply depth: 4)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<815E2BE2D0A06E5E.271EC548D4BDFAD2.F956EC88D776BCA3@library-proxy.airnews.net>`
- **References:** `<365b3b78.284973252@news.trxinc.com> <365b84eb.9434039@news1.ibm.net> <7B2B6D8B8B5B1778.293092E1E503F97A.0A004031CBE149C2@library-proxy.airnews.net> <73hql6$31p@dfw-ixnews3.ix.netcom.com>`

```
On Wed, 25 Nov 1998 12:50:55 -0800, "William M. Klein"
<wmklein@ix.netcom.com> enlightened us:

>
>SkippyPB wrote in message
…[11 more quoted lines elided]…
>

Yes we do have an ANSI'85 compiler.  Its not the Cobol that complains,
it is something else that I just can't remember right now.  Happens
when I write stuff on the PC then upload to the mainframe via TSO,
which was what the original poster was questioning.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Today's tip for annoying your relatives over the holidays:
Make beeping noises when you back up.


 Steve
```

###### ↳ ↳ ↳ Re: Saving Fujitsu Cobol source files

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73mtbj$ios@dfw-ixnews7.ix.netcom.com>`
- **References:** `<365b3b78.284973252@news.trxinc.com> <365b84eb.9434039@news1.ibm.net> <7B2B6D8B8B5B1778.293092E1E503F97A.0A004031CBE149C2@library-proxy.airnews.net> <73hql6$31p@dfw-ixnews3.ix.netcom.com> <815E2BE2D0A06E5E.271EC548D4BDFAD2.F956EC88D776BCA3@library-proxy.airnews.net>`

```

SkippyPB wrote in message
   <snip>
>>
>>I assume you are saying that you don't have an ANSI'85 compiler.  This
…[7 more quoted lines elided]…
>


From my days working at Micro Focus (where such problems were reported every
month or two), a couple of things to look at/think about:

1) Check your "codeset" setting on both the PC and the mainframe.  This is
particularly a problem if you are in England or some other "English
speaking" country that does not use the US dollar sign as its currency
sign - but does use the same "normal" alphabetic characters.

2) Make certain that you have some facility for NOT converting any literals
with un-printable (or "extended") characters - or converts them in a
regulated fashion (i.e. that when you convert from the PC to the mainframe
and back it gets back to the original character.  Believe it or not, this is
NOT a trivial task)

3) Always remember to use a facility that converts from "line sequential"
(PC) to "fixed length" (mainframe).

If you still have problems with mixed case source code, I would be
interested in hearing what the problems are (as we were always able to
"resolve" them back in my MF days).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
