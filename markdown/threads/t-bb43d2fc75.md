[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Asynchronous call from Cobol

_3 messages · 3 participants · 1998-04_

---

### Asynchronous call from Cobol

- **From:** "sat..." <ua-author-16842988@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3532DE61.3A660AB2@pop.mpls.uswest.net>`

```
Hello Cobol mates,

I've a question that I hope one of you can answer.
Assuming that the underlying Operating System is capable of handling
multiple processes,
for eg: Windows NT -
Is there any means to trigger the execution of a (DOS) batch file from
within a COBOL program and return control to the next COBOL statement
without waiting for the batch file to complete running?


Satish

Hello Cobol mates,
I've a question that I hope one of you can answer.
Assuming that the underlying Operating System is capable of handling
multiple processes,
for eg: Windows NT -
Is there any means to trigger
the execution of a (DOS) batch file from within a COBOL program and return
control to the next COBOL statement without waiting for the batch file
to complete running?
Â 

Satish
```

#### ↳ Re: Asynchronous call from Cobol

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bb43d2fc75-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3532DE61.3A660AB2@pop.mpls.uswest.net>`
- **References:** `<3532DE61.3A660AB2@pop.mpls.uswest.net>`

```
Satish,

Which COBOL product are you using?

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.
sat··.@pop··t.net wrote in message <353··.@pop··t.net>...
Hello Cobol mates,
I've a question that I hope one of you can answer.
Assuming that the underlying Operating System is capable of handling multiple processes,
for eg: Windows NT -
Is there any means to trigger the execution of a (DOS) batch file from within a COBOL program and return control to the next COBOL statement without waiting for the batch file to complete running?


Satish








Satish,
Â 
Which COBOL product are you using?
Â 
Paddy Coleman
Team Leader, Distributed Computing Support
(WinTel)Â 
Micro Focus International.Â 

sat··.@pop··t.net
wrote in message <353··.@pop··t.net>...Hello
Cobol mates,
I've a question that I hope one of you can answer. Assuming that the
underlying Operating System is capable of handling multiple processes,
for eg: Windows NT - Is there any means to trigger the
execution of a (DOS) batch file from within a COBOL program and return
control to the next COBOL statement without waiting for the batch file to
complete running? Â 
Satish
```

#### ↳ Re: Asynchronous call from Cobol

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bb43d2fc75-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3532DE61.3A660AB2@pop.mpls.uswest.net>`
- **References:** `<3532DE61.3A660AB2@pop.mpls.uswest.net>`

```


› Is there any means to trigger the execution of a (DOS) batch file from
› within a COBOL program and return control to the next COBOL statement
› without waiting for the batch file to complete running?


That sort of thing is ussually compiler specific. With LIANT, you would
use a
CALL "SYSTEM" using command-line.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
