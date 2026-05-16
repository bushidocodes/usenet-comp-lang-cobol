[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pass values from cobol to c

_5 messages · 4 participants · 2006-03_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Pass values from cobol to c

- **From:** rodrigotraverso@gmail.com
- **Date:** 2006-03-15T09:29:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`

```
Hi, we are trying to use a C++ dll from cobol, when we use a numeric
values works fine by value and by reference, but when we use string
values there's a problem, by value work fine but by reference not, when
c change the value cobol takes trash.

Cobol Program:

      $set SourceFormat"Free"
      $set case
 identification division.

 program-id. cobcallc.
 data division.
 working-storage section.

 01 Rodri1         pic x(10).

 procedure division.
    set pptr to entry "ddlcplus.dll".
    if pptr not = null
       move z"1234567890"     to Rodri1
       display "Alfa"
       stop " "
       call "Alfa" using by reference Rodri1
       display "Cobol Show: " Rodri1
       display "Hit Enter to end..."
       stop " "
     else
        display "failed to load ddlcplus.dll"
     end-if.
     stop run.

Function in C:
__declspec(dllexport) void Alfa(char *d[])
	{
		*d = "Funciono";
		printf ("C Show: %s \n", *d);
	}

In then console when we run cobol progrma, we see this:

Alfa

C Show:: Funciono
Cobol Show: Φû►567890
Hit Enter to end...

Some one have and idea or an example of the problem.

Thanks
Rodrigo
```

#### ↳ Re: Pass values from cobol to c

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-15T19:38:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<23_Rf.147124$B94.42974@pd7tw3no>`
- **In-Reply-To:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`
- **References:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`

```
rodrigotraverso@gmail.com wrote:
> Hi, we are trying to use a C++ dll from cobol, when we use a numeric
> values works fine by value and by reference, but when we use string
> values there's a problem, by value work fine but by reference not, when
> c change the value cobol takes trash. <snip>

For starters, have you looked at COBOL calling C and vice versa, using 
the N/E 4.0 examples :-

http://supportline.microfocus.com/examplesandutilities/nesamp.asp#MixedLanguage

If that doesn't give you what you want, sign up for the free Micro Focus 
Forum at microfocus.com, where you can then post messages under Net Express.

Jimmy
```

#### ↳ Re: Pass values from cobol to c

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-15T14:48:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121grurcuuvmk67@corp.supernews.com>`
- **References:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`

```

<rodrigotraverso@gmail.com> wrote in message
news:1142443774.909734.125290@i40g2000cwc.googlegroups.com...
>Hi, we are trying to use a C++ dll from cobol, when we use a numeric
>values works fine by value and by reference, but when we use string
>values there's a problem, by value work fine but by reference not, when
>c change the value cobol takes trash.

It is probably not "trash", more likely it is the address
of "Funciono".

>Cobol Program:
>
…[8 more quoted lines elided]…
> 01 Rodri1         pic x(10).

This should be "pic x(11)", to hold the nul character terminator.

> procedure division.
>    set pptr to entry "ddlcplus.dll".
>    if pptr not = null
>       move z"1234567890"     to Rodri1

This move is 11 characters, not the 10 it appears to be.

>       display "Alfa"
>       stop " "
…[10 more quoted lines elided]…
>__declspec(dllexport) void Alfa(char *d[])

"(char *d[])" is a pointer to an array of pointers to char.
Use "(char *d)", instead.

>{
>*d = "Funciono";

This assigns the address of "Funciono" to d.
Use "strcpy(d,"Funciono");" instead.

>printf ("C Show: %s \n", *d);

Use "d" without the indirection operator, "*".

>}
>
…[5 more quoted lines elided]…
>Cobol Show: ?�?567890

The strange characters in the first four positions are
probably the address of "Funciono".

>Hit Enter to end...
>
…[3 more quoted lines elided]…
>Rodrigo

I think this is as close as I can be without actually testing.
```

#### ↳ Re: Pass values from cobol to c

- **From:** hcmason@sbcglobal.net
- **Date:** 2006-03-15T18:17:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1142475453.967900.188340@p10g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`
- **References:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com>`

```
Years ago I used Microfocus cobol and called a C routine.  I had to
delimit the strings with a low-value.  C strings sometimes continue
until a low value or \0 in escape sequence is found.

01 MY-STRING.
   05 FILLER PIC X(10) VALUE "MYSTRING".
   05 FILLER PIC X(01) VALUE LOW-VALUES.
call "_cjunk' using my-string.

If you leave off the low-values (binary zeroes) the c runtime won't
know where the C string ends.  I remember having to use nstrcpy to
handle strings that didn't have low-values...
Chris.
```

##### ↳ ↳ Re: Pass values from cobol to c

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-03-16T03:40:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N65Sf.146979$H%4.83146@pd7tw2no>`
- **In-Reply-To:** `<1142475453.967900.188340@p10g2000cwp.googlegroups.com>`
- **References:** `<1142443774.909734.125290@i40g2000cwc.googlegroups.com> <1142475453.967900.188340@p10g2000cwp.googlegroups.com>`

```
hcmason@sbcglobal.net wrote:
> Years ago I used Microfocus cobol and called a C routine.  I had to
> delimit the strings with a low-value.  C strings sometimes continue
…[11 more quoted lines elided]…
> 
I don't know C languages at all but with reference to M/F currently he 
can have following which are also used within COBOL  :-

------------------------------------------------------------------------
Nonnumeric literals can be assigned hexadecimal values by expressing the 
literals as: X"nn", where each n is a hexadecimal digit , and nn can be 
repeated up to 160 times.The number of hexadecimal digits can be odd. 
For example, the following two lines are permitted and are equivalent:

01 an-item PIC X	
MOVE X"04" to an-item
MOVE X"4" to an-item

A null-terminated string can be created by specifying Z"string" and can 
be used anywhere a nonnumeric literal is permitted. The resultant 
literal is equivalent to concatenating X"00" (a null byte) to the end of 
the specified string. In other words, the two following lines are 
equivalent:

MOVE Z"my-literal" TO an-item
MOVE "my-literal" & X"00" TO an-item

** My Note - both the above examples assume that 01 an-Item is at least 
11 characters; any more characters, just chops them off with the x'00'.
**

In the following example, the PICTURE declaration has an extra byte for 
the zero-byte:

01 my-name	PIC X(5) VALUE Z"Jane".
-----------------------------------------------------------------------

I just took a quick look at the M/F zipfile I've already referred him 
to. The two COBOL programs I viewed were using :-

SPECIAL-NAMES.
Call Convention ??

So he may/or may not need that feature.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
