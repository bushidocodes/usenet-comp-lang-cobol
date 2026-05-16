[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# embedded SQL/COBOL TimeStamp

_2 messages · 2 participants · 2001-06_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Date and calendar processing`](../topics.md#dates)

---

### embedded SQL/COBOL TimeStamp

- **From:** "clv" <clemus@orden.cl>
- **Date:** 2001-06-19T14:52:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2fa007$1@dnewserver.firstcom.cl>`

```
In Open Client embedded SQL/COBOL,
that data type I must use to receive a field of type timestamp ??

thanks.

clv.-
```

#### ↳ Re: embedded SQL/COBOL TimeStamp

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-20T11:00:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2fd989_1@Usenet.com>`
- **References:** `<3b2fa007$1@dnewserver.firstcom.cl>`

```
Use comp-2 with no picture.

it is a 64 bit floating pointing point number with the date as days since
1900 to the left of the decimal, and the time as a fraction of a day in
seconds to the right.

Pete.

"clv" <clemus@orden.cl> wrote in message
news:3b2fa007$1@dnewserver.firstcom.cl...
> In Open Client embedded SQL/COBOL,
> that data type I must use to receive a field of type timestamp ??
…[5 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
