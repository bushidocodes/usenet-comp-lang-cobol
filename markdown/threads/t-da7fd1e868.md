[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SCO resources for AcuCobol-85?

_6 messages · 2 participants · 2003-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### SCO resources for AcuCobol-85?

- **From:** brian@brie.com (Brian Lavender)
- **Date:** 2003-09-03T00:01:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53fb18f9.0309022301.2aad5247@posting.google.com>`

```
I just converted an application that originally ran on SCO 3.2v4.2 to
SCO OSR 5.0.7. I am having various problems with the application. Do I
need to tune SCO OSR 5.0.7 for running the Accucobol app? Here's the
info regarding AcuCobol.

ortho@trouble[~]> runcbl -version
ACUCOBOL-85 runtime version 2.1.1
Vision version 3 file system
Copyright (c) 1985 - 1992, Acucobol, Inc.

Are there various settings in /etc that I would need to transfer from
the old server?

brian
```

#### ↳ Re: SCO resources for AcuCobol-85?

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-03T18:17:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qd8clvoomsq09le33hsm79afempk3dviog@4ax.com>`
- **References:** `<53fb18f9.0309022301.2aad5247@posting.google.com>`

```
On 3 Sep 2003 00:01:05 -0700, brian@brie.com (Brian Lavender) wrote:

>I just converted an application that originally ran on SCO 3.2v4.2 to
>SCO OSR 5.0.7. I am having various problems with the application. Do I
…[11 more quoted lines elided]…
>brian
And what problems are you having exactly?

If it is printing problems the solution is one thing
If it is console display problems itï¿½s another one

So please be very specific about the problems.

You will at least the configuration file if it is on /etc.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: SCO resources for AcuCobol-85?

- **From:** Brian Lavender <brian@brie.com>
- **Date:** 2003-09-09T22:26:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2mctlvk9bth9ddih23dnlh0414q7hdochr@4ax.com>`
- **References:** `<53fb18f9.0309022301.2aad5247@posting.google.com> <qd8clvoomsq09le33hsm79afempk3dviog@4ax.com>`

```
On Wed, 03 Sep 2003 18:17:21 +0100, Frederico Fonseca
<real-email-in-msg-spam@email.com> wrote:

>On 3 Sep 2003 00:01:05 -0700, brian@brie.com (Brian Lavender) wrote:
>
…[21 more quoted lines elided]…
>You will at least the configuration file if it is on /etc.

Here is the error I saw today, and I have seen before. /dev/ttya03 is
where patients can check themselves in. I have seen the error at the
terminal where the receptionist works.

remove SRTSCHa03? Dating the CheckinCRT /dev/ttya03 **remove SRTSCHa03

I type 'yes'and then I get the following error.

File error 92 on PATFILE.DAT
COBOL error at 008084 in ODECK1
Called from 0005B0 in ODRIVE

I had a previous error on the datafile DECKFILE.DAT where the data
became corrupted.

File error 98,01 on DECKFILE.DAT
COBOL error at 0080AF in ODECK1
Called from 0005B0 in ODRIVE

I replaced DECKFILE.DAT from the original tar file created to transfer
this app which was just transferred over. This restored file was out
of sync with the rest of the application. This was before I found out
about the vutil command. I thought maybe the app would pick up the
inconsistencies, or the inconsistencies would become immediately
evident. I think things might still be broken.

I think that I may have messed up when bringing the app from the
original server to the newly built one. I tarred the directory
containing the data, cobol engine, and application while users were
using it. I was thinking that it would be ok to do this, but after
thinking about it, I realized that the app probably had various data
files open during the transfer process, which may cause problems. Does
this sound likely. I tested this app before transferring it, and
things worked well with the data set used for testing. 

brian
```

###### ↳ ↳ ↳ Re: SCO resources for AcuCobol-85?

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-10T08:48:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udltlvk51krihk9cm507o1gb0r99psn8o5@4ax.com>`
- **References:** `<53fb18f9.0309022301.2aad5247@posting.google.com> <qd8clvoomsq09le33hsm79afempk3dviog@4ax.com> <2mctlvk9bth9ddih23dnlh0414q7hdochr@4ax.com>`

```
On Tue, 09 Sep 2003 22:26:59 -0700, Brian Lavender <brian@brie.com>
wrote:

>On Wed, 03 Sep 2003 18:17:21 +0100, Frederico Fonseca
><real-email-in-msg-spam@email.com> wrote:
…[30 more quoted lines elided]…
>remove SRTSCHa03? Dating the CheckinCRT /dev/ttya03 **remove SRTSCHa03
The above is part of the application. You should check the code to see
where this particular message is displayed and why.
>
>I type 'yes'and then I get the following error.
…[26 more quoted lines elided]…
>things worked well with the data set used for testing. 

NEVER NEVER NEVER create a backup with users using the files.

If this new machine has already became the prodution one then you may
already have lost vital information, and you will need to speak with
whoever created the application for them to go there and run
verification programs on all files.

If not then create a backup of the original files when NO ONE is using
them (e.g. quick everyone out and keep them out!!), and then restore
them to the new machine.

If at all feasible run vutil on the new machine, one file at the time,
and teste the application then.

regards

Frederico


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: SCO resources for AcuCobol-85?

_(reply depth: 4)_

- **From:** Brian Lavender <brian@brie.com>
- **Date:** 2003-09-10T09:31:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9kulv8njatg3n90lnbeb8hukj65ufumd7@4ax.com>`
- **References:** `<53fb18f9.0309022301.2aad5247@posting.google.com> <qd8clvoomsq09le33hsm79afempk3dviog@4ax.com> <2mctlvk9bth9ddih23dnlh0414q7hdochr@4ax.com> <udltlvk51krihk9cm507o1gb0r99psn8o5@4ax.com>`

```
On Wed, 10 Sep 2003 08:48:56 +0100, Frederico Fonseca
<real-email-in-msg-spam@email.com> wrote:

>On Tue, 09 Sep 2003 22:26:59 -0700, Brian Lavender <brian@brie.com>
>wrote:
…[14 more quoted lines elided]…
>>>>Copyright (c) 1985 - 1992, Acucobol, Inc.
[snip]
>>I think that I may have messed up when bringing the app from the
>>original server to the newly built one. I tarred the directory
…[19 more quoted lines elided]…
>and teste the application then.

Frederico, thanks for the advice. Is there a special option that I
should use with vutil? Or do I just use?

$ vutil <file.DAT>

I am thinking of going back to the old server, tar up the old data,
and reenter the new data.

brian
```

###### ↳ ↳ ↳ Re: SCO resources for AcuCobol-85?

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-10T18:34:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<utnulvocpbt9fhv9d2oog78bgihlhv6828@4ax.com>`
- **References:** `<53fb18f9.0309022301.2aad5247@posting.google.com> <qd8clvoomsq09le33hsm79afempk3dviog@4ax.com> <2mctlvk9bth9ddih23dnlh0414q7hdochr@4ax.com> <udltlvk51krihk9cm507o1gb0r99psn8o5@4ax.com> <c9kulv8njatg3n90lnbeb8hukj65ufumd7@4ax.com>`

```
On Wed, 10 Sep 2003 09:31:04 -0700, Brian Lavender <brian@brie.com>
wrote:

>On Wed, 10 Sep 2003 08:48:56 +0100, Frederico Fonseca
><real-email-in-msg-spam@email.com> wrote:
…[51 more quoted lines elided]…
>

I don't have a manual at hand at the moment.
vutil will have a rebuild option, and this in turn has a few options
that I don't remember what they are for.

so if nothing else
vutil -rebuild filename(s)


See in your users manual

As for entering the new data that is advisable if possible, as you
will be almost sure you have not lost anything.


Regards

Frederico


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
