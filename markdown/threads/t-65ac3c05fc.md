[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe Software Packaging.

_9 messages · 5 participants · 2002-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Mainframe Software Packaging.

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-20T02:17:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com>`

```
    I'm looking for some advice on an application 

and its packaging for the Mainframe. I'm just about to 

release my Asset Management and Recurring Billing 

packages into the OS/390 market, and to tell the truth, 

packaging is really throwing me a curve. :)  

 

  On the mainframe, these are COBOL and a few assembler 

programs, currently ported to take advantage of LE and TX Server.

I have a few issues there:

 

  I want to release a version that runs VSAM to avoid the cost of 

  DB/2, and wonder if anyone has advice about how to deliver 

  the empty VSAM files. I currently plan to just deliver a IDCAMS

  job and custom COBOL program to create, load, index, and test

  the files. This would also allow an installation to easily customize

  the VSAM catalog it uses, the sizes and other tunable parameters,

  and the names. However, I want to come up with a good workable 

  default. It takes a good deal of savvy to create the dozens of VSAM

  files and indexes necessary to run the application, and some of the

  potential customers might not have the savvy or the resources to 

  expend on a lot of customization. The IDCAMS job takes a HLQ

  as a parameter, and creates its own VSAM catalog. It also uses

  my preference for a naming schema for the files, indexes, and paths.

  Is this a reasonable approach?



  The CICS resources are all in their own group with a basic job to load

   them. It still has to be modified on site to adapt the HLQ for the 

   VSAM files.  This seems like the least possible trouble for a end user. 



   Of course, I know the system inside and out, but from a dead standing

   start, I can install the Asset Management app in about 30 mins. That 

   is without the internal setup and customization that the application 

   requires internally. (i.e. Setting up asset tag ranges and all sorts of 

   "application only" stuff.)   



A definite issue is that TX Server with LE seems to present a few 

differences from CICS/ESA. BMS maps that work perfectly well 

under CICS in a non LE environment give me junk data 

problems under TX Server in a LE region. This means that

I am doing things for LE that make it not a good idea to run under

ESA.  (?) 

 

My current thought is to 'package' the application for 

TX Server and LE. I know this limits the immediate

usefulness of the software to some people - I'm willing 

to be convinced that multi-packaging is necessary. :) 

 

Secondly, similar to what I do with workstation and 

OS/400 versions of the software, I want to offer a 

range of licensing options; from a very low cost 

binary only distribution to a version with source and 

redistribution rights. By low cost, I mean perhaps as 

low as $2500 for a single application with maintenance 

of about $1000/year. (That's the projected cost for the

Asset Management application. I use it as a bit of a

loss leader; it solves a need for some organizations 

and it gets my software in the door very fast. That's

the pricing for the AS/400 version  - I would like to 

maintain that price in the OS/390 world if at all possible.) 



I'm kind of wondering if it even makes sense to have a 

non-source distribution in the OS/390 world, and is at the 

core of this message. Would most systems folks feel comfortable

installing a binary only package? I'm more concerned with meeting



I have one client on the AS/400  who regularly customizes 

the software and puts it up as an ASP application for 

their clients. Works great for me, as I made the licensing 

cheaper for them if they gave me the right to include software fixes

they make into the general distribution. :) 

 

 Third, I would like to tap into a potential but pretty well 

non-existent Mainframe Market - small business. 

 

Short of spending a million dollars I do not have to host an 

ASP version of the software under OS/390, I think there is a 

definite S/390 market for the business willing to invest say 

$70K to $125K in their hardware and software investment. 



At that level, it will have to involve Flex, UMX, or (better yet) 

low cost MultiPrise systems. I am not at all happy with the Flex 

people. They are focused on defending their small piece 

of turf instead of growing new markets. They do an alright 

deal through some resellers for PWD development systems, 

but they are patronizing towards the idea of entering the small

business market.  I don't know enough about UMX to make any 

reasonable choices there. That leaves the MP market, which 

is 'high end' for the small business in the $1 - $10m /year market. 

Still, it is a potentially very profitable area, and opens lots of 

avenues for support. Obviously, in that market, support and 

the recurring revenue stream it generates is the primary

goal.

 

The MP is a very possible scenario, with some creative leasing

from IBM. (I love IBM, even if they can be aggravating to deal with.)  

 

Lastly, I've been tentatively exploring Linux on the S/390 platform. 

I must say, I am not convinced there is any vast advantage to it 

at this time. A z800 is impressive and nicely priced, but what the 

heck does it do to make the great price difference between it and 

an RS/6000? (Excuse me, pSeries machine.)  RS/6000's in useable 

configurations, with OS software, start in at about $2700. 

 

I do not think that Linux on an S/390 can be targeted towards a 

small business at this time, other than perhaps running under something 

like Hercules. And except for clean upward scalability, why take the 

performance hit to do that? COBOL development tools from IBM are 

not there yet either. 

 

Still, I have the nagging feeling that I am missing something here. 

Opinions welcome!

 

Sorry for the long post, but I am looking for opinions and advice 

here, even if it is something I don't really want to hear. :) 

 

Thanks 

-Paul
```

#### ↳ Re: Mainframe Software Packaging.

- **From:** Richard Fuller <rfuller1@pdq.net>
- **Date:** 2002-04-20T23:39:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CC1FC71.6040401@pdq.net>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com>`

```
Why don't you go out in the field and do the installations. For a fee, 
of course.

Paul Raulerson wrote:

>     I'm looking for some advice on an application
>
…[235 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Mainframe Software Packaging.

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-21T02:04:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m6pw8.24075$o86.953634@typhoon.austin.rr.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com> <3CC1FC71.6040401@pdq.net>`

```
Unreasonable expense and demands on my time. :)

Seriously, the business plan calls for not being onsite as much as possible,
to
keep the cost of the software low. The income is basically recurring revenue
for support. And even *that* should be an order of magnitude less expensive
than it currently is.

It also is something we think is wrong with the mainframe software
industry -
why should software be so complicated that you need to have a specialist go
onsite to install  and configure it?

After all, most Sysadmins are more than capable of managing their own
systems,
and no software anywhere should be so complex that it cannot be installed in
at
most, a couple or three hours.

We have a different philosophy as you can see. Whether or not it turns out
to
be nicely profitable yet remains to be seen, but we have faith. :)


-Paul


"Richard Fuller" <rfuller1@pdq.net> wrote in message
news:3CC1FC71.6040401@pdq.net...
> Why don't you go out in the field and do the installations. For a fee,
> of course.
…[6 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Mainframe Software Packaging.

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2002-04-21T20:10:09+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<210420022010090265%josephk@iinet.net.au>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com> <3CC1FC71.6040401@pdq.net> <m6pw8.24075$o86.953634@typhoon.austin.rr.com>`

```
In article <m6pw8.24075$o86.953634@typhoon.austin.rr.com>, Paul
Raulerson <praulerson@NO-SPAM.hot.rr.com> wrote:

> It also is something we think is wrong with the mainframe software
> industry -
…[8 more quoted lines elided]…
> 
Most Unix sys admins have a fixed file heirarchy to manage.

Such a thing DOES NOT EXIST on the mainframe.

You had better make ALL your file (dataset) names options on any
install jobs.

The most frustrating thing I finf as a sysprog for mainframes is PC
types not understanding that the programs are differentiated from the
data that they operate on.

In a typical mainframe environment the same programs may operate on
production data and a number of testing environment data sets. This is
possible because the programs only ever refer to DDNAMES or CICS files.

It is the responsibility of the SITE to determine when and what those
ddnames refer to.

To create a package for a mainframe that disobeys this concept is just
asking for trouble. Unlike Unix and Windows, Mainframe packages Must
differentiate between the programs and the data. They MUST NOT be
installed in such a way to force the user to accept what the supplier
wanted, but must be capable of reflecting what the user wants. The user
in this situation is NOT the company owner, but the system programmer
that is hired to run the show.

The closer you are to standard MVS operating principals you are, the
better your product will be received.

1. Ship the Product as a SMP/E package.
There is NO EXCUSE for not doing this.

2. Provide sample JOBS to create the Dataset's that the package will
need for operation.
Clearly label those datasets that are optional. Do not worry about the
dataset names as it will be a forgone conclusion that any naming
standard you come up with will offend someone. Furthermore, the nature
of the mainframe is such that any names you come up with will be
renamed by the local standards.

3. DO NOT require a unique catalog or catalogs for your product.
Catalogs are system management things and have nothing what so ever to
do with applications.

4. Ship sample jobs to run your application. Better would by a JCL
procedure that the system programmer can copy and modify to local
standards.

5. DO NOT Name your program libraries SYS1.anything. These are by
convention reserved for the operating system and as a default usually
have the highest level of security access applied to them. Security is
a customer issue, you have no rights to force this upon them.

6. DO NOT create PLT programs for CICS systems to INSTALL CICS
resources. DO create DFHCSDUP jobs and statements to define the CICS
resources. DO NOT create documentation that describes the CICS
resources to be defined and then provide no JCL and samples to define
them.

7. Ship the manuals as BookManager files, so that the standard library
reader can read them. Optionally, supply PDF's.

Hope this helps. :)
```

###### ↳ ↳ ↳ Re: Mainframe Software Packaging.

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-21T19:53:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pNEw8.20926$R33.1015039@typhoon.austin.rr.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com> <3CC1FC71.6040401@pdq.net> <m6pw8.24075$o86.953634@typhoon.austin.rr.com> <210420022010090265%josephk@iinet.net.au>`

```

"Joseph Katnic" <josephk@iinet.net.au> wrote in message
news:210420022010090265%josephk@iinet.net.au...
> In article <m6pw8.24075$o86.953634@typhoon.austin.rr.com>, Paul
> Raulerson <praulerson@NO-SPAM.hot.rr.com> wrote:
…[4 more quoted lines elided]…
>

It doesn't actually have to exist under UNIX either. We have seen a few
alien file systems we wish had never landed... (*sigh*)

> You had better make ALL your file (dataset) names options on any
> install jobs.
…[4 more quoted lines elided]…
>

Yes, we find the same thing. By the same token though, I think there is some
value in suggesting at least a standard file naming schema for the less
technically adept. (Actually, I tend to fall into that region my self. A
system
programmer I am not, though with a little help from my friends, I manage to
get done what I need to get done. Okay, make that a LOT of help... :)



> In a typical mainframe environment the same programs may operate on
> production data and a number of testing environment data sets. This is
…[4 more quoted lines elided]…
>
Most definately, we do this in every environment, AS/400, UNIX, and
even in Windows where possible. (With Windows it isn't always possible,
but we try... )


> To create a package for a mainframe that disobeys this concept is just
> asking for trouble. Unlike Unix and Windows, Mainframe packages Must
…[5 more quoted lines elided]…
>

MM- to some degree, I must disagree here. One thing our research has found
is that the very best shops do not have much, if any, of that separation
between
the sys progs and managment. Indeed, in those shops, management actually
makes the descisions, or at least approves them. We have seen really poor
efficiency caused by egos in other shops - those egos being either on the
sys progs side, management's side, or worse yet, on both sides.

At the bottom line, the people who authorize the money to be spent are the
people we have to satisfy, and that does mean not antagonizing their sys
progs.
It is a hard job to make *everybody* happy, but somebody has to do it!! :)
:) :)

Also, a relatively competent sys prog would have no problem changing any
dataset names they want, or setting up multiple copies of the software for
test/production etc. We have NOT built any of that knowledge into the
software
itself at this time. (In fact, that is one of the 'bones of contention' we
deal with
internally. Some of us think we should, some os us think we should not.
Mostly
we have all stated our point of view and just moved ahead. If we get it
wrong, we
will come back and do it over again - and do it more correct the
second/third/fourth,
or however many times it takes to get it right.)



> The closer you are to standard MVS operating principals you are, the
> better your product will be received.
…[3 more quoted lines elided]…
>

Do itty bitty shops use SMP/E much? Is there any reason to NOT use SMP/E for
them?


> 2. Provide sample JOBS to create the Dataset's that the package will
> need for operation.
…[27 more quoted lines elided]…
>

<grin> Well, we internally decided on PDF as the documenation ship vehicle.
There was some - ah - disagreement about that as well. The reason PDF's got
selected is the master-of-the-documenation uses a Macintosh, and really
likes
PDF's. Also he convinced us that most people are going to view the docs on a
PC anyway so....


> Hope this helps. :)

Very much indeed! Thank you -Paul
```

#### ↳ Re: Mainframe Software Packaging.

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2002-04-21T08:18:09+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ol4cuopdjor3cmp3lvr6pmik892ntb9dv@4ax.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com>`

```
On Sat, 20 Apr 2002 02:17:00 GMT, "Paul Raulerson"
<praulerson@NO-SPAM.hot.rr.com> wrote:
> The IDCAMS job takes a HLQ as a parameter, and creates its own VSAM catalog. 

This may or may not be a good thing.  Make it variable in such a way
that the customer can decide to place the files into an already
existing catalog

>  my preference for a naming schema for the files, indexes, and paths.

Very probably not a good thing.  customers already have a decided on
name space, and are reluctant to change.  Also, they may have rules in
place (like ACS routines for SMS) which makes changing the rules ...
difficult


>  The CICS resources are all in their own group with a basic job to load
>   them. It still has to be modified on site to adapt the HLQ for the 
>   VSAM files.  This seems like the least possible trouble for a end user. 

There is an even less intrusive approach:  EXEC CICS CREATE resource,
which can define CICS resources on the fly.  You would have to provide
a PLT program to do this once on CICS startup.  Other than that, the
approach looks fine to me.  The job that builds the IDCAMS commands
can as well build the DFHCSDUP commands to populate the CSD


>A definite issue is that TX Server with LE seems to present a few 
>differences from CICS/ESA. BMS maps that work perfectly well 
…[3 more quoted lines elided]…
>ESA.  (?) 

Hm, did you do MOVE LOW-VALUSES to mymapO before doing anything else
with the map?  If you don't  do this for CICS/ESA and above, you can
expect random data showing up in your map, and worse (PROG 705, ABEND,
whatever)

>
> 
I am not going to comment on the other issues,  I am a very happy
Flex-ES customer here, and an MP3K would be way out of my range,
monetarywise.....
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Doing gets it done.
      
        (Another bit of Wisdom from my fortune cookie jar)         


-----------== Posted via Newsfeeds.Com, Uncensored Usenet News ==----------
   http://www.newsfeeds.com       The Largest Usenet Servers in the World!
------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

##### ↳ ↳ Re: Mainframe Software Packaging.

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-21T19:41:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PBEw8.20882$R33.1013672@typhoon.austin.rr.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com> <5ol4cuopdjor3cmp3lvr6pmik892ntb9dv@4ax.com>`

```
Thanks Volker, good advice as usual! :)

"Volker Bandke" <vbandke@bsp-gmbh.com> wrote in message
news:5ol4cuopdjor3cmp3lvr6pmik892ntb9dv@4ax.com...
> On Sat, 20 Apr 2002 02:17:00 GMT, "Paul Raulerson"
> <praulerson@NO-SPAM.hot.rr.com> wrote:
> > The IDCAMS job takes a HLQ as a parameter, and creates its own VSAM
catalog.
>
> This may or may not be a good thing.  Make it variable in such a way
> that the customer can decide to place the files into an already
> existing catalog
>

That could be easily controlled by changing the HLQ onsite I think. In fact,
we are kind of confused
by the intricate possibilities of this issue. For example, one potential
client is a small publishing shop
running on a P/390. They don't have the onsite skillset to do deep analysis,
so we want to have a
setup there that is simple and very easy.

Another possible client is so far out at the other end of the range they
might as well be in a different
galaxy. *Everything* for this customer is going to be changed, if for no
other reason than their current
system progs' ego won't allow anything she has not changed on her system.
They may change system
progs soon and flip to the end of the spectrum evidenced by our potential
P/390 client.

Definately making it a variable thing is good, though I wonder if we should
should setup some kinf of
user freindly configuration program? That would probably be a lot of work,
but if it is worth doing, it
might save a lot of grief later. (?)


> >  my preference for a naming schema for the files, indexes, and paths.
>
…[4 more quoted lines elided]…
>

While anyone with any experience at all can easily change all the DD names
and the IDCAMS
job to set them up, finding the correct balance between simplicity and
flexibilty is a very hard
job. At least it is for me. :)

For the sake of support simplicity, we would like to be able to "strongly
recommend' that all the working
datasets retain the same HLQ and the same pattern we use for indexes and
paths. No compelling technical
reason to do so, but with clients at the lower end of the scale, this will
save us hours of support issues. (Did the
IDCAMS job fail for some reason? How to find out?  Go to ISPF 3.4, enter
HLQ, press enter, and read
off the list of files you see to us please... etc. etc.)


>
> >  The CICS resources are all in their own group with a basic job to load
> >   them. It still has to be modified on site to adapt the HLQ for the
> >   VSAM files.  This seems like the least possible trouble for a end
user.
>
> There is an even less intrusive approach:  EXEC CICS CREATE resource,
…[4 more quoted lines elided]…
>
 This sounds like a great idea for most of the potential clients. Why did
none of
us think of it before? Thanks Volker, I owe you (root) beer, your
preference.

>
> >A definite issue is that TX Server with LE seems to present a few
…[10 more quoted lines elided]…
>
I think we did, but it is a great idea to go and triple check. Some of the
screens are still changing,
do that is not a difficult task to assign and accomplish.  We actually see
PROG755's (bad data)
from PCOMM, so this is probably a lurking culprit. Funny thing though, the
other emulators we test
with seem to work okay. Just PCOMM putting up a bit of a fuss...

> >
> >
…[3 more quoted lines elided]…
>

Oh heck, I can't afford a personal MP3K myself (yet! :)  I really was
talking about clients
who are willing to spend around six digits of capital.


>      With kind Regards            |\      _,,,---,,_
>                             ZZZzz /,`.-'`'    -.  ;-;;,
…[8 more quoted lines elided]…
> -----------== Posted via Newsfeeds.Com, Uncensored Usenet News
==----------
>    http://www.newsfeeds.com       The Largest Usenet Servers in the World!
> ------== Over 100,000 Newsgroups - Ulimited downloads - 19 servers ==-----
```

#### ↳ Re: Mainframe Software Packaging.

- **From:** pdw@marcdatabase.com (Peter D. Ward)
- **Date:** 2002-04-21T11:52:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e5e370.0204211052.468385d9@posting.google.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com>`

```
"Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:<wc4w8.15343$R33.733039@typhoon.austin.rr.com>...

> I am not at all happy with the Flex 
> people. They are focused on defending their small piece 
> of turf instead of growing new markets. 

What is your idea of new markets that "the Flex people" are not
focused on growing?  I will be happy to provide some description of
our efforts in any new market that you can name.


> They do an alright 
> deal through some resellers for PWD development systems, 
> but they are patronizing towards the idea of entering the small
> business market. 

Can you provide an example of 
the "flex people" being patronizing toward "the idea of entering the
small
business market"? 

 Small business
production systems is our primary focus, and I am not aware that
you've ever have approached us or one of our many resellers with a
proposition involving your product.  We have many vertical application
resellers that are using or are considering Flex for hosting their
application either administered remotely in the customer's shop or as
an ASP, or of course, good old time-share.

Peter D. Ward
Fundamental Software
http://www.funsoft.com
```

##### ↳ ↳ Re: Mainframe Software Packaging.

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-21T19:27:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_oEw8.20833$R33.1009686@typhoon.austin.rr.com>`
- **References:** `<wc4w8.15343$R33.733039@typhoon.austin.rr.com> <4e5e370.0204211052.468385d9@posting.google.com>`

```
Sorry Peter - I replied to you much more fully offline. I certainly
did not intend to slam Flex, and rereading that it looks like I did.
We have not had great success in communicating with some of your
resellers our needs and intentions, and even less success getting
quotes back from them that are appropriate to use in a quote to a
potential customer. Part of this is just that we have not dug out all the
facts regarding how you do business yet, and where, if anywhere,
our business plan and your operation can and should work together.
We are, however, at the point where we can talk a bit more openly
about our business plan and strategies, so perhaps my opinion will
soon change.

I'll restate publicly that your personal contacts with us have been
appropriate and useful.

 Thanks
-Paul


"Peter D. Ward" <pdw@marcdatabase.com> wrote in message
news:4e5e370.0204211052.468385d9@posting.google.com...
> "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message
news:<wc4w8.15343$R33.733039@typhoon.austin.rr.com>...
>
> > I am not at all happy with the Flex
…[28 more quoted lines elided]…
> http://www.funsoft.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
