[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Powercobol to initialize the fields at run-time at zero binary

_2 messages · 2 participants · 2007-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Powercobol to initialize the fields at run-time at zero binary

- **From:** "Massimo" <blue_max_53@hotmail.com>
- **Date:** 2007-01-08T09:56:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hzooh.102381$uv5.1366775@twister1.libero.it>`

```
Hi, a suggestion serves me:
in the programs microfocus the fields defined in the working-storage are 
initialized at run-time (zero, spaces, ecc).
In the fujitsu powercobol the fields defined in the working-storage remain 
to binary zero to run-time.(As standard Cobol language),
 Does exist an option for set the powercobol to initialize the fields at 
run-time (zero, spaces, ecc) ?
Thanks for the help.
Massimo From Rome.
```

#### ↳ Re: Powercobol to initialize the fields at run-time at zero binary

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-01-08T13:54:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s2soh.3907$ji1.1015@newssvr12.news.prodigy.net>`
- **References:** `<Hzooh.102381$uv5.1366775@twister1.libero.it>`

```
"Massimo" <blue_max_53@hotmail.com> wrote in message 
news:Hzooh.102381$uv5.1366775@twister1.libero.it...
> Hi, a suggestion serves me:
> in the programs microfocus the fields defined in the working-storage are 
…[4 more quoted lines elided]…
> run-time (zero, spaces, ecc) ?

Yes. See the VALUE [IS] clause for elementary items in working-storage. 
That will work with ANY COBOL.


MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
