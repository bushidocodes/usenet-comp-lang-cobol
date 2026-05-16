[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable length records in Cobol MVS

_5 messages · 5 participants · 1999-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### Variable length records in Cobol MVS

- **From:** "gee" <grant_englebrecht@nospam.compuware.com>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375db00a@199.186.16.51>`

```
I have a variable length dataset that I am trying to read from and output
some records from.
If I don't have the right copybook how can I determine the length to output
I know I can define it as a 1 to n table of 1 byte fields and the set the
length as the index of this table but this seems a lengthy process.
the FD says
record contains 1 to n chars
block contains 0 records.

when run it takes the maximum lenght of the record layout as the record
length to write out
```

#### ↳ Re: Variable length records in Cobol MVS

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ggj73.28$_F2.3493@dfiatx1-snr1.gtei.net>`
- **References:** `<375db00a@199.186.16.51>`

```
If you don't know the length of the records, you could try something like:

FD THE-MYSTERY-FILE
     RECORD IS VARYING FROM 1 TO 1000 CHARACTERS
     DEPENDING ON MYSTERY-FILE-REC-LENGTH.
01  MR-RECORD   PIC X(1000)


WORKING STORAGE...
77  MYSTERY-FILE-REC-LENGTH   PICTURE S9(04) USAGE BINARY.


.. and something similar on the "write" side.

If 1000 characaters isn't enough, make it bigger and try again.
```

#### ↳ Re: Variable length records in Cobol MVS

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990609094945.07916.00002814@ng-fs1.aol.com>`
- **References:** `<375db00a@199.186.16.51>`

```
"gee" <grant_englebrecht> writes ...

 >I have a variable length dataset that I am trying to read from and output
>some records from.
>If I don't have the right copybook how can I determine the length to output

What are you saying here? Why do you need a copybook? You need the record
layout? Is it not documented anywhere? Is there no copybook? How can you do any
work with no record layout? At the least, use ISPF 3.4 or 3.2 and find out the
record length and blocksize from the label.


>I know I can define it as a 1 to n table of 1 byte fields and the set the
>length as the index of this table but this seems a lengthy process.

Actually, I don't see how you can "set the length as the index of this table";
where would you get this index value?

>the FD says
>record contains 1 to n chars
>block contains 0 records.
>
So you have a program that tells you the [maximum] record size? Or is this what
you made up in your program? What's "n"?


>when run it takes the maximum lenght of the record layout as the record
>length to write out

Well, you need an FD for the output [hmm, was your earlier FD for the input or
the output?] and the record description has to give COBOL some clue how to
determine what record length to use. So, the 01 after your FD needs to include
an "occurs depending on" clause. Usually, but not always, the object of the
depending on clause is a field in the record. So, something like:

FD  outfile
       block contains 0 records.
01   out-rec.
      02   fixed-part     pic x(200).
      02   no-var-parts  pic s9(4) binary.
      02  var-part occurs 1 to 200 times
                     depending on no-var-parts.
             03  field-a   pic...
             03   field-b  pic....
             .
             .
             .

Then, you're responsible for building the output record, including putting the
right value in no-var-parts.

There is no magic in this business. You need information. If it is not given to
you, it is your responsibility to get it.

Regards,

       

Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Variable length records in Cobol MVS

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jokop$kck$1@nnrp1.deja.com>`
- **References:** `<375db00a@199.186.16.51>`

```
In article <375db00a@199.186.16.51>,
  "gee" <grant_englebrecht@nospam.compuware.com> wrote:
> I have a variable length dataset that I am trying to read from and
>output some records from.

<snip>

> when run it takes the maximum lenght of the record layout as the
> record length to write out
>

You simply have to set the record-length of your output record equal to
the length of the input record:

 FD  FI-INFILE
     RECORD IS VARYING FROM 1 TO nnn CHARACTERS
     DEPENDING ON LENGTH-INFILE
     RECORDING MODE IS V.
 01 .......
 FD  FI-OUTFILE
     RECORD IS VARYING FROM 1 TO nnn CHARACTERS
     DEPENDING ON LENGTH-OUTFILE
     RECORDING MODE IS V.
 01 .......

 01 LENGTH-INFILE  PIC 9(4) COMP.
 01 LENGTH-OUTFILE PIC 9(4) COMP.

      READ FI-INFILE
*------ that's the point!
      MOVE LENGTH-INFILE TO LENGTH-OUTFILE
      WRITE ...... FROM ....
```

##### ↳ ↳ Re: Variable length records in Cobol MVS

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3761B10B.763D9908@zip.com.au>`
- **References:** `<375db00a@199.186.16.51> <7jokop$kck$1@nnrp1.deja.com>`

```
Daniel Jacot wrote:
>  FD  FI-INFILE
>      RECORD IS VARYING FROM 1 TO nnn CHARACTERS
       DEPENDING ON WS-REC-LENGTH    ***
>      RECORDING MODE IS V.

>  FD  FI-OUTFILE
>      RECORD IS VARYING FROM 1 TO nnn CHARACTERS
       DEPENDING ON WS-REC-LENGTH    ****
>      RECORDING MODE IS V.

   01 WS-REC-LENGTH  PIC 9(4) COMP.


>  ***     MOVE LENGTH-INFILE TO LENGTH-OUTFILE

Move no longer required, very small optimisation.
Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
