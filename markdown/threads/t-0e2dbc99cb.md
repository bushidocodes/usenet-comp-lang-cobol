[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Oracle free to use release q

_13 messages · 7 participants · 2010-03_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Oracle free to use release q

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2010-03-17T18:36:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1268850987@f1.n250.z2.fidonet.ftn>`

```
Hello All!

Does anyone know if there is pro*cobol available on one of the free Oracle 11g 
(or later)  variants.

I would like to play with it with Open Cobol (if poss) and may be rework 
generated results to operate with Mysql.

I downloaded cobolcompiler-sources/oracle-xe-10.2.0.1-1.0.i386.rpm

but its hard to see what is included!

Vince
```

#### ↳ Re: Oracle free to use release q

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-03-17T13:13:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn>`

```
On Mar 18, 2:36 pm, "Vince Coen" <VBCoenDesp...@btconnect.com> wrote:
> Hello All!
>
…[8 more quoted lines elided]…
> but its hard to see what is included!

Use midnight commander (mc). This has a virtual file system for RPMs
(and tar, zip, gz, etc). Navigate to the rpm file, press enter and it
goes inside. CONTENTS.cpio is a directory of the files being installed
so you can move around to see what is there.

yum install mc
```

##### ↳ ↳ Re: Oracle free to use release q

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-03-18T14:40:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com>`

```
Richard wrote:
>
> Use midnight commander (mc). This has a virtual file system for RPMs
> (and tar, zip, gz, etc). Navigate to the rpm file, press enter and it
> goes inside. CONTENTS.cpio is a directory of the files being installed
> so you can move around to see what is there.

As long as we're trumpeting software, I'd like to suggest Mikogo.

Mikogo is a remote desktop tool that allows you to transfer the desktop, 
mouse, and keyboard to your machine - or vice-versa. You can also move files 
between machines.

Mikogo is free, even for commercial use, and does not require anything to be 
installed on the remote computer.

The remote user simply navigates to www.mikogo.com and enters a session-id 
which you provide. After that, the two machines are as one. Further up to 
six additional remote machines can participate in the session.

What makes this product superior to others is that it is free for commercial 
use. You can remotely assist one of your clients legally and without 
installing anything on their machine.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-03-18T17:45:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26018e7b-570c-4da3-b649-819da95ed97f@t34g2000prm.googlegroups.com>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com> <jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com>`

```
On Mar 19, 8:40 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Richard wrote:
>
…[5 more quoted lines elided]…
> As long as we're trumpeting software, I'd like to suggest Mikogo.

Does it help in finding out what is included in an RPM file ?


> Mikogo is a remote desktop tool that allows you to transfer the desktop,
> mouse, and keyboard to your machine - or vice-versa. You can also move files
…[11 more quoted lines elided]…
> installing anything on their machine.

No. That is not true.

The 'organizer' or 'presenter', ie the machine that is being looked at
by the others, _does_ require software to be installed. In the case of
providing support for a client it is the client that must install the
software so that the support can see the client's problem.

The 'participants' or viewers see the presenter's desktop on their web
browser.

While it is capable of switching to a 'participants' desktop that is
only possible if that user has the software installed.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-03-19T10:58:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdmdnRniDsO0Aj7WnZ2dnUVZ_gGdnZ2d@earthlink.com>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com> <jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <26018e7b-570c-4da3-b649-819da95ed97f@t34g2000prm.googlegroups.com>`

```
Richard wrote:
> On Mar 19, 8:40 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
>> Richard wrote:
…[8 more quoted lines elided]…
> Does it help in finding out what is included in an RPM file ?

No, Sorry. I was counting on you to be able to deduce that yourself.

We experienced computer users call this "thread drift" - it's fairly 
common - and we old-timers sometimes forget that neophytes read what we 
write.

I apologize for the oversight.

>
>
…[27 more quoted lines elided]…
> only possible if that user has the software installed.

You are mistaken. The remote location need not load any software or do 
anything other than log on to the Mikogo web site. The initiation can be 
configured to immediately take control of the remote location's computer 
upon connection (with permission). We use this several times a month and I 
assure you the remote locations load nothing on their computer.

"...an ideal feature for remote support session organizers. With it, you can 
start a session, invite a participant, and have the participant instantly 
become the presenter and show their screen to you. You can even obtain 
initial remote control of your participant's keyboard & mouse..."

You youngsters should really leave the technical stuff to your betters.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 5)_

- **From:** Duke Normandin <dukeofperl@ml1.net>
- **Date:** 2010-03-19T17:07:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbOon.71475$PH1.50284@edtnps82>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com> <jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <26018e7b-570c-4da3-b649-819da95ed97f@t34g2000prm.googlegroups.com> <bdmdnRniDsO0Aj7WnZ2dnUVZ_gGdnZ2d@earthlink.com>`

```
On 2010-03-19, HeyBub <heybub@NOSPAMgmail.com> wrote:
> Richard wrote:
>> On Mar 19, 8:40 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
…[18 more quoted lines elided]…
>

[snip]

> You youngsters should really leave the technical stuff to your betters. 


ROTFL ....... :))  :))
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-03-19T11:30:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3178fc38-5cda-4bf2-aaaf-6a8fd4201367@u5g2000prd.googlegroups.com>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com> <jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <26018e7b-570c-4da3-b649-819da95ed97f@t34g2000prm.googlegroups.com> <bdmdnRniDsO0Aj7WnZ2dnUVZ_gGdnZ2d@earthlink.com>`

```
On Mar 20, 4:58 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Richard wrote:
> > On Mar 19, 8:40 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
…[53 more quoted lines elided]…
> anything other than log on to the Mikogo web site.


From the mikogo site:

"""To join, participants simply run an executable file, which can be
downloaded directly from the Internet on demand and which is only
saved in a temporary download folder."""

I suggest that you take you leave the technical stuff to mikogo.


> The initiation can be
> configured to immediately take control of the remote location's computer
…[8 more quoted lines elided]…
> You youngsters should really leave the technical stuff to your betters.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 6)_

- **From:** Duke Normandin <dukeofperl@ml1.net>
- **Date:** 2010-03-19T18:55:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jMPon.71483$PH1.20795@edtnps82>`
- **References:** `<1268850987@f1.n250.z2.fidonet.ftn> <a9794065-3347-4e4b-8bae-5020b0ab2171@u19g2000prh.googlegroups.com> <jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <26018e7b-570c-4da3-b649-819da95ed97f@t34g2000prm.googlegroups.com> <bdmdnRniDsO0Aj7WnZ2dnUVZ_gGdnZ2d@earthlink.com> <3178fc38-5cda-4bf2-aaaf-6a8fd4201367@u5g2000prd.googlegroups.com>`

```
On 2010-03-19, Richard <riplin@Azonic.co.nz> wrote:
>
> I suggest that you take you leave the technical stuff to mikogo.
>

<plonk>
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

- **From:** starwars <nonscrivetemi@tatooine.homelinux.net>
- **Date:** 2010-03-20T20:42:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<935a533c0ad7566b8c683a16ddfd1e5e@tatooine.homelinux.net>`
- **References:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote:

How many times can you say "free" in one post?

Anything going through anybody else's server is not free. It may not cost
you money, but it costs you security.

No thanks.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-03-22T18:19:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-6OdncPQFNm8ZjrWnZ2dnUVZ_hidnZ2d@earthlink.com>`
- **References:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <935a533c0ad7566b8c683a16ddfd1e5e@tatooine.homelinux.net>`

```
starwars wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote:
>
…[5 more quoted lines elided]…
> No thanks.

In the abstract, you are correct.

But running your own server carries a not-insignificant price and even then 
you are at the mercy of nefarious packet-sniffer snoops on the internet 
connection.

You could personally visit the remote site, but that, too, costs a 
significant amount of moola. I suppose the remote site could ship their 
computer to you and, if it was, say, a laptop, it shouldn't be too 
expensive. There's the time involved, but what's a few days for security 
concerns (neglecting the small, but non-zero chance the package may be 
tampered with enroute).

All in all, as you succinctly point out, one has to weigh the benefits vs. 
confidentiality of helping a 70-year old set up an internet dominos game so 
he can play with his grandson.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-03-23T12:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hoaagf$8qk$1@reader1.panix.com>`
- **References:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <935a533c0ad7566b8c683a16ddfd1e5e@tatooine.homelinux.net> <-6OdncPQFNm8ZjrWnZ2dnUVZ_hidnZ2d@earthlink.com>`

```
In article <-6OdncPQFNm8ZjrWnZ2dnUVZ_hidnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>starwars wrote:
>> "HeyBub" <heybub@NOSPAMgmail.com> wrote:
…[8 more quoted lines elided]…
>In the abstract, you are correct.

[snip]

>All in all, as you succinctly point out, one has to weigh the benefits vs. 
>confidentiality of helping a 70-year old set up an internet dominos game so 
>he can play with his grandson. 

One may also have to weigh the benefits vs. the aggravation of hearing a 
Corner-Office Idiot wail 'But my father can use this to play dominoes with 
my sun, why can't *we* use it to share our in-house quartely financial 
breakdowns?'

DD
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-03-23T12:09:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<au0iq5lmshrvnke1j6cuj8rr977hucivq6@4ax.com>`
- **References:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <935a533c0ad7566b8c683a16ddfd1e5e@tatooine.homelinux.net> <-6OdncPQFNm8ZjrWnZ2dnUVZ_hidnZ2d@earthlink.com> <hoaagf$8qk$1@reader1.panix.com>`

```
On Tue, 23 Mar 2010 12:00:15 +0000 (UTC), docdwarf@panix.com () wrote:

>One may also have to weigh the benefits vs. the aggravation of hearing a 
>Corner-Office Idiot wail 'But my father can use this to play dominoes with 
>my sun, why can't *we* use it to share our in-house quartely financial 
>breakdowns?'

I'm trying to imagine how that game is played.
```

###### ↳ ↳ ↳ Re: Oracle free to use release q

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-03-23T19:19:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hob47s$66k$1@reader1.panix.com>`
- **References:** `<jMudnSZX_sohHD_WnZ2dnUVZ_sadnZ2d@earthlink.com> <-6OdncPQFNm8ZjrWnZ2dnUVZ_hidnZ2d@earthlink.com> <hoaagf$8qk$1@reader1.panix.com> <au0iq5lmshrvnke1j6cuj8rr977hucivq6@4ax.com>`

```
In article <au0iq5lmshrvnke1j6cuj8rr977hucivq6@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 23 Mar 2010 12:00:15 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[5 more quoted lines elided]…
>I'm trying to imagine how that game is played.

Only those with The Big Picture do, or so I've been told.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
