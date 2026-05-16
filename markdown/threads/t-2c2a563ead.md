[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

_3 messages · 3 participants · 2008-11 → 2008-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Databases and SQL`](../topics.md#databases)

---

### COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

- **From:** plastiksprengstoff@googlemail.com
- **Date:** 2008-11-26T12:37:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14102947-7263-4caf-bf63-e155606d804b@y18g2000yqn.googlegroups.com>`

```
in 2006 i post this question - i dont beleve that see also
http://groups.google.de/group/comp.lang.cobol/browse_thread/thread/46b66a92066f7241/d6302fd446c27054?#d6302fd446c27054
:

 Hello all

System: z/OS and LE for MVS

Why is it possible to compile a COBOL/CICS/DB2 program with the
options:

NODYNAM . . . ?????

nowerdays thats not the state of the art, because:

IMS could be called dynamic
COBOL and ASSEMBLER could be called dynamic

why not inside of a CICS environment

I asked this question, because i mus used the same sources in two
environments:

DB2 Batch (IMS/DSN) - one compile and link
DB2 CICS - a second compile and link

i have to manage two sources inside a revision environment!!!

The first source could be compiled with the option: DYNAM for batch -
and all calls are managed by COBOL and MVS

in CICS, the precompiler sets the COBOL options to NODANM. Therefore i
need a second source to manage the environment. I must use the
CICS-link library to link the DSNHLI and i can NOT use the same module
in IMS/TSO, because they need different HLI's: for IMS propagator
DSNHLI from IMS for DSN propagator DSNHLI from DB2.

I would link a DB2 module without a specific DSNHLI.......

Is DFHECI unable to be called dynamic? IMS module DFSLI000 could.

Why does DB2 precompiler generate calls like: CALL 'DSNHLI' USING
PLIST-x, instead of CALL DSNHLI USING PLIST-x, where DSNHLI ist
defined as a variable inside the working-storage section?

I am not pleased about this situation.

I hope, that you could follow my intention... :-)

i am not so stable in english

Einen schoenen Tag
Andreas Lerch

but today - i have a solution.....

inside the cobol program i use this:

end program main.
id division.
program-id. DSNHLI.
data division.
working-storage section.
work-dsnhli pic x(8) value 'dsnhli'.
linkage section.
01 link-dsnhli pic x(1)
procedure division using link-dsnhli.
call work-dsnhli using link-dsnhli end-call
goback.
end program dsnhli.

now i can use the NODYNAM option within the compiler to call the
propagator dsnhlin within the application dynamicly...

cics --> DSNHLI of cics
ims --> DSNHLI of ims and any more

cool

einen schoenen tag
Andreas Lerch
```

#### ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-12-04T08:36:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sEMZk.90183$786.16767@fe11.news.easynews.com>`
- **References:** `<14102947-7263-4caf-bf63-e155606d804b@y18g2000yqn.googlegroups.com>`

```
Are you aware that under CICS when you use the NODYNAM compiler option you can 
still use the
   CALL identifier
       rather than
   CALL "literal"

format so all CALLs to *YOUR* application subprograms are dynamic?  In that 
case, only the CICS/IBM supplied subroutines must be link-edited (bound) into 
your load module.

I can't remember when this was first supported, but I know it has been possible 
for over a decade and a half.
```

##### ↳ ↳ Re: COBOL/CICS/DB2 - COBOL for MVS and compile option DYNAM - solution from 2006

- **From:** CG <Carl.Gehr.ButNoSPAMStuff5@MCGCG.Com>
- **Date:** 2008-12-07T00:45:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77bdd$493b62fe$d066afd4$7256@FUSE.NET>`
- **In-Reply-To:** `<sEMZk.90183$786.16767@fe11.news.easynews.com>`
- **References:** `<14102947-7263-4caf-bf63-e155606d804b@y18g2000yqn.googlegroups.com> <sEMZk.90183$786.16767@fe11.news.easynews.com>`

```
On 12/04/08 03:36 am, William M. Klein wrote:
> Are you aware that under CICS when you use the NODYNAM compiler option you can 
> still use the
…[9 more quoted lines elided]…
> for over a decade and a half.

I believe it goes back to the early/mid 1970s when dynamic calls were 
first implemented.
Carl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
