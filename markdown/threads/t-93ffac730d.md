[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# On User Defined Functions and OO

_2 messages · 2 participants · 2008-12_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### On User Defined Functions and OO

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-22T22:26:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WLZ3l.3469$kG.2563@en-nntp-06.dc1.easynews.com>`

```
I am not now, nor was I ever a "compiler developer" (or even a run-time 
developer).  I know COBOL for its "externals" (and I know those VERY well).

However,
  in response to the "what does User defined functions have to do with adding OO 
to OpenCOBOL" question, I did some thinking.  I may be totally wrong on this, 
but here is my take on this.  (Probably NOT what was meant by the original 
poster).

To me, there are "two flavors" (or externals) for Object Orientation (at least 
in COBOL).  The source code that "uses" options via
  - INVOKE statement
  - inline object reference

Such code may be "traditional procedural COBOL code" *or* it may be within the 
methods of an Object itself.

From an explicitly EXTERNAL point of view, the compiler developer really needs 
to do very little more for INVOKE than CALL (especially CALL with returning) 
already supports.  Furthermore, again from my external point of view,
  CALL with RETURNING is to User (or intrinsic) Functions
      as
  INVOKE is to inline object references

I can (relatively) easily imagine both of these being coded by compiler 
developers in "similar" ways.

Now, when it comes to RUN-TIME support for these,  there is a lot more than 
"traditional" CALL support.  There is "resolution" of what method is being 
invoked as determined by the object being "used".  Furthermore, there is the 
whole question of "conformance" of parameters (especially with polymorphism and 
method overloading).  I may be crazy on this, but I do see these as run-time, 
not compiler issues.  Furthermore, for those implementations that include 
support for the (extension) ENTRY feature of COBOL, some of the "resolution" 
issues may already be solved (at least in part).  And with "parameter 
conformance" and "call prototypes" in the 2002 Standard, I can imagine the OO 
features being solved in "similar" (NOT identical) ways as features that are 
required by non-OO support.

Now, as far as compiler (and run-time) support for CLASS definitions and the 
entire "OO structure" of source code, this does require a different set of 
compiler support.  But again, with nested programs, global and local data, even 
EXTERNAL data that "persists" across programs, I would think that much (not all) 
of the "development" may be there.  And once again, support for multiple ENTRY 
statements within a "procedural" program MAY be the starting point for 
developing compile and run-time support for multiple methods within the same 
class definition.

And back to user defined functions, it would seem to me that if a compiler did 
support these (and their parameter conformance checking issues and "inline" 
syntax) much of this could be used as the basis for OO support in the compiler 
(and possibly even the run-time).

  ***

What needs to be made SUPER clear with this note is that I am *not* saying that 
the "paradigm" of coding OO COBOL is that similar to existing (traditional 
procedural) COBOL.  I am only saying that I can imagine compiler and run-time 
support for nested programming, ENTRY (extension), and user defined functions as 
being the "implementer" starting point for providing OO support in a COBOL 
implementation.

However, as I started out, it is also important to say that I am not an 
implementor, so what would seem "similar" to me for externals may well actually 
provide little or no help to developing a full OO COBOL compiler (and run-time).

As usual, your mileage may vary <G>
```

#### ↳ Re: On User Defined Functions and OO

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-12-24T09:16:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6rcv9hFmlr9U1@mid.individual.net>`
- **References:** `<WLZ3l.3469$kG.2563@en-nntp-06.dc1.easynews.com>`

```
William M. Klein wrote:
> I am not now, nor was I ever a "compiler developer" (or even a
> run-time developer).  I know COBOL for its "externals" (and I know
…[23 more quoted lines elided]…
> compiler developers in "similar" ways.

The mechanics are certainly similar.
>
> Now, when it comes to RUN-TIME support for these,  there is a lot
…[5 more quoted lines elided]…
> issues.

That depends on whether the object is early or late bound. I only use late 
bound, so for me at least, it is a runtime issue, but with early bound code 
compliance is checked at compile time, using the Repository to obtain 
formats and prototypes.


 Furthermore, for those implementations that include support
> for the (extension) ENTRY feature of COBOL, some of the "resolution"
> issues may already be solved (at least in part).

Hmmm... I think I understand what you're saying, Bill, but not sure about 
that. Reference to entry points can be resolved statically or dynamically, 
as you know, and the mechanism is different for each of these. Nevertheless, 
there are general similarities and if a compiler writer already had this 
covered, that code could almost certainly serve as a template for method 
invocation.


>  And with "parameter
> conformance" and "call prototypes" in the 2002 Standard, I can
> imagine the OO features being solved in "similar" (NOT identical)
> ways as features that are required by non-OO support.

Yes, that sems likely.
>
> Now, as far as compiler (and run-time) support for CLASS definitions
…[7 more quoted lines elided]…
> the same class definition.

It's a bit tenuous I think, but in principle, "probably" :-)
>
> And back to user defined functions, it would seem to me that if a
> compiler did support these (and their parameter conformance checking
> issues and "inline" syntax) much of this could be used as the basis
> for OO support in the compiler (and possibly even the run-time).

You'd think so...
>
>  ***
…[6 more quoted lines elided]…
> starting point for providing OO support in a COBOL implementation.

I agree that would make sense if a compiler was being built from scratch. 
The difficulty arises, I think, in having to "bolt on" the OO functionality 
without upsetting what is already in place. I have never ceased to be amazed 
by the engineers who did this for Fujitsu and Micro Focus; it is an 
extraordinary piece of work.

>
> However, as I started out, it is also important to say that I am not
…[3 more quoted lines elided]…
> As usual, your mileage may vary <G>

I take your points that there is mechanical similarity in some of the 
existing functionality, but neither of us are actually going to do it and it 
really comes down to what the implementor already has to work with. I think 
if I were tasked todo this, I would use existing code as a model but would 
keep the whole area separate from the rest of the compiler, even if this 
meant some duplication of code.

It would certainly be an interesting challenge... :-)

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
