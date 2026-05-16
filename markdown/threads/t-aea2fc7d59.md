[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCobol MSChart

_4 messages · 2 participants · 2004-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### AcuCobol MSChart

- **From:** martin_xxxxx@hotmail.com (Martje)
- **Date:** 2004-11-23T04:54:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34c4918b.0411230454.d3b8497@posting.google.com>`

```
Hi,

I want to use MS Chart within my cobol program, but don't know where to start.
Who've got an example program for me, so i can learn more about this.

Thanx
```

#### ↳ Re: AcuCobol MSChart

- **From:** "Cheesle" <cheesle@NoSpamPlease.online.no>
- **Date:** 2004-11-23T16:24:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICIod.9278$rh1.236638@news2.e.nsc.no>`
- **References:** `<34c4918b.0411230454.d3b8497@posting.google.com>`

```
> I want to use MS Chart within my cobol program, but don't know where to
start.
> Who've got an example program for me, so i can learn more about this.

It is pretty straight forward.

Provided you have your definition file readily at hand (mschart.def) and a
valid license;

       IDENTIFICATION               DIVISION.
       PROGRAM-ID.                  Chart1.
       AUTHOR.                      Cheesle.
       REMARKS.

       ENVIRONMENT                  DIVISION.
       CONFIGURATION                SECTION.
       SPECIAL-NAMES.
    COPY "MSCHART.DEF".
                .
       WORKING-STORAGE              SECTION.
       77  CNTL-FONT                USAGE HANDLE OF FONT SMALL-FONT.

       SCREEN                       SECTION.

       01 CHART-FORM.
           03 CheeseChart           MSCHART
              COL                   10
              LINE                  5
              LINES                 30
              SIZE                  40
              Visible               0.

       PROCEDURE DIVISION.
       ACU-MAIN-LOGIC.
           DISPLAY STANDARD         GRAPHICAL WINDOW
                   LINES            30
                   SIZE             50
                   BACKGROUND-LOW
                   CONTROL FONT     CNTL-FONT
                   TITLE            "Pie Chart demo".
           DISPLAY CHART-FORM.
           MODIFY  CheeseChart
                   DataGrid::RowLabelCount = 1
                   DataGrid::ColumnCount = 3
                   DataGrid::RowCount = 1
                   ChartType        = VtChChartType2dPie.
           MODIFY  CheeseChart
                   Row              = 1
                   @Column          = 1
                   @Data            = 100.
           MODIFY  CheeseChart
                   Row              = 1
                   @Column          = 2
                   @Data            = 100.
           MODIFY  CheeseChart
                   Row              = 1
                   @Column          = 3
                   @Data            = 100.

           MODIFY  CheeseChart
                   DataGrid::ColumnLabel(1, 1, "Slice 1")
                   DataGrid::ColumnLabel(2, 1, "Slice 2")
                   DataGrid::ColumnLabel(3, 1, "Slice 3")
                   DataGrid::RowLabel(1, 1, "The Row label")
                   ShowLegend       = 1
                   Visible          = 1.

           ACCEPT  OMITTED.
           EXIT    PROGRAM
           STOP    RUN
           .
```

##### ↳ ↳ Re: AcuCobol MSChart

- **From:** martin_xxxxx@hotmail.com (Martje)
- **Date:** 2004-11-24T01:20:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34c4918b.0411240120.3d90344e@posting.google.com>`
- **References:** `<34c4918b.0411230454.d3b8497@posting.google.com> <ICIod.9278$rh1.236638@news2.e.nsc.no>`

```
Thanx Cheesle !

I've tested it, and everything is working! And most important, i
understand your sample program.
I only have one more question about this issue.
Instead of MSCHART.DEF, i used MSCHRT20.DEF (I don't know if they are
the same), but when i test the program on a computer (Windows 98)
where i didn't install the visual basic program (i only downloaded
from the microsoft site the runtime for VB6), the program is not
working, and i'll get an error creating ActiveX control.
Purhapse, do you know what to download more, so i can get this program
working on every computer, whitout installing a complete program for
VB6? Or purhapse, must i use the standard MSCHART.DEF instead of the
MSCHRT20.DEF i've used? And if so, where can i find the correct
version of MSCHART.DEF

Thanx again!
```

###### ↳ ↳ ↳ Re: AcuCobol MSChart

- **From:** "Cheesle" <cheesle@NoSpamPlease.online.no>
- **Date:** 2004-11-24T15:58:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gj1pd.9431$rh1.239884@news2.e.nsc.no>`
- **References:** `<34c4918b.0411230454.d3b8497@posting.google.com> <ICIod.9278$rh1.236638@news2.e.nsc.no> <34c4918b.0411240120.3d90344e@posting.google.com>`

```
What you need to add is a license. One way to get that is to get it is to
upgrade to version 6.2 of ACUCOBOL-GT.
Another one is to get a utility from MSDN (Licreqst.exe) which you can use
on the machine of which you have Visual Basic installed and then execute and
get the license key that way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
