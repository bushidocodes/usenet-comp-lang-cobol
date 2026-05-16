[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Erroneous results in COMPUTE and MOVE

_35 messages · 11 participants · 2006-03_

---

### Erroneous results in COMPUTE and MOVE

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-06T14:07:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```
I will appreciate if anyone can help me. I have done many exhauting
tests, read a lot, but without success. When COMPUTE and MOVE, I am
getting unexpected results. For example, I am not getting this result:
91.47 * 100 = 9147. Following, more details. Thanks in advance.

 FD FCBTEST
     LABEL RECORD STANDARD.
  01 RECORD-FCBTEST.
     02 T1			PIC X(3).
     02 N1			PIC 99V99.

 FD 1CBTEST
     LABEL RECORD STANDARD.
 01 RECORD-1CBTEST.
     02 N2			PIC 99.99.

 WORKING-STORAGE SECTION.

 77 N3			PIC 99V99 VALUE ZEROES.
 ................................................
 FORMAT-1CBTEST.
     COMPUTE N3 = N1 * 100.
     MOVE N3 TO N2
     WRITE RECORD-1CBTEST.
................................................
```

#### ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-06T14:20:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141683610.426592.222920@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```

hmitchell@cc.tt wrote:
>. For example, I am not getting this result:
> 91.47 * 100 = 9147. Following, more details. Thanks in advance.
>
>  77 N3			PIC 99V99 VALUE ZEROES.

This Picture of the field specifes that it is to have at most 2 digits
in the number part and two digits in the decimal part. Thus the value
that this feld can hold is between 00.00 and 99.99.

I would expect your result to be 47.00.

You may want to try other Pictures to see what other results you will
get from them.
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-07T05:25:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141737952.736672.38780@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com>`

```
Dear Richard,
Thanks for the answer but, I made a mistake with the details. The
following details replace what I sent before. Please notice N2. The
problem still persist. Thanks in advance for your help.

FD FCBTEST
     LABEL RECORD STANDARD.
  01 RECORD-FCBTEST.
     02 T1                      PIC X(3).
     02 N1                      PIC 99V99.


 FD 1CBTEST
     LABEL RECORD STANDARD.
 01 RECORD-1CBTEST.
     02 N2                      PIC 9999.


 WORKING-STORAGE SECTION.


 77 N3                  PIC 99V99 VALUE ZEROES.
 ................................................
 FORMAT-1CBTEST.
     COMPUTE N3 = N1 * 100.
     MOVE N3 TO N2
     WRITE RECORD-1CBTEST.
................................................
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-07T13:29:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com>`

```
On 7 Mar 2006 05:25:52 -0800, hmitchell@cc.tt wrote:

>Thanks for the answer but, I made a mistake with the details. The
>following details replace what I sent before. Please notice N2. The
>problem still persist. Thanks in advance for your help.

N2 isn't your problem - the result will be truncated when it's
calculated in N3. Give that four digits before the sign and it will
work.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 4)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-07T13:31:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<to2r02ldl6ipp8n0kmh20ti84rkdtebied@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`

```
On Tue, 07 Mar 2006 13:29:54 +0000, Ian Dalziel
<iandalziel@lineone.net> wrote:

>Give that four digits before the sign

Sign schmign. Point.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 4)_

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-03-07T09:52:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5afbe$440d9d35$453d8f8b$24523@FUSE.NET>`
- **In-Reply-To:** `<dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`

```
Ian Dalziel wrote:
> On 7 Mar 2006 05:25:52 -0800, hmitchell@cc.tt wrote:
> 
…[8 more quoted lines elided]…
> work.

And Mr Dalziel, remember that when you graduate to using
decimal positions as your multiplier that the "rounded"
tag is very important to get desired results.

Bob.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2006-03-07T10:02:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b368$440d9fa6$453d8f8b$24987@FUSE.NET>`
- **In-Reply-To:** `<5afbe$440d9d35$453d8f8b$24523@FUSE.NET>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <5afbe$440d9d35$453d8f8b$24523@FUSE.NET>`

```
Bob Iles wrote:
> Ian Dalziel wrote:
> 
…[18 more quoted lines elided]…
> Bob.
Sorry, Should have been addressed to hmitchell@cc.tt
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-07T16:45:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s3er02dlmkscn14bpkum9h2unfj78ic43d@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <5afbe$440d9d35$453d8f8b$24523@FUSE.NET>`

```
On Tue, 07 Mar 2006 09:52:27 -0500, Bob Iles <bobi@mikal.com> wrote:

>Ian Dalziel wrote:
>> On 7 Mar 2006 05:25:52 -0800, hmitchell@cc.tt wrote:
…[14 more quoted lines elided]…
>

Kind of depends whether you need the answer rounded or not, doesn't
it?
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 4)_

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-07T07:14:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141744476.490567.164950@p10g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com>`

```
Dear Ian,
I have tried many combinations without success. This is only a key
piece of a bigger project. I do not know what to do. What I have up to
now is:
The FCBTEST file has one (1) record as: ABC91.47
As a result the 1CBTEST file got two (2) records, which are totally
wrong as: 9244 and 0000.
1st. I have to have one (1) record and
2nd. the accurate figure should be 9147.

I know when I change the N1 PIC 999V99, the 1CBTEST file gets one (1)
record but with another wrong number as: 2447

 FD FCBTEST
     LABEL RECORD STANDARD.
  01 RECORD-FCBTEST.
     02 T1			PIC X(3).
     02 N1			PIC 99V99.

 FD 1CBTEST
     LABEL RECORD STANDARD.
 01 RECORD-1CBTEST.
     02 N2			PIC 9999.

 WORKING-STORAGE SECTION.

 77 N3			PIC 9999 VALUE ZEROES.
....................................................
 FORMAT-1CBTEST.
     COMPUTE N3 = N1 * 100.
     MOVE N3 TO N2
     WRITE RECORD-1CBTEST.
....................................................
I will appreciate your help. I did not understand when you say: "Give
that four digits before the sign and it will work". Can you write it
for me?
Many thanks in advance for your help.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-07T08:26:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h99r02hkm7t5qh7m0b0394a78jqumcf7u7@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com>`

```
On 7 Mar 2006 07:14:36 -0800, hmitchell@cc.tt wrote:

>The FCBTEST file has one (1) record as: ABC91.47

...

> FD FCBTEST
>     LABEL RECORD STANDARD.
>  01 RECORD-FCBTEST.
>     02 T1			PIC X(3).
>     02 N1			PIC 99V99.

The picture element "V" is an implied decimal place.   It isn't really
taking up a spot in your input, it only tells your code that your
number is 90 + 1 + .4 + .07 for its manipulations.

Were you given the input format (that is common for CoBOL
programmers), or did you create it to test your code?
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 6)_

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-07T07:38:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141745926.456299.271450@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<h99r02hkm7t5qh7m0b0394a78jqumcf7u7@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com> <h99r02hkm7t5qh7m0b0394a78jqumcf7u7@4ax.com>`

```
Dear Howard,
I created it to test the code for a greater project. This is a key
issue.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-07T08:51:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fiar02l7cj2dpuimqrrnutsfqbdkkd12du@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com> <h99r02hkm7t5qh7m0b0394a78jqumcf7u7@4ax.com> <1141745926.456299.271450@i40g2000cwc.googlegroups.com>`

```
On 7 Mar 2006 07:38:46 -0800, hmitchell@cc.tt wrote:

>Dear Howard,
>I created it to test the code for a greater project. This is a key
>issue.

Will the greater project need data with a hard-coded decimal?    Will
that decimal point always be in the came column of your input?

If it moves around, you will want to use the NUMVAL function.   If it
is always the same spot, you will want to read around it, and combine
both sides of the number by hand.   You will want to do arithmetic
with the implied decimal, not with the hard-coded decimal.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-07T15:50:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duka3t$3ma$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com>`

```
In article <1141744476.490567.164950@p10g2000cwp.googlegroups.com>,
 <hmitchell@cc.tt> wrote:
>Dear Ian,
>I have tried many combinations without success.

Try posting a few here... just so that other's don't duplicate your 
efforts, you know.

[snip]

>I did not understand when you say: "Give
>that four digits before the sign and it will work".

Find where the sign is in 'that' and put four digits before (to the left 
of) it... although you might find this advice to be more helpful were you 
to substitute 'decimal' for 'sign'.

>Can you write it
>for me?

I'm sure he could.  Can you write him a check of sufficient size to retain 
his services?

If not... please do your own homework.

DD
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 6)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-07T16:47:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38er029s8p4f00tuuqs90ab3cgjvmhnkbf@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com> <duka3t$3ma$1@reader2.panix.com>`

```
On Tue, 7 Mar 2006 15:50:22 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <1141744476.490567.164950@p10g2000cwp.googlegroups.com>,
> <hmitchell@cc.tt> wrote:
…[14 more quoted lines elided]…
>

I did, I did - three nanoseconds after I hit "enter"!
:-)
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-07T17:05:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dukeh7$rtu$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com> <duka3t$3ma$1@reader2.panix.com> <38er029s8p4f00tuuqs90ab3cgjvmhnkbf@4ax.com>`

```
In article <38er029s8p4f00tuuqs90ab3cgjvmhnkbf@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On Tue, 7 Mar 2006 15:50:22 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <1141744476.490567.164950@p10g2000cwp.googlegroups.com>,
>> <hmitchell@cc.tt> wrote:

[snip]

>>>I did not understand when you say: "Give
>>>that four digits before the sign and it will work".
…[7 more quoted lines elided]…
>:-)

The moving finger, having hit 'enter', moves on... if this was the worst 
error of the day then it may have been a pleasant day, indeed.

DD
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-03-07T11:59:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141761579.182608.174410@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1141744476.490567.164950@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com>`

```

hmitchell@cc.tt wrote:

> The FCBTEST file has one (1) record as: ABC91.47

>   01 RECORD-FCBTEST.
>      02 T1			PIC X(3).
>      02 N1			PIC 99V99.

The 'V' is an _implied_ decimal position.  The value of 1.50 will be
represented by the 4 characters 0150 in the record.  You have a full
stop in the record where the first decimal digit should be.

That is the record should be 'ABC9147'.

> I will appreciate your help. I did not understand when you say: "Give
> that four digits before the sign and it will work".

He meant before the decimal point position.  You are only allowing for
numbers up to 99.99 to be used.  Also you are only allowing for
positive numbers, negatives will be treated as positivs because you
have not specified a sign in the picture.

In your COMPUTE statement you should add

            COMPUTE N3 = N1 * 100
                     ON SIZE ERROR DISPLAY "I STILL CAN"T GET IT RIGHT"
            END-COMPUTE


You should note that Cobol is _not_ giving you 'erroneous results', it
is doing exactly what you have told it to do, if the results do not
meet your expectations then it is your expectations that are erroneous.

> Can you write it for me?

It seems to me that someone wrote the original for you 'to get you
started' but deliberately made it such that you would have to work out
what was wrong.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-08T22:10:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ODIPf.69543$TK5.61191@fe06.news.easynews.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com>`

```
Ian,
    I *think* that this (earlier) post should not cause overflow or truncation.

Am I missing something?

Now, do I know what the input was actually supposed to look like MUCH less what 
the program was supposed to do?
  Answer: NO
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 6)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-09T09:18:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhsv02ttrucepduq99ffsbke9naku4pi2f@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141683610.426592.222920@i40g2000cwc.googlegroups.com> <1141737952.736672.38780@p10g2000cwp.googlegroups.com> <dj2r02tlqdsitebpa27a2u6iddht7mmn3e@4ax.com> <1141744476.490567.164950@p10g2000cwp.googlegroups.com> <ODIPf.69543$TK5.61191@fe06.news.easynews.com>`

```
On Wed, 08 Mar 2006 22:10:54 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Ian,
>    I *think* that this (earlier) post should not cause overflow or truncation.
>
>Am I missing something?
>

No, quite right - I misread that one. Only the input picture to garble
the result.
```

#### ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** "PradeepR" <pradeep.ravle@gmail.com>
- **Date:** 2006-03-06T20:09:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141704541.611647.185630@z34g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```
hmitchell@cc.tt wrote:
> For example, I am not getting this result:
> 91.47 * 100 = 9147.
>
>  02 N2			PIC 99.99.

>  77 N3			PIC 99V99 VALUE ZEROES.
>  ................................................
…[4 more quoted lines elided]…
> ................................................

I assume you are new to COBOL. This is quite basic and any COBOL book
will provide you with the truncation rules that COBOL follows.

Here
9147 has 4 digits so declaration of variable which needs to store this
should have minimum 4 digits, otherwise truncation takes place. If
declaration is changed to
PIC 9(4)V99 for N2 and similarly for N3, you will not lose the value.

PNR
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-07T05:27:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141738029.106998.43720@p10g2000cwp.googlegroups.com>`
- **In-Reply-To:** `<1141704541.611647.185630@z34g2000cwc.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141704541.611647.185630@z34g2000cwc.googlegroups.com>`

```
Dear PradeepR,
Thanks for the answer but, I made a mistake with the details. The
following details replace what I sent before. Please notice N2. The
problem still persist. Thanks in advance for your help.

FD FCBTEST
     LABEL RECORD STANDARD.
  01 RECORD-FCBTEST.
     02 T1                      PIC X(3).
     02 N1                      PIC 99V99.


 FD 1CBTEST
     LABEL RECORD STANDARD.
 01 RECORD-1CBTEST.
     02 N2                      PIC 9999.


 WORKING-STORAGE SECTION.


 77 N3                  PIC 99V99 VALUE ZEROES.
 ................................................
 FORMAT-1CBTEST.
     COMPUTE N3 = N1 * 100.
     MOVE N3 TO N2
     WRITE RECORD-1CBTEST.
................................................
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2006-03-07T09:42:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tZgPf.1041$Qh1.25924@news20.bellglobal.com>`
- **In-Reply-To:** `<1141738029.106998.43720@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141704541.611647.185630@z34g2000cwc.googlegroups.com> <1141738029.106998.43720@p10g2000cwp.googlegroups.com>`

```
hmitchell@cc.tt wrote:
> Dear PradeepR,
> Thanks for the answer but, I made a mistake with the details. The
…[26 more quoted lines elided]…
> 

You are calculating N3, not N2. Moving a wrong answer somewhere else
will not fix it.

Donald
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-07T15:26:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duk8n3$94b$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141704541.611647.185630@z34g2000cwc.googlegroups.com> <1141738029.106998.43720@p10g2000cwp.googlegroups.com> <tZgPf.1041$Qh1.25924@news20.bellglobal.com>`

```
In article <tZgPf.1041$Qh1.25924@news20.bellglobal.com>,
Donald Tees  <donald_tees@sympatico.ca> wrote:
>hmitchell@cc.tt wrote:

[snip]

>>  ................................................
>>  FORMAT-1CBTEST.
…[7 more quoted lines elided]…
>will not fix it.

Oh, I *cannot* resist...

... someone might tell this to managers who 'fix things' by moving their 
wrong-answering subordinates to other departments.

Speaking of Managerial Duties... for the second time in as many weeks the 
building's security-card system has been rejecting all cards as invalid; 
this makes getting to one's work-area a bit... difficult.  A couple of 
employees were standing by the microwave oven discussing the matter when I 
came in to boil up a pot of water to make tea... and I said something 
approximating this:

'The doors aren't working again... and now you know why I never moved up 
to Management.  My response to this situation would be to go to *my* boss 
and say 'This is impossible.  My people can't get to their work and when 
they can't get *to* their work they can't *do* their work.  My people 
*like* doing their work... because when they do their work and do it well 
they get rewarded and when they get rewarded they are happier and when 
they're happier they do more work... and they're here to do work.  *Who* 
is getting in the way of my people making themselves happier and the 
company more profitable and how do we get them *out* of the way so we can 
all Do More Work?!?''

... and the response from both employee was a rueful laugh, with one 
saying 'No, you don't go into Management... *you* talk about people 
getting rewarded for doing a good job, Management doesn't... they don't 
talk about it, they don't do it, they don't even want to hear about it.'

DD
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-07T08:29:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nl9r029rb2popjn150n37dinuh0q1vverd@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141704541.611647.185630@z34g2000cwc.googlegroups.com> <1141738029.106998.43720@p10g2000cwp.googlegroups.com> <tZgPf.1041$Qh1.25924@news20.bellglobal.com> <duk8n3$94b$1@reader2.panix.com>`

```
On Tue, 7 Mar 2006 15:26:27 +0000 (UTC), docdwarf@panix.com () wrote:

>... and the response from both employee was a rueful laugh, with one 
>saying 'No, you don't go into Management... *you* talk about people 
>getting rewarded for doing a good job, Management doesn't... they don't 
>talk about it, they don't do it, they don't even want to hear about it.'

Not implicitly.   You reward someone for doing a good job by offering
to make him management.    Being like us is the ultimate reward.
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-07T15:53:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dukaa9$mm0$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <tZgPf.1041$Qh1.25924@news20.bellglobal.com> <duk8n3$94b$1@reader2.panix.com> <nl9r029rb2popjn150n37dinuh0q1vverd@4ax.com>`

```
In article <nl9r029rb2popjn150n37dinuh0q1vverd@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 7 Mar 2006 15:26:27 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[6 more quoted lines elided]…
>to make him management.    Being like us is the ultimate reward.

This seems to be rather... human behavior, Mr Brazee.  As I recall there 
are a few groups of the species who refer to themselves with concepts that 
translate into English as 'the Human Beings'.

DD
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-07T09:01:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<icbr02ddfhmnalupom92vsorbfsgkqi5mr@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <tZgPf.1041$Qh1.25924@news20.bellglobal.com> <duk8n3$94b$1@reader2.panix.com> <nl9r029rb2popjn150n37dinuh0q1vverd@4ax.com> <dukaa9$mm0$1@reader2.panix.com>`

```
On Tue, 7 Mar 2006 15:53:45 +0000 (UTC), docdwarf@panix.com () wrote:

>>Not implicitly.   You reward someone for doing a good job by offering
>>to make him management.    Being like us is the ultimate reward.
…[3 more quoted lines elided]…
>translate into English as 'the Human Beings'.

I suspect that other species know that they are the ultimate as well.

Managers don't discriminate against programmers - except for those
programmers who don't act like managers.  (replace these terms with
applicable terms regarding race, gender, church, etc.).
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-07T17:02:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dukebc$al8$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <nl9r029rb2popjn150n37dinuh0q1vverd@4ax.com> <dukaa9$mm0$1@reader2.panix.com> <icbr02ddfhmnalupom92vsorbfsgkqi5mr@4ax.com>`

```
In article <icbr02ddfhmnalupom92vsorbfsgkqi5mr@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Tue, 7 Mar 2006 15:53:45 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>I suspect that other species know that they are the ultimate as well.

Others appear to have had similar suspicions, Mr Brazee, and a few years 
ago.  From http://www.bartleby.com/66/27/40527.html :

--begin quoted text:

QUOTATION: If triangles had a god, they would give him three sides. 

ATTRIBUTION: Charles Louis de Secondat Montesquieu (1689�1755), French 
philosopher, lawyer. Persian Letters, no. 59 (1721), trans. by C.J. Betts 
(1973).

--end quoted text

... gotta love this Web-thingie... and this seems to be a passable 
translation, from http://big.chez.com/bacfrancais/lpersanes-integrale.html :

(note - accents removed to accomodate newsreaders)

--begin quoted text

On a dit fort bien que si les triangles faisaient un dieu, ils lui 
donneraient trois cotes.

--end quoted text

... except for the rendering of 'faisaient' as 'had'.

>
>Managers don't discriminate against programmers - except for those
>programmers who don't act like managers.  (replace these terms with
>applicable terms regarding race, gender, church, etc.).

I barely know whom *I* discriminate for or against, Mr Brazee... let alone 
others.

DD
```

#### ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-07T05:29:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141738144.155011.135850@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```
Dear guys,
I made a mistake with the details. The following details replace what I
sent before. Please notice N2. The problem still persist. Thanks in
advance for your help.

FD FCBTEST
     LABEL RECORD STANDARD.
  01 RECORD-FCBTEST.
     02 T1                      PIC X(3).
     02 N1                      PIC 99V99.


 FD 1CBTEST
     LABEL RECORD STANDARD.
 01 RECORD-1CBTEST.
     02 N2                      PIC 9999.


 WORKING-STORAGE SECTION.


 77 N3                  PIC 99V99 VALUE ZEROES.
 ................................................
 FORMAT-1CBTEST.
     COMPUTE N3 = N1 * 100.
     MOVE N3 TO N2
     WRITE RECORD-1CBTEST.
................................................
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-03-07T11:42:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<120rhg3cpdvg278@news.supernews.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141738144.155011.135850@u72g2000cwu.googlegroups.com>`

```
hmitchell@cc.tt wrote:
> Dear guys,
> I made a mistake with the details. The following details replace what
…[25 more quoted lines elided]…
> ................................................

You can't get 9147 pounds of stuff in a bag that only holds 99 pounds.

N3 only holds 99.99 pounds of stuff.

You'll have to make several trips.
```

#### ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2006-03-07T21:57:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SAsPf.284$316.173@fe03.lga>`
- **In-Reply-To:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```
hmitchell@cc.tt wrote:
> I will appreciate if anyone can help me. I have done many exhauting
> tests, read a lot, but without success. When COMPUTE and MOVE, I am
…[23 more quoted lines elided]…
> 
If N1 = 91.47
and you issue a command like COMPUTE N3 = N1 * 100.
What will happen is the compiler computes the number and then it looks 
at the receiving field.  Then it will try to round it for the precision. 
  But, when you do this on paper and you try to put it in the field what 
happens?  You end up truncating the top two digits.  You are running 
into an Overflow condition.

In an IBM Compiler Compute has an on overflow option to do some 
alternate task or option when it has an overflow condition.  One option 
would be to display an error message.

The largest number that will fit in any field with a picture clause of :

PIC 99V99 is 99.99

If you attempt to put a number any larger than 99.99 in your compute 
result field you will get unexpected results.
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-08T09:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dum808$pqb$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <SAsPf.284$316.173@fe03.lga>`

```
In article <SAsPf.284$316.173@fe03.lga>,
Last Boy Scout  <eggbtr@ezl.com> wrote:
>hmitchell@cc.tt wrote:

[snip]

>>  FORMAT-1CBTEST.
>>      COMPUTE N3 = N1 * 100.
…[10 more quoted lines elided]…
>into an Overflow condition.

You know... after getting a 'can you write it for me' refused my intuition 
tells me that there may not be too many more postings from the Original 
Poster.

DD
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-08T15:06:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zpCPf.29329$x96.25627@fe02.news.easynews.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <SAsPf.284$316.173@fe03.lga> <dum808$pqb$1@reader2.panix.com>`

```
For those who didn't see what the final answer(S) were:

1) The OP showed examples WITH the PIC having sufficient 9's left and right of 
the decimal point for all items.

2) It turns out OP was "creating" their own test data and had items like 
"1234.56" (with ".") for input defined with "V".
and we ALL know what that causes <G>
```

###### ↳ ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

_(reply depth: 4)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2006-03-08T21:20:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kiu02thlq5t3g5qh5ppk5smfd7t8kidtc@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <SAsPf.284$316.173@fe03.lga> <dum808$pqb$1@reader2.panix.com> <zpCPf.29329$x96.25627@fe02.news.easynews.com>`

```
On Wed, 08 Mar 2006 15:06:07 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>For those who didn't see what the final answer(S) were:
>
>1) The OP showed examples WITH the PIC having sufficient 9's left and right of 
>the decimal point for all items

Didn't arrive on my server if he did - there was still an inadequate
intermediate store on the last one I saw.

>2) It turns out OP was "creating" their own test data and had items like 
>"1234.56" (with ".") for input defined with "V".
>and we ALL know what that causes <G>

Indeed. Depends whether it's EBCDIC or ASCII (or whatever!). I can't
see the results he quoted without truncation as well, though?
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-03-08T07:31:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hkqt0214kbe3u7s50vi798f7j25r8cdsjt@4ax.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <SAsPf.284$316.173@fe03.lga>`

```
On Tue, 07 Mar 2006 21:57:38 -0600, Last Boy Scout <eggbtr@ezl.com>
wrote:

>In an IBM Compiler Compute has an on overflow option to do some 
>alternate task or option when it has an overflow condition.  One option 
>would be to display an error message.

I very rarely have any need for this as I already know the data and
can usually avoid overflow conditions.
```

#### ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** hmitchell@cc.tt
- **Date:** 2006-03-08T07:46:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141832786.135680.243130@v46g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com>`

```
I have to thank all you guys for your valuable help and time. You all
in some way made me understand what is the problem. I had an erroneous
conception about the hard coded decimal point. However, I have
alternative options to get what I am expecting. So, from my side I
consider closed this topic.
```

##### ↳ ↳ Re: Erroneous results in COMPUTE and MOVE

- **From:** docdwarf@panix.com ()
- **Date:** 2006-03-08T16:26:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dun0j2$n62$1@reader2.panix.com>`
- **References:** `<1141682865.886063.156010@p10g2000cwp.googlegroups.com> <1141832786.135680.243130@v46g2000cwv.googlegroups.com>`

```
In article <1141832786.135680.243130@v46g2000cwv.googlegroups.com>,
 <hmitchell@cc.tt> wrote:

[snip]

>However, I have
>alternative options to get what I am expecting. So, from my side I
>consider closed this topic.

How interesting... didn't someone post something here, rather recently, 
about how 'after getting a 'can you write it for me' refused my intuition 
tells me that there may not be too many more postings from the Original 
Poster.'?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
