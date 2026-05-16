[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus File Share Component

_4 messages · 4 participants · 1999-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus File Share Component

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uj7k2.965$x5.17896239@news1.i1.net>`

```
If there is anyone out in here who is currently using Micro Focus File Share
for Windows NT Server 4.0, and you are having problems with it please email
me this is very important.
Problems like:
1.  File share running very slow
2.  CPU resources being hogged by file share
3.  Corrupted date
4.  ANY THING ELSE PERTAINING TO FILE SHARE

THIS IS VERY IMPORTANT

twright@larimore.net
```

#### ↳ Re: Micro Focus File Share Component

- **From:** <kenmullins@mindspring.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76tbgf$mln$1@camel0.mindspring.com>`
- **References:** `<Uj7k2.965$x5.17896239@news1.i1.net>`

```
Haven't had problems with corrupted dates, but I can tell you that fileshare
is VERY CLIENT HEAVY...i.e. most of the processing seems to be done on the
client machine rather than the server machine...I have used it in several
applications now, and find it is better to have faster client machines than
a faster server...I posted complaints and documentation etc to MF, but as
usual, no response from them as to why nor any info on possibly tuning the
environments...

Ken Mullins
Atlanta, GA

Tom Wright wrote in message ...
>If there is anyone out in here who is currently using Micro Focus File
Share
>for Windows NT Server 4.0, and you are having problems with it please email
>me this is very important.
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Micro Focus File Share Component

- **From:** "J���rgen Ibelgaufts" <ibelgaufts@gfc-net.de>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369DE328.3EA2E9A0@gfc-net.de>`
- **References:** `<Uj7k2.965$x5.17896239@news1.i1.net>`

```
HI,

I tried fileshare a couple of years ago and I took my fingers off it because:

- it was very slow (although faster than opening fines through a network without
fileshare)

- you have to install the complete software on all client machines

- you have to UPDATE all client machines when your application changes

- you have to carefully think about security because ALL data will be transferred
through the network

I changed our software into client/server software where instead of
DISPLAYing/ACCEPTing I make calls to a communication program that sends and
receives the screens to/from the client machines. The client machines contain only
the client software while the server holds the data files and runs the user
programs. All files are opened locally by the server. The network will only see
the screen data and not the complete data. Files do not break when a user kills
his client program, and the thing is quite fast. When you sit in front of the
server, you can see what the users do because every user has a console program
running on the server printing out the currently used screen name. 

Juergen Ibelgaufts

----------------------------------------------------------------------

Tom Wright schrieb:
> 
> If there is anyone out in here who is currently using Micro Focus File Share
…[10 more quoted lines elided]…
> twright@larimore.net
```

##### ↳ ↳ Re: Micro Focus File Share Component

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369DFD73.8DAA82EA@bdssoftware.com>`
- **References:** `<Uj7k2.965$x5.17896239@news1.i1.net> <369DE328.3EA2E9A0@gfc-net.de>`

```


"Jï¿½rgen Ibelgaufts" wrote:
[snip]
> I changed our software into client/server software where instead of
> DISPLAYing/ACCEPTing I make calls to a communication program that sends and
…[3 more quoted lines elided]…
> the screen data and not the complete data.
[snip]
Interesting.  What communications program are you using?
TIA

Scott
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
