[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing Parameters - Error 104

_3 messages · 3 participants · 2000-12_

---

### Re: Passing Parameters - Error 104

- **From:** "John P Fife" <jfife1@home.com>
- **Date:** 2000-12-15T17:30:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yys_5.70615$15.15180388@news1.rdc1.az.home.com>`
- **References:** `<90k19p$32b$1@nnrp1.deja.com> <90ken5$lov$1@slb1.atl.mindspring.net> <90khou$foh$1@nnrp1.deja.com> <90kkc2$21p$1@slb0.atl.mindspring.net>`

```
Bill, Just a question wouldn't it cause less confusion is you just stated
that it is a physical address that is being passed from the calling program
to the called program. This is the reasons the names do not have to match,
you just have to have the same sequence and you should have the same size
otherwise you could wipe out pieces of core storage between the 2 programs.
I know you stated all this it just took a while to digest.

John
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:90kkc2$21p$1@slb0.atl.mindspring.net...
> You don't understand the linkage section completely (yet).
>
> The linkage section in a CALLED program (subprogram) matches the storage
> (usually Working-Storage - but also possibly File or other sections) in
the
> CALLING program.  The "matching" is NOT done by name or anything like that
> it.  It is done by "matching" the parameters in the order they appear in
the
> CALL USING statement (in the CALLING program) to those in the Procedure
> Division USING statement (of the called program).  For example, the
…[48 more quoted lines elided]…
> 4) The field descriptions do NOT need to be the same (although the
"length"
> should be).  What happens when this rule is "violated" depends on the
> operating system and the compiler - but it is NOT a good thing to do.
…[41 more quoted lines elided]…
>
```

#### ↳ Re: Passing Parameters - Error 104

- **From:** "������������������������ ���������������������" <dksoft@otenet.gr>
- **Date:** 2000-12-16T13:29:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91fj7r$157u$1@ulysses.noc.ntua.gr>`
- **References:** `<90k19p$32b$1@nnrp1.deja.com> <90ken5$lov$1@slb1.atl.mindspring.net> <90khou$foh$1@nnrp1.deja.com> <90kkc2$21p$1@slb0.atl.mindspring.net> <Yys_5.70615$15.15180388@news1.rdc1.az.home.com>`

```
CHANGES MADE IN PROGRAM 2.
LINKAGE SECTION.
01 LS1 PIC 99.
01 LS2.
     02 LS2-A PIC XX.
     02 LS2-B PIC X.
01 LS3 PIC XX.
PROCEDURE DIVISION USING LS1 LS2 LS3.


IT WORKS.


"John P Fife" <jfife1@home.com> wrote in message
news:Yys_5.70615$15.15180388@news1.rdc1.az.home.com...
> Bill, Just a question wouldn't it cause less confusion is you just stated
> that it is a physical address that is being passed from the calling
program
> to the called program. This is the reasons the names do not have to match,
> you just have to have the same sequence and you should have the same size
> otherwise you could wipe out pieces of core storage between the 2
programs.
> I know you stated all this it just took a while to digest.
>
…[8 more quoted lines elided]…
> > CALLING program.  The "matching" is NOT done by name or anything like
that
> > it.  It is done by "matching" the parameters in the order they appear in
> the
…[41 more quoted lines elided]…
> > 1) The calling program puts the fields in Working-Storage and CALL
USING,
> > the called program puts them in Linkage and PROCEDURE DIVISION USING.
> >
…[3 more quoted lines elided]…
> > Procedure Division USING statement - it is the LATTER that must match
the
> > CALL using statement
> >
…[6 more quoted lines elided]…
> >   It is "nice" to put things in the same order, with the same names
(often
> > with different prefixes) and with the same data descriptions - but this
is
> > NOT how the compiler matches parameters.
> >
…[37 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Passing Parameters - Error 104

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-16T12:45:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91gd6i$7uo$1@slb0.atl.mindspring.net>`
- **References:** `<90k19p$32b$1@nnrp1.deja.com> <90ken5$lov$1@slb1.atl.mindspring.net> <90khou$foh$1@nnrp1.deja.com> <90kkc2$21p$1@slb0.atl.mindspring.net> <Yys_5.70615$15.15180388@news1.rdc1.az.home.com> <91fj7r$157u$1@ulysses.noc.ntua.gr>`

```
I understand that this would work AS WELL - but so would the original. The
entire point was that you did NOT need to have the Linkage Section items in
the same order as the Procedure Division USING statement. (This doesn't mean
that you shouldn't or can't - but that you don't have to)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
