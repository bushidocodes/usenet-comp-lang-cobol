[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Define a transaction for a COBOL program on OS/390?

_9 messages · 6 participants · 2000-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Define a transaction for a COBOL program on OS/390?

- **From:** uniware@my-deja.com
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qbj7k$12s$1@nnrp1.deja.com>`

```
I learn how to write a simple COBOL program mixed
with EXEC CICS command. After writing the JCL to
tranlate, comply, and link-edit the program, I
don't know how to define a transaction in CICS to
let CICS know the program I want to run.
The platform is OS/390.
Can anyone help me? Thanks.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Define a transaction for a COBOL program on OS/390?

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3dy5.1109$5p.10059@news2.mia>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com>`

```
There are several steps.  You will not be doing them most likely.

An entry  for the Transaction Name (if it can be executed by a user) in the
Program Contol Table
an entry in a group for the program specifiying language type, data
location, many
status items, etc.

Ths is usually done thru CEDB/CEDA.

<uniware@my-deja.com> wrote in message news:8qbj7k$12s$1@nnrp1.deja.com...
> I learn how to write a simple COBOL program mixed
> with EXEC CICS command. After writing the JCL to
…[8 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

- **From:** uniware@my-deja.com
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qcl5r$76q$1@nnrp1.deja.com>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com> <c3dy5.1109$5p.10059@news2.mia>`

```
In article <c3dy5.1109$5p.10059@news2.mia>,
  "mangogwr" <learn_the_law@bellsouth.net> wrote:
> There are several steps.  You will not be doing them most likely.
>
> An entry  for the Transaction Name (if it can be executed by a user)
in the
> Program Contol Table
> an entry in a group for the program specifiying language type, data
…[4 more quoted lines elided]…
>
  Thanks. I now know how to define a PROGram and a TRANSaction using
CEDB/CEDA. Since there are no item to indicate which dataset member
the program resides, how can CICS know where the program is? After I
define the program and the transaction, I can't start it. When I use
    CEMT SET PROG(TEST)
CICS told me that program not found!
Would you like to give me an example and tell me how CICS locates the
program?

> <uniware@my-deja.com> wrote in message
news:8qbj7k$12s$1@nnrp1.deja.com...
> > I learn how to write a simple COBOL program mixed
> > with EXEC CICS command. After writing the JCL to
…[10 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-01683C.22095821092000@news.m.iinet.net.au>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com> <c3dy5.1109$5p.10059@news2.mia> <8qcl5r$76q$1@nnrp1.deja.com>`

```
In article <8qcl5r$76q$1@nnrp1.deja.com>, uniware@my-deja.com wrote:

> In article <c3dy5.1109$5p.10059@news2.mia>,
>   "mangogwr" <learn_the_law@bellsouth.net> wrote:
…[19 more quoted lines elided]…
> 
CICS looks in the //DFHRPL DD concatenation for all the programs defined 
by CEDA.

You will have to either, copy your program into an existing library 
included in that concatenation, or Add your program library to the 
concatenation.
```

###### ↳ ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

_(reply depth: 4)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83yy5.3184$5p.16301@news2.mia>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com> <c3dy5.1109$5p.10059@news2.mia> <8qcl5r$76q$1@nnrp1.deja.com> <josephk-01683C.22095821092000@news.m.iinet.net.au>`

```
Actually, that is the DEFAULT  where CICS looks.

If you have access then go to SDSF, DA,
PRE whatever CICS region you are trying to run in:  lets say you logon to
CICSABCD
do PRE CICSAB* and look for CICSABCD (some shops have Prod and Test
in the same CICS system)

Then look for LOAD or LOADLIB or ONLINE.LOAD, and soforth

Then you will find the loadlib concatenation.

Most likely, the one you can use will have 'TEST' in the name.

You must copy the program to there

HTH

Joseph Katnic <josephk@iinet.net.au> wrote in message
news:josephk-01683C.22095821092000@news.m.iinet.net.au...
> In article <8qcl5r$76q$1@nnrp1.deja.com>, uniware@my-deja.com wrote:
>
…[22 more quoted lines elided]…
> CICS looks in the file://DFHRPL DD concatenation for all the programs
defined
> by CEDA.
>
…[7 more quoted lines elided]…
> Joe Katnic josephk@iinet.net.au
```

###### ↳ ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-22T02:05:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000921220534.12696.00000040@ng-fw1.aol.com>`
- **References:** `<83yy5.3184$5p.16301@news2.mia>`

```
>From: "mangogwr" mangogwr@bellsouth.net 
>Date: 9/21/00 11:46 PM Eastern Daylight Time

>Actually, that is the DEFAULT  where CICS looks.
>
…[15 more quoted lines elided]…
>

I don't know about the location any of you are at but when I do a CICS compile
the load automatically goes into the correct load library for test and after my
program/transaction/map etc are in the proper tables all I have to do is enter
the 4 position transaction on a blank screen, press the enter key and voila -
my program executes.

When it is ready for production the proper department compiles it to the
production load libraries. 

No moving of loads etc for me or anyone else.

Eileen
```

###### ↳ ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CB11CF.E42DFDCD@worldnet.att.net>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com> <c3dy5.1109$5p.10059@news2.mia> <8qcl5r$76q$1@nnrp1.deja.com> <josephk-01683C.22095821092000@news.m.iinet.net.au>`

```
Joseph Katnic wrote:
> 
> In article <8qcl5r$76q$1@nnrp1.deja.com>, uniware@my-deja.com wrote:
…[28 more quoted lines elided]…
> concatenation.

And of course, if you add a new library to your DFHRPL DD concatenation,
then you will need to recycle your CICS region before the new library is
available.  And if you recycle the region you won't have to do the
NEWCOPY.
```

###### ↳ ↳ ↳ Re: Define a transaction for a COBOL program on OS/390?

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g18wd10.pminews@news.wanadoo.es>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com> <c3dy5.1109$5p.10059@news2.mia> <8qcl5r$76q$1@nnrp1.deja.com>`

```
On Fri, 22 Sep 2000 09:42:22 GMT, uniware@my-deja.com wrote:

>  Thanks. I now know how to define a PROGram and a TRANSaction using
>CEDB/CEDA. Since there are no item to indicate which dataset member
…[5 more quoted lines elided]…
>program?

Hi,

CICS looks in the libraries defined for the region where it runs. Ask your
systems programmer
where to copy your program.

Bye
Willem
```

#### ↳ Re: Define a transaction for a COBOL program on OS/390?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000920222857.20844.00000137@ng-fb1.aol.com>`
- **References:** `<8qbj7k$12s$1@nnrp1.deja.com>`

```
>From: uniware@my-deja.com
>Date: 9/20/00 8:03 PM Eastern Daylight Time

>I learn how to write a simple COBOL program mixed
>with EXEC CICS command. After writing the JCL to
…[4 more quoted lines elided]…
>Can anyone help me? Thanks.

Things like this are usually done by the CICS systems programmer at your
facility. You'll need to give that person the transaction you are going to use
for the program (most shops use the first 4 positions of the program name for
this but it will be whatever you look at in EIBTRAN), and the program name as
that has to be loaded to the program table and associated with the transaction.

Then you have to contact your security people as there is probably security on
your site to let them know who can access the transaction (don't forget
yourself!). 

Once this is all done don't forget to newcopy your program via the CEMT
command.

Eileen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
