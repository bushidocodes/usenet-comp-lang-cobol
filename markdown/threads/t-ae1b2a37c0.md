[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Time from 24 hr to US

_1 message · 1 participant · 2000-12_

---

### Re: Time from 24 hr to US

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-12-07T10:06:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wAOX5.3437$NB1.94589@news2.atl>`
- **References:** `<20001207005738.18787.00001411@ng-cn1.aol.com>`

```
"Deek40" <deek40@aol.com> wrote:
> I am trying to get like 00:53 to like 12:53 .  i am stuck how would i
> change that?


03  HourMin.
    05  Hour  pic 99.
    05  Min   pic 99.

if Hour > 12
    subtract 12 from Hour
else
    if hour < 01
        add 12 to Hour.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
