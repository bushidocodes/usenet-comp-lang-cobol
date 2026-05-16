[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BI-DIRECTIONAL PIPE READ TIMEOUT

_1 message · 1 participant · 2005-04_

---

### BI-DIRECTIONAL PIPE READ TIMEOUT

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-04-14T12:23:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113506591.598491.161300@l41g2000cwc.googlegroups.com>`

```
Is there a way to make a READ statement on a bidirectional pipe timeout
if no data is present?

Platform: HP-UX 11i
COBOL: MF Server Express 4.0 SP1


Code snippet:

dd_ftppipe=|ftp -n

select optional        FTP-PIPE
  assign to disk       "ftppipe"
  organization is      line sequential
  file status is       ERROR-STATUS.

fd  FTP-PIPE.
01  FTP-PIPE-REC                pic  x(256).

open i-o FTP-PIPE

write FTP-PIPE-REC
  from "open <hostname>"
end-write

read FTP-PIPE-REC end-read


Using this code - assuming that the open within FTP fails for some
unknown reason - I don't want to get stuck indefinitely in the read. If
the FTP process cannot connect within x seconds - I need to hop out and
fire off some alerts (as this is an internal process and FTP should
respond immediately).

If there's anything I'm leaving out, please let me know.

Thanks in advance,
Chris
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
