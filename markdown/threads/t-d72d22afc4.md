[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Negative numbers in Cobol picture

_12 messages · 11 participants · 1997-07_

---

### Negative numbers in Cobol picture

- **From:** "newman" <ua-author-101267@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

A system we are developing for the PC needs to export data in a format
specified by our bank. All the fields have a cobol picture to tell us
how to store the information.

Most of the fields we are OK with - but we have one problem.

One of the fields has PIC S9(11)V99, and it is supposed to hold a
negative number.

A positive number (eg +1234.56) should look like this:
0000000123456

What would a negative number look like? Does it have a hyphen '-' in
it, at the beginning or end of the number? Someone mentioned something
about coding the negative sign into the last digit (eg 6C in hex).

Any help would be appreciated - as well as any pointers to cobol picture
information on the internet.

Regards,
Kevin Newman
Medwise (Pty) Ltd
kne··.@ico··o.za
+27 82 920 4401
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "patrick henry" <ua-author-13505@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

Newman wrote:
› 
› A system we are developing for the PC needs to export data in a format
…[22 more quoted lines elided]…
› +27 82 920 4401

You can specify the sign as a separate character, either leading or
trailing, if you need the sign to be separate. However, as defined in
your post, the sign is superimposed over the last digit.
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

.Newman wrote:
.>
.> A system we are developing for the PC needs to export data in a
format
.> specified by our bank. All the fields have a cobol picture to tell us
.> how to store the information.
.>
.> Most of the fields we are OK with - but we have one problem.
.>
.> One of the fields has PIC S9(11)V99, and it is supposed to hold a
.> negative number.
.>
.> A positive number (eg +1234.56) should look like this:
.> 0000000123456
.>
.> What would a negative number look like? Does it have a hyphen '-' in
.> it, at the beginning or end of the number? Someone mentioned
something
.> about coding the negative sign into the last digit (eg 6C in hex).
.>
.> Any help would be appreciated - as well as any pointers to cobol
.picture
.> information on the internet.
.>
.> Regards,
.> Kevin Newman
.> Medwise (Pty) Ltd
.> kne··.@ico··o.za
.> +27 82 920 4401



The sign is totally Cobol compiler vendor-independent. If your compiler
supports some sort of process (compiler switch, etc.) that may solve
your problem. If not, you will have to translate the sign from within
your program for the target platform. Since it's signed, you should
account for positive signs as well as negative signs.

For example, the negative value -123456 in CA-Realia Cobol is generated
as 12345&. If your target platform is an IBM mainframe after
translation, the value would be converted to 12345O. Note that the last
character is an alpha "O", not zero. This example also assumes you are
using the compilers "sign is separate", which in my experience is the
most widly used sign convention and the default on the IBM mainframe
Cobol compiler.

Mike Dodas
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

On 12 Jul 1997 19:52:14 GMT, "Newman" wrote:

› A system we are developing for the PC needs to export data in a format
› specified by our bank. All the fields have a cobol picture to tell us
…[21 more quoted lines elided]…
› +27 82 920 4401

I'm missing something here. sounds like the answer requires knowledge
of the hardware. the author documents what the positive number looks
like, then indicates the hex value may be different. If the author
will confirm the hex value of a positive vaule, the negative value
will come easy. I'm suspicious about the statement about a positive
number.

David d.s··.@ix.··m.com
____________________________________
```

##### ↳ ↳ Re: Negative numbers in Cobol picture

- **From:** "lee" <ua-author-15794@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d72d22afc4-p4@usenetarchives.gap>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za> <gap-d72d22afc4-p4@usenetarchives.gap>`

```

David wrote:
› 
› On 12 Jul 1997 19:52:14 GMT, "Newman"  wrote:
…[34 more quoted lines elided]…
› ____________________________________

The field you described, PIC S9(11)V99 allows for printing a positive or
negative number using editing symbols. If you wanted the field to print
a leading minus symbol you would define the PIC for your output report
as PIC -9(11)V99. If you want it to print as a trailing symbol you
would code your output PIC as PIC 9(11)V99-. A positive amount would
not print a sign. If you want to print a sign for both positive and
negative amounts, use the + editing symbol instead of -.

Lee (l.··.@s··.net)
```

##### ↳ ↳ Re: Negative numbers in Cobol picture

- **From:** "barry steinholtz" <ua-author-789746@usenetarchives.gap>
- **Date:** 1997-07-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d72d22afc4-p4@usenetarchives.gap>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za> <gap-d72d22afc4-p4@usenetarchives.gap>`

```

Hi:

What has to be understood is the fact that you maybe trying to send
the PC, which is ASCII, to a mainframe that could be EBCDIC. These are
different codes and they do have a habbit of changing negative numbers
to positive or something else. The best way to handle the problem is
have the sign as a field by itself. Then by changing some logic you can
then treat the field properly. Another way would be to run the uploaded
file through an inhouse utility that will format the PC file into the
proper format after the upload.

Barry Steinholtz - mailto:Bst··.@Mic··e.Net
MicroFone InfoServices/Metuchen NJ USA
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "newman" <ua-author-101267@usenetarchives.gap>
- **Date:** 1997-07-12T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p7@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

Thanks to all who replied to my previous posting.

Perhaps I should try and explain myself a bit more clearly this time... :)

1. I am not a Cobol programmer, and the system we are developing is
not being developed with Cobol: that's why I'm having difficulty.
2. Our system needs to export a data file to our local IBM/Intel PC. The
file then gets sent to the bank's mainframe for processing.
3. The fields in the data file have a Cobol picture to explain to us how
we must store the information.
4. The data file uses 8 bit ASCII character representation on our side.
5. All currency fields are defined as PIC S9(11)V99. Example files from
the bank tell us that a number (eg 1234.56) would be represented as:
0000000123456
The hexadecimal values for this field in the file would be
30 30 30 30 30 30 30 31 32 33 34 35 36

In other words there are 13 bytes written to the file, and, for example,
'6' is stored as the ASCII value 36 (hex).

We are the only customer of the bank doing *payments* instead of
purchases using these data file transfers, so we need to be able to use
negative numbers, but we do not have any example files to help us.

As far as I can tell from kind replies etc., is that numbers in Cobol
are represented *internally* by the compiler in a certain packed-byte
format, which differs from platform to platform. It seems to me that
we are not using this packed format because our PC obviously uses
a much different data storage format than the mainframe.

Therefore, I think that the pictures tell us how the numbers would look
in a report, etc. So perhaps my question should be:
How would a Cobol program format a negative number if it was given
PIC S9(11)V99 as the picture.

Once again, thanks to anyone who can help me out.

Regards,
Kevin Newman
Medwise (Pty) Ltd
kne··.@ico··o.za
+27 82 920 4401
```

##### ↳ ↳ Re: Negative numbers in Cobol picture

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-07-13T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d72d22afc4-p7@usenetarchives.gap>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za> <gap-d72d22afc4-p7@usenetarchives.gap>`

```

Newman wrote:
› 
› Thanks to all who replied to my previous posting.
…[7 more quoted lines elided]…
›    file then gets sent to the bank's mainframe for processing.
--snip--
Kevin,
Based on your 2nd statement, it seems pretty clear what your
requirements are.
Your bank is apparently looking for what is known as a 'zoned decimal',
although there are other names for it (flamers back off!).
Let's take a shorter example, say PIC S9(4). On the mainframe, the value
+1234 would be stored in hex as "F1F2F3C4", and -1234 would be
"F1F2F3D4". The high-order nibble of the last byte signifies positive
("C" or "F") or negative ("D").
Unfortunately, since you're data is in ASCII format, you need to take
into consideration how the data is going to be translated (by you or
them?) before the bank 'imports' it. An ASCII "32" will no doubt
translate to an EBCDIC "F2", but what would translate to a "D2"?!
Hope this helps.
Cheers :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*          United Retail Group, Inc.          *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-07-12T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p9@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

What you're hunting for is an over-punch in the last position. Not too
difficult, >>IF<< the language you're working in can handle either hex or
decimal characters directly >>AND<< you're going from ASCII to ASCII (e.g.,
PC to a VAX).

Just be happy the bank isn't requesting packed decimal... LOL!

Basically, what you've gotta do is include the sign and the value of the last
digit in the same byte. The hex values you want are C for positive (or zero,
since zero is usually considered positive), and D for negative. So +123.45
becomes 1234¥ (or X'313233345C') and -543.26 becomes 5432m (or X'353433326D').
Remember that +2.50 becomes X'32350C' and -17.40 becomes X'3137340D', while
0.00 is always X'30300C' (zero is usually considered positive!). When the COBOL
program at the other end interprets the "¥" and "m" characters (or form-feed
and carriage-return characters!) as part of the picture string, it'll
automatically 'know' to split the last byte into the two zones: value|sign. Of
course, you'll have to right justify and zero fill (so +123.45 is sent as
"000000001234¥", etc.).

If you're going from a PC to an AS/400 or other EBCDIC based machine, however,
you're gonna have to bypass any ASCII/EBCDIC translators, and do your own,
selective translating by mapping the two character sets in an array and base
your output on what's in there. For example: X'0C' and X'0D' (form-feed and
carriage-return) are the same in both character sets, so that would be no
problem, but X'2C' and X'2D' are comma and hyphen in ASCII, which are X'6B' and
X'60' in EBCDIC. Unfortunately X'6B' is the character "k", which the standard
ASCII/EBCDIC translator will turn into a X'92' at the IBM end, driving you
deeper and deeper into a hole. This is the reason why most places simply won't
transfer anything other than plain string type data between an ASCII and EBCDIC
environment. So, if you want to transfer +123.45, -543.26, +2.50, -17.40, and
0.00 from the ASCII based PC to an EBCDIC based machine, where the picture
string is S9(11)V99, then send X'F1F2F3F45C', X'F5F4F3F26D', X'F2F50C',
X'F1F7F40D', and X'F0F00C' respectively. Again, of course, right justify and
zero fill the data field (so -543.26 becomes X'FOFOFOFOFOFOFOFOF5F4F3F26D').

In Visual BASIC, I'd first build my number (positive or negative), then use the
Format$() function get a string interpretation, and then, for each character in
the resulting string, use the Asc() function to obtain the decimal value,
translate this into its EBCDIC equivalent, and then use the Chr$() function to
build the EBCDIC value, taking care to mesh the value and sign when I reached
the final digit.

Hope this helps! :D
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "10025..." <ua-author-17071258@usenetarchives.gap>
- **Date:** 1997-07-13T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p10@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

I am very surprised that the bank has not specified precisely
what is required. From what you said, an "overpunch" is
required, which could be either leading or trailing. This is
most surprising. The "shifted" digits are different for
different implementations. For example, under VME, which runs on
an EBCDIC mainframe, they are mainly uppercase letters near the
beginning of the alphabet. Using Microfocus Cobol on a Unix box
using ASCII, they are mostly lower case letters near the end of
the alphabet.

Using PIC S9(11)V9(2) USAGE DISPLAY, SIGN IS [LEADING|TRAILING]
OVERPUNCH will produce a result, but you need to ask your bank,
or to check the documentation more carefully, to find out exactly
what the bank expects, as well as experimenting to find out the
results of using, for example, the above data definition.

The worst case scenario is that you will have to map the final
byte under a function (in the mathematical sense). I did this
with a subroutine which employed the TRANSLATE verb. If you are
not using Cobol, you might be able to do the task manually
simnply by adding a constant to the first, or the last byte,
depending upon the bank's expectations, whenever the value is
negative.

I hope this helps.
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "lindy mayfield" <ua-author-13980060@usenetarchives.gap>
- **Date:** 1997-07-13T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p11@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

I read through some the answers given to you, but I didn't feel like your question was answered correctly.

The easy answer is to simply add the negative sign (-) to the front or the back and make the Cobol picture
match it. Note this Cobol example:

01 NUMBER-TESTS.
05 NUM-A PIC S9(11)V99.
05 DIS-A PIC -9(11).99.
05 DIS-B PIC 9(11).99-.

Now if the number you are reading is -1234567.89 it will need to be stored as follows on an IBM Mainframe:
NUM-A = 000012345678R (example of what your example looks like stored internally in EBCDIC)
(hex) FFFFFFFFFFFFD
0000123456789

DIS-A = -00001234456.89 (this or the following is what your PC program would write out)

DIS-B = 00001234567.89-

Note that the display versions need two extra bytes for the negative sign and decimal point. Also note that if
the numbers are positive you will need to put a space where the - sign is, either at the beginning or at the
end depending of course where the sign is in the picture clause. (Space is X'40' in hex)

As others pointed out, if you are going through a conversion from ASCII to EBCDIC you need to stick with
display characters, 1-9, +, -, A-Z, etc. It's easier than converting on the PC side when writing the file.

Also note that in EBCDIC the numbers are stored in hex as F1, F2, F3, etc. for 1, 2, 3, but with a D or C over
instead of F when the number is signed. The D and C (probably) stand for Debit and Credit. D is for negative,
C for positive. That's why the number in the NUM-A example came out as the letter R. D9 is hex for the letter
R in EBCDIC.

Hope this helps.
Lindy
li··.@con··x.com


Newman wrote:
› 
› A system we are developing for the PC needs to export data in a format
…[22 more quoted lines elided]…
› +27 82 920 4401
```

#### ↳ Re: Negative numbers in Cobol picture

- **From:** "john hofstad-parkhill" <ua-author-6589075@usenetarchives.gap>
- **Date:** 1997-07-20T02:09:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d72d22afc4-p12@usenetarchives.gap>`
- **In-Reply-To:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`
- **References:** `<022cac76$29ede660$20df1ac4@pnewman.icon.co.za>`

```

› A positive number (eg +1234.56) should look like this:
› 0000000123456

The MF implementation I use (albeit old) goes as does the mainframe. Signed
display decimal numbers encode the sign in the high-order 4-bits (nybble)
of the low order byte, and the signs are consistant with the mainframe
(S/370) where x'c0' is positive, and x'd0' is negative.

This -1234.56
000000012345x (x is not a printable ascii character)
30 30 30 30 30 30 30 31 32 33 34 35 D6

In ascii, in ebcdic

F0 F0 F0 F0 F0 F0 F0 F1 F2 F3 F4 F5 D6

As noted, an ascii to ebcdic translation may not handle X'D6' correctly,
however it's not difficult to translate to EBCDIC by yourself.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
