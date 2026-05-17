[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL FAQ

_3 messages · 2 participants · 1998-02_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### COBOL FAQ

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dc0ja$8pi@dfw-ixnews6.ix.netcom.com>`

```

COBOL FAQ
(Frequently Asked Questions)

Last-Modified: Sunday, March 01, 1998
(The current version of this document still includes significant information
from the February '97 edition. I am attempting to update this as time
permits. For details of what technical items have changed so far, please see
Appendix A.2 - Changes to create Version 2.0x.)
This page accessed times
Version: 2.05
Additional information and corrections are encouraged. Please send comments
to
wmk··.@ix.··m.com
0. CONTENTS
1. Copying this FAQ
2. Where can I get this FAQ?
3. Where can I get a COBOL compiler?
3.1 for DOS, Windows or OS/2?
3.2 for Windows/NT?
3.3 for UNIX?
3.4 for Linux?
3.5 for the Macintosh?
3.6 for other environments?
4. Is there a free COBOL compiler?
4.1 for DOS, Windows or OS/2?
4.2 for Windows/NT?
4.3 for UNIX?
4.4 for the Macintosh?
4.5 for other environments?
5. Commercial COBOL Products
5.1 Micro Focus
5.2 AcuCOBOL
5.3 Liant/RM
5.4 CA-Realia
5.5 PCYACC
6. Where can I contact...
6.1 AcuCOBOL?
6.2 Liant?
6.3 Micro Focus?
6.4 CA?
6.5 RM?
6.6 mbp ?
6.8 Sinc Inc.?
6.9 Flexus?
7. COBOL standards.
7.1 What standards exist?
7.2 Can I get the standards via FTP?
7.3 What is happening with the draft of the next COBOL Standard and what is
in it?
8. COBOL 6.50
8.1 How do I compile my programs?
8.2 How do I link my objects?
9. What about OO COBOL?
9.1 ANSI and ISO Work
9.2 Micro Focus
9.3 IBM
9.4 Others
10. Books about COBOL
10.5 "COBOL For Dummies"
10.22 "Teach Yourself COBOL in 21 Days",
11. Is there a COBOL to C converter?
12. COBOL code generators
12.1 Telon
13. COBOL Tools
13.1 Windowing
13.1.1 VanGui for RM/COBOL
13.1.2 Dialog System for Micro Focus COBOL
13.1.3 Flexus COBOL spII
13.1.4 CA-Visual Realia
13.2 Sinc Inc. products
13.2.1 FlexGen 4GL Rapid Application Development Environment
13.2.2 Legacy Liberator COBOL Migration Toolset
13.2.3 Easy Query
13.2.4 ODBC Access Tools
13.3 Misc. tools
14. Other sources of information.
14.1 CompuServe
14.2 Bix
14.3 Micro Focus Faxback
14.4 Micro Focus WWW server
14.5 CA WWW server
14.6 Liant Ryan McFarland WWW server
14.7 AcuCOBOL WWW server
14.8 The COBOL Foundation
14.9 The IBM COBOL products WWW server
14.10 The Flexus WWW server
14.11 COBOL User Groups
15. Information required for the FAQ
16. Contributors to the FAQ
17. What about the Y2K (Millenium) Issue?
17.1 Where can I get information about the Y2K problem?
18. What can/should I post in the COBOL newsgroups?
18.1 Can I get help with homework via the newsgroups?
18.2 Can I post job openings in the newsgroups and if so what should I
include?
Appendix A. Changes in recent revisions
Appendix A.1 - Changes to create Version 2.0
Appendix A.2 - Changes to create Version 2.0x

1. Copying this FAQ.
This FAQ is copyright 1994-19978 by William M. Klein.
It may be freely redistributed as long as it is completely unmodified and
that no attempt is made to restrict any recipient from redistributing it on
the same terms. It may not be sold or incorporated into commercial documents
without the written permission of the copyright holder.
Permission is granted for this document to be made available for file
transfer from sites offering unrestricted file transfer on the Internet and
from the COBOL Forums on CompuServe and Bix.
This document is provided as is, without any warranty. Your mileage may
vary.

2. Where can I get this FAQ?
This document should be archived at many sites on the Internet, including
rtfm.mit.edu -- the archive site for all FAQs. It is also available via
e-mail from the author (wmk··.@ix.··m.com).
An HTML version of the latest FAQ is also available from
http://www.netcom.com/~wmklein/cobolfaq.htm

3. Where can I get a COBOL compiler?
There are many vendors who sell COBOL compilers. Almost all of the mainframe
hardware/operating system vendors, also sell a COBOL compiler for their
systems. The following are some of the vendors providing COBOL compilers for
systems where they are not the operating system vendor.
3.1 for DOS, Windows, or OS/2?
AcuCOBOL, CA, Ryan McFarland, IBM, and Micro Focus all produce compilers for
one or more of these environments. Microsoft used to re-badge the Micro
Focus compiler, but not any more.
3.2 for Windows/NT?
Micro Focus has a COBOL 32-bit SDK available for Windows/NT and also the OO
COBOL product. AcuCOBOL-85 (again 32-bit) is also available. Fujitsu's
compiler also works under Windows/NT.
3.3 for UNIX?
AcuCOBOL, Ryan McFarland, and Micro Focus have products available across a
large number of UNIX platforms. Some OEMs re-badge and/or re-engineer these
products for their own systems too.
Liant has LPI COBOL available for Sun SPARC with Solaris 2, HP 9000 with
HP-UX and Intel-based machines with UNIX SVR4, SVR3, and SCO.
3.4 for Linux?
AcuCOBOL-85 and AcuCOBOL-GT are available for Linux. Also, the iBCS2 code
for Linux should mean that it is possible to get some of the i486 COBOL
packages for operating systems such as SCO UNIX to work.
Ralf Draeger (dra··.@inf··n.de) reports that it is
possible to get programs compiled using Micro Focus COBOL on SCO UNIX to run
on Linux.
Norman Hull (nor··.@i··.ie) adds :
"Using Micro Focus COBOL v3.1 for SCO UNIX and Linux kernels 1.1.35 and
1.1.45 with the iBCS code, programs will compile on Linux to .int code, but
fail when data is entered (the tictac demo. program fails with illegal
character in numeric field, whatever data is entered).
When the .int code is created under SCO and transferred to Linux, it runs in
exactly the same way as it does on SCO.
If compiled to .gnt code, the program runs without any problems on Linux."
3.5 for the Macintosh?
Micro Focus and AcuCOBOL produce a COBOL development system for the Mac
running A/UX.
3.6 for other environments?
Ryan McFarland COBOL is also available for OpenVMS.
AcuCOBOL-85 and AcuCOBOL-GT are available on a wide range of environments,
including OpenVMS.
Most major vendors have their own COBOL implementation, or have someone
else's ported to their platform(s). There are quite a few available for CP/M
and MP/M, and one is even rumored to have been available for the PERQ
workstation.

4. Is there a free COBOL compiler?
Just for the record, no COBOL tools are listed in the Catalog of compilers,
interpreters, and other language tools posted to comp.compilers and
comp.lang.misc. This probably means that there are no freely available COBOL
compiler sources.
However, several books in the booklists come with a COBOL compiler. See
section 10 for details.

4.1 for DOS, Windows or OS/2.
There is a freely available COBOL compiler for DOS. It can be found on many
archive sites, named COBOL650.ZIP. You also need DPATH30.ZIP. Have a read
through Section 8 before you start.
Bob Wolfe has made the compiler available at the Flexus FTP site,
http://www.flexus.com.
It is widely rumored that the sources for this compiler are available from a
BBS. This no longer appears to be the case. Numerous attempts have
completely failed to track down the sources.
There is a COBOL701.ARJ archive that contains a version of COBOL 6.50 with a
limited number of compiles. It was an attempt at a full integrated
development environment, including an editor. Unfortunately, no
documentation is included.
Also, it may be possible to run the freely available CP/M compiler (see 4.5)
under a freely available CP/M emulator.
In addition, Fujitsu is currently offering a copy of their PowerCOBOL to
those who register at
http://www.adtools.com/
4.2 for Windows/NT?
The CP/M compiler/emulator combination should work here too; as does the
Fujitsu compiler.
4.3 for UNIX?
There are no well-documented examples of a freely available COBOL compiler
for UNIX. COBOL 6.50 might run under a UNIX emulation of a DOS system,
however. (For example, VP/ix, SoftPC or dosemu under Linux.)
The CP/M compiler (see 4.5) should run under a CP/M emulator for UNIX in a
similar fashion.
4.4 for the Macintosh?
Not that I know of.
4.5 for other environments ?
There is a freely available CP/M COBOL compiler/interpreter (NPS Micro
COBOL). This is available via anonymous FTP from oak.oakland.edu in
/pub/cpm/cobol. However, Stefano Priola (s70··.@gal··o.it) comments
:
"I've used the CPM COBOL ... I think that this compiler is much too old to
use or for a student to learn COBOL."

5. Commercial COBOL Products
In order to present an un-biased list of commercial COBOL product offerings
I've pulled in the product overviews from each company's marketing
information. For detailed product descriptions, you should probably contact
the specific vendor.
5.1 Micro Focus
5.1.1 Micro Focus(r) Object COBOL v4.0 (32-bit) for OS/2
Micro Focus Object COBOL v4.0 is a powerful 32-bit development environment,
enabling development and deployment of COBOL and Object COBOL applications
for OS/2.(r) Micro Focus has brought the power of COBOL to the PC with
extensive syntax support, including object oriented COBOL, IBM(r) OS/VS
COBOL, DOS COBOL, COBOL/370(tm) and a wide range of other dialects. This
release of Object COBOL extends the power of previous versions of Micro
Focus COBOL by adding full support for object oriented programming and
exploiting the power of the 32-bit architecture.
5.1.2 Micro Focus(r) Object COBOL(tm) v4.0 (32-bit) for Windows NT and
Windows(r) 95
Micro Focus Object COBOL v4.0 is a powerful 32-bit programming environment
for the development and deployment of COBOL and Object COBOL applications on
Windows NT(tm) and Windows(r) 95. Micro Focus has brought the power of COBOL
to the PC with extensive syntax support, including object oriented COBOL,
IBM(r) OS/VS COBOL, DOS COBOL, COBOL/370(tm) and a wide range of other
dialects. This release of Object COBOL extends the power of previous
versions of Micro Focus COBOL by adding full support for object oriented
programming and exploiting the power of the 32-bit architecture.
5.1.3 Object COBOL (tm) D e v e l o p e r Suite v4.1 for UNIX
Micro Focus Object COBOL Developer Suite v4.1 for UNIX is an advanced
integrated programming environment for developing and deploying client
/server Object COBOL and procedural COBOL applications on a wide range of
UNIX (r) operating environments. It includes: a flexible, cross-platform
COBOL compiler; a set of powerful programmer productivity tools; a set of
Object COBOL class libraries; transparent support for large files; support
for DBCS applications; COBOL access to industry standard Object Request
Broker (ORB) technology; user interface development tools; new on-line
documentation; the ability to execute COBOL CGI's; and run-time facilities
to simplify application deployment.
5.1.4 Personal COBOL for Windows v3.1, with Object Orientation
Micro Focus Personal COBOL for Windows 3.1, with Object Orientation, is an
educational version of Micro Focus COBOL for anyone interested in learning
procedural COBOL programming or the new object-oriented COBOL extensions in
a Windows 3.1 environment.
Personal COBOL is ideal for educational institutions, students, training
organizations and self-learners who need an inexpensive, yet full-featured
and modern learning tool for introductory or advanced COBOL.
5.1.5 COBOL Workbench(r) v4.0
Workbench integrates the industry-standard COBOL compiler with development
and testing tools that promote programmer productivity, satisfaction and
quality systems development. It features powerful editing, debugging and
communications facilities as well as graphical data tools - all within a
powerful and easy to use development environment. Micro Focus COBOL
Workbench supports the creation and maintenance of enterprise-wide
client-server applications in addition to offloading development and
maintenance of mainframe application to PCs.
5.2 AcuCOBOL
5.2.1 AcuCOBOL-GT
AcuCOBOL-GT enables COBOL programmers to implement and deliver full-featured
GUI COBOL applications on any of over 600 platforms, with full object code
portability using a single set of COBOL source code. Programmers can create
graphical applications including floating windows, graphical controls (such
as entry fields, frames, radio buttons, push buttons, and labels), menu
bars, bitmaps, and toolbars using COBOL extensions that are consistent with
traditional COBOL syntax.
5.2.2 AcuCOBOL-85
AcuCOBOL-85 is a powerful ANSI-85 COBOL compiler that offers exceptionally
compact, highly optimized machine-independent COBOL code. AcuCOBOL-85 is
portable across over 600 different platforms, including: AIX, AOS/VS,
BSD/OS, DG/UX, Digital UNIX, HP-UX, Linux, MS-DOS, MPE/iX, Open VMS, OS/2,
Solaris, Ultrix, UNIX, UnixWare, Windows, Windows NT, and Xenix.
5.3 Liant/Ryan McFarland
5.3.1 RM/COBOL Compiler and Runtime System
RM/COBOL's sophisticated runtime system permits the maintenance of single
source and object code - and the easy deployment of applications on a wide
choice of open client/server platforms.
5.3.2 RM/Interface Builder
RM/COBOL developers can now use their choice of industry-standard tools such
as Microsoft's Visual Basic and Borland's Delphi to develop a true Windows
client user interface for Windows or UNIX-based COBOL application
5.3.3 RM/Enterprise CodeBench
RM/COBOL developers can now take full advantage of their client/server
development environments. This new version of our powerful graphical
workbench enables the management of existing UNIX- or Windows-based RM/COBOL
applications to be handled from a remote Windows workstation.
5.4 Computer Associates/Realia
5.4.1 CA-Realia(r) COBOL
CA-Realia(r) COBOL is a comprehensive, mainframe-compatible COBOL
development platform for the PC. It enables users to downsize mainframe
applications to produce cost-effective PC-LAN-based applications; offload
mainframe COBOL program development to PC-based programmer workstations; and
develop state-of-the-art PC applications. Available for: DOS, OS/2
5.5 PCYACC
PCYACC 7.5 is a complete language development environment that generates C,
C++, Java, Delphi, and VBS source code from input Language Description
Grammars for building Assemblers, Compilers, Interpreters, Browsers, Page
Description Languages, Language Translators, Syntax Directed Editors,
Language Validators, Natural Language Processors, Expert System Shells, and
Query Languages. The PCYACC Tool-Kit includes PCLEX, Visual Debugging Tools,
Object-Oriented Class Library's, and Pre-Written "Drop-In" Language engines
for virtually every computer language in the world.
Note the original information stated that support was for the 77 and 90
Standards (which are good years for the Fortran Standard but not for COBOL).
It is assumed that they actually support the 74 and 85 Standards of COBOL.
Contact them at:
http://www.abxsoft.com/

6. Where can I contact ...
6.1 AcuCOBOL?
AcuCOBOL
7950 Silverton Avenue
Suite 201
San Diego, CA 92126
Tel: 619-689-7220 (or 1-800-COBOL-85 in the US)
Fax: 619-566-3071
Email: in··.@acu··l.com and sup··.@acu··l.com.
CompuServe: GO AcuCOBOL
WWW: http://www.acucobol.com
6.2 Liant?
6.2.1 In the US
Liant Software Corporation
959 Concord Street
Framingham, MA 01701
USA
Tel: (508) 872-8700
Fax: (508) 626-2221
Email: in··.@lpi··t.com sup··.@lpi··t.com
www: http://lsc.liant.com/index.html
6.2.2 In the UK
Liant Software Ltd
2 Caxton Street
St. James Park
London SW1H 0QE
UK
Tel: +44 71 799 2434
Fax: +44 71 799 2552
Email: in··.@lia··o.uk
6.2.3 In Japan
Nippon Liant Ltd
31-8, Takasecho
Funabashi City,
Chiba 273, Japan
Tel: +81 47 437 9816
Fax: +81 47 437 9818
6.3 Micro Focus?
6.3.1 In the US
Micro Focus Inc.
701 E. Middlefield Road
Mountain View, CA 94043
Tel: 650-938-3700
Fax: 415-856-6134
WWW: http://www.microfocus.com
6.3.2 In the UK
Micro Focus Ltd
The Lawn,
Old Bath Road,
Newbury,
Berks.
RG14 1QN
UK
Tel: 01635-32646
Fax: +44-635-33966
WWW: http://www.mfltd.co.uk
6.4 Computer Associates?
6.4.1 For product inquiries
Computer Associates
One Computer Associates Plaza
Islandia,
NY 11788-7000
USA
Tel: 1-800-CALL CAI (225-5224
email: cai··.@c··.com
www: http://www.cai.com/
6.4.2 For technical inquiries:
Computer Associates
2400 Cabot Drive
Lisle,
IL 60532-3652
USA
Tel: (708) 505-6885
6.5 Ryan McFarland?
6.5.1 In the US
Ryan McFarland
a Division of Liant Software Ltd
8911 N. Capital of Texas Highway
Suite 4300
Austin, TX 78759
Tel: (512) 343-1010
Fax: (512) 343-9487
Toll Free: 1-800-RM-COBOL

Sales information is also available by e-mail from rm_··.@li··t.com
6.5.2 In the UK
Ryan McFarland
a Division of Liant Software Ltd
2 Caxton Street
St. James Park
London SW1H 0QE
UK
Tel: +44 71 799 2434
Fax: +44 71 799 2552
6.5.3 In Japan
Nippon Liant Ltd.
31-8, Takasecho
Funabashi City,
Chiba 273, Japan
Tel: +81 47 437 9816
Fax: +81 47 437 9818

6.8 Sinc Inc.?
6.8.1 In the US
Sinc, Inc
Dayton, Ohio
Tel: 513-438-5553
Fax: 513-438-5377
glu··.@day··n.net
CompuServe: 75224,3207
6.8.2 in Europe
EasiRun Europa Gmbh
Usingen,
Germany
Tel: (0)6081 91603
Fax: (0)6081 916049
100··.@com··e.com
6.8.3 In South Africa
EasiRun International
Johannesburg,
South Africa
Tel: (0)11 421 4800
Fax: (0)11 421 4999
Pa··.@eas··o.za
6.8.4 In Australia
EasiRun Australia
Sydney,
NSW
Tel: (0)2 955 5058
Fax: ()4 754 4359
100··.@com··e.com

6.9 Flexus?
Flexus
PO Box 640,
Bangor,
PA 18013-0640
Tel: 610 588 9400
Fax: 610 588 9475
BBS: 610 863 4740
E-mail: in··.@fle··s.com, tec··.@fle··s.com
www: http://www.flexus.com/

7. What about COBOL standards?
7.1 What standards exist ?
The current COBOL standard is the ISO/ANSI '85 standard. This replaced the
ANSI '74 standard.
There are two amendments to the COBOL '85 standard -- intrinsic functions
and corrections.
ISO should be producing a new standard in 1997. Don Nelson is the editor and
has offered to answer any questions about it.
7.2 Can I get the standards via FTP.
The standards do not appear to be available via FTP. This is probably
because they are very large and are copyrighted by ANSI and/or ISO, although
the issue of copyright is put into doubt given the following statement from
Bill Klein :
Whether or not the next COBOL Standard will or will not be copyrighted is a
matter of discussion and argument. As the current Standard was put into the
"public domain" and the next standard is a "derived" work, it is
questionable whether or not the next Standard will have an ISO or ANSI - or
any other copyright.
7.3 What is happening with the draft of the next COBOL Standard and what is
in it?

First "9x" has become "0x". After the last public review, it turns out that
there will need to be at least one more public review before it gets
approved.
1. Major features/enhancements:
A. OO gets all the press
B. Common exception handling, C-ification (pointers, call prototypes,
typedefs, and everything else needed to use C-type APIs), user-defined
functions, file-sharing/record-locking, 31-digit numbers, portable
arithmetic, National character handling (MOCS or DBCS but more so), are all
some of the "biggies" that some people are looking for.
C. In the category of "old technology" getting a new face lift and being
added to the Standard (as required) see Report Writer enhancements, VALIDATE
feature, and character screen I/O support via ACCEPT/DISPLAY.
1. Little things (and there are too many for me to remember off the top of
my head) include everything from dynamic file assignment (in the
SELECT/ASSIGN statement), assigning multiple values via the VALUE statement
in tables, sorting tables, hex literals, GOBACK verb, apostrophe as quote,
bits and Boolean support,
and LOTS more

8. COBOL 6.50
8.1 How do I compile my programs?
It is assumed you have installed cobol650.zip in the directory C:\COBOL650.
In install.doc you will find some information on running the compiler.
1. Add C:\COBOL650 to the PATH
2. Run APPEND on C:\COBOL650 :
APPEND C:\COBOL650
3. The install.doc contained in cobol650.zip refers to a program DPATH.COM
to be run instead of APPEND. The DOS program APPEND seems to work too.
4. Now you can compile your .cob files as explained in install.doc.
When trying to compile sources in a directory other than that where the
compiler is installed, the compiler terminates without an error. This
restriction is not documented in install.doc, which is probably a result of
using APPEND instead of DPATH.
The compiler accesses drive A:. You should have a disk in this drive.
Peter Mikalajunas adds:
To avoid the need to use drive A:, you should do the following :
subst a: c:\cobol650
When you type A: you will drop into the C:\COBOL650 subdirectory. The
compiler will behave normally at this point, not constantly searching drive
A:.
When you are done with a session do the following :
C:
subst a: /D
8.2 How do I link my objects ?
There is no linker with the COBOL 6.50 compiler. To link objects you need to
use the linker from MS-DOS v3.3 or earlier.
Ralf Laemmel adds :
You can use newer linkers, especially from newer Microsoft compiler
products, too.
And Peter Mikalajunas has found that :
Tlink compiled with obj files without complaint, but the exe's were useless.
What did work was Link version 5.31.009 which comes with Visual Basic for
DOS. It compiled all obj files I tried and the EXEs ran perfectly.
Clinton G. Downing also reports :
The linker from IBM DOS v2.1 does now work, at least on the PS/2 70. The
MS-DOS v3.3 linker works fine, however.
Steve ??? has reported some success with a linker
from the SimTel archives. Look for sl101a.zip.

9. What about OO COBOL?
9.1 ANSI and ISO Work
The draft of the Committee Draft (CD !>!) of the next COBOL Standard which
underwent public review in 1997 included significant OO COBOL support. Based
on the comments received J4 (ANSI) and WG4 (ISO) or currently revising it
(and deleting some features. In order to see a copy of the latest draft of
the current definition see 7.2 Can I get the standards via FTP ?
9.2 Micro Focus
Micro Focus has an OO COBOL product. It does not conform exactly to the OO
COBOL proposal currently being discussed, however -- the syntax is a subset
of the current proposal with a few variations. Multiple inheritance,
conformance and garbage collection are not implemented. Also, vocabularies
are implemented though these are not currently part of the proposed
standard.
9.3 IBM
IBM offers OO COBOL products for MVS, OS/2, Windows, and AIX. (It does not
currently offer it for OS/400 or VM). There implementation is a subset of s
snap-shot of the Standard as it was in 1995. The syntax is portable across
their platforms and interfaces with SOM and DSOM.
9.4 Others
I believe that other vendors are at various stages of developing, testing,
and distributing OO COBOL products. For specific product information, you
should contact the vendor (such as Fujitsu, Hitachi, Realia, etc)

10. Books about COBOL.
10.1 "Advanced ANSI COBOL with Structured Programming (2nd ed.)"
ISBN 0-471-54786-7
by Gary DeWard Brown, published by John Wiley & Sons.
Apparently this is one of the few books which covers ANSI 85 COBOL.
10.2 "Application Programming and File Processing in COBOL",
ISBN 0-669-16570-0
by Yuksel Uckan, published by D.C. Heath and Co., 1992
This is also available in two volumes :
10.3 "Application Programming in COBOL (Volume 1)"
ISBN 0-669-28207-3
"File Processing in COBOL (Volume 2)". ISBN 0-669-28208-1.
10.4 "COBOL 85 For Programmers"
ISBN 0-444-01232-X
by Don Nelson, published by North-Holland, price 10 USD.
It is available only from the author.
10.5 "COBOL For Dummies"
To install the Fujitsu compiler that comes with this book, you will need to
enter a serial number that was accidentally left out of the first printing
of the book. It will install with this number:
103-2001 1699-03317-70168
The first part of the number should already be in the window, so all you
will have to enter is
99-03317-70168
10.6 "COBOL 85 For Programmers"
ISBN 0-471-92156-4
by Jim Inglis, published by John Wiley and Sons.
First edition in 1989, 287 pages.
Third reprint cost 17.50 UKP, May '91.
10.7 "COBOL: Der Einstieg
ISBN 3-8006-1673-4
By Andreas Tietz, published by Vahlen Verlag, Mï¿½nchen.
A German language book.
10.8 "COBOL from Micro to Mainframe"
ISBN 0-13-138686-7
by Robert Grauer, published by Prentice Hall.
This includes a disk containing a student edition of CA-Realia COBOL and
interactive COBOL debugger.
US price (May '94) : $55
This book may have been released as several volumes and as a complete work.
I'm not sure to which the ISBN applies. The ISBN 0-13-140179-3 has been
suggested for Volume I by William Fang .
10.9 "The COBOL Presentation Manager Programming Guide"
ISBN 0-442-01293-4
by David M. Dill, published by Van Nostrand Reinhold.
10.10 "Comprehensive Structured COBOL"
ISBN unknown
by L. Wayne Horns. Comes with an RM compiler.
10.11 "Comprehensive Structured COBOL (Third edition)",
ISBN 0-534-91781-X
by Gary S. Popkin, published by PWS-KENT (Division of Wadsworth Inc).
Covers ANSI-74 and ANSI-85 COBOL in detail. Highly recommended by
m.w··.@rea··o.uk.
10.12 "Modern COBOL Programming"
ISBN 0-394-39100-4
by Price/Olson published by McGraw Hill
Comes with RM/COBOL-85
US price (June '94): ~$55
10.13 "Object Orientation: An Introduction for COBOL programmers"
ISBN unknown
by Raymond Obin published by Micro Focus Press.
10.14 "OS/2 Presentation Manager Programming for COBOL Programmers"
ISBN unknown
by Robert B. Chapman, published by John Wiley & Sons.
10.15 "The Revolutionary guide to COBOL with compiler"
ISBN 1-874416-17-6
by Yevsei Handel and Boris Degtyar.
Comes with a disk containing a (rest of this information lost in the history
of this FAQ)
10.16 COBOL compiler
written by Dmitry Bronnikov.
Published by Wrox Press Ltd, 1334 Warwick Rd, Birmingham, UK.
10.17 "Comprehensive COBOL
ISBN 0-07-909613-1 (5.25 inch disks)
by Bradley ISBN 0-07-836549-X (3.5 inch disks)
Includes a Liant RM/COBOL-85 DOS compiler and development environment
US price ( April '94): $60.50
10.18 "Structured COBOL, 3rd Edition"
ISBN 0-07-835423-4 (5.25 inch disks)
ISBN 0-07-836489-2 (3.5 inch disks)
by Welburn/Price
Includes a Liant RM/COBOL-85 DOS compiler and development environment
US price (April '94): $67.38
The above two books may be ordered from Mitchell/McGraw Hill,
Tel: (800) 338-3987 (US only) or (619) 426-5000
Juergen Linkens adds :
The compiler is limited as following:
* max. 800 lines of code
* max. 4 files
* max. 1000 records per file
* max. 100 bytes per file record
BTW, the editor coming with it isn't very good either. This is not meant to
be a complaint, just a hint for future issues. I never expected a fully
unlimited compiler for a book price, just a few less limitations.
10.19 "Structured ANSI COBOL Part 1 : A Course for novices using a subset of
1974 or 1985 ANSI COBOL"
ISBN unknown
by Mike Murach and Associates Inc. (1987)
10.20 "Structured ANSI COBOL Part 2 : An advanced course using 1974 or 1985
ANSI COBOL"
ISBN unknown
by Mike Murach and Associates Inc. (1987)
10.21 "Structured COBOL with Business Applications"
ISBN unknown
by Stanley E. Myers published by Prentice Hall.
10.22 "Teach Yourself COBOL in 21 Days
ISBN 0-672-30469-4 by Mo Budlong,
published by SAMS Publishing/MacMillan Computer Publishing
10.23 "Structured COBOL Programming (7th Edition)"
ISBN 0-471-30580-4
by Stern & Stern, published by John Wiley & Sons.
Comes with a syntax guide and an order form for a special offer cut-down
RM/COBOL 85 or Micro Focus Personal COBOL (unmodified).

11. Is there a COBOL to C converter ?
Asking this question anywhere appears to generate much general flaming and
general language wars and very little useful information.
No such beast is listed in the free compilers FAQ, but an ad has appears in
the US publication "Programmer's Shop Catalog" for COBOL to C (and PL/I to
C) translators. Contact :
Micro-Processor Services,
92 Stone Hurst Lane,
Dix Hills, NY 11746
Tel: (516) 499 4461
Fax: (516)- 499-4727
E-Mail: in··.@mps··c.com, mps··.@net··a.net
www: http://www.mpsinc.com
http://www.netusa.net/~mpsinc
A toolset for conversion from COBOL to several other languages is available.
A tool first produces structured diagrams (Nassi-Shneiderman) from existing
source files. Structural errors are identified and you can edit to correct
them. Another tool takes those same diagrams and produces source code in one
of several languages (COBOL, C, Ada, Basic, Clipper, dBaseIV, Fortran,
Modula 2, Natural, PL/1, etc.)
The toolset is called XperCase by Siemens, and is available in the US from:
Boston Technical Distribution Corp.
3 Center Plaza, Suite 440
Boston, MA 02108
Tel: (617) 248-8989
Fax: (617) 248-8986
Laurent Sabarthez contributed :
Some years ago I was Project Leader on a software project termed COBTOC
(COBol TO C translation). The company is by now out of business, but the
rights on this product were purchased by NSI (Network Solutions Inc.,
Herndon, VA, USA - Emitt McHenry was Chairman).
COBTOC is actually a translator generator. It can produce a specialized
translator for any reasonable COBOL dialect, given a dialect description
very close to the usual syntax notation one can find into any COBOL
Reference Manual. "semantics" peculiarities are also described in this way.
Once a translator has been produced in this way, a source management module
allows automated translation of the COBOL source modules. A run-time library
is also automatically produced as a by-product of the translator.
The COBTOC user gets a set of C files, each being the translation of a
corresponding COBOL file. You can get K&R C, ANSI C, or common variants like
Turbo C. The overall structure of the COBOL program is preserved upon
translation. Identifiers are straightforward transformations of COBOL names.
Paragraph structure and flow control are also preserved, like all name space
properties attached to I/O and file management.
The C files are compiled and linked with the run-time library, which
supports data handling, edition, arithmetic, direct I/O, file I/O and
transaction management (e.g. CICS).
Executables are intended to run on any platform supporting POSIX C compiling
and standard library linkage.
COBTOC was left by my co-workers and me in an alpha release state, mid 1993.
I don't know the end of the story, but NSI should provide more up-to-date
information about it.
There is also a project running to create a COBOL to C converter (possibly
COBOL to C++ ?) available under the GNU license.
For more details, see
http://rucs2.sunlab.cs.runet.edu/~msharov/cobcy/cobcy.html, the COBCY WWW
page.
Some people consider that it is possibly cheaper to hire someone to do the
conversion job than to have a program produce C code which could be quite
difficult to read and maintain.
[Note: The above URL for the COBCY Homepage no longer exists.
I will remove this information from a future release of the FAQ unless
someone can update it for me - Bill Klein]

12. COBOL code generators
12.1 Telon
Telon it is a cross between a code database and a code generator. It can be
used to store 'standard' sections of code and 'custom' sections of code from
which you can generate a COBOL program by defining it to use certain sets of
the standard and custom code. This allows you to keep common code once in
the database and maintain it there.
Telon also offers support for screen design.
There is a PC version of the product as well as the mainframe version.
Note: The original vendors have been bought by CA, so Telon is now a CA
Product.

12.3 ETK
ETK (Easy ToolKit) was developed by SEMA Group in Belgium. It is now
marketed by TOSC International, Inc :
TOSC International, Inc.
3900 Essex Lane, suite 250
Houston, TX 77027
Tel: 713 961 1201
Fax: 713 961 4989
Contact Ted Langlie. TOSC will also soon be on the Internet.
ETK works with a repository where the programmer/analyst describes the
system to be generated in terms of data domains, elements, tables,
relationships, business rules, and data mappings. From this description ETK
generates complete COBOL-based applications that will run on many platforms.

13. COBOL Tools
This section documents some of the add-on tools that are available for use
with COBOL compilers. Further submissions are welcomed, but please try to
keep them as free from marketing "hype" as possible.
Note: This section seems to be entirely devoted to tools that run in or are
targeted at the PC and/or Unix world. Mainframe additions are welcome, but
will probably be a while before I can add them.
13.1 Windows and Windowing.
13.1.1 VanGui for RM/COBOL.
VanGui consists of two major components: a design tool and a runtime system.
The design tool is a Windows application which provides COBOL developers
with the capability to define windows, populate those windows with standard
Windows and VBX controls, adjust the properties of those controls and attach
COBOL event-handling logic to their events.
The VanGui Runtime is a Windows .DLL that manages Windows messages, provides
runtime support for the controls, and provides a COBOL interface to the
Windows API.
For more information on VanGui, see
http://www.liant.com/rm/toolset/vangui.html.
13.1.2 Dialog System for Micro Focus COBOL
Dialog System provides a design tool for defining windows and their contents
and creating code for manipulating data and events within those windows. The
resulting output is platform independent, allowing code to be transferred
between DOS/Windows, OS/2 and UNIX. Under UNIX, only the character-based
version of Dialog System is still supported -- support for the X11 version
has been stopped.
13.1.3 Flexus COBOL spII
COBOL spII allows the COBOL programmer to create GUI or character mode
screens using ANSI standard COBOL CALL USING statements. COBOL spII screen
definitions and source programs are 100% COBOL compiler independent, 100%
operating system independent and 100% text mode to GUI mode independent.
Automatic screen conversion tools for many proprietary environments are also
available from Flexus. These automate the task of converting screen
definitions from proprietary character mode screens to GUI screen
definitions.
13.1.4 CA-Visual Realia
[From CA's Web site:]
CA-Visual Realia is a complete Windows development environment that provides
COBOL programmers with an easy-to-use set of tools for creating
mission-critical GUI client/server applications. CA-Visual Realia allows you
to create Windows applications using COBOL for the business logic and GUI
tools for the user interface. CA-Visual Realia combines tools designed for
Windows user interface development with powerful COBOL program development
tools. Creating a program's user interface can be as easy as dragging
controls onto forms, and then modifying the control's properties.
13.1.5 Micro Focus NetExpress
Micro Focus NetExpress is an integrated development environment for creating
distributed applications using existing business logic. NetExpress combines
Micro Focus Object COBOL(tm) technology with a specialized set of tools for
developing applications targeted at PC-workstations, distributed computing
environments and the Internet/Intranet.
13.2 Sinc Inc. products
13.2.1 FlexGen 4GL Rapid Application Development Environment
A repository-based, data dictionary-driven tool set and code generator. It
supports and generates code for RM/COBOL, AcuCOBOL, Micro Focus COBOL,
Realia (DOS Only), mbp (DOS Only) and runs and deploys under DOS, Windows,
Windows 95, NT, many flavors of UNIX, VAX/VMS and Open VMS.
13.2.2 Legacy Liberator COBOL Migration Toolset
For rehosting proprietary COBOLs, converting them to open systems, AcuCOBOL,
RM/COBOL or MF COBOL. User interfaces can be converted to FlexGen user
interfaces including the ability to upgrade them to GUI.
13.2.3 Easy Query
A point-and-shoot report writer and query tool.
13.2.4 ODBC Access Tools
Allows Windows ODBC-enabled applications to access COBOL data.
13.3 Misc. tools
13.3.1 Flexus WinPrint
COBOL WinPrint allows the COBOL programmer to make ANSI standard COBOL CALL
USING statements to completely control and communicate with the Windows
Print Manager. Forms may be designed interactively with the Forms Editor to
include bitmaps, special fonts, colors and many other modern features. These
reports may be viewed on the screen prior to printing or sent directly to
the Print Manager.

14. Other sources of information.
14.1 CompuServe
Micro Focus runs a COBOL Forum on CompuServe. Just
GO MICROFOCUS
to get to it.
CA also has a Forum. To get to this, use
GO CAIDEV
Liant has a Forum too, to support the RM/COBOL and Relativity(TM) family of
products. To access it, use
GO LIANT
14.2 Bix
There is a COBOL forum on Bix. Don Nelson is the moderator.
14.3 Micro Focus Faxback
In Palo Alto, Micro Focus runs a system for obtaining certain technical
information by fax. You need a tone-dial 'phone to use it.
The number is (415) 496 7170.
14.4 Micro Focus WWW server
Micro Focus has a WWW server covering many COBOL issues. The
URL is http://www.mfltd.co.uk/

14.5 CA WWW server
CA also has a WWW server. It's URL is http://www.cai.com/
14.6 Liant and Ryan McFarland WWW server
Liant has a WWW server at http://lsc.liant.com/. This server also hosts the
RM WWW site at http://lsc.liant.com/rm/.
14.7 The AcuCOBOL WWW server
This is at http://www.acucobol.com/.
14.8 The COBOL Foundation
Dave McFarland, formerly of Ryan McFarland, has begun an organization aimed
at promoting COBOL and providing information to and about the COBOL
community. Members (including RM, MF, and IBM) pay yearly dues and in return
are included in the Foundation's promotion efforts, literature, directories,
etc. and have their company and product information posted on the
Foundation's web server. The URL for the server is
http://www.cobol.org/

14.9 The IBM COBOL products WWW server
IBM has enhanced the COBOL you currently use with powerful features to
increase development productivity, simplify the maintenance of your legacy
code, and provide seamless portability from your host to your workstation.
Whether you're maintaining or reengineering legacy code or creating new
object-oriented client/server applications, IBM's COBOL family offers you
the year 2000 ready application development environment designed to do the
job right.
IBM COBOL provides a complete offering of compatible, cross platform, cross
product compilers which support OS/2(r), OS/390(tm), MVS(tm), VM,
VSE/ESA(tm), AS/400(r), AIX(r), and Windows(r). IBM gives you the tools you
need to tackle your COBOL year 2000 challenge while leveraging your existing
applications. IBM COBOL also provides the tools you need to amplify your
program development, enabling you to position your enterprise to take
advantage of tomorrow's technologies.
See http://www.software.ibm.com/ad/cobol/

14.10 The Flexus WWW server
Contains all sorts of information, including a copy of the COBOL 650
compiler. It's at http://www.flexus.com/
14.11 COBOL User Groups
There are a large number of Micro Focus User Groups. Rather than reproduce
the list here and have it constantly out of date, it can be found at
http://pita.microfocus.com/UserGroup_PC/
The list and the web pages are maintained by Debbie Vincent <
tom··.@a··.com>.

15. Information required for the FAQ.
Corrections and additions to existing material are always welcome. I'd like
to add a section of reviews of different COBOL books. If I am sent any
reviews I will collate them and add these to the FAQ. More information on
mainframe COBOL products would be useful.
A section covering COBOL programming could be worthwhile.
Note: I still have a "folder full" of comments sent to the last owner of
this FAQ that have yet to be applied. It is my intent to get them verified
and applied as soon as possible.

16. Contributors to the FAQ.
The following people have contributed to the creation of this FAQ :
James Fidell
Don Nelson
Clarence A Booth, Jr.
Kelly Brown ???
Gary Henry
Stan Cox
Gary Crook
Robert D. Davis
Uwe Baemayr
Bernd Backhaus
Wayne Gallant
Jonathan Beit-Aharon
Stefano Priola
Todd G. Beets
Joachim Blome <100··.@com··e.com>
John M.
Kathleen McSpurren
Thomas Koehler
Al Sinclair
Mike Wilson
Erkki Ruohtula
Ralf Laemmel
Tom Willard
Peter Mikalajunas
Laurent Sabarthez
Norman Hull
Juergen Linkens
Clinton G. Downing
Ryan Stryker
Chuck McComas
Leif Svalgaard
Bob Wolfe
Dan Clarke

17. What about the Y2K (Millenium) Issue?
* Yes, the year 2000 IS a leap year
* Yes, the millenium really starts on January 1, 2001 - but the software
"bug" refers to January 1, 2000 (and several other dates)
17.1 Where can I get information about the Y2K problem?
The Year 2000 Information Center home page on the World Wide Web is at
http://www.year2000.com.
The Information Center has a countdown clock, articles on various aspects of
the problem, vendor information, this FAQ, and links to related information.
There is an Internet mailing list operated by Peter de Jager for discussions
of year 2000 computer problems. The list has over 1200 members, and gets an
average of about 25 messages per business day. This is a moderated mailing
list managed by a paid administrator and fully supported by its members on a
"shareware" basis. Each member is asked to pay a subscription fee of US $50
yearly. (You may contribute more if you wish.)
New subscribers get a 30-day free trial.
To subscribe, select the "Year 2000 Announcement List" link from the Year
2000 Information Center home page at http://www.year2000.com. On the
subscription form, select the Yes adio button for the Discussion List. You
can also subscribe by sending e-mail to 2.··.@tor··p.net with
SUBSCRIBE
in the subject line of the message. Subscriptions are processed manually, so
please be patient. The list can optionally be received in digest form
instead of individual messages. Invoices and receipts are available if
needed. Details will be sent when you subscribe.
The Year 2000 Forum on CompuServe has discussions of all year 2000 issues,
and a collection of files, including this FAQ. There are over 1000 members.
To reach the forum, GO YEAR2000.
The Usenet newsgroup comp.software.year-2000 is dedicated to discussions of
year 2000 computer issues.
The current version of this Year 2000 FAQ is available from several web
sites, an FTP site, and on CompuServe. It is in ASCII text form at all these
sites.
On the Year 2000 Information Center home page at
http://www.year2000.com,
select the "Year 2000 Archive" link. The FAQ is the last item listed on the
Archive page

18. What can/should I post in the COBOL newsgroups?
Both comp.lang.cobol and alt.cobol are UN-moderated newsgroups. Therefore,
you can post whatever you want there. However, there are some guidelines
that will help you get the most out of both your viewing and postings at
these sites.
* Comp.lang.cobol is the preferred site to use - especially for technical
issues related to COBOL.
* Although threads do stray from the topics, the more targeted your inquiry
is - and the more closely it relates to COBOL, the more likely you are to
receive a useful and prompt response. (If you know that you are leaving the
current subject, consider changing the subject line in your post.)
* When asking about a specific structure, error message, or situation, it is
always best to specify both the compiler that you are using and the
operating system where you are working. (What you may think is a general
COBOL question may actually be very specific to your current environment.)
Note: For those who are interested, the "charter" for the comp.lang.cobol
newsgroup can be found at:
ftp://ftp.uu.net/usenet/news.announce.newgroups/comp/comp.lang.cobol
18.1 Can I get help with homework via the newsgroups?
Yes, you can get help with your homework via these newsgroups. HOWEVER, that
does mean that you will receive help - you will NOT find many participants
who will be very happy if you ask them to do your homework FOR YOU. Some
hints that you should consider when drafting your post for assistance with
homework include:
* Make it clear from the beginning that you are asking for homework help.
(Most of the newsgroup participants are very good at sniffing out those who
try and pose homework questions as "business need" questions - and they are
not very polite in replying to such questions).
* Make certain that you specify what compiler and operating system your
homework is targeted at. Solutions may vary significantly based on this.
(You might also want to include what text book you are using.)
* The more information that you can give that demonstrates that you really
have tried to solve the problem yourself (using your text book, class
material/presentations, lab assistance, etc), the more likely it is that you
will get useful and friendly responses. If you let us know what you have
found on your own and why you are still uncertain or confused, you will
usually get helpful responses; if it looks like you are asking us questions
without trying to solve it yourself, you are likely to get very pointed
replies.
18.2 Can I post job openings in the newsgroups and if so what should I
include?
These newsgroups are an excellent place for posting job openings. Some
participants (those with jobs) often wish that less of the bandwidth was
spent on job postings, but, for those who are looking for
positions/contracts, these postings are quite useful. There are, however,
some guidelines that you should follow when posting positions - unless you
like getting abusive and non-responsive replies to your postings.
* Always, ALWAYS, include rates, a range of rates, or your best information
on what rates are available. Phrases like "based on experience" and
"competitive" are bound to receive replies questioning your motives. The
assumption is that ALL such posts are "trolling" for resumes or rates and
not serious job searches.
* Try to give the best summary of job location and desired expertise in the
subject line of your posting. This will assist you in attracting readers
that are actually potentially interested in your openings.
* The newsgroups are international in nature, but are dominated by
Americans. If you are posting a position outside the US, please make it
clear whether foreigners are or are not welcome to apply - and if so what
visas and other paperwork is required If you are posting for a job with
specific citizenship requirements, please make that clear from the start.
* In general, the more information that you provide in your postings, the
better the match will be from those who reply. If, however, you are
"attaching" a job description, please make certain that you make it clear
what type of document-reader is required to process it AND make certain that
you have virus scanned the document before you post it.

Appendix A. Changes in recent revisions
This appendix documents the major changes that were made to create the
various (recent) versions of this document.
Appendix A.1 - Changes to create Version 2.0
Huge numbers of changes! Version numbering jumped from 1.xxx to 2.0 to
reflect this.
FAQ availability details.
Added section on Commercial COBOL Products.
Removed 'what happened to Realia?' section.
Removed references to Wang, as I can find no information on any Wang COBOL
Products.
Checked all URLs, and updated/added as appropriate.
Removed reference to IBM 'COBOL Products WWW site'.
Added entries in 'GUI Tools' section for Micro Focus Dialog System and Net
Express, Flexus COBOL spII, and CA-Visual Realia.
Removed ADS/Online from 'Code Generators' section as it's not, apparently.
Also noted that Cullinet have been acquired by CA, who now sell the Telon
product.
Appendix A.2 - Changes to create Version 2.0x
* Significant reformatting
* Updated OO COBOL Section
* Add URL for IBM COBOL Web site
* Added information on "COBOL for Dummies"
* Added initial Y2K section
* Added information on using the newsgroups
* Added information on PCYACC
```

#### ↳ Re: COBOL FAQ

- **From:** "jim rivera" <ua-author-902354@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-32fccb26f8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6dc0ja$8pi@dfw-ixnews6.ix.netcom.com>`
- **References:** `<6dc0ja$8pi@dfw-ixnews6.ix.netcom.com>`

```

William M. Klein wrote:
›
› COBOL FAQ

It might cut down on the newsgroup traffic if this were posted
weekly...

JR
```

##### ↳ ↳ Re: COBOL FAQ

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-32fccb26f8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-32fccb26f8-p2@usenetarchives.gap>`
- **References:** `<6dc0ja$8pi@dfw-ixnews6.ix.netcom.com> <gap-32fccb26f8-p2@usenetarchives.gap>`

```


Jim Rivera wrote in message <6dclrp$j.··.@bgt··t.net>...
› William M. Klein wrote:
›› 
…[5 more quoted lines elided]…
› JR

My current plan is to post it twice a month. I was actually afraid that I
would get complaints about doing it that often (given how big it is). I do
plan on putting something out weekly with the pointer to the HTML web site.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
