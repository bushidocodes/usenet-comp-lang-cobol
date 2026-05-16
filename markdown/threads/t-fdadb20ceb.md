[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Question about jcl

_5 messages · 4 participants · 2002-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] Question about jcl

- **From:** "Capellone" <.capellone@libero.it>
- **Date:** 2002-07-10T17:02:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aghigg$cds$1@newsreader.mailgate.org>`

```
Hi to everybody, i know i'm out of topic,
but the 2 newsgroups i found where i could leave this kind of messages are
not so much frequented.

But i think most of you all work with jcl, and maybe someone can help me.

I need to simulate a load into a DB2 table. The load is sent thru a jcl
which takes the data  from a file.
I want all the spool as usual, but i don't want really update the table.

I hope you understand what i meant.

thanks
Capellone
```

#### ↳ Re: [OT] Question about jcl

- **From:** Susan A Allen <susan.a.allen@boeing.com>
- **Date:** 2002-07-10T22:46:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2CB92A.BB784240@boeing.com>`
- **References:** `<aghigg$cds$1@newsreader.mailgate.org>`

```


Capellone wrote:
> 
> Hi to everybody, i know i'm out of topic,
…[13 more quoted lines elided]…
> 

In order to test the JCL you will have to really load something (I
assume you are planning to use the DB2 Load Utility?).


I have a test where I deliberately attempt to load duplicate records
(which rejected to an error file), this does more then simulate a load,
the table will not load the duplicated records, but the JCL stream will
work fine.

	Susan A
```

##### ↳ ↳ Re: [OT] Question about jcl

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2002-07-11T02:14:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D2D222F.3070609@optonline.NOSPAM.net>`
- **References:** `<aghigg$cds$1@newsreader.mailgate.org> <3D2CB92A.BB784240@boeing.com>`

```
Susan A Allen wrote:
> 
> Capellone wrote:
…[27 more quoted lines elided]…
> 	Susan A

Maybe the Job card parameter "TYPRUN=SCAN" wound be useful? This would 
validate your JCL but not execute anything user code.

I suspect, though, that you want to execute the load utility but not 
update your database. I don't know DB2, so I can't say one way or the 
other. For straight batch programs, you could assign the output file to 
DUMMY and run the job. Usually the program being invoked would run as 
though it were creating an output file (it's possible to check the 
attributes of the DD cards and, thus, know that the output file was 
dummied out). Could you update a copy of the table, then discard it?
```

##### ↳ ↳ Re: [OT] Question about jcl

- **From:** "Capellone" <.capellone@libero.it>
- **Date:** 2002-07-11T10:24:55+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agjfqq$dp5$1@newsreader.mailgate.org>`
- **References:** `<aghigg$cds$1@newsreader.mailgate.org> <3D2CB92A.BB784240@boeing.com>`

```

Susan A Allen <susan.a.allen@boeing.com> wrote in message
3D2CB92A.BB784240@boeing.com...
>
> In order to test the JCL you will have to really load something (I
> assume you are planning to use the DB2 Load Utility?).
>
Once established my data are ok, i will really load the table.
I use the instruction "load data into table" into my jcl.
>
> I have a test where I deliberately attempt to load duplicate records
> (which rejected to an error file), this does more then simulate a load,
> the table will not load the duplicated records, but the JCL stream will
> work fine.

I don't have to test my jcl, i need to see if my data follows all the
integrity, and if it is, i don't want
it to write anyway, not yet.
I think in your case, nothing is simulated, your records are just discarded
because duplicated isn't it?

Thanks

Capellone
```

###### ↳ ↳ ↳ Re: [OT] Question about jcl

- **From:** docdwarf@panix.com
- **Date:** 2002-07-11T06:02:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agjl33$13c$1@panix1.panix.com>`
- **References:** `<aghigg$cds$1@newsreader.mailgate.org> <3D2CB92A.BB784240@boeing.com> <agjfqq$dp5$1@newsreader.mailgate.org>`

```
In article <agjfqq$dp5$1@newsreader.mailgate.org>,
Capellone <.capellone@libero.it> wrote:

[snip]

>I don't have to test my jcl, i need to see if my data follows all the
>integrity, and if it is, i don't want
>it to write anyway, not yet.

It seems like you want to LOAD your table and then do a ROLLBACK on it to 
make sure that your data meet the various table definitions for ranges, 
foreign keys, formats and various constraints; this smells, to me, like 
'let's test this in production'... anyways, I am not sure this is 
possible.

Might you be able to create a test copy of the INDD file and modify a 
field of it to flag it for deletion?  You can run a FileAid against it 
and, for instance, REPL all the street-address fields to '123 PALAZZO 
PAZZO' or change all the user-id fields to 'AIAIAIEE'... or anything 
uniquely associable with your test.  After you run your LOAD you then run 
another batch job with SQL to delete from the table any rows which match 
these criteria.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
