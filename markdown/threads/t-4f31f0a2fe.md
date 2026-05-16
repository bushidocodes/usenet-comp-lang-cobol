[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating a tar file from COBOL

_8 messages · 4 participants · 2005-08_

---

### Creating a tar file from COBOL

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-08-16T12:57:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`

```
Hi all.

COBOL:  MF Server Express 4.0 SP2
OS: HP-UX 11i

Challenge: Create a tar package from within a cobol application.

Inside the COBOL application, I am cycling through a (sometimes rather
LARGE) random list of file names. Each file needs to be added to a tar
package that will be transmitted to a remote machine.

I've come up with two methods for this:

1) Build the names of the files into a single command line, then shell
out one time to the tar command so that it can create the archive (tar
cf mytar file1 fil2 ...).

2) Shell out for each individual file name using the tar command to add
it to the existing archive (tar [cr]f mytar file).

Option 1 is somewhat difficult because my command line could easily
grow to more than the command line limit set by HP-UX (currently 256
bytes I believe).

Option 2 is clumsy because I will use a lot of overhead with the
repeated system calls.

I'm looking for a better/cleaner/faster way to do this, if anyone knows
of one? >>fingers crossed<<

Perhaps there is a native compression utility within COBOL that I am
unaware of?

Any and all suggestions are welcome. Thanks in advance.

Chris
```

#### ↳ Re: Creating a tar file from COBOL

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-08-16T13:17:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124223462.030570.284620@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`

```
I've discovered a 3rd option (using pax).

I could build an output file containing the names of the files to be
archived, then 'cat' its outputs to the pax command at the end of the
routine (cat filelist | pax -c -f bundle.pax).

This would seem to solve my command line length problem, but still it
is rather clumsy.

Still looking for a better mousetrap.

Thanks.
```

#### ↳ Re: Creating a tar file from COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-16T14:26:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124227611.591431.174550@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`

```
> Any and all suggestions are welcome.

>From man tar on Linux:

    -T, -I, --files-from=F
              get names to extract or create from file F

Write the list of files to file F and use this option, if available.
```

##### ↳ ↳ Re: Creating a tar file from COBOL

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-08-17T06:02:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124283751.625007.132370@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1124227611.591431.174550@o13g2000cwo.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com> <1124227611.591431.174550@o13g2000cwo.googlegroups.com>`

```
Thanks Richard  - Linux is a wonderful thing.

Unfortunately these optoins are not available on the version of tar
that ships with HP-UX 11i.

The use of pax gives me this same flexibility, but I am not sure if pax
is POSIX so that it will be supported across many different flavors of
UNIX.
```

###### ↳ ↳ ↳ Re: Creating a tar file from COBOL

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-08-17T20:36:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<de073h02h0c@news3.newsguy.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com> <1124227611.591431.174550@o13g2000cwo.googlegroups.com> <1124283751.625007.132370@f14g2000cwb.googlegroups.com>`

```

In article <1124283751.625007.132370@f14g2000cwb.googlegroups.com>, "Chris" <ctaliercio@yahoo.com> writes:
> 
> The use of pax gives me this same flexibility, but I am not sure if pax
> is POSIX so that it will be supported across many different flavors of
> UNIX.

It is; more precisely, it's part of the Single UNIX Specification
version 3, which is simultaneously The Open Group Base Specifications
Issue 6, POSIX (IEEE 1003.1-2004 and 1003.2-2004), and ISO/IEC 9945-1
and 9945-2.  (These are the so-called "Austin Group" participants.)

See:
   http://www.opengroup.org/onlinepubs/009695399/utilities/pax.html
   http://www.opengroup.org/onlinepubs/009695399/idx/misc.html

SUSv3 is relatively recent (2004), but I believe pax has been in
POSIX since at least 2001.

Another alternative would be to generate the tar file within your
process.  The tar file format is documented; there are probably open
source libraries to create tar files programmatically.  By the same
token, if you did want compression you could use a library such as
Gailly and Adler's zlib to create an archive with compression.[1]
While these libraries are typically written in C, they generally
build on all modern Unix platforms without requiring any code changes
- just download and follow the instructions.


1. Actually, zlib (http://www.zlib.net) doesn't create zip archives
by itself, but it comes with a sample C program that does.  There's
probably another open source library that will create zip archives
without doing any additional work.
```

###### ↳ ↳ ↳ Re: Creating a tar file from COBOL

- **From:** clvrmnky <clvrmnky-uunet@coldmail.com.invalid>
- **Date:** 2005-08-17T16:42:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JiNMe.7749$p5.3919@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<1124283751.625007.132370@f14g2000cwb.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com> <1124227611.591431.174550@o13g2000cwo.googlegroups.com> <1124283751.625007.132370@f14g2000cwb.googlegroups.com>`

```
On 17/08/2005 9:02 AM, Chris wrote:
> Thanks Richard  - Linux is a wonderful thing.
> 
…[6 more quoted lines elided]…
> 
pax _is_ POSIX.2.  See the x/OPEN Portability Guide 4.0.

tar is not strictly POSIX, but is often recommended on POSIX systems for
portability reasons and based on it's BSD Unix legacy.  But it is not
part of any POSIX standard I know about.
```

#### ↳ Re: Creating a tar file from COBOL

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-16T14:35:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124228133.584820.152580@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com>`

```
> (tar cf mytar file1 fil2 ...).

> Perhaps there is a native compression utility

Note that tar is not a 'compression' utility unless you specify the Z
or z option or similar (if supprted).
```

##### ↳ ↳ Re: Creating a tar file from COBOL

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-08-17T06:04:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1124283849.415282.32170@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1124228133.584820.152580@g49g2000cwa.googlegroups.com>`
- **References:** `<1124222267.915431.173050@g47g2000cwa.googlegroups.com> <1124228133.584820.152580@g49g2000cwa.googlegroups.com>`

```
Yes - I should have been more clear on that. The intention is not
really to compress the files (though that would also be nice), its more
to consolidate them into a single file for relay to multiple servers.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
