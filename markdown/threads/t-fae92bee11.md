[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# trim

_4 messages · 1 participant · 2003-12_

---

### trim

- **From:** Alain Reymond <>
- **Date:** 2003-12-18T14:54:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rsb3uv414ck62r0dmkhk7vgvp1q3l3qvtp@4ax.com>`

```
Here is a small piece of code :

testrim is calling trim. The name says what it does :

testtrim
      $set sourceformat"free"    
       1 b pic x(2000).
       procedure division.
           move "ABCDEFGHIJKLMNOPQRSTUVWXYZ" to b
           call "trim" using 
               by reference address of b
               by content length of b
           end-call
           exit program
           stop run.

Can someone explain why this version works :
trim.cbl
      $set sourceformat"free" 
       working-storage section.
       01 i pic 9(4) comp.
       linkage section.
       01 ls-pStr usage pointer.
       01 ls-len   pic s9(9) usage binary.
       01 lnk-texte   pic x.
       procedure division using ls-pStr, ls-len.
       paragraphe.
           *>version 1
           set address of lnk-texte to ls-pStr
           perform varying i from ls-len by -1
           until ((i < 1) or (lnk-texte(i:1) <> " "))
               move x'00' to lnk-texte(i:1)
           end-perform
           exit program
           .
while this version hangs if b has a picture higher than 108 ? (but is
ok if you define b pic x(108) !!).

      $set sourceformat"free" 
       working-storage section.
       01 tally-count pic 9(7).
       linkage section.
       01 ls-pStr usage pointer.
       01 ls-len   pic s9(9) usage binary.
       01 lnk-texte   pic x.
       procedure division using ls-pStr, ls-len.
       paragraphe.
           *> version 2  
           set address of lnk-texte to ls-pStr
           move zero to tally-count
           inspect function reverse (lnk-texte(1:ls-len))
             tallying tally-count
             for leading spaces
           if tally-count > 0 then
             move low-values to lnk-texte(ls-len - tally-count + 1 :
tally-count)
           end-if
           exit program
           .

I am working with Micro Focus v4.1 under Linux.

This is a small routine to cut spaces at the end of a string. This is
useful in combination with the string instruction :

string 
name delimited by low-values
" " deimited by size
last-name delimited by low-values
into a-string...

Regards.

Alain
```

#### ↳ Re: trim

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-18T10:08:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-MadnXfnQZ6NTHyi4p2dnA@giganews.com>`
- **References:** `<rsb3uv414ck62r0dmkhk7vgvp1q3l3qvtp@4ax.com>`

```
Alain Reymond wrote:
> Here is a small piece of code :
>
…[67 more quoted lines elided]…
> into a-string...

The answer is: Luck?

Where does the subprogram get access to "lnk-texte?" It's certainly never
passed by the calling program.

As an aside, isn't this process a bit more complicated than it needs to be,
what with "pointer" and "by content?"

Just ruminating, mind you:

01  LengthOfString    PIC 9(9).
01  MyString  PIC X(2000).

Move "ABC" to MyString.
Compute LengthOfString = Function Length (MyString)

CALL 'TRIM' Using LengthOfString MyString

--- Called program

Linkage Section.
01  Lnk-Len    PIC 9(9).
01  Lnk-StringX.
   02  Filler occurs 1 to 32000 Depending On Lnk-Len PIC X.

Procedure Division Using Lnk-Len Lnk-StringX.

Inspect Function Reverse Lnk-StringX Tallying TALLY for Leading Space.
Move Low-Values to Lnk-StringX(Lnk-Len - Tally + 1:)
Exit Program
```

##### ↳ ↳ Re: trim

- **From:** Alain Reymond <>
- **Date:** 2003-12-18T23:50:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<db94uvgp1ragqjrcvgk0j4c11bl640be0n@4ax.com>`
- **References:** `<rsb3uv414ck62r0dmkhk7vgvp1q3l3qvtp@4ax.com> <-MadnXfnQZ6NTHyi4p2dnA@giganews.com>`

```
>> Here is a small piece of code :
>>
…[98 more quoted lines elided]…
>Exit Program


Your solution works. And with 
1 lnk-len   pic s9(9) usage binary.
you can use length of directly in the call which spares a move or
compute.

lnk-texte is not passed by the calling program. It is a string that
point to the string passed by the program. ( set address of lnk-texte
to ls-pStr). I can work on this string because I know the length of
it.

But there is no luck in computing! There must be a logical explanation
to the fact that a solution with a pointer does not work when the size
of the passed string is too long...

Regards.

Alain
```

###### ↳ ↳ ↳ Re: trim

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-18T17:39:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<auidndhBv9JVp3-iRVn-hQ@giganews.com>`
- **References:** `<rsb3uv414ck62r0dmkhk7vgvp1q3l3qvtp@4ax.com> <-MadnXfnQZ6NTHyi4p2dnA@giganews.com> <db94uvgp1ragqjrcvgk0j4c11bl640be0n@4ax.com>`

```
Alain Reymond wrote:
>>> Here is a small piece of code :
>>>
…[105 more quoted lines elided]…
> compute.

If you say so. I've never used it. I've never had to use a type declaration
of pointer, either. Nor have I ever found a need to use BY CONTENT when
calling a COBOL subprogram.

One reason is that using "pointer" is like using dynamite -- ask any C
programmer. When it goes bad it goes spectacularily bad.

>
> lnk-texte is not passed by the calling program. It is a string that
> point to the string passed by the program. ( set address of lnk-texte
> to ls-pStr). I can work on this string because I know the length of
> it.

Sure, but it still seems to be the hard way.

>
> But there is no luck in computing! There must be a logical explanation
> to the fact that a solution with a pointer does not work when the size
> of the passed string is too long...

Now if you were using the Fujitsu compiler, you could:

Compute Len = Function Stored-Char-Length(B).
Move Low-values to B(Len + 1:)

thereby avoiding all these complications.

In our universe, we squeeze out multiple blanks in a text field. After that
it's pretty easy to do what I figure is your next operation:

STRING TEXT-FIELD DELIMITED "  " {that's double-blank}.....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
