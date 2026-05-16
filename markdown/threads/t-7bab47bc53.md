[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File formatting.

_1 message · 1 participant · 1999-05_

---

### File formatting.

- **From:** nospam@nospam-please.com (nospam@nospam-please.com)
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc.1dcede5a1c8a00001dcede5afd953dd0.4017dfb@city.magnet.at>`

```
I am writing a program in Cobol to convert an ASCII file into a formatted
file so that I can import the files into a database.

The original file has different length fields with fields in different
places - eg. NAME[Neil Capel]AGE[21]ADD1[------- etc.

I want to read a line at a time and then look at each character for [ and
].
Do I have to move the read line into, say -
 1 conv-line.
     3 1char  x.
     3 2char  x.
     3 3char  x.

etc.

and then look at each character?  Is there a better way?  PLEASE HELP.

Also I will need to search and replace - is it possible to replace end of
line chars with spaces?  How do I look for end of line chars.

Please e-mail me:

neilc@1sitedesigns.net



Message-ID: <DoEZ2.3184$%x.2654@wards>
Path:
magnet.at!newsfeed03.univie.ac.at!newsrouter.chello.at!newsfeed.ecrc.net!btnet-peer!btnet-feed1!btnet!landlord!wards.POSTED!not-for-mail
Date: Mon, 10 May 1999 17:35:10 +0100
From: "John" <nospam@nospam-please.com>
Subject: File formatting.
Lines: 25
Newsgroups: comp.lang.cobol
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
