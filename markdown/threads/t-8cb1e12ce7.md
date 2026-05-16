[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT x FROM DATE issue

_1 message · 1 participant · 1998-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Date and calendar processing`](../topics.md#dates)

---

### Re: ACCEPT x FROM DATE issue

- **From:** "Paddy Coleman" <pc@microfocus.com>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71mgvp$nd@hyperion.mfltd.co.uk>`
- **References:** `<1997Jan15.171737.14661@RedBrick.COM> <kudra.853354119@hubcap>`

```
The latest Micro Focus products (3.4, 4.0 and NetExpress) support the new
ACCEPT x FROM DATE syntax which will return a four digit year.  The
syntax is as follows:

...
ACCEPT x FROM DATE YYYYMMDD.
...

Where x is a PIC X(8) or equivalent.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

sallie j kudra wrote in message ...
>phorn@linkline.com (Paul Horn) writes:
>
>>Anyone have a good workaround for the fact that the ACCEPT identifier FROM
>>DATE command gives only two digits for the year? I'm coding some routines
to
>>timestamp output files and would feel sort of stupid if they "expire" in
three
>>years.
>
…[19 more quoted lines elided]…
>===========================================================================
=====
>  Think of me what you will          | Sallie Kudra, Applications Analyst
II
>  I've got a little space to fill... | ISD, Clemson University, Clemson, SC
>                 Tom Petty           | kudra@hubcap.clemson.edu
>===========================================================================
=====
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
