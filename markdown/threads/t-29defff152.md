[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# All X'0D' lost during reading line sequential file using microfocus se

_69 messages · 12 participants · 2008-07 → 2008-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-24T02:40:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com>`

```
Hi all

I'm writing a batch source to match 2 input files which is exported
from AIX DB2 giving the matched records.

All other characters are going well except X'0D':all of them get lost
when reading the input files into the program. I tried many file
handler options and runtime switches but no one worked. Any advice is
appreaciated. Thanks in advance!

Line sequential file, variable-length record.

This is the file handler I'm using now:
[XFH-DEFAULT]
STRIPSPACE=OFF
INSERTNULL=OFF
EXPANDTAB=OFF

AIX 5.3, Microfocus Server Express 5.0
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-24T12:28:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com>`

```
On Thu, 24 Jul 2008 02:40:37 -0700 (PDT), taoxianfeng@gmail.com wrote:

>Hi all
>
…[16 more quoted lines elided]…
>AIX 5.3, Microfocus Server Express 5.0

Define the file as record sequential, record length 512, and parse the lines yourself. The
last short block is a little tricky.
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-24T17:51:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com>`

```
On Jul 25, 2:28 am, Robert <n...@e.mail> wrote:
> On Thu, 24 Jul 2008 02:40:37 -0700 (PDT), taoxianf...@gmail.com wrote:
> >Hi all
…[22 more quoted lines elided]…
> - Show quoted text -

Do you mean fixed-length record sequential? The record exported from
AIX DB2 is variable-length so I think it will be even worse.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-24T22:31:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1lhi84d9gaeni3o2lk2lds4444bg11ubga@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com>`

```
On Thu, 24 Jul 2008 17:51:59 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On Jul 25, 2:28ï¿½am, Robert <n...@e.mail> wrote:
>> On Thu, 24 Jul 2008 02:40:37 -0700 (PDT), taoxianf...@gmail.com wrote:
…[26 more quoted lines elided]…
>AIX DB2 is variable-length so I think it will be even worse.

A variable length record is just a string of bytes terminated by x'0D'. Line sequential
parses the records for you. You are complaining about that. Line sequential just gives you
512 bytes of raw data, allowing you to parse them yourself.

Is the problem that you don't know the length of an input line sequential record? Why do
you care? The tail end will be filled with spaces. You COULD search right to left for a
non-space, or follow Richard's instructions for getting the length.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-25T00:41:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com>`

```
On Jul 25, 12:51 pm, taoxianf...@gmail.com wrote:
> On Jul 25, 2:28 am, Robert <n...@e.mail> wrote:
>
…[29 more quoted lines elided]…
> AIX DB2 is variable-length so I think it will be even worse.

Sequential fixed length files have nothing but the data bytes, no
header or termination bytes. Defining the file as sequential with a
fixed length will allow you to read (and write) whatever bytes you
want but it will read <record size> bytes and you will get an
exception on the last record because it does not fill the record
buffer. You can have single byte sequential to avoid the last record
problem, but it may be somewhat slow.

Set up the file as sequential with single byte record and read into a
buffer in W-S until you find the record terminator.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-25T01:22:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05678c39-d214-4037-9360-93b395284430@i24g2000prf.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com> <928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com>`

```
On Jul 25, 4:41 pm, Richard <rip...@azonic.co.nz> wrote:
> On Jul 25, 12:51 pm, taoxianf...@gmail.com wrote:
>
…[46 more quoted lines elided]…
> - Show quoted text -

umm...It should be an approach.Probably a bit slow. I will have a try.

Thank you very much.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-07-26T16:07:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<opSdndvUn6CYDxbVnZ2dnUVZ_rzinZ2d@earthlink.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com> <928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com> <05678c39-d214-4037-9360-93b395284430@i24g2000prf.googlegroups.com>`

```
taoxianfeng@gmail.com wrote:
>>
>> Set up the file as sequential with single byte record and read into a
…[7 more quoted lines elided]…
> Thank you very much.

A "bit slow" ain't the half of it.

Fortunately, our compiler has a method of reading a file given 
{starting-byte} {length of string to read}. To read the file sequentially we 
do:

MOVE 0 TO START-BYTE
MOVE 32000 TO LENGTH-STRING.
PERFORM UNTIL TOO-TIRED
  (read the file using START-BYTE and LENGTH-STRING)
  (determine length of record - ours ends with a TAB character)
  (process record)
  ADD LENGTH-OF-RECORD TO START-BYTE
  END-PERFORM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-26T17:23:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a75a44a-794a-47cb-b612-50e8d0fa0639@h17g2000prg.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com> <928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com> <05678c39-d214-4037-9360-93b395284430@i24g2000prf.googlegroups.com> <opSdndvUn6CYDxbVnZ2dnUVZ_rzinZ2d@earthlink.com>`

```
umm...it probably doesn't work either. Do you think X'0D' will be
handled differently
under this way?

I will have a try. Thanks.

On Jul 27, 6:07 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> taoxianf...@gmail.com wrote:
>
…[23 more quoted lines elided]…
>   END-PERFORM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-07-28T11:24:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rM-dnWv0LLFbbxDVnZ2dnUVZ_trinZ2d@earthlink.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com> <928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com> <05678c39-d214-4037-9360-93b395284430@i24g2000prf.googlegroups.com> <opSdndvUn6CYDxbVnZ2dnUVZ_rzinZ2d@earthlink.com> <5a75a44a-794a-47cb-b612-50e8d0fa0639@h17g2000prg.googlegroups.com>`

```
taoxianfeng@gmail.com wrote:
> umm...it probably doesn't work either. Do you think X'0D' will be
> handled differently
> under this way?
>
> I will have a try. Thanks.

Sure it'll work.

INSPECT {record name} TALLYING {record-length} FOR CHARACTERS BEFORE X'0D'.


>
> On Jul 27, 6:07 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
…[26 more quoted lines elided]…
>> END-PERFORM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T19:32:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfa205b4-bbc8-4ef2-87d2-481e04963586@e39g2000hsf.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <3bc9c1cd-2384-4d90-ad1f-30cb0e717928@k36g2000pri.googlegroups.com> <928d3040-2a52-4fb0-b872-fe1c03e266fd@z6g2000pre.googlegroups.com> <05678c39-d214-4037-9360-93b395284430@i24g2000prf.googlegroups.com> <opSdndvUn6CYDxbVnZ2dnUVZ_rzinZ2d@earthlink.com> <5a75a44a-794a-47cb-b612-50e8d0fa0639@h17g2000prg.googlegroups.com> <rM-dnWv0LLFbbxDVnZ2dnUVZ_trinZ2d@earthlink.com>`

```
On Jul 29, 1:24 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> taoxianf...@gmail.com wrote:
> > umm...it probably doesn't work either. Do you think X'0D' will be
…[42 more quoted lines elided]…
> - Show quoted text -

I'm sorry I still can't fully understand your meaning.But when I'm
trying like that:

     FD
INFILE1
     DATA RECORD IS IN-
REC1
     RECORDING MODE
V
     RECORD IS VARYING IN SIZE FROM 1 TO
5000
     DEPENDING ON WK-INREC1-
LEN.
     01  IN-REC1                      PIC
X(5000).
     ……
     READ  INFILE1
     ……
     INSPECT IN-REC1 TALLYING WK-TMP1 FOR CHARACTERS BEFORE X'0D'

The result of WM-TMP1 is 5001 added by the actual length decided by
X'0A' and EXLUDING X'0D'. For example:
...0D..0D.0A      (record length is 8 including 0D but 0A)
Then the value of WM-TMP1 is 5007.(only 6 characters were counted)
........0A        (record length is 8 exluding 0A)
Then the value of WM-TPM1 is 5009.(all 8 characters were counted since
no X'0D')

So that means X'0D' is discarded when READing the file and the INSPECT
always gives the maximium record length since it can't find X'0D'.

And my question by "it probably doesn't work either" means reading the
file by a given length will also discard the X'0D', though I have not
tried yet.
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2008-07-29T09:31:31+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<488e7301$0$3508$a82e2bb9@reader.athenanews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com...
> On Thu, 24 Jul 2008 02:40:37 -0700 (PDT), taoxianfeng@gmail.com wrote:
>
…[22 more quoted lines elided]…
> last short block is a little tricky.

MOVE ALL X0D TO FD before the READ.

Old programmers' trick.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T19:50:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b054ff78-270b-4304-8e1d-9477cb8a39c5@56g2000hsm.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <488e7301$0$3508$a82e2bb9@reader.athenanews.com>`

```
On Jul 29, 10:31 am, "billious" <billious_1...@hotmail.com> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[36 more quoted lines elided]…
> - Show quoted text -

Move before the read? Could you explain it with more detail? Thanks a
lot.
How can I move X'0D' since I don't know where and how much of them
will be in the record?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-28T23:22:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo3t84l0ni5tcnu8qofrubgjaqk40pabo2@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <488e7301$0$3508$a82e2bb9@reader.athenanews.com> <b054ff78-270b-4304-8e1d-9477cb8a39c5@56g2000hsm.googlegroups.com>`

```
On Mon, 28 Jul 2008 19:50:25 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On Jul 29, 10:31ï¿½am, "billious" <billious_1...@hotmail.com> wrote:
>> "Robert" <n...@e.mail> wrote in message
…[42 more quoted lines elided]…
>will be in the record?

He meant initialize the record area so the tail of the last block would be filled with
x'0D'. Spaces would be a better choice. I would do it like this:

select input-file assign to INFILE1 
 record sequential
 file status file-status.

fd input-file.
01  input-record.
    05  input-byte occurs 512 pic x.

01 file-status pic x(2).
01 pic x. 88 end-of-file value 'y' false low-value.
01 pic x. 88 last-sector value 'y' false low-value.
01 pic x. 88 in-quotes value 'y' false low-value.
01 pic x. 88 end-of-record value 'y' false-low-value.
01 sub-in pic 9(4)  binary.
01 sub-out pic 9(4) binary.
01  output-record.
     05  output-byte occurs 512 pic x.

set end-of-file, last-sector, in-quotes to false
open input input-file
perform read-sector

perform until end-of-file
  set end-of-record to false
  move spaces to output-record
  move 1 to sub-out
  perform until end-of-record or end-of-file
   evaluate input-byte (sub-n) also true
      when space also not in-quotes
        move low-value to input-byte (sub-n)
      when x'0A' also not in-quotes
        set end-of-record to true
      when quote also not in-quotes
        set in-quotes to true
      when quote also in-quotes
        set in-quotes to false
   end-evaluate 
   if  input-byte (sub-n) not equal to low-value
       move input-byte (sub-in) to output-byte (sub-out) 
       add 1 to sub-out
       if  sub-out greater than length of output-record
          display 'Record  too big ' output-record
          call 'abort'
       end-if
   end-if
   add 1 to sub-in
    if  sub-in greater than length of input-record
         perform read-sector
    end-if
   end-perform
   [do something with output-record]
end-perform

close input-file
exit program.
  
read-sector.
  if  last-sector
      set end-of-file to true
  else
     move spaces to input-record
     read input-file at end set end-of-file to true end-read
     move 1 to sub-in
     evaluate file-status
       when '92'
         set last-sector to true
       when not = zero and not end-of-file
        display 'Read error ' file-status
        call 'abort'
    end-evaluate
  end-if.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2008-07-29T13:50:22+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<488eafad$0$3398$a82e2bb9@reader.athenanews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <kpeh84lkodm0ksj8hub80dsc28h9ojmtn4@4ax.com> <488e7301$0$3508$a82e2bb9@reader.athenanews.com> <b054ff78-270b-4304-8e1d-9477cb8a39c5@56g2000hsm.googlegroups.com>`

```
taoxianfeng@gmail.com wrote:
> On Jul 29, 10:31 am, "billious" <billious_1...@hotmail.com> wrote:
>> "Robert" <n...@e.mail> wrote in message
…[43 more quoted lines elided]…
> will be in the record?

LINE INPUT transfers characters from the input datastream until the next 
X'0D'/X'0A' (depending on system) into the input record. Hence, X'0D' and 
X'0A' should never appear in the input record.

Problem is that the transfer merely stops at the character before the 
End-Of-Line (whatever it may be) - the record is not 'filled' - so any 
characters from a LONGER previous record are not overwritten.

Hence, if you simply

MOVE SPACES TO INPUT-RECORD.
READ INPUT-FILE.

then the data appearing will simply be the contents of the shorter 
next-record, filled with spaces.

Now whether you move SPACES or LOW-VALUES or HIGH-VALUES or ASCII-CR or 
ASCII-LF or ASCII-NULL is up to you, and how you wish to process the data. 
You appeared to be worried about X'0D' being absent - use ASCII-CR if that 
suits your purpose. I last ran into that problem on a DEC/VMS machine, but 
it was a standard problem.

Outputting such a record normally suppresses trailing-spaces, so probably 
spaces would be the better idea. Depends on what you want to do overall.

I've assumed that you have a record something like

01 INPUT-RECORD.
 03 INPUT-CHARS PIC X(01) OCCURS HOWEVER-MANY.

And also that you have a copybook of constants like

01 STANDARD-CONSTANTS.
 03 ASCII-NULL.
  05 FILLER PIC 9(02) COMP VALUE 0.
 03 ASCII-LF.
  05 FILLER PIC 9(02) COMP VALUE 10.
 03 ASCII-CR.
  05 FILLER PIC 9(02) COMP VALUE 13.
 03 ASCII-DOUBLE-QUOTES.
  05 FILLER PIC 9(02) COMP VALUE 34.
 03 ASCII-QUOTES.
  05 FILLER PIC 9(02) COMP VALUE 39.

(I do it that way - and establish other symbolic constants like this because 
it is implementation-independent)
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-07-24T11:47:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rrfh845hlp12g2h6ae385cl5nr8ueit6h0@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com>`

```
I noticed that a free editor for the Mac (Textwrangler) gives people
the option of saving a text file about a dozen different ways.   (Mac,
Unix, various Unicode, Windows, line-feed, form-feed).

I'm wondering if there are similar free or cheap utilities that can do
this kind of conversion on your platform.
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-24T18:16:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b502782-f4fc-46cc-a026-791dfe0453be@o40g2000prn.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <rrfh845hlp12g2h6ae385cl5nr8ueit6h0@4ax.com>`

```
On Jul 25, 2:47 am, Howard Brazee <how...@brazee.net> wrote:
> I noticed that a free editor for the Mac (Textwrangler) gives people
> the option of saving a text file about a dozen different ways.   (Mac,
…[3 more quoted lines elided]…
> this kind of conversion on your platform.

We are restricted to solving the problem within the cobol program, not
to mention the Mac editor...
Thanks anyway
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-24T12:30:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com>`

```
On Jul 24, 9:40 pm, taoxianf...@gmail.com wrote:
> Hi all
>
…[8 more quoted lines elided]…
> Line sequential file, variable-length record.

LINE SEQUENTIAL is defined as being variable records where the end of
each record is indicated (on AIX) by a x'0D' character. These are
added automatically when writing and stripped off when reading.

You have specified that the file is 'line sequential' and then
complain when you get the designated behavior.

Specify the file like this:

           SELECT TextFile
               ASSIGN whatever
               ORGANIZATION LINE SEQUENTIAL
               FILE STATUS ..
           .

       DATA DIVISION.
       FILE SECTION.
       FD  TextFile
           RECORD VARYING FROM 0 TO 256 DEPENDING ON TSize.
       01  TextLine.
           03 TLc                      PIC X(256).


TSize will contain the record length. You can insert a x"0D" after
that or use reference modification on the compares, or just compare
lengths.
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-24T18:45:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aad4907-50fd-4d09-b0ed-283da6cd3ef7@j33g2000pri.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com>`

```
On Jul 25, 4:30 am, Richard <rip...@azonic.co.nz> wrote:
> On Jul 24, 9:40 pm, taoxianf...@gmail.com wrote:
>
…[36 more quoted lines elided]…
> lengths.

I don't agree.Isn't line sequential file delimited by X'0A'?

These are the documentation I referred:
(JP)http://www.microfocus.co.jp/manuals/SE40/fhorgs.htm
(EN)http://supportline.microfocus.com/Documentation/books/sx50/
sx50indx.htm

Line Sequential Files
The primary use of line sequential files (which are also known as
"text files" or "ASCII files") is for display-only data. Most PC
editors, for example Notepad, produce line sequential files.

In a line sequential file, each record in the file is separated from
the next by a record delimiter. The record delimiter, which is the
line feed (x"0A") character, is inserted after the last non-space
character in each record. A WRITE statement removes trailing spaces
from the data record and appends the record delimiter. A READ
statement removes the record delimiter and, if necessary, pads the
data record (with trailing spaces) to the record size defined by the
program reading the data.

To define a file as line sequential, specify ORGANIZATION IS LINE
SEQUENTIAL in the SELECT clause for the file in your COBOL program,
for example:

 select lineseq assign to "lineseq.dat"
     organization is line sequential.


Or could you give me the documentation link saying that line
sequential file is delimited by X'0D'?
Thank you very much
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-25T09:42:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kdhik.100238$o12.10431@fe03.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com>`

```
OK,  I think I understand the "desire".  You want to use X"0A" but *not* X"0D0A" 
as the record delimiter for line sequential files.  (Something that is 
"operating system" and/or application dependent).  Your desire is to be able to 
have X"0D" *data* in LINE SEQUENTIAL files.

From a "usually reliable source" Micro Focus *does* support (allow) this.  The 
following is the solution that I was provided:
 ***
"File Handler configuration option LSRECDELIM set in EXTFH.CFG can be used to 
set the record delimiter used for LSEQ files.

Syntax:

LSRECDELIM=[0A|0D0A]

Parameters:

0A The hexadecimal character x"0A" is used as the record delimiter for line 
sequential files.

0D0A The hexadecimal characters x"0D0A" are used as the record delimiter for 
line sequential files."
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-25T18:31:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com>`

```
On Jul 25, 6:42 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> OK,  I think I understand the "desire".  You want to use X"0A" but *not* X"0D0A"
> as the record delimiter for line sequential files.  (Something that is
…[49 more quoted lines elided]…
> - Show quoted text -

Thanks for you advice. But I tried it and the result is the same. I
think the LSRECDELIM option just affect the record delimiter (0A or
0D0A) but failed to change something for a single 0D.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-26T03:20:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rKwik.295630$3p2.79161@fe10.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com>`

```

```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-26T03:22:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7Mwik.295652$3p2.60961@fe10.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com>`

```
I think the additional information that you need was in another note that I 
received which states,

" ...the information you are after is there but hidden away in the 
documentation. The File Handler configuration option INSERTNULL allows any 
character to be added to a line sequential file by adding a null character 
before each character less than x"20". These then get stripped out on the read. 
Again this is not documented fully in the INSERTNULL documentation but is in the 
documentation for the "N run-time switch"

Therefore, it seems that a READ (with MF and Line Sequential) will ALWAYS "strip 
away" characters < X"20".
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-26T08:41:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com>`

```
Actually I have also tried INSERTNULL=ON (default is on and I'm using
off now) in the extfh config file
and the N runtime switch(default is on).
All the other characters less than X'20' were successfully outputted
with a X'00' (null) before them.
BUT THE X'0D' STILL DISAPPEARED. I really can't believe this and I'm
getting confused why some file handler
options and runtime switches seem to be conflicting or doing the same
thing, such as:

INSERTNULL and N runtime switch
EXPANDTAB/INSERTTAB and T runtime switch

and the file handler options have higher priority.
Who can explain it?

On Jul 26, 12:22 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I think the additional information that you need was in another note that I
> received which states,
…[78 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-26T18:26:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q%Jik.317256$Ev5.117862@fe09.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com>`

```
If you are current on your Micro Focus support (i.e. paid up), then the place to 
ask this questions is via supportline.

HOWEVER, the bottom-line is that if you define a file as line sequential, then 
you will have problems trying to read records that include (as data) bytes with 
characters less than X"20".  This is documented - even if not well.

Treating the file as Record Sequential and "building" it yourself will work (as 
you have indicated).  However, there is also the question of HOW and WHY you 
have "line sequential" files with X'0D" "data" or any other bytes with < X"20". 
These may cause problems with other applications - not just Micro Focus COBOL 
(as the X"1?" notes in this thread have indicated and as previous notes 
discussing "tabs" have indicated.)
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-26T14:22:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e0a3512-3cd3-4570-b3cc-a72a8f8d7566@p31g2000prf.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com>`

```
On Jul 27, 6:26 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> If you are current on your Micro Focus support (i.e. paid up), then the place to
> ask this questions is via supportline.
…[31 more quoted lines elided]…
> Who can explain it?

The N and T runtime switch usage dates back to MF's Level II COBOL on
1982 and has been retained for compatability reasons in every MF Cobol
since.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-26T17:19:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com>`

```
I'm new to that project so not quite clear about the Microfocus
support. I will try to
contact them through my boss.

I'm also wondering why these characters less than X'20' are inlcuded
in the data such as 0A,0D,09.
Take 0A for example, sometimes a db2 record is exported like that:
"xxx",1234,"...0A
..."
I have to count the quotation marks to determine if a record is
divided into several lines and
combine them together.

But at present, the most suprising point is, all the characters less
than X'20' EXCEPT X'0D'
are handled correctly. What on earch is the particularity of X'0D'?

On Jul 27, 3:26 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> If you are current on your Micro Focus support (i.e. paid up), then the place to
> ask this questions is via supportline.
…[123 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-26T23:29:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com>`

```
On Sat, 26 Jul 2008 17:19:09 -0700 (PDT), taoxianfeng@gmail.com wrote:

>I'm new to that project so not quite clear about the Microfocus
>support. I will try to
…[13 more quoted lines elided]…
>are handled correctly. What on earth is the particularity of X'0D'?

0D is Carriage Return. It is used in the combination 0D0A on Windows. Apparently Micro
Focus simplified end of record detection by discarding 0D and looking for 0A. 

DB2 is mainframe, not Unix. If your files were exported from DB2, it's not clear why 0D
appears in the middle of a record, why it needs to be preserved nor why a row would be
split across two records. This is NOT NORMAL. 

X'09' is tab, which is another source of frustration. Tab is used to compress repeating
spaces, but there is NO STANDARD on how to expand tabs. Many programs assume a tab stop
every eight bytes, but spreadsheets use tab to mean Next Field, which could be any number
of bytes away. Whenever I get a file with tabs, I convert them to spaces, then line up the
resulting mess. Tabs are a Bad Idea.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-27T01:21:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com>`

```
Do you mean it would be impossible for us to get the 0D if Micro Focus
simply discarded it?

I can't understand your "DB2 is mainframe, not Unix". It should be a
series of cross-platform databases though each of them may different
from each other.This is the documentation of DB2 for Unix:
http://publib.boulder.ibm.com/infocenter/db2luw/v9/index.jsp
And the data is EXPORTed from db2 on AIX(Actually comes from mainframe
DB2 since it's a migration project).

But I have to admit the data is quite unusual.Fortunately I have
handled X'09' correctly with EXPANDTAB=OFF.

On Jul 27, 1:29 pm, Robert <n...@e.mail> wrote:
> On Sat, 26 Jul 2008 17:19:09 -0700 (PDT), taoxianf...@gmail.com wrote:
> >I'm new to that project so not quite clear about the Microfocus
…[29 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-27T10:10:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>`
- **References:** `<Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com>`

```
On Sun, 27 Jul 2008 01:21:51 -0700 (PDT), taoxianfeng@gmail.com wrote:

>Do you mean it would be impossible for us to get the 0D if Micro Focus
>simply discarded it?

It's impossible when using LINE SEQUENTIAL.

>I can't understand your "DB2 is mainframe, not Unix". It should be a
>series of cross-platform databases though each of them may different
>from each other.This is the documentation of DB2 for Unix:
>http://publib.boulder.ibm.com/infocenter/db2luw/v9/index.jsp

For many years, DB2 on Unix was called UDB -- Universal Data Base. Evidently, IBM recently
changed the name to DB2. 

>And the data is EXPORTed from db2 on AIX(Actually comes from mainframe
>DB2 since it's a migration project).
>
>But I have to admit the data is quite unusual.Fortunately I have
>handled X'09' correctly with EXPANDTAB=OFF.

Users entered tabs to make columns line up on a monospaced display. Those tabs probably
won't work the same way on your new platform. Same for the carriage returns and line
feeds.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-27T16:05:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6i6c9$7qj$1@reader1.panix.com>`
- **References:** `<Kdhik.100238$o12.10431@fe03.news.easynews.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com> <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>`

```
In article <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>For many years, DB2 on Unix was called UDB -- Universal Data Base.
>Evidently, IBM recently
>changed the name to DB2. 

Mr Wagner, you betray yourself as a COBOL programmer; I first worked with 
an IBM product called DB2 on a mainframe in 1987 and the product was first 
released (according to http://en.wikipedia.org/wiki/IBM_DB2 ) in 1983.

COBOL programmers, at times, seem to have... different ideas of 
'recently'.

DD
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-27T12:01:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9adc8a94-d1f9-42e0-aebf-f6b0139f60d4@v39g2000pro.googlegroups.com>`
- **References:** `<Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com> <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>`

```
On Jul 28, 3:10 am, Robert <n...@e.mail> wrote:
> On Sun, 27 Jul 2008 01:21:51 -0700 (PDT), taoxianf...@gmail.com wrote:
> >Do you mean it would be impossible for us to get the 0D if Micro Focus
…[10 more quoted lines elided]…
> changed the name to DB2.

You are wrong. The name of the product is, and has been, "DB2
Universal Database" which is available on z/OS, OS/390, iSeries, AIX/
Unix/Linux and Windows. Other products are "DB2 Connect" and "DB2
Warehouse Manager".
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-27T22:42:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<66fq84d2u01vq8cuet5vjrs6sn1tiblhjb@4ax.com>`
- **References:** `<7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com> <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com> <9adc8a94-d1f9-42e0-aebf-f6b0139f60d4@v39g2000pro.googlegroups.com>`

```
On Sun, 27 Jul 2008 12:01:23 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>On Jul 28, 3:10ï¿½am, Robert <n...@e.mail> wrote:
>> On Sun, 27 Jul 2008 01:21:51 -0700 (PDT), taoxianf...@gmail.com wrote:
…[16 more quoted lines elided]…
>Warehouse Manager".

In this book (published 2000), our friends in AS/400 land refer to it as UDB/400.
http://books.google.com/books?id=lqtc0c3UjIMC&pg=PA1&lpg=PA1&dq=buy+udb&source=web&ots=7JOfYeQgsE&sig=38qWI4siZc8_hxGkSAUP_RLHZ3Y&hl=en&sa=X&oi=book_result&resnum=10&ct=result#PPP1,M1

Mainframe DB2 is written in PL/S; the non-mainframe version is written in C++. Although
functionally similar, they are different code bases. 

FWIW, I've never worked at a Unix shop that used DB2/UDB, and that included several AIX
shops. Wal-Mart and one other used Informix, the other ten used Oracle. I get the
impression DB2 users are clinging to their mainframe origins.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-27T21:14:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb974cf5-193e-44c8-86e3-41ce56c64abd@u6g2000prc.googlegroups.com>`
- **References:** `<7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com> <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com> <9adc8a94-d1f9-42e0-aebf-f6b0139f60d4@v39g2000pro.googlegroups.com> <66fq84d2u01vq8cuet5vjrs6sn1tiblhjb@4ax.com>`

```
On Jul 28, 3:42 pm, Robert <n...@e.mail> wrote:
> On Sun, 27 Jul 2008 12:01:23 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >On Jul 28, 3:10 am, Robert <n...@e.mail> wrote:
…[19 more quoted lines elided]…
> In this book (published 2000), our friends in AS/400 land refer to it as UDB/400.http://books.google.com/books?id=lqtc0c3UjIMC&pg=PA1&lpg=PA1&dq=buy+u...


"""Preface.
... One reason for that success is the system's integrated database
management system known as DB2 Universal Database for AS/400 (UDB/
400)."""

Also AS/400 is not Unix.


> Mainframe DB2 is written in PL/S; the non-mainframe version is written in C++. Although
> functionally similar, they are different code bases.
…[3 more quoted lines elided]…
> impression DB2 users are clinging to their mainframe origins.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-07-28T18:42:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<488E1325.6F0F.0085.0@efirstbank.com>`
- **References:** `<Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com> <dbe4b91c-8f69-49e9-bdbd-13b12071f2cf@w39g2000prb.googlegroups.com> <1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>`

```
>>> On 7/27/2008 at 9:10 AM, in message
<1s2p84d2u4k2lfhh72bmpe2hepb7f3n0cu@4ax.com>, Robert<no@e.mail> wrote:
> On Sun, 27 Jul 2008 01:21:51 -0700 (PDT), taoxianfeng@gmail.com wrote:
> 
…[8 more quoted lines elided]…
> changed the name to DB2. 
 
Not that it matters much, but "distributed platform" DB2 was named "IBM
DB2(R) Universal Database" (DB2 UDB) at least back as far as version 5, from
as far as I can tell.

Older names that it had were DB2/2 (for OS/2) and DB2/6000 (for RS/6000,
which I believe is the hardware that ran AIX).

Even before that (I think!) it was called OS/2 Extended Edition Database
Manager.  As far as I can tell, that was the only version (of the line from
which the current DB2 for Linux, UNIX and Windows decends) that did not have
DB2 in the name.

Anyway, as of version nine (9.1) the "Universal Database" part was dropped,
and it is not IBM DB2 for Linux, UNIX and Windows.

By the way, I have an unused version of (according to the package) Database
2 OS/2 (with DB2/2 also listed on the box) Version 1.0 if anyone wants it. 
:-)  Just kidding.  I wouldn't give it away.  Too historically important! 
:-)

Hmm, actually, here's a good link that I just found (after I wrote all of
the above):

http://wiki.ibmdatabasemag.com/index.php/DB2_History_--_A_Timeline 

So it looks like this...

1982: SQL/DS for VSE and VM released (1)
1983: DATABASE 2 (DB2) released on MVS (2)
1987: OS/2 V1.0 Extended Edition, with relational database capabilities (3)
1988: SQL/400 for release for AS/400 (4)
1993: DB2 for OS/2 V1 (DB2/2) and DB2 for AIX V1 (DB2/6000)
1995: DB2 Common Server V2, which appears to now support Windows in addition
to OS/2 and AIX (3)
1996: Not sure what happened to version 3 and 4, but apparently we are now
at DB2 Universal Database V5 (3)
1997: DB2 for OS/390 V5 (2)
1997: DB2 Universal Database for Unix, Windows and OS/2 (3)
1998: DB2 UDB for AS/400 (4)
1999: DB2 supported on Linux.  I'm assuming this is where they just started
calling it DB2 Universal Database, but that's just a guess (3)

At some point SQL/DS for VSE and VM is renamed DB2 Server for VSE and VM.
(1)

At some point the "MVS" version is renamed DB2 for z/OS (I think!).  Also
for version 8 at least, the "MVS" product was "DB2 Universal Database for
z/OS".  It looks like version 7 was "DB2 Universal Database for z/OS and
OS/390".

As of version nine (9.1), released in 2006, we now have DB2 for Linux, UNIX
and Windows (3).
As of version nine (9.1), released in 2007, we now have DB2 for z/OS.
I gave up on AS/400, iSeries.

(1) VSE and VM
(2) MVS / OS/390 / z/OS
(3) OS/2, AIX, Windows, UNIX, Linux
(4) AS/400, iSeries

Talk about confusing!  And I'm sure I have some things wrong.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-07-27T08:43:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J__ik.2763$zv7.213@flpi143.ffdc.sbc.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:l1tn841tkan6cu73ob3lq48sgju3revd21@4ax.com...
> On Sat, 26 Jul 2008 17:19:09 -0700 (PDT), taoxianfeng@gmail.com wrote:
>
…[4 more quoted lines elided]…
> split across two records. This is NOT NORMAL.

This gives me a thought ....

I have encountered similar problems when the data itself contained delimiter 
characters.

Yes, it does make you think your logic, your compliler or your utilities are 
acting naughty, when what is really happening is, "garbage in, garbage out."

Worth checking methinks.

MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-27T15:57:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xV0jk.351000$tY4.318793@fe06.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com>`

```
Have you replied yet to the question:

Does the DB2 table include any fields defined as Packed-Decimal or Binary 
(possibly COMP, COMP-3, COMP-5)?

If so, then using Line Sequential files is almost CERTAINLY not the way to go.

Line Sequential files are INTENDED for "display" data.

(Record Sequential files are FINE for binary and packed-data).

If your original data doesn't include any binary or packed data, can you tell us 
what type of field INCLUDES the X'0D" data - and what it is intended to be - as 
data?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-27T19:26:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com>`

```
On Jul 28, 12:57 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Have you replied yet to the question:
>
…[15 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

I know that Line Sequential files are for 'text' data.
And all the 0D comes from VARCHAR field(in several tables since I
tried several programs). So I guess(not very sure) the data contains
only Japanese characters and no binary data.As I said before, the
data's origin is mainframe DB2. But I can't determine the 0D exists in
the mainframe DB(since I can't access it), or is injected during the
data transportation to AIX DB2, or something else.

Then I'm unable to explain what it is intended to be - acautally my
boss said the 0D should have no essential meanings and it's probably
OK even being discarded. He said that the effect will be finally
evaluated at the test phase.

That' all guys. I just wanna have a rest now.

Thank you for all your patience and kindness.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-28T04:36:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A1cjk.142335$bC5.117339@fe07.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com>`

```
I now can guess at your problem.

If you look at:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnapj11/2.3.3

You will see that the "normal" COBOL equivalent of VARCHAR is:

   10 var.
      49 var_LEN PIC 9(4)   USAGE COMP.
      49 var_TEXT PIC X(n).

This means that the length field is stored as a bINARY field.  Therefore, a 
X"0D" would occur for a 13 byte VARCHAR field.

I don't know how you (your organization) is getting the data from the DB2 table, 
but you need to do something to EITHER convert the binary length field to 
display OR to not create (try to create) a line sequential file.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 10)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T03:07:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com>`

```
I'm sorry it's not like your imagine.

Varchar is handled with such a structure ONLY in SQL embedded
program(.sqb,etc). The field length and real content will be stored
into it when fetching a cursor or some other way.

BUT now I'm just writing a pure cobol source matching some "special"
text file.

You can do a experiment to see how is a varchar field exported(into
DEL format) - only the characters.

I can't show my data but some records contain no 0D and some have lots
of 0D spreading the whole varchar field. They are not the binary-form
field length.

On Jul 28, 1:36 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I now can guess at your problem.
>
…[66 more quoted lines elided]…
> - Show quoted text -
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-07-28T07:58:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ojjk.16538$mh5.7665@nlpi067.nbdc.sbc.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com>`

```
>I can't show my data but some records contain no 0D and some have lots
>of 0D spreading the whole varchar field. They are not the binary-form
>field length.

Well, that simpifies things. If the data contain x0D (or x0A, depending on 
any available record delimiter character settings supported) you cannot get 
it with a COBOL program treating the file as 'line sequential'. You'll have 
to find another way, period.

MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-28T16:49:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rMmjk.347471$I42.44563@fe04.news.easynews.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com>`

```
Besides the comment that Line Sequential just won't work, you really SHOULD 
contact the "owner" of the data on the mainframe.  If the data itself actually 
contains X"0D" (or any other X"0?" or X"1?" data), you should VERIFY with the 
owner that they think this is "valid" data.  Personally (especially with the 
manager's comment that these can be "ignored") I am guessing that there is a 
problem somewhere in the extraction and transfer process.  It certainly is 
POSSIBLE that this is "valid" data - but it is also possible that it is a 
symptom of another problem that needs correcting.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-29T13:01:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f78fcFa6m8pU1@mid.individual.net>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <rMmjk.347471$I42.44563@fe04.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:rMmjk.347471$I42.44563@fe04.news.easynews.com...
> Besides the comment that Line Sequential just won't work, you really 
> SHOULD contact the "owner" of the data on the mainframe.

That would be the CEO of the company, according to some recent posts in 
CLC... :-)

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T18:16:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46cb4a44-3330-4e46-bf7c-b5aa16f5e9c0@m44g2000hsc.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <rMmjk.347471$I42.44563@fe04.news.easynews.com>`

```
On Jul 29, 1:49 am, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Besides the comment that Line Sequential just won't work, you really SHOULD
> contact the "owner" of the data on the mainframe.  If the data itself actually
…[102 more quoted lines elided]…
> - Show quoted text -

I'll take your suggestion seriously. It's really necessary for me to
check the validity of the data before writing the program and
discussing with you all.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-07-28T13:25:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com>`

```

<taoxianfeng@gmail.com> wrote in message
news:a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com...

[snip]

> BUT now I'm just writing a pure cobol source matching some "special"
> text file.

> You can do a experiment to see how is a varchar field exported(into
> DEL format) - only the characters.

> I can't show my data but some records contain no 0D and some have lots
> of 0D spreading the whole varchar field.

[snip]

A bit of research (google using: site:ibm.com db2 +aix +hex)
shows that a HEX function is available (in DB2 V9) that may be
used during EXPORT to convert the characters in the VARCHAR
column to hex display. Using this function would seem to simplifiy
the problem with having control character values as data.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 12)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T18:23:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet>`

```
On Jul 29, 2:25 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> <taoxianf...@gmail.com> wrote in message
>
…[17 more quoted lines elided]…
> the problem with having control character values as data.

Well, it's really a fantastic method! All data is successfully
outputted.

There's only one more thing:
I need to import the matched data back to the table, so I'm searching
the way to convert the HEX displayed varchar column back. Would you
mind give me a bit more hint?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-28T22:19:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com>`

```
On Mon, 28 Jul 2008 18:23:18 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On Jul 29, 2:25ï¿½am, "Rick Smith" <ricksm...@mfi.net> wrote:
>> <taoxianf...@gmail.com> wrote in message
…[26 more quoted lines elided]…
>mind give me a bit more hint?

Code Page 1252 is hex

 load from filename of del modified by codepage=1252
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 14)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-28T22:28:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com>`

```
On Jul 29, 12:19 pm, Robert <n...@e.mail> wrote:
> On Mon, 28 Jul 2008 18:23:18 -0700 (PDT), taoxianf...@gmail.com wrote:
> >On Jul 29, 2:25 am, "Rick Smith" <ricksm...@mfi.net> wrote:
…[33 more quoted lines elided]…
> - Show quoted text -

The DB2 codepage is set to IBM-943 (Japanese) so a SQL2754N "cannot be
converted" error happens when trying to load data with codepage 1252.
Maybe I should change the DB codepage?
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-29T05:59:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ykyjk.6700$DJ2.1138@fe06.news.easynews.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com>`

```
<taoxianfeng@gmail.com> wrote in message 
news:71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com...
<snip>

The DB2 codepage is set to IBM-943 (Japanese) so a SQL2754N "cannot be
converted" error happens when trying to load data with codepage 1252.
Maybe I should change the DB codepage?

Is the actual mainframe data "NATIONAL" (or DBCS) data (stored in the DB2 table? 
If so, then it is CERTAINLY possible that the actual DBCS/national data includes 
X"OD" bytes within a double byte (or Unicode) data.

"Converting" (or handling) mainframe DBCS/National data via Micro Focus on AIX 
is a VERY different issue than anything that you have mentioned up to now.

If the mainframe data is NOT DBCS or National, can you find out WHY it is 
defined as "IBM-943 (Japanese)"? If it does include SOME actual Japanese data, 
can you find out if it is ALL "national" - or if it is a mixture of national and 
alphanumeric data.

If the mainframe data includes a combination of EBCDIC and DBCS (or Unicode) 
data, then I think you need to be VERY careful of your "conversion" (export) 
procedures AND you need to make certain that "conversions" in transfer to AIX 
"maintains" valid data AND that you are using the proper language (NLS and 
codepage) settings when processing the data with Micro Focus.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 16)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-29T18:28:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com>`

```
On Jul 29, 2:59 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> <taoxianf...@gmail.com> wrote in message
>
…[27 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

I just become despaired since it keeps involving more and more
questions...
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-30T17:37:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fad0cFagmb6U1@mid.individual.net>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com>`

```


<taoxianfeng@gmail.com> wrote in message 
news:51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com...
On Jul 29, 2:59 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> <taoxianf...@gmail.com> wrote in message
>
…[35 more quoted lines elided]…
> wmklein <at> ix.netcom.com

I just become despaired since it keeps involving more and more
questions...

[Pete]

I understand how you feel. I've been watching the thread, but refrained from 
comment.

1. Don't give up.
2. Think about what you have gained.

You have a lot more information than you had when you first posted and you 
have found out things that you didn't know.

Some of the information you received has been misleading, but that's normal 
on Usenet. People here have been trying hard to help, but the statement of 
the problem is not accurate. While it may be true that your x'0D' s are 
being "stripped out", to most people here that is normal behaviour for a 
Line Sequential file. (that's why it is happening).     You didn't tell us 
the file contained Japanese Language characters which could be represented 
in a number of ways, and can contain x'0D' as a matter of course.

Bill's post above is simply addressing this, and he is trying to help you. 
(Trust him, he is wise... :-))

Unfortunately, you still haven't been able to resolve your problem, and 
pressure to do so is mounting.

Rick pointed out the possibility of being able to export the data as 
character format Hex. Very useful.

So now, although it all seems very overwhelming, you are really close to a 
solution. This is not the time to quit or despair... :-)

At the moment it seems that as soon as you can reconstruct the original data 
stream from the Hex, you have solved the problem.

How hard can that be?

Robert suggested using a code page (unfortunately, he was a bit off the 
mark, but the idea was good...)

Personally, I wouldn't even attempt to change the code page for the DB; that 
is likely to upset a number of people :-).

Think some more about the Hex string. Each byte is represented by 2 hex 
symbols. If you had to, you could easily write a little COBOL routine that 
would give you the same byte in binary... Here's an example that is by no 
means definitive, but which I'm sure you can modify for your particular 
environment...

*> interface
01  two-bytes-in   pic xx.
01  one-byte-out   pic x.

*> reference data
01 hc  pic x(16) value '01234567890ABCDEF'.
01 filler redefines hc.
     12 hexchars     pic x occurs 16
                                 indexed by hc-x1.
01 hv usage comp.
     12  x0              pic s9(4) value zero.
     12  x1              pic s9(4) value 1.
     12  x2              pic s9(4) value 2.
     12  x3              pic s9(4) value 3.
     12  x4              pic s9(4) value 4.
     12  x5              pic s9(4) value 5.
     12  x6              pic s9(4) value 6.
     12  x7              pic s9(4) value 7.
     12  x8              pic s9(4) value 8.
     12  x9              pic s9(4) value 9.
     12  xA              pic s9(4) value 10.
     12  xB              pic s9(4) value 11.
     12  xC              pic s9(4) value 12.
     12  xD              pic s9(4) value 13.
     12  xE              pic s9(4) value 14.
     12  xF              pic s9(4) value 15.
01 filler redefines hv.
     12 hexvalues   pic s9(4)  comp occurs 16
                                          indexed by hv-x1.

*> work fields

01 current-byte pic x.
01 num-x pic xx.
01 num-b redefines num-x pic s9(4) comp.
01 binary-work-fields usage comp.
    12 bin-work  pic s9(4).
    12 bin-1        pic s9(4).
    12 bin-2        pic s9(4).

....

convert-hex-chars section.
chc000.
    move two-bytes-in (1:1) to current-byte
    perform get-binary
    move bin-work to bin-1
    move two-bytes-in (2:1) to current-byte
    perform get-binary
    move bin-work to bin-2
    compute num-b = (bin-1 * 16) + bin-2
    move num-x (2:1) to one-byte-out
    .
chc999.
    exit.
*>--------------------------
get-binary section.
gb000.
    set hc-x1 to 1
    search hexchars
        at end
            *> the HEX, isn't... drastic action needed...not shown here
         when current-byte = hexchars (hc-x1)
                  set hv-x1 to hc-x1 *> you might need to adjust this on 
MicroFocus
                  move hexvalue (hv-x1) to bin-work
    end-search
    .
gb999.
    exit.

This is necessarily a little unwieldy because MicroFocus COBOL (as far as I 
can ascertain) doesn't support PIC 1 for true binary (we really need to 
address 4 bits here), and that means it is necessary to fudge it in 16 bit 
fields.

If you build a little "machine" (like the above) it isn't too hard to push 
your HEX string through it and so obtain the original binary representation 
which could be anything, including National Characters, Katakana, DBCS, 
whatever. (Or even just standard ASCII)

Even if you don't go this way but find another solution, never give up 
because people are asking questions. Answer the ones you can, ignore the 
ones you can't or respond with "I don't know"... :-)

You have invested a large amount of time and effort in this.

You are way too close to a solution to despair now :-)


Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 18)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-30T00:34:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net>`

```
On Jul 30, 2:37 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <taoxianf...@gmail.com> wrote in message
>
…[191 more quoted lines elided]…
> - Show quoted text -

You gave an excellent conclusion.

I'm really a newbie and I gained a lot from this post.

I also think the HEX scalar function is very near to the solution.

I'm busy with some other business so replying a little slowly.

I will keep trying. Thank you very much.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-30T10:20:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IfXjk.339886$fz6.206173@fe08.news.easynews.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com>`

```
I just want to repeat that if you have a mixture of EBCDIC and National (DBCS or 
Unicode) data in the DB2 table on the mainframe, that you will really need a LOT 
of information to be able to "correctly" migrate this to AIX.

Question 1:
  Do you want to convert the EBCDIC data to ASCII?  If so, you may still need to 
find out which EBCDIC code page (there are more than one) is being used on the 
mainframe.  You also won't be able to "automatically" convert the data - as you 
will NOT want to use the same routine for converting the Japanese data.

Question 2:
  Is the mainframe "Japanese" data in DBCS or Unicode?  Do you want it to be in 
Unicode?  Shift-Jis,  IBM DBCS, or what format on AIX?  IBM mainframe COBOL (and 
I think - but am not certain DB2) can handle EITHER DBCS or Unicode data.  There 
are differences (some minor and some major) between these.  You will need to 
make certain that you know which format is used on the mainframe AND which 
format you are supposed to create on AIX.  Again, conversions of this data will 
need to happen "field by field" as you will NOT want to use the same conversion 
algorithms for this data as the originally EBCDIC data.

  ***

On Windows (but I am not positive it is true on AIX), Micro Focus *does* provide 
facilities for using mixed EBCDIC and IBM mainframe DBCS data "as if it were 
native/Windows" data.  This *might* be the easies method for doing your 
conversion/migration work.  HOWEVER, it is not recommended for "production" work 
on AIX.  Therefore, you would still want to convert the mainframe-style data to 
AIX data (i.e. EBCDIC -> ASCII and DBCS -> Unicode) for "production" work.

P.S.  This is NOT the type of migration that is usually given to a "Newbie" so I 
certainly can understand your frustration.  If this is an 'In-house" migration 
project, then you should be able to find in-house expertise to help you.  If 
this is something that your organization has "contracted" to do, then I think 
that someone made a commitment that they hadn't properly "sized" before bidding 
on.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 20)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-31T03:05:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fbe9aFao3kpU1@mid.individual.net>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:IfXjk.339886$fz6.206173@fe08.news.easynews.com...
>I just want to repeat that if you have a mixture of EBCDIC and National 
>(DBCS or Unicode) data in the DB2 table on the mainframe, that you will 
>really need a LOT of information to be able to "correctly" migrate this to 
>AIX.

That may not be the case, Bill. There has been no suggestion that a MIXTURE 
is in use.

Taoxianfeng said they are on a straight Japanese code page.

If the AIX machine can recognise the DBCS, it should all be fine. DBCS is 
like Unicode (inasmuch as it comes in standard "flavours"); it's a standard 
format for any platform that supports IBM's DBCS.

(I had to use it once many years ago and have never forgotten the 
experience...)

Quoting from IBM:

The IBM-932 code page (Japanese) is one example of a DBCS code page in 
which:
X'00' to X'7F' are single-byte codes
X'81' to X'9F' are double-byte introducer
X'A1' to X'DF' are single-byte codes
X'E0' to X'FC' are double-byte introducer

(No wonder the stripped out x'0D's are problematic... :-))

I think the problem is arising because the CONTAINER for the data is a LINE 
SEQUENTIAL file, which happens to use x'0D' for a special purpose.

The data is there, because when it is HEX encoded it arrives at the AIX 
machine correctly.

If the data is converted back to the original, and the AIX machine is also 
running the Japanese code page, I believe everything will work correctly.

It isn't the difference in OS that is the problem, it is the transport 
layer. (Rick's suggestion to HEX encode it solves this nicely.)


>
> Question 1:
…[4 more quoted lines elided]…
> Japanese data.

Assumes there is EBCDIC data. If it is all Japanese it is DBCS.


>
> Question 2:
>  Is the mainframe "Japanese" data in DBCS or Unicode?  Do you want it to 
> be in Unicode?

Why would that matter? He just wants it to be readable on the AIX machine. 
Once that is working, the niceties of DBCS vs Unicode could be explored as a 
separate issue. I think this is just complicating the issue.

> IBM mainframe COBOL (and I think - but am not certain DB2) can handle 
> EITHER DBCS or Unicode data.  There are differences (some minor and some 
> major) between these.  You will need to make certain that you know which 
> format is used on the mainframe AND which format you are supposed to 
> create on AIX.

Surely that is covered by the code page? We have established it is Japanese 
(DBCS on the mainframe, and the equivalent Japanese page on the AIX machine, 
presumably.)

> Again, conversions of this data will need to happen "field by field" as 
> you will NOT want to use the same conversion algorithms for this data as 
> the originally EBCDIC data.

I have no idea why you would say this... :-)?  Keep it simple.


>
>  ***
…[8 more quoted lines elided]…
>

Yes, very fair comment and right on ** IF ** we are dealing with "mixed" 
encoding AND the AIX system DOESN'T support  DBCS...

> P.S.  This is NOT the type of migration that is usually given to a 
> "Newbie" so I certainly can understand your frustration.

He has had a lot to deal with. It would be really good if this can be solved 
without complicating it any more than absolutely necessary... :-)

Given that he is using Japanese code pages (DBCS) on both systems, can you 
see any problem with him simply decoding the HEX encoded message?

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 21)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T12:27:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com>`
- **References:** `<599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net>`

```
On Thu, 31 Jul 2008 03:05:12 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[40 more quoted lines elided]…
>layer. (Rick's suggestion to HEX encode it solves this nicely.)

I think the problem is that Micro Focus does not know the input file contains DBCS codes. 
It is treating the input as single-byte US-ASCII. You tell it about the codeset using the
codecomp program to create a codeset file and the MFCODESET environment variable to tell
it to use that page at execution time. 

http://supportline.microfocus.com/supportline/documentation/books/sx22sp1/sx22indx.htm
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-31T12:22:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fcetcFb05uoU1@mid.individual.net>`
- **References:** `<599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net> <hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com...
> On Thu, 31 Jul 2008 03:05:12 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[52 more quoted lines elided]…
> It is treating the input as single-byte US-ASCII.

It certainly looks that way.

>You tell it about the codeset using the
> codecomp program to create a codeset file and the MFCODESET environment 
…[3 more quoted lines elided]…
> http://supportline.microfocus.com/supportline/documentation/books/sx22sp1/sx22indx.htm

So, are you saying Robert, that if Taoxianfeng simply sets the MFCODESET EV 
to point at the Japanese code page, at the time he runs his MF COBOL 
program, it should work? Definitely worth a try...

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 23)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T22:25:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v8b294lklakslrjhj4l2g4fj22an4b97ge@4ax.com>`
- **References:** `<71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net> <hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com> <6fcetcFb05uoU1@mid.individual.net>`

```
On Thu, 31 Jul 2008 12:22:03 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[69 more quoted lines elided]…
>program, it should work? Definitely worth a try...

Yes. Add compiler option DBCS, and pic G instead of pic X. There is also an environment
variable LANG, but it apears to be for NLS (Latin alphabet).

The manual talks about calling _CODESET to translate EBCDIC DBCS to ASCII DBCS. I'm
guessing that involves quotes, commas and other punctuation characters. If embedded 0D and
others below x'20' go away, the need for EBCDIC-ASCII translation should be evident from
viewing the output file.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-31T04:29:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adbkk.375429$I42.267291@fe04.news.easynews.com>`
- **References:** `<71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net> <hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com> <6fcetcFb05uoU1@mid.individual.net> <v8b294lklakslrjhj4l2g4fj22an4b97ge@4ax.com>`

```
FYI,
  "PIC G" (and DISPLAY-1) are still available, but certainly NOT what I would 
use for IBM mainframe "migration".

I would use PIC N and USAGE NATIONAL.

However, I would still want to see how the files are defined on the mainframe 
(either for DB2 or for COBOL).

As I read the information online at:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnsqj11/2.9.4.4

and

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/dsnugj11/2.30.2.3.9

There really are LOTS of things to know about the unloaded mainframe DB2 table. 
It appears as if the original data (GRAPHIC or VARGRAPHIC) can be either DBCS or 
Unicode.  It also appears that what the "delimiter" is (for Unloaded delimited 
files) defaults differently depending on which it is - and that the person doing 
the unload can specify what to use.

If the mainframe DB2 table includes ONLY "graphic" and "vargraphic" data (no 
"single byte") info, then if the unload specified a DBCS or Unicode delimiter, 
then the unloaded file SHOULD be able to be handled on AIX with a Micro Focus 
file in which the FD file has ONLY "PIC N" data.  If the X'0D' data is part of 
such characters, I think it MIGHT be handled correctly.  However, the MF 
documentation does seem pretty clear that it strips out all X'0D' bytes for Line 
Sequential files, so I am not at all certain this would work - unless you call 
the file RECORD sequential (rather than line sequential).

  ***

It seems to me that there needs to be a LOT of research into how the DB2 table 
and unloaded file are actually defined on the mainframe before a "good" solution 
can be done on the PC.  The copy directly  of the table would seem to allow for 
"proper" processing of the table(s) on the PC without conversion issues, but 
even that would require knowing how the table data is actually defined (DBCS, 
Unicode, whatever).
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 22)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-30T19:46:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1a36708-d950-44d5-a0af-7d96bf49a5dc@j1g2000prb.googlegroups.com>`
- **References:** `<599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net> <hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com>`

```
On 7月31日, 午前2:27, Robert <n...@e.mail> wrote:
> On Thu, 31 Jul 2008 03:05:12 +1200, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[56 more quoted lines elided]…
> - 引用テキストを表示 -

Thank you Robert.

I tried exporting MFCODESET ev directly then recompile and run the
program. But it gives nothing different.

(referencing the codeset No. from http://www.microfocus.com/000/20031001_003_tcm21-6159.pdf
, I used 0081,0939 and 9122)

So I'm trying to use the codecomp utility to build new mapping now.

However, I feel that it's all about ASCII and EBCDIC since the
document says "The Codecomp utility enables you to reconfigure the
_CODESET program for single-byte characters."
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 23)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T22:59:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qc294d3ietfn3hf9lb9ee0vpodbjl7uh2@4ax.com>`
- **References:** `<Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com> <6fbe9aFao3kpU1@mid.individual.net> <hs8194lv6og5gvrbh58kv2andqrlbneql6@4ax.com> <c1a36708-d950-44d5-a0af-7d96bf49a5dc@j1g2000prb.googlegroups.com>`

```
On Wed, 30 Jul 2008 19:46:02 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On 7?31?, ??2:27, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jul 2008 03:05:12 +1200, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[62 more quoted lines elided]…
>program. But it gives nothing different.

It appears that compiler option NLS is required to use a codeset at execution time. I
thought it was DBCS, but now see that applies to DBCS in source code at compile time, not
in data files at execution time.  

Also, define the record with DISPLAY-1 PIC G, which tells it to allocate two bytes per
character.

>(referencing the codeset No. from http://www.microfocus.com/000/20031001_003_tcm21-6159.pdf
>, I used 0081,0939 and 9122)
…[5 more quoted lines elided]…
>_CODESET program for single-byte characters."

I would first try to get rid of control characters less than x'20'. If strings in the
output look like valid katakana, THEN deal with ASCII-EBCDIC. If strings are not bounded
by quotes, that would be a sure sign you need translation, the bounding character must be
an untranslated EBCDIC quote.

If you DO need to convert, see 8.11.4 function 4 here:
http://supportline.microfocus.com/supportline/documentation/books/sx22sp1/prnals.htm#s024
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 20)_

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-30T18:43:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7f08813-335f-4c76-81fe-8b017bdbafae@26g2000hsk.googlegroups.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com> <IfXjk.339886$fz6.206173@fe08.news.easynews.com>`

```
On 7月30日, 午後7:20, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I just want to repeat that if you have a mixture of EBCDIC and National (DBCS or
> Unicode) data in the DB2 table on the mainframe, that you will really need a LOT
…[247 more quoted lines elided]…
> - 引用テキストを表示 -

Frankly speaking , I can't anwser your questions since I don't have
much experience on both mainframe and AIX.

I can only agree that this problem is not well "sized" before
commencing. It's too ridiculous and confidential to be talked about
here. Just forget it.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-07-30T22:34:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6faudlF7r1lrU1@mid.individual.net>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com>`

```


<taoxianfeng@gmail.com> wrote in message 
news:7cd6c4c1-3929-418e-b211-9c7e86abd8f3@a3g2000prm.googlegroups.com...
On Jul 30, 2:37 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <taoxianf...@gmail.com> wrote in message
>
…[203 more quoted lines elided]…
> - Show quoted text -

You gave an excellent conclusion.

I'm really a newbie and I gained a lot from this post.

I also think the HEX scalar function is very near to the solution.

I'm busy with some other business so replying a little slowly.

I will keep trying. Thank you very much.

[Pete]

You are very welcome.... :-)
(I was a newbie myself once...)

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 18)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-30T23:05:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com>`
- **References:** `<a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net>`

```
On Wed, 30 Jul 2008 17:37:20 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>Think some more about the Hex string. Each byte is represented by 2 hex 
>symbols. If you had to, you could easily write a little COBOL routine that 
…[33 more quoted lines elided]…
>

>get-binary section.
>gb000.
…[8 more quoted lines elided]…
>    end-search

There is a much simpler way to convert hex digits:

INSPECT current-byte CONVERTING 
  '0123456789ABCDEF' TO
X'000102030405060708090A0B0C0D0E0F'
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-08-01T04:10:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fe6fnFb7tatU1@mid.individual.net>`
- **References:** `<a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com...
> On Wed, 30 Jul 2008 17:37:20 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[55 more quoted lines elided]…
> X'000102030405060708090A0B0C0D0E0F'

Cool!

Will it work on ANY platform...?

Pete.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 20)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-31T12:24:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j5t394p8198810n80ihric85fm4ffffar4@4ax.com>`
- **References:** `<i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com> <6fe6fnFb7tatU1@mid.individual.net>`

```
On Fri, 1 Aug 2008 04:10:30 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[63 more quoted lines elided]…
>Will it work on ANY platform...?

INSPECT .. CONVERTING and hex literals are in the 2002 Standard.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 21)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-07-31T17:30:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4891F6AF.6F0F.0085.0@efirstbank.com>`
- **References:** `<i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com> <6fe6fnFb7tatU1@mid.individual.net> <j5t394p8198810n80ihric85fm4ffffar4@4ax.com>`

```
>>> On 7/31/2008 at 11:24 AM, in message
<j5t394p8198810n80ihric85fm4ffffar4@4ax.com>, Robert<no@e.mail> wrote:
> 
> INSPECT .. CONVERTING and hex literals are in the 2002 Standard. 

I'm guessing it should work on any Cobol that supports the 1985 standard. 
For instance, Cobol for VSE.  Works like a charm.  Wish I had thought of it!
 :-)

Frank
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file usingmicrofocus se

_(reply depth: 22)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-07-31T17:36:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4891F802.6F0F.0085.0@efirstbank.com>`
- **References:** `<i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com> <Ykyjk.6700$DJ2.1138@fe06.news.easynews.com> <51a1467d-8e2d-41ab-926b-6732b313957f@w7g2000hsa.googlegroups.com> <6fad0cFagmb6U1@mid.individual.net> <o7e29413ea3ou9hjb0lq59msdkdkef2s9p@4ax.com> <6fe6fnFb7tatU1@mid.individual.net> <j5t394p8198810n80ihric85fm4ffffar4@4ax.com> <4891F6AF.6F0F.0085.0@efirstbank.com>`

```
>>> On 7/31/2008 at 5:30 PM, in message
<4891F6AF.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick<Frank.Swarbrick@efirstbank.com> wrote:
>>>> On 7/31/2008 at 11:24 AM, in message
> <j5t394p8198810n80ihric85fm4ffffar4@4ax.com>, Robert<no@e.mail> wrote:
…[7 more quoted lines elided]…
>  :-)

By the way, on VSE at least this appears to be amazingly efficient.

45E0 D136               BAL  14,310(0,13)            TGT TEST INFORMATION
AREA +10                  
               GN=12    EQU  *                                              
                       
DC4F 9000 A018          TR   0(80,9),24(10)          MY-STRING              
          PGMLIT AT +20
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-29T08:05:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n4u84lc46b7f4d2fi0j2netn5759sa51s@4ax.com>`
- **References:** `<xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com> <71e6da43-8789-4de7-8fc7-54f14fb69dbf@34g2000hsh.googlegroups.com>`

```
On Mon, 28 Jul 2008 22:28:35 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On Jul 29, 12:19ï¿½pm, Robert <n...@e.mail> wrote:
>> On Mon, 28 Jul 2008 18:23:18 -0700 (PDT), taoxianf...@gmail.com wrote:
…[38 more quoted lines elided]…
>Maybe I should change the DB codepage?

My mistake. Code page 1252 converts only to US-ASCII. Japanese explains why you couldn't
show the data here.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 14)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-29T00:07:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f45eb51-d111-4b11-8c7b-7eb9698956b4@z72g2000hsb.googlegroups.com>`
- **References:** `<ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com> <4f379b88-5332-46f9-b9f6-5506401ef969@q28g2000prh.googlegroups.com> <A1cjk.142335$bC5.117339@fe07.news.easynews.com> <a9c0db14-398e-47ef-a705-59e8b9657ba1@j22g2000hsf.googlegroups.com> <i8Wdnc2tRI1inRPVnZ2dnUVZ_qjinZ2d@posted.mid-floridainternet> <599eaea0-9c7c-49d9-8f9f-666551ac81fe@m36g2000hse.googlegroups.com> <qv2t84d3nmiaba75gqo5okuscfv3vvk30d@4ax.com>`

```
On Jul 29, 3:19 pm, Robert <n...@e.mail> wrote:
> On Mon, 28 Jul 2008 18:23:18 -0700 (PDT), taoxianf...@gmail.com wrote:
> >On Jul 29, 2:25 am, "Rick Smith" <ricksm...@mfi.net> wrote:
…[31 more quoted lines elided]…
>  load from filename of del modified by codepage=1252

Do you think that he is running on Windows now ??
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-27T23:09:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oggq84t2hj17pakrgddm22miuq4dpgkivq@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <Kdhik.100238$o12.10431@fe03.news.easynews.com> <c6cb331a-8e7d-493a-8d3b-872e94b2c6fd@j7g2000prm.googlegroups.com> <7Mwik.295652$3p2.60961@fe10.news.easynews.com> <a1910703-f28b-44d8-a0b0-94e10617dbbe@k36g2000pri.googlegroups.com> <Q%Jik.317256$Ev5.117862@fe09.news.easynews.com> <ec1fbab6-3052-401e-92df-087337992ab8@i20g2000prf.googlegroups.com> <xV0jk.351000$tY4.318793@fe06.news.easynews.com>`

```
On Sun, 27 Jul 2008 15:57:17 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Have you replied yet to the question:
>
>Does the DB2 table include any fields defined as Packed-Decimal or Binary 
>(possibly COMP, COMP-3, COMP-5)?

There are no such DB2 types. The corresponding types are INTEGER and DECIMAL. They would
be in display format when exported by any utility. 

>If your original data doesn't include any binary or packed data, can you tell us 
>what type of field INCLUDES the X'0D" data - and what it is intended to be - as 
>data?

Taoxianfeng's 0D and 0A are in strings -- database type VARCHAR, Cobol PIC X. We know that
because he said "I have to count the quotation marks to determine if a record is
divided into several lines and combine them together." Strings are bounded by quotes;
numbers aren't. He is saying there was a 0A in a string.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
