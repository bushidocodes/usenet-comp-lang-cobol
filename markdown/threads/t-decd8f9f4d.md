[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen-IO

_7 messages · 6 participants · 1998-12_

---

### Screen-IO

- **From:** iriepeer@my-dejanews.com
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<748onl$41i$1@nnrp1.dejanews.com>`

```
Hi,

I know there is a function called "screen-IO".
>> CALL "SCREEN-IO" USING ......

It can be used to read and write buffers from/to the screen. I am working in
Micro Focus Workbench, but for some reason there is no help available. I
reaLly need to know how this function works, Including the parameters you
have to send to it aso. Can anyone please help me? Also, please reply to this
address : Stoopspet.Nospam@Hotmail.com but remove the "NoSpam" part !! :-)

Tnx a lot in advance !!

Greetings, Peace

IriePeer

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Screen-IO

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36681609.325168617@news.freeserve.net>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com>`

```
On Fri, 04 Dec 1998 13:40:05 GMT, iriepeer@my-dejanews.com wrote:

>Hi,
>
>I know there is a function called "screen-IO".
>>> CALL "SCREEN-IO" USING ......

Are you sure it's not CALL SCREEN-IO USING ....

where SCREEN-IO is a level 78 defined as x"B7" ?

>
>It can be used to read and write buffers from/to the screen. I am working in
>Micro Focus Workbench, but for some reason there is no help available. 

Look up CALL BY NUMBER in the Operating Guide.


>I
>reaLly need to know how this function works, Including the parameters you
>have to send to it aso. Can anyone please help me? Also, please reply to this
>address : Stoopspet.Nospam@Hotmail.com but remove the "NoSpam" part !! :-)

ok. but you'll have to use the newsgroup to reply to me as I don't
accept any mail with a hotmail.com domain on the end (or msn either)
```

##### ↳ ↳ Re: Screen-IO

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OvMGErCI#GA.256@upnetnews03>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com> <36681609.325168617@news.freeserve.net>`

```

Shaun C. Murray wrote in message <36681609.325168617@news.freeserve.net>...
>On Fri, 04 Dec 1998 13:40:05 GMT, iriepeer@my-dejanews.com wrote:
>
…[10 more quoted lines elided]…
>>It can be used to read and write buffers from/to the screen. I am working
in
>>Micro Focus Workbench, but for some reason there is no help available.
>
…[5 more quoted lines elided]…
>>have to send to it aso. Can anyone please help me? Also, please reply to
this
>>address : Stoopspet.Nospam@Hotmail.com but remove the "NoSpam" part !! :-)
>
>ok. but you'll have to use the newsgroup to reply to me as I don't
>accept any mail with a hotmail.com domain on the end (or msn either)
>


Would you also deny acceptance of email originated in MS Outlook 98 or MS
Outlook Express or Windows Messaging?  That would make as much sense to me
as including all addresses in the MSN.com domain in your spam filter.  I've
been using MSN.com for internet access, along with Compuserve.com, for
several years and it has been my experience that I get very, very little
SPAM originated via the MSN.com domain.  But you are definitely on the right
track about hotmail.com, which was purchased by M$ a few months back.

BTW, I just read that hotmail now has a total of over 30 million users, and
I definitely agree that way too many of them are prolific spammers.
```

###### ↳ ↳ ↳ Re: Screen-IO

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74bbci$bo8$1@news.igs.net>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com> <36681609.325168617@news.freeserve.net> <OvMGErCI#GA.256@upnetnews03>`

```
Dennis J. Minette wrote in message ...

>BTW, I just read that hotmail now has a total of over 30 million users, and
>I definitely agree that way too many of them are prolific spammers.


No, they only have 7 users.  Those seven post
using 30 million names.
```

###### ↳ ↳ ↳ Re: Screen-IO

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1998-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367658ed.77841850@news.freeserve.net>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com> <36681609.325168617@news.freeserve.net> <OvMGErCI#GA.256@upnetnews03>`

```
On Sat, 5 Dec 1998 03:34:09 -0500, "Dennis J. Minette"
<dennis_minette@email.msn.com> wrote:


>
>Would you also deny acceptance of email originated in MS Outlook 98 or MS
>Outlook Express or Windows Messaging? 

No - not that fussy.

> That would make as much sense to me
>as including all addresses in the MSN.com domain in your spam filter. 

It's a political thing but it does sort out the clueless. I actually
do accept msn.com and aol.com mail but it goes into my non-important
mail folder and I look through it at my leisure.

> I've
>been using MSN.com for internet access, along with Compuserve.com, for
>several years and it has been my experience that I get very, very little
>SPAM originated via the MSN.com domain.  But you are definitely on the right
>track about hotmail.com, which was purchased by M$ a few months back.

Both of which are why I don't accept hotmail at all. M$ have been
buying up quite a few companies like hotmail. LinkExchange being
another important one of late. Rumour has it that hotmail use Linux
for their servers although M$ wanted them to use NT servers - the NT
servers weren't reliable enough. ;-)

>
>BTW, I just read that hotmail now has a total of over 30 million users, and
>I definitely agree that way too many of them are prolific spammers.

...and pirates and hackers. For instance, a recent case was a hotmail
account being used inside a trojan horse. The trojan would email your
account details to a hotmail account. 700 accounts and passwords were
stolen this way before the author of the Amiga TCP/IP stack that was
being accused of piracy found out about it.
```

#### ↳ Re: Screen-IO

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-YdzDEWd2LEwM@Dwight_Miller.iix.com>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com>`

```
On Fri, 4 Dec 1998 13:40:05, iriepeer@my-dejanews.com wrote:

> Hi,
> 
…[7 more quoted lines elided]…
> address : Stoopspet.Nospam@Hotmail.com but remove the "NoSpam" part !! :-)

It  looks to me like you are using the NORCOM Product SCREENIO - check
their website for details, or look for your SCREENIO book.
```

#### ↳ Re: Screen-IO

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7498dr$g56@hyperion.mfltd.co.uk>`
- **References:** `<748onl$41i$1@nnrp1.dejanews.com>`

```
I suspect that the eason you cannot find any help on this call is that it is
not part of the Workbench product (as far as I am aware) . Perhaps you are
using a module from another company/product


iriepeer@my-dejanews.com wrote in message
<748onl$41i$1@nnrp1.dejanews.com>...
>Hi,
>
…[3 more quoted lines elided]…
>It can be used to read and write buffers from/to the screen. I am working
in
>Micro Focus Workbench, but for some reason there is no help available. I
>reaLly need to know how this function works, Including the parameters you
>have to send to it aso. Can anyone please help me? Also, please reply to
this
>address : Stoopspet.Nospam@Hotmail.com but remove the "NoSpam" part !! :-)
>
…[7 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
