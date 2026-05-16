[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# copy replacing part of words, instead of complete word

_5 messages · 5 participants · 1998-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### copy replacing part of words, instead of complete word

- **From:** ruudvisser@my-dejanews.com
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71rrnm$hpj$1@nnrp1.dejanews.com>`

```


COPY "IOHANDLE.PRC" replacing ==XXXX== by ==CUST==.

In this copy there are statements like

         Move XXXX       to ANOTHER-FIELD.       <-- is replaced
         Move USER-INPUT to KEY-XXXX.            <-- should also be replaced


I want all XXXX's to be replaced, but the replace only works on the complete
word. Is there any kind of wild-character ???????

please help me (to prevent hunderds of copybooks instead of just 1)



-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: copy replacing part of words, instead of complete word

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3647d015.6286801@news-server>`
- **References:** `<71rrnm$hpj$1@nnrp1.dejanews.com>`

```
On Thu, 05 Nov 1998 09:39:02 GMT, ruudvisser@my-dejanews.com
enlightened us:

>
>
…[16 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own    

You might try the following:

COPY "IOHANDLE.PRC" replacing ==XXXX== by ==CUST==
                                       replacing ==-XXXX== by ==-CUST.

Cheers,

          ////
         (o o)
-oOO--(_)--OOo-
Q:  What was the first question they asked Linda Tripp at her make over?
A:  Paper or plastic!

 Steve
```

##### ↳ ↳ Re: copy replacing part of words, instead of complete word

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71t41i$q2n@dfw-ixnews9.ix.netcom.com>`
- **References:** `<71rrnm$hpj$1@nnrp1.dejanews.com> <3647d015.6286801@news-server>`

```
I don't think the post to which I am responding is correct.  Please see
below for corrected (ANSI'85 Standard) solution.

SkippyPB wrote in message <3647d015.6286801@news-server>...
>On Thu, 05 Nov 1998 09:39:02 GMT, ruudvisser@my-dejanews.com
>enlightened us:
…[8 more quoted lines elided]…
>>         Move USER-INPUT to KEY-XXXX.            <-- should also be
replaced
>>
>>
>>I want all XXXX's to be replaced, but the replace only works on the
complete
>>word. Is there any kind of wild-character ???????
>>
…[20 more quoted lines elided]…
> Steve

COPY "IOHANDLE.PRC" replacing ==:XXXX:== by ==CUST==.

In this copy there are statements like

     Move :XXXX:       to ANOTHER-FIELD.       <-- is replaced
     Move USER-INPUT to KEY-:XXXX:.            <-- should also be replaced

Notes:

   A) This means the COPY member will NOT compile cleanly - if "xxxx" is not
replaced.
   B) The next Standard will have cleaner (specific) syntax for doing
"partial word replacement" (which is what this is).
   C) Instead of the colons ":" you can use opening and closing
parenthesis -- however, many people think that the colon is a "cleaner"
variation.
   D) If you want to know the technical reason why this works, you need to
understand the difference between a "text word" and a "COBOL word" -
something that normally makes little or no difference.
```

##### ↳ ↳ Re: copy replacing part of words, instead of complete word

- **From:** spolacek@my-dejanews.com
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tcms$nvk$1@nnrp1.dejanews.com>`
- **References:** `<71rrnm$hpj$1@nnrp1.dejanews.com> <3647d015.6286801@news-server>`

```
In article <3647d015.6286801@news-server>,
  swiegand@neo.rr.com (SkippyPB) wrote:
> On Thu, 05 Nov 1998 09:39:02 GMT, ruudvisser@my-dejanews.com
> enlightened us:
…[20 more quoted lines elided]…
>
 If you have COBOL/MVS you may want to try using the REPLACE command.
This is different from the REPLACE option of the COPY command.

I included the documentation for the REPLACE command.

You would code the REPLACE command as follows:

REPLACE ==XXXX== by ==CUST==.
COPY IOHANDLE.PRC.
REPLACE OFF.

----------------------------------------------------------------------------------------------------------------------------
                       *** REPLACE STATEMENT ***

 The REPLACE statement is a compiler-directing statement which  provides
 an  automatic  method  of applying a change to an entire source program
 (i.e.,  without having to manually identify and modify all places  that
 need  to  be  changed).  It  is  especially  handy  for  simple  string
 substitutions.

      Format 1
      --------
        REPLACE ==pseudo-text1== BY ==pseudo-text2==.

 Each occurence of pseudo-text1 is replaced by the corresponding pseudo-
 text2 value.

      Format 2
      --------
        REPLACE OFF.

 The  Format  2  REPLACE  statement  terminates  any  text   replacement
 currently in effect.  If a Format 2 REPLACE statement is not specified,
 a  Format  1  REPLACE  statement  will  remain in effect until the next
 appearance of a Format 1 REPLACE statement or  until  the  end  of  the
 source program.

 The REPLACE statement must be terminated by  a  separator  period  and,
 unless  it  is  the  first  statement  in  the source program,  must be
 preceded by a separator period.

 Pseudo-text1  must  contain  one  or more text words.  Pseudo-text2 may
 contain one or more text words;  alternatively, it may be a "null" item
 (i.e., == ==).

 The Format 1 REPLACE statement may consist of a single BY phrase or  it
 may  be  specified with two or more BY phrases.  Each pseudo-text1 item
 specified is replaced by the corresponding pseudo-text2 item  specified
 in the same BY phrase.

 Pseudo-text1 in the first BY phrase is compared to an equivalent number
 of  contiguous source program text words starting with the first source
 program text word following the  REPLACE  statement.  If  no  match  is
 found,  the  comparison  is  repeated with each successive occurence of
 pseudo-text1.  When all occurences of pseudo-text1 have  been  compared
 and no match has been found, the comparison operation moves to the next
 successive source program text word.

 When a match is found, the corresponding pseudo-text2 item replaces the
 matching pseudo-text1 item.  The comparison  operation  then  continues
 starting  with  the  source program text word which immediately follows
 the rightmost text word that was just replaced.

 The source program segment which follows:

      REPLACE ==RPL== BY ==EMP==.
      01  RPL-RECORD.
          05  RPL-KEY    PIC X(5).
          05  RPL-DATA   PIC X(95).
      REPLACE OFF.

 would be modified as shown below:

      01  EMP-RECORD.
          05  EMP-KEY    PIC X(5).
          05  EMP-DATA   PIC X(95).







-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: copy replacing part of words, instead of

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298309.64264.19109@kcbbs.gen.nz>`
- **References:** `<71rrnm$hpj$1@nnrp1.dejanews.com>`

```
In message <<71rrnm$hpj$1@nnrp1.dejanews.com>> ruudvisser@my-dejanews.com writes:
> 
> COPY "IOHANDLE.PRC" replacing ==XXXX== by ==CUST==.
…[8 more quoted lines elided]…
> word. Is there any kind of wild-character ???????

The replace only works on Cobol words, this is the defined
behaviour.  What you need to do is use a Cobol word instead
of XXXX.  For example (XXXX).  So your copy book would
be:

              MOVE (XXXX)      TO Another-Field
              MOVE User-Input  TO Key-(XXXX)

Then:

            COPY "file"   REPLACING ==(XXXX)== BY ==CUST==.

will do as you require.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
