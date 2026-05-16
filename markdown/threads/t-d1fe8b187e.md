[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# unknown error

_4 messages · 3 participants · 1999-05_

---

### unknown error

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990504162434.10952.00002346@ng-cm1.aol.com>`

```
I get this error:
Run time error number: 013
eventhough the program compiles and ran fine
just 2 days ago.  I changed nothing in the data
or in the program.  What could be causing this?


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

#### ↳ Re: unknown error

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DfJX2.1842$JC1.109286@axe.netdoor.com>`
- **References:** `<19990504162434.10952.00002346@ng-cm1.aol.com>`

```
Dupavoy wrote in message <19990504162434.10952.00002346@ng-cm1.aol.com>...
>I get this error:
>Run time error number: 013
>eventhough the program compiles and ran fine
>just 2 days ago.  I changed nothing in the data
>or in the program.  What could be causing this?


Good question.  Without knowing what compiler you are using or the operating
system you are running it's hard to tell from here.  Do you know what
statement it was trying to run when it crashed?  Have you run it in debug?
If not have you thrown in a number of temporary DISPLAY statements to let
you know where you are? (display "read at 110", read .........  display
"finished read at 110").  Has someone changed a file you referenced with a
COPY statement?

Without some specifics, it is hard to offer any help.
```

##### ↳ ↳ Re: unknown error

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990505140846.21678.00002733@ng-fp1.aol.com>`
- **References:** `<DfJX2.1842$JC1.109286@axe.netdoor.com>`

```

Dupavoy wrote in message <19990504162434.10952.00002346@ng-cm1.aol.com>...
>I get this error:
>Run time error number: 013
>eventhough the program compiles and ran fine
>just 2 days ago.  I changed nothing in the data
>or in the program.  What could be causing this?


Good question.  Without knowing what compiler you are using or the operating
system you are running it's hard to tell from here.  Do you know what
statement it was trying to run when it crashed?  Have you run it in debug?
If not have you thrown in a number of temporary DISPLAY statements to let
you know where you are? (display "read at 110", read .........  display
"finished read at 110").  Has someone changed a file you referenced with a
COPY statement?

Without some specifics, it is hard to offer any help.



--Problem solved!  I was using an external
file that was more than 8 characters.


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

###### ↳ ↳ ↳ Re: unknown error

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<925978235.7170.0.nnrp-06.9e98b131@news.demon.co.uk>`
- **References:** `<DfJX2.1842$JC1.109286@axe.netdoor.com> <19990505140846.21678.00002733@ng-fp1.aol.com>`

```
If you're using MF COBOL then RT 013 just means file not found.

Are you running with the same set up?  Does a path to the file exist?

Regards
Rick

Dupavoy wrote in message <19990505140846.21678.00002733@ng-fp1.aol.com>...
>
>Dupavoy wrote in message <19990504162434.10952.00002346@ng-cm1.aol.com>...
…[7 more quoted lines elided]…
>Good question.  Without knowing what compiler you are using or the
operating
>system you are running it's hard to tell from here.  Do you know what
>statement it was trying to run when it crashed?  Have you run it in debug?
…[20 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
