[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help ASAP !!!

_6 messages · 6 participants · 1995-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help ASAP !!!

- **From:** "jati..." <ua-author-17088150@usenetarchives.gap>
- **Date:** 1995-03-01T23:46:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`

```
What does the error "ambiguous reference -- check name qualification mean and h
how can I get rid of it ? Pl. reply ASAP
Thanks in advace !!!
```

#### ↳ Re: Help ASAP !!!

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-03-03T13:02:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a1f71bcdd1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`
- **References:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`

```
Adina Adler (p.··.@ath··t.edu) wrote:
: > jat··.@bon··s.edu (JATINDER S. DHALIWAL) writes:

: > What does the error "ambiguous reference -- check name qualification
: > mean and h how can I get rid of it ? Pl. reply ASAP

: You probably have two variables with the same name. Look at the
: variables used on the line referenced by the error message.
: --
: Adina Adler
: p.··.@ath··T.EDU
:
: My opinions, and
: nothing but

COBOL allows you to reuse variable names if they can be differentiated
by belonging to different groups. When you have two variable of the same
name and you do not refer to the group it belongs to, you get this error.
Advice: avoid duplicate names, if need be, try using group prefixes:

MD-RATE MF-RATE as opposed to RATE OF MD and RATE OF MF

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

##### ↳ ↳ Re: Help ASAP !!!

- **From:** "2sd8ch..." <ua-author-17087730@usenetarchives.gap>
- **Date:** 1995-03-03T16:21:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a1f71bcdd1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a1f71bcdd1-p2@usenetarchives.gap>`
- **References:** `<3j3iju$aeh@geraldo.cc.utexas.edu> <gap-a1f71bcdd1-p2@usenetarchives.gap>`

```
In article <3j7ljd$e.··.@Mar··s.com>, fr··.@M··.COM (Lawrence Free/ A.F. Software Services) writes:
› Adina Adler (p.··.@ath··t.edu) wrote:
› : > jat··.@bon··s.edu (JATINDER S. DHALIWAL) writes:
…[17 more quoted lines elided]…
› 

Sometimes you have a CALL command, i.e to call a specific library,
which has the same variable name as the one in your own program. The
only way you can find it is by creating a *.LIS file. At the $ prompt,
just type in $cob/list/copy program.COB, if it's a COBOL file, else you'd
have to use SCOB or RCOB for SQL and RDB respectively. A file with an
extension .LIS will be created and you can use FIND to locate the occurences,
if there's any....

Hope this will help!

-emptyV-

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Zul Abas
2sd··.@vms··u.edu
Ab··.@vms··u.edu (-o-)
che··.@stu··u.edu
zul@vinny
IP: 134.32.24.38

(-o-)
EX-XWing Fighter Pilot who is now serving the Emperor!!
COME AND JOIN THE DARK SIDE!!
___________________________________________________________________________
```

#### ↳ Re: Help ASAP !!!

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-03-03T18:02:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a1f71bcdd1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`
- **References:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`

```
he best guess is that the message saying you have an ambiguous reference
eans exactly what it says, i.e. a reference that does not uniquely
indentify a single data name (e.g. A of C could mean A of B of C or
A of Q of C, if both are present)
```

#### ↳ Re: Help ASAP !!!

- **From:** "e..." <ua-author-17073894@usenetarchives.gap>
- **Date:** 1995-03-03T18:49:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a1f71bcdd1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`
- **References:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`

```
In article
p.··.@ath··t.edu "Adina Adler" writes:

›› jat··.@bon··s.edu (JATINDER S. DHALIWAL) writes:
› 
…[4 more quoted lines elided]…
› variables used on the line referenced by the error message.

Yes, but that's perfectly legal in COBOL.

You could have something like this in your data division:

01 GROUP-1.
03 AAA PIC X.
03 BBB PIC 999.
01 GROUP-2.
03 AAA PIC X.
03 CCC PIC ZZZ.
03 BBB PIC X(30).

In your program you refer to them as "AAA OF GROUP-1" or "AAA OF GROUP-2".
(same with BBB, but there is no need to qualify CCC as it is unique).

Enzo------------------------------------------------------------------
And everything under the sun is in tune
but the sun is eclipsed by the moon.
Siri------------------------------------------------------------------
```

#### ↳ Re: Help ASAP !!!

- **From:** "kim..." <ua-author-3680929@usenetarchives.gap>
- **Date:** 1995-03-04T09:30:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a1f71bcdd1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`
- **References:** `<3j3iju$aeh@geraldo.cc.utexas.edu>`

```
In article <3j3iju$a.··.@ger··s.edu>,
jat··.@bon··s.edu (JATINDER S. DHALIWAL) wrote:
› What does the error "ambiguous reference -- check name qualification mean 
› and h
› how can I get rid of it ? Pl. reply ASAP
› Thanks in advace !!!
›     
Most likely you have a data field defined on more than one record - e.g.,
file FD and Working Storage.

If this is the case, the 'dup' field must be 'qualified' as illustrated
below:

field of recxx or field of recxx (n) <-- if it is an array.
-- -- ---
This applies to all SCREEN (assuming that OCCURS is not specified) and
PROCEDURE statements.


-----------------------------------------------
John Lee - Consultant
Kim Software, Inc.
e-mail: kim··.@bro··l.com
Voice (614)766-4900 FAX (614)766-7009 EST
http://198.4.94.79/kim.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
