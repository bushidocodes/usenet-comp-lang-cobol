[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# error msg: invalid type cast

_4 messages · 3 participants · 2003-03_

---

### error msg: invalid type cast

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-03-07T10:10:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AD2aa.6338$KJ3.928071@news20.bellglobal.com>`

```
Hi

In the final of my cobol prgram have below procedure function(which was
being called several times before):
097600 Z000-DONE.
09760000
097700     GOBACK
09770000
097800     .
09780000

the compiler(oipen-cobol) choked on this :
parser.y:3570: invalid type cast from `GOBACK:'
Aborted (core dumped)

what could be possible reason ?

thanks
Paul
```

#### ↳ Re: error msg: invalid type cast

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-03-07T10:47:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea3aa.6354$KJ3.931726@news20.bellglobal.com>`
- **References:** `<AD2aa.6338$KJ3.928071@news20.bellglobal.com>`

```
sorry but rechecked the error caused by this line
066600     MOVE length of csc              TO CSC-cc-length
06660000

"Paul" <paulhbliu@hotmail.com> wrote in message
news:AD2aa.6338$KJ3.928071@news20.bellglobal.com...
> Hi
>
…[18 more quoted lines elided]…
>
```

#### ↳ Re: error msg: invalid type cast

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-08T07:29:22+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4aoj5$14r$1@aklobs.kc.net.nz>`
- **References:** `<AD2aa.6338$KJ3.928071@news20.bellglobal.com>`

```
Paul wrote:

> the compiler(oipen-cobol) choked on this :
> parser.y:3570: invalid type cast from `GOBACK:'
> Aborted (core dumped)
> 
> what could be possible reason ?

GOBACK is not part of the Cobol standard that open-cobol is being written 
to.  It is an IBM thing that some compilers support as an extension.  

Use STOP RUN or EXIT PROGRAM as appropriate.
```

#### ↳ Re: error msg: invalid type cast

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-07T19:38:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E68F5B6.25BEB707@shaw.ca>`
- **References:** `<AD2aa.6338$KJ3.928071@news20.bellglobal.com>`

```


Paul wrote:

> Hi
>
…[16 more quoted lines elided]…
> Paul

Paul,

This is not answering your query but merely making comment on your use of
line numbers. Consider this in the light of your circumstances. The
compiler you are using may DEMAND that you have line numbers, or it may
well be an Installation Standard. Further, the compiler may list errors
quoting the line number ? Chances are though, with a PC-based compiler that
you can click on the error message which will immediately take you to the
offending code.

I'm guessing you are fairly new to COBOL so a little history. Back when
Noah was still hewing the wood for his Ark, COBOL source was written on
pads printed with the A and B areas etc. The information on the coding pads
was keypunched on to 80 column cards. (In my initial installation, paper
tape). There were no fancy VDUs, CRTs or Screens back in ye olden dayse.
The next phase was key to (magnetic) tape, swiftly followed by key to Disk
and finally our current situation - text editors with screens.

So back then Columns 1 - 6 were used as a sequencing line. A fairly common
practice was to include the Program-id in Columns 73-80. So your actual
code was 7 - 72, (7 being used for "D"., "/", "*"). On the sequence line, a
technique was to increment line numbers in unitsl of 10 - if you wanted to
subsequently add additional code then after Line 000100 you could add
000101, 000102 etc.

Now I note from your code you are at line 096700 - indicating that
mentally, you have probably 'segmented' the number breaks into logical
coding units. That was also a common practice, also tied in with
Segmentation - a feature which is no longer important as we have so much
more memory to process an individual program..

The really important thing back in Noah's time was that some poor sod could
be carrying a huge box of cards, (let's say for *two* programs), from one
room to another, trips, going ass over apex and the cards are spewed across
the floor. Agony, agony ! All was not lost - the cards were gathered
together and put through a card sorter which put them back into line
sequence by program-id.

Comments above may be irrelevant to your situation. If you *can* drop the
line numbers - life may well be simpler.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
