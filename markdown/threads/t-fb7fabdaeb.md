[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# No accented characters in COBOL? (Newbie Q)

_8 messages · 6 participants · 1998-12 → 1999-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### No accented characters in COBOL? (Newbie Q)

- **From:** textuur@my-dejanews.com
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76d5vj$irf$1@nnrp1.dejanews.com>`

```
I am new to COBOL and have downloaded Fujitsu COBOL 3.0.
One of the things I notice is that COBOL (at least this
version) doesn't seem to support accented characters.
I checked the manuals but couldn't find pertinent information,
just a 7 bit ASCII-table.

Can somebody give some info please, or a pointer? Thank you.

Karel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: No accented characters in COBOL? (Newbie Q)

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368A7B18.5B35A1F5@IMN.nl>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com>`

```
textuur@my-dejanews.com wrote:

> I am new to COBOL and have downloaded Fujitsu COBOL 3.0.
> One of the things I notice is that COBOL (at least this
> version) doesn't seem to support accented characters.

Not in the RESERVED words of the language, nor in the programmer-defined
names (variable, procedures). But in alphnumeric variables and literal
strings the whole bunch of characters from ASCII, EBCDIC or whatever
char.set you're working with is available.

Read more about this in your COBOL manual. The following is an extract from
Micro Focus docs:

[start]
The most basic and indivisible unit of the language is the character. The
set of characters used to form COBOL character strings and separators
includes the letters of the alphabet, digits and special characters, and is
defined below:

Character Meaning
0 to 9 Digits
A to Z Uppercase letters
a to z Lowercase letters
Space
+ Plus sign
ï¿½ Minus sign or hyphen
* Asterisk
/ Oblique stroke/slash
= Equal sign
$ Dollar sign
. Period or decimal point
, Comma or decimal point
; Semicolon
" Quotation mark
( Left parenthesis
) Right parenthesis
> Greater Than symbol
< Less Than symbol
: Colon
Lowercase letters can be used in character strings and text words; except
when used in nonnumeric literals and except for some picture symbols, each
lowercase letter is equivalent to the corresponding uppercase letter.
This COBOL implementation is restricted to the above character set, but the
content of nonnumeric literals, comment lines, comment entries and data can
include any of the characters available under the character encoding scheme
used for the COBOL source program.
[end]

The Frog

> I checked the manuals but couldn't find pertinent information,
> just a 7 bit ASCII-table.
…[6 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: No accented characters in COBOL? (Newbie Q)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76gudq$cdf@dfw-ixnews10.ix.netcom.com>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com> <368A7B18.5B35A1F5@IMN.nl>`

```
FYI,
  Some implementations (including MF) allow "extended characters" as part of
user-defined words - if the correct directives are set.  Furthermore, this
will be allowed as a part of the next Standard - but there are a bunch of
things needed to figure out what characters are allowed and what characters
are considered upper-/lower-case equivalents.

Check your current compiler's manual under (probably) "national character"
support (or possibly under "DBCS" or "MOCS") for further information on
this.

COBOL Frog (Huib Klink) wrote in message <368A7B18.5B35A1F5@IMN.nl>...
>textuur@my-dejanews.com wrote:
>
…[74 more quoted lines elided]…
>
```

#### ↳ Yes, they are there, but (Re: No accented characters in COBOL?)

- **From:** textuur@my-dejanews.com
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76gcki$1cg$1@nnrp1.dejanews.com>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com>`

```
In article <76d5vj$irf$1@nnrp1.dejanews.com>,
  I wrote:
> I am new to COBOL and have downloaded Fujitsu COBOL 3.0.
> One of the things I notice is that COBOL (at least this
…[6 more quoted lines elided]…
> Karel

And the only reason I didn't find them was the interface of
Fujitsu (the accented character only becomes visible when
you press another key, then both appear). And I did not know
I was supposed to look under 'computer character set'  B-)

Now if only an indexed file would sort these characters right.
No, not in extended ASCII sequence. Help is appreciated.

Karel
```

##### ↳ ↳ Re: Yes, they are there, but (Re: No accented characters in COBOL?)

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76hbo1$r1g$1@server.cntfl.com>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com> <76gcki$1cg$1@nnrp1.dejanews.com>`

```

textuur@my-dejanews.com wrote in message
<76gcki$1cg$1@nnrp1.dejanews.com>...
[...]
>
>Now if only an indexed file would sort these characters right.
>No, not in extended ASCII sequence. Help is appreciated.
>
If you do not mind scrambling the index key, you can cause the
records to be arranged in any order you choose.

Consider the following:

       01 native-order pic x(52) value
           "ABCDEFGHIJKLMNOPQRSTUVWXYZ" &
           "abcdefghijklmnopqrstuvwxyz".
       01 lexical-order pic x(52) value
           "ACEGIKMOQSUWYacegikmoqsuwy" &
           "BDFHJLNPRTVXZbdfhjlnprtvxz".
       01 ascending-digit pic x(10) value "0123456789".
       01 descending-digit pic x(10) value "9876543210".

If, before writing the index record, I do:

            inspect key-name
                converting native-order to lexical-order.

The values in the key will be ordered as: AaBb ... Zz.

After reading the record, I do:

            inspect key-name
                converting lexical-order to native-order.

The key will again be returned to its correct representation.

It is a matter of setting the correct values into the native and lexical
orders. Characters that are unchanged in their order need not be
represented. Note that the example would allow the ASCII characters
between 'Z' and 'a' to be sorted into their normal order. This would
cause those character to appear between the letters 'm" and "N".

Ordering an index for descending numeric values is another
interesting use of key scrambling; but is left, as an exercise,
to the reader.

HTH
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Yes, they are there, but (Re: No accented characters in COBOL?)

- **From:** cpcohen@inforamp.net (Charles P. Cohen)
- **Date:** 1999-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368e457a.4550052@news.istar.ca>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com> <76gcki$1cg$1@nnrp1.dejanews.com> <76hbo1$r1g$1@server.cntfl.com>`

```
"Rick Smith" <ricksmith@aiservices.com> wrote:

>If you do not mind scrambling the index key, you can cause the
>records to be arranged in any order you choose.

What you suggest is a neat trick.  

But it doesn't work  well for the situation in which two different
characters (say, "a" and "accented a", or Finnish "v" and "w") have
the _same collating order_, or where a _pair_ of characters collates
the same as a single character (I believe this occurs with "i" and
"ij" in Dutch).

The "general case" needs a record key, and a sort key -- related but
different fields.
```

###### ↳ ↳ ↳ Re: Yes, they are there, but (Re: No accented characters in COBOL?)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76on7q$t2p@sjx-ixn3.ix.netcom.com>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com> <76gcki$1cg$1@nnrp1.dejanews.com> <76hbo1$r1g$1@server.cntfl.com> <368e457a.4550052@news.istar.ca>`

```

Charles P. Cohen wrote in message <368e457a.4550052@news.istar.ca>...
>"Rick Smith" <ricksmith@aiservices.com> wrote:
>
…[12 more quoted lines elided]…
>different fields.

Please do check with your specific vendor.  I know that Micro Focus has had
NLS (National Language Support) for years (not to be confused  - in this
case - with National Character Support - i.e. DBCS/MOCS).  It does include
(as I recall) support for all the "extended" Western European Character
sets.  (Again, vague memory is that it supported both indexed keys and
collating sequences - or a combination of the two.  However, this is only a
vague memory.)

Obviously, full support will come with the next Standard and any ISO-10646
supporting system.
```

##### ↳ ↳ Re: Yes, they are there, but (Re: No accented characters in COBOL?)

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-RnLxTfBxgRdd@Dwight_Miller.iix.com>`
- **References:** `<76d5vj$irf$1@nnrp1.dejanews.com> <76gcki$1cg$1@nnrp1.dejanews.com>`

```
On Thu, 31 Dec 1998 17:35:14, textuur@my-dejanews.com wrote:

> Now if only an indexed file would sort these characters right.
> No, not in extended ASCII sequence. Help is appreciated.
> 

I hear rumors of an NFS version of Fujitsu in the works that might 
just do that!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
