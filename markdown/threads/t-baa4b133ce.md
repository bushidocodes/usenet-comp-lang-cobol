[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# debug options in cobol os/390

_1 message · 1 participant · 2000-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: debug options in cobol os/390

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-12-12T13:16:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001212081655.26594.00004186@ng-fu1.aol.com>`
- **References:** `<90limt$hhl10@sunsv007>`

```
Noï¿½l Garnier writes ...

>Hello,
>
…[6 more quoted lines elided]…
>

I thought we had this one just last week.

Anyway, TEST(ALL,SYM) costs a lot in terms of performance and should never be
used in production (I don't have a number on the cost, though).

In our class "COBOL Debugging and Maintenance in the LE Environment" we
recommend TEST(NONE,SYM). This embeds your data map in your load module. This
can create signficantly larger load modules but you get no performance hit
(except for module load time). But, if you abend you get a formatted dump of
all data division items. With V2R10 and COBOL for OS/390 & VM V2R2 you can code
TEST(NONE,SYM,SEPARATE) and the data map will be stored in a separate file;
this shrinks your load module and you only need to ensure the file containing
the data map is in your STEPLIB.

Hope this helps.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
