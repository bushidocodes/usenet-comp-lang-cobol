[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VB 6 call to Fujitsu COBOL DLL problem

_3 messages · 2 participants · 2002-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### VB 6 call to Fujitsu COBOL DLL problem

- **From:** corek@nospam.hotmail.com
- **Date:** 2002-07-02T13:38:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rb73iusdd01jef9mea2o1k2roqcatmjq13@4ax.com>`

```
I have followed the instructions in the Fujitsu handbook, using 
their Programming Staff, for Hicobol,  but when I try and link to it
from the VB
application I get 
Run-Time error '453'

Can't find DLL entry point Hicobol in
and then the Path.

Is it me or VB6?

Cobol
000010 IDENTIFICATION DIVISION.
000020  PROGRAM-ID. HICOBOL.
000030 ENVIRONMENT DIVISION.
000040 DATA DIVISION.
000041 WORKING-STORAGE SECTION.
000050 LINKAGE SECTION.
000070*
000080  01  vbinteger           PIC S9(4) COMP-5.
000100  01  vbstring            PIC X(16).
000120 PROCEDURE DIVISION WITH STDCALL LINKAGE
000160                    USING vbinteger, vbstring.
000170      MOVE 101   TO vbinteger.
000180      MOVE "Hello from COBOL"  to vbstring.
001560
001570      EXIT PROGRAM.
001580 


VB Code
Private Declare Sub Hicobol Lib
"C:\COBOL\fsc\PCOBOL32\samples\Hicobol\HICOBOL.DLL" (vbinteger As
Integer, ByVal vbstring As String)
Private Declare Sub JMPCINT2 Lib "C:\cobol\fsc\pcobol32\F3BIPRCT.DLL"
()
Private Declare Sub JMPCINT3 Lib "C:\cobol\fsc\pcobol32\F3BIPRCT.DLL"
()

Private Sub cmdCbl_Click()
Dim vbinteger As Integer
Dim vbstring As String * 16
Call JMPCINT2
Call Hicobol(vbinteger, vbstring)
txtText.Text = vbstring
Call JMPCINT3
End Sub

Private Sub cmdReset_Click()
txtText.Text = "Text set to Visual Basic"
End Sub
```

#### ↳ Re: VB 6 call to Fujitsu COBOL DLL problem

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-07-02T15:57:33+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afsbd9$oda$1@mailnews.kub.nl>`
- **References:** `<rb73iusdd01jef9mea2o1k2roqcatmjq13@4ax.com>`

```
Maybe an error in the call from vb:

Private Declare Sub Hicobol Lib
 "C:\COBOL\fsc\PCOBOL32\samples\Hicobol\HICOBOL.DLL" (vbinteger As
Integer, ByVal vbstring As String)

should be:

Private Declare Sub Hicobol Lib
 "C:\COBOL\fsc\PCOBOL32\samples\Hicobol\HICOBOL.DLL" (ByVal vbinteger As
Integer, ByVal vbstring As String)

you might have forgotten the ByVal of vbinteger in the Hicobol.lib declaration?

Kind regards,

Rik Hendriks

<corek@nospam.hotmail.com> wrote in message news:rb73iusdd01jef9mea2o1k2roqcatmjq13@4ax.com...
> I have followed the instructions in the Fujitsu handbook, using 
> their Programming Staff, for Hicobol,  but when I try and link to it
…[48 more quoted lines elided]…
> End Sub
```

##### ↳ ↳ Re: VB 6 call to Fujitsu COBOL DLL problem

- **From:** corek@nospam.hotmail.com
- **Date:** 2002-07-02T23:22:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q94iuk6f7o0icvglna8k9310qm7bkifgn@4ax.com>`
- **References:** `<rb73iusdd01jef9mea2o1k2roqcatmjq13@4ax.com> <afsbd9$oda$1@mailnews.kub.nl>`

```
On Tue, 2 Jul 2002 15:57:33 +0200, "R. Hendriks" <R.Hendriks_1@kub.nl>
wrote:

Turned out that the VB was wrong
The
      Call Hicobol(vbinteger, vbstring)
should have been
     Call HICOBOL (vbinteger, vbstring)

i.e. All capitals (bloody stupid thing)

>Maybe an error in the call from vb:
>
…[67 more quoted lines elided]…
>> End Sub
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
