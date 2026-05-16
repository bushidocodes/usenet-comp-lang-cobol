[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe systems?

_9 messages · 7 participants · 2000-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Mainframe systems?

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>G Moore wrote:
>> 
…[8 more quoted lines elided]…
>Strange question, are you willing to give up any more info.

i was just wondering if there is any need to upgrade from mainframes
and dumb (3270) terminals to client/server for clients.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: Mainframe systems?

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.13567d4ba9d369fa9896a5@news.freedombird.net>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com>`

```
I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
> Ken Foskey <waratah@zip.com.au> wrote:
> 
…[13 more quoted lines elided]…
> and dumb (3270) terminals to client/server for clients.

None that I have ever seen, especially as the 3270 isn't as dumb as a lot 
of people try to make out.  If you want good CAD/CAM stuff, CADAM/Catia 
provides this in spades but I've forgotten the model numbers for the 
terminals used with that sort of application.

The only justification for PCs with terminal emulators is the 
availability of wordprocessing and the like, and consequently not wanting 
to take up deskspace with two keyboards and screens.

I honestly don't understand why the likes of IBM haven't come up with a 
terminal that also has a few, possibly hard-wired, local applications.  I 
did think that they might have done this when Java appeared on the scene, 
but no.  If they could be produced at a reasonable price, I'm sure a lot 
of IT managers would look seriously at them to reduce the on-cost that 
PCs incur, not only in hardware and software, but also in network and 
support costs, not to mention getting rid of the Toytown stuff that a lot 
of users crowd their PCs with.  I've never had a virus at home but I've 
seen loads of them infesting PC LANs in big offices.
```

##### ↳ ↳ Re: Mainframe systems?

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38EC93A8.5D46D530@cusys.edu>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net>`

```
Charles F Hankel wrote:
> 
> The only justification for PCs with terminal emulators is the
> availability of wordprocessing and the like, and consequently not wanting
> to take up deskspace with two keyboards and screens.

I love being able to cut and paste.  CTL-C & CTL-V are my good friends,
even when the only program I'm running is my 3270 emulator.

I just wish it were easier to switch between 80 and 132 column
emulation.
 
> I honestly don't understand why the likes of IBM haven't come up with a
> terminal that also has a few, possibly hard-wired, local applications.  I
…[6 more quoted lines elided]…
> seen loads of them infesting PC LANs in big offices.

It is cheaper to simply have a network computer.   The primary
applications we use at work are:
1.  3270 Emulator
2.  Microsoft Office on the LAN (primarily for documentation on the LAN)
3.  Netscape on the LAN (primarily for documentation on the LAN)
4.  E-mail

For the above, there certainly isn't a need for a floppy drive, and a
hard drive could be eliminated as well (making it easier to dial in from
home and access my saved e-mail).
```

###### ↳ ↳ ↳ Re: Mainframe systems?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OpYAIGDo$GA.271@cpmsnbbsa04>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net> <38EC93A8.5D46D530@cusys.edu>`

```
There used to be a product called TPX (for MVS), or Terminal Productivity
Executive.  It's main purpose was to manage multiple sessions in differing
software at once so that you could be logged into CA-7, TSO, CICS, and
anything else made known to TPX.  It had a cut and paste feature usable in
any of these environments, although it wasn't as good as a PC's cut and
paste.  The ISPF/PDF editing facility had CUT and PASTE after a fashion, but
it was only inside ISPF.

You're not the only one wishing it was a snap to switch between 80 and 132
columns.  My favorite working screen was 43x80, but that was only because
the 132 column screens did weird things when you had ISPF split screens when
one screen supported 132 columns fully, and the other screen did not.  Oh,
and this was all back on an MVS/XA system.


"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:38EC93A8.5D46D530@cusys.edu...
> Charles F Hankel wrote:
> >
> > The only justification for PCs with terminal emulators is the
> > availability of wordprocessing and the like, and consequently not
wanting
> > to take up deskspace with two keyboards and screens.
>
…[7 more quoted lines elided]…
> > terminal that also has a few, possibly hard-wired, local applications.
I
> > did think that they might have done this when Java appeared on the
scene,
> > but no.  If they could be produced at a reasonable price, I'm sure a lot
> > of IT managers would look seriously at them to reduce the on-cost that
> > PCs incur, not only in hardware and software, but also in network and
> > support costs, not to mention getting rid of the Toytown stuff that a
lot
> > of users crowd their PCs with.  I've never had a virus at home but I've
> > seen loads of them infesting PC LANs in big offices.
…[10 more quoted lines elided]…
> home and access my saved e-mail).
```

##### ↳ ↳ Re: Mainframe systems?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j3opes8tqsj4bv23ouckc0hagl7ohcfqgk@4ax.com>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net>`

```
On Thu, 6 Apr 2000 14:21:47 +0100, Charles F Hankel <noos@hankel.freedombird.net> wrote:

>I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
>> Ken Foskey <waratah@zip.com.au> wrote:
…[20 more quoted lines elided]…
>
Of course the 3270 is dumb - Look at this: You take an Intelligent Work Station,  ADD to
this Hardware (like NIC), and Software (like PC comm 4.3), and what is the result of the
added value - a 3270 emulatin (dumb terminal) ... eerrrh - am I  getting some mixed
signals here?

>The only justification for PCs with terminal emulators is the 
>availability of wordprocessing and the like, and consequently not wanting 
…[3 more quoted lines elided]…
>terminal that also has a few, possibly hard-wired, local applications.

Like the IBM 3600?  or 4700?, or 8100?, of course, at least 2 out of these 3 are history
now
 
With kind regards

Volker Bandke
     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Ultimate office automation: networked coffee.
```

###### ↳ ↳ ↳ Re: Mainframe systems?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cthr101jmk@enews4.newsguy.com>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net> <j3opes8tqsj4bv23ouckc0hagl7ohcfqgk@4ax.com>`

```
True, our "Host Explorer" is just a dumb terminal really with some decent 
cut and paste features that are handy.  Why doesn't someone invent the
double cut and paste.  Cut 1  Cut  2   Paste 1  Paste 2 in the Edit menu.  2
clipboards, if you will.

I'm not disagreeing with anyone at all, but my job necessitates me to use
more than just the "Host Explorer."  I also use many other tools every day.

I find Windows NT pretty stable to be honest with you.  Our old "Dynacomm
Elite" terminal used to crash the whole desktop when the connection to the
host was lost.  WordPerfect is sometimes unstable, especially when doing
macros and scripts.  But it's working pretty good for me lately, it probably
only crashes about once a month and that's being used pretty much all day on
my 8-5 shifts.

Some FUEL for the FIRE baby!

Jeff (on call)

----------
In article <j3opes8tqsj4bv23ouckc0hagl7ohcfqgk@4ax.com>, Volker Bandke
<vbandke@bsp-gmbh.com> wrote:


> On Thu, 6 Apr 2000 14:21:47 +0100, Charles F Hankel
> <noos@hankel.freedombird.net> wrote:
…[28 more quoted lines elided]…
> added value - a 3270 emulatin (dumb terminal) ... eerrrh - am I  getting some
mixed
> signals here?
>
…[19 more quoted lines elided]…
>          Ultimate office automation: networked coffee.
```

###### ↳ ↳ ↳ Re: Mainframe systems?

_(reply depth: 4)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000410195739.15256.00000818@ng-cn1.aol.com>`
- **References:** `<8cthr101jmk@enews4.newsguy.com>`

```
Jeff Baynard writes...

[snip]

> Why doesn't someone invent the
>double cut and paste.  Cut 1  Cut  2   Paste 1  Paste 2 in the Edit menu.  2
>clipboards, if you will.

[snip]

The newest ISPF editor (IBM mainframe editor) can do that and more (up to 10
clipboards; and you can append into a clipboard).

Regards,



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Mainframe systems?

_(reply depth: 4)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fic5fsk6ljc0i3eqkec5ba4skhtcshdr35@4ax.com>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net> <j3opes8tqsj4bv23ouckc0hagl7ohcfqgk@4ax.com> <8cthr101jmk@enews4.newsguy.com>`

```
On Mon, 10 Apr 2000 17:41:48 -0400, "Jeff Baynard" <union27@macconnect.com> wrote:

>True, our "Host Explorer" is just a dumb terminal really with some decent 
>cut and paste features that are handy.  Why doesn't someone invent the
>double cut and paste.  Cut 1  Cut  2   Paste 1  Paste 2 in the Edit menu.  2
>clipboards, if you will.
>
If I remember correctly, this feature is part of OFFICE 2000.  On the mainframe you have
it in ISPF, where you can cut/paste to more than one clipboard

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Daddy, why doesn't this magnet pick up this floppy disk?
```

###### ↳ ↳ ↳ Re: Mainframe systems?

_(reply depth: 5)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d0fbi02r8j@enews1.newsguy.com>`
- **References:** `<38E19325.DEF76E92@pacbell.net> <n3j4eso8avdar2ja50aq71322a4pk2981h@4ax.com> <38E35916.E61F4564@zip.com.au> <j4faes8f9dnaa7qcteod3kqu1jkt7rdite@4ax.com> <MPG.13567d4ba9d369fa9896a5@news.freedombird.net> <j3opes8tqsj4bv23ouckc0hagl7ohcfqgk@4ax.com> <8cthr101jmk@enews4.newsguy.com> <fic5fsk6ljc0i3eqkec5ba4skhtcshdr35@4ax.com>`

```
But we use Roscoe in our Programmer's Workbench environment.  I don't think
it has such capabilities.

Jeff

----------
In article <fic5fsk6ljc0i3eqkec5ba4skhtcshdr35@4ax.com>, Volker Bandke
<vbandke@bsp-gmbh.com> wrote:


> On Mon, 10 Apr 2000 17:41:48 -0400, "Jeff Baynard" <union27@macconnect.com>
wrote:
>
>>True, our "Host Explorer" is just a dumb terminal really with some decent
…[13 more quoted lines elided]…
>          Daddy, why doesn't this magnet pick up this floppy disk?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
