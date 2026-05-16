[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rtsora32 error codes

_10 messages · 4 participants · 2010-04_

---

### rtsora32 error codes

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-15T07:29:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com>`

```
Can I assume error codes returned by rtsora32 should be the same as
what comes out of cobrun?

http://supportline.microfocus.com/Documentation/books/sx40sp2/rhrerr01.htm
is my reference.

I'm trying to understand the 102 error code.

This is the return code of an rtsora32 command after the the programs
run in-full.
```

#### ↳ Re: rtsora32 error codes

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-04-15T11:32:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com>`

```
On Apr 16, 2:29 am, Derek Schrock <derekschr...@gmail.com> wrote:
> Can I assume error codes returned by rtsora32 should be the same as
> what comes out of cobrun?
…[4 more quoted lines elided]…
> I'm trying to understand the 102 error code.

"Sequential file with non-integral number of records"

The file size is not a multiple of the record size. Reading the last
record in the file gave only part record.

> This is the return code of an rtsora32 command after the the programs
> run in-full.
```

##### ↳ ↳ Re: rtsora32 error codes

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-15T12:23:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com>`

```
On Apr 15, 2:32 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Apr 16, 2:29 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[16 more quoted lines elided]…
>

That's what I was thinking but wouldn't it kill the program since it's
a fatal error?
Where would the 102 code be?  The file status storage?  If it's at the
end of the file when it files the incomplete record the status would
be 102 then 10 at the "same time?"
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-04-15T13:58:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com>`

```
On Apr 16, 7:23 am, Derek Schrock <derekschr...@gmail.com> wrote:
> On Apr 15, 2:32 pm, Richard <rip...@Azonic.co.nz> wrote:
>
…[24 more quoted lines elided]…
> be 102 then 10 at the "same time?"

If you have a file status for the file you will get a 9/102 status
value. ie first byte 9 second byte x"66" (decimal 102). This is
because it is a failure to reach a proper end of file.

If you had not specified the file status clause for the file then to
102 error would kill the program because it is fatal.

It may be that you have specified an incorrect record size or that the
file has become corrupted.
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 4)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-16T05:08:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8611815f-6868-4d2e-8a58-5d949a6f177d@w42g2000yqm.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com>`

```
On Apr 15, 4:58 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Apr 16, 7:23 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[36 more quoted lines elided]…
> file has become corrupted.

Well program isn't being killed because it runs to the end "STOP RUN."
But back to the original question:  should I expect all error codes
returned by rtsor32 match with Microfocus' error code page?  Will
rtsora32 introduce any new return codes or use any that MF runtime is
already producing?
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 4)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-16T05:24:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3147aace-5d84-4bb8-a52c-d63cda431ce1@y17g2000yqd.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com>`

```
On Apr 15, 4:58 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Apr 16, 7:23 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[36 more quoted lines elided]…
> file has become corrupted.

Also, after removing all file status vars the program still does not
stop.  It ends with the ending "STOP RUN." statement.
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 4)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-16T08:48:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com>`

```
On Apr 15, 4:58 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Apr 16, 7:23 am, Derek Schrock <derekschr...@gmail.com> wrote:
>
…[36 more quoted lines elided]…
> file has become corrupted.

Turns out it's an Oracle issue... SQLBEX is setting RETURN-CODE to 102
early is the program's life.

Assuming error codes don't change that much.. (duck)

http://download-uk.oracle.com/docs/cd/A87862_01/NT817CLI/server.817/a76999/pcbeus.htm

PCB-00102 Input file name length exceeds the maximum length

    Cause: The file name length specified exceeded the maximum length.
Some operating systems have a maximum file name length.

    Action: Use a file name of length less than or equal to the
maximum platform specific file name length.

This is preprocessed code too...

....
  1004          CALL "SQLBEX" USING
  1005              SQLCTX
  1006              SQLEXD
  1007              SQLFPN
....

SQLFPN = ^^BN0711P.pco

Interesting...
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-04-16T15:54:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqa16r$2ek$1@reader1.panix.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com> <be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>`

```
In article <be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>,
Derek Schrock  <derekschrock@gmail.com> wrote:
>On Apr 15, 4:58?pm, Richard <rip...@Azonic.co.nz> wrote:
>> On Apr 16, 7:23?am, Derek Schrock <derekschr...@gmail.com> wrote:

[snip]

>Turns out it's an Oracle issue... SQLBEX is setting RETURN-CODE to 102
>early is the program's life.

... and this may be seen as a reason for some folks saying 'Debugging code 
is like peeling an onion... a layer at a time, and sometimes you cry.'

DD
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-04-16T14:24:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FH3yn.225616$K81.143239@newsfe18.iad>`
- **In-Reply-To:** `<be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com> <be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>`

```
Derek Schrock wrote:
> Turns out it's an Oracle issue... SQLBEX is setting RETURN-CODE to 102
> early is the program's life.
…[25 more quoted lines elided]…
> 

Nice when you find out what the REAL problem is :-)

Might try a bit of XP(e(X)treme (P)rogramming) on this one as you have 
hit  the particular error. Within ORACLE :-

IF length of input-Filename > Max-Platform-Length
	we have a problem
	generate an error-message

The other thing is you were misled by the Error 102 - there is no way 
that M/F File handling would have generated a three-digit file-status 
code which is a pic x(02). If file-status-1 = "9" then you have to do a 
convert on file-status-2 to get the numeric value.  Somewhere in your 
manuals you will find an M/F example to convert status-codes starting 
with "9" into a three-digit code. Here's a current reference to their 
file-status codes :-

http://kb.microfocus.com/display/1n/index.aspx?c=12&cpc=BTakh05i2p2gM801Slr08SHyX275E544jc&cid=2&cat=&catURL=&r=0.519614815711975

*> REPEAT :

*> http://kb.microfocus.com/display/1n/index.aspx?
*>c=12&cpc=BTakh05i2p2gM801Slr08SHyX275E544jc&cid=2&cat=&catURL
*>=&r=0.519614815711975


Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: rtsora32 error codes

_(reply depth: 5)_

- **From:** Derek Schrock <derekschrock@gmail.com>
- **Date:** 2010-04-19T06:00:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95ff3cbe-3e0f-49de-9f9e-98909fcfc07c@r1g2000yqb.googlegroups.com>`
- **References:** `<71b626ab-cf8e-4121-827a-2194acb682b0@z6g2000yqz.googlegroups.com> <5b051851-a2e0-448c-bdaa-9e10cc48fa25@k33g2000yqc.googlegroups.com> <fe73e947-c76d-4917-b56b-32a9279c5efd@j21g2000yqh.googlegroups.com> <2f2fa7af-3ee2-440d-a409-0b2f3ce48fce@j17g2000yqa.googlegroups.com> <be2da34b-eac8-4793-aa03-55072bf4159b@30g2000yqi.googlegroups.com>`

```
On Apr 16, 11:48 am, Derek Schrock <derekschr...@gmail.com> wrote:
> On Apr 15, 4:58 pm, Richard <rip...@Azonic.co.nz> wrote:
>
…[66 more quoted lines elided]…
> Interesting...

So it turns out the above error isn't the correct message... and the
funny thing is.. there isn't a message:

http://www.stanford.edu/dept/itss/docs/oracle/10g/appdev.101/a96109/pcoabops.htm

B.1.6 RETURN-CODE Special Register May Be Unpredictable.

The contents of the RETURN-CODE special register (for those systems
that support it) are unpredictable after any SQL statement or SQLLIB
function.

During the closing part of the cobol program adding a EXEC SQL COMMIT
EXEC fixed the problem.

The odd thing is that we're not using cursors or updates, just
standard selects.

So why the need for a commit statement?  I could have just as easily
ran a CALL cobol statement to set RETURN-CODE to 0.  I don't see any
where in Oracle's docs that require ending all Pro*COBOL programs with
a commit... interesting to say the least.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
