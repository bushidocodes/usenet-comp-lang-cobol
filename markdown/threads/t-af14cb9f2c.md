[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EZTrieve - DB2 question

_3 messages · 3 participants · 1998-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### EZTrieve - DB2 question

- **From:** Steve Young <syoung@bcpl.net>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35919E4D.BF68CD16@bcpl.net>`

```

I am learning eztrieve on my own with very little support, and only 5
months of programming experience. I have been given the task of
retrieving certain data from a DB2 Table. I am having trouble with my
logic ( IF, END-IF). I can get the data by doing more than one report
because there are only 10 account numbers. However, I need to put it
into one report. Can anyone help? 

     EX.	GROUP-NO	ACCT-NO		NAME
		123		098		XYZ CO.
 		123		678		XYZ CO.		
		123 		---		XYZ CO.
		123		---		XYZ CO.
   		123 		---		XYZ CO.
		234		---		PQT CO.
		234		---		PQT CO.
		345		687		IRQ CO.
		345		---		IRQ CO.

What I need to extract are the groups, one time, unless they have
multiple accts.       

   EX.          123		098		XYZ CO.
		123             678		XYZ CO.	
		234 		---		PQT CO.
		345		687		IRQ CO.


Thanks in advance.

Steve
```

#### ↳ Re: EZTrieve - DB2 question

- **From:** Gilbert Berry <redbranch@earthlink.net>
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<359274CA.5E2B@earthlink.net>`
- **References:** `<35919E4D.BF68CD16@bcpl.net>`

```

Steve Young wrote:
> 
> I am learning eztrieve on my own with very little support, and only 5
…[27 more quoted lines elided]…
> Steve
Try select distinct if you only need the summary.  If you need both,
write out the query results to a veritual file and read it back in using
single file matching: job input (virtual-file-name key(group-no acct-no
name)) (this is, of course after you sort by those keys!)  If you had a
quantitative field i.e. one defiend with 0 or more decmial places, you
could use the report facility's summary option.  Hope this helps.  If
you need help with syntax, just email me.

Gilbert Berry
```

#### ↳ Re: EZTrieve - DB2 question

- **From:** michaelw@acslink.net.au (Michael Williams)
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mt5ro$tcl@inferno.mpx.com.au>`
- **References:** `<35919E4D.BF68CD16@bcpl.net>`

```

Steve Young <syoung@bcpl.net> wrote:

>I am learning eztrieve on my own with very little support, and only 5
>months of programming experience. I have been given the task of
…[3 more quoted lines elided]…
>into one report. Can anyone help? 

>     EX.	GROUP-NO	ACCT-NO		NAME
>		123		098		XYZ CO.
…[7 more quoted lines elided]…
>		345		---		IRQ CO.

>What I need to extract are the groups, one time, unless they have
>multiple accts.       

>   EX.          123		098		XYZ CO.
>		123             678		XYZ CO.	
>		234 		---		PQT CO.
>		345		687		IRQ CO.


>Thanks in advance.

>Steve


I would have thought that using the Report facililty options of
summary and break processing is the way to generate the report you
need.  I am sure there are examples in the Easytrieve manual.  Why
haven't you attended the requisite course from the CA people?  It is
all there in the lesson materials.

Easytrieve is named that way because it is supposed to be an easy
retrieval and reporting system though it does require you to
understand the underlying concepts.  Then it is easy.  Good luck.

Michael
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
