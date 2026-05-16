[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Novice Programmer needs help doing something simple, MERGE

_9 messages · 8 participants · 1999-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Novice Programmer needs help doing something simple, MERGE

- **From:** "Ray" <rferruol@csc.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7peqp8$vst$1@lore.csc.com>`

```
I have 2 files coming into the program that need to be merged, there is a
common key field but the rest of the data does not match,
1st file 69 characters, 2nd file 33 characters, the only field that matches
up is the key.  Can you send some examples of what my code should look like
or offer suggestions, I know this is a simple one, but my college books just
graze over it.
Thanks in advance

rferruol@csc.com
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<935001804.3806.0.nnrp-14.c1edc1b5@news.demon.co.uk>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```

Ray,

Try posting your code here, if your code is very long then just post the
problem area, and im very sure one of us can help you.

Simon R Hart
Eaton.


Ray <rferruol@csc.com> wrote in message news:7peqp8$vst$1@lore.csc.com...
> I have 2 files coming into the program that need to be merged, there is a
> common key field but the rest of the data does not match,
> 1st file 69 characters, 2nd file 33 characters, the only field that
matches
> up is the key.  Can you send some examples of what my code should look
like
> or offer suggestions, I know this is a simple one, but my college books
just
> graze over it.
> Thanks in advance
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** Eileen Preston <epreston@lear.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pf75h$ijd$1@nnrp1.deja.com>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```
In article <7peqp8$vst$1@lore.csc.com>,
  "Ray" <rferruol@csc.com> wrote:
> I have 2 files coming into the program that need to be merged, there
is a
> common key field but the rest of the data does not match,
> 1st file 69 characters, 2nd file 33 characters, the only field that
matches
> up is the key.  Can you send some examples of what my code should look
like
> or offer suggestions, I know this is a simple one, but my college
books just
> graze over it.
> Thanks in advance
>
> rferruol@csc.com

You have your basic 2 file match here.  I'm going to call your 69
character file FILE-A and the 33 character file FILE-B.  Basic code is:

    PERFORM READ-FILE-A-PARA
    PERFORM READ-FILE-B-PARA
    PERFORM MATCH-PARA UNTIL END-OF-FILE-A AND END-OF-FILE-B

MATCH-PARA.
    IF KEY-A = KEY-B
        PERFORM CREATE-OUTPUT-PARA
    ELSE
    IF KEY-A > KEY-B
        what you want to do in this case
        PERFORM READ-FILE-B-PARA
    ELSE
    IF KEY-A < KEY-B
        what you want to do in this case
        PERFORM READ-FILE-A-PARA
    END-IF
    END-IF
    END-IF
    .

READ-FILE-A-PARA.
    READ FILE-A AT END MOVE HIGH-VALUES TO KEY-A.

READ-FILE-B-PARA.
    READ FILE-B AT END MOVE HIGH-VALUES TO KEY-B.

CREATE-OUTPUT-PARA.
     what you want to do here
     WRITE OUTPUT-REC

If you are putting the 2 different records on the same output file then
your output file will be variable length and in your JCL the LRECL would
be 73 (that's 69 the larger record + 4 for the variable stuff).  Be sure
that your FD specifies variable as well.

Once you've coded this up save it in your forever file, you will
definately be doing this again and why reinvent the wheel?


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** "Ray" <rferruol@csc.com>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pf058$28a$1@lore.csc.com>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```
I hope this one gets through....


I have 2 files coming into the program that need to be merged, there is a
common key field but the rest of the data does not match,
1st file 69 characters, 2nd file 33 characters, the only field that matches
up is the key.  Can you send some examples of what my code should look like
or offer suggestions, I know this is a simple one, but my college books just
graze over it.
Thanks in advance

rferruol@csc.com
```

##### ↳ ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BB8D9D.BE0BEA4@att.net>`
- **References:** `<7peqp8$vst$1@lore.csc.com> <7pf058$28a$1@lore.csc.com>`

```
Ray wrote:
> 
> I hope this one gets through....
…[3 more quoted lines elided]…
> 1st file 69 characters, 2nd file 33 characters,

Ask yourself why the different length make a difference. Just match the
keys. Can you get duplicate keys? Does the output sequence matter when
you do?

As someone else suggested, take a stab & post here. Few of us want to do
some else's homework, but most are happy to help someone who's doing
his/her own.

Bill Lynch
```

##### ↳ ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C36C2F.8378C4F1@acm.org>`
- **References:** `<7peqp8$vst$1@lore.csc.com> <7pf058$28a$1@lore.csc.com>`

```
Ray wrote:
> I hope this one gets through....
> 
…[7 more quoted lines elided]…
> rferruol@csc.com

A Generalized Merge Algorithm in pseudo code:

Initialize and Open files
Read next filea record
If EOF-on-filea Then{set filea_key to high_values}
Read next fileb record
If EOF-on-fileb Then {set fileb_key to high_values}
While ~EOF-on-fileb | ~EOF-on-fileb
  {Case
    {(filea_key < fileb_key):
         {Process unmatched filea record and get next filea record
          }
     (filea_key = fileb_key):
         {If filea_key = high_values Then Leave loop
          Else {Merge filea record and fileb record and get next
                record for both filea and fileb
                }
         }
     (filea_key > fileb_key):
         {Process unmatched fileb record and get next fileb record
         }
    }
  }
Close files and other termination actions 

As long as high-values is not an acceptable key value in the external
files, by forcing the fields used for the key comparisons to high-values
on an EOF, the loop logic doesn't need to handle EOF as a special case. 
Translating this into acceptable COBOL, which requires resolving the
details of the merge process and how to handle unmatched records,
depends on the details of your specific application and is left as an
exercise to the reader.
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** docdwarf@clark.net ()
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yLEu3.1006$qt5.49909@iad-read.news.verio.net>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```
In article <7peqp8$vst$1@lore.csc.com>, Ray <rferruol@csc.com> wrote:
>I have 2 files coming into the program that need to be merged, there is a
>common key field but the rest of the data does not match,
…[3 more quoted lines elided]…
>graze over it.

I suggest that you do your own homework, please.

DD
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-08-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oGEu3.212$H23.3007@news3.mia>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```
Ray wrote:
>I have 2 files coming into the program that need to be merged, there is a
>common key field but the rest of the data does not match,

PROCESS.
    OPEN INPUT  FILE-1
                FILE-2
         OUTPUT FILE-3.
    PERFORM READ-FILE-1.
    PERFORM READ-FILE-2.
    PERFORM MERGE-FILES
        UNTIL (HIGH-VALUES = FILE-1-KEY AND FILE-2-KEY).
    CLOSE FILE-1 FILE-2 FILE-3.
    STOP RUN.

READ-FILE-1.
    READ FILE-1
       AT END
           MOVE HIGH-VALUES TO FILE-1-KEY.

READ-FILE-2.
    READ FILE-2
       AT END
           MOVE HIGH-VALUES TO FILE-2-KEY.

MERGE-FILES.
    IF (FILE-1-KEY NOT > FILE-2-KEY)
        <write FILE-1 to FILE-3>
        PERFORM READ-FILE-1
    else
        <write FILE-2 to FILE-3>
        PERFORM READ-FILE-2.
```

#### ↳ Re: Novice Programmer needs help doing something simple, MERGE

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BC097C.5843D62D@zip.com.au>`
- **References:** `<7peqp8$vst$1@lore.csc.com>`

```
Ray wrote:
> 
> I have 2 files coming into the program that need to be merged, there
…[4 more quoted lines elided]…
> but my college books just graze over it.

Look up balanced line algorithm.

There was a link posted about six months ago that described this
method.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
