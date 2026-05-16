[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I FTP load modules from MVS-->PC-->MVS

_1 message · 1 participant · 2000-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How do I FTP load modules from MVS-->PC-->MVS

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O0XeAp9h$GA.259@cpmsnbbsa04>`
- **References:** `<38C21C29.73AC6914@viewtech.com.au> <u8$9#9ph$GA.215@cpmsnbbsa02> <38C393C5.3FD9C45C@viewtech.com.au> <uSfoXu2h$GA.276@cpmsnbbsa03> <3wXw4.303$GL.814@news4.mia>`

```
To be honest, I would not be transferring load or object modules.
I would transfer the source and recompile.
I wouldn't want to become know as the person who does this.
1) Dennis knows how to do it, ask him.
2) Worse yet, because I can do it, I have this assigned as one of my job
duties.

I once worked at a software vendor.
Release tapes were sent out with load modules, but when asked, we would
recommend that the client compile & link the programs themselves.
There were too many problems when people would place the load modules in
libraries with the wrong block size.

James King <mangogwr@bellsouth.net> wrote in message
news:3wXw4.303$GL.814@news4.mia...
> I have researched this and the answer I found is:
> You can NOT do this.  The 'load Lib' is a special format:
…[17 more quoted lines elided]…
> > If it can be done, it will eliminate possible PC Upload/download
problems.
> >
> > There may also be a problem if the load libraries have different block
> > sizes.
> >
> > There are others who have apparently done this, see other messages in
this
> > thread.
> >
…[4 more quoted lines elided]…
> > > way that I know of is to FTP the load modules to a PC, then upload to
a
> > web
> > > site where they can be downloaded anywhere anytime.
…[14 more quoted lines elided]…
> > > > > The load modules on the MVS reside in a PDS and I FTP them to the
PC
> > > > > using the binary option with a record format of 'U'  (undefined).
I
> > use
> > > > > the same options when transferring back from the PC to the MVS.
The
> > > > > transfers work OK but the load module is unusable on the MVS.
> > > > >
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
