[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rebuild under Vista

_9 messages · 5 participants · 2007-11_

---

### Rebuild under Vista

- **From:** foodman <foodman123@aol.com>
- **Date:** 2007-11-26T06:42:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`

```
Hellough:

I upgraded to Vista a few months ago and was happy to see that my
ancient 16-bit MicroFocus-SP2 software runs as happily as it did under
all the prior versions of Windows.

I seldom  use Rebuild since I rarely have problems with files.
However,
I recently ran Rebuild (at the command prompt) and got  "not a valid
win32 application".  My software and the compiler work perfectly.

Strangely, If I make a shortcut to run Rebuild (with file name
specified)
it works perfectly.

Any ideas?

By the way, Murkosoft has not given up on DOS.  I noticed that there
are new commands in the Vista version. One of which is ROBOCOPY,
(Robust Copy).  I think this was in other versions of Windows.

Tony Dilworth
```

#### ↳ Re: Rebuild under Vista

- **From:** "robertwessel2@yahoo.com" <robertwessel2@yahoo.com>
- **Date:** 2007-11-26T15:24:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb12b89f-baa2-4a13-9f3a-50dd6726dfd7@o42g2000hsc.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`

```
On Nov 26, 8:42 am, foodman <foodman...@aol.com> wrote:
> Hellough:
>
…[13 more quoted lines elided]…
> Any ideas?


Try running the program with the forcedos command.  Alternatively,
look carefully at the options you're seeing in the shortcut properties
- those may give you a clue as to what options are needed to run the
16 bit application, and there are a number of settings you can make
that affect the 16 bit emulation environment.


> By the way, Murkosoft has not given up on DOS.  I noticed that there
> are new commands in the Vista version. One of which is ROBOCOPY,
> (Robust Copy).  I think this was in other versions of Windows.


Do *not* confuse the command line with DOS.  There are a huge number
of 32 bit (and 64 bit) command line executable programs in Windows,
and likely always will be.  MS-DOS emulation (which often happens
automatically when you run a 16 bit program from the command line), is
a whole different story.  While MS-DOS emulation in *32* bit versions
of Vista is basically unchanged from that in XP, it is flatly gone in
all 64 bit versions of Windows.  The command prompt remains in all
cases, but only 32 and 64 bit programs are executable from there under
64 bit versions of Windows.
```

##### ↳ ↳ Re: Rebuild under Vista

- **From:** foodman <foodman123@aol.com>
- **Date:** 2007-11-27T06:04:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ac703f9-9714-4eba-a72b-64ff127bd8ae@i29g2000prf.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com> <eb12b89f-baa2-4a13-9f3a-50dd6726dfd7@o42g2000hsc.googlegroups.com>`

```
> Try running the program with the forcedos command.

Seems like ForceDos is not in Vista.  I copied it from an XP machine
but
get "failed to create the process" on the Vista machine.

In case anyone is interested in the DOS commands in Vista, here they
are:



For more information on a specific command, type HELP command-name
ASSOC          Displays or modifies file extension associations.
ATTRIB         Displays or changes file attributes.
BREAK          Sets or clears extended CTRL+C checking.
BCDEDIT        Sets properties in boot database to control boot
loading.
CACLS          Displays or modifies access control lists (ACLs) of
files.
CALL           Calls one batch program from another.
CD             Displays the name of or changes the current directory.
CHCP           Displays or sets the active code page number.
CHDIR          Displays the name of or changes the current directory.
CHKDSK         Checks a disk and displays a status report.
CHKNTFS        Displays or modifies the checking of disk at boot time.
CLS            Clears the screen.
CMD            Starts a new instance of the Windows command
interpreter.
COLOR          Sets the default console foreground and background
colors.
COMP           Compares the contents of two files or sets of files.
COMPACT        Displays or alters the compression of files on NTFS
partitions.
CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
               current drive.
COPY           Copies one or more files to another location.
DATE           Displays or sets the date.
DEL            Deletes one or more files.
DIR            Displays a list of files and subdirectories in a
directory.
DISKCOMP       Compares the contents of two floppy disks.
DISKCOPY       Copies the contents of one floppy disk to another.
DISKPART       Displays or configures Disk Partition properties.
DOSKEY         Edits command lines, recalls Windows commands, and
               creates macros.
DRIVERQUERY    Displays current device driver status and properties.
ECHO           Displays messages, or turns command echoing on or off.
ENDLOCAL       Ends localization of environment changes in a batch
file.
ERASE          Deletes one or more files.
EXIT           Quits the CMD.EXE program (command interpreter).
FC             Compares two files or sets of files, and displays the
               differences between them.
FIND           Searches for a text string in a file or files.
FINDSTR        Searches for strings in files.
FOR            Runs a specified command for each file in a set of
files.
FORMAT         Formats a disk for use with Windows.
FSUTIL         Displays or configures the file system properties.
FTYPE          Displays or modifies file types used in file extension
               associations.
GOTO           Directs the Windows command interpreter to a labeled
line in
               a batch program.
GPRESULT       Displays Group Policy information for machine or user.
GRAFTABL       Enables Windows to display an extended character set
in
               graphics mode.
HELP           Provides Help information for Windows commands.
ICACLS         Display, modify, backup, or restore ACLs for files and
               directories.
IF             Performs conditional processing in batch programs.
LABEL          Creates, changes, or deletes the volume label of a
disk.
MD             Creates a directory.
MKDIR          Creates a directory.
MKLINK         Creates Symbolic Links and Hard Links
MODE           Configures a system device.
MORE           Displays output one screen at a time.
MOVE           Moves one or more files from one directory to another
               directory.
OPENFILES      Displays files opened by remote users for a file share.
PATH           Displays or sets a search path for executable files.
PAUSE          Suspends processing of a batch file and displays a
message.
POPD           Restores the previous value of the current directory
saved by
               PUSHD.
PRINT          Prints a text file.
PROMPT         Changes the Windows command prompt.
PUSHD          Saves the current directory then changes it.
RD             Removes a directory.
RECOVER        Recovers readable information from a bad or defective
disk.
REM            Records comments (remarks) in batch files or
CONFIG.SYS.
REN            Renames a file or files.
RENAME         Renames a file or files.
REPLACE        Replaces files.
RMDIR          Removes a directory.
ROBOCOPY       Advanced utility to copy files and directory trees
SET            Displays, sets, or removes Windows environment
variables.
SETLOCAL       Begins localization of environment changes in a batch
file.
SC             Displays or configures services (background processes).
SCHTASKS       Schedules commands and programs to run on a computer.
SHIFT          Shifts the position of replaceable parameters in batch
files.
SHUTDOWN       Allows proper local or remote shutdown of machine.
SORT           Sorts input.
START          Starts a separate window to run a specified program or
command.
SUBST          Associates a path with a drive letter.
SYSTEMINFO     Displays machine specific properties and configuration.
TASKLIST       Displays all currently running tasks including
services.
TASKKILL       Kill or stop a running process or application.
TIME           Displays or sets the system time.
TITLE          Sets the window title for a CMD.EXE session.
TREE           Graphically displays the directory structure of a drive
or
               path.
TYPE           Displays the contents of a text file.
VER            Displays the Windows version.
VERIFY         Tells Windows whether to verify that your files are
written
               correctly to a disk.
VOL            Displays a disk volume label and serial number.
XCOPY          Copies files and directory trees.
WMIC           Displays WMI information inside interactive command
shell.

For more information on tools see the command-line reference in the
online help.
```

#### ↳ Re: Rebuild under Vista

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2007-11-27T07:27:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xFP2j.158805$kj1.68453@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`

```
foodman wrote:
> Hellough:
> 
…[19 more quoted lines elided]…
> Tony Dilworth

I am hoping to stay on XP for as long as possible.  I've heard bad 
things about DRM bloat in Vista.

In XP I am accustomed to using CMD.EXE for the command-line window.  I 
found that the old Realia COBOL educational compiler blows up if run 
in a CMD.EXE window.  But XP still has COMMAND.COM, and the 1990 
Realia compiler runs fine in COMMAND.COM.  The generated executables 
run file in either CMD.EXE or COMMAND.COM.

I have been using ROBOCOPY for backups for the last 2 or 3 years, but 
it was not part of Windows.  ROBOCOPY is free, but I had to download a 
Microsoft SDK in order to get it.  If ROBOCOPY is included in Vista, 
that's a plus.
```

##### ↳ ↳ Re: Rebuild under Vista

- **From:** foodman <foodman123@aol.com>
- **Date:** 2007-11-27T06:12:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ada8d2-86ed-4cf6-b0c5-586b44511189@d27g2000prf.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com> <xFP2j.158805$kj1.68453@bgtnsc04-news.ops.worldnet.att.net>`

```
>
> I am hoping to stay on XP for as long as possible. �I've heard bad
> things about DRM bloat in Vista.


Based on my several months of experience with Vista, I cannot think of
a single reason why anyone would want to get it.  I had BIG problems
installing the stupid thing, too.  Originally, I had 'only' 1g of RAM,
I added another 512mb and it is still as slow as molasses.

For unimaginable reasons, Microsoft has chosen to change lots of
things
such as the Search.  By no stretch of my imagination can I find ANY
improvements in Vista, but there are lots of things which are just
different (and worse).

And, it is no more dependable than XP.
```

###### ↳ ↳ ↳ Re: Rebuild under Vista

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-11-27T08:19:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BHV2j.3849$4q5.3712@nlpi069.nbdc.sbc.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com> <xFP2j.158805$kj1.68453@bgtnsc04-news.ops.worldnet.att.net> <74ada8d2-86ed-4cf6-b0c5-586b44511189@d27g2000prf.googlegroups.com>`

```
"foodman" <foodman123@aol.com> wrote in message 
news:74ada8d2-86ed-4cf6-b0c5-586b44511189@d27g2000prf.googlegroups.com...

>Based on my several months of experience with Vista, I cannot think of
>a single reason why anyone would want to get it. ...

>For unimaginable reasons, Microsoft has chosen to change lots of
>things ...no stretch of my imagination can I find ANY
>improvements in Vista, but there are lots of things which are just 
>different (and worse).

I think I've heard this about every new operating system, ever.

> And, it is no more dependable than XP.

Here, you have a really good point. Even Win/XP took a couple of service 
packs (= a couple of years)  to get all the kinks out. I recently purchased 
a new laptop, and paid extra to "downgrade" from the included Vista to 
Win/XP Pro precisely for that reason.

Features are nice, but they are no substitute for reliability.

MCM
```

##### ↳ ↳ Re: Rebuild under Vista

- **From:** foodman <foodman123@aol.com>
- **Date:** 2007-11-27T06:20:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ed2cf904-9f7f-458c-ab53-dbe0fe87a041@s19g2000prg.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com> <xFP2j.158805$kj1.68453@bgtnsc04-news.ops.worldnet.att.net>`

```
But XP still has COMMAND.COM, and the 1990
> Realia compiler runs fine in COMMAND.COM. �The generated executables
> run file in either CMD.EXE or COMMAND.COM.


I tried both CMD and COMMAND, neither of them run Rebuild.exe

tony
```

#### ↳ Re: Rebuild under Vista

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-11-27T21:34:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Qd2dneIdGcNWctHanZ2dnUVZ_hadnZ2d@comcast.com>`
- **In-Reply-To:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com>`

```
foodman wrote:
> Hellough:
> 
…[13 more quoted lines elided]…
> Any ideas?

Is it a 64-bit version of Vista?  The 64-bit Vista doesn't support 
16-bit Windows applications.

Since a shortcut works, though, it's strange that it doesn't work under 
a command prompt.  Maybe the shortcut looks at the executable, and sets 
a "compatibility mode" for it.  Inspect the properties of the shortcut, 
and see if any of those are set.  If so, you can make a shortcut to 
cmd.exe with those same compatibilities set, and you should be good to go.
```

##### ↳ ↳ Re: Rebuild under Vista

- **From:** foodman <foodman123@aol.com>
- **Date:** 2007-11-28T04:31:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4dc5ed3-e16e-4ed3-b8e2-919686d23f6a@e1g2000hsh.googlegroups.com>`
- **References:** `<f36afd86-e1c0-4bc1-9695-6e9972f346e6@d61g2000hsa.googlegroups.com> <Qd2dneIdGcNWctHanZ2dnUVZ_hadnZ2d@comcast.com>`

```
�Inspect the properties of the shortcut,
> and see if any of those are set. �If so, you can make a shortcut to
> cmd.exe with those same compatibilities set, and you should be good to go.


Thanks for the suggestion, but, it still does not work!

tony
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
