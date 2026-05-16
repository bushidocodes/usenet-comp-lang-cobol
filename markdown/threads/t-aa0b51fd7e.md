[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 32-bit (NT) compiler for MF COBOL

_6 messages · 5 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### 32-bit (NT) compiler for MF COBOL

- **From:** "Ian Bate" <ian.bate@virgin.net>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net>`

```
Firstly, I don't program in COBOL at all.

We have a team who writes COBOL for an IBM MVS m/f using Micro Focus COBOL
(quite an old version).  They run COBOL Workbench on Windows 3.1.

There are certain pieces of code which we, (the PC Development team), get
from them and compile (using workbench) into a 16-bit DLL which we call from
Visual Basic (16-bit).

Trouble is, we are moving the Visual Basic code to 32-bit and so need to
(re)compile the DLL as 32-bit.  I don't know what we need.  The 32-bit
version of Workbench?  Net Express?  Mainframe Express?

I'd be grateful for any suggestions, Merant are being like really unhelpful
and not answering our support calls.
```

#### ↳ Re: 32-bit (NT) compiler for MF COBOL

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<801lc8$dc8$1@news.inet.tele.dk>`
- **References:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net>`

```
Hi Ian,
I am a little frustrated to hear that Merant is unhelpful. They have some
expensive 1st quality products, and I beleive they should show some interest
to your problem.

Nevertheless, your choice of product should depend on the flavour of the
Cobol Code you have to maintain. Your staff is satisfied?? with WB 3.1 but
you haven't told if you have CICS Option, IMS Option or in what way you
interact with VB.

MVS Express is for maintaining mainframe programs, NetExpress is for PC
programs including Internet applications. If you can buy WB 4.0 (and update
to 4.0.38), you will have a new and better workbench, similar to the one you
have now.

Please feel free to mail me if you like my opinion. Tell me a little bit
more about your use of Cobol now and in the future, and I will help you to
find the right product from Merant.

I am not employed by Merant or any of the distributors. I have been a
support engineer at a distributor for almost 10 years, but today I have no
commercial interest in your choice.

I just like the products and hate to see customers ignored.

Cheers
Ib
Ian Bate skrev i meddelelsen
<801hhu$hkt$1@nclient13-gui.server.virgin.net>...
>Firstly, I don't program in COBOL at all.
>
…[4 more quoted lines elided]…
>from them and compile (using workbench) into a 16-bit DLL which we call
from
>Visual Basic (16-bit).
>
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: 32-bit (NT) compiler for MF COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3824A3C4.A7BF3CEC@home.com>`
- **References:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net> <801lc8$dc8$1@news.inet.tele.dk>`

```


Ib Tanding wrote:
> 
> Hi Ian,
> I am a little frustrated to hear that Merant is unhelpful. They have some
> expensive 1st quality products, and I beleive they should show some interest
> to your problem.

Couldn't agree with you more Ib. Our friends should be taking a closer
look at Fujitsu spport philosophy; recall I wrote M/F kyboshed their
Compuserve forum ? In the NG we have seen nothing but glowing reports
about Fujitsu.

Jimmy
```

###### ↳ ↳ ↳ Re: 32-bit (NT) compiler for MF COBOL

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<802kkv$15l$1@news.inet.tele.dk>`
- **References:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net> <801lc8$dc8$1@news.inet.tele.dk> <3824A3C4.A7BF3CEC@home.com>`

```
Hi,
That is one of the reasons I had when I asked for more information, If Ian
is spending a huge amount of money, just to compile a few Cobol programs,
without special mainframeflavours as CICS- or IMS-options, he could save
money (and time) to follow your advice.

On the other hand, if he is using connection to SCCS, EBCDIC support,
integrated preprocessors etc.etc., he might feel more comfortable to get WB
4.0.

I hope that Ian gets the best for him - not just what I know best.

Ib

James J. Gavan skrev i meddelelsen <3824A3C4.A7BF3CEC@home.com>...
>
>
…[4 more quoted lines elided]…
>> expensive 1st quality products, and I beleive they should show some
interest
>> to your problem.
>
…[5 more quoted lines elided]…
>Jimmy
```

#### ↳ Re: 32-bit (NT) compiler for MF COBOL

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<801v5r$t84$1@aklobs.kc.net.nz>`
- **References:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net>`

```
Ian Bate <ian.bate@virgin.net> wrote:

: Trouble is, we are moving the Visual Basic code to 32-bit and so need to
: (re)compile the DLL as 32-bit.  I don't know what we need.  The 32-bit
: version of Workbench?  Net Express?  Mainframe Express?

Probably Workbench 4.0.  They do sell this, but they prefer not to.

: I'd be grateful for any suggestions, Merant are being like really unhelpful
: and not answering our support calls.
```

#### ↳ Re: 32-bit (NT) compiler for MF COBOL

- **From:** mark.warren@merant.com (Mark Warren)
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38278d3b.1812658@hyperion>`
- **References:** `<801hhu$hkt$1@nclient13-gui.server.virgin.net>`

```
On Sat, 6 Nov 1999 15:30:09 -0000, "Ian Bate" <ian.bate@virgin.net>
wrote:

>Firstly, I don't program in COBOL at all.
>
Don't worry about it, maybe one day ... ;-)

>We have a team who writes COBOL for an IBM MVS m/f using Micro Focus COBOL
>(quite an old version).  They run COBOL Workbench on Windows 3.1.
These people will want Mainframe Express to get the IMS support. It
really has moved on a long way since V3.1. In particular, there are
some very exciting IMS additional features out soon.

>Trouble is, we are moving the Visual Basic code to 32-bit and so need to
>(re)compile the DLL as 32-bit.  I don't know what we need.  The 32-bit
>version of Workbench?  Net Express?  Mainframe Express?
You'll need Net Express to do the linking of COBOL with another
language such as VB. Mainframe Express doesn't have the tools or run
time libraries to do the linking (but that's not really what it's
intended for). Once those DLLs are built, then there shouldn't be any
problem calling them from COBOL in Mainframe Express (watch out for
EBCDIC/ANSI issues though - use the "Non-mainframe debugging" option).

Don't worry too much about the need for two products. In reality not
everyone is going to need both - I guess the IMS people don't do a lot
of the VB work. But even if you did want everyone to have both, I'm
sure MERANT would be able to help out making a reasonable deal
(especially if upgrading from an older product). 

>
>I'd be grateful for any suggestions, Merant are being like really unhelpful
>and not answering our support calls.

Very disappointed to hear this. Let me know via email who you've been
talking to  and I'll see what I can do.
>

If you'd like any more information, please contact me via email and
I'll see what I can do.
Regards,
Mark Warren
MERANT International, Newbury, UK
Email: Mark.Warren@MERANT(removethis).COM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
