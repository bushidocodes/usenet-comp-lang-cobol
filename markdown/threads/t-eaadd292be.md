[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# using fujitsu power cobol and crystal reports

_11 messages · 4 participants · 2003-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### using fujitsu power cobol and crystal reports

- **From:** "Hopeful" <me@mynet.net>
- **Date:** 2003-10-04T13:10:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za>`

```
Hi

CRAXDDRT is the crystal reports runtime library but I'm confused as to how
to access or use the library so I've attempted to follow the vb syntax and
code accordingly.

Any ideas as to what the equivilant power cobol syntax is for the following
vb syntax

Dim m_Application As New CRAXDDRT.Application
Dim m_Report As CRAXDDRT.Report

I've managed to put the viewer control and the embedded designer control
onto the form and can change various properties but don't seem to be able to
setup the ReportSource property as it seems to rely on the above m_Report
object being defined and setup.

CRViewer1.ReportSource = m_Report

Please assist if possible.

Nik



---
Outgoing mail is certified Virus Free.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.522 / Virus Database: 320 - Release Date: 03/09/29
```

#### ↳ Re: using fujitsu power cobol and crystal reports

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2003-10-07T02:22:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0310070122.4e29c516@posting.google.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za>`

```
"Hopeful" <me@mynet.net> wrote in message news:<rOqdnUIiTLkrN-OiU-KYuA@is.co.za>...
> Hi
> 
…[26 more quoted lines elided]…
> Version: 6.0.522 / Virus Database: 320 - Release Date: 03/09/29

Hi,
Any special reason for using Crystal thru the COM interface ? 
You stated that you're able to put the "embedded designer control onto
the form". Are you designing the report inside your program ?

I'm asking this because if you have a pre-formated report, the normal
path would be to embed the ActiveX control onto your form and then
update the "ReportFileName" property, and probably, a few others like
"SelectionFormula" and "Connect".

regards,
Paulo Vieira
```

##### ↳ ↳ Re: using fujitsu power cobol and crystal reports

- **From:** "Hopeful" <me@mynet.net>
- **Date:** 2003-10-07T13:39:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfydnWU18Zh-OB-iU-KYgw@is.co.za>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com>`

```
> Any special reason for using Crystal thru the COM interface ?
> You stated that you're able to put the "embedded designer control onto
…[5 more quoted lines elided]…
> "SelectionFormula" and "Connect".

I'm using CR 9 and the CRViewer ActiveX control doesn't seem to have the
above mentioned
properties so I've been forced to go this route unfortunately. (unless i'm
really a sucker for punishment)

In the interim I have made some progress in that I've managed to create the
COM objects as follows.

01 WK                    PIC X(1024)
01 CApplication  OBJECT REFERENCE COM.
01 CReport         OBJECT REFERENCE COM.
01 CReportName    PIC X(1024)

.....

Move "CrystalRuntimeApplication" TO WK.
INVOKE COM "CREATE-OBJECT" USING WK RETURNING CApplication.
Move "CrystalRuntimeReport" TO WK.
INVOKE COM "CREATE-OBJECT" USING WK RETURNING CReport.

Move "MyReport.rpt" TO CReportName.
INVOKE CApplication "OpenReport" USING CReportName RETURNING CReport.

.....

The above compiles and runs error free but I still need to assign the
CReport to the CRViewer9 control.
I am battling to figure our how to do the powercobol equivilent of the
following vb syntax.

CRDesignerCtrl1.ReportObject = m_Report   (m_Report being the equivilent of
my CReport)

CRViewer1.ReportSource = m_Report

CRViewer1.ViewReport

The c++ syntax has a similar assignment

m_Report = m_Application->OpenReport(ReportPath, dummy);
m_Viewer.SetReportSource(m_Report);

but I can't seem to figure out how to assign CReport to ReportSource as the
compiler regards the following as illegal.

MOVE CReport TO "ReportSource" OF CRViewer91.


Nik



---
Outgoing mail is certified Virus Free.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.522 / Virus Database: 320 - Release Date: 03/09/29
```

###### ↳ ↳ ↳ Re: using fujitsu power cobol and crystal reports

- **From:** "Hopeful" <me@mynet.net>
- **Date:** 2003-10-07T16:25:26+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0JidnXiUTviWUB-iXTWJhg@is.co.za>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com> <UfydnWU18Zh-OB-iU-KYgw@is.co.za>`

```
I've managed to figure it out....
Procedure below to save someone a weeks worth of frustration.

01 WK                  PIC X(1024)
01 CApplication     OBJECT REFERENCE COM.
01 CReport            OBJECT REFERENCE COM.
01 CobReport        OBJECT REFERENCE POW-COBJECT.
01 CReportName   PIC X(1024)
 .....

 Move "CrystalRuntimeApplication" TO WK.
INVOKE COM "CREATE-OBJECT" USING WK RETURNING CApplication.
Move "CrystalRuntimeReport" TO WK.
INVOKE COM "CREATE-OBJECT" USING WK RETURNING CReport.

Move "MyReport.rpt" TO CReportName.
INVOKE CApplication "OpenReport" USING CReportName RETURNING CReport.

CALL "POWERCONVFROMCOM" USING CReport RETURNING CobReport.

MOVE CobReport TO "ReportSource" OF CRViewer91.

INVOKE CRViewer91 "ViewReport"
 .....

The key was to convert the COM object back to a 'PowerCobol' one.

Nik


---
Outgoing mail is certified Virus Free.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.522 / Virus Database: 320 - Release Date: 03/09/29
```

###### ↳ ↳ ↳ Re: using fujitsu power cobol and crystal reports

_(reply depth: 4)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-10-09T14:15:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<donaov4840rtmn4tr6dif2jifu1rv22b7v@4ax.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com> <UfydnWU18Zh-OB-iU-KYgw@is.co.za> <0JidnXiUTviWUB-iXTWJhg@is.co.za>`

```
On Tue, 7 Oct 2003 16:25:26 +0200, "Hopeful" <me@mynet.net> wrote:
snip
>CALL "POWERCONVFROMCOM" USING CReport RETURNING CobReport.

Nik,

would you be so kind as to point me out on which manual you found this
info? I can't find it, and whatever part of the manual this is
referred may help me solve another prob I have.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: using fujitsu power cobol and crystal reports

_(reply depth: 5)_

- **From:** "Hopeful" <me@mynet.net>
- **Date:** 2003-10-10T15:01:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ht-dnZks8cMTMBuiU-KYhw@is.co.za>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com> <UfydnWU18Zh-OB-iU-KYgw@is.co.za> <0JidnXiUTviWUB-iXTWJhg@is.co.za> <donaov4840rtmn4tr6dif2jifu1rv22b7v@4ax.com>`

```
> would you be so kind as to point me out on which manual you found this
> info? I can't find it, and whatever part of the manual this is
> referred may help me solve another prob I have.

There are no references that I could find using POWERCONVFROMCOM other than
in the ADO examples provided with Fujitsu but I did find the POWERCONVTOCOM
documented in.....

POWERCOBOL Users Guide
Chaper 9 PowerCOBOL Programming Techniques Pg 243

Receiving Objects Using the COBOL *COM CLASS

Trust this helps...if not post the query and maybe I can assist.


---
Outgoing mail is certified Virus Free.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.525 / Virus Database: 322 - Release Date: 03/10/09
```

###### ↳ ↳ ↳ Re: using fujitsu power cobol and crystal reports

_(reply depth: 6)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-10-10T15:22:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odfdov4eoeat403f3laaq37nmlip0qcbfq@4ax.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com> <UfydnWU18Zh-OB-iU-KYgw@is.co.za> <0JidnXiUTviWUB-iXTWJhg@is.co.za> <donaov4840rtmn4tr6dif2jifu1rv22b7v@4ax.com> <ht-dnZks8cMTMBuiU-KYhw@is.co.za>`

```
On Fri, 10 Oct 2003 15:01:00 +0200, "Hopeful" <me@mynet.net> wrote:

>> would you be so kind as to point me out on which manual you found this
>> info? I can't find it, and whatever part of the manual this is
…[11 more quoted lines elided]…
>Trust this helps...if not post the query and maybe I can assist.
Thanks for that.

I was hoping that you had found how/when to use these type of
cunctions.

I think I am going to email Fujitsu and ask for the manual of those
functions.


My particular query, and I have not yet spent to much time with it, is
that I have a OCX that returns a address to a memory area on one of
it's properties. This area needs then to be accessed as a PIC X(???)
to be saved to a file.

At a second stage the info will also be read from the file, placed on
a PIC X(???) and then its memory location must be placed on the same
control property so that it is availble to the control for further
processing.

so my issue is really how to do the following.

cobol_variable memory location = control->property
and
control->property = cobol_variable memory location


As I said I haven't spent to much time on this yet, but knowing
PowerCOBOL as I do it probably won't be that straightforward to find.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: using fujitsu power cobol and crystal reports

_(reply depth: 7)_

- **From:** "Hopeful" <me@mynet.net>
- **Date:** 2003-10-13T17:30:09+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vt6cnUFBb7uWWBeiXTWJlg@is.co.za>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <b5b8d7c7.0310070122.4e29c516@posting.google.com> <UfydnWU18Zh-OB-iU-KYgw@is.co.za> <0JidnXiUTviWUB-iXTWJhg@is.co.za> <donaov4840rtmn4tr6dif2jifu1rv22b7v@4ax.com> <ht-dnZks8cMTMBuiU-KYhw@is.co.za> <odfdov4eoeat403f3laaq37nmlip0qcbfq@4ax.com>`

```
> so my issue is really how to do the following.
>
…[6 more quoted lines elided]…
> PowerCOBOL as I do it probably won't be that straightforward to find.

Why does the term 'by reference' ring a bell....



---
Outgoing mail is certified Virus Free.
Checked by AVG anti-virus system (http://www.grisoft.com).
Version: 6.0.525 / Virus Database: 322 - Release Date: 03/10/09
```

#### ↳ Re: using fujitsu power cobol and crystal reports

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-10-13T18:56:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3451793.1066085761@dbforums.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za>`

```

Hi Frederico



First, a little correction on what Nik wrote...the name of the correct
function is "POWERCONVTOCOM" not "POWERCOMFROMCOM"...



Second, if you have a variable that points to a memory location you need
to declare this variable as POINTER, then use the FUNCTION ADDRESS
(variable_name) to obtain the correct variable assignment.



Hope in this help



Gianni
```

##### ↳ ↳ Re: using fujitsu power cobol and crystal reports

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-10-14T10:34:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q9gnov03idkvobk7mvpvok5bmi570potqf@4ax.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za> <3451793.1066085761@dbforums.com>`

```
On Mon, 13 Oct 2003 18:56:01 -0400, gmspano <member9303@dbforums.com>
wrote:

>
>Hi Frederico
…[14 more quoted lines elided]…
>Hope in this help

Not really.
Bear in mind that it is the CONTROL PROPERTY that is a pointer. You
can not change the definition of these.

Function address will retrieve the address of a variable only, it will
not set a variable address (other than a pointer) to another address.

So though I could theoretically do the following
     move function addr(imagem) to "SaveBufferHandle" OF im1.
(This does not work either - error from FJ. Property or method for IM1
not found)

I can not do the reverse as it is invalid.
     move "SaveBufferHandle" OF im1 to function addr(imagem).


Thanks anyway.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: using fujitsu power cobol and crystal reports

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-10-15T09:15:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3483927.1066223743@dbforums.com>`
- **References:** `<rOqdnUIiTLkrN-OiU-KYuA@is.co.za>`

```

Hi Frederico



Could you send me the ocx to look into it?



Use this email: softline2000@tin.it



Gianni
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
