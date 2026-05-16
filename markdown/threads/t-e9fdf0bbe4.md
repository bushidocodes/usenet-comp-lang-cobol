[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wacky scope terminators was Re: IF-statement

_7 messages · 5 participants · 1999-07_

---

### Re: Wacky scope terminators was Re: IF-statement

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <MSN.Bus.News@rmpcp.com>
- **Date:** 1999-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eD0MbZxy#GA.356@cpmsnbbsa05>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca>`

```
Isn't there a Not on size error clause to provide the else to the on size
error clause, just like Not at end?


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmp@rmpcp.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

#### ↳ Re: Wacky scope terminators was Re: IF-statement

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378A43D2.38CAD94B@IMN.nl>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05>`

```
"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> 
> Isn't there a Not on size error clause to provide the else to the on size
> error clause, just like Not at end?

Yes, for every "on/at xxx" there is a "not on/at xxx"
```

##### ↳ ↳ Re: Wacky scope terminators was Re: IF-statement

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mdqgv$4mv@dfw-ixnews16.ix.netcom.com>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05> <378A43D2.38CAD94B@IMN.nl>`

```

The COBOL Frog <H.Klink@IMN.nl> wrote in message
news:378A43D2.38CAD94B@IMN.nl...
> "Robert M. Pritchett - RMP Consulting Partners LLC" wrote:
> >
> > Isn't there a Not on size error clause to provide the else to the on
size
> > error clause, just like Not at end?
>
> Yes, for every "on/at xxx" there is a "not on/at xxx"
>
>

Just to be "obscure",

Check out the CALL verb.

There is a
    "NOT ON EXCEPTION" phrase

but there is NO
    "NOT ON OVERFLOW" phrase

(Hence, ON OVERFLOW is going into the archaic or obsolete category in the
NEXT Standard).

I have heard the "historical" reasons for this, but it is just a bit of
trivia for your amusement.
```

###### ↳ ↳ ↳ Re: Wacky scope terminators was Re: IF-statement

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oKJi3.5863$iA1.27092@news4.mia>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05> <378A43D2.38CAD94B@IMN.nl> <7mdqgv$4mv@dfw-ixnews16.ix.netcom.com>`

```
William M. Klein wrote:
>
>Just to be "obscure",
…[13 more quoted lines elided]…
>trivia for your amusement.

If you permit two 'NOT ON <execution>' phrases within one command, and
no exception occurs, in what order should they both be executed?  ;-)
```

###### ↳ ↳ ↳ Re: Wacky scope terminators was Re: IF-statement

_(reply depth: 4)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378CFB49.32A6D052@IMN.nl>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05> <378A43D2.38CAD94B@IMN.nl> <7mdqgv$4mv@dfw-ixnews16.ix.netcom.com> <oKJi3.5863$iA1.27092@news4.mia>`

```
Judson McClendon wrote:
> 
> If you permit two 'NOT ON <execution>' phrases within one command, and
> no exception occurs, in what order should they both be executed?  ;-)
I prefer the reverse order (2nd one 1st). 'cause of the NOT NOT.
:)
> --
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)
> Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
> "For God so loved the world that He gave His only begotten Son, that
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: Wacky scope terminators was Re: IF-statement

_(reply depth: 4)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378d1efb.4469466@netnews>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05> <378A43D2.38CAD94B@IMN.nl> <7mdqgv$4mv@dfw-ixnews16.ix.netcom.com> <oKJi3.5863$iA1.27092@news4.mia>`

```
'Twas Tue, 13 Jul 1999 11:23:42 -0500, when "Judson McClendon"
<judmc123@bellsouth.net> illuminated comp.lang.cobol thusly:

> William M. Klein wrote:
> >
…[19 more quoted lines elided]…
> Judson McClendon      judmc123@bellsouth.net  (remove numbers)

No, if there's an ON OVERFLOW clause, you can't have [NOT] ON EXCEPTION.  

Bill, I wasn't familiar with this one.  Now that I look it up, I don't
find the word "arcahic" or "obsolete" in an the description of CALL.
```

###### ↳ ↳ ↳ Re: Wacky scope terminators was Re: IF-statement

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mji7d$5st@dfw-ixnews7.ix.netcom.com>`
- **References:** `<7lfkt7$q1j$1@endevour.netg.se> <377BE098.51CC@compaq.com> <377CBF37.D1AF156A@NOSPAMhome.com> <377d352a.8529028@netnews> <#VOZzkRx#GA.306@nih2naaa.prod2.compuserve.com> <377E06FA.666993E6@zip.com.au> <3782036B.9DA4E214@NOSPAMhome.com> <37834C0E.4BDB193@zip.com.au> <378356A2.D5CFB608@NOSPAMhome.com> <3783f0d3.90480471@news1.ibm.net> <3783FCB7.26967643@nbnet.nb.ca> <eD0MbZxy#GA.356@cpmsnbbsa05> <378A43D2.38CAD94B@IMN.nl> <7mdqgv$4mv@dfw-ixnews16.ix.netcom.com> <oKJi3.5863$iA1.27092@news4.mia> <378d1efb.4469466@netnews>`

```
Randall Bart <Barticus@att.spam.net> wrote in message
  <much snippage>
>
> No, if there's an ON OVERFLOW clause, you can't have [NOT] ON EXCEPTION.
…[3 more quoted lines elided]…
> --

Check out item 4 in the "Archaic Language" list, page 815 of CD 1.5.
  (In case I confused anyone,  "ON OVERFLOW" is being made "archaic" in the
*next* Standard.  It is "fully" supported in the '85 Standard.)

P.S.  I will send a note to J4 telling them that it should get a "note"
added under the General Format - the same way that "NEXT SENTENCE" has one
under the IF statement.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
