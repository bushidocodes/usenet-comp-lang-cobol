[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Drive Volume Information

_7 messages · 4 participants · 2002-05_

---

### Drive Volume Information

- **From:** "Rob" <rng519@hotmail.com>
- **Date:** 2002-05-16T16:54:02+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<abvl4f$263d$1@arachne.labyrinth.net.au>`

```
Hi,
Anybody know a way in Cobol to retrieve a computer drive volume information
ie. Volume name, serial number etc.
We have a routine in VB to do this, so another possibility is to find a way
to call a VB program from Cobol and have the parameter pass back to Cobol.

Can anybody offer any suggestion?
Thanks
```

#### ↳ Re: Drive Volume Information

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-16T16:49:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CE3E2F6.685AA775@shaw.ca>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au>`

```


Rob wrote:

> Hi,
> Anybody know a way in Cobol to retrieve a computer drive volume information
…[5 more quoted lines elided]…
> Thanks

You haven't specified which compiler, but with your reference to VB, guess it
has to be a PC. Check out any library routines available - if you compiler has
them. Another alternative there *may* be a an API routine by Young Kim - see
his :-

http://www.kimsoft.com/api-cobol/api-cobol.htm

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Drive Volume Information

- **From:** "Rob" <rng519@hotmail.com>
- **Date:** 2002-05-17T09:11:37+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ac1e90$dqp$1@arachne.labyrinth.net.au>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au> <3CE3E2F6.685AA775@shaw.ca>`

```
Sorry forgot to tell you that I am using Fujitsu Version 5.0 on a Win 2K PC.
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3CE3E2F6.685AA775@shaw.ca...
>
>
…[3 more quoted lines elided]…
> > Anybody know a way in Cobol to retrieve a computer drive volume
information
> > ie. Volume name, serial number etc.
> > We have a routine in VB to do this, so another possibility is to find a
way
> > to call a VB program from Cobol and have the parameter pass back to
Cobol.
> >
> > Can anybody offer any suggestion?
> > Thanks
>
> You haven't specified which compiler, but with your reference to VB, guess
it
> has to be a PC. Check out any library routines available - if you compiler
has
> them. Another alternative there *may* be a an API routine by Young Kim -
see
> his :-
>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Drive Volume Information

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2002-05-17T01:19:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dUYE8.2358$iw7.126821623@newssvr16.news.prodigy.com>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au> <3CE3E2F6.685AA775@shaw.ca> <ac1e90$dqp$1@arachne.labyrinth.net.au>`

```
Rob,

I've never used this particular API, but I have used:

     CALL "GetWindowsDirectoryA" WITH STDCALL USING
                         BY REFERENCE WINDOWS-DIRECTORY
                         BY VALUE 240
                         RETURNING Returnvalue.

so that I know whether I'm running under Windows NT or 95/98/ME, and I
believe Windows 2000 still installs under WINNT (I'm not sure tonight,
however, I can check it out tomorrow at work).  I don't run W2K at home
since XP is the latest flavor of MS.  At work, I have a "triple boot" PC
that runs Win98/Win NT 4.0/Win 2000, but I honestly never paid any attention
to where Windows 2000 installed.

I've also used:

     CALL "GetDriveTypeA" WITH STDCALL USING
                         BY REFERENCE ROOTPATH-NAME
                         RETURNING Returnvalue.

to make sure that Users don't try to map a drive to a CD-ROM or floppy.

Although I'm using Fujitsu 6.1, I think the same API calls will work for
5.0.  You need to link with "kernel32.lib" and within that lib is
"GetVolumeInformationA", which should give you the information that you
need.  Unfortunately, I don't have the additional parameters to add to the
call, but I think others in this group can help you, or possibly a search of
"GetVolumeInformation" at the MS support site will give you the parameters.
You'll need to translate the "C" parameters to COBOL, as was done above, but
hopefully, this will give you a place to start.

Best of Luck,

Denny

"A Unisys Mainframe guy trying to become "semi" Fujitsu PC COBOL literate"

"Rob" <rng519@hotmail.com> wrote in message
news:ac1e90$dqp$1@arachne.labyrinth.net.au...
> Sorry forgot to tell you that I am using Fujitsu Version 5.0 on a Win 2K
PC.
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3CE3E2F6.685AA775@shaw.ca...
…[8 more quoted lines elided]…
> > > We have a routine in VB to do this, so another possibility is to find
a
> way
> > > to call a VB program from Cobol and have the parameter pass back to
…[5 more quoted lines elided]…
> > You haven't specified which compiler, but with your reference to VB,
guess
> it
> > has to be a PC. Check out any library routines available - if you
compiler
> has
> > them. Another alternative there *may* be a an API routine by Young Kim -
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Drive Volume Information

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-17T01:47:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<viZE8.1077$pa.236711@bin4.nnrp.aus1.giganews.com>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au> <3CE3E2F6.685AA775@shaw.ca> <ac1e90$dqp$1@arachne.labyrinth.net.au> <dUYE8.2358$iw7.126821623@newssvr16.news.prodigy.com>`

```

"Denny Brouse" <denden@prodigy.net> wrote in message
news:dUYE8.2358$iw7.126821623@newssvr16.news.prodigy.com...
> Rob,
>
…[11 more quoted lines elided]…
> that runs Win98/Win NT 4.0/Win 2000, but I honestly never paid any
attention
> to where Windows 2000 installed.
>
…[12 more quoted lines elided]…
> call, but I think others in this group can help you, or possibly a search
of
> "GetVolumeInformation" at the MS support site will give you the
parameters.
> You'll need to translate the "C" parameters to COBOL, as was done above,
but
> hopefully, this will give you a place to start.

Try:

http://www.allapi.net/
```

###### ↳ ↳ ↳ Re: Drive Volume Information

_(reply depth: 5)_

- **From:** "Rob" <rng519@hotmail.com>
- **Date:** 2002-05-17T14:07:59+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ac1vl2$ovr$1@arachne.labyrinth.net.au>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au> <3CE3E2F6.685AA775@shaw.ca> <ac1e90$dqp$1@arachne.labyrinth.net.au> <dUYE8.2358$iw7.126821623@newssvr16.news.prodigy.com> <viZE8.1077$pa.236711@bin4.nnrp.aus1.giganews.com>`

```
Thanks for everyone help.
I've solved the problem using
     CALL "GetVolumeInformationA" WITH STDCALL USING
                                  By Value RootPathName
                                  By Value VolumeNameBuffer
                                  By Value VolumeNameSize
                                  By Reference VolumeSerialNumber
                                  By Reference MaximumComponentLength
                                  By Reference FileSystemFlags
                                  By Value FileSystemNameBuffer
                                  By Value FileSystemNameSize.



"JerryMouse" <nospam@invalid.com> wrote in message
news:viZE8.1077$pa.236711@bin4.nnrp.aus1.giganews.com...
>
> "Denny Brouse" <denden@prodigy.net> wrote in message
…[29 more quoted lines elided]…
> > need.  Unfortunately, I don't have the additional parameters to add to
the
> > call, but I think others in this group can help you, or possibly a
search
> of
> > "GetVolumeInformation" at the MS support site will give you the
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Drive Volume Information

_(reply depth: 5)_

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2002-05-17T11:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ep5F8.3305$L07.114618422@newssvr15.news.prodigy.com>`
- **References:** `<abvl4f$263d$1@arachne.labyrinth.net.au> <3CE3E2F6.685AA775@shaw.ca> <ac1e90$dqp$1@arachne.labyrinth.net.au> <dUYE8.2358$iw7.126821623@newssvr16.news.prodigy.com> <viZE8.1077$pa.236711@bin4.nnrp.aus1.giganews.com>`

```
Jerry,

Great Link!  I can see why the author feels the need to shut it down in a
few years.  What a wealth of information.

Thanks,

Denny

"JerryMouse" <nospam@invalid.com> wrote in message
news:viZE8.1077$pa.236711@bin4.nnrp.aus1.giganews.com...
>
> "Denny Brouse" <denden@prodigy.net> wrote in message
…[29 more quoted lines elided]…
> > need.  Unfortunately, I don't have the additional parameters to add to
the
> > call, but I think others in this group can help you, or possibly a
search
> of
> > "GetVolumeInformation" at the MS support site will give you the
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
