[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data conversion on READ (why not?)

_2 messages · 2 participants · 1999-11_

---

### Re: Data conversion on READ (why not?)

- **From:** Jeff Farkas <jeffreyfarkas@earthlink.net>
- **Date:** 1999-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.129e1d2232c56f3e9896ab@news.earthlink.net>`
- **References:** `<38324AB2.2D3EB293@worldnet.att.net> <19991117095522.04551.00000239@ng-cd1.aol.com>`

```
In article <19991117095522.04551.00000239@ng-cd1.aol.com>, 
roadraat@aol.com says...
>>Sure you can do that, but what will your program do if JOBCODE-REC or
>>MINSAL-REC contain non-numeric data?
…[20 more quoted lines elided]…
>
I'm sure this has been beat to death.. but since this post has not been 
replied to.. at least on my server... 

 First, testing the SQLCODE will only check the results of the call to 
DB2 and not the contents or validity of the data.

 Second, READ INTO works differently than the MOVE statements you use. 

 Let's look at an example. Assume you have a record with an invalid 
numeric value and you read it into your buffer. You then execute your 
move in the READ statement it will abend and the dump will not have 
display the data you tried to move to the working storage because it was 
invalid and the buffer was wiped clean. 

 
Hope that helps..
Jeff..

http://home.earthlink.net/~jeffreyfarkas/
```

#### ↳ Re: Data conversion on READ (why not?)

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3834AD7E.17C74531@nbnet.nb.ca>`
- **References:** `<38324AB2.2D3EB293@worldnet.att.net> <19991117095522.04551.00000239@ng-cd1.aol.com> <MPG.129e1d2232c56f3e9896ab@news.earthlink.net>`

```
Huh:

READ file-name INTO record-name is defined as a READ followed by a group
level MOVE. That means that the record read exists both in
WORKING-STORAGE and in the buffer.  It may contain complete garbage but
if a record was read as opposed to end-of-file, record-not-found or
i-o-error of some sort that record will be in the buffer.  If you
execute a COBOL instruction that does an explicit arithmetic operation
(or an implicit one such as a MOVE from a smaller numeric field to a
larger one in packed-decimal on an IBM mainframe which would use a Zero
Add Packed Instruction) you will probably get an arithmetic exception
and the receiving field contents may be the value prior to the
instruction or something else.  The sending field in the buffer or
WORKING-STORAGE will still be there as will the buffer.  On any IBM
mainframe COBOL 85 using LE at a high enough level the offending record
will be in the dump in an area associated with its BLF number.  I
believe that the LE is 1.5 with PTF's and I know that LE with OS390 2.5
works this way (1.8 I THINK).  I will try to check the manual in the
morning for the exact description of READ ... INTO for the exact
description when variable length records are involved. 

Jeff Farkas wrote:
> 
> > snip
…[19 more quoted lines elided]…
> -- Crow MST3K
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
