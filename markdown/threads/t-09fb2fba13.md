[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol application running on NT4 server & clients

_4 messages · 3 participants · 1999-01_

---

### Cobol application running on NT4 server & clients

- **From:** "Stevo" <s_stevo@hotmail.com>
- **Date:** 1999-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<785d9q$kdd$1@news1.skynet.be>`

```
I work on application that was originally intended for unix and DOS
(Windows) .
The application is rather large (> 500 programs), the compiler used is from
MicroFocus (.int - files run with cobrun)

Since november this year we adapted it slightly so it runs also in a full NT
environment in a DOS-only environment.  Internal test showed that it runs
but it is 2 times slower than under win98.

Anyone that encountered this problem. Is it a setting in NT?

Best regards,

Desperate stevo.
```

#### ↳ Re: Cobol application running on NT4 server & clients

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36a69f64.169740248@news1.ibm.net>`
- **References:** `<785d9q$kdd$1@news1.skynet.be>`

```
On Wed, 20 Jan 1999 21:17:45 +0100, "Stevo" <s_stevo@hotmail.com>
wrote:

>I work on application that was originally intended for unix and DOS
>(Windows) .
…[11 more quoted lines elided]…
>Desperate stevo.

Steve, you have to remember that unless you compiled it 32 Bit - NT
has to do a lot of 16 bit Emulation - Unlike Windows 95/95 (Which is
still a 32 bit hack on top of a 16 bit OS).  

One thing that MIGHT help - and I'd appreciate you posting your
results is to use: FORCEDOS yourprogram
on the command line.

That assumes you are still compiling it for DOS and not Windows.
```

##### ↳ ↳ Re: Cobol application running on NT4 server & clients

- **From:** "Stevo" <s_stevo@hotmail.com>
- **Date:** 1999-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78f22n$r31$1@news0.skynet.be>`
- **References:** `<785d9q$kdd$1@news1.skynet.be> <36a69f64.169740248@news1.ibm.net>`

```
Thanks for your input on this matter :

FORCEDOS makes it possible to run the program
as well as DOSONLY.  I haven't found any difference yet.  What the averall
speed is concerned I found out that with a lot of users the cause laid in
malconfigured virusscanners, schedulers , ...

I was wondering if it isn't possible to get out of  that dosonly environment
to start for eg Word of Excell??
and than return to my 16bit application.

----
Compiling the application for NT (dll, gnt) is at this stage not really an
option.  We have to stay compatible with our DOS and WIN95/98, Novell users
and adding an other version complicates this too much.
(already support for 2 languages, 2 types of OS : unix sco - dos/windows)



Thane Hubbell heeft geschreven in bericht
<36a69f64.169740248@news1.ibm.net>...
>On Wed, 20 Jan 1999 21:17:45 +0100, "Stevo" <s_stevo@hotmail.com>
>wrote:
…[3 more quoted lines elided]…
>>The application is rather large (> 500 programs), the compiler used is
from
>>MicroFocus (.int - files run with cobrun)
>>
>>Since november this year we adapted it slightly so it runs also in a full
NT
>>environment in a DOS-only environment.  Internal test showed that it runs
>>but it is 2 times slower than under win98.
…[16 more quoted lines elided]…
>
```

#### ↳ Re: Cobol application running on NT4 server & clients

- **From:** "J���rgen Ibelgaufts" <ibelgaufts@gfc-net.de>
- **Date:** 1999-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A72813.A268B080@gfc-net.de>`
- **References:** `<785d9q$kdd$1@news1.skynet.be>`

```
Hi,

I wonder why you use the .int format and not the .gnt format (or .dll on windows
nt). gnt and dll are ***MUCH*** faster (I experienced 20 times in some cases) in
case you use a 32 bit Cobol. All you have to do is change the compiler option to
omf"gnt" or use the CBLLINK program with the option to create a .dll (on windows)

Hope this helps
Juergen Ibelgaufts

------------------------------------------------------------------------

Stevo schrieb:
> 
> I work on application that was originally intended for unix and DOS
…[12 more quoted lines elided]…
> Desperate stevo.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
