[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress and Caps Lock issues

_7 messages · 5 participants · 2000-03_

---

### NetExpress and Caps Lock issues

- **From:** Aaron Cardon <aaron@amnutrition.com>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DBBB7D.E8EE06FA@amnutrition.com>`

```
I am running NetExpress 3.0 with all of the patches on a PC LAN.  The
runtime system is located on a Netware 4.11 file server and the clients
registry points to the shared runtime directory.  This configuration
seems to be working well for us, with one exception.  The caps lock acts
like it is on when it is off and visa versa.  This caps lock issue is
only seen when running cobol programs.

Has anyone experienced any similar problems?

Thank You,
Aaron Cardon
American Nutrition Inc.
```

#### ↳ Re: NetExpress and Caps Lock issues

- **From:** JohndeV <johndevNOjoSPAM@yahoo.com.invalid>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<03135d23.6314a988@usw-ex0104-028.remarq.com>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com>`

```
Aaron

Is this happening on Win98 workstations only ?

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

##### ↳ ↳ Re: NetExpress and Caps Lock issues

- **From:** Aaron Cardon <aaron@amnutrition.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DC14DD.32B69F8D@amnutrition.com>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com> <03135d23.6314a988@usw-ex0104-028.remarq.com>`

```
This is happening with Windows 95 and 98.  I'm not sure if the problem occurs
with WinNT since we don't have many NT workstations running these programs.


Aaron Cardon
American Nutrition Inc.

JohndeV wrote:

> Aaron
>
…[3 more quoted lines elided]…
> The fastest and easiest way to search and participate in Usenet - Free!
```

###### ↳ ↳ ↳ Re: NetExpress and Caps Lock issues

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bna35$902$1@hyperion.mfltd.co.uk>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com> <03135d23.6314a988@usw-ex0104-028.remarq.com> <38DC14DD.32B69F8D@amnutrition.com>`

```
Aaron (et al),

This is a configuration problem in Win9x rather than a problem in
NetExpress. I do not know exactly what causes it but I DO have a solution
for you. If you ensure that the following are in CONFIG.SYS and AUTOEXEC.BAT
the problem should disappear :

CONFIG.SYS:


 DEVICE=<install-dir>\command\display.sys con=(ega,,1)

AUTOEXEC.BAT:

 mode con codepage prepare=((nnn) <install-dir>\COMMAND\ega.cpi)
 mode con codepage select=nnn
 keyb xx,,<install-dir>\COMMAND\keyboard.sys

where nnn will be 437 if you are in the U.S, and xx will be us

I hope this helps.


Aaron Cardon <aaron@amnutrition.com> wrote in message
news:38DC14DD.32B69F8D@amnutrition.com...
> This is happening with Windows 95 and 98.  I'm not sure if the problem
occurs
> with WinNT since we don't have many NT workstations running these
programs.
>
>
…[9 more quoted lines elided]…
> > * Sent from RemarQ http://www.remarq.com The Internet's Discussion
Network *
> > The fastest and easiest way to search and participate in Usenet - Free!
>
```

###### ↳ ↳ ↳ Re: NetExpress and Caps Lock issues

_(reply depth: 4)_

- **From:** Aaron Cardon <aaron@amnutrition.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFBA8E.E866D7E4@amnutrition.com>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com> <03135d23.6314a988@usw-ex0104-028.remarq.com> <38DC14DD.32B69F8D@amnutrition.com> <8bna35$902$1@hyperion.mfltd.co.uk>`

```
Gael,
You don't know how pleased our users are to finally have a solution to this
problem.  They have been putting up with this annoyance for over a year now.
I'm sure if I asked, they would bake you cakes and cookies.

Thanks again!
Aaron Cardon
American Nutrition Inc.

Gael Wilson wrote:

> Aaron (et al),
>
…[39 more quoted lines elided]…
> >
```

#### ↳ Re: NetExpress and Caps Lock issues

- **From:** "Robert Kovacic" <rjk@bigpond.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_cXC4.40656$oD3.15923@newsfeeds.bigpond.com>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com>`

```
I can confirm similar problems, but I do not have a solution.

Regards, Robert Kovacic.

Aaron Cardon <aaron@amnutrition.com> wrote in message
news:38DBBB7D.E8EE06FA@amnutrition.com...
> I am running NetExpress 3.0 with all of the patches on a PC LAN.  The
> runtime system is located on a Netware 4.11 file server and the clients
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: NetExpress and Caps Lock issues

- **From:** "Aaron Cardon" <acardon@relia.net>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5_6D4.5601$Og6.1203072@tw12.nn.bcandid.com>`
- **References:** `<38DBBB7D.E8EE06FA@amnutrition.com> <_cXC4.40656$oD3.15923@newsfeeds.bigpond.com>`

```
Do you have any other Cobol runtime environments hanging around?  Are you
still using old Cobol programs that haven't been compiled under NetExpress?


Regards,
Aaron Cardon
American Nutrition Inc.

Robert Kovacic wrote in message
<_cXC4.40656$oD3.15923@newsfeeds.bigpond.com>...
>I can confirm similar problems, but I do not have a solution.
>
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
