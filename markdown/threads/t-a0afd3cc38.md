[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How BIG is a mainframe?

_1 message · 1 participant · 1999-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: How BIG is a mainframe?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dAT%3.8$3L2.998@typhoon01.swbell.net>`
- **References:** `<81126@news2.mia> <gnqh3s81jmoe1fgc236e5aqe506muk1du8@4ax.com> <81ddu6$o3v$1@nntp9.atl.mindspring.net> <e6fm3sk3d315osgfvua3n5t33tte62f4o0@4ax.com> <383BF349.ED910724@NOSPAMhome.com> <81jdb3$er8$1@news.igs.net> <383DEDF6.7522DD8D@att.net> <1t6s3sspfd4bri2gmhbpd78utqpgu06qk5@4ax.com>`

```
G Moore <gvwmoore@spam.ix.netcom.com> wrote in message
news:1t6s3sspfd4bri2gmhbpd78utqpgu06qk5@4ax.com...
>
> there are a couple of things about the mainframe standards. first,
> until raid becomes available for pcs, the standards are all
> theoretical, in regards to 24/7 operation. windows, as an os, does
not
> have the concept of disk mirroring.

RAID and Mirroring (and Disk Duplexing) have been available in
WinNT for quite some time. Software utilities are available to add
RAID and Mirroring to Win95.

> so if the code crashes on a single
> cpu, it's over. since the *data* is usually run from a third party
…[4 more quoted lines elided]…
> maintenance (always the case). then we have the problems of
mainframes
> having *channels* which, the pc's equiviliant, is smartdrive.

Smartdrive was a disk-cache program - not even close in concept
to a 'channel.' Channels are programmable, access memory
directly, operate independently of the CPU, etc. Smartdrive is a
buffer.

>I  believe smartdrive is removed from 95+ (gee, it couldn't be gates
is
> sleeping with the mainframers?).

It was not so much 'removed' as 'replaced' by dynamic disk cacheing
as an automatic (and less error-prone) feature. In Win95 no resources
are dedicated to a disk cache, the resources are shared amongst
running tasks. A disk-intensive application on Win9x could easily have
a much larger cache than Smartdrive in Win3.xx, and conversely a
compute-
intensive application could use the RAM otherwise dedicated to
Smartdrive to improve efficiency.

In other words, Win9x says that RAM is a resource that should be
dynamically shared among active programs; sometimes as a disk
cache, sometimes as an application partition, sometimes as
something else, and these priorities will be adjusted every couple
of milliseconds.

>it also could be the case that
> database vendors wrote their own caching software, and it interferes
> with smartdrive, and they took it out for that reason.

Yep. Database vendors probably decided a) The operating system can
maintain a cache much more efficiently than we, and b) If the OS is
cacheing, having an additional cache in our software means that TWO
giant caches have to be searched for every access.

> using alternate news server source.
> reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
