[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with netexpress

_6 messages · 3 participants · 2001-12_

---

### Problem with netexpress

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 2001-12-14T11:14:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C19D10C.1050203@medecine.unige.ch>`

```
Hello,
I use the NetExpress 3.0.14 and
when I compile my program I receive this message:

Starting rebuild
Rebuilding         observe.cob
C:\Src\Observe\observe.cob(3460,74): * 804-S Source limit of
2200 lines exceeded

I dont know why I have a limit of source code.
I'm bying this product with no limit? for lines sources code!

As anybody are some explanation?

Thanks in advance
Alain.
```

#### ↳ Re: Problem with netexpress

- **From:** jean.villemaire@microfocus.com (Jean Villemaire)
- **Date:** 2001-12-14T06:44:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b9b30ab.0112140644.3c0746f4@posting.google.com>`
- **References:** `<3C19D10C.1050203@medecine.unige.ch>`

```
Alain Chappuis <Alain.Chappuis@medecine.unige.ch> wrote in message news:<3C19D10C.1050203@medecine.unige.ch>...
> Hello,
> I use the NetExpress 3.0.14 and
…[22 more quoted lines elided]…
> +----------------------+----------------------------------------+

Alain

If you are using the Net Express University Edition product you are
limited to a maximum number of lines per program.  Net Express UE is a
low-cost compiler for Academic purposes only and therefore impose a
limit on the size of a program.  If you wish to exceed this limit then
you should upgrade to the production version of Net Express v3.1.

Jean Villemaire
Micro Focus
```

##### ↳ ↳ Re: Problem with netexpress

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2001-12-20T08:34:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C219492.7206D34E@medecine.unige.ch>`
- **References:** `<3C19D10C.1050203@medecine.unige.ch> <3b9b30ab.0112140644.3c0746f4@posting.google.com>`

```
Jean Villemaire a ï¿½crit :
> 
> Alain Chappuis <Alain.Chappuis@medecine.unige.ch> wrote in message news:<3C19D10C.1050203@medecine.unige.ch>...
> > Hello,
> > I use the NetExpress 3.0.14 and
> > when I compile my program I receive this message:

> If you are using the Net Express University Edition product you are
> limited to a maximum number of lines per program.  Net Express UE is a
> low-cost compiler for Academic purposes only and therefore impose a
> limit on the size of a program.  If you wish to exceed this limit then
> you should upgrade to the production version of Net Express v3.1.

Let me know...My program take approximatly 3002 lines with not
comments counted. For several days I have compiled without problem.
I does not understand why once it makes me this message?
For me that does not do anything, but it is a quite arbitrary
limit, you do not find-not.

Alain.
```

#### ↳ Re: Problem with netexpress

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-14T19:30:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1A53D1.30385934@shaw.ca>`
- **References:** `<3C19D10C.1050203@medecine.unige.ch>`

```


Alain Chappuis wrote:

> Hello,
> I use the NetExpress 3.0.14 and
…[11 more quoted lines elided]…
>

Alain,

Are you using University Edition ? I can't guarantee but there *might*
be a limitation. Check on-line help 'Limits", "Limitation" etc.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Problem with netexpress

- **From:** Alain Chappuis <alain.chappuis@medecine.unige.ch>
- **Date:** 2001-12-17T11:25:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1DC81D.A288EE3F@medecine.unige.ch>`
- **References:** `<3C19D10C.1050203@medecine.unige.ch> <3C1A53D1.30385934@shaw.ca>`

```
Hello again,

"James J. Gavan" a ï¿½crit :

> > I use the NetExpress 3.0.14 and
> > when I compile my program I receive this message:
…[9 more quoted lines elided]…
> > As anybody are some explanation?

> 
> Are you using University Edition ? 

Yes exactly I use it!

> I can't guarantee but there *might*
> be a limitation. Check on-line help 'Limits", "Limitation" etc.

But it's very stange comportment, doesn't some time 
the compiler stop with this limit, and of other time say anything?

I dont know why...

> Jimmy, Calgary AB

Thanks four yours ansered.

Alain.
```

###### ↳ ↳ ↳ Re: Problem with netexpress

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-17T20:44:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1E59B0.856E14B1@shaw.ca>`
- **References:** `<3C19D10C.1050203@medecine.unige.ch> <3C1A53D1.30385934@shaw.ca> <3C1DC81D.A288EE3F@medecine.unige.ch>`

```


Alain Chappuis wrote:

> > Are you using University Edition ?
>
> Yes exactly I use it!
>

Alain,

Sorry I can't answer your specific question, and it is frustrating when
something 'sometimes works' and other times 'doesn't work'. I haven't
got University Edition loaded but I did check the on-line help from  the
CD,  using the key "Limits". Under the Software License Agreement - it
does make the point NOT to have programs greater than 1,500 coded lines
- so that gives you a hint about limitations.

Who supports you in Geneva -  France, Germany or UK  ? The addresses
below :-

In the U.K.

Phone:  (01635) 565524
Fax:  (01635) 565312
Email:  mftsupp@merant.com

In Germany

Phone:  (089) 42094-150
Fax:  (089) 42094-118
Email:  hotline@merant.de

In France

Phone:  (1) 47 75 75 99
Fax:  (1) 47 75 75 80
Email:  frtsupp@merant.com

You may need to change the e-mail addresses from "merant" to
"microfocus".

Bon chance !

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
