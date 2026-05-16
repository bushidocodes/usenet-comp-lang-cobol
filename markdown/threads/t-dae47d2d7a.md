[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data records....

_5 messages · 5 participants · 1999-11_

---

### Data records....

- **From:** morella3253@my-deja.com
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81ejd0$6om$1@nnrp1.deja.com>`

```
Hi to all,

A few questions that have left me puzzled:

1) I have a record which has a filler PIC X(21) around the center
   of the record. I am now going to use 6 of those characters to
   hold a number (PIC 9(6)). All new records will have the 6 characters
   set to 000000 - 999999. What happens when I read an old record that
   has spaces (ie. part of PIC X(21)). Will i have to handle this in
   the program or can I do a CONVERT (OPENVMS) to pad or fill the
   6 characters with 000000?

2)  I have a field that is PIC 9(6) COMP-3, and its contents are
    NL but in one column (i.e. the N is above the L). What is this
    and what would happen if I read this field into PIC X(6)?

3) I have a record that is 256 characters and is made up of fields
   characters, comps, etc...
   Why is it that some records are longer than others, does 256 mean
   that if I counted 256 columns along the record, this should give me
   the end of the record? The FDL says that the record is 256
   characters and it is a fixed length record.

Thanks in advance for any help

Morella Hernandez


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Data records....

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81erap$g0a$1@news.inet.tele.dk>`
- **References:** `<81ejd0$6om$1@nnrp1.deja.com>`

```
1. Convert the data (If Blah-Blah not numeric move zeroes to Blah-Blah
End-if)
When you convert all records, you can be sure that the records match the
definition and you can avoid a data exception.

2. a comp-3 field is packed numeric data. Your 9(6) takes 4 bytes (2 digits
in every byte except the last byte. It contains 1 digit and 1 sign (C og
D)). +125 would look like this:
1st byte x'00'
2nd byte x'00'
3rd byte x'12'
4th byte x'5C'

If you count, you can see, that pic 9(7) would also take 4 byte. In fact, I
always define Comp-3 fields as an odd number of digits. You can easily move
a comp-3 field to a pic x field, but I cannot see why, except if you want to
display the contents. If so, move the com-3 field to a pic S9 (7) first.

3 A fixed length 256 record is 256 bytes long.

Regards
Ib
morella3253@my-deja.com skrev i meddelelsen <81ejd0$6om$1@nnrp1.deja.com>...
>Hi to all,
>
…[27 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Data records....

- **From:** johnw@stones.com (John Whistler)
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B460DEE0966860A7C9@relay06-b.indigo.ie>`
- **References:** `<81ejd0$6om$1@nnrp1.deja.com> <81erap$g0a$1@news.inet.tele.dk>`

```
In article <81erap$g0a$1@news.inet.tele.dk>,
"Ib Tanding" <ib@tanding.dk> wrote:

>morella3253@my-deja.com wrote
>>Hi to all,
…[49 more quoted lines elided]…
>

1) The VMS Convert command will not alter the contents of a record, it can
only alter the type of file (sequential to indexed, variable to fixed etc.)
You will need to write a program to replace the spaces with zeros.

2) I assume you're looking at the data using the editor. This displays the
control characters corresponding to the binary value of a byte. The "NL"
means that the byte contains x'00' which, as Ib explains above, is
perfectly valid for a comp-3 field.

3) Again, I assume you're using the editor. If a comp or comp-3 field
contains x'09', the editor reads this as a tab character and moves the
cursor to the next tab stop. The only way to see exactly what is in your
data is to use the VMS 'dump' command. try 'dump/record' which will dump
records rather than disk blocks. 'help dump' will explain the format of the
output.

Regards,

John.
```

#### ↳ Re: Data records....

- **From:** Michiel Erens <I.dont.want.spam@my.address.in.NL>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383B14E8.45CC@my.address.in.NL>`
- **References:** `<81ejd0$6om$1@nnrp1.deja.com>`

```
morella3253@my-deja.com wrote:
> 
> Hi to all,
…[9 more quoted lines elided]…
>    6 characters with 000000?

I don't believe Convert can do it. You don't want to extend the record,
but just fill it on a certain place. I would write a small program that
sequentially reads all the records and puts zeroes in the field. 

> 2)  I have a field that is PIC 9(6) COMP-3, and its contents are
>     NL but in one column (i.e. the N is above the L). What is this
>     and what would happen if I read this field into PIC X(6)?

Which utilily do you use to view the file ? 
 
> 3) I have a record that is 256 characters and is made up of fields
>    characters, comps, etc...
…[3 more quoted lines elided]…
>    characters and it is a fixed length record.

Again, which utilily do you use to view the file ? I guess the editor ?
Use the DUMP command to view the contents in decimal and hex notation. 
With DUMP /RECORD you can see the seperate records and their contents. 
With DUMP /RECORD=(START:5,COUNT:12) you'll see 12 records, starting
with 
number 5.
```

#### ↳ Re: Data records....

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383B8B39.2289FF12@att.net>`
- **References:** `<81ejd0$6om$1@nnrp1.deja.com>`

```
morella3253@my-deja.com wrote:
> 
> Hi to all,
> 
(snip)
> 
> 3) I have a record that is 256 characters and is made up of fields
…[4 more quoted lines elided]…
>    characters and it is a fixed length record.

This one rang a bell - are you by any chance passing data from an IBM
mainframe to a UNIX box? UNIX (Solaris, anyway) doesn't do
packed-decimal (COMP-3) and the printouts make the mainframe data look
longer than it is. (I'm obviously a mainframed, sorry for any errors
concerning UNIX)

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
