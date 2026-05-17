[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

_10 messages · 5 participants · 1998-03 → 1998-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Object-oriented COBOL`](../topics.md#oo)

---

### MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-03-31T22:34:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fscdt$v6g$1@nnrp1.dejanews.com>`

```

I am looking to build contacts to share information and problems with
building an application with OO COBOL. I am actually building one now and
have run into a number of road blocks. I have been told by MicroFocus that
they are not even making fixes to this product now as all of their efforts
are concentrated on their Net Express Tool and Y2K Consulting ....

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6fscdt$v6g$1@nnrp1.dejanews.com>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com>`

```

gen··.@ste··m.com wrote in message <6fscdt$v6g$1.··.@nnr··s.com>...
› I am looking to build contacts to share information and problems with
› building an application with OO COBOL.  I am actually building one now and
…[5 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading

You do understand that NetExpress contains all the OO support (and more) of
the older Visual COBOL product don't you? What they are saying is that the
fixes are going into the current release, not the old one.
```

##### ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-04-01T22:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p2@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap>`

```

In article <6fsga4$l.··.@dfw··m.com>,
"William M. Klein" wrote:
› 
› gen··.@ste··m.com wrote in message <6fscdt$v6g$1.··.@nnr··s.com>...
…[20 more quoted lines elided]…
› 

I do know that NetExpress has the OO support. However after talking to
technical support at MicroFocus even less has been done with the OO Class
libraries in the NetExpress product than in the WorkBench product. And
NetExpress is not the new release. It is a different product altogether.
Workbench is still the current product, however a new product WorkBench 2000
is in the works which will be the next release of the WorkBench product.
Having said all that they are no doing anymore work now with the OO Support
in NetExpress either ... they are on the "Web Development and Y2K" show me
the money bandwagon ... (which is not that unusual ... still have to feed the
cat)

Another big down side (to me or other cross-platform developers) is that the
NetExpress product is a windows only solution. The closest I have been told
(again by tech support) is that you might be able to take code generated from
NetExpress and compile it with the WorkBench product.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p3@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap>`

```

Gene,

With you permission I would like to step in here and clarify some of your
points.

1) NetExpress does have full OO COBOL support. The statement about this
support being limited is strange and in my opinion incorrect. The OO
support
in NetExpress (GUI, OLE etc) is extensive and very powerful. For example:

The GUI class library in Workbench 4.0 is based on Panels 2. This means you
get portability but inherit the restrictions of Panels 2. In NetExpress the
GUI
class library is based on the native Win32 API which means enhanced
functionality and performance.

OLE class library - in 4.0 there is only support for production ole clients.
In
NetExpress this has been extended to cover ole servers as well. There is
also
an OLE wizard in NetExpress which greatly simplifies the creation of these
programs.

2) NetExpress 2.0 is our latest distributing computing product. It was
released
last December and has been very well received in the market. You are
correct
when you say it is a different product from Workbench - it does have a new
compiler, runtime and development environment. This product will *not* be
replaced by Workbench 2000!

Workbench 2000 is now available and is a repackaging of Workbench 4.0. It
brings together all our 32 bit tools on to one CD and is targeted at the
Offload
market. Workbench 4.0 is still available for those Customer's who do not
want NetExpress (?).

3) As far as I am aware the OO in our COBOL is fully supported and
development
is continuing. It is true to say that a major focus of ours is the web and
Y2K but
this is not at the expense of NetExpress and our other distributed computing
solutions.

4) You are correct when you say that NetExpress is a Win32 product. It
does have
the "Publish to UNIX" option within it however. This means you can develop
on
a PC and deploy on UNIX. For those Customer's wishing to target DOS or OS/2
we still have the Workbench products available.

5) My Team in the UK are still actively supporting the 4.0 product line.
We raise
issues with our Developers and deliver fixes to our Customers. I am not
aware that
this policy has changed. I think the Engineer you spoke to in the U.S. is
misinformed.

I hope the above is of help to everyone on the newsgroup. If anyone has any
specific
concerns about Support please feel free to email me and I will be happy to
look in
to it for them.

Many thanks.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus UK.

› 
 
 
› gen··.@ste··m.com wrote in message <6fuuqb$7k2$1.··.@nnr··s.com>...
› In article <6fsga4$l.··.@dfw··m.com>,
…[54 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

_(reply depth: 4)_

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-04-02T10:51:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p4@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap> <gap-b0c9be262a-p4@usenetarchives.gap>`

```

In article <6fvfap$1.··.@hyp··o.uk>,
"Paddy Coleman" wrote:
› 
› Gene,
…[129 more quoted lines elided]…
› 
Thanks for your input. Let me start of by saying that I have used MicroFocus
products for the last ten years (even when I had the opportunity to change to
other vendors and in one case where all of the tools and support were offered
free!).

This thread is not meant to be a knock on MicroFocus as a company or a
product. However! Having said all of that ... I have had numberous problems
and have been unable to get technical support for the OO version of the
product.

I don't feel it is appropriate to carry on this thread much further in the
newsgroup. Anyone who would like more information as to problems that I have
run into (be it MicroFocus personnel or just interested by standers) lets do
it via email.

I personally would love to see OO COBOL flurish as I think it has a great
potential.

I have based my comments on email received from MicroFocus technical support.
While it would not be fair to publish that email here I would be happy to
pull the person's name off and forward it to anyone who is interested.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

_(reply depth: 4)_

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-04-02T17:20:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p4@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap> <gap-b0c9be262a-p4@usenetarchives.gap>`

```

In article <6fvfap$1.··.@hyp··o.uk>,
"Paddy Coleman" wrote:
› 
› Gene,
…[129 more quoted lines elided]…
› 
Thanks for the clarification. In specific I am concerned with the file
handling and file key class libraries. I learned today that these are not
even supported in NetExpress. How can something so fundamental as file
handling (I have never worked on a project of any size that didnt access
files)be left out. I realize you can still use the good old fashioned
methods to access indexed and relative files ... but doesnt that just make
building generic class clibraries and reusable code a whole lot harder?

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "smb" <ua-author-13098204@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p3@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap>`

```

In article <6fuuqb$7k2$1.··.@nnr··s.com>, gen··.@ste··m.com wrote:
› I do know that NetExpress has the OO support. However after talking to
› technical support at MicroFocus even less has been done with the OO Class
› libraries in the NetExpress product than in the WorkBench product.

Untrue. The OO class libraries in NetExpress are actively being developed,
and use the native Windows APIs for the GUI classes. This has *extended*
the capabilities of the class libraries.

› And NetExpress is not the new release. It is a different product altogether.

Not the new release of Workbench, but a new product (it first appeared in
1997). The OO support in NetExpress supercedes that in Workbench.

› Workbench is still the current product, however a new product WorkBench 2000
› is in the works which will be the next release of the WorkBench product.
…[3 more quoted lines elided]…
› cat)

Again, the OO support is being actively developed in and for NetExpress.
NetExpress *also* has Web development support.
The Y2K product is SoftFactory/2000.

[Snip]

Steve.
(MF Development, NetExpress)
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

_(reply depth: 4)_

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-04-02T10:45:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p7@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap> <gap-b0c9be262a-p7@usenetarchives.gap>`

```

In article <6fveut$s.··.@hyp··o.uk>,
s··@mfl··o.ukx (Steve Biggs) wrote:
› 
› In article <6fuuqb$7k2$1.··.@nnr··s.com>, gen··.@ste··m.com wrote:
…[34 more quoted lines elided]…
› 
Would you mind outlining (briefly) the enhancements to the class libraries in
the NetExpress product versus the WorkBench product. I have submitted bug
fixes to the class libraries in the WorkBench product only to be told that
"nothing will be done with them"

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

_(reply depth: 5)_

- **From:** "smb" <ua-author-13098204@usenetarchives.gap>
- **Date:** 1998-04-01T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b0c9be262a-p8@usenetarchives.gap>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com> <gap-b0c9be262a-p2@usenetarchives.gap> <gap-b0c9be262a-p3@usenetarchives.gap> <gap-b0c9be262a-p7@usenetarchives.gap> <gap-b0c9be262a-p8@usenetarchives.gap>`

```

In article <6g0bom$scj$1.··.@nnr··s.com>, gen··.@ste··m.com wrote:
› Would you mind outlining (briefly) the enhancements to the class libraries in
› the NetExpress product versus the WorkBench product.  I have submitted bug
› fixes to the class libraries in the WorkBench product only to be told that
› "nothing will be done with them"

We are maintaining Workbench issues here in Development, but not actively
developing the product. Quite a few areas in the original Workbench releases
of Object COBOL were early-release items (and marked as such), and are no
longer actively maintained.
(Of course, there is nothing to stop you taking the original class sources
from WB and making them your own new class in NetExpress!)

The class libraries in NetExpress comprise of the same basics of Workbench
(Base, GUI, OLE) but everything is full release.

The main changes are in OLE automation support (we now have full client and
server functionality), GUI support (using the native Win32 APIs) and
improvements in speed and usability (Object COBOL browser and wizards in the
IDE). Most of the base classes have been very little changed, since they were
well designed to being with, except to add more functionality and streamline
their operations.

Hope that's answered the question,
Steve.
Micro Focus Development.
```

#### ↳ Re: MicroFocus OO Compiler (4.0.32) or Any OO COBOL Compiler

- **From:** "angel..." <ua-author-877667@usenetarchives.gap>
- **Date:** 1998-04-03T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b0c9be262a-p10@usenetarchives.gap>`
- **In-Reply-To:** `<6fscdt$v6g$1@nnrp1.dejanews.com>`
- **References:** `<6fscdt$v6g$1@nnrp1.dejanews.com>`

```

good evening, I am a new user to microfocus cobol.
I have the 32 bit edition with the cics option and sql,
I really need assistance in configuring and setting up the
environment, if you can help it will be much appreciated
thank you in advance
marc
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
