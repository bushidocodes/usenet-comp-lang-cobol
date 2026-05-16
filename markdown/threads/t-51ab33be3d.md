[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# data exception

_4 messages · 4 participants · 1999-02_

---

### data exception

- **From:** <myron.coulson@ibm.net>
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c78b7f@news1.us.ibm.net>`

```
I'm debugging a program that keeps moving character data into a numeric
field. I've checked every instance where this field is referenced, and I
don't see in data lay over    or anything like that. this field is being
passed data from a sub-program that calculates a fee for the field. I have
heard that this type of thing can happen when tables are exceeded. the
invalid data remains in the field and when the field is referenced down
stream, soc7.  any ideas?  thank you...
```

#### ↳ Re: data exception

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c7a906.18419688@news1.ibm.net>`
- **References:** `<36c78b7f@news1.us.ibm.net>`

```
On Sun, 14 Feb 1999 21:56:22 -0800, <myron.coulson@ibm.net> wrote:

>I'm debugging a program that keeps moving character data into a numeric
>field. I've checked every instance where this field is referenced, and I
…[4 more quoted lines elided]…
>stream, soc7.  any ideas?  thank you...

Check the call parms against the linkage section of the called
program.  Make sure EVERYTHING matches.
```

#### ↳ Re: data exception

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36C80E94.9D27E1EC@zip.com.au>`
- **References:** `<36c78b7f@news1.us.ibm.net>`

```
You state S0C7 and therefore I assume MVS.  Compile with the option
SSRANGE.  This will introduce all the checking automatically and if you
use TEST(ALL,SYM) it will give you a line number and a structured dump.

Let us know what happens...
Ken

myron.coulson@ibm.net wrote:
> 
> I'm debugging a program that keeps moving character data into a numeric
…[5 more quoted lines elided]…
> stream, soc7.  any ideas?  thank you...
```

##### ↳ ↳ Re: data exception

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990216112214.03165.00002433@ng18.aol.com>`
- **References:** `<36C80E94.9D27E1EC@zip.com.au>`

```
It sounds like you are on track with your thinking and the good recommendations
 that you have received so far.  

Additionally, you might want to do some problem isolation.  Display the data
just before and after the invocation of the submodule to confirm that the
problem lies therein. Display the data as character data (perhaps from a group
item) not as numeric.

In addition to a hunt for wild subscripts in table processes, you may wish to
review any reference modification.

Also, another postor recommended that you review in your submodule the specific
linkage section data layout for exact match to the layout of data in your
calling program. Note further, if you pass more than one area, that it is the
sequence of the items in the invoking and receiving USING clauses that
determine the areas to be matched up. (rarely, but sometimes, folks do not
realize that the sequence of 01s in the LINKAGE section has no effect).

Best WIshes,

Robert Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
