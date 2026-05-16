[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Did I write a good (efficient) program?

_10 messages · 3 participants · 2008-04_

---

### Re: Did I write a good (efficient) program?

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-04-01T13:04:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47F232DA.6F0F.0085.0@efirstbank.com>`

```
>>> On 3/31/2008 at 8:40 PM, in message
<c463v3p7pdl8dc6dl5seo7j6u0mfrev3qr@4ax.com>, Robert<no@e.mail> wrote:
> In 1973 everything (except files) was fixed length. We used fixed length 
> strings, numbers,
…[4 more quoted lines elided]…
> are opposed.

Is anyone here a member of this Old Guard that is opposed to variable length
strings?  I certainly am not.  I would love them.

Frank
```

#### ↳ Re: Did I write a good (efficient) program?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-04-02T02:54:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vzCIj.8760$fY6.7941@fe11.news.easynews.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com>`

```
Frank,
  As currently included in WD 1.10, I am very much opposed to it.  The problem 
is that the current definition allows the data to be stored within the structure 
("DIRECT") and to have such items within ODO's and with data after this.  What 
this means is that the "data" after the variable length field MUST be "moved" in 
storage each time the variable data size changes.

If the proposed definition
 - only allowed for "direct" variable length fields at the 01-level,
 - allowed for "indirect" variable length items within structures
 - figured out how to handle such fields within FILES (or disallowed it there),
 - didn't allow the same variable length field to be BOTH prefixed and suffixed

then I would be for it.
```

##### ↳ ↳ Re: Did I write a good (efficient) program?

- **From:** Robert <no@e.mail>
- **Date:** 2008-04-01T23:41:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh66v3h1ml3rjf9ic3nbgli94sh1j5fr1i@4ax.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com>`

```
On Wed, 02 Apr 2008 02:54:19 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Frank,
>  As currently included in WD 1.10, I am very much opposed to it.  The problem 
…[11 more quoted lines elided]…
>then I would be for it.

18.16.2.3
3) The INDIRECT phrase specifies that the subject of the entry is an indirect elementary
data item as defined in 8.5.1.7.2, Location of any-length elementary items. If the
INDIRECT phrase is not specified, an any-length elementary item declared at the 01 or 77
level or containing the LIMIT phrase is a direct elementary data item;
otherwise, that data item is an indirect elementary data item.

I read that to say a direct data item in the middle of a record (other than 01/77) must
have a LIMIT. The compiler is expected to allocate LIMIT bytes, similar to ODO, thus
eliminating the need to move everything following when the length changes.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-04-02T05:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O%EIj.28668$du1.1564@fe12.news.easynews.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <gh66v3h1ml3rjf9ic3nbgli94sh1j5fr1i@4ax.com>`

```
It does have a "limit" - but it still needs to "move" the following data.  (Of 
course in Standard COBOL there can't be data following an ODO). "for contiguity" 
of items, see,

"8.5.1.8.1 Contiguity of data items
A variable-length data item may be part of any group structure, and its 
neighbors may be non-variable-length data
items or variable-length data items. A variable-length data item is logically 
but not necessarily physically
contiguous with its neighbors. However a variable-length data item behaves in 
all respects as though it were in fact
contiguous with its neighbors whenever a procedural operation is applied to a 
group containing it."

In other words, no matter how direct items are stored, if you process the "group 
item" containing them, it must "appear" as if the following items are directly 
after the current length - not after the MAXIMUM length.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-04-02T02:37:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tce6v3hriqrje7kcom4petuon9rp0a84bl@4ax.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <gh66v3h1ml3rjf9ic3nbgli94sh1j5fr1i@4ax.com> <O%EIj.28668$du1.1564@fe12.news.easynews.com>`

```
On Wed, 02 Apr 2008 05:41:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>It does have a "limit" - but it still needs to "move" the following data.  (Of 
>course in Standard COBOL there can't be data following an ODO). "for contiguity" 
…[14 more quoted lines elided]…
>after the current length - not after the MAXIMUM length.

The next paragraph seems to confirm that, when it qualifies any-length with indirect. The
implication is that a change to a direct any-length item DOES affect the addresses of its
neighbors. 

"The physical address of a variable-length data item may change during execution of the
program. Dynamic-capacity tables and indirect any-length elementary items, however they
may change during execution, do not in any way affect the addresses of their neighbors."

What procedural operations are they referring to? A MOVE and comparison would work if the
maximum length were allocated and following items not shifted. I can think of two
situations where it matters. FUNCTION LENGTH says nothing about variable-length groups,
which seems like an error.  Reference modification cannot be used on variable-length
groups. 

How can a program tell whether the item following an any-length elementary item is
contiguous? What behavior would be different?

Suppose program A calls B with the address of an indirect any-length item or
variable-length group containing a direct any-length item. B changes the item's size and
address. How does A know the new address? The parameter passed was the address of the item
or group, not the address of its base pointer. If a Cobol program did pass the addess of
the base pointer, which it would almost have to, that would cause problems for other
languages, including the OS API.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-04-02T21:37:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i0TIj.320701$r03.243115@fe10.news.easynews.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <gh66v3h1ml3rjf9ic3nbgli94sh1j5fr1i@4ax.com> <O%EIj.28668$du1.1564@fe12.news.easynews.com> <tce6v3hriqrje7kcom4petuon9rp0a84bl@4ax.com>`

```
The problems with using the "max" rather than the "current" size occurs when 
referencing the entire group item and moving it, for example, to a single 
receiving item.  Having "undefined/garbage" data in the "unused" portion of the 
max part will cause problems.  The GROUP item doesn't know (need to know) how 
the individual sub-items are defined.

Is this clear?  If not, I can try doing an example.

  ***

As far as you example goes, when passing an indirect  variable length item or a 
group containing one, what will be past is a pointer.  If the called program is 
in another language, then you would define the structure with a pointer as what 
was received and need to process it "accordingly".  If the subprogram did 
something that COBOL couldn't handle when it came back, then various "exception 
conditions" might be raised.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-04-02T19:55:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9t88v3148big672ic4d609aekrhauoceqd@4ax.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <gh66v3h1ml3rjf9ic3nbgli94sh1j5fr1i@4ax.com> <O%EIj.28668$du1.1564@fe12.news.easynews.com> <tce6v3hriqrje7kcom4petuon9rp0a84bl@4ax.com> <i0TIj.320701$r03.243115@fe10.news.easynews.com>`

```
On Wed, 02 Apr 2008 21:37:18 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>The problems with using the "max" rather than the "current" size occurs when 
>referencing the entire group item and moving it, for example, to a single 
>receiving item.  Having "undefined/garbage" data in the "unused" portion of the 
>max part will cause problems.  The GROUP item doesn't know (need to know) how 
>the individual sub-items are defined.

I think a group move DOES need to handle any-length items separately. 8.5.1.9 says:

"Unlike other group items, a variable-length group is not equivalent to an alphanumeric
data item and cannot undergo a comparison or a move operation, in either direction,
explicitly or otherwise, unless the other operand is a compatible group. Groups are
compatible if all variable-length data items correspond and match as specified
below. For the purposes of compatibility, either both operands may be variable-length
groups or only one of the operands may be a variable-length group.

Determination of compatibility between a variable-length group and another group is as
follows:
3) For each any-length elementary item in either group there is a corresponding any-length
elementary item in the other group as specified in 8.5.1.9.1, Positional correspondence."


You say, above, a variable length group can be moved to a single receiving item. The last
sentence of the first paragraph says the same. But the first sentence and 3) appear to
require they both be variable-length groups with corresponding any-length items. 

It is easy picture a move from a variable-length group to a fixed-length item, such as a
file record. It is not as easy to picture the reverse. Say it's moving bytes until it gets
to an any-length string defined as prefixed by binary-long. The input doesn't contain a
binary-long. How does it determine the length of the string?

Getting back to a move between two variable-length groups, 
there is no requirement that the corresponding any-length items match on 
       direct/indirect
       prefixed/delimited
       limit

On a group move, the sending group might contain a direct item (with limit) while the
corresponding item in the receiving group is indirect. The sending item might be delimited
by low-value while the receiving group is prefixed by binary-long. 

For these reasons, it seems a grouip move would have to be three operations
    copy the bytes preceding the any-length item
    copy the any-length item, which may require scanning for a delimiter
        or allocating memory
    copy the bytes following the any-length item

>Is this clear?  If not, I can try doing an example.

I would appreciate an example that deals with the above points. 

>  ***
>
…[5 more quoted lines elided]…
>conditions" might be raised.

I found the answer under CALL. Any-length items and variable-length groups are NOT ALLOWED
to be passed as parameters, period. That avoids dealing with the issue of size changing in
the called program. 

The returning item is not allowed to be an any-length item, but can be a variable-length
group containing an any-length item. This is not a mistake, it shows that someone on the
standards committee understands the issues I asked about. If the returning were an
any-length elementary item, the called program would have no way to communicate its new
location after a size change. But when the returning item is a group, the group contains
pointers to its variable-length elements, enabling the called program to pass back their
new locations. 



>
>-- 
…[64 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Did I write a good (efficient) program?

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-04-03T18:31:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47F5226D.6F0F.0085.0@efirstbank.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com>`

```
I'm not talking about how the Cobol standard has them specified.  Just that,
as a feature, I would like some better way to work with variable length
strings.

With regard to DIRECT...  Without actually reading the standard, here is
what I would intuitively *expected* with regard to a direct "any length"
data item (fixed length font required for this to make any sense at all!):

01  AN-01-DATA-AREA.
    05  FIXED-STR-10       PIC X(10).
    05  VARIABLE-STR-10    PIC X ANY LENGTH LIMIT IS 10 DELIMITED BY X'00'.
    05  A-CHAR             PIC X.


MOVE 'XXXXXXXXXX' TO FIXED-STR-10
MOVE 'TEST' TO VARIABLE-STR-10
MOVE 'Z' TO A-CHAR
MOVE 'YYYYYYYYYY' TO VARIABLE-STR-10

Result in memory, before the final MOVE:
XXXXXXXXXXTEST_      Z
^^^^^^^^^^^^^^^^^^^^^^
After the final MOVE:
XXXXXXXXXXYYYYYYYYYY_Z
^^^^^^^^^^^^^^^^^^^^^^
The underscore represents the delimiter 'null' character.

What you say says to me that before the final move we would instead see
XXXXXXXXXXTEST_Z

I would agree that this is rather crazy.

I think how I am looking at it, which is apparently not how you would
support it, is that if DIRECT is specified *along with a limit*, then the
maximum storage required would be used.  This is just like how in C you can
have, for instance:

struct my_struct {
    char[21] field1;
    char[21] field2;
    char x;
};

void cfunc(struct my_struct *s) {
    strcpy(s->field1, "This is a test");
    strcpy(s->field2, "Another test");
    s->x = 'X';
}

Result in memory:
This is a test_      Another test_        X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If I wanted to call cfunc from Cobol I could do this:

01  MY-STRUCT.
    05  field-1    PIC X ANY LENGTH LIMIT IS 20 DELIMITED BY X'00'.
    05  field-2    PIC X ANY LENGTH LIMIT IS 20 DELIMITED BY X'00'.
    05  X          PIC X.


CALL 'cfunc' USING MY-STRUCT
DISPLAY field-1 '/' field-2 '/' x

Result:
This is a test/Another test/X


Now as for a DIRECT any-length data item without a limit specified, I don't
think that makes sense.  Is it even allowed?  My brain doesn't want to try
to interpret the standard right now.

Frank


n 4/1/2008 at 8:54 PM, in message
<vzCIj.8760$fY6.7941@fe11.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
> Frank,
>   As currently included in WD 1.10, I am very much opposed to it.  The 
…[17 more quoted lines elided]…
> then I would be for it.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

- **From:** Robert <no@e.mail>
- **Date:** 2008-04-03T23:38:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v3ebv39km41qelvaflpo6p1k1nolmskunp@4ax.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <47F5226D.6F0F.0085.0@efirstbank.com>`

```
On Thu, 3 Apr 2008 18:31:09 -0600, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
wrote:

>I'm not talking about how the Cobol standard has them specified.  Just that,
>as a feature, I would like some better way to work with variable length
…[26 more quoted lines elided]…
>XXXXXXXXXXTEST_Z

That's what you'd get if you moved the group to a flat string. The standard doesn't say
what memory would look like. It does say the address of a-char will not change if the
any-length string is indirect (is represented by an inline pointer). I take that to mean
the address of a-char MIGHT change if the any-length string is direct. The compiler author
gets to decide whether to shift a-char when its neighbor changes length. 

>I would agree that this is rather crazy.
>
…[33 more quoted lines elided]…
>This is a test/Another test/X

Compatibility with C is a non-issue because .. get this .. you are NOT ALLOWED to pass a
variable length structure as a CALL parameter. 

I seriously doubt any compiler author would enforce that restriction. Then, to be
compatible with C, he would NOT shift X around. 

>Now as for a DIRECT any-length data item without a limit specified, I don't
>think that makes sense.  Is it even allowed?  My brain doesn't want to try
>to interpret the standard right now.

DIRECT items must have a LIMIT except at the 01 level. If you leave it off, they default
to INDIRECT. 


>n 4/1/2008 at 8:54 PM, in message
><vzCIj.8760$fY6.7941@fe11.news.easynews.com>, William M.
…[20 more quoted lines elided]…
>> then I would be for it.
```

###### ↳ ↳ ↳ Re: Did I write a good (efficient) program?

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-04-04T16:49:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47F65C34.6F0F.0085.0@efirstbank.com>`
- **References:** `<47F232DA.6F0F.0085.0@efirstbank.com> <vzCIj.8760$fY6.7941@fe11.news.easynews.com> <47F5226D.6F0F.0085.0@efirstbank.com> <v3ebv39km41qelvaflpo6p1k1nolmskunp@4ax.com>`

```
>>> On 4/3/2008 at 11:38 PM, in message
<v3ebv39km41qelvaflpo6p1k1nolmskunp@4ax.com>, Robert<no@e.mail> wrote:
> On Thu, 3 Apr 2008 18:31:09 -0600, "Frank Swarbrick" 
> <Frank.Swarbrick@efirstbank.com>
…[14 more quoted lines elided]…
>>    05  VARIABLE-STR-10    PIC X ANY LENGTH LIMIT IS 10 DELIMITED BY
X'00'.
>>    05  A-CHAR             PIC X.
>>
…[23 more quoted lines elided]…
> the address of a-char MIGHT change if the any-length string is direct. The

> compiler author
> gets to decide whether to shift a-char when its neighbor changes length. 
…[41 more quoted lines elided]…
> variable length structure as a CALL parameter. 

Wow!  That is lame.  It seems to me one of the benefits to variable length
structures would be passing them between programs/routines, whether written
in Cobol or something else.
 
> I seriously doubt any compiler author would enforce that restriction. 
> Then, to be
> compatible with C, he would NOT shift X around. 

Indeed.
 
>>Now as for a DIRECT any-length data item without a limit specified, I 
> don't
…[6 more quoted lines elided]…
> to INDIRECT. 

Seems to me that even at the 01 level they would have to be INDIRECT if
there was no length limit.
 
Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
