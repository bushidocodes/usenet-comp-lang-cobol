[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-3 binary format

_11 messages · 7 participants · 2001-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COMP-3 binary format

- **From:** "John R" <jr@mpv.com>
- **Date:** 2001-06-29T11:32:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net>`

```
I have COBOL generated file with some COMP-3 fields that I need to convert
to IEEE 754 (Double precision floating point ) format so I can access the
data from Java. Can some one tell me how COMP-3 fields are stored and
possibly how to convert them.

J.R.
```

#### ↳ Re: COMP-3 binary format

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-06-29T10:14:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3CB773.7992@paralynx.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net>`

```
John R wrote:
> 
> I have COBOL generated file with some COMP-3 fields that I need to convert
> to IEEE 754 (Double precision floating point ) format so I can access the
> data from Java. Can some one tell me how COMP-3 fields are stored and
> possibly how to convert them.

COMP-3 is otherwise known as "packed decimal" and squeezes two digits into each byte 
plus it takes half a byte for a sign.

A generic parser like ParseRat (http://www.parserat.com/) can unpack it for you and 
export it as ASCII (CSV etc.) for import into something else if you don't want to write 
the code yourself.
```

##### ↳ ↳ Re: COMP-3 binary format

- **From:** "John H. Lindsay" <eil@kingston.net>
- **Date:** 2001-06-29T14:51:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3CCE45.B247E151@kingston.net>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com>`

```
Hi Folks:

Ed Guy wrote:
> 
> John R wrote:
…[11 more quoted lines elided]…
> something else if you don't want to write the code yourself.
.....

Probably right, but do watch this one.  The meaning of COMP-n 
is strongly machine, OS and compiler dependant, and thus 
changing ANY of the machine, the operating system, and the 
compiler, even in one case the run-time library, may alter 
the meaning of COMP-3.  You'd better state these.  I've seen 
COMP-3 as signed packed decimal, unsigned packed decimal, and 
both bytewise low-endian and high-endian fixed point binary, 
depending on the machine etc.  Without you knowing the details, 
this type of conversion can lead to interesting results.

John.
```

###### ↳ ↳ ↳ Re: COMP-3 binary format

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-06-29T13:38:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3CE75B.200B@paralynx.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com> <3B3CCE45.B247E151@kingston.net>`

```
John H. Lindsay wrote:
> 
> Hi Folks:
…[26 more quoted lines elided]…
> this type of conversion can lead to interesting results.

Absolutely correct, however I think COMP (pure binary) and COMP-3 are pretty much 
standard.  Signed COMP-3 and unsigned COMP-3 usually have the same representation in a 
file, COBOL just ignores the sign nibble if the PIC is unsigned.

"Endianism" can affect all non-DISPLAY number representations.  That's why I put an 
"Endianism" selecting checkbox on the ParseRat binary data selection screen. You can see 
the effect change as you check or uncheck it.  I also display the results of EACH 
of several possible conversions of a field (http://www.guysoftware.com/primgg.jpg) so 
that you see them as you go through a few records and select which one matches the kind 
of data you expect from the fields.

You also have to be aware of data which started as EBCDIC, where a conversion by 
something like Kermit or IND$FILE might have garbled the binary.  For that reason I 
added a function to ParseRat to allow for that too.
```

###### ↳ ↳ ↳ Re: COMP-3 binary format

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-29T19:04:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hj52u$ci8$1@slb2.atl.mindspring.net>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com> <3B3CCE45.B247E151@kingston.net> <3B3CE75B.200B@paralynx.com>`

```
Actually, COMP-3 is the "most common" (but certainly NOT guaranteed) to be
portable of the COMP formats.  I know of none (but there may be some) where
it is not "equivalent" to USAGE PACKED-DECIMAL (in '85 Standard compilers).
Those implementations that I know of that include support for "unsigned"
packed decimal - do it as COMP-6.

COMP on the other hand really DOES vary widely.  Even in the "IBM world"
   OS/390 - it is binary little endian
   OS/400 - it is packed-decimal
   OS/2, WinTel - it is binary big endian (controllable by directive)
   Unix (AIX) - binary little endian

P.S.  I may have the "little/big endians" backwards in the list above, but I
know that the default on OS/390 can be the opposite of the WinTel default.
```

###### ↳ ↳ ↳ Re: COMP-3 binary format

_(reply depth: 5)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-06-29T21:11:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3D515C.3493@paralynx.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com> <3B3CCE45.B247E151@kingston.net> <3B3CE75B.200B@paralynx.com> <9hj52u$ci8$1@slb2.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Actually, COMP-3 is the "most common" (but certainly NOT guaranteed) to be
…[12 more quoted lines elided]…
> know that the default on OS/390 can be the opposite of the WinTel default.

You have, but you'r right - they are opposite.

The WinTel default is  "Little Endian" (within a given word, bytes at lower addresses 
have lower significance - the word is stored "little-end-first"). The PDP-11 and VAX 
families of computers and Intel microprocessors and a lot of communications and 
networking hardware are little-endian. 

Big Endian is the architecture in which, within a given multi-byte numeric 
representation, the most significant byte has the lowest address (the word is stored 
"big-end-first"). Most processors, including the IBM 370 family, the PDP-10, the 
Motorola microprocessor families, and most of the various RISC designs, are big-endian. 

You'll note that DEC is represented on both sides.
```

###### ↳ ↳ ↳ Re: COMP-3 binary format

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-30T14:09:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3d35c9_6@Usenet.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com> <3B3CCE45.B247E151@kingston.net> <3B3CE75B.200B@paralynx.com>`

```

"Ed Guy" <ed_guy@paralynx.com> wrote in message
news:3B3CE75B.200B@paralynx.com...
>
> Absolutely correct, however I think COMP (pure binary) and COMP-3 are
pretty much
> standard.  Signed COMP-3 and unsigned COMP-3 usually have the same
representation in a
> file, COBOL just ignores the sign nibble if the PIC is unsigned.
>
OH NO IT DOESN'T!

Blatant error here, sorry...

On IBM mainframes (for which the packed decimal format was "invented") the
sign is NEVER ignored (by COBOL or anything else).

You should NEVER code UNSIGNED Packed decimal in COBOL on this architecture
because the compiler will generate EXTRA CODE to FORCE the sign to be
positive!

The basic rule with using packed fields in COBOL is:

"ALWAYS define an odd number of digits and a sign."

EXAMPLE:

f1  pic s9(3) comp-3.  (or "PACKED" nowadays).

(occupies 2 bytes, with no additional code to force a sign or zero the first
nibble (may depend on compiler options)

RATHER THAN...

f2 pic 99 comp-3.
(occupies 2 bytes, but has additional 'OR' with x'F' into the low order sign
nibble, and also 'AND's x'F' into the high order nibble in order to clear
it...)

This results in optimum code generation (if you care about that sort of
thing anymore...<G>)

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: COMP-3 binary format

_(reply depth: 5)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-06-29T21:03:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3D4F9F.7C64@paralynx.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <3B3CB773.7992@paralynx.com> <3B3CCE45.B247E151@kingston.net> <3B3CE75B.200B@paralynx.com> <3b3d35c9_6@Usenet.com>`

```
Peter E. C. Dashwood wrote:
> 
> "Ed Guy" <ed_guy@paralynx.com> wrote in message
…[17 more quoted lines elided]…
> positive!

Poor choice of words on my part. You are right. The "ignoring" takes some extra work.

What I should have said was that the external representation is the same, but an 
unsigned PIC behaves as you'd expect unsigned to behave, whatever the "sign" in the 
file.
```

#### ↳ Re: COMP-3 binary format

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-06-29T20:12:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hineq$vvn$1@news.netmar.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net>`

```
In article <3b3cae1a$0$2990$39cecf19@news1.twtelecom.net>, John R
<jr@mpv.com> writes:
>I have COBOL generated file with some COMP-3 fields that I need to convert
>to IEEE 754 (Double precision floating point ) format so I can access the
…[5 more quoted lines elided]…
>
Why don't you just create a new file with unpacked fields with a Cobol Program
 Some report generators will make a simple download file you can use also. 
It might be possible to make a very small assembly program that could unpack
one field at a time and you could just call that each time you get to the
field instead of rewriting the entire file.  You could also do the same thing
with a callable Cobol program that just accepts one number unpacks it and
returns a second field.  All cobol does to unpack a field is move it from one
field to another one, or use a compute statement computer FLDP = FLD9.  

I wander if one of the OO cobol compilers has an API that can do that for
you?


 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

##### ↳ ↳ Re: COMP-3 binary format

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-29T21:20:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3CF0DD.25254B5B@home.com>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <9hineq$vvn$1@news.netmar.com>`

```


chammond@lc.cc.il.us wrote:

> I wander if one of the OO cobol compilers has an API that can do that for
> you?

Surely that should be, "I wonder if Windows has an API to do it....". I doubt it.
If it has then you don't need OO to do it, just call the API from the appropriate
language.

Not intentional I know - but your question implies OO is used solely for windowing.

Jimmy


>
>  -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
>   http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
>    NewsOne.Net prohibits users from posting spam.  If this or other posts
> made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

##### ↳ ↳ Re: COMP-3 binary format

- **From:** "John R" <jr@mpv.com>
- **Date:** 2001-06-29T16:27:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3cf31a$0$2993$39cecf19@news1.twtelecom.net>`
- **References:** `<3b3cae1a$0$2990$39cecf19@news1.twtelecom.net> <9hineq$vvn$1@news.netmar.com>`

```
Thanks for all the information and prompt responce. I found out that the
fields I was trying to convert are bigendian 2's complement COMP. I ended up
writing the following small Java method to convert the raw data to and
object:

 public BigDecimal compToDecimal(byte[] buf, int scale)
 {
  return new BigDecimal(new BigInteger(buf), scale);
 }
and it seems to work fine on my data.

Thanks again!
J.R.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
