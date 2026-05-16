[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# To Recover a deleted file from MVS Backup

_1 message · 1 participant · 2006-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: To Recover a deleted file from MVS Backup

- **From:** "Joel C. Ewing" <jcREMOVEewing@CAPSacm.org>
- **Date:** 2006-01-22T03:27:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lYCAf.4311$vU2.3785@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<1137734359.955244.30830@g49g2000cwa.googlegroups.com>`
- **References:** `<1137734359.955244.30830@g49g2000cwa.googlegroups.com>`

```
This may leave many with a dangerously optimistic misconception about 
how much backup activity is done for you automatically on MVS and how 
omniscient MVS is about application backup requirements.

The backups to which you refer are backups that are taken by the product 
DFSMShsm, an optional product of z/OS which might not be active in all 
installations.  HSM is highly customizable and also tied to System 
Managed Storage (SMS) definitions, which are customized and unique to a 
specific MVS installation.  The installation would have to define an SMS 
Management Class with the autobackup attribute, and a dataset would have 
to be associated (implicitly or explicitly) with such a management class 
in order to be eligible for autobackup.

Autobackup is scheduled for a specific, installation-chosen, time period 
during the 24-hour day and autobackup of a specific dataset will be done 
at most once a day during that time period.  The installation can also 
choose how many backups will be retained for that management class and 
whether a minimum number of days must have elapsed from a prior backup. 
If a dataset undergoes multiple changes before it becomes eligible for 
autobackup again, only the last state of the dataset will be saved in an 
autobackup.  Also, if the dataset can possibly be changed during the 
daily autobackup process (which may run for several hours), then you 
can't even predict in advance whether the backup up version of that 
dataset will be taken before or after it changes.

Bottom line, you have to know and understand the conventions that are in 
place at your specific MVS installation relating to autobackup 
eligibility and scheduling.  If this means you have an application that 
isn't adequately protected for recovery or re-run, it is the application 
implementer's responsibility to create required backups at the required 
times and with the required retention cycle.  MVS has no way to guess 
what the requirements might be for an arbitrary application.


mftips@gmail.com wrote:
> In Mainframes, MVS takes backup of files/datasets, every time they are
> changed. Also it keeps backup of these changed versions at any point of
> time. So, at any point of time we can recover deleted datasets as well
> as its previous versions.
...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
