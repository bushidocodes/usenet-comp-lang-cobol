[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with datatype float

_1 message · 1 participant · 1996-07_

---

### Problems with datatype float

- **From:** "j.j.g. daamen" <ua-author-8579834@usenetarchives.gap>
- **Date:** 1996-07-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31D9187F.9C9@bvh.nl>`

```

Regards: Problems with number of datatype "float" and "real" in SYBASE
SQL-server V4.9.2
Differences with floating point numbers on Digital VAX/OpenVMS
versus ALPHA/OpenVMS in COBOL


Flower Auction Holland is a company that is selling all kinds of
agricultural products, that have a decorative value
(amongst other products all kinds of cutflowers and potplants).

The auction uses DIGITAL VAX/OpenVMS computers and ALPHA AXP/OpenVMS
computers, as well as a number of UNIX-systems.

Most of the applications are client/server applications,
the server being a SYBASE SQL-server.
All SYBASE SQL-servers are currently of release V4.9.2.
This release is operational on both the VAX/OpenVMS systems (EBF-level
4156),
as well as on the ALPHA AXP/OpenVMS (EBF-level 4158). Although the
binaries,
of course, differ, both versions should be functionally equivalent.

The Flower Auction is considering migrating the two SQL-servers that are
handling it's two main sales-processes from the VAX/OpenVMS platform to
the
ALPHA AXP/OpenVMS platform. Because of the importance of these servers
for
the sales processes, some initial testing has already been performed in
advance of the migration itself. These tests have been conducted with
the
aforementioned EBF4158. During our initial testing on this server, we
found
considerable differences with regards to the handling of the "float"
datatype. Both the VAX and the ALPHA do produce results that suffer from
inprecision in the third (!) decimal.
For instance, 1.001 * 1000 produced 1000 instead of 1001, and 1.005
rounded to two decimals produced 1.00 instead of 1.01.
Moreover, the results are not cross-platform consistent: sometimes the
VAX
is more accurate, sometimes the ALPHA, although the VAX does seem to be
the
more precise platform in most of the cases. The reason appears to be the
1-to-1 mapping from datatype "float" to a machine-dependent datatype,
while
SYBASE does not provide for a certain minimal accuracy or cross-platform
consistency. The problem is reported to be similar for the "real"
datatype,
but we have not tested that, since our company does not use the "real"
datatype.

SYBASE itself is very reserved and only recommends an upgrade to System
10
or System 11 with simultaneous conversion to the "numeric" or "decimal"
datatype as a possible solution. In handling these datatypes, SYBASE has
provided for cross-platform independency and better accuracy. However,
for
the Flower Auction this is not a viable solution at this moment in time.


Hence the following questions:

* Is there any company with knowledge of functional and/or technical
problems
connected to a migration from SYBASE SQL-server V4.9.2 from a
VAX/openVMS
platform to an ALPHA/OpenVMS platform, that is willing to share this
knowledge with the Flower Auction ?
* Is there any company, that knows of other companies that already have
performed a similar migration, or that are currently in the process of
performing this migration ?
* Is there any company with knowledge of any work-arounds (and the
possible
impact of these work-arounds) to compensate for the inaccuracies on
the
V4.9.2 platform ?

Any COBOL-program with floating point arithmetic is likely to produce
different results when compiled, linked and run on the ALPHA/OpenVMS
(DEC COBOL V2.0-271) versus on the VAX/OpenVMS system (VAX COBOL
V5.1-10).
Both the accuracy and the way expressions with mixed datatypes (e.g.
integer
and floating-point) are handled, differ. The results can be very
surprising
in a negative way ! So far, we have not been able to get through to the
DEC Porting Centre, so we do not know DIGITAL's view on this topic.

Hence the following questions, similar to those connected to the
floating
point problem with SYBASE:

* Is there any company with knowledge of functional and/or technical
problems connected to platform VAX COBOL V5.1-10 versus DEC COBOL
V2.0-271,
that is willing to share this knowledge with the Flower Auction ?
* Is there any company, that knows of other companies that already have
performed a similar migration, or that are currently in the process of
performing a migration from a COBOL-application from VAX/OpenVMS to
ALPHA/OpenVMS ?
* Is there any company with knowledge of any work-arounds (and the
possible
impact of these work-arounds) to compensate for the inaccuracies and
the
differences ?

Everyone who is willing to reflect on this, should email to
jda··.@b··.nl


With kind regards John Daamen (Technical Consultant IT-Infrastructure).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
