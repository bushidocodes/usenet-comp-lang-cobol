[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing parameters in JCL

_2 messages · 2 participants · 2001-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Passing parameters in JCL

- **From:** De Tijd <bart.van.diest@tijd.com>
- **Date:** 2001-01-27T16:27:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1103_980612833@tdn22128>`

```
Hi,

I'm working as a Cobol-programmer on an IBM Mainframe.
The bank I'm working for uses a lot of variables in their
JCL. (e.g. &HDAT which is translated into the current date).
I'm not sure but I believe this is done daily by a 'Change All'.
Now I was wondering if it is possible to let the value
of one of those variables depend on the value of a record
in a file ? (e.g. to translate &v into the value of the first
byte of the first record). 
If anyone knows the answer, it would really help me a lot.
Thanks,

Bart
```

#### ↳ Re: Passing parameters in JCL

- **From:** keldin@earthlink.not (TJ Dombrowski)
- **Date:** 2001-01-27T19:16:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns9036920C4A8EDkeldinearthlink@207.217.77.25>`
- **References:** `<1103_980612833@tdn22128>`

```
De Tijd <bart.van.diest@tijd.com> wrote in <1103_980612833@tdn22128>:

>Hi,
>
…[14 more quoted lines elided]…
>

the variables are set thru an OPC variable table by your scheduling group.
Like if today is friday, and you are processing Thrusdays Data.  
You can make the run-date be thursday, even though it is executing on 
friday.
If you want to read lines at run time you can use //%OPC FETCH MEMBERNAME
where member name is in member in a pds in your JCL run path.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
