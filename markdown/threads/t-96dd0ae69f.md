[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# determining the OS

_2 messages · 2 participants · 2001-03_

---

### determining the OS

- **From:** Marcello.Clarizia@siae.it ("Marcello Clarizia")
- **Date:** 2001-03-12T11:49:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<000801c0aae1$dc36b430$0a02320a@fsi.dg.siae>`

```
Is there a way, in COBOL, to tell which version of Windows is running ?
I have to create files with longname, using a DOS shell and a batch file. The shell is COMMAND.EXE in Win95, or CMD.EXE in WinNT, so the COBOL program has to know which OS it's running under, before calling the batch file.
```

#### ↳ Re: determining the OS

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-03-12T15:59:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-DRk8yP3FKWLd@tcpserver>`
- **References:** `<000801c0aae1$dc36b430$0a02320a@fsi.dg.siae>`

```
On Mon, 12 Mar 2001 10:49:40, Marcello.Clarizia@siae.it ("Marcello 
Clarizia") wrote:

> This is a multi-part message in MIME format.
> 
…[3 more quoted lines elided]…
> 
<snipped HTML out of the post - please turn this off>

If you are using the MERANT (Microfocus) COBOL products they provide a
runtime routine called "cbl_get_os_info" that will tell you what OS is
running. 

If you are not using the MERANT compiler check the documentation of 
the one you are using to see if they offer an equivalent routine, if 
one is not available, you could always call the appropriate Windows 
API (you only mentioned Windows(TM) varients so I assume that is the 
only OS you are using).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
