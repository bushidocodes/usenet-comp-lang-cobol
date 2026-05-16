[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL for MVS question

_1 message · 1 participant · 1998-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: COBOL for MVS question

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998082804281500.AAA24003@ladder01.news.aol.com>`
- **References:** `<35DB5C13.176E@ibm.net>`

```
The  comments you are receving are exactly correct.  The new COBOL execution
environments in OS/390 must have LE, and the whole shooting match is RES.  

COBOL sevice modules are now less modules and more vectors, a la message
handling in primitive object oriented programming environments.

A call to a service routine is not so much resolvable as an address to goto but
a set of functions guaranteed by the product that must be performed before
control is returned.

In the message oriented program design context you do not construct solidified
executable behemoths.  Instead your deploy large arrays of executable
components that coalesce dynamically into a fluid mosaic.

With reference to the language service modules, the hard link is obsolete.
Right behind that is the fact that erstwhile traditional application managment
styles of statically linked application code is also, I regret to opine, passe.

You overall strategy has technical challenges in the new world.  Your target
market may not have COBOL, but it will likely have LE.

There are ways to get LE in pre-OS/390 environs (LE/370 for MVS ESA, for
example).  But the window will shut upon that course for your clients.

For the intermediate, a possible combination approach may involve back-versions
of the linker/binder for clients not yet on OS/390, to support their LE/370,
and forward- version  linker/binder for those racing ahead into Y2K compliance
early with OS/390.

Fortunately, the COBOL 85 standard syntax COBOL code you develop should be
deployable across this temporary morass, as long as you do not rely on the
FUNCTION jazz.
(Although complete Y2K compliance on behalf of your more modern customers may
require certain alternations in select soure modules).

You can do all of this, but if you are like the rest of us, resources are
short, the new COBOL and LE learning curve is steep and long, ... so really,
... the best thing is to keep it simple.  Target one environment; the full Y2K
compliant environment, OS/390.  OS/390 comes with LE in towe.

It is a fact that the extremely broad based switch to the new technologies can
have a devastating effect on some companies markets. As a technician, you may
be the first to fully recognize the implications, not top management, and not
the product marketers.

It may seem an inconveneience, but your clients need to get to Y2K right
quickly. If they are not talking OS/390, you need to help them.  If they are
not talking OS/390 soon, you  need to help them.

If you are planning to relaease hard linked monoliths some one needs to help
you.  Trust me,  I know that it is not easy to change such a fundamental
concept as your link strategy.
If you respond in time, your product will have a bright future.

By the way, the FCC abend problem mentioned by one of the responders to this
thread is very important. It can bring a Y2K project to a dead halt for an
intolerable period of time.
All hands could potentially be idle while the organization swallows that pill. 


The Abend basically means that some module (a COBOL service module or
LE/370/390 gizmo) has hauled off and tried to execute an SVC that is not in the
hardware.  SSCCRREECCHH!
 
It is a fact that many COBOL application projects on planet earth do not even
have in their possession a single piece of paper with a single word on it that
would give even the slightest clue as to what this is.

It can happen in neat situations like COBOL programs with internal sorts, where
the sort ultimately invokes an access method (which takes us back to COBOL
sevice) routines.

If the victim has SyncSort, they think it is not Y2K compliant or that the
manuals need updating.

When the support gurus finnally recover from this braod-side, the answer that
eminates from their quarters natually leaves the COBOLers asking "what's an
SVC?"













Robert Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
