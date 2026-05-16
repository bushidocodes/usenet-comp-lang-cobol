[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM COBOL, Netware, and file corruption

_1 message · 1 participant · 2001-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: RM COBOL, Netware, and file corruption

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-09T14:11:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8Y9q6.5185$Mz2.54137@weber.videotron.net>`
- **References:** `<3aa8f708.6295060@news.kih.net> <a78q6.8844$EM2.53015@wagner.videotron.net> <ffskatgf7fc9kmmp9iu3jdgm5k75uhi0s2@4ax.com>`

```
First, thank's for your answer Frederico.

I already know those options but we have a conflict with the technician guy
supporting there system, and they decide that it was the runtime who was to
old, so we have to setup the windows runtime even if I know we will still
have those errors, because the last documentation  I have concerning error
98/02 come from the windows runtime.  Anyway it's my problem...


Concerning this:
> >We are trying the new Runtime 7, but we have to change our printing
> >technique since capture command always open a DOSWindows.
…[4 more quoted lines elided]…
>

I tried this and there was no change.  When my program isued a call system
to a capture command or if I do a call system to a batch file, a dos windows
still opening and it do not close (I need to do alt-f4 on the X button to
close or for a batch file go to each station and select the batch file and
check the close on exit option in property -not really a good solution).

On wich program do I need to set this property, the one who's calling the
command (call system):
Our app begin with a first program (a login and first menu), then it call a
second one (a second menu wich is calling other program).  In the second
program I isued some call system and sometime in other program.

I changed "SYSTEM window type" to "HIDDEN" in the options panel in property
of the program at the top left, when running the program.  This should
change the registry, as the book, for my pc only.  If it this the right way,
we should also be able to change it programmaticaly, like the option Title,
or the enable close, if yes how?  Because I tried to call this option before
the call system and there was no difference.





"Frederico Fonseca" <frederico_fonseca@eudoramail.com> a �crit dans le
message news: ffskatgf7fc9kmmp9iu3jdgm5k75uhi0s2@4ax.com...
> Hi both.
>
>
> >We do support for 25 company for our software and only one company keeps
> >having file corruption and it's a Novell system (Netware 4.11).  We get
file
> >corruption every weeks, and sometime 2 time a days.  We are going crazy.
> >We are working on .
…[23 more quoted lines elided]…
> >recovery on this file.bak and we copy back this file over the old one
(ex:
> >file.001).  After this process it works find.
> This is normally due to the fact that the file is still being locked
…[33 more quoted lines elided]…
> Frederico Fonseca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
