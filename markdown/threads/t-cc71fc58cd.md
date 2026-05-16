[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fixed -Really wierd problem!!!

_1 message · 1 participant · 1999-09_

---

### Re: Fixed -Really wierd problem!!!

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s1f0g$5e5$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<nm6C3.14899$ei1.29469@newsfeeds.bigpond.com> <7rav46$lgn$4@news.igs.net> <Yk8C3.125$D84.6202@dfiatx1-snr1.gtei.net> <37da9191.355700@news.indigo.ie> <YxqC3.15437$ei1.31103@newsfeeds.bigpond.com> <4KMC3.16029$ei1.31353@newsfeeds.bigpond.com> <bRjD3.9247$mo.362609@viper> <ZhmD3.17051$ei1.34393@newsfeeds.bigpond.com> <iAFD3.9928$mo.389559@viper> <7rq246$1em$10@ssauraab-i-1.production.compuserve.com> <7rra24$poo@dfw-ixnews12.ix.netcom.com> <7rsss5$kj0$3@ssauraac-i-1.production.compuserve.com> <7ru798$4cn@dfw-ixnews17.ix.netcom.com>`

```
    Bottom line - you have to pay attention.  I remember writing reports in
FORTRAN.  At that time we had to put the carriage control stuff in ourself.
And if we printed source code on the "other" Mainframes (Not IBM
compatable), we had to run a utility that shifted everyting over 1 char,
leaving a blank in col 01.  (They were control data machines).





William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:7ru798$4cn@dfw-ixnews17.ix.netcom.com...
> I can't speak for all mainframes, but on an IBM mainframe,
>
…[7 more quoted lines elided]…
> If you use a Standard "WRITE" statement (with BEFORE/AFTER advancing),
then
> you will (probably) get a DCB=F type file.  If you use WRITE AFTER
> ADVANCING, then you will (usually) get FA or FBA type files (although - as
…[4 more quoted lines elided]…
> file that you use for source code.  WRITE AFTER ADVANCING *may* get the
same
> type of file.  Using WRITE BEFORE ADVANCING will NEVER get you the same
type
> of file as your source code.
>
…[7 more quoted lines elided]…
> > cobol compiler expects on that system.  This varys from place to place.
I
> > believe that my compiler manual defined line sequential in this manner
> > (since the cobol manual is used on all platforms, not just pc's).
> >
> >     I do wonder does a mainframe compiler even accept that terminology
at
> > all?   And what would it do?   I have never thought about that before.
My
> > main point was the fact that if you use write before 1, avoiding write
> > before 2 and so forth, than the file will be easy to view on line with
…[21 more quoted lines elided]…
> > > >     I realize that this is something of a religous topic, but I
would
> > like
> > > > to point out
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
