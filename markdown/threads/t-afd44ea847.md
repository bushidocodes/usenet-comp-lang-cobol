[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Windows 95 VS NT 4.0 API Call Results

_4 messages · 3 participants · 1998-10_

---

### Windows 95 VS NT 4.0 API Call Results

- **From:** dblaze@merchants-fla.com
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36394c8b.446130341@news.mci2000.com>`

```
I have an application written in MF 4.0.032 Cobol that uses API calls
to access a COMM port to communicate with a modem.  I developed it on
NT 4.0 and tried to move it to a Windows 95 machine.  It works fine on
NT but on two of the API calls, I get back a difference result.  The
two calls in question are :  GetCommState and SetCommState.  In NT I
get back +1 while in 95 I get back +0.  Is this correct?  Does 95
return +0 as TRUE where NT returns +1 when making the API calls?

Thanks in advance
Doug
```

#### ↳ Re: Windows 95 VS NT 4.0 API Call Results

- **From:** smb@mfltdz.co.ukz (Steve Biggs)
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<717nod$91l@hyperion.mfltd.co.uk>`
- **References:** `<36394c8b.446130341@news.mci2000.com>`

```
dblaze@merchants-fla.com wrote:
>I have an application written in MF 4.0.032 Cobol that uses API calls
>to access a COMM port to communicate with a modem.  I developed it on
…[4 more quoted lines elided]…
>return +0 as TRUE where NT returns +1 when making the API calls?

Hi Doug,
According to the documentation for these APIs, a return value of 0 
indicates that the function failed, and you should call GetLastError to 
get extended error information. The docs don't indicate any difference 
between Windows 95 and NT.

Steve.
Micro Focus Development.
```

##### ↳ ↳ Re: Windows 95 VS NT 4.0 API Call Results

- **From:** dblaze@merchants-fla.com
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364389b9.73326728@news.mci2000.com>`
- **References:** `<36394c8b.446130341@news.mci2000.com> <717nod$91l@hyperion.mfltd.co.uk>`

```
Thanks for the information Steve.  It turned out to be my problem and
I feel really stupid because of it!  I didn't have a modem on the port
at the time I was testing.  I figured since the port was actively
defined on the system and was valid, up until I tried to send out an
AT command it should return good status values - stupid me!  I hooked
up a modem during further test and getting my InstallShield script to
run and it reported back with the +1 like NT did.

Doug



>Hi Doug,
>According to the documentation for these APIs, a return value of 0 
…[5 more quoted lines elided]…
>Micro Focus Development.
```

#### ↳ Re: Windows 95 VS NT 4.0 API Call Results

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298301.65435.5002@kcbbs.gen.nz>`
- **References:** `<36394c8b.446130341@news.mci2000.com>`

```
In message <<36394c8b.446130341@news.mci2000.com>> dblaze@merchants-fla.com writes:
> to access a COMM port to communicate with a modem.  I developed it on
> NT 4.0 and tried to move it to a Windows 95 machine.  It works fine on
…[3 more quoted lines elided]…
> return +0 as TRUE where NT returns +1 when making the API calls?

Sorry, did you think that there was 'one Windows' ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
