[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling DLL's within COBOL

_6 messages · 3 participants · 2002-06_

---

### Calling DLL's within COBOL

- **From:** davidrodan18@hotmail.com (David Rodan)
- **Date:** 2002-06-16T21:35:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88a269be.0206162035.12d254b3@posting.google.com>`

```
Hello,
I am trying to call a routine within a 'C' DLL from COBOL (AcuCOBOL
5.2). I can call the DLL correctly but when I call the first routine
within the DLL it falls over with a Dr Watson error. I think the DLL
itself is OK as it works correctly with the VB and C samples provided.

Below is part of the code: 

01 qa-flags                 usage signed-long.
01 qa-return-val            usage signed-long. 

call "qatest.dll"

move zero to qa-flags
             qa-return-val
call "QA_Startup" using 
              by value qa-flags,
              returning qa-return-val
end-call


The sample 'C' equivilant is: 

int iCode;                
iCode = QA_Startup(0)

The manual for the DLL states that this startup routine should be
passed zero as a 'C' style long integer. I have tried changing the
usage to signed-int but this fails also. I have also tried to pass
zero to the routine manually, i.e. call "QA_Startup" using 0, but this
also falls over with this same error. I believe its either the way I'm
calling the DLL or the type and size of the variables I'm passing to
the routine.

Any help would be appreciated.

David Rodan.
```

#### ↳ Re: Calling DLL's within COBOL

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-06-17T04:11:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aek93t02gaa@enews1.newsguy.com>`
- **References:** `<88a269be.0206162035.12d254b3@posting.google.com>`

```
> I am trying to call a routine within a 'C' DLL from COBOL (AcuCOBOL
> 5.2). I can call the DLL correctly but when I call the first routine
> within the DLL it falls over with a Dr Watson error. I think the DLL
> itself is OK as it works correctly with the VB and C samples provided.

It's worth checking the calling convention of the DLL, as well as your
declarations in COBOL.  If this does not match, you can certainly pick up
exceptions of this order.
```

##### ↳ ↳ Re: Calling DLL's within COBOL

- **From:** davidrodan18@hotmail.com (David Rodan)
- **Date:** 2002-06-17T16:22:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88a269be.0206171522.661894cc@posting.google.com>`
- **References:** `<88a269be.0206162035.12d254b3@posting.google.com> <aek93t02gaa@enews1.newsguy.com>`

```
> It's worth checking the calling convention of the DLL, as well as your
> declarations in COBOL.  If this does not match, you can certainly pick up
> exceptions of this order.

Thank's, the calling convention is 'C' style, I do have another DLL
which I have been able to call correctly so I think that the call of
the DLL is correct, but either the data types of the variable I'm
passing is wrong or the way I'm passing the variables is wrong.

David Rodan.
```

###### ↳ ↳ ↳ Re: Calling DLL's within COBOL

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-06-17T19:18:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aelu8p04bu@enews3.newsguy.com>`
- **References:** `<88a269be.0206162035.12d254b3@posting.google.com> <aek93t02gaa@enews1.newsguy.com> <88a269be.0206171522.661894cc@posting.google.com>`

```

"David Rodan" <davidrodan18@hotmail.com> wrote in message
news:88a269be.0206171522.661894cc@posting.google.com...
> > It's worth checking the calling convention of the DLL, as well as your
> > declarations in COBOL.  If this does not match, you can certainly pick
up
> > exceptions of this order.
>
…[3 more quoted lines elided]…
> passing is wrong or the way I'm passing the variables is wrong.

'C' style is the cdecl convention?
```

#### ↳ Re: Calling DLL's within COBOL

- **From:** "Dennis Edward" <temp020305@ipipeline.net>
- **Date:** 2002-06-18T08:27:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ViIP8.3737$H67.20007@tor-nn1.netcom.ca>`
- **References:** `<88a269be.0206162035.12d254b3@posting.google.com>`

```
You need to have this in your program, or have the variable set in your
config:

 SET ENVIRONMENT "DLL-CONVENTION" TO 1.

"David Rodan" <davidrodan18@hotmail.com> wrote in message
news:88a269be.0206162035.12d254b3@posting.google.com...
> Hello,
> I am trying to call a routine within a 'C' DLL from COBOL (AcuCOBOL
…[34 more quoted lines elided]…
> David Rodan.
```

##### ↳ ↳ Re: Calling DLL's within COBOL

- **From:** davidrodan18@hotmail.com (David Rodan)
- **Date:** 2002-06-18T16:30:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88a269be.0206181530.7fe96395@posting.google.com>`
- **References:** `<88a269be.0206162035.12d254b3@posting.google.com> <ViIP8.3737$H67.20007@tor-nn1.netcom.ca>`

```
"Dennis Edward" <temp020305@ipipeline.net> wrote in message news:<ViIP8.3737$H67.20007@tor-nn1.netcom.ca>...
> You need to have this in your program, or have the variable set in your
> config:
> 
>  SET ENVIRONMENT "DLL-CONVENTION" TO 1.
> 

That fixed it.

Thanks for that Dennis, I did know about this config setting but for
some reason I did not have it in my config file.

Regards,

David Rodan.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
