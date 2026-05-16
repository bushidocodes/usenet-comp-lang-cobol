[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Porting source from Win32 to MVS

_4 messages · 4 participants · 1999-10_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Porting source from Win32 to MVS

- **From:** Alessandro Santini <a.santini@cgi.it>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38057BD7.B772537E@cgi.it>`

```
Hi everybody,

does anyone of you know if there is a development suite which allows
no-intervention source compatibility from Win32/ODBC to MVS/DB2?

Thank you in advance,

Alessandro
```

#### ↳ Re: Porting source from Win32 to MVS

- **From:** JohndeV <johndevNOjoSPAM@yahoo.com.invalid>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0a0133f8.8e59afdb@usw-ex0102-010.remarq.com>`
- **References:** `<38057BD7.B772537E@cgi.it>`

```
Alessandro

Check the Micro Focus Site, actually it is now Merant.

http://www.merant.com/ads/


* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Porting source from Win32 to MVS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u55f6$noq@dfw-ixnews16.ix.netcom.com>`
- **References:** `<38057BD7.B772537E@cgi.it>`

```
Coming from a Micro Focus (now MERANT) background, I would suggest that you
look at their products.  However, you should also consider:

  A) IBM's VisualAge (and related products) - this is compatible - because
the "front-end" is actually the identical code.
  B) CA-Realia (definitely targeting the "off-loading" environment)
  C) Fujitsu (I personally think they are more in the Workstation or
Client/Server "target" market than offloading development - but they do have
some IBM mainframe compatibility.  HOWEVER, the last that I checked they did
NOT support the latest IBM mainframe compiler, i.e. IBM COBOL for OS/390 &
VM - with MLE.)
  D) IMHO, RM and AcuCOBOL aren't really in the IBM compatibility business,
but you might still want to check them out.
  E) As far as I know, PerCOBOL totally ignores this market (but would allow
you to develop on the PC and port to a "JAVA-ish" mainframe environment.)
```

#### ↳ Re: Porting source from Win32 to MVS

- **From:** Ed Stevens <ed.stevens@home.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ohwGOLH=QyfPladNsETLPdROjbLy@4ax.com>`
- **References:** `<38057BD7.B772537E@cgi.it>`

```
One approach (and possibly the only one that gives the best chance
source level compatibility) is to not re-host the program in the first
place.  If it is already accessing a data via ODBC, all you need is a
gateway product and appropriate ODBC drive to reach DB2/MVS from the
PC.  With that approach, you shouldn't have to touch the PC pgm (well,
not exactly, as I'll explain in a minute) but simply define a
different ODBC Data Source Name to point through the gateway to DB2.
The pgm will never know the difference --- EXCEPT  . ...  not all
RDBMS's are created equal.  Just has you have vendor extensions to the
COBOL language, you have vendor extensions/interpretations to the
relational data model.  For instance, DB2 has a data type called
"timestamp" which holds time down to the hundredth (thousandth?  I
don't work with it daily, and don't have a manual handy) of a second,
as well as a "date" type and a "time" type.  Most other RDBMS's have
no equivalent to "timestamp" and combines "date" and "time" into a
single data type.  There are also vendor specific
variations/extensions in the SQL language itself.  All this would have
to be accounted for in any porting project.  I would assume that if
you are porting an application pgm from the Windows world to the MVS
world, you are also porting the database, so you would have to
consider these differences in the database design as well as the
application.

Another thing to consider if you decide to actually port the app
itself is that the Win/32 app may very well be doing things for which
there is no equivalent in the MVS world, and therefore no possibility
of 'no intervention' translation.  Things like, perhaps, an API call
to get information from the system registry, or almost any user
interface things.

On Thu, 14 Oct 1999 08:44:39 +0200, Alessandro Santini
<a.santini@cgi.it> wrote:

>Hi everybody,
>
…[5 more quoted lines elided]…
>Alessandro

Ed Stevens/TN
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
