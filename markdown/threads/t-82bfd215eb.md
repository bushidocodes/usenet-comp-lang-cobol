[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about Spool32

_2 messages · 2 participants · 2000-03_

---

### Question about Spool32

- **From:** "Roberto Bongini" <futura.softw@mclink.it>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8a31e3$rdp$1@news.mclink.it>`

```
Hi,
I use NetExpress 2.0 and I have a problem about a program that in Animate
run correctly with the standard call "PC_PRINTER_xxx". When I build my EXE
the program print only 4 page of 52.

Why?
Is possible that the program is fast and the call "PC_PRINTER_CLOSE" stop
the spool, and in the animate (with F11) is very slow that the spool can
complete the job?

Anybody know the API, and relative DLL, to retrieve the status of printer
spooler of Win9x, like the jobs on the queue or the print is busy etc.?


Thanks in advance.
Roberto.

FV
```

#### ↳ Re: Question about Spool32

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<38C578F3.DAE405CA@home.com>`
- **References:** `<8a31e3$rdp$1@news.mclink.it>`

```


Roberto Bongini wrote:
> 
> Hi,
…[11 more quoted lines elided]…
> 
I only use PC_PRINT for all my printing but with N/E V3.0 - so there
possibly could have been some subtle fixes between 2.0 and 3.0. As a
suggestion :-

- Can you trap on the Animator as you are about to do a page-change,
  where you get the line-count from PC_PRINT and see if it follows  
through with page 5

- regarding printer status - I check the status within PC_PRINT every  
time I throw a print-line at it - just as I check file-status for
  every flat-file access.

- another thought - do you have the latest "fixed" version  
(CBLPRINT.DLL, I think), when you are building your EXEs - if you have
  a Redistribution directory it must contain the 'fixes' not the  
originals from the CD

The next two are dumb, but it happens :-

In your print routines have you got your IF END-IFs or in-line PERFORM,
END-PERFORM paired off correctly ? Coupled with PERFORM do you use EXIT
PERFORM. Not doing that on some occasions has left me a bit quizzical
until I spotted it. I'm assuming you aren't using OO - but if you are
watch out for incorrect use of EXIT METHOD, e.g :-

	*>--------------
	Method-id. "print-something".
	*>--------------------

	 evaluate true
	  when 	a-condition perform A-record
	  when  b-condition perform B-record
	 End-evaluate

	 invoke self "print-detail-line".

	 Exit Method.		*> this is the one you DO need

	A-record.
	  move x ....
	  move ...
	  .

 	B-Record.
	  move x ....
	  move ...
	  .

	Exit Method   *> <<< delete this sucker - otherwise you'll exit
		      *> the first time you perform B-Record without 			      *> a
chance of invoking "print-detail-line"

	End Method "print-something".	
	*>-----------------------------------------------------------	

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
