[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Logical vs. Physical Cancel in MF Cobol

_3 messages · 3 participants · 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Logical vs. Physical Cancel in MF Cobol

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981014091916.23889.00000514@ng25.aol.com>`
- **References:** `<70260t$squ$1@nnrp1.dejanews.com>`

```

I am not familliar with the specific compiler you are using, yet I have an idea
of what the problem is.

CANCEL only guarantees that data memory will be reset to the initial values. 
So if you had a subroutine B and had called it once or many times, iterating
through various loops.  You could reset all loop controls and all of data
memory with the CANCEL command in the higher level program which called it.

However, CANCEL does not reload the executable procedure division. There may be
an IDE command or debugger command that can do that. But CANCEL does not, and I
do not know of a COBOL verb that would.

Incremental compile and link may be built into your tools, but it does not
surface at the syntax level of the procedure division.

So you may wish to check that your recompile of program B actually entails a
relink.  Some development tools hace a Rebuild menu option. I don't know your
compiler, but you must rebuild the .EXE file not just recompile the submodule;
and then coerce a reload of the executables.


Hope that Helps,
 


Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Logical vs. Physical Cancel in MF Cobol

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-bUVMnncfSdLN@Dwight_Miller.iix.com>`
- **References:** `<70260t$squ$1@nnrp1.dejanews.com> <19981014091916.23889.00000514@ng25.aol.com>`

```
On Wed, 14 Oct 1998 13:19:16, rkrayhawk@aol.com (RKRayhawk) wrote:

> CANCEL only guarantees that data memory will be reset to the initial values. 
> So if you had a subroutine B and had called it once or many times, iterating
> through various loops.  You could reset all loop controls and all of data
> memory with the CANCEL command in the higher level program which called it.
> 

In actuality, you are not even guarenteed that - though most compilers
do, and many actually unload from memory - all you are guarenteed is 
that the items in WS with a VALUE clause are reset to that value.
```

##### ↳ ↳ Re: Logical vs. Physical Cancel in MF Cobol

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<702so4$g@dfw-ixnews3.ix.netcom.com>`
- **References:** `<70260t$squ$1@nnrp1.dejanews.com> <19981014091916.23889.00000514@ng25.aol.com> <Jl0PnHJ5PvPd-pn2-bUVMnncfSdLN@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Wed, 14 Oct 1998 13:19:16, rkrayhawk@aol.com (RKRayhawk) wrote:
>
>> CANCEL only guarantees that data memory will be reset to the initial
values.
>> So if you had a subroutine B and had called it once or many times,
iterating
>> through various loops.  You could reset all loop controls and all of data
>> memory with the CANCEL command in the higher level program which called
it.
>>
>
…[3 more quoted lines elided]…
>

A difference between the '74 and '85 Standard is that in the '85 Standard,
you ARE guaranteed that all PERFORM ranges will be "reset" by a CANCEL.
(The times that this can cause a difference are pretty obscure - but happen
when you GO TO an EXIT PROGRAM within a PERFORMED paragraph of a subroutine
and then recall it and some how hit the exit of the PERFORM range without it
being currently PERFORMED.  As I say, this is pretty obscure, but is a
documented difference between the two Standards.)

P.S.  Release of storage is definitely NOT required by the Standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
