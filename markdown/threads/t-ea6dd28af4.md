[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Power Cobol Using Janus Dbgrid

_1 message · 1 participant · 2002-08_

---

### Re: Power Cobol Using Janus Dbgrid

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-08-10T06:01:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0208100501.2e64c0f@posting.google.com>`
- **References:** `<3D528AE5.6E7D6D76@attglobal.net>`

```
I do have some experience with this control using Fujtisu COBOL with
COBOL sp2 from Flexus and their ActiveX support.  I don't know how
PowerCOBOL handles events, and populating the grid is all tied up in
the events.  With this control when you do not have an associated
database, you need to setup the grid - and then wait for the
"UnboundReadData" event.  BEFORE you return from that event you have
to do your set's for the values for the grid.  The cell needing
population will be passed by the event.  The setting of the values
requires using the object reference returned by the event and is only
valid within the context of the event - once you return from the
event, using that object reference that was returned is invalid.


Carlos Lages <clages@attglobal.net> wrote in message news:<3D528AE5.6E7D6D76@attglobal.net>...
> Hi folks
> 
…[18 more quoted lines elided]…
> ps. Power 6.1
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
