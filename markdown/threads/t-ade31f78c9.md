[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Decoding COMP numbers

_12 messages · 9 participants · 1998-04 → 1998-05_

---

### Decoding COMP numbers

- **From:** "tlass..." <ua-author-17075594@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`

```

Can anyone tell me how COMPutational numbers or encoded. I need to read COMP
numbers stored in a file created in MicroFocus COBOL on a DOS platform. I'm
using C and PowerBuilder on a Windos NT platform. Help!

Please CC: responses to troy_lassitter at pensacola.dfas.mil.

Thanks,
Troy
```

#### ↳ Re: Decoding COMP numbers

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`

```

Tlassitter wrote:
› Can anyone tell me how COMPutational numbers or encoded.  I need to read
› COMP numbers stored in a file created in MicroFocus COBOL on a DOS platform.
› I'm using C and PowerBuilder on a Windos NT platform.  Help!
› 
› Please CC: responses to troy_lassitter at pensacola.dfas.mil.


MF COBOL stores COMP data as two's complement binary. There are compiler
options which affect the details of word alignment, etc. One problem you
might have with other languages on Intel CPUs is expecting the data to be
stored in byte-reversed form, as in MF COBOL COMP-5 format. For example:

03 xxxxx PIC S9(9) COMP VALUE 305419896.

takes 4 bytes and is stored high to low, left to right as hex:

12 34 56 78

but this field:

03 xxxxx PIC S9(9) COMP-5 VALUE 305419896.

would be stored high to low, right to left in byte reversed form as hex:

78 56 34 12

it is the latter form which would be expected for a 32 bit long integer.
All this in in your MF COBOL Language Reference manual.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove numbers from email id to respond)
```

#### ↳ Re: Decoding COMP numbers

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`

```

Tlassitter wrote:
› 
› Can anyone tell me how COMPutational numbers or encoded.  I need to read COMP
…[3 more quoted lines elided]…
› Please CC: responses to troy_lassitter at pensacola.dfas.mil.

C will have them as (int) depending on the size of the computational
field, you might need to make that a short int (for 16-bit comp), a
regular int (32-bit comp) or a long int (64-bit) comp.
```

##### ↳ ↳ Re: Decoding COMP numbers

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p3@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap>`

```

Joe Zitzelberger wrote:
› 
› Tlassitter wrote:
…[9 more quoted lines elided]…
› regular int (32-bit comp) or a long int (64-bit) comp.

On a DOS platform, COBOL COMP items (big endian) will not be the same as
C native types (little endian). Also, although you can probably expect a
"short" to be 16-bit, "int" and "long" are more likely to be different
to
how you have described them, depending on the C compiler and directives
being
used.

Cheers,
Kev.
```

###### ↳ ↳ ↳ Re: Decoding COMP numbers

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p4@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap> <gap-ade31f78c9-p4@usenetarchives.gap>`

```



Psychedelic Harry wrote in message ...

>much snippage<

› but my understanding of the
› standard was that COMPUTATIONAL was 'the machines native numeric
› representation'.

Some day I am going to track down where this misconception comes from.
There is really NO restriction on what COMP means (in the Standard).
Often - but certainly not universally - it is either the native numeric
format or an efficient storage method - but this certainly is NOT because
the Standard says so!

FYI - Most of the PC compilers that I know of have a compiler
option/directive to determine whether COMP fields are big-endian or
little-endian (for those that even have it as "binary" - which some do no).
I think that most DO default to little-e-endian. HOWEVER, many have a
generic "mainframe compatibility mode" that switches this around.
```

###### ↳ ↳ ↳ Re: Decoding COMP numbers

_(reply depth: 4)_

- **From:** "joe zitzelberger" <ua-author-8235501@usenetarchives.gap>
- **Date:** 1998-05-03T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p5@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap> <gap-ade31f78c9-p4@usenetarchives.gap> <gap-ade31f78c9-p5@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Psychedelic Harry wrote in message ...
…[11 more quoted lines elided]…
› the Standard says so!

I got it from you when you were flameing me about being a mainframe
bigot a few weeks back...when we were discussing calling conventions and
VA parmlists and comp-3 -v- comp and at every post you added the
response something like:

> [selected quote of me]
Please not, the above only applies to IBM Mainframes...blah
...blah...the 'STANDARD' defines so-and-so as 'whatever'.
+ C is a nice language to start with \
+ etc

I believe I had made the mistake of saying it was 'Always Binary' or
some such...
```

##### ↳ ↳ Re: Decoding COMP numbers

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p3@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap>`

```

Joe Zitzelberger wrote:
› 
› Tlassitter wrote:
…[9 more quoted lines elided]…
› regular int (32-bit comp) or a long int (64-bit) comp.


Not quite accurate. Since he said Micro Focus I know that we have the
BigEndian/LittleEndian byte reversal problem. If the numbers were
stored as COMP-5 instead of COMP, you would be entirely correct.
```

###### ↳ ↳ ↳ Re: Decoding COMP numbers

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p7@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap> <gap-ade31f78c9-p7@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Joe Zitzelberger wrote:
…[14 more quoted lines elided]…
› BigEndian/LittleEndian byte reversal problem. 

Hi all. A quick clarification :
This is not a "Micro Focus" problem, as Thane implies.

It's because he is mixing COBOL (portable byte ordering) and C (native
byte
ordering) on a (presumed Intel) chip which does not have the same byte
ordering
as COBOL. The same issue occurs with any COBOL running under these
conditions.

› If the numbers were
› stored as COMP-5 instead of COMP, you would be entirely correct.

Yes, Micro Focus provides COMP-5 as a variant of COMP which mimics the C
types
in that they are native order. I wouldn't recommend writing such items
to a
disk file, though - they are really to facilitate inter-language
communication
and improve speed.

Cheers, Kev.
```

###### ↳ ↳ ↳ Re: Decoding COMP numbers

_(reply depth: 4)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p8@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap> <gap-ade31f78c9-p7@usenetarchives.gap> <gap-ade31f78c9-p8@usenetarchives.gap>`

```


Kevin Digweed wrote in message <354··.@mfl··o.uk>...

› It's because he is mixing COBOL (portable byte ordering) and C (native
› byte
…[4 more quoted lines elided]…
› 
Kevin,
I don't know of any such thing as "COBOL (portable byte ordering)".To the
best of my knowledge, the "storage" mechanism for *ALL* USAGEs and
categories of data in COBOL are implementor defined. How they work
(semantics) is defined in the Standard (so you get truncation to the PICTURE
clause for BINARY items), but how the items are stored and what the compiler
vendor does to get Standard conforming behavior are completely up to the
implementor.
```

###### ↳ ↳ ↳ Re: Decoding COMP numbers

_(reply depth: 5)_

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-05-01T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ade31f78c9-p9@usenetarchives.gap>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com> <gap-ade31f78c9-p3@usenetarchives.gap> <gap-ade31f78c9-p7@usenetarchives.gap> <gap-ade31f78c9-p8@usenetarchives.gap> <gap-ade31f78c9-p9@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Kevin Digweed wrote in message <354··.@mfl··o.uk>...
…[15 more quoted lines elided]…
› implementor.

He said "portable" not "standard". Big-endian format is used by IBM
mainframes and various other 32 bit computers, so it is relatively
portable, whereas I know of no little-endian platform other than Intel.
(Preparing for flames from XYZ platform bigot.)

Not that Unisys people consider 32-bit formats portable.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: Decoding COMP numbers

- **From:** "johan" <ua-author-21418@usenetarchives.gap>
- **Date:** 1998-04-30T14:20:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p11@usenetarchives.gap>`
- **In-Reply-To:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`

```

Tlassitter wrote in article
<199··.@lad··l.com>...
› Can anyone tell me how COMPutational numbers or encoded.  I need to read
› COMP
…[8 more quoted lines elided]…
› 

Troy, here is my 2c worth:

Identify the field (lengths fixed according to pic clause).
Look at the very first bit - switched on, you have a negative field (firts
half byte will have a value > 7).
If the field is positive, you simply convert the hex representation you see
to decimal to get the stored value.
If the field is negative, subtract one from the hex number, compliment it
(subtract from FFFFFFFF) and then convert to decimal.

I hope I understood your problem and that this helps.

Johan Potgieter
www.choicetraining.com
jnp··.@big··t.com
```

#### ↳ Re: Decoding COMP numbers

- **From:** "gvwm..." <ua-author-47960@usenetarchives.gap>
- **Date:** 1998-05-02T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade31f78c9-p12@usenetarchives.gap>`
- **In-Reply-To:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`
- **References:** `<1998043013175500.JAA28044@ladder01.news.aol.com>`

```

On 30 Apr 1998 13:17:55 GMT, tla··.@a··.com (Tlassitter) wrote:

› Can anyone tell me how COMPutational numbers or encoded. I need to read COMP
› numbers stored in a file created in MicroFocus COBOL on a DOS platform. I'm
› using C and PowerBuilder on a Windos NT platform. Help!

hmm. i know comp3 (or packed decimal) is stored like this

(debugging appreciated)

signed long read_packed_decimal(int boolean_S,
int number_of_9s, FILE *fp)
{
/* reads number of digits from file
at last digit it determines if the byte is signed
uses multiply by 10 to move decimal positions.
(faster method not implemented because i didnt think
about it at the time
= read in all but last byte, convert to
number and multiply by 10, read in last byte for sign and add)

*/
int loop;
int temp;
signed return_value;

for( loop=0; loop<(number_of_9s-1);++loop)
{
return_value*= 10;
return_value+= atoi( fgetc(fp));
}
if(boolean_S)
{
return_value*= 10;
temp= fgetc( fp);

if( isdigit( temp))
return_value+= atoi( temp);
else
{
return_value+= _atoi(
tolower(temp)-
'a');


/*reverse sign*/
return_value= (- return_value);
}

}


return(return_value);
}




gvw··.@ix.··m.com to reply remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
