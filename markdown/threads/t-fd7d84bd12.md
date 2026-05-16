[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CBL_CHECK_FILE_EXIST

_6 messages · 3 participants · 2002-07_

---

### CBL_CHECK_FILE_EXIST

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-07-03T05:39:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0207030439.74af3ed8@posting.google.com>`

```
I have a problem with the routine CBL_CHECK_FILE_EXIST.
my environment:
machine: IBM RS/6000 (AIX)
compiler: microfocus object cobol v4.1.06.
If I use this routine with a file on a directory, which is mounted
with NFS, and the machine with this directory is down, my program
hangs.
I think I have to test, if the machine is down or not, but how?
```

#### ↳ Re: CBL_CHECK_FILE_EXIST

- **From:** ctimmer@gci.net (Curt Timmerman)
- **Date:** 2002-07-03T16:36:56
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns924057A43318Cctimmermanacsalaskac@10.136.100.32>`
- **References:** `<bcfdd616.0207030439.74af3ed8@posting.google.com>`

```
g.friedrich@fiuka.de (Friedrich) wrote in 
<bcfdd616.0207030439.74af3ed8@posting.google.com>:

>I have a problem with the routine CBL_CHECK_FILE_EXIST.
>my environment:
…[5 more quoted lines elided]…
>I think I have to test, if the machine is down or not, but how?

Did you give it enough time? When the remote host is down, an NFS request 
will have to time out before an error is returned. It could take a couple 
of minutes.
```

#### ↳ Re: CBL_CHECK_FILE_EXIST

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2002-07-03T18:43:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com>`
- **References:** `<bcfdd616.0207030439.74af3ed8@posting.google.com>`

```
ghItlh g.friedrich@fiuka.de (Friedrich) 

>I have a problem with the routine CBL_CHECK_FILE_EXIST.
>my environment:
…[5 more quoted lines elided]…
>I think I have to test, if the machine is down or not, but how?

This will happen with hard NFS mounts.

Make sure you understand the differences, but if you want your program
just to bomb if the NFS server goes away, use soft mount.
```

##### ↳ ↳ Re: CBL_CHECK_FILE_EXIST

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-07-03T23:17:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0207032217.38e2c765@posting.google.com>`
- **References:** `<bcfdd616.0207030439.74af3ed8@posting.google.com> <qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com>`

```
qIroS <qIroS@tlhIngan.co.uk> wrote in message news:<qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com>...
> This will happen with hard NFS mounts.
> 
> Make sure you understand the differences, but if you want your program
> just to bomb if the NFS server goes away, use soft mount.

perfect!! "soft mount" is the solution. Thank you very much
```

###### ↳ ↳ ↳ Re: CBL_CHECK_FILE_EXIST

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-07-04T22:58:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0207042158.26b8a50a@posting.google.com>`
- **References:** `<bcfdd616.0207030439.74af3ed8@posting.google.com> <qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com> <bcfdd616.0207032217.38e2c765@posting.google.com>`

```
g.friedrich@fiuka.de (Friedrich) wrote in message news:<bcfdd616.0207032217.38e2c765@posting.google.com>...
> qIroS <qIroS@tlhIngan.co.uk> wrote in message news:<qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com>...
> > This will happen with hard NFS mounts.
…[4 more quoted lines elided]…
> perfect!! "soft mount" is the solution. Thank you very much

Sorry, "soft mount" was not the solution!!
My first test was:
unmount the directory; so CBL_CHECK_FILE_EXIST says: "file not exist" at once
and I thought: that is the solution.

My second test was:
the directory ist mounted but the machine with the directory was down,
then CBL_CHECK_FILE_EXIST hangs
```

###### ↳ ↳ ↳ Re: CBL_CHECK_FILE_EXIST

- **From:** g.friedrich@fiuka.de (Friedrich)
- **Date:** 2002-07-09T05:45:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfdd616.0207090445.4f357c4@posting.google.com>`
- **References:** `<bcfdd616.0207030439.74af3ed8@posting.google.com> <qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com> <bcfdd616.0207032217.38e2c765@posting.google.com>`

```
soft mount was not the solution.
if the directory ist mounted but the machine with the directory was down,
then CBL_CHECK_FILE_EXIST hangs.
Is there any parameter for CBL_CHECK_FILE_EXIST?.
Or is there any commando to check the connection without any hang?


g.friedrich@fiuka.de (Friedrich) wrote in message news:<bcfdd616.0207032217.38e2c765@posting.google.com>...
> qIroS <qIroS@tlhIngan.co.uk> wrote in message news:<qfd6iucaug2vns36a0u8lcat36qlchdd6q@4ax.com>...
> > This will happen with hard NFS mounts.
…[4 more quoted lines elided]…
> perfect!! "soft mount" is the solution. Thank you very much
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
