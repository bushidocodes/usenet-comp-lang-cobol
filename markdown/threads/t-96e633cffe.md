[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# need help with jcl coding

_3 messages · 3 participants · 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### need help with jcl coding

- **From:** al3x <member@mainframeforum.com>
- **Date:** 2002-11-14T17:51:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dd428e0$1_3@news.onlynews.com>`

```
ok below is a cataloged procedure,

//SUMMARY PROC //EDIT EXEC PGM=EDIT //OUTPUT DD DSN=&&OUTPUT //
DISP=(NEW,PASS), // UNIT=SYSDA // SPACE=(TRK,10) //RUN EXEC PGM=SALES
//INPUT DD DNS=&&OUTPUT, // DISP=(OLD,DELETE) //REPORT DD SYSOUT=A

how can i go about coding the jcl so that it can execute this procedure
with the following modifications: program EDIT should have a region of
80k, sales should not be executed if program EDIT returns a condition
code equal to 100, program EDIT requires input stream data supplied
under the ddname TRANFILE, and data set &&OUTPUT requires 20 tracks. any
help would be appreciated. im new to JCL.
```

#### ↳ Re: need help with jcl coding

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-14T17:34:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ar1bua$hgu$1@slb9.atl.mindspring.net>`
- **References:** `<3dd428e0$1_3@news.onlynews.com>`

```
Not answering you directly, but I suggest that you read the section

  "5.2 Modifying Procedures"

at:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/iea2b630/5.2

I think it will give you most of the answers you want
```

#### ↳ Re: need help with jcl coding

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-11-15T13:26:56+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iem9tu4s9121f9li8ej6kiv0akopk2nd8r@4ax.com>`
- **References:** `<3dd428e0$1_3@news.onlynews.com>`

```
On 14 Nov 2002 17:51:12 -0500 al3x <member@mainframeforum.com> wrote:

:>ok below is a cataloged procedure,

:>//SUMMARY PROC //EDIT EXEC PGM=EDIT //OUTPUT DD DSN=&&OUTPUT //
:>DISP=(NEW,PASS), // UNIT=SYSDA // SPACE=(TRK,10) //RUN EXEC PGM=SALES
:>//INPUT DD DNS=&&OUTPUT, // DISP=(OLD,DELETE) //REPORT DD SYSOUT=A

:>how can i go about coding the jcl so that it can execute this procedure
:>with the following modifications: program EDIT should have a region of
:>80k, sales should not be executed if program EDIT returns a condition
:>code equal to 100, program EDIT requires input stream data supplied
:>under the ddname TRANFILE, and data set &&OUTPUT requires 20 tracks. any
:>help would be appreciated. im new to JCL.

First of all - correct the subject.

It should read "need help with homework".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
