[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How much is a run-time fee?

_2 messages · 2 participants · 2002-08_

---

### How much is a run-time fee?

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2002-08-14T11:28:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020814072809.20360.00000303@mb-fv.aol.com>`

```
As I understand it, Microfocus COBOL requires a "run-time fee." 
How much is it?  Is it a one-time payment?  Or do you pay monthly? 
Does the size of the payment vary with the size of the program?  Or vary
with the size of the customer's ability to pay?  

If it's a one-time one-rate-for-everybody payment...
Suppose you install a second program?  Is there another fee to pay? 

If I write a program and sell it to a customer, and that one customer
runs the program on four stand-alone PC's, is that four run-time fees? 
Is there a discount for additional copies at the same site?  
Suppose the customer installs one program on a server and ten
PC's run it off the network, is that one run-time fee or ten? 



Ross
http://community.webshots.com/user/ross_klatte
```

#### ↳ Re: How much is a run-time fee?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-14T14:24:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0208141324.68fa8446@posting.google.com>`
- **References:** `<20020814072809.20360.00000303@mb-fv.aol.com>`

```
klatteross@aol.commmm (Ross Klatte) wrote

> As I understand it, Microfocus COBOL requires a "run-time fee." 
> How much is it?  Is it a one-time payment?  Or do you pay monthly? 
> Does the size of the payment vary with the size of the program?  Or vary
> with the size of the customer's ability to pay?  

You purchase run-times (or are supposed to) in 10 user packs for a
site. Annual support is extra at around 20% of purchase or so.

Up until the most recent versions of MF the developer licence has
allowed construction of run-time free distribution as long as only a
subset of the facilities are built into the program.  For example on
DOS/Windows the program must be built from .EXEs and .DLL and not .int
or .gnt. Things like callable rebuild, panels, fileshare server, some
called routines meant that run-time licence was required.

While this free subset was specifically in the manual and in the
licence most MF sales people categorically denied that this existed or
meant what it stated and/or didn't apply in any case and had been
superceeded and replaced (even if the developer hadn't upgraded).

On Unix it seems that there is a way of static linking a system to
avoid run-times but it is quite restrictive.

> If it's a one-time one-rate-for-everybody payment...
> Suppose you install a second program?  Is there another fee to pay? 

The run-time licence is per user.  However if the user is running two
applications (or one appication twice) at the same time then that
counts as two users - apparently.

> If I write a program and sell it to a customer, and that one customer
> runs the program on four stand-alone PC's, is that four run-time fees? 

Yes.  Or 10 as user licences come in 10 packs.  Allegedly small
developers can split packs for small users as a 'concession'.

> Is there a discount for additional copies at the same site?  
> Suppose the customer installs one program on a server and ten
> PC's run it off the network, is that one run-time fee or ten? 

One pack of 10.  Or more if users want to run multiple copies of an
application on their screen.  However if at one time only 5 of those
machines run two copies each then that too, is 10 (allegedly).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
