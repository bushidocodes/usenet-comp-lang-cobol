[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Transition from Mainframe COBOL to Merant Object COBOL

_5 messages · 4 participants · 2000-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Transition from Mainframe COBOL to Merant Object COBOL

- **From:** Art <manwae@my-deja.com>
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8atgft$hrp$1@nnrp1.deja.com>`

```
Anyone out there familiar with migrating an existing mainframe COBOL
application calling IMS to a Merant COBOL app on UNIX accesssing a DB2
or Oracle Database on another box.  Also any particular issues or
pitfalls that need to be avoided.  We are in the process of evaluating
whether to migrate to C/C++ on unix or to stay with COBOL.  Thanks much.
         ART
```

#### ↳ Re: Transition from Mainframe COBOL to Merant Object COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8auk0s$41r$1@slb0.atl.mindspring.net>`
- **References:** `<8atgft$hrp$1@nnrp1.deja.com>`

```
Are you using IMS for "DB" or "DC"?  (not their current name, but boils down
to are you using it as a database or a transaction/screen/io system - or
both)?

The answer to pitfalls on migration will vary depending on that.
```

##### ↳ ↳ Re: Transition from Mainframe COBOL to Merant Object COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D318D7.E7770F33@home.com>`
- **References:** `<8atgft$hrp$1@nnrp1.deja.com> <8auk0s$41r$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Are you using IMS for "DB" or "DC"?  (not their current name, but boils down
…[3 more quoted lines elided]…
> The answer to pitfalls on migration will vary depending on that.

A bit of amplification on what Bill has written - up-front yes I've done
my time as a systems manager with mainframes - but as a programmer -
only dinky-doo desktops.

Evaluate, evaluate. Scale of system doesn't matter, if I design A/P for
a desktop user it is pretty close to what you would do for a mainframe -
but you give yours major refinements - totally unnecessary for the small
user - but imperative for big users.

Whatever you do - don't take the big bang approach - use if possible one
self-contained module as a test-bed so that you can continue to run the
'real' application while testing the OO version and fine tuning it. Use
a common sense approach - confirm in your own minds that OO really can
do something for you. You have the necessary bread ($) - check around -
is there anybody who can talk to you as a group about OO COBOL - and not
go all prima donna on you about how MAH-VELL-USS it is - but talk in
practical terms so you can make a judgement before ever trying it.

May not be what you're after - don't know the man, having only spoken to
him briefly over the 'phone some two years ago - but talk to Will
(Wilson) Price at objectz.com/cobolreport.com; he's spent many years as
a lecturer and written one of the few practical books about OO COBOL -
he might be interested in talking to you as a group.

Jimmy
```

##### ↳ ↳ Re: Transition from Mainframe COBOL to Merant Object COBOL

- **From:** Art <manwae@my-deja.com>
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b5bj7$bi7$1@nnrp1.deja.com>`
- **References:** `<8atgft$hrp$1@nnrp1.deja.com> <8auk0s$41r$1@slb0.atl.mindspring.net>`

```
We use IMS for both the DB and DC aspects.  However in the application I
am looking at the there is no DC aspect.  The application is a
background reporting app.  We have COBOL programmers that maintaint the
existing application.  We are looking at rehosting the data on a UNIX
box and the group wants to figure out if they should make the break to
C/C++ for this or go to Object COBOL.  I would not say that the group is
experienced in OO methods and the first attempt if they write the Object
COBOL will likely be more a port than a reenginering.
                            ART

In article <8auk0s$41r$1@slb0.atl.mindspring.net>,
"William M. Klein" <wmklein@nospam.netcom.com> wrote:
> Are you using IMS for "DB" or "DC"? (not their current name, but boils
down
> to are you using it as a database or a transaction/screen/io system -
or
> both)?
>
…[5 more quoted lines elided]…
> Art <manwae@my-deja.com> wrote in message
news:8atgft$hrp$1@nnrp1.deja.com...
> > Anyone out there familiar with migrating an existing mainframe COBOL
> > application calling IMS to a Merant COBOL app on UNIX accesssing a
DB2
> > or Oracle Database on another box. Also any particular issues or
> > pitfalls that need to be avoided. We are in the process of
evaluating
> > whether to migrate to C/C++ on unix or to stay with COBOL. Thanks
much.
> > ART
> >
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Transition from Mainframe COBOL to Merant Object COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d26083.740771927@news.cox-internet.com>`
- **References:** `<8atgft$hrp$1@nnrp1.deja.com>`

```
On Fri, 17 Mar 2000 14:46:23 GMT, Art <manwae@my-deja.com> wrote:

>Anyone out there familiar with migrating an existing mainframe COBOL
>application calling IMS to a Merant COBOL app on UNIX accesssing a DB2
>or Oracle Database on another box.  Also any particular issues or
>pitfalls that need to be avoided.  We are in the process of evaluating
>whether to migrate to C/C++ on unix or to stay with COBOL.  Thanks much.

I think you want to go with Mainframe Express.  The advantage?
Virtually all of your code stays the same.  The disadvantage?  The C++
Weenie doesn't get his way. The next advantage?  The project suceeds.
I've seen many attempted ports from COBOL to C++ fail - sometimes
taking the company with them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
