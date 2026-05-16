[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

_6 messages · 5 participants · 2001-07_

---

### COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** liptakj@hotmail.com (John Liptak)
- **Date:** 2001-07-17T02:03:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com>`

```
A am getting the following compiler error on Fujitsu.  Cobol version is COBOL 85.

"REVERSED PHRASE MUST BE SPECIFIED IN START STATMENT"  for the statement below;

--->  START PARAM-FILE KEY IS <= PARAM-RECORD-KEY   

Does anyone know what this is trying to tell me.

/john
```

#### ↳ Re: COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-07-18T00:54:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b543b76_2@news2.newsgroups.com>`
- **References:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com>`

```
John

Trying to establish position with a relational operator involving "LESS
THAN" is pointless for a file which is in ascending sequence.  You will
always return the first record on the file, or no record.

Fujitsu recognise this and offer an extension which allows ISAM files to be
in DESCENDING sequence, and in this case it makes sense to issue a
positioning START with a relational operator which includes "<".

However, if you use such a relational operator you must use the REVERSED
phrase with your START.

Think again about what you are trying to do... If the file is indeed in
ascending sequence (and every ISAM file I have ever dealt with was) then it
is illogical to issue a "START  <="

Imagine:  Start <= 'A'        gets first record on file, or none if there
are no As
                 Start <= 'B'        gets first record on file or none if
there is nothing prior to C. It doesn't get the first B, it gets the first
record on file...probably an A if there is one.
                 Start <= 'G'        Gets first record on file (probably A
if there is one) or none if there is nothing prior to H.

Although you may have intended to start at the beginning of the Bs or the
Gs, you will always be returned the first record on the file (which will be
an A if there are any, or whatever...)

Hope this helps,

Pete.


"John Liptak" <liptakj@hotmail.com> wrote in message
news:9db5eaf6.0107170103.3fb8eef3@posting.google.com...
> A am getting the following compiler error on Fujitsu.  Cobol version is
COBOL 85.
>
> "REVERSED PHRASE MUST BE SPECIFIED IN START STATMENT"  for the statement
below;
>
> --->  START PARAM-FILE KEY IS <= PARAM-RECORD-KEY
…[3 more quoted lines elided]…
> /john




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

#### ↳ Re: COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-07-17T11:38:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378AFE2DE3299A49.F8CE590FF240DD27.774D119BB51E9CD0@lp.airnews.net>`
- **References:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com>`

```
On 17 Jul 2001 02:03:20 -0700, liptakj@hotmail.com (John Liptak)
enlightened us:

>A am getting the following compiler error on Fujitsu.  Cobol version is COBOL 85.
>
…[6 more quoted lines elided]…
>/john

Pete has responded with the long answer.  The short answer is, you
cannot do a START with a LESS THAN operator.  You can use EQUAL or
GREATER THAN or GREATER THAN OR EQUAL only.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Clones are people two.


Remove nospam to email me.

Steve
```

#### ↳ Re: COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-17T19:32:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107171832.56824f73@posting.google.com>`
- **References:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com>`

```
liptakj@hotmail.com (John Liptak) wrote in message news:<9db5eaf6.0107170103.3fb8eef3@posting.google.com>...
> A am getting the following compiler error on Fujitsu.  Cobol version is COBOL 85.
> 
…[6 more quoted lines elided]…
> /john

*----------------------
The "less than" conditions on START are implementor extensions, where
they exist at all.
Pete has explained how it works on Fujitsu (your case). Here is how it
works in IBM (NOT the mainfrme, where it has not yet been implemented
at all):

X >_Workstation_> Under AIX and Windows, the following relational
operators
X are allowed in the KEY phrase: 


 X LESS THAN                               < 
 X NOT GREATER THAN                        NOT > 
 X LESS THAN OR EQUAL TO                   <=        <_Workstation_< 




X If you specify the KEY to be 'less than', or 'less than or equal to'
the
X data item, the file position indicator is positioned to the last
logical
X record currently existing in the file satisfying the comparison. 



X For an indexed file, if the key that satisfies the comparison has 
X duplicate entries, the file position indicator is positioned to the
last
X of these entries. 

(The x's indicate an IBM extension to the standard.)
-----------------------------------------------------------------------
In the proposed new standard, the "less than" relations WILL be
allowed. These are the rules:

For Relative files:
b) If the relational operator is LESS, NOT GREATER, or LESS OR EQUAL,
the file position indicator is set to the relative record number of
the first logical record in the file whose key satisfies the
comparison searching the file in reverse order.

For indexed files:
d) If the relational operator is LESS, NOT GREATER,or LESS OR EQUAL,
the file is searched in reverse order

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: Get involved in the standards process! Get your company to send
you to 3-star hotels in the suburbs, where you can argue grammar and
usage for 8 hours a day!
```

##### ↳ ↳ Re: COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-07-18T20:22:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b554cd2_2@news2.newsgroups.com>`
- **References:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com> <4145699b.0107171832.56824f73@posting.google.com>`

```

"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message >
> PS: Get involved in the standards process! Get your company to send
> you to 3-star hotels in the suburbs, where you can argue grammar and
> usage for 8 hours a day!

That's a relief...for a while there Stephen, I thought you'd lost your sense
of humour...<G>

Pete.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

#### ↳ Re: COBOL "REVERSED" PHRASE MUST BE SPECIFIED IN START STATMENT

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-18T08:00:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B55341B.8018F0EC@Azonic.co.nz>`
- **References:** `<9db5eaf6.0107170103.3fb8eef3@posting.google.com>`

```
John Liptak wrote:
> 
> A am getting the following compiler error on Fujitsu.  Cobol version is COBOL 85.
…[5 more quoted lines elided]…
> Does anyone know what this is trying to tell me.

It is trying to tell you that for the '<=' comparison to work you must
specify 'REVERSED'.

If you don't want to read reversed then you should specify 'NOT <' or
'>='.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
