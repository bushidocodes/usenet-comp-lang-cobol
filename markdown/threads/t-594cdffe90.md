[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# All X'0D' lost during reading line sequential file using microfocus se

_11 messages · 6 participants · 2008-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-24T23:05:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com>`

```
On Thu, 24 Jul 2008 18:34:40 -0700 (PDT), taoxianfeng@gmail.com wrote:

>I don't agree.Isn't line sequential file delimited by X'0A'?

The operating system, not Cobol, specifies the line terminator. AIX and other Unix use
x'0D'. Old Macs (OS9) used 0A. Windows uses 0D0A.

A FILE is delimited by its size (in the directory), not by a character. If your textbook
says a file is terminated by 0A or 1A, it is 25 years out of date.
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-24T23:27:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eb452c1-c6bd-4259-87c5-fbdd9c4f63b9@z11g2000prl.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com>`

```
On Jul 25, 1:05 pm, Robert <n...@e.mail> wrote:
> On Thu, 24 Jul 2008 18:34:40 -0700 (PDT), taoxianf...@gmail.com wrote:
> >I don't agree.Isn't line sequential file delimited by X'0A'?
…[5 more quoted lines elided]…
> says a file is terminated by 0A or 1A, it is 25 years out of date.

Well...seems I failed to address it clearly.Let's read MY code:

     SELECT INFILE1
     ORGANIZATION IS LINE SEQUENTIAL
     ASSIGN TO EXTERNAL INFILE1.

     FD INFILE1
     DATA RECORD IS IN-REC1
     RECORDING MODE V
     RECORD IS VARYING IN SIZE FROM 1 TO 5000
     DEPENDING ON WK-INREC1-LEN
     BLOCK CONTAINS 0.
     01  IN-REC1                      PIC X(5000).
…………
      01  WK-INREC1-LEN               PIC  9(008).


1. The RECORD LENGTH will be stored into the WK-INREC1-LEN variable
automatically when executing "READ INFILE1" each time. And, believe
or
not, it's decided by X'0A' like that(the input read counter also
proves it):

1 dot for 1 byte;0D for 1 byte
......0D.....0A       (record length:12)
...0D......0D....0A   (record length:14)


I know the rest of IN-REC1 is filled by space (or nothing if using
SPACEFILL=OFF); I also know the method of searching for the 1st non-
space reading from right to left. BUT I DON'T NEED THEM since I have
no problem about the length of each record.


2.The doc I referred to is saying "The record delimiter, which is the
line feed (x"0A") character". I didn't mean file delimiter(EOF,X'1A'
or something else) either.


I'm just talking about RECORD DELIMITER or LINE DELIMITER and
doubting
your "AIX and other Unix use x'0D'".


3.Take the example again, my ESSENTIAL QUESTION is ALL X'0D' WERE
LOST
LIKE THIS:
input file:
......0D.....0A
...0D......0D....0A


output file:
...........0A
.............0A


IF, the record is delimited with X'0D' as you said, then how can I
get
it in the output file since it exists in the input file?
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-25T19:11:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42nk84lcgufvm6iimkg6724066o3tceeuf@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <8eb452c1-c6bd-4259-87c5-fbdd9c4f63b9@z11g2000prl.googlegroups.com>`

```
On Thu, 24 Jul 2008 23:27:52 -0700 (PDT), taoxianfeng@gmail.com wrote:

>On Jul 25, 1:05ï¿½pm, Robert <n...@e.mail> wrote:
>> On Thu, 24 Jul 2008 18:34:40 -0700 (PDT), taoxianf...@gmail.com wrote:
…[22 more quoted lines elided]…
>      01  WK-INREC1-LEN               PIC  9(008).

Most of those FD clauses are superfluous for LINE SEQUENTIAL. You should have written
FD INFILE1 RECORD VARYING FROM 1 TO 5000 DEPENDING ON WK-INREC1-LEN.

BLOCK CONTAINS 0 is a silly mainframeism.

>1. The RECORD LENGTH will be stored into the WK-INREC1-LEN variable
>automatically when executing "READ INFILE1" each time. And, believe
…[6 more quoted lines elided]…
>...0D......0D....0A   (record length:14)

>I know the rest of IN-REC1 is filled by space (or nothing if using
>SPACEFILL=OFF); I also know the method of searching for the 1st non-
>space reading from right to left. BUT I DON'T NEED THEM since I have
>no problem about the length of each record.

I'm happy to see you took Richard's suggestion.

>2.The doc I referred to is saying "The record delimiter, which is the
>line feed (x"0A") character". I didn't mean file delimiter(EOF,X'1A'
…[5 more quoted lines elided]…
>your "AIX and other Unix use x'0D'".

You are correct; I got them backwards. 0A is Unix, 0D is Mac.

>3.Take the example again, my ESSENTIAL QUESTION is ALL X'0D' WERE
>LOST
…[13 more quoted lines elided]…
>it in the output file since it exists in the input file?

The reasons are:

1. Characters less than x'20' (space) are Control Characters, not data. 
    They are instructions to the file system. 
2. Due to non-standardization, most file systems are generalized to handle formats from
other operating systems. Most Unix programs, with the notable exception of vi, can read
Windows files terminated by 0D0A. Most Windows programs can read Unix-style files
terminated by 0A. 

The discarding of your 0Ds is a side-effect of that generalization. 

This assignment appears to be a 'trick question' to teach you that different operating
systems use different standards. 

Now let's look at solutions. Bill Klein showed how to specialize the Micro Focus file
system to recognize only 0A. That's specific to Micro Focus, not Cobol. A Unix flavored
solution would be to run the input file through the 'tr' program before piping it into
your Cobol program, like this:

cat INFILE1 | tr "\r| "\v" | yourcobol | tr "\v" "\r" > OUTFILE1

Confusing, right? It is translating 0D (Ctrl-M = return) into 0B (Ctrl-K = vertical tab)
before your program and translating it back after. 

My suggestion to parse lines yourself, recognizing only 0A, is pure Cobol. It will work
with any compiler, on any machine.  To handle the last sector on Micro Focus,

1. Initialize the record area to low-values (binary zeros)
2. Read 
3. If return-code - '92'   *> short record
       remember you are at end of file
      search backward for the first non-low-value to get sector length
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** taoxianfeng@gmail.com
- **Date:** 2008-07-25T18:49:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83ad9761-5cae-4ed1-b1ee-d3d1e83af30e@j1g2000prb.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <8eb452c1-c6bd-4259-87c5-fbdd9c4f63b9@z11g2000prl.googlegroups.com> <42nk84lcgufvm6iimkg6724066o3tceeuf@4ax.com>`

```
On Jul 26, 9:11 am, Robert <n...@e.mail> wrote:
> On Thu, 24 Jul 2008 23:27:52 -0700 (PDT), taoxianf...@gmail.com wrote:
> >On Jul 25, 1:05 pm, Robert <n...@e.mail> wrote:
…[110 more quoted lines elided]…
> - Show quoted text -


I have thought of transforming the data with shell at the beginning of
this assignment. But as I said before, I'm restricted to handle it
with in the cobol source. Maybe I should try to persuade my boss since
it would be easier with some shell script.

About parsing the line by myself, I agree that it's a "simple and
stupid" approach which fit for most situations. I will take this.

Thank you very much.
```

#### ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-07-25T15:42:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6euajhF8v6jrU2@mid.individual.net>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com>`

```
In article <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com>,
	Robert <no@e.mail> writes:
> On Thu, 24 Jul 2008 18:34:40 -0700 (PDT), taoxianfeng@gmail.com wrote:
> 
…[3 more quoted lines elided]…
> x'0D'. Old Macs (OS9) used 0A. Windows uses 0D0A.

Ummm...   No...  Unix has always used 0x0A and I would be very surprised if
AIX used anything different.  

> 
> A FILE is delimited by its size (in the directory), not by a character. If your textbook
> says a file is terminated by 0A or 1A, it is 25 years out of date.

That would depend on a number of things primary of which would be the OS.
Windows still supports FAT and FAT had two differnt kinds of text files.
One delimited by size and one that ended upon the reaching a ^Z.  There 
was no way I am aware of to determine which method a file used without
examining the file.  This caused a lot of headaches for people writing
file transfer software as using the wrong method usually reulted in
garbage on the end of the file.

bill
```

##### ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-25T21:22:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net>`

```
On 25 Jul 2008 15:42:42 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>In article <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com>,
>	Robert <no@e.mail> writes:
…[20 more quoted lines elided]…
>garbage on the end of the file.

1A ceased marking end of file with MSDOS 2.0, 25 years ago. Ctrl-Z now means Undo under
Windows and Suspend Task under Unix.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-07-26T13:47:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f0o6nF979ieU1@mid.individual.net>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net> <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>`

```
In article <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>,
	Robert <no@e.mail> writes:
> On 25 Jul 2008 15:42:42 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:
> 
…[24 more quoted lines elided]…
> 1A ceased marking end of file with MSDOS 2.0, 25 years ago. 

Hardly.  Ity is not a part of DOS, it is a part of FAT and that is till
with us and probably will be for quite some time still.

>                                                              Ctrl-Z now means Undo under
> Windows and Suspend Task under Unix. 

That is just what certain applications do with it.  Undo is not a Windows
command, it is something the various editors understand.  And You Unix
example is totally dependant on the shell in use as some of them do not
support job control at all.

Try this experiment!

On your Windows Box open a window for command.com.
type "COPY CON: JUNK"
type in a few lines of text.
at some point, type ^Z (that's the control key and the letter "Z").
hit return.
Notice you are back to prompt and you now have the file JUNK containing
what you typed.
Again, this is behavior of the terminal driver but basicly it is
that driver interpreting the ^Z as EOF on CON: and terminating the copy.
I do not expect this behavior to ever go away in the MS world as long
as we have keyboards for input!!

bill
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-26T11:41:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u5im84d8rkk8mfioccqtv8iuklp7uvn2nb@4ax.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net> <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com> <6f0o6nF979ieU1@mid.individual.net>`

```
On 26 Jul 2008 13:47:04 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>In article <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>,
>	Robert <no@e.mail> writes:
>> On 25 Jul 2008 15:42:42 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

>> 1A ceased marking end of file with MSDOS 2.0, 25 years ago. 
>
…[19 more quoted lines elided]…
>what you typed.

I did that, then looked at the file with a hex editor. There wasn't a 1A at the end. I
changed one of the characters in the middle to 1A, saved it, looked at it, 1A was still in
the middle of the line. Then I copied it and looked at the copy. 1A was still in the
middle and there was stuff after it. If 1A designated end of file, the stuff after it
would be missing. However, 'type junk' and 'copy junk con' DID terminate on the 1A.

I brought up a Unix shell -- ch -- under command.com.  'cat junk' DID stop on the 1A, but
vi showed ^Z and cp copied the stuff following and 'wc -c junk' counted all.  More
baffling, 'cat junk >junk1' copied the 1A and the stuff following.

It seems 1A means end of file on the console, not on disk files.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 5)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-07-26T11:55:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WHIik.5827$np7.1707@flpi149.ffdc.sbc.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net> <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com> <6f0o6nF979ieU1@mid.individual.net> <u5im84d8rkk8mfioccqtv8iuklp7uvn2nb@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:u5im84d8rkk8mfioccqtv8iuklp7uvn2nb@4ax.com...
> On 26 Jul 2008 13:47:04 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

> It seems [hex] 1A means end of file on the console, not on disk files.

It means end of file only to an application which wants it to mean end of 
file.

To many ancient applications, x'1A' does mean end of file... it started with 
applications first written for the CP/M operating system and early MS-DOS 
applications which DID use x'1A' as an end-of-file marker. I think that 
stopped with MS-DOS 2.0, but some applications still retain the logic of 
"x'1A'=EOF"

(Remember using EDLIN? you could either type Ctrl+Z or use one of the 
function keys (F6?) which did the same thing.)

MCM
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

_(reply depth: 6)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-07-26T14:10:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67e744b1-3af9-4083-87e8-6a88e6b1f5ce@w1g2000prk.googlegroups.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <a6d770cd-88cb-4091-8674-8f2d5956e362@u12g2000prd.googlegroups.com> <dcff421c-6e9d-48c7-8b3a-0d7f9d6fe0bd@j33g2000pri.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net> <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com> <6f0o6nF979ieU1@mid.individual.net> <u5im84d8rkk8mfioccqtv8iuklp7uvn2nb@4ax.com> <WHIik.5827$np7.1707@flpi149.ffdc.sbc.com>`

```
On Jul 27, 4:55 am, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[15 more quoted lines elided]…
> function keys (F6?) which did the same thing.)

CP/M 1.x to 2.x files only held the end of file as a sector number so
all file sizes were multiples of 128 bytes. Applications, such as text
editors filled the last sector beyond the actual data with 0x1A as a
convention.

MS-DOS, even 1.0, did have the file size in bytes but many
applications were converted from CP/M, or had versions for CP/M, and
still used 0x1A. Even edlin was originally written for CP/M.
```

###### ↳ ↳ ↳ Re: All X'0D' lost during reading line sequential file using microfocus se

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-26T14:04:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6fat8$mal$1@reader1.panix.com>`
- **References:** `<75979a92-6155-4583-9cf4-c80425d1b015@v39g2000pro.googlegroups.com> <e5ji84te3em3ejs7bi75271mgekufiu8ri@4ax.com> <6euajhF8v6jrU2@mid.individual.net> <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>`

```
In article <5f2l849u1mjm8b5aguavl6gjpluiuftn39@4ax.com>,
Robert  <no@e.mail> wrote:
>On 25 Jul 2008 15:42:42 GMT, billg999@cs.uofs.edu (Bill Gunshannon) wrote:

[snip]

>>Windows still supports FAT and FAT had two differnt kinds of text files.
>>One delimited by size and one that ended upon the reaching a ^Z.  There 
…[7 more quoted lines elided]…
>Windows and Suspend Task under Unix. 

Mr Wagner, here's a little experiment you might want to try on a Windows 
machine:

Start ==> Run ==> cmd
copy con hexfile
this is a test <== press Enter key
^Z <== control-Z

... and see how Windows handles what you assert is an Undo.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
