[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CA-Realia Workbench II Debugger

_4 messages · 4 participants · 1996-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### CA-Realia Workbench II Debugger

- **From:** "nor..." <ua-author-17071493@usenetarchives.gap>
- **Date:** 1996-09-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32389a79.67264780@gateway>`

```

Am I the only grouchy one out here who desperatly misses the RealDbug
option in the Realia 5.0 compiler supplied with Workbench?

I find the Workbench one unacceptable:
You cant debug under windows unless you compiled it under windows
You cant debug without the cvx files, which are HUGE compared to
the sym files
Cant use the workbench debugger at all if you need to start data
engines, map drives, or other things before you fire up your

application (cant run a bat and debug)

Perhaps it is because we have such huge applications, 2 to 300
subroutines in some cases, but I dont find the WB much help. In a
dos box i can launch a compile and relink of the entire system and go
to lunch. The WB will not even let me select that many programs, let
alone compile them. Therefore, I use the WB to work with small
subsets of programs, but revert to batch for large re-compiles etc.

But, still no debugger! The compiler (in one form or another) has been
out for over a year now, and the latest release even didn't even have
the windows debugger CARCWIND in it anymore. The WB debugger,
to the extent it works at all, has been known to keep on running after
the application abended out from under it! The only way out is
reboot.

Still running 4.2 - just so I can debug!

_______________________________
John Andersen
NORCOM
http://www.alaska.net/â€¾norcom
```

#### ↳ Re: CA-Realia Workbench II Debugger

- **From:** "mike..." <ua-author-13596@usenetarchives.gap>
- **Date:** 1996-09-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e8f68f4dc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32389a79.67264780@gateway>`
- **References:** `<32389a79.67264780@gateway>`

```

On Thu, 12 Sep 1996 23:40:44 GMT, nor··.@ala··a.net (John S. Andersen)
wrote:

› Am I the only grouchy one out here who desperatly misses the RealDbug
› option in the Realia 5.0 compiler supplied with Workbench?
…[29 more quoted lines elided]…
› http://www.alaska.net/â€¾norcom

You have missed some of the other finer points to the CA-Realia
Workbench II Debugger such as the inability to debug a DOS extended
application under DOS without windows and the inability of the
debugger to run under Windows NT.
```

##### ↳ ↳ Re: CA-Realia Workbench II Debugger

- **From:** "mri..." <ua-author-8217666@usenetarchives.gap>
- **Date:** 1996-09-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e8f68f4dc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0e8f68f4dc-p2@usenetarchives.gap>`
- **References:** `<32389a79.67264780@gateway> <gap-0e8f68f4dc-p2@usenetarchives.gap>`

```

mik··.@ix.··m.com (Michael Anderson) wrote:

› You have missed some of the other finer points to the CA-Realia
› Workbench II Debugger such as the inability to debug a DOS extended
› application under DOS without windows and the inability of the
› debugger to run under Windows NT.

Does it not even work if you run it with FORCEDOS? Thats what you have
to do to get the 4.2 debugger to work under DOS.
```

#### ↳ Re: CA-Realia Workbench II Debugger

- **From:** "god..." <ua-author-3198336@usenetarchives.gap>
- **Date:** 1996-09-22T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e8f68f4dc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32389a79.67264780@gateway>`
- **References:** `<32389a79.67264780@gateway>`

```

nor··.@ala··a.net (John S. Andersen) wrote:

› Am I the only grouchy one out here who desperatly misses the RealDbug
› option in the Realia 5.0 compiler supplied with Workbench?
 
› I find the Workbench one unacceptable:
›    You cant debug under windows unless you compiled it under windows
…[3 more quoted lines elided]…
›         engines, map drives, or other things before you fire up your
 
›         application (cant run a bat and debug)
 
› Perhaps it is because we have such huge applications, 2 to 300
› subroutines in some cases, but I dont find the WB much help.  In a
…[3 more quoted lines elided]…
› subsets of programs, but revert to batch for large re-compiles etc.
 
› But, still no debugger! The compiler (in one form or another) has been
› out for over a year now, and the latest release even didn't even have
…[3 more quoted lines elided]…
› reboot.
 
› Still running 4.2 - just so I can debug! 
 
› _______________________________
› John Andersen
› NORCOM
› http://www.alaska.net/~norcom
John,

Your posting was brought to my attention by Charles Godwin, a fellow
employee at Computer Associates. On behalf of CA I would like to
address your concerns. I can understand that you may miss the
DOS-based REALDBUG debugger, however, with a little familiarization
I believe that most users will find the new Windows-hosted debugger
to be a very powerful and intuitive tool for debugging COBOL
programs. Also please bear in mind that our clients, and the
industry as a whole is moving towards Windows-based environments.
In fact, demand for the Windows95 version of the Workbench was so
strong that we had to turn down many beta requests.

In this reply I will attempt to respond to each point that you have
raised, however if you require further information please feel free
to contact our CA-REALIA II Workbench Support Hotline at (919)
677-2890 from 8AM-6PM EST. Our support people will be happy to help
you, and we really do need to get specific information about the
problems you've experienced.

Please find below your statements and our responses to them:

1. You can't debug under windows unless you compiled it under
windows.

You do not need to compile under Windows in order to use
the debugger. If you wish to continue to write batch files to do
your compilation you can find information on the command line
interface in the COBOL reference manual provided with the product.

You can continue to invoke the compiler from the command line or via
batch files and then debug under the workbench, however we feel that
a more effective and efficient way to do massive compiles is to
compiles is to take advantage of the "application" definition
through the Workbench. Using the application interface allows you
to dynamically build a list of programs that you wish to submit in a
"batch compile and link". From a point and click dialog box you can
select one, several, or many programs to be compiled and the
Workbench will dynamically build a compile script, submit for
compile and show the results of each compilation(again in an easy to
use dialog box), allowing you to easily view and correct errors.
Most users I have spoken to find this to be one of their favorite
enhancements, as it does not force you into writing batch files for
each set of programs to be compiled. It also has an
error-highlighting feature in the editor to expedite the correction
of any compilation errors.


2. You can't debug without the .cvx files, which are HUGE compared
to the sym files.

CVX files give you a whole lot more capabilities than did REALDBUG
-- specifically the extensive analysis capabilities which allow you
to view program structure through a GUI interface, as well as
effectively simulate program execution and trace logic flow
throughout your program. You can also now suppress the generation
of the .lst file as the .cvx file contains the entire listing of the
program.


3. You can't use the workbench debugger at all if you need to start
data engines, map drives, or other things before you fire up your
application (cant run a .bat and debug).

The "additional environmentals" option was added into Workbench 2.0
in order to enable you to do things such as set environmentals that
you would typically have to do previously by manually running a .bat
file. This enables you to associate these specifically to a program
or application, and have them set automatically whenever you run or
debug a program under Workbench. Once the association is in place
you no longer have to remember to invoke a bat file prior to running
or debugging a program. In addition release 2.0 of the Workbench
allows you to run and/or debug a batch file from within the
Workbench. Again, if you need further details please contact our
technical support hotline.


4. You state "Perhaps it is because we have such huge applications,
2 to 300 subroutines in some cases, but I don't find the WB much
help. In a DOS box I can launch a compile and relink of the entire
system and go to lunch. The WB will not even let me select that
many programs, let alone compile them. Therefore, I use the WB to
work with small subsets of programs, but revert to batch for large
re-compiles etc."

I believe that if you review the application concept you will see
that you can use this to BUILD complete applications (which do not
require opening each file) -- and with much better feedback than
using a batch file.

Yes, the Workbench will not let you select/open hundreds of files at
once, but that is not needed for an application defined BUILD. The
workbench builds a complete compile and link list based on your
definition of an application. We have developers at Computer
Associates who regularly compile several hundred programs via the
Workbench and I have spoken to a user in the UK who has 900+
programs defined in an application. Again, I would suggest that you
contact technical support with details so that we can investigate
your problem and help find a solution.

5. You also state "But, still no debugger! The compiler (in one
form or another) has been out for over a year now, and the latest
release even didn't even have the windows debugger CARCWIND in it
anymore. The WB debugger, to the extent it works at all, has been
known to keep on running after the application abended out from
under it! The only way out is reboot.

There is some truth in part of this statement but I believe it needs
clarification.

First, the compiler has not been out for over a year now. It only
went GA (via our workbench and Plus products) in July.

Secondly, there is not a debugger for windows included in the
workbench since workbench was designed primarily for the debugging
of character-based applications. Computer Associates offers
CA-Visual Realia for developing Windows applications, however due to
the demands of our clients who want to develop Windows standalone
executables we have committed to delivering a Windows standalone
debugger by the end of the year, which you will be able to use with
Release 2.0 of the Workbench or CA-Realia COBOL Plus. In addition
release 3.0 of the workbench (our 32-bit product which is due to
enter beta testing next month) will allow the debugging of either
text-based or GUI applications via a common debugger.

Thirdly, we have many, many clients successfully using the debugger
and I am not aware of the problems that you state. Have you
reported this to technical support? If so I would like to know what
the incident numbers are as I am not aware of any open issues such
as you describe, and I personally review all open issues regularly.
Please let me assure you that if we were aware of such problems we
would not have released the product, and if such problems were
reported they would be corrected as soon as possible.

As always if you have enhancement suggestions we will be glad to
consider them for a future release and if you have any problems we
will endeavor to correct them as soon as possible, however I would
also suggest that you first contact our technical support line as
they may be able to explain how to take advantage of the many new
features in this release to accomplish what you want to do and
increase your productivity levels with the product.

Sincerely,

Siegfried Forster
Client Base Owner
Computer Associates
FOR··.@mai··i.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
