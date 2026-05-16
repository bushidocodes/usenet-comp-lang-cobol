[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rmcobol and dos commands

_12 messages · 6 participants · 2001-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### rmcobol and dos commands

- **From:** "John Magill" <jmagill@icon.co.za>
- **Date:** 2001-06-18T17:18:58+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2e1957$0$231@hades.is.co.za>`

```
Hi
Been a while since i programmed using rmcobol. Cannot figure out if i can
interface to the dos command shell to use certain operating system features.
I am using a fairly old version 2.01 of rnmcobol-85. I have managed to call
a few .exe files using the CALL but most of these give an error requesting
they be run in win32bit mode.
Any input would be appreciated.
thanks
John
```

#### ↳ Re: rmcobol and dos commands

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2001-06-19T00:27:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010618202744.03410.00000699@nso-cb.aol.com>`
- **References:** `<3b2e1957$0$231@hades.is.co.za>`

```
Hi John,

You can use the Win32API commands (CreateProcess) to execute DOS commands.  I
use NetExpress and have not used RM-COBOL, but if you would like some samples
please e-mail me.

Bob Hennessey
```

##### ↳ ↳ Re: rmcobol and dos commands

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-06-19T09:37:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com>`

```
On 19 Jun 2001 00:27:44 GMT, bob7536@aol.com (Bob7536) wrote:

>Hi John,
>
…[4 more quoted lines elided]…
>Bob Hennessey
It would hardly work as v 2.01 is a DOS 16 bits version.

There is one program that will allow you do execute a call to other
programs.

This is "system" (which is supplyed as a separate executable
"system.exe" and you may be able to find it in you supplied media (not
sure though). If not then see if someone else can supply you with
this.

Cheers

Frederico Fonseca
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

- **From:** "John Magill" <jmagill@icon.co.za>
- **Date:** 2001-06-19T11:35:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2f1a6e$0$231@hades.is.co.za>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com> <7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com>`

```
Do not have this executable. Nor is it on the origonal disks which i still
have. I have written the equivalent in c but it cannot be called from the
cobol call statement i think becuase i have compiled the c using a 32bit
compiler.

"Frederico Fonseca" <frederico_fonseca@eudoramail.com> wrote in message
news:7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com...
> On 19 Jun 2001 00:27:44 GMT, bob7536@aol.com (Bob7536) wrote:
>
> >Hi John,
> >
> >You can use the Win32API commands (CreateProcess) to execute DOS
commands.  I
> >use NetExpress and have not used RM-COBOL, but if you would like some
samples
> >please e-mail me.
> >
…[13 more quoted lines elided]…
> Frederico Fonseca
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

- **From:** "Rob Heady" <R.Heady@Liant.com>
- **Date:** 2001-06-19T15:23:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DOX6.114$Xh7.5194@nnrp1.sbc.net>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com> <7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com>`

```
John,

The SYSTEM.EXE was not included in RM/COBOL v2.01.  I believe it was first
released with v5.30.00. For grins I tried calling the 5.30 system.exe from a
2.01 runtime and it crashed my DOS box.

You may have to write a assembly language program to do this or upgrade to
v7.00.03 for 32-bit windows.

-Robert Heady

Frederico Fonseca wrote in message
<7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com>...
>On 19 Jun 2001 00:27:44 GMT, bob7536@aol.com (Bob7536) wrote:
>
>>Hi John,
>>
>>You can use the Win32API commands (CreateProcess) to execute DOS commands.
I
>>use NetExpress and have not used RM-COBOL, but if you would like some
samples
>>please e-mail me.
>>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

_(reply depth: 4)_

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-06-19T22:45:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uehvitgr15o3ke1m6k8p1q6jok91cql7tp@4ax.com>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com> <7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com> <3DOX6.114$Xh7.5194@nnrp1.sbc.net>`

```
Hi,

the "system" executable was before 5.3.

And there was a version that would work with 2.01 whether supplied by
Liant (at the time RyanMcFarland) or not.
Unfortunatelly I no longer have this one.


Cheers

FF

On Tue, 19 Jun 2001 15:23:09 -0500, "Rob Heady" <R.Heady@Liant.com>
wrote:

>John,
>
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

_(reply depth: 5)_

- **From:** "Rob Heady" <R.Heady@Liant.com>
- **Date:** 2001-06-20T09:34:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LH2Y6.1396$Xh7.20692@nnrp1.sbc.net>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com> <7j3uitk217o3ciluvbr22nfk6nef7bn7p2@4ax.com> <3DOX6.114$Xh7.5194@nnrp1.sbc.net> <uehvitgr15o3ke1m6k8p1q6jok91cql7tp@4ax.com>`

```
You are correct sir.  It was version 5.20.00 for DOS.  I didn't dig deep
enough.
It would not work with 2.01 either.  I could not find an earlier version.

-Rob

Frederico Fonseca wrote in message ...
>Hi,
>
…[17 more quoted lines elided]…
>>released with v5.30.00. For grins I tried calling the 5.30 system.exe from
a
>>2.01 runtime and it crashed my DOS box.
>>
…[11 more quoted lines elided]…
>>>>You can use the Win32API commands (CreateProcess) to execute DOS
commands.
>>I
>>>>use NetExpress and have not used RM-COBOL, but if you would like some
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: rmcobol and dos commands

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-19T12:19:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2f42e0.25511688@news1.attglobal.net>`
- **References:** `<3b2e1957$0$231@hades.is.co.za> <20010618202744.03410.00000699@nso-cb.aol.com>`

```
One interesting note on this.  I have a client going for Windows
Certification with his software.  In order to get "Platinum"
certification you can't use CreateProcess in your application.  The
"Preferred" way according to MS is to use the ShellExecute API.  The
only problem I have with that is that there seems to be no way to
"wait" for a process to complete before returning to the spawning
process.  With CreateProcess I can use a "monitoring" call to wait for
the process to complete before continuing.


On 19 Jun 2001 00:27:44 GMT, bob7536@aol.com (Bob7536) wrote:

>Hi John,
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2001-06-21T01:03:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010620210318.03823.00000003@nso-cq.aol.com>`
- **References:** `<3b2f42e0.25511688@news1.attglobal.net>`

```
Hi Thane,

I use the Win32API "WaitForSingleObject" to wait until the batch file or
whatever program I have executed to complete.  Is this the monitoring call that
you are talking about ?

Thanks,
Bob
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-21T12:11:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvlY6.315$qz2.38452@paloalto-snr1.gtei.net>`
- **References:** `<3b2f42e0.25511688@news1.attglobal.net> <20010620210318.03823.00000003@nso-cq.aol.com>`

```

It looks like ShellExecuteEx returns a process handle in the
ShellExecuteInfo Structure. I haven't tried this, but perhaps this handle
can be used with WaitForSingleObject to do "wait for completion without
using CreateProcess".

Maybe I'll test that later today. I really don't feel like working, anyway.
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-22T13:37:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106221237.1fec4b2b@posting.google.com>`
- **References:** `<3b2f42e0.25511688@news1.attglobal.net> <20010620210318.03823.00000003@nso-cq.aol.com> <vvlY6.315$qz2.38452@paloalto-snr1.gtei.net>`

```
The process handle returned is not the right sort of animal for
waitforsingleprocess, so it won't work.  Cheesle sent me an idea to
use this API then wait for "something" idle.  I don't have the message
here with me right now to give you the exact details.


"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<vvlY6.315$qz2.38452@paloalto-snr1.gtei.net>...
> It looks like ShellExecuteEx returns a process handle in the
> ShellExecuteInfo Structure. I haven't tried this, but perhaps this handle
…[17 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: rmcobol and dos commands

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-22T13:33:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106221233.34db09d6@posting.google.com>`
- **References:** `<3b2f42e0.25511688@news1.attglobal.net> <20010620210318.03823.00000003@nso-cq.aol.com>`

```
Yes - but that can be used with CreateProcess but not ShellExecute or
ShellExecuteEx which are what is "not allowed" by the Platinum
certification.

bob7536@aol.com (Bob7536) wrote in message news:<20010620210318.03823.00000003@nso-cq.aol.com>...
> Hi Thane,
> 
…[5 more quoted lines elided]…
> Bob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
