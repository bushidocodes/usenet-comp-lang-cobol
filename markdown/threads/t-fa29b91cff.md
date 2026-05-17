[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PLEASE HELP PC COBOL

_4 messages · 3 participants · 1996-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### PLEASE HELP PC COBOL

- **From:** "morris jones jr" <ua-author-2526020@usenetarchives.gap>
- **Date:** 1996-05-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net>`

```

PLEASE HELP I AM IN SCHOOL IN COBOL 2 TRYING TO JUST READ A ESDS FILE
AND WRITE IT OUT AS A KSDS FILE USING THE RM-85 PC COMPILER, THE TEACHER
SAYS THAT OTHER STUDENTS HAVE DONE IT BUT DOES NOT KNOW HOW ,HE ONLY KNOWS
THE MAINFRAME SIDE. I KNOW IT WILL HAVE TO BE A ISAM AND NOT A VSAM FILE
BUT NOT HAVING ANY LUCK ANY IDEAS WILL BE VERY HELPFUL THANKS MORRIS JONES
```

#### ↳ Re: PLEASE HELP PC COBOL

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1996-05-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fa29b91cff-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net>`
- **References:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net>`

```

MORRIS JONES JR wrote:
› 
› PLEASE HELP I AM IN SCHOOL IN COBOL 2 TRYING TO JUST READ A ESDS FILE
…[3 more quoted lines elided]…
› BUT NOT HAVING ANY LUCK ANY IDEAS WILL BE VERY HELPFUL THANKS MORRIS JONES


The primary difference between a PC Cobol Isam and a mainframe VSAM
file (simply speaking) is that the mainframe requires that the VSAM
cluster definition be defined first using the IDCAMS utilitiy. After
that, the file can be used. Although I have not used RM Cobol, but
have used CA-Realia and Micro Focus Cobol, the CA-Realia and MF Cobol
will create the ISAM files based on your Cobol program's file
descriptions when an open is issued to the file--pre-allocation of
the file is not necessary.

A VSAM file is an IBM file structure. A VSAM KSDS file is actually a
VSAM sequential file. A VSAM KSDS file is a keyed sequential dataset
(behaves the same as a PC ISAM file). If you are concerned that the
coding in your program is different for a PC ISAM file than it is for
a VSAM KSDS file, the code is the same. As a matter of fact, it's
easier on the PC because you don't have to worry about IDCAMS. Creating
alternate indicies with PC Cobol is also easier. The code below, if
RM Cobol behaves like CA-Realia and Micro Focus, will create the ISAM
file.


Select My-Indexed-File Assign To Mastfile
Organization is Indexed
Access is Random
Record Key Is Employee-Number.

Open Output My-Indexed-File.

Mike DOdas
```

##### ↳ ↳ Re: PLEASE HELP PC COBOL

- **From:** "morris jones jr" <ua-author-2526020@usenetarchives.gap>
- **Date:** 1996-05-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fa29b91cff-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-fa29b91cff-p2@usenetarchives.gap>`
- **References:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net> <gap-fa29b91cff-p2@usenetarchives.gap>`

```

hey mike , thanks for the help i will give that a shot and let you know if
i have any more trouble thanks again morrs jones
```

#### ↳ Re: PLEASE HELP PC COBOL

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-05-27T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fa29b91cff-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net>`
- **References:** `<4o05ej$5kb@mtinsc01-mgt.ops.worldnet.att.net>`

```

In article <4o05ej$5.··.@mti··t.net>,
m.j··.@wor··t.net says...
›
*>PLEASE HELP I AM IN SCHOOL IN COBOL 2 TRYING TO JUST READ A ESDS FILE
*>AND WRITE IT OUT AS A KSDS FILE USING THE RM-85 PC COMPILER, THE TEACH
*>ER
*>SAYS THAT OTHER STUDENTS HAVE DONE IT BUT DOES NOT KNOW HOW ,HE ONLY K
*>NOWS
*>THE MAINFRAME SIDE. I KNOW IT WILL HAVE TO BE A ISAM AND NOT A VSAM FI
*>LE
*>BUT NOT HAVING ANY LUCK ANY IDEAS WILL BE VERY HELPFUL THANKS MORRIS J
*>ONES
›


Oops - a typo. In a previous responses I said:

"A VSAM file is an IBM file structure. A VSAM KSDS file is actually a
VSAM sequential file. A VSAM KSDS file is a keyed sequential dataset
(behaves the same as a PC ISAM file)."

I referred to a VSAM KSDS file as a sequential file. I meant to say a
VSAM *ESDS* file is a VSAM sequential file. Sorry.

Mike Dodas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
