[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC -> UNIX

_6 messages · 4 participants · 2001-07_

---

### PC -> UNIX

- **From:** "Bill Gentry" <billgentry2@home.com>
- **Date:** 2001-07-12T14:47:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com>`

```
Hello,

Anyone have experience reading MicroFocus Line Sequential files on UNIX that
were produced on the PC?  I have to produce a variable-length, line
sequential file on Win98 that's going to be processed by a UNIX cobol app.
I don't *think* there's going to be a problem, since both platforms use the
ASCII character set, but you never know.

I intend to contact MicroFocus, but I'd feel better getting some feedback
from anyone having experience with this.

Thanks,
BG
```

#### ↳ Re: PC -> UNIX

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-13T07:27:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4E94B4.87EF3F6C@Azonic.co.nz>`
- **References:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com>`

```
Bill Gentry wrote:
> 
> Anyone have experience reading MicroFocus Line Sequential files on UNIX that
…[3 more quoted lines elided]…
> ASCII character set, but you never know.

I don't have any problem doing this.  In fact I don't have any problem
in transferring indexed or relative files either, just get the names
right.
```

##### ↳ ↳ Re: PC -> UNIX

- **From:** "Bill Gentry" <billgentry2@home.com>
- **Date:** 2001-07-12T21:32:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Io37.408317$K5.42899130@news1.rdc1.nj.home.com>`
- **References:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com> <3B4E94B4.87EF3F6C@Azonic.co.nz>`

```
Great!  Thanks

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3B4E94B4.87EF3F6C@Azonic.co.nz...
> Bill Gentry wrote:
> >
> > Anyone have experience reading MicroFocus Line Sequential files on UNIX
that
> > were produced on the PC?  I have to produce a variable-length, line
> > sequential file on Win98 that's going to be processed by a UNIX cobol
app.
> > I don't *think* there's going to be a problem, since both platforms use
the
> > ASCII character set, but you never know.
>
> I don't have any problem doing this.  In fact I don't have any problem
> in transferring indexed or relative files either, just get the names
> right.
```

###### ↳ ↳ ↳ Re: PC -> UNIX

- **From:** "Jude Robert" <juderobert1@home.com>
- **Date:** 2001-07-14T13:37:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6WX37.30115$EW.239832@news1.rdc1.tx.home.com>`
- **References:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com> <3B4E94B4.87EF3F6C@Azonic.co.nz> <6Io37.408317$K5.42899130@news1.rdc1.nj.home.com>`

```
Be sure to convert the files using the UNIX dos2unix command or if you use
ftp
use the ASCII mode.

"Bill Gentry" <billgentry2@home.com> wrote in message
news:6Io37.408317$K5.42899130@news1.rdc1.nj.home.com...
> Great!  Thanks
>
…[4 more quoted lines elided]…
> > > Anyone have experience reading MicroFocus Line Sequential files on
UNIX
> that
> > > were produced on the PC?  I have to produce a variable-length, line
> > > sequential file on Win98 that's going to be processed by a UNIX cobol
> app.
> > > I don't *think* there's going to be a problem, since both platforms
use
> the
> > > ASCII character set, but you never know.
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: PC -> UNIX

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-15T14:20:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B51989D.D0F1426F@Azonic.co.nz>`
- **References:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com> <3B4E94B4.87EF3F6C@Azonic.co.nz>`

```
Jude Robert (juderobert1@home.com) wrote:
> Be sure to convert the files using the UNIX dos2unix command or if you use
> ftp use the ASCII mode.

I never found the need for this when reading files into Cobol systems.
It may be needed if the file is to be edited, depending on the editor.
```

###### ↳ ↳ ↳ Re: PC -> UNIX

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-14T22:16:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ir22s$ihv$1@slb1.atl.mindspring.net>`
- **References:** `<KLi37.407929$K5.42772897@news1.rdc1.nj.home.com> <3B4E94B4.87EF3F6C@Azonic.co.nz> <3B51989D.D0F1426F@Azonic.co.nz>`

```
I have a *vague* memory about problems/issues with
  CR/LF (carriage-return/line-feed)
     versus
  LF (only)

when "moving" Line Sequential files from DOS environments to Unix
environments.  If you are having problems, I would suggest checking this
out.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
