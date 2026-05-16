[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# runcobol under linux: keyword problem

_5 messages · 2 participants · 2004-04_

---

### runcobol under linux: keyword problem

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-10T13:43:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404101243.6a8a6315@posting.google.com>`

```
Hi friends

Im using application in runcobol running in a RH 9.0
My machine is a PC compatible PIII
I can access the application but my problem is that I cant use either
funtion keys nor cursor keys.
My TERM=xterm
Is there a better terminal for this ?
What terminal should I use in order to get these keys works?

Thanks in advance
Juan
```

#### ↳ Re: runcobol under linux: keyword problem

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-04-10T22:20:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5pg701k3t2senstjnmc4ebhphdv5153ms@4ax.com>`
- **References:** `<bf8a559b.0404101243.6a8a6315@posting.google.com>`

```
On 10 Apr 2004 13:43:53 -0700, jchipocov@yahoo.com.ar (Juan) wrote:

>Hi friends
>
…[9 more quoted lines elided]…
>Juan

Look at the configuration section of your Runtime users manual

You can configure what keys are going to act as cursor/functions keys.

This is done by using the correct terminfo.cfg file, associated with a
complete terminfo (or termcap) entry.

If you donï¿½t know how to do this please post the configuration file
you are using along with your terminfo/termcap configuration for the
TERM used. 





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: runcobol under linux: keyword problem

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-10T23:03:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404102203.762b150f@posting.google.com>`
- **References:** `<bf8a559b.0404101243.6a8a6315@posting.google.com> <b5pg701k3t2senstjnmc4ebhphdv5153ms@4ax.com>`

```
Hi Frederico

I have been looking for information about terminfo.cfg and there is
few pages
My terminfo file is like liant page:
http://www.liant.com/support/terminal/terminfo.cfg
My /etc/terminfo and /etc/termcap are very large to post here
If you send me your email I could send you

But if you have some link that can help me I will apreciate you
kindness.

Juan
jchipoco@hotmail.com


Frederico Fonseca <real-email-in-msg-spam@email.com> wrote in message news:<b5pg701k3t2senstjnmc4ebhphdv5153ms@4ax.com>...
> On 10 Apr 2004 13:43:53 -0700, jchipocov@yahoo.com.ar (Juan) wrote:
> 
…[29 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: runcobol under linux: keyword problem

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-04-11T21:14:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0c9j705lcgfceb99ga4pkslm2tq69id6vp@4ax.com>`
- **References:** `<bf8a559b.0404101243.6a8a6315@posting.google.com> <b5pg701k3t2senstjnmc4ebhphdv5153ms@4ax.com> <bf8a559b.0404102203.762b150f@posting.google.com>`

```
On 10 Apr 2004 23:03:45 -0700, jchipocov@yahoo.com.ar (Juan) wrote:
Moved Top-post to correct place
>Hi Frederico
>
…[45 more quoted lines elided]…
>
Juan,

Each terminal will have itï¿½s own entry on the terminfo/termcap.
So if you are using a xterm terminal type this is the one you have to
post here, not the whole file.

As for what you need to look for on the entry, here is an example.

Your terminfo.cfg has the following entries
TERM-INPUT action=left-arrow			kcub1
TERM-INPUT action=right-arrow			kcuf1

For these keys to work as left/right arrows within your program you
need to have kcub1 and kcuf1 defined on your terminfo entry, and they
should have the correct value.

The value can sometimes be found by hitting the corresponding key on a
xterm window, and hitting enter after pressing each key you are
testing. This will sometimes display a value you can interpret and
compare with the value on the terminfo definition.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: runcobol under linux: keyword problem

_(reply depth: 4)_

- **From:** jchipocov@yahoo.com.ar (Juan)
- **Date:** 2004-04-14T20:42:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8a559b.0404141942.467d406d@posting.google.com>`
- **References:** `<bf8a559b.0404101243.6a8a6315@posting.google.com> <b5pg701k3t2senstjnmc4ebhphdv5153ms@4ax.com> <bf8a559b.0404102203.762b150f@posting.google.com> <0c9j705lcgfceb99ga4pkslm2tq69id6vp@4ax.com>`

```
Thaks Frederico
I did the following:
#infocmp xterm > xterm.txt copied the source code for the TERM setting
into a file called xterm.txt then I changed the up and down arrows
configuration and run this command:
#tic xterm.txt 
The compiled output was placed into a subdirectory of the directory
defined by the TERMINFO environment variable. This subdirectory is
named with the first letter of the first line in the terminfo source
file. Then I got my cursor keys work ok.
Now I have following problem:
My rm Cobol application is in 80x24 format and I would wish that some
reports
appears in a 132x65 format. When I tried :#xterm -geometry 132x65 I
got my xterm terminal resize to that resolution but my cobol
application keeps with 80x24 format, Where should I do the changes in
order to resize my application size???

Thanks in advance

Juan
 





Frederico Fonseca <real-email-in-msg-spam@email.com> wrote in message news:<0c9j705lcgfceb99ga4pkslm2tq69id6vp@4ax.com>...
> On 10 Apr 2004 23:03:45 -0700, jchipocov@yahoo.com.ar (Juan) wrote:
> Moved Top-post to correct place
…[73 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
