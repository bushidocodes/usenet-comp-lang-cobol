[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-3 conversion to C integer

_6 messages · 6 participants · 1997-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COMP-3 conversion to C integer

- **From:** "didier" <ua-author-812834@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3460FAD6.CC982B23@club-internet.fr>`

```

how to convert COBOL COMP-3 datatypes to C integer type ?
Does it exist a standard routine ?
Thanks
```

#### ↳ Re: COMP-3 conversion to C integer

- **From:** "j. funk" <ua-author-13468618@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ab2a447bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3460FAD6.CC982B23@club-internet.fr>`
- **References:** `<3460FAD6.CC982B23@club-internet.fr>`

```



Didier wrote in article
<346··.@clu··t.fr>...
› how to convert COBOL COMP-3 datatypes to C integer type ?
› Does it exist a standard routine ?
› Thanks
›
›

It would help to know more about the environment in which you are working,
and more about why you need to convert.

In the meantime, making certain assumptions, what about something like:

01 SAMPLE-32-BIT-INT PIC S9(9) COMP.
01 SAMPLE-COMP-3-FIELD PIC S9(7) COMP.



MOVE SAMPLE-COMP-3-FIELD TO SAMPLE-32-BIT-INT.
```

#### ↳ Re: COMP-3 conversion to C integer

- **From:** "gro..." <ua-author-17072356@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ab2a447bd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3460FAD6.CC982B23@club-internet.fr>`
- **References:** `<3460FAD6.CC982B23@club-internet.fr>`

```

ON PC:
MOVE VAR-COMP-3 TO VAR-COMP-5

VAR-COMP-5 is compatible with C int (big endian vs low endian)

In article <346··.@clu··t.fr>, dfr··.@clu··t.fr
says...
›
› how to convert COBOL COMP-3 datatypes to C integer type ?
› Does it exist a standard routine ?
› Thanks
›
```

#### ↳ Re: COMP-3 conversion to C integer

- **From:** "scott williamson" <ua-author-1281267@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ab2a447bd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3460FAD6.CC982B23@club-internet.fr>`
- **References:** `<3460FAD6.CC982B23@club-internet.fr>`

```

Didier wrote in article
<346··.@clu··t.fr>...
› how to convert COBOL COMP-3 datatypes to C integer type ?
› Does it exist a standard routine ?
› Thanks
›

This is the code I've used for the conversion. Most of it comes from Mo
Budlong's book - my contribution is fairly minimal. If anyone can improve
it or tidy it up, why not post it back to the newsgroup?

Scott Williamson
sco··.@eas··v.uk
or s.··.@cdv··o.uk






double cvt_packed(int, int, int, int, unsigned char *);
static unsigned int hi_nybble_value(unsigned int),
lo_nybble_value(unsigned int);
static int lo_nybble_sign(signed int);


char tran_char[2048];


void output_rec()
/* this is sample code for the call to cvt_packed
the raw COBOL file data is stuffed into the tran_char array
parameters are:
field offset in buffer
field length in bytes
decimal digits
sign indicator 0 = unsigned, 1 = signed
buffer name

works on both comp-3 and comp-6 data.
*/

{

printf("\n");
printf("%8.0f ", cvt_packed(36, 4, 0, 0,tran_char));
printf("%7.2f ", cvt_packed(40, 6, 2, 1,tran_char));
}

double cvt_packed( int start_ch, int no_chars,
int dec_digits, int sign_val, char *str)
{
double result;
int value, i;
result=0.0;
for(i=0,j=start_ch;no_chars>1;--no_chars,i++,j++)
{
result *=10;
result+=hi_nybble_value(str[j]);
result *=10;
result+=lo_nybble_value(str[j]);
}
result *=10;
result+=hi_nybble_value(str[j]);
if (sign_val==0)
{
result *=10;
result+=lo_nybble_value(str[j]);
}
else
result*=lo_nybble_sign(str[j]);
while(dec_digits--)
result /=10;
return(result);

}
static unsigned hi_nybble_value(unsigned int byte)
{
byte >>=4;
return(byte);
}
static unsigned lo_nybble_value(unsigned int byte)
{
byte &=0x0f;
return(byte);
}
static signed lo_nybble_sign(signed int byte)
{
byte &=0x0f;
if(byte==0x0d)
return(-1);
else
return(+1);
}
```

##### ↳ ↳ Re: COMP-3 conversion to C integer

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ab2a447bd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6ab2a447bd-p4@usenetarchives.gap>`
- **References:** `<3460FAD6.CC982B23@club-internet.fr> <gap-6ab2a447bd-p4@usenetarchives.gap>`

```

›
› This is the code I've used for the conversion. Most of it comes from Mo
› Budlong's book - my contribution is fairly minimal. If anyone can improve
› it or tidy it up, why not post it back to the newsgroup?
›
...snipped long meandering esoteric obsure code fragment.

Good God!
All that just to convert a field from comp-3 to display format. I'll
never understand why so many people thing C is such a great language.
Why doesn't it just accept the standard packed decimal format? Every
time I have to do anything with the C heads at work it's a big fat
mess. No program structure, no system definition, no standard formats,
no compatibility, no data flow, no record layouts, no nothing. But C
is Gods gift to computers... yeah right!

Just to keep the record clear too. Packed decimal is a format built
into the hardware of IBM mainframe machines. There are specific
machine language instructions to manipulate packed data. It is NOT a
COBOL format per se. Comp-3 is how COBOL impliments the use of packed
decimal.

COBOL

05 FIELD-A PIC 9(9)V99 COMP-3.
05 FIELD-B PIC 9(9)V99.

MOVE FIELD-A TO FIELD-B.


ASSEMBLER

FIELDA DS PL6
FIELDB DS CL11

UNPK FIELDB,FIELDA
```

#### ↳ Re: COMP-3 conversion to C integer

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1997-11-05T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ab2a447bd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3460FAD6.CC982B23@club-internet.fr>`
- **References:** `<3460FAD6.CC982B23@club-internet.fr>`

```

Didier wrote:
›
› how to convert COBOL COMP-3 datatypes to C integer type ?
› Does it exist a standard routine ?
› Thanks

One possible solution is to write a very simple COBOL program to
read the file and make the output field be numeric.

Rgds,
Chip
chi··.@sym··a.co
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
