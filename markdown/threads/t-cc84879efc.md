[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Double Byte Character Set (DBCS) application

_2 messages · 2 participants · 2000-04_

---

### Double Byte Character Set (DBCS) application

- **From:** jason@getridofthistoemail.comlinkusa.com
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e90740.261244025@209.98.98.12>`

```
We currently have an accounting app written in MF COBOL (for UNIX).
We would like to use this app in an environment that uses a DBCS.  The
Oracle database has been created to use the required character set.
Does the MF COBOL source code require any modification to support a
DBCS?

I thank you in advance for your time!

Jason Martin
```

#### ↳ Re: Double Byte Character Set (DBCS) application

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cb2i4$a1c$1@slb2.atl.mindspring.net>`
- **References:** `<38e90740.261244025@209.98.98.12>`

```
Look at PICTURE "N" and USAGE NATIONAL for support of DBCS characters

I am not positive about UNIX, but there are restriction on how it works on
WinTel depending upon whether or not you have a "dbcs" enabled machine and
OS.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
