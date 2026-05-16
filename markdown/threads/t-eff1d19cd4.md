[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Another correction to my posts on index data items

_2 messages · 2 participants · 2003-02 → 2003-03_

---

### Another correction to my posts on index data items

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-28T12:22:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3oge8$2vqm$1@si05.rsvl.unisys.com>`

```
Robert Wagner requested in another thread that I reexamine the behavior of
index data items when the values contained in them are retrieved into
different indices from those that served as the most recent source.

In the process of developing a response (see below), I find that I was
mistaken in my expectation that the contents of an index data item could be
presumed to represent directly the ordinal position to which the source
index to which it was SET originally pointed.  That presumption is not
warranted by the standard (any of them).    When a numeric data item is set
to an index item, yes, the conversion from "implementor defined format" to
"occurrence number format" is indeed required.  Not when an index data item
is set to an index-name; the value is transferred intact.

For SET index-name TO index-data-item, as an example, ANSI X3.23-1974
indicates (on Page III-12 under 3.4, THE SET STATEMENT, General Rule 3a)
that index-name is set to the contents of index-data-item with no conversion
at all.   The contents of an index-data-item are meaningful ONLY in the
context of the index-name to which they were last SET, and the association
of an index data item with a given index-name (and thus a given table) thus
BOTH end up being the user's responsibility, not the compiler's, not the
implementor's.

While an implementation MAY treat the contents of an index -- and also that
of an index data item -- as a subscript rather than an offset, there is no
standard requirement that it do so.   While an implementation MAY provide
that an index data item is the same FORMAT as an index-name, there is no
standard requirement that it do so.  Unisys MCP/AS COBOL compilers do
neither.

In the Unisys MCP/AS implementations, the contents of an index are always an
offset -- in COBOL74 from the beginning of the record, in COBOL85 from the
beginning of the table.  There is no value conversion when an index data
item is SET to an index-name.  There is likewise no value conversion when an
index-name is SET to an index data item.  This makes for a fairly rapid SET
in either direction, but it means that if an index data item is used to SET
an index-name that's different from the one from which it was SET in the
first place, the results may be meaningless.  That is permitted by the
standard.

Given Robert's declarations (upcased and double-quoted for compatibility
with COBOL74):
 01  UNQUALIFIED-VARIABLES.
     05  INDEX-DATA-NAME         INDEX.
     05  TABLE-1 VALUE "123".
         10  TABLE-ENTRY OCCURS 3 INDEXED INDEX-NAME-1 PIC X(01).
     05  TABLE-2 VALUE "1 2 3".
         10  TABLE-ENTRY OCCURS 3 INDEXED INDEX-NAME-2 PIC X(02).

and the following code:
    SET INDEX-NAME-1 TO 3.
    SET INDEX-DATA-NAME TO INDEX-NAME-2.
    SET INDEX-NAME-2 TO INDEX-DATA-NAME.
    DISPLAY TABLE-ENTRY OF TABLE-2 (INDEX-NAME-2).

For COBOL74:  Both indices, and the index data item, all contain 6.  Since
COBOL74 doesn't do bounds checking for indices at all, the value displayed
is "31".  If COBOL74 did do bounds checking on indices, I would expect a
range error here.

If  the COBOL74 program were revised to put TABLE-2 in a different 01-level
record so that TABLE-1 terminated the 01-level record, I would expect some
sort of execution-time memory-protection failure might occur here.

For COBOL85:  Both indices, and the index data item, all contain 2.  No
boundary issues present themselves with that value, so the value displayed
is "2 ".

*As I recall it*, the original complaint was that *indexing* is unreliable
and unpredictable and best avoided.  I don't think that's true.  But index
data items -- as distinct from index-names -- must be used with great care,
and indexing can be used very successfully in a wide variety of environments
and constructs without EVER declaring a USAGE INDEX data item.  .

As a side note, the memory allocation and format methodology used on Unisys
MCP/AS COBOL compilers has been standardized for intra-system file
compatibility for many, many years for all Burroughs architectures as
PICTURE S9(7) PACKED-DECIMAL SIGN LEADING.  While that was great on the
native-decimal-equipped Burroughs Small Systems and Medium Systems, on the
Large Systems architecture and its successors it is somewhat less efficient
than a "native" integer format would be.  The fact that no "value"
conversion (subtract the offset, divide by the stride to come up with an
occurrence number) is even allowed, much less required, when an index-name
is stored into it offsets at least some part of the conversion costs to and
from the word-integer format of the index itself.   As index-names aren't
data items that occupy user-visible space in the program's memory, their
format is entirely up to the implementor and presents no portability issues.

    -Chuck Stevens
```

#### ↳ Re: Another correction to my posts on index data items

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T00:28:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5ffec6.183460108@news.optonline.net>`
- **References:** `<b3oge8$2vqm$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>In the process of developing a response (see below), I find that I was
>mistaken in my expectation that the contents of an index data item could be
…[5 more quoted lines elided]…
>is set to an index-name; the value is transferred intact.

Thank you for the graceful retraction. I admire your posts for their mannerly
demeanor, lack of ego and attempting to provide helpful information, unlike 'you
know who'. 

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
