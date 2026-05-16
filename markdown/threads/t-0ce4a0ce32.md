[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Warning/Errors Line Numbers

_6 messages · 5 participants · 2010-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Warning/Errors Line Numbers

- **From:** Derek Schrock <dereks@lifeofadishwasher.com>
- **Date:** 2010-11-17T11:43:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com>`

```
Does anyone know if there's a compiler directive for MC SE 4.0 SP2
that reports the original line number before copy books are included
when an error or warning is reported?
```

#### ↳ Re: Microfocus Warning/Errors Line Numbers

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-17T18:01:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tV_Eo.32251$lL3.21536@newsfe08.iad>`
- **In-Reply-To:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com>`
- **References:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com>`

```
On 11/17/2010 12:43 PM, Derek Schrock wrote:
> Does anyone know if there's a compiler directive for MC SE 4.0 SP2
> that reports the original line number before copy books are included
> when an error or warning is reported?

I'd been inclined to say 'No'. I take it 'SE" above refers to Server 
Express ? It's copacetic with Net Express, so they will both do the same 
thing.

Not quite what you are after, but it illustrates - I have originals of 
some of my classes in a separate folder \Copylib - these are a bunch 
which are constantly re-used with different projects, in Develpment ode 
- I've no intent of producing DLLs or EXEs. For compatibility, if 
changing \Copylib\Program-A I compile in that folder\project and ANY 
errors including errors in the structure of any copyfiles get reported 
with sequential line numbering for the WHOLE source of Program-A.

Now I might have a small Project, like 99-Bottles coming up which uses 
\Copylib\Program-A and the Bottles project has a file :-

*>----------- Program-A.COB-------------
copy "\Copylib\Program-A.cbl".
*>--------------------------------------

That one-liner is added to the Bottles project and is shown in the IDE 
for Bottles and using the Alt + F2 brings up the source of Program-A, 
(the original). Note, only yesterday hit on the idea of giving the file 
above the extension ...COB to differentiate between the receiving 
project with ....CBL files and those ....COB files which refer to \Copylib.

OK, so sometimes I'll make changes to what is if you like currently 
Program-A.COB because I'm cross referencing to other programs ...COB or 
more likely the traditional ....CBL in the Bottles Project.

I'll get errors perhaps, but like you wont get correct references to the 
prime text or copyfiles because they don't match. I have to get back to 
\Copylib\Program-A.cbl and do a re-compile and that takes me direct to 
the error lines.

I said 'No' at the beginning, because when first designing DIRECTIVES, I 
very much doubt M/F took into account dumb users like me buggering 
around with project structures :-).

You could raise the question in the old M/F Forum, but they appear to 
have tailed-off on that, particularly Net Express. Might well be 
different for Server Express.

Jimmy, Calgary AB
```

#### ↳ Re: Microfocus Warning/Errors Line Numbers

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-18T05:58:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6d79b207-bad4-440d-af0c-9fa70acbd3e4@t13g2000yqm.googlegroups.com>`
- **References:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com>`

```
On Nov 17, 7:43 pm, Derek Schrock <der...@lifeofadishwasher.com>
wrote:
> Does anyone know if there's a compiler directive for MC SE 4.0 SP2
> that reports the original line number before copy books are included
> when an error or warning is reported?

There appears to be no obvious directive but you could try NOCOPYLIST
which suppresses the expansion of COPY libs.
```

##### ↳ ↳ Re: Microfocus Warning/Errors Line Numbers

- **From:** abrsvc <dansabrservices@yahoo.com>
- **Date:** 2010-11-18T06:54:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f803a10e-b57d-4724-9100-77abbf3902bf@g25g2000yqn.googlegroups.com>`
- **References:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com> <6d79b207-bad4-440d-af0c-9fa70acbd3e4@t13g2000yqm.googlegroups.com>`

```
On Nov 18, 8:58 am, Alistair Maclean
<alistair.j.l.macl...@googlemail.com> wrote:
> On Nov 17, 7:43 pm, Derek Schrock <der...@lifeofadishwasher.com>
> wrote:
…[6 more quoted lines elided]…
> which suppresses the expansion of COPY libs.

You are correct in that the "nocopylsit" will suppress the listing of
the copybooks, but it will not affect the line number generation.

Dan
```

###### ↳ ↳ ↳ Re: Microfocus Warning/Errors Line Numbers

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-18T10:16:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<293452a8-f48e-4a85-9cb9-eeb3deb0cb02@l8g2000yqh.googlegroups.com>`
- **References:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com> <6d79b207-bad4-440d-af0c-9fa70acbd3e4@t13g2000yqm.googlegroups.com> <f803a10e-b57d-4724-9100-77abbf3902bf@g25g2000yqn.googlegroups.com>`

```
On Nov 18, 2:54 pm, abrsvc <dansabrservi...@yahoo.com> wrote:
> On Nov 18, 8:58 am, Alistair Maclean
>
…[14 more quoted lines elided]…
> Dan

Then the answer to your original question is: No. Sorry.
```

###### ↳ ↳ ↳ Re: Microfocus Warning/Errors Line Numbers

- **From:** Wiggy <wignomore@nospam.btopenworld.com>
- **Date:** 2010-11-19T01:14:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XeGdnfoaTvL6UnjRnZ2dnUVZ8tWdnZ2d@bt.com>`
- **In-Reply-To:** `<f803a10e-b57d-4724-9100-77abbf3902bf@g25g2000yqn.googlegroups.com>`
- **References:** `<738b690c-78f2-4082-bc35-621da8d7da1e@n30g2000vbb.googlegroups.com> <6d79b207-bad4-440d-af0c-9fa70acbd3e4@t13g2000yqm.googlegroups.com> <f803a10e-b57d-4724-9100-77abbf3902bf@g25g2000yqn.googlegroups.com>`

```
On 18/11/2010 14:54, abrsvc wrote:
> On Nov 18, 8:58 am, Alistair Maclean
> <alistair.j.l.macl...@googlemail.com>  wrote:
…[13 more quoted lines elided]…
> Dan

ERRFORMAT(2) may have the desired effect. I've only tried it on Windows :

 >cobol myapp nognt list() errformat(2);
Micro Focus Net Express
Version 6.0.11055  Copyright (C) 1984-2010 Micro Focus (IP) Limited.
URN AXCGG/AA0/00000
     50     accept svr
**    COBCH0012S Operand SVR is not declared  : myapp.cbl(27,21)
     58     END-EXEC
**    COBES0109S SVR is not a data item.   : myapp.cbl(35,19)
* Checking complete - errors found

The "50" indicates the listing line number including the expanded 
copybook, but the myapp.cbl(27,21) shows the real source line and column.

The documentation can be found at 
http://documentation.microfocus.com:8080/help/index.jsp?topic=/com.microfocus.eclipse.infocenter.studee60ux.sp01/HRCDRHCDIRCI.html 


Hope that helps,
SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
