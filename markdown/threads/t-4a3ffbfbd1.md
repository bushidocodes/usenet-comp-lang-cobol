[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VMS Cobol COPY LIBRARY

_2 messages · 2 participants · 2003-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### VMS Cobol COPY LIBRARY

- **From:** samuli.raikkonen@enfo.fi (Sam)
- **Date:** 2003-02-26T04:41:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1668a2c6.0302260441.b5c9112@posting.google.com>`

```
Hullo!
Just a simple - yes, a dumb and simple - question:

How can I tell VMS COBOL where to find the COPY LIBRARIES? I decided
against using a library and chose to use separate text-files instead
(suits our purpose better at this stage), and I'd like to put all the
separate text-files to a single directory. How can I tell the COBOL
compiler where these files are located?

So what to do without much ado?

- Thanks in advance, Sam
```

#### ↳ Re: VMS Cobol COPY LIBRARY

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 2003-02-27T08:31:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5dbe45@nntp.unige.ch>`
- **References:** `<1668a2c6.0302260441.b5c9112@posting.google.com>`

```
Sam a ï¿½crit:
> Hullo!
> Just a simple - yes, a dumb and simple - question:
…[5 more quoted lines elided]…
> compiler where these files are located?


COPY "LIBRARY-FILE" FROM COPYLIB.

The COPY Statement, Dictionaries and Libraries

Including the COPY statement in your program allows separate programs to 
share common source text, reducing development and testing time as well 
as storage requirements. You can use the COPY statement to access 
modules in libraries. The COPY statement causes the compiler to read the 
file or module specified during the compilation of a program. When the 
compiler reaches the end of the included text, it resumes reading from 
the previous input file.

By using the /INCLUDE qualifier on the COBOL command line, you can set 
up a search list for files specified by the COPY statement. For more 
information, see the Compaq COBOL Reference Manual.

You can use the COPY FROM DICTIONARY statement in your program to access 
a data dictionary and copy Oracle CDD/Repository record descriptions 
into your program as COBOL record descriptions. Before you can copy 
record descriptions from Oracle CDD/Repository, you must create the 
record descriptions using the Common Data Dictionary Language (CDDL) or 
Common Dictionary Operator (CDO).

For more information about using Oracle CDD/Repository and creating and 
maintaining text libraries, refer to the Compaq COBOL Reference Manual 
and Using Oracle CDD/Repository on OpenVMS Systems.

AC
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
