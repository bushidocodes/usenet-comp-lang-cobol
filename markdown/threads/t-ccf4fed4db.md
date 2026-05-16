[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compile static binaries +opencobol

_5 messages · 3 participants · 2005-09_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### compile static binaries +opencobol

- **From:** Cydrome Leader <presence@MUNGEpanix.com>
- **Date:** 2005-09-26T13:11:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dh8s1f$hhb$1@reader1.panix.com>`

```
How does one compile static binaries with opencobol under FreeBSD? I don't 
see any options to do this in the literature, and the resulting binaries 
obviously will not function on other systems where the cobol libraries are 
not installed. Error below is from trying to excute the result of "cobc 
count.cbl" on a different system.

[host]user:~/cobol$ ./count
/usr/libexec/ld-elf.so.1: Shared object "libcob.so.1" not found, required 
by "count"
```

#### ↳ Re: compile static binaries +opencobol

- **From:** clvrmnky <clvrmnky-uunet@coldmail.com.invalid>
- **Date:** 2005-09-26T15:18:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YPXZe.13038$p5.1117@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<dh8s1f$hhb$1@reader1.panix.com>`
- **References:** `<dh8s1f$hhb$1@reader1.panix.com>`

```
On 26/09/2005 9:11 AM, Cydrome Leader wrote:
> How does one compile static binaries with opencobol under FreeBSD? I don't 
> see any options to do this in the literature, and the resulting binaries 
…[7 more quoted lines elided]…
> 
That would be the run-time environment, I guess.  The docs are thin, but
did you try:
<http://www.opencobol.org/modules/bwiki/index.php?cmd=read&page=UserManual%2F2_2#content_1_1>

The variable COB_LDFLAGS should accept the right options to make static
libs, that you can then make into a library, or link to your app to make
a FreeBSD ELF executable.

If not, then perhaps the run-time environment does not support static
linking.  I'd expect this to be in the OpenCOBOL docs somewhere.
```

#### ↳ Re: compile static binaries +opencobol

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-26T12:24:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127762683.799686.272810@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<dh8s1f$hhb$1@reader1.panix.com>`
- **References:** `<dh8s1f$hhb$1@reader1.panix.com>`

```
> How does one compile static binaries with opencobol
> under FreeBSD? I don't see any options to do this in
> the literature,

I don't know that you can create a static binary at all. You can use
-fstatic-call to incorporate your own called programs statically, but
not the underlying runtime.

> and the resulting binaries obviously will not function on
> other systems where the cobol libraries are not
> installed.

What is the problem with installing the runtime libraries on the target
machine ?  Just install OpenCobol and then install your programs.
```

##### ↳ ↳ Re: compile static binaries +opencobol

- **From:** Cydrome Leader <presence@MUNGEpanix.com>
- **Date:** 2005-09-26T23:51:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dha1i4$9nj$1@reader1.panix.com>`
- **References:** `<dh8s1f$hhb$1@reader1.panix.com> <1127762683.799686.272810@f14g2000cwb.googlegroups.com>`

```
Richard <riplin@azonic.co.nz> wrote:
>> How does one compile static binaries with opencobol
>> under FreeBSD? I don't see any options to do this in
…[11 more quoted lines elided]…
> machine ?  Just install OpenCobol and then install your programs.

disk space is cheaper than the time it takes to install/remove/track/audit 
programming environments on various machines.
```

###### ↳ ↳ ↳ Re: compile static binaries +opencobol

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-26T17:06:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1127779607.437033.300650@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<dha1i4$9nj$1@reader1.panix.com>`
- **References:** `<dh8s1f$hhb$1@reader1.panix.com> <1127762683.799686.272810@f14g2000cwb.googlegroups.com> <dha1i4$9nj$1@reader1.panix.com>`

```
> disk space is cheaper than the time it takes to install/remove/track/audit
> programming environments on various machines.

Then build an RPM or PKG or whatever is used by the systems that you
want to target and have this install the libcobc and everything else
that is required as it installs your program.

OpenCobol may also require libdb, libltdl, libgpm, ncurses and much
else, and these will rely on libc and others and may require a specific
version.  You may include checks in the RPM or PKG for all the required
libraries. You may even include RPM or PKG for these on your
distribution media.

Alternately you could purchase a Cobol implementation that takes care
of all these fiddling details for you, or at least has existing
solutions, but that will cost money.

If you write in Perl you need to ensure that there is a Perl system
installed, same with Python, Java, even C#, and these may need to be of
a specific version and/or have additional modules or packages
installed. OpenCobol is no different.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
