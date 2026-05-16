[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with cobol cics program calling assembler module

_10 messages · 5 participants · 1998-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Problem with cobol cics program calling assembler module

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35910C96.5082@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

Erich Quant wrote:
 
> I have a big problem and hope you could give me a hint: We have CICS
> COBOL/COBOL2 application system that is using several assembler 
…[4 more quoted lines elided]…
> application.
 
I seem to remember reading somewhere that a called program in CICS 
environment should not have an alternate entry point, i.e. ENTRY point 
of the module should be same as the CSECT name. I have looked but have 
not yet located where I read this; can anyone else confirm this?

Another thing to check:  Your ASSTSTP module is set to use AMODE=31 
and RMODE=ANY.  What about the calling program? 
"If you are passing control between programs executing in different 
addressing modes, you must change the AMODE indicator in the PSW". 
(MVS Assembler Services Reference, GC28-1910).

Module ASSTSTP does not issue any CICS commands, so it does not 
have to be processed by CICS Translator, nor do you need an entry 
for it in the PPT.  That being so, all CALLs to ASSTSTP *have* to 
be static; neither dynamic CALLs nor a CICS LINK is possible.

Hope this is of some help!
MfG, 
Bal
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mt51o$f41$1@nnrp1.dejanews.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net>`

```

In article <35910C96.5082@ibm.net>,
  oberoi@ibm.net wrote:
>
> Erich Quant wrote:
…[13 more quoted lines elided]…
>

I have never tried to use an alternate entry in such a program, but I can't
imagine that this should cause any problem at all.

> Another thing to check:  Your ASSTSTP module is set to use AMODE=31
> and RMODE=ANY.  What about the calling program?

Another question which seems much more important: Is your assembler-module
linked reentrant? And is it really reentrant?

> "If you are passing control between programs executing in different
> addressing modes, you must change the AMODE indicator in the PSW".
> (MVS Assembler Services Reference, GC28-1910).
>

The dynamic COBOL-call does this automatically for you!

> Module ASSTSTP does not issue any CICS commands, so it does not
> have to be processed by CICS Translator, nor do you need an entry
> for it in the PPT.  That being so, all CALLs to ASSTSTP *have* to
> be static; neither dynamic CALLs nor a CICS LINK is possible.
>

I am shure that you have to define your ASSEMBLER in the PPT when called
dynamically from COBOL. And via COBOL, you don't load the module from the
STEPLIB but rather from the DFHRPL. Only ASSEMBLER-ASSEMBLER via the LINK- or
LOAD-macro works directly without CICS between (and with poor performance for
the whole CICS)! Both dynamic calls and CICS LINK work fine. I wrote a little
ASSEMBLER which is used in production via dynamic call since one year and I
use CICS LINK with several different ASSEMBLER routines.

> Hope this is of some help!
> MfG,
…[8 more quoted lines elided]…
>

Cheers

Daniel


"Murpy was an optimist!"

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3593AA30.704E@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com>`

```

daniel.jacot@winterthur.ch wrote:


> 
> > "If you are passing control between programs executing in different
…[4 more quoted lines elided]…
> The dynamic COBOL-call does this automatically for you!

Agreed. However, unless Erich has the time and inclination to make 
changes to his Assembler programs, dynamic CALLs are not an option.
For a program to be called dynamically it has to satisfy several 
requirements.  A couple I can think of are:
1. It must be CICS-aware, i.e. it must be coded to expect 
   EIB and CommArea as the first two among the parameters that the 
   calling program passes to it.
2. The subprogram should be passed through the Translator prior to 
   assembly, and it should have an entry in the PPT. 

> 
> > Another thing to check:  Your ASSTSTP module is set to use 
…[3 more quoted lines elided]…
> assembler-module linked reentrant? And is it really reentrant?

If the CALL to the subprogram is static (i.e. it is linkedited as 
part of *each* calling COBOL load module) then reentrancy is not a 
requirement; it's enough if it's serially reuseable, or 
"quasi-reentrant". 

Regards,
Bal
----- 
oberoi@ibm.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things, 
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35945209.79B9@sprynet.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net>`

```

Bal Oberoi wrote:
> 
> > unknown person wrote:
…[15 more quoted lines elided]…
>    assembly, and it should have an entry in the PPT.

I believe this is not true.  I have a completely batch program called CHKALPHA.PHASE.
As long as it is in the PPT, I can call it the following way from a CICS program:

working-storage section.
  01  CHKALPHA    PIC X(8)   VALUE 'CHKALPHA'.

procedure division.
  CALL CHKALPHA USING [parameters].

Because I am calling it, not LINKing to it, the EIB and COMMAREAs are not
required in the called program.

Now, CHKALPHA is a COBOL II program, not an assembler program, but I can't
imagine why assembler programs could not be called the same way.

Note that we use VSE, not MVS, but I doubt this makes a difference.
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 4)_

- **From:** stevewie@apk.dot.net (SkippyPB)
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<359523ca.3949052@news.apk.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com>`

```

On Fri, 26 Jun 1998 18:59:37 -0700, Frank Swarbrick
<infocat@sprynet.com> was insane enough to write:

>Bal Oberoi wrote:
>> 
…[37 more quoted lines elided]…
>work: frank.swarbrick@1stbank.com

You are correct.  This is a static call.  The object of CHKALPHA is
embedded in the object of the calling program at linkedit time and,
therefore, doesn't need a PPT entry nor needs to be aware of the EIB
and COMMAREA.  However, if the program was called using EXEC CICS LINK
or EXEC CICS XCTL, it would have to be CICS eligible.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Ambition is a poor excuse for not having enough sense to be lazy.
 Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6n41at$5lg@bgtnsc03.worldnet.att.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net>`

```

SkippyPB wrote:
> 
(snip)
> >I believe this is not true.  I have a completely batch program called CHKALPHA.PHASE.
> >As long as it is in the PPT, I can call it the following way from a CICS program:
…[23 more quoted lines elided]…
> or EXEC CICS XCTL, it would have to be CICS eligible.

No, no, calling a data_name is *always* a dynamic call, even with the
NODYNAM compiler option. If you're calling an Asm pgm and it doesn't
issue CICS commands, you needn't pass the EIB & Commarea; but you
*always* need a PPT entry for a dynamic call (that's inherent in it's
being dynamic). In the above case the called module (CHKALPHA) will not
be made part of the load module by the linkage editor/Binder.

I think you're mixing the notions of dynamic vs. static with the ability
to issue CICS commands or not.

Bill Lynch

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 6)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3595B520.3A01@sprynet.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net>`

```

Bill Lynch wrote:
> 
> SkippyPB wrote:
…[37 more quoted lines elided]…
> to issue CICS commands or not.

I didn't get SkippyPB's reply to my message, but thanks for coming to my
defense!  You are exactly correct.  And I can prove it because I never compiled
a CHKALPHA.OBJ, and therefore there's no possible way it could have linked into
my program!
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 6)_

- **From:** stevewie@apk.dot.net (SkippyPB)
- **Date:** 1998-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35986d71.3026751@news.apk.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net>`

```

On Sat, 27 Jun 1998 20:05:02 -0400, Bill Lynch
<wblynch@worldnet.att.net> was insane enough to write:

>SkippyPB wrote:
>> 
…[40 more quoted lines elided]…
>(snipped)

Bill, you are absolutely correct.  I missed seeing that he was calling
the program using a data name.  Got confused because the data name
value and the actual phase name were the same.  

Sorry about that!

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Everyone has a photographic memory. Some don't have film.
 Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 7)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1998-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6n693c$7o8@bgtnsc03.worldnet.att.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net> <35986d71.3026751@news.apk.net>`

```

SkippyPB wrote:
> 
(snip)
> >
> >No, no, calling a data_name is *always* a dynamic call, even with the
…[15 more quoted lines elided]…
> value and the actual phase name were the same.

Not to worry - I do that all the time, too!

Bill Lynch :-)

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 4)_

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3595300F.66C2@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com>`

```

Frank Swarbrick wrote:

> > > > "If you are passing control between programs executing in 
> > > > different addressing modes, you must change the AMODE indicator 
> > > > in the PSW".  (MVS Assembler Services Reference, GC28-1910).

> > > The dynamic COBOL-call does this automatically for you!

> >
> > Agreed. However, unless Erich has the time and inclination to make
…[7 more quoted lines elided]…
> >    assembly, and it should have an entry in the PPT.

> 
> I believe this is not true.  I have a completely batch program called 
…[15 more quoted lines elided]…
> Note that we use VSE, not MVS, but I doubt this makes a difference.

Well, I stand corrected! I have never seen it done, but the manual, 
(COBOL for MVS/VM, Prog. Gde.), certainly backs you up:

* CALL identifier can be used with the NODYNAM compiler option to 
  dynamically call a program.  Called programs can contain any 
  function supported by CICS for the language.  Dynamically called 
  programs have to be defined in the CICS program processing table 
  (PPT).
* If you are calling a COBOL program that has been translated, you 
  must pass DFHEIBLK and DFHCOMMAREA as the first two parameters in 
  the CALL statement.

It's a tad ambiguous. But based on your experience it would appear 
that: 
  If a subprogram, called dynamically, does not use any CICS 
  functions, it does not have to be translated. 
  And if the Translator did not stick any CICS-related stuff into the 
  code, it does not have to be passed pointers to EIB and CommArea.
  In any event, for a dynamic CALL to work, the called program must 
  have an entry in the PPT.

Thanks for sharing your experience, Frank.  

Best of regards,
Bal
----- 
oberoi@ibm.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things, 
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
