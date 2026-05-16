[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu and MS Access datatypes

_5 messages · 3 participants · 2002-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu and MS Access datatypes

- **From:** Robin Lee <robinlee@rr.com>
- **Date:** 2002-03-20T01:09:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C97E004.352BB29B@rr.com>`

```
I've been given an Access database which I am to populate using Fujitsu
COBOL. However, if my program makes any reference to fields defined in
Access as "Memo" datatype, the program build fails.

I've noticed on the ODBC control Field property sheet that these items
have their "spectacles" icon greyed-out, and PowerCOBOL identifies them
as being over two gigabytes in size!

I've looked thru a few Access reference books but they seem to be
procedure oriented and rather low on substance regarding datatypes. 
Could anyone give me a few pointers here please?

Also, I haven't gotten to this point yet, but I think I recall reading
that the Currency datatype is Pic s9(14)v9(4).  Is this correct?  Any
help would be greatly appreciated! Thanks!
```

#### ↳ Re: Fujitsu and MS Access datatypes

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-21T10:09:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9918f6_9@Usenet.com>`
- **References:** `<3C97E004.352BB29B@rr.com>`

```

Robin Lee <robinlee@rr.com> wrote in message
news:3C97E004.352BB29B@rr.com...
> I've been given an Access database which I am to populate using Fujitsu
> COBOL. However, if my program makes any reference to fields defined in
…[5 more quoted lines elided]…
>
Memo items are "best avoided" when using ACCESS with COBOL. If you set the
Host Variable to be Picture X(nnn) where "nnn" is a large number (don't
exceed the compiler limit...I'm not sure what it is from memory, but say you
set it to 2048 (well within the limit)) then when you SELECT... INTO it,
ACCESS will load the HV with as much data as you have provided for. (in this
case 2048 bytes).  If you really have a database with 2 GIG Memo fields on
it (whose bright idea was THAT?! <G>) you will probably need to "preprocess"
using some ACCESS code. If I were you, I'd really try and get thos fields
removed. Consider setting up some attached tables that can grow in a more
controlled manner than just having a giant "bin" to put stuff in. I'm sure
you know that Memo fields cannot be indexed, so anything that is put there
will take FOREVER to search (irrespective of whether it is searched in COBOL
or ACCESS or any other form of access to the data.)

The bottom line is that I know of no way you can actually load these fields
into embedded SQL. It's not a restriction in COBOL; it is a restriction in
the ODBC driver (guess the designers of this software expected people to be
rational when they design databases....<G>)

> I've looked thru a few Access reference books but they seem to be
> procedure oriented and rather low on substance regarding datatypes.
…[4 more quoted lines elided]…
> help would be greatly appreciated! Thanks!

Yes, you are correct. The currency data type is held as a 64 bit floating
point number  (comp-2 in Fujitsu COBOL) that is really a FLOAT where the
decimal is ALWAYS fixed to 4 places, by convention.  (COBOL s9(14)v9(4)).
You CAN set the host variable to be comp-2 and it will return it, but there
can be obscure problems in doing this. One way that always works (and I
therefore ensure that my data definition generator uses it) is to define the
host variable as: pic s9(14)v9(4).  (this is DISPLAY format by default).
This works correctly every time and is therefore useful...

If you have further problems with data definitions you should pick up
DECLGEN. It will analyse your tables and generate COBOL Host Variable
definitions (that work...) and COBOL Record layouts for inclusion in
programs. If you are doing this for your personal use, I'll let you have it
free, otherwise it costs $US 100.00. (Site license $US 500 - Runs under Win
32 and is written in PowerCOBOL).

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Fujitsu and MS Access datatypes

- **From:** "PorTy" <euromercante1@clix.pt>
- **Date:** 2002-03-22T09:22:26
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3LCm8.136$EM6.597127@newsserver.ip.pt>`
- **References:** `<3C97E004.352BB29B@rr.com> <3c9918f6_9@Usenet.com>`

```
From the where i can do the download this tool?

Regards,
Joe

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> escreveu na mensagem
news:3c9918f6_9@Usenet.com...
>
> Robin Lee <robinlee@rr.com> wrote in message
…[11 more quoted lines elided]…
> exceed the compiler limit...I'm not sure what it is from memory, but say
you
> set it to 2048 (well within the limit)) then when you SELECT... INTO it,
> ACCESS will load the HV with as much data as you have provided for. (in
this
> case 2048 bytes).  If you really have a database with 2 GIG Memo fields on
> it (whose bright idea was THAT?! <G>) you will probably need to
"preprocess"
> using some ACCESS code. If I were you, I'd really try and get thos fields
> removed. Consider setting up some attached tables that can grow in a more
> controlled manner than just having a giant "bin" to put stuff in. I'm sure
> you know that Memo fields cannot be indexed, so anything that is put there
> will take FOREVER to search (irrespective of whether it is searched in
COBOL
> or ACCESS or any other form of access to the data.)
>
> The bottom line is that I know of no way you can actually load these
fields
> into embedded SQL. It's not a restriction in COBOL; it is a restriction in
> the ODBC driver (guess the designers of this software expected people to
be
> rational when they design databases....<G>)
>
…[11 more quoted lines elided]…
> You CAN set the host variable to be comp-2 and it will return it, but
there
> can be obscure problems in doing this. One way that always works (and I
> therefore ensure that my data definition generator uses it) is to define
the
> host variable as: pic s9(14)v9(4).  (this is DISPLAY format by default).
> This works correctly every time and is therefore useful...
…[4 more quoted lines elided]…
> programs. If you are doing this for your personal use, I'll let you have
it
> free, otherwise it costs $US 100.00. (Site license $US 500 - Runs under
Win
> 32 and is written in PowerCOBOL).
>
…[8 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu and MS Access datatypes

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-23T11:30:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9be145_4@Usenet.com>`
- **References:** `<3C97E004.352BB29B@rr.com> <3c9918f6_9@Usenet.com> <3LCm8.136$EM6.597127@newsserver.ip.pt>`

```

PorTy <euromercante1@clix.pt> wrote in message
news:3LCm8.136$EM6.597127@newsserver.ip.pt...
> From the where i can do the download this tool?
>
…[3 more quoted lines elided]…
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> escreveu na
mensagem
> news:3c9918f6_9@Usenet.com...
> >
> > Robin Lee <robinlee@rr.com> wrote in message
> > news:3C97E004.352BB29B@rr.com...
> > > I've been given an Access database which I am to populate using
Fujitsu
> > > COBOL. However, if my program makes any reference to fields defined in
> > > Access as "Memo" datatype, the program build fails.
> > >
> > > I've noticed on the ODBC control Field property sheet that these items
> > > have their "spectacles" icon greyed-out, and PowerCOBOL identifies
them
> > > as being over two gigabytes in size!
> > >
> > Memo items are "best avoided" when using ACCESS with COBOL. If you set
the
> > Host Variable to be Picture X(nnn) where "nnn" is a large number (don't
> > exceed the compiler limit...I'm not sure what it is from memory, but say
…[4 more quoted lines elided]…
> > case 2048 bytes).  If you really have a database with 2 GIG Memo fields
on
> > it (whose bright idea was THAT?! <G>) you will probably need to
> "preprocess"
> > using some ACCESS code. If I were you, I'd really try and get thos
fields
> > removed. Consider setting up some attached tables that can grow in a
more
> > controlled manner than just having a giant "bin" to put stuff in. I'm
sure
> > you know that Memo fields cannot be indexed, so anything that is put
there
> > will take FOREVER to search (irrespective of whether it is searched in
> COBOL
…[4 more quoted lines elided]…
> > into embedded SQL. It's not a restriction in COBOL; it is a restriction
in
> > the ODBC driver (guess the designers of this software expected people to
> be
…[10 more quoted lines elided]…
> > Yes, you are correct. The currency data type is held as a 64 bit
floating
> > point number  (comp-2 in Fujitsu COBOL) that is really a FLOAT where the
> > decimal is ALWAYS fixed to 4 places, by convention.  (COBOL
s9(14)v9(4)).
> > You CAN set the host variable to be comp-2 and it will return it, but
> there
…[25 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu and MS Access datatypes

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-03-23T11:43:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9be149_4@Usenet.com>`
- **References:** `<3C97E004.352BB29B@rr.com> <3c9918f6_9@Usenet.com> <3LCm8.136$EM6.597127@newsserver.ip.pt>`

```
Mail me privately. (remove "nospam" from my mail address). Tell me what you
want it for and, if it is for personal use, I'll let you have it free.

I wrote this tool (DECLGEN) for my own use and I am not attempting to market
it (yet). A number of people (and one or two organisations) have found it
useful. The latest release is full Win32 and automatically detects your
database engine. It uses direct access to RDB internals (via OO PowerCOBOL)
to analyse the structure of your DB and generates COBOL pictures and data
structures that are compatible with it. It is a small part of a much larger
system for converting ISAM/VSAM-KSDS to Relational Database. (ISAM2RDB).

Pete.

PorTy <euromercante1@clix.pt> wrote in message
news:3LCm8.136$EM6.597127@newsserver.ip.pt...
> From the where i can do the download this tool?
>
…[3 more quoted lines elided]…
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> escreveu na
mensagem
> news:3c9918f6_9@Usenet.com...
> >
> > Robin Lee <robinlee@rr.com> wrote in message
> > news:3C97E004.352BB29B@rr.com...
> > > I've been given an Access database which I am to populate using
Fujitsu
> > > COBOL. However, if my program makes any reference to fields defined in
> > > Access as "Memo" datatype, the program build fails.
> > >
> > > I've noticed on the ODBC control Field property sheet that these items
> > > have their "spectacles" icon greyed-out, and PowerCOBOL identifies
them
> > > as being over two gigabytes in size!
> > >
> > Memo items are "best avoided" when using ACCESS with COBOL. If you set
the
> > Host Variable to be Picture X(nnn) where "nnn" is a large number (don't
> > exceed the compiler limit...I'm not sure what it is from memory, but say
…[4 more quoted lines elided]…
> > case 2048 bytes).  If you really have a database with 2 GIG Memo fields
on
> > it (whose bright idea was THAT?! <G>) you will probably need to
> "preprocess"
> > using some ACCESS code. If I were you, I'd really try and get thos
fields
> > removed. Consider setting up some attached tables that can grow in a
more
> > controlled manner than just having a giant "bin" to put stuff in. I'm
sure
> > you know that Memo fields cannot be indexed, so anything that is put
there
> > will take FOREVER to search (irrespective of whether it is searched in
> COBOL
…[4 more quoted lines elided]…
> > into embedded SQL. It's not a restriction in COBOL; it is a restriction
in
> > the ODBC driver (guess the designers of this software expected people to
> be
…[10 more quoted lines elided]…
> > Yes, you are correct. The currency data type is held as a 64 bit
floating
> > point number  (comp-2 in Fujitsu COBOL) that is really a FLOAT where the
> > decimal is ALWAYS fixed to 4 places, by convention.  (COBOL
s9(14)v9(4)).
> > You CAN set the host variable to be comp-2 and it will return it, but
> there
…[25 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
