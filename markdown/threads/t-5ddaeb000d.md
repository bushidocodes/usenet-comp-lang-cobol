[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# simple compression routine

_9 messages · 7 participants · 2008-09_

---

### simple compression routine

- **From:** foxgrove@shaw.ca
- **Date:** 2008-09-17T07:52:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```
I need to store nine bytes in an eight byte field.
This is an old COBOL application, where I cannot simply change record
layouts.
The compilers used are MF and Fuj for SCO and Linux. I cannot use
reference modification.
The contents of the field is uppercase letters, numeric digits, spaces
and hyphens.
I don't want to link to external routines, just do it with COBOL code.
My first thought is to convert to octal, using six bits per character.

I'm looking for suggestions on how to best do this.

And NO this is not a school assignment.

Thanks,  Charlie
```

#### ↳ Re: simple compression routine

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-09-17T15:12:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jcl2rF2ll0tU1@mid.individual.net>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```
In article <4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>,
	foxgrove@shaw.ca writes:
> I need to store nine bytes in an eight byte field.
> This is an old COBOL application, where I cannot simply change record
…[11 more quoted lines elided]…
> 

Well, if it is ASCII you only need 7 bits per character and 9 packed
7 bit values will fit easily in 8 bytes with one bit left over, 

I leave the implementation to you, just offering the algorithm.  :-)

bill
```

#### ↳ Re: simple compression routine

- **From:** docdwarf@panix.com ()
- **Date:** 2008-09-17T15:26:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gar7jb$klu$1@reader1.panix.com>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```
In article <4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>,
 <foxgrove@shaw.ca> wrote:
>I need to store nine bytes in an eight byte field.

Other folks need nine dollar's worth of food to be purchased for eight 
dollars (or any other unit of currency).  One learns to live within one's 
budget or one generates debts.

>This is an old COBOL application, where I cannot simply change record
>layouts.

Changing record layouts is rarely a matter of 'simply'... be wary of those 
'all ya gotta do is...' prefaces.

>The compilers used are MF and Fuj for SCO and Linux. I cannot use
>reference modification.

What is the reason that forbids this?

>The contents of the field is uppercase letters, numeric digits, spaces
>and hyphens.

Essentially... any alphanumeric character.

>I don't want to link to external routines, just do it with COBOL code.

What is the reason for this limitation?

>My first thought is to convert to octal, using six bits per character.

There is a Chinese adage along the lines of 'first thought, best 
thought'... you appear to be disproving it.

>
>I'm looking for suggestions on how to best do this.

That depends on a variety of things... what kind of application are you 
dealing with?  What is the transaction volume?  What kind of historical 
requirements for data retention and accessibility must be met in 
accordance with the law?  With 'internal policy'?  Who is making up these 
silly requirements that 'we have to fit nine pounds of fertiliser into a 
eight pound bag without changing anything about the bag or anything which 
surrounds it' and still being taken seriously?

>
>And NO this is not a school assignment.

It doesn't sound like one, no... it sounds like the business has expanded 
to the point where a key field has to be expanded and nobody wants to pay 
for the work that *really* needs to be done.

Having said all this... see if you can't find a copy of ETKPAK out there 
on the web and perhaps what Mr Svalgaard wrote in the COMPPK subroutine is 
of use to you.  Now I know that the original was written to be CALLed as a 
subroutine... but all the source code's there, maybe someone on-site can 
turn it into an inline routine.

DD
```

#### ↳ Re: simple compression routine

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-17T09:38:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0m82d4lut2paj5cajdfj95a4rpm7cfn210@4ax.com>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```
On Wed, 17 Sep 2008 07:52:18 -0700 (PDT), foxgrove@shaw.ca wrote:

>I need to store nine bytes in an eight byte field.

ASCII, EBCDIC?   Platform?

I have a routine that uses the following:

 01  HOLD-KEYS.                                              
     05  HOLD-DBKEY        PIC S9(16) COMP.                  
     05  HOLD-DBKEY-A      REDEFINES HOLD-DBKEY PIC X(8).    


COMPUTE HOLD-DBKEY = 256 * PASSED-DBCONV-PAGE-N  
                   + PASSED-DBCONV-POS-N.        

or

                                                
 DIVIDE  HOLD-DBKEY BY 256 GIVING PASSED-DBCONV-PAGE-N    
           REMAINDER PASSED-DBCONV-POS-N. 
```

#### ↳ Re: simple compression routine

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-09-17T13:20:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oGdnY2UVKqGoUzVnZ2dnUVZ_rXinZ2d@posted.mid-floridainternet>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```

<foxgrove@shaw.ca> wrote in message
news:4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com...
> I need to store nine bytes in an eight byte field.
> This is an old COBOL application, where I cannot simply change record
…[12 more quoted lines elided]…
> Thanks,  Charlie

Feel free to use whatever parts of these you want.

I used Micro Focus COBOL 3.2.50 for MS-DOS
for code and test.
-----
      $set ans85 flag"ans85" flagas"s"
       identification division.
       program-id. to-8byte.
       data division.
       working-storage section.
       1 9-byte-work.
         2 9-byte-char pic x occurs 9 times.
       1 8-byte-work.
         2 8-byte-value binary pic 9(18) value 0.
       1 temp-work.
         2 x pic 9(4) value 0.
         2 char-value pic 9(4) value 0.
       1 first-time-flag pic x value "y".
         88 first-time value "y".
         88 not-first-time value "n".
       1 8-bit-code
           value "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -".
         2 8-bit-char occurs 38 times pic x.
       1 6-bit-code.
         2 6-bit-char occurs 38 times pic x.
       linkage section.
       1 9-byte pic x(9).
       1 8-byte pic x(8).
       procedure division using 9-byte 8-byte.
       begin.
           if first-time
               perform build-6-bit-code-table
               set not-first-time to true
           end-if
           move zero to 8-byte-value
           move 9-byte to 9-byte-work
           inspect 9-byte-work converting
               8-bit-code to 6-bit-code
           perform varying x from 1 by 1
           until x > 9
               compute char-value =
                   function ord (9-byte-char (x)) - 1
               compute 8-byte-value = (8-byte-value * 38)
                   + char-value
           end-perform
           move 8-byte-work to 8-byte
           exit program
           .
       build-6-bit-code-table.
           perform varying x from 1 by 1
           until x > 38
               move function char (x) to 6-bit-char (x)
           end-perform
           .
       end program to-8byte.
-----
      $set ans85 flag"ans85" flagas"s"
       identification division.
       program-id. to-9byte.
       data division.
       working-storage section.
       1 9-byte-work.
         2 9-byte-char pic x occurs 9 times.
       1 8-byte-work.
         2 8-byte-value binary pic 9(18) value 0.
       1 temp-work.
         2 x pic 9(4) value 0.
         2 char-value pic 9(4) value 0.
       1 8-bit-code
           value "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -".
         2 8-bit-char occurs 38 times pic x.
       linkage section.
       1 8-byte pic x(8).
       1 9-byte pic x(9).
       procedure division using 8-byte 9-byte.
       begin.
           move 8-byte to 8-byte-work
           perform varying x from 9 by -1
           until x < 1
               divide 8-byte-value by 38
                   giving 8-byte-value
                   remainder char-value
               move 8-bit-char (char-value + 1) to 9-byte-char (x)
           end-perform
           move 9-byte-work to 9-byte
           exit program
           .
       end program to-9byte.
-----
      $set ans85 flag"ans85" flagas"s"
       identification division.
       program-id. to-test.
       environment division.
       configuration section.
       special-names. class valid-chars is
           "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -".
       data division.
       working-storage section.
       1 9-byte pic x(9).
       1 8-byte.
         2 8-byte-value binary pic 9(18) value 0.
       procedure division.
       begin.
           perform with test after
           until 9-byte = spaces
               display "? " with no advancing
               accept 9-byte
               if 9-byte = spaces
                   continue
               else
                   if 9-byte is valid-chars
                       call "to-8byte" using 9-byte 8-byte
                       display 9-byte space 8-byte-value
                       call "to-9byte" using 8-byte 9-byte
                       display 8-byte-value space 9-byte
                   else
                       display "invalid characters in input"
                   end-if
               end-if
           end-perform
           stop run
           .
       end program to-test.
----- Output
? ABCDEFGHI
ABCDEFGHI 000000120683784706
000000120683784706 ABCDEFGHI
? A-B 2 JU
A-B 2 JU  000004239300331328
000004239300331328 A-B 2 JU
? 1-2-3-4-5
1-2-3-4-5 000121711064759229
000121711064759229 1-2-3-4-5
? abcdefg
invalid characters in input
? SUCCESS
SUCCESS   000080554759843508
000080554759843508 SUCCESS
?
-----
```

#### ↳ Re: simple compression routine

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-17T19:22:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f63d4drbqs2ir23j0b0qqj6g9v8qnvcju@4ax.com>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com>`

```
On Wed, 17 Sep 2008 07:52:18 -0700 (PDT), foxgrove@shaw.ca wrote:

>I need to store nine bytes in an eight byte field.
>This is an old COBOL application, where I cannot simply change record
…[10 more quoted lines elided]…
>And NO this is not a school assignment.

You are using 7 bits (ASCII) of bytes 1 through 8. Store the bits of byte 9 in the unused
high-order bits.

01  number-nx.      
     05      pic x value low-value.  
     05   byte-n pic x.
01 number-n redefines number-nx binary pic s9(4).
01  number-9x.
     05      pic x value low-value.
     05   byte-9 pic x. 
01 number-9 redefines number-9x binary pic s9(4).
01 bit-9 binary pic s9(4).


move input-byte (9) to byte-9
perform varying n from 1 by 1 until n > 8
    move input-byte (n) to byte-n
    divide 2 into number-9 giving number-9 remainder bit-9
    compute number-n = number-n + (bit-9 * 128)
    move byte-n to output-byte (n)
end-perform
```

##### ↳ ↳ Re: simple compression routine

- **From:** foxgrove@shaw.ca
- **Date:** 2008-09-18T08:17:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cbf05fda-8630-4dc1-80d7-9fc07c5b6530@a3g2000prm.googlegroups.com>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com> <4f63d4drbqs2ir23j0b0qqj6g9v8qnvcju@4ax.com>`

```
Thanks all for the advice and techniques.
Cludge in place, on to next......
```

###### ↳ ↳ ↳ Re: simple compression routine

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-09-18T16:23:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jfdjkF32fepU1@mid.individual.net>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com> <4f63d4drbqs2ir23j0b0qqj6g9v8qnvcju@4ax.com> <cbf05fda-8630-4dc1-80d7-9fc07c5b6530@a3g2000prm.googlegroups.com>`

```
In article <cbf05fda-8630-4dc1-80d7-9fc07c5b6530@a3g2000prm.googlegroups.com>,
	foxgrove@shaw.ca writes:
> Thanks all for the advice and techniques.
> Cludge in place, on to next......

Actually, after I sent my first suggestion I thought about another.
RADIX50.  :-)

bill
```

###### ↳ ↳ ↳ Re: simple compression routine

_(reply depth: 4)_

- **From:** epc8@juno.com
- **Date:** 2008-09-18T11:05:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4f410be-1903-461b-aa0c-7db33b560861@m3g2000hsc.googlegroups.com>`
- **References:** `<4fa756dd-e4cd-47af-821f-493d99d8353f@n33g2000pri.googlegroups.com> <4f63d4drbqs2ir23j0b0qqj6g9v8qnvcju@4ax.com> <cbf05fda-8630-4dc1-80d7-9fc07c5b6530@a3g2000prm.googlegroups.com> <6jfdjkF32fepU1@mid.individual.net>`

```
On Sep 18, 12:23 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <cbf05fda-8630-4dc1-80d7-9fc07c5b6...@a3g2000prm.googlegroups.com>,
>         foxgr...@shaw.ca writes:
…[7 more quoted lines elided]…
> bill

see http://en.wikipedia.org/wiki/RADIX-50

Note that 50 is OCTAL for the size of the character set.

SIXBIT is yet another DEC character encoding. A different six-bit
character set belonged to Univac. Maybe the OP's application needs to
interface with Fieldata Cobol?

- e
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
