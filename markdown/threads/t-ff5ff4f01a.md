[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MFCobol application under NT service

_3 messages · 3 participants · 1999-11_

---

### MFCobol application under NT service

- **From:** dkerov@my-deja.com
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vovbe$gqc$1@nnrp1.deja.com>`

```
DISPLAY under NT service in MFCOBOL.

Could anyone help with following issue:

We have NT Service which sometimes starts
executeable created using MF COBOL.

This COBOL executable looks like following:

	1000-BEGIN.
	Do some database processing.
	.....
	DISPLAY result-of-database-processing
	.....
	CALL WIN32WaitForSingleObject USING OUR-
PROPRIATARY-EVENT, INFINITE
	GO TO	1000-BEGIN.

We have no problems when running executable from
the command prompt(without service).
But under the service this executable exits when
current user performs LOGOFF.

The service was started automatically at NT
startup under SYSTEM account and
the executable also started under SYSTEM account
at that same moment.

When we removed all DISPLAY statements the
problem disappeared.....

Does sombody knows what is the problem.

Thank you very much.
Dmitry Kerov.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: MFCobol application under NT service

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vp9eq$7ik$1@hyperion.mfltd.co.uk>`
- **References:** `<7vovbe$gqc$1@nnrp1.deja.com>`

```
If its V4 of MF COBOL then there was a fix made that stopped an COBOL
application terminating when the current user logged off. I would recommend
getting the latest updates V4.0.38 as that should cure your problem.

Regards
David.

<dkerov@my-deja.com> wrote in message news:7vovbe$gqc$1@nnrp1.deja.com...
> DISPLAY under NT service in MFCOBOL.
>
…[36 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: MFCobol application under NT service

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vpj9u$1d7$1@news.cerf.net>`
- **References:** `<7vovbe$gqc$1@nnrp1.deja.com>`

```
dkerov@my-deja.com wrote in message <7vovbe$gqc$1@nnrp1.deja.com>...
>DISPLAY under NT service in MFCOBOL.

There are several opportunities here.

One issue is that there is a known bug in Windows NT, such that 32 bit
console applications being launched from an application or console does not
get their STDERR, STDOUT etc properly setup, actually the fail. There were
suggested a work around to this issue on MSDN, unfortunately I don't
remember it, you may want to look for it yourself, I believe I searched for
STDERR.

An other issue is the security context, which although is good to have,
sometimes may drive a man crazy. Check out in your service manager that your
application actually has system (local system) as owning process. Then look
up

    Start | Programs | Administrative tools | User manager

Choose

    Policies | User rights

Check

    Show advanced user rights

Click on the list box and select:

    Act as part of the operating system

See if the

    Administrator

Is one of those granted. If not, add the user group.

I don't know for sure this will help, but it is worth a try. Remember to
reboot after the change.

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
