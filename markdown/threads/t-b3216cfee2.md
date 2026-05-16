[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting Cobol to C

_12 messages · 10 participants · 2001-10_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Converting Cobol to C

- **From:** "Peter Nolan" <peternolan9@eircom.net>
- **Date:** 2001-10-17T13:47:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```
Hi All,
this is possibly not a 'popular' place to ask this question..

I have a bunch of cobol with imbedded SQL statements doing simple things
like read a file and update/insert into tables etc.  I want to convert it to
C. (No flames please).

I was wondering if anyone attached to this newsgroup had experience at cobol
to C conversions for batch processing style programs.

If so, could you let me know directly?  I'd be interested to talk with
anyone who has done this before.

Thanks

Peter Nolan
```

#### ↳ Re: Converting Cobol to C

- **From:** "Peter Nolan" <peternolan9@eircom.net>
- **Date:** 2001-10-17T18:38:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rqjz7.71$8s4.247@news.indigo.ie>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```
Hi PaulR,
I got your email but when I have tried to email you directly it bounces with
a message saying an error in remote mailer.  I have seen this happen before.
You you have another email address? (Rather than put a long post here)
Thanks
Peter
```

#### ↳ Re: Converting Cobol to C

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-18T07:11:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BCE729B.4310CE1C@Azonic.co.nz>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```
Peter Nolan wrote:
> 
> I have a bunch of cobol with imbedded SQL statements doing simple things
> like read a file and update/insert into tables etc.  I want to convert it to
> C. (No flames please).

This is not a flame, but just asks why would you want to do this.

It won't be any faster in C than the Cobol speed because this is going
to be a factor of the disk system.

It won't be more maintainable (probably worse).  There was an argument
raised a decade or so ago where a survey had found that there was a
higher proportion of Cobol programmers doing 'maintenance' than C
programmers.  The bogus conclusion was that if the Cobol code was
converted to C the programmers would do less maintenance and more new
development.

This was a completely incompetent conclusion because 'Cobol maintenance'
is primarily to keep the system reflecting changes in the business model
and is a result of the types of applications that Cobol is useful for. 
The majority of C programs tend not to need changing due to changes in
business and 'maintenence' is primarily bug-fixing.

Change an application from Cobol to C and it still requires maintenece
to the business model _and_ it requires bug-fixing.

Also, if it is a convertion, rather than a complete rewrite, you just
get Cobol programs written in the C language and you do not get C
programs.  The advantages of Cobol are lost in the convertion but any
advantages that C has (localisation, modularity, conciseness,
reusability through libraries, etc) are not gained.
```

##### ↳ ↳ Re: Converting Cobol to C

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-17T19:56:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tnlz7.201$wQ1.38654@paloalto-snr1.gtei.net>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3BCE729B.4310CE1C@Azonic.co.nz...
> Peter Nolan wrote:
> >
> > I have a bunch of cobol with imbedded SQL statements doing simple things
> > like read a file and update/insert into tables etc.  I want to convert
it to
> > C. (No flames please).
>
> This is not a flame, but just asks why would you want to do this.

I'm obviously not the original poster, but the legitimate possibilities
include...

1. Migrating to a platform where "C" is available and COBOL is not.
2. Migrating to "C" due to personnel changes: COBOL people have left, C
people have arrived.
3. Bad outside consultant trying to justify his existence; this consultant
is, coincidentally, the owner's brother.

MCM
```

##### ↳ ↳ Re: Converting Cobol to C

- **From:** "Peter Nolan" <peternolan9@eircom.net>
- **Date:** 2001-10-17T22:01:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpmz7.193$8s4.1153@news.indigo.ie>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz>`

```
Richard,
no reason so sinister....

Simply put, very few (if any) people under the age of 30 speak cobol on unix
boxes nowadays.  If I want to use this code again and have it developed or
maintained by grads with <5 years experience then it is going to have to be
in C.....

I personally understand all the arguements about both, and have used cobol
on unix many times......but I think it is time to use C on unix/NT.

I agree, all I will finish up with is cobol programs written in C.  After
all, the programs are just file processing programs....what cobol was always
good at.

Peter
```

###### ↳ ↳ ↳ Re: Converting Cobol to C

- **From:** "Paul Barnett" <paul.barnett@merant.com>
- **Date:** 2001-10-25T17:40:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r9gbo$jtq$1@hyperion.eu.merant.com>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz> <gpmz7.193$8s4.1153@news.indigo.ie>`

```
Peter,

Your post suggests that you are not aware that COBOL is also available on
NT, I would recomment NetExpress from Micro Focus. Check out
www.microfocus.com

Regards,
Paul


"Peter Nolan" <peternolan9@eircom.net> wrote in message
news:gpmz7.193$8s4.1153@news.indigo.ie...
> Richard,
> no reason so sinister....
>
> Simply put, very few (if any) people under the age of 30 speak cobol on
unix
> boxes nowadays.  If I want to use this code again and have it developed or
> maintained by grads with <5 years experience then it is going to have to
be
> in C.....
>
…[4 more quoted lines elided]…
> all, the programs are just file processing programs....what cobol was
always
> good at.
>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Converting Cobol to C

_(reply depth: 4)_

- **From:** "Jan de Nysschen" <jadeinfo@lantic.net>
- **Date:** 2001-10-27T08:42:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rdkrf$oan$1@ctb-nnrp1.saix.net>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz> <gpmz7.193$8s4.1153@news.indigo.ie> <9r9gbo$jtq$1@hyperion.eu.merant.com>`

```
Do you need to convert COBOL to C, Why , Because then you do not need a
COBOL compiler, Need some HELP, Contact Me.
Jan de Nysschen at jadeinfo@lantic.net I will be able to help.

Jan


"Paul Barnett" <paul.barnett@merant.com> wrote in message
news:9r9gbo$jtq$1@hyperion.eu.merant.com...
> Peter,
>
…[15 more quoted lines elided]…
> > boxes nowadays.  If I want to use this code again and have it developed
or
> > maintained by grads with <5 years experience then it is going to have to
> be
> > in C.....
> >
> > I personally understand all the arguements about both, and have used
cobol
> > on unix many times......but I think it is time to use C on unix/NT.
> >
> > I agree, all I will finish up with is cobol programs written in C.
After
> > all, the programs are just file processing programs....what cobol was
> always
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Converting Cobol to C

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2001-10-28T02:15:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yTJC7.143887$3d2.4795707@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz> <gpmz7.193$8s4.1153@news.indigo.ie> <9r9gbo$jtq$1@hyperion.eu.merant.com> <9rdkrf$oan$1@ctb-nnrp1.saix.net>`

```
    I think that I remember some of the older Microfocus Cobol
compilers for unix required the presence of a C compiler in order to work.

    I don't know what sort of "C" it generated.  I suspect that
suicide would look good after a while if you had to deal with
the sort of code a compiler would generate.


"Jan de Nysschen" <jadeinfo@lantic.net> wrote in message
news:9rdkrf$oan$1@ctb-nnrp1.saix.net...
> Do you need to convert COBOL to C, Why , Because then you do not need a
> COBOL compiler, Need some HELP, Contact Me.
…[9 more quoted lines elided]…
> > Your post suggests that you are not aware that COBOL is also available
on
> > NT, I would recomment NetExpress from Micro Focus. Check out
> > www.microfocus.com
…[10 more quoted lines elided]…
> > > Simply put, very few (if any) people under the age of 30 speak cobol
on
> > unix
> > > boxes nowadays.  If I want to use this code again and have it
developed
> or
> > > maintained by grads with <5 years experience then it is going to have
to
> > be
> > > in C.....
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Converting Cobol to C

_(reply depth: 6)_

- **From:** Nestor Aragon <Nestor.Aragon@motorola.com>
- **Date:** 2001-10-29T15:42:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDD6ACF.F57C3F1A@motorola.com>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie> <3BCE729B.4310CE1C@Azonic.co.nz> <gpmz7.193$8s4.1153@news.indigo.ie> <9r9gbo$jtq$1@hyperion.eu.merant.com> <9rdkrf$oan$1@ctb-nnrp1.saix.net> <yTJC7.143887$3d2.4795707@bgtnsc06-news.ops.worldnet.att.net>`

```
Now it is not needed, we use Microfocus COBOL for UNIX and it works without the
need of C compiler, of course we have some procedures made in C and then call
from within the COBOL programs.
Nestor Aragon
Cracow Poland

Russell Styles wrote:

>     I think that I remember some of the older Microfocus Cobol
> compilers for unix required the presence of a C compiler in order to work.
…[60 more quoted lines elided]…
> >
```

#### ↳ Re: Converting Cobol to C

- **From:** "tj dombrowski" <tj@keldin.net>
- **Date:** 2001-10-21T04:20:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e2sA7.6214$J12.701554@newsread1.prod.itd.earthlink.net>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```
check out c for cobol programmers a business approach by jim gearing ISBN
0-8053-1660-4.  Its might be available from halfprice computer books are
ebay cheap.

TJ

"Peter Nolan" <peternolan9@eircom.net> wrote in message
news:z9fz7.7747$w5.48598@news.indigo.ie...
> Hi All,
> this is possibly not a 'popular' place to ask this question..
>
> I have a bunch of cobol with imbedded SQL statements doing simple things
> like read a file and update/insert into tables etc.  I want to convert it
to
> C. (No flames please).
>
> I was wondering if anyone attached to this newsgroup had experience at
cobol
> to C conversions for batch processing style programs.
>
…[8 more quoted lines elided]…
>
```

#### ↳ Re: Converting Cobol to C

- **From:** tal_rosenberger@hotmail.com (Tal Rosenberger)
- **Date:** 2001-10-21T22:27:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4151cf5b.0110212127.376398ba@posting.google.com>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```
"Peter Nolan" <peternolan9@eircom.net> wrote in message news:<z9fz7.7747$w5.48598@news.indigo.ie>...
> Hi All,
> this is possibly not a 'popular' place to ask this question..
…[13 more quoted lines elided]…
> Peter Nolan

Dear Peter Nolan,

What you probably need is Intercomp's MigrateIT.

If you are intersted, please send me your full contact details and I'll contact you.

Regards,
Tal Rosenberger
```

#### ↳ Re: Converting Cobol to C

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-22T13:24:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6VA7.560388$Lw3.34707715@news2.aus1.giganews.com>`
- **References:** `<z9fz7.7747$w5.48598@news.indigo.ie>`

```

"Peter Nolan" <peternolan9@eircom.net>

> I was wondering if anyone attached to this newsgroup had experience at
cobol
> to C conversions for batch processing style programs.

Will wonders never cease? COBOL to C!

I heard of a lot of the reverse, C to COBOL, but this is amazing!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
