[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can I run Micro Focus COBOL /2 v1.2.29 from XP Pro "Cmd" Window ?

_4 messages · 4 participants · 2007-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Can I run Micro Focus COBOL /2 v1.2.29 from XP Pro "Cmd" Window ?

- **From:** "Will" <Will@somewhere.com>
- **Date:** 2007-12-15T09:09:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4763e00d$0$4976$4c368faf@roadrunner.com>`

```
OK guys, it appears the original program was written using .. Micro Focus 
COBOL/2 Version 1.2.29 L2.2 revision 003

QUESTION: Can I run any of the Micro Focus stuff on my XP Pro machine by 
going to the DOS prompt via... Start | Run | Cmd ??

I copied the files from the old DOS 6.2 machine and put them on my XP Pro 
machine... here are the directories/folders I have... (in the root directory 
on C:)

PGM
..COPYBOOK (Copybook files here)
..FILES (.FIL and .IDX files here)
..PROGRAMS (.CBL, .GNT,
MF-COBOL
MF-RTE

Looking at the BAT file that seems to launch the application it appears the 
the application runs under an old GUI program called HI-SCREEN Pro II. (Last 
line below is a file named hs-beg.com and appears also in another folder 
named HSPRO2. Maybe this is why it won't run on a Windows XP Pro machine... 
the hs-beg.com program must be some sort of hi-res program for old DOS 
machines.

I would have thought there there would have been some compiled .COM or .EXE 
file that was the actualy Application... but looking at the startup BAT 
below it seems they...
... setup the data .FIL's..
... then point to the Run Time Environment...
... not sure what COBSW=-F does
... then launch this HI-Screen Pro II application which somehow knows to run 
the application

===== Startup Batch File:
REM ..Load External File Names
SET F1=c:\PGM\FILES\CONTROL.FIL
SET F2=c:\PGM\FILES\CONTDATA.FIL
SET F3=c:\PGM\FILES\AUDIT.FIL
SET F4=c:\PGM\FILES\ITEMMST.FIL
SET F5=c:\PGM\FILES\OWNERMST.FIL
SET F6=c:\PGM\FILES\PLOTMSTR.FIL
SET F7=c:\PGM\FILES\TRUSTBNK.FIL
SET F8=c:\PGM\FILES\INTERINF.FIL
SET F9=c:\PGM\FILES\NOTES01.FIL
SET FA=c:\PGM\FILES\SALESMAN.FIL
SET FB=c:\PGM\FILES\SMANSALE.FIL
SET COBDIR=c:\MF-RTE
SET LIB=\c:MF-RTE
SET DSDIR=c:\MF-RTE
SET COBSW=-F
CD \PGM\PROGRAMS
Echo launching hs-beg.com
hs-beg
===== End of Bach File

Thanks for any comments or suggestions.
```

#### ↳ Re: Can I run Micro Focus COBOL /2 v1.2.29 from XP Pro "Cmd" Window ?

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-12-15T08:15:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kR8j.39687$L%6.23889@bignews3.bellsouth.net>`
- **References:** `<4763e00d$0$4976$4c368faf@roadrunner.com>`

```
"Will" <Will@somewhere.com> wrote:
> OK guys, it appears the original program was written using .. Micro Focus COBOL/2 Version 1.2.29 L2.2 revision 003
>
> QUESTION: Can I run any of the Micro Focus stuff on my XP Pro machine by going to the DOS prompt via... Start | Run | Cmd ??

I have never had problems running the DOS versions of Micro Focus
COBOL under Windows 95, 98, 2K or XP. If you have problems with
cmd.exe, try command.exe, which is the specific WinXP DOS emulator.

In fact, I have found XP to be extremely DOS program friendly, better
even than the 9X versions. Vista appears to be DOS hostile, from what
I've heard.
```

#### ↳ Re: Can I run Micro Focus COBOL /2 v1.2.29 from XP Pro "Cmd" Window ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-12-15T17:08:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jST8j.185075$Bk7.85391@fe01.news.easynews.com>`
- **References:** `<4763e00d$0$4976$4c368faf@roadrunner.com>`

```
I thought I asked this already, but in the directory
   \PGM\PROGRAMS

what files do you have with their root being
   hs-beg

If you have any ending with .GNT or .INT - those are probably what is being 
"run"

You might want to try
   forcedos hs-beg

as the way to start the application
```

#### ↳ Re: Can I run Micro Focus COBOL /2 v1.2.29 from XP Pro "Cmd" Window ?

- **From:** Robert <no@e.mail>
- **Date:** 2007-12-15T11:12:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be18m31rh0cqnleu4tban503c3asuq8c00@4ax.com>`
- **References:** `<4763e00d$0$4976$4c368faf@roadrunner.com>`

```
On Sat, 15 Dec 2007 09:09:28 -0500, "Will" <Will@somewhere.com> wrote:

>OK guys, it appears the original program was written using .. Micro Focus 
>COBOL/2 Version 1.2.29 L2.2 revision 003
>
>QUESTION: Can I run any of the Micro Focus stuff on my XP Pro machine by 
>going to the DOS prompt via... Start | Run | Cmd ??

Yes. Even better, you can create a shortcut that starts the program (and cmd). Do a right
click on hs-beg.com, select Send To, Desktop. If necessary, adjust the properties of the
shortcut it created. 

>I copied the files from the old DOS 6.2 machine and put them on my XP Pro 
>machine... here are the directories/folders I have... (in the root directory 
…[7 more quoted lines elided]…
>MF-RTE

You don't need source code (.cbl .cpy) at execution time. You do need RTE.

>Looking at the BAT file that seems to launch the application it appears the 
>the application runs under an old GUI program called HI-SCREEN Pro II. (Last 
…[3 more quoted lines elided]…
>machines.

It was probably a graphical user interface (GUI) program for DOS. It started the
application.

>I would have thought there there would have been some compiled .COM or .EXE 
>file that was the actualy Application... but looking at the startup BAT 
…[5 more quoted lines elided]…
>the application

It appears your application was compiled to .gnt files. This is native machine language
like an .exe file, but in a proprietry Micro Focus format. It is loaded by the MF runtime,
usually called COBRUN, with the command COBRUN (your app name). HS Pro probably has a
configuration file containing that command. If it is not in a file, it may be compiled
into hs-beg.com. 

The -F flag tells the MF runtime  to bypass verifying that numeric fields contain numeric
data. It applies only when running interpreted 'intermediate' code, found in .int files,
not to native code found in .gnt files. It was set to speed up execution (speed up
interpreted code??). It is not significant here.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
