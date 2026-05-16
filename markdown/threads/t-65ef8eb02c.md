[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress API RS232

_5 messages · 4 participants · 2000-02_

---

### NetExpress API RS232

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 2000-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KUbo4.3860$a27.122870@news1.rdc1.mb.home.com>`

```
I am porting a bunch of programs from CTOS environment where there are
system calls for I-O to RS-232 ports.  The programs set comm parameters,
raise lower and check RS232 leads, rely on OS to do buffering on both input
and output.

It seems that the Win32 API can be used with NetExpress.  I have downloaded
the sample program from Merant's support site.  It compiles, and executes
when I use CBLLINK, but does not seen to work.  I have tried the IDE but it
gives error saying called program not found.

1.  How do I use Win32 calls from within IDE?

2.  Can someone provide a working example of the serial I-O using API.

3.  Are there better alternatives? (yes I need to be in 32bit environment)
```

#### ↳ Re: NetExpress API RS232

- **From:** jgill_1@my-deja.com
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87vu02$cgg$1@nnrp1.deja.com>`
- **References:** `<KUbo4.3860$a27.122870@news1.rdc1.mb.home.com>`

```
I had a situation where I had to read the output of an electronic scale
using the RS-232 port. This was strictly an input operation using MF
Cobol 16bit. I finally had to write an assembler program is Microsoft
Assembler and then call it from Cobol. The Assembler program polled the
RS-232 port and read the output from the scale and passed it back to the
Cobol program.
John Gill    (jdgill@juno.com)












In article <KUbo4.3860$a27.122870@news1.rdc1.mb.home.com>,
  "Charles Goodman" <cgoodman@mbnet.mb.ca> wrote:
> I am porting a bunch of programs from CTOS environment where there are
> system calls for I-O to RS-232 ports.  The programs set comm
parameters,
> raise lower and check RS232 leads, rely on OS to do buffering on both
input
> and output.
>
> It seems that the Win32 API can be used with NetExpress.  I have
downloaded
> the sample program from Merant's support site.  It compiles, and
executes
> when I use CBLLINK, but does not seen to work.  I have tried the IDE
but it
> gives error saying called program not found.
>
…[4 more quoted lines elided]…
> 3.  Are there better alternatives? (yes I need to be in 32bit
environment)
>
> --
…[12 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: NetExpress API RS232

- **From:** Bob7536@aol.com
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<881cob$du7$1@nnrp1.deja.com>`
- **References:** `<KUbo4.3860$a27.122870@news1.rdc1.mb.home.com>`

```
Hi John and Charles,

I am using Win32 API call to communicate with a number of different
serial devices.  For example scale, pin pad, pole display etc.  If you
would like the Win32 API calls that I use to accomplish this please
send me an e-mail.  I am using NetExpress 3.0 and Flexus Sp2.

Thanks,
Bob Hennessey



Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: NetExpress API RS232

- **From:** tom@taltech.com (Thomas Lutz)
- **Date:** 2000-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38afb904.79012753@news.earthlink.net>`
- **References:** `<KUbo4.3860$a27.122870@news1.rdc1.mb.home.com> <881cob$du7$1@nnrp1.deja.com>`

```
For a number of great tools for serial communications and data
acquisition, visit www.taltech.com
Be sure to look in the Free Software section of the site as well as
look at the Software Wedge product line.

On Fri, 11 Feb 2000 16:18:24 GMT, Bob7536@aol.com wrote:

>Hi John and Charles,
>
…[11 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: NetExpress API RS232

- **From:** tom@taltech.com (Thomas Lutz)
- **Date:** 2000-02-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38bd4570.32646774@news.earthlink.net>`
- **References:** `<KUbo4.3860$a27.122870@news1.rdc1.mb.home.com>`

```
 You may want to look at a tool called the Software Wedge at
www.taltech.com
The rpogram is designed to add serial communications capabilities to
other Windows programs with little or no programming at all.




On Wed, 09 Feb 2000 11:08:26 GMT, "Charles Goodman"
<cgoodman@mbnet.mb.ca> wrote:

>I am porting a bunch of programs from CTOS environment where there are
>system calls for I-O to RS-232 ports.  The programs set comm parameters,
…[12 more quoted lines elided]…
>3.  Are there better alternatives? (yes I need to be in 32bit environment)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
