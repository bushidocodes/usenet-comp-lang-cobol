[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe Express Enterprise Edition

_2 messages · 2 participants · 2004-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Mainframe Express Enterprise Edition

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-06-09T03:16:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aivxc.7422$uX2.5032@newsread2.news.pas.earthlink.net>`

```
to: comp.lang.cobol & IBM-MAIN

I attended Micro Focus' "Mainframe Express Enterprise Edition" launch today and
found it interesting (especially with my background both with IBM mainframes and
Micro Focus).  For those interested in seeing what the new product offers, may I
suggest that you go to:

  http://www.microfocus.com/_ex/products/mfeee/tutorials/

and "play" with the live tutorial.

If you want "fact sheets" and all that stuff, you can find it at:

   http://microfocus.com/products/mfeee/index.asp

***

This shouldn't be "confused" with their "lift and shift" offerings (best used
for migrating existing IBM mainframe applications to other platforms) that you
can read about at:

  http://microfocus.com/solutions/migrate/

***

For comparison (with MFEEE - Mainframe Express Enterprise Edition), you might
want to look at IBM's own

"IBM WebSphere Studio Enterprise Developer V5.1.1 brings J2EE, Web services,
rapid development, and teaming to diverse Java, COBOL, and PL/I application
environments"

See:

    http://www.ibm.com/isource/cgi-bin/goto?it=usa_annred&on=204-066

or even  CA's

"Advantage CA-Realia II Workbench "

See:

  http://www3.ca.com/Solutions/Product.asp?ID=1475

***

IMHO - none of the other COBOL vendors (Fujitsu, RM, AcuCorp, etc) really
provide full "IBM mainframe development off-loading workbenches" to compare with
these - although several other compiler vendors provide products that can handle
(at least older) IBM COBOL source code.
```

#### ↳ Re: Mainframe Express Enterprise Edition

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-10T16:46:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406101546.563ab0fc@posting.google.com>`
- **References:** `<aivxc.7422$uX2.5032@newsread2.news.pas.earthlink.net>`

```
Bill,

thanks for the private post as well as this public one.

I was VERY interested to see the component generator tool that is part
of this.

Some comments below...

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<aivxc.7422$uX2.5032@newsread2.news.pas.earthlink.net>...
> to: comp.lang.cobol & IBM-MAIN
> 
…[47 more quoted lines elided]…
> (at least older) IBM COBOL source code.

>>>
Yes, these tools are impressive.

However, I still have a few reservations.

The e-biz transaction generator uses a "language" that is NOT COBOL. I
would have thought that MicroFocus would learn from the experience
with DIALOG (which also had its own language) and use COBOL for this.
There was nothing wrong with the DIALOG language and the e-biz
transaction language seems to be pretty simple also, but why add
something to the equation when COBOL can handle it nicely? I remember
that when I moved from MicroFocus to Fujitsu I was relieved to be able
to write "DIALOG event processing" in COBOL; it just makes it all
simpler.

For me, it was particularly interesting to see a drag and drop
interface that can lever existing COBOL legacy code into standard
components. While purists may argue that the "interfaces" to these
components are not true component interfaces (they are really
properties of the bean or component)and using this tool does not
appear to produce clearly defined Methods and Properties, for many
mainframe COBOL programmers this will be a welcome introduction to the
world of component based design.

I was surprised to see the mainframe being relegated to a "big server"
role in the multi-tier design, with everything driven from the middle
tier, but, on reflection, there is really no other way that would make
sense.

As the cost of these tools will be prohibitive for individuals (and
not many of us have a mainframe in the garage anyway), it will be
interesting to see if corporations will invest in the necessary
training of their existing people in order to bring their legacy code
into the 21st Century. (The alternative would be to simply re-develop
existing apps as their shelf life runs out, using the many tools that
are available. Either way, it is bleak for "The future of COBOL" which
MicroFocus have bravely taken as their catchphrase. If you buy their
tools you end up with Java Beans (or .NET). If you don't buy their
tools you may well still end up with Java Beans (or VB, or .NET)...

It will also require some affinity for the Client/Server environment
on the part of the staff concerned and, in my experience, this is
often absent; for the most part, they see the PC and the Network as
the "enemy". Hopefully this is changing.

I could see many existing CICS installation using these tools to
convert CICS transactions into e-biz transactions, and the support for
doing this is really fantastic in the tools. I was very impressed with
the automatic analysis of work flow and decomposition into components.
Together with the processing of screens and COMM areas, I think this
is the most marketable part of the whole package.

Most of my "reservations" are really "niggles"; on the whole it is an
excellent implementation and MicroFocus are to be congratulated.

I wish them every success with it.

Pete.

PS Wasn't the tutorial excellent? Many companies could take a lesson
from this exemplary presentation. I found it encouraged me to want to
do it over.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
