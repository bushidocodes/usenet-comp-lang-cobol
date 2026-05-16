[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Another sample, Another possible "component" or "user defined function"

_2 messages · 2 participants · 2009-01_

---

### Another sample, Another possible "component" or "user defined function"

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-09T18:27:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xXR9l.87521$zQ4.13002@en-nntp-02.dc1.easynews.com>`

```
For other reasons, I was looking at the presentation foils for a SHARE (IBM user 
group) presentation
  "Got COBOL?
    Bet you didn't know you could do THIS in COBOL"
at:
  http://www-01.ibm.com/support/docview.wss?uid=swg27009580&aid=1

In it (among other things) is a sample of how to convert an input string to 
"printable Hex".  I decided to take that code and come up with a possible 
"component" to answer how to do this.  I know that we have been asked how to do 
this in CLC on several occasions.  I hadn't stored any of the sample, so I just 
went ahead and modified the SHARE code and created a (slightly 
expanded/enhanced) version.  I have coded it as a "stand-alone" because that is 
easy for me to test.  A couple of comment lines need uncommenting to make it a 
callable routine - and others could make it a component or user-defined function 
or whatever.

As always, your style may not be my style <G> (indentation depends on fonts and 
tabs).

**** sample code starts here

       Identification Division.
        Program-ID.  CONV2HEX.
      * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
      * This code is based on a program that can be seen at:          *
      *http://www-01.ibm.com/support/docview.wss?uid=swg27009580&aid=1*
      * The presentation foils for a SHARE presentation               *
      *   "Got COBOL? Bet you didn't know you could do THIS in COBOL" *
      * and similar programs viewable elsewhere                       *
      * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
       Data Division.
        Working-Storage Section.
       01  HEXSTR  Pic  X(16)  Value "0123456789ABCDEF".
       01  DEC   Pic S9(04)  Binary Value Zero.
       01  FILLER Redefines DEC.
           05    Pic  X(01).
           05  DECBYTE  Pic  X(01).
       01  Sub   Pic S9(02)  Binary.
       01  Q   Pic S9(02)  Binary.
       01  R   Pic S9(02)  Binary.
      *
      *  Uncomment the Linage Section header and the USING statements on the 
Procedure
      *    Division Header when this is a callable subroutine
      *  Linkage Section.
       01  String-Length Pic 9(02).
       01  String-In.
           05  SI-Byte occurs 1 to 99 Times
                   Depending on String-length
                   Pic X(01).
       01  String-Out.
           05  SO-Bytes Occurs 1 to 99 Times
                  Depending on String-Length
                  Pic X(02).
       Procedure Division
      *        Using String-Length
      *              String-In
      *               String-Out
                .
        Mainline.
           If   String-Length Numeric
            and String-Length not Zero
               Display "  Input String:" String-In
               Perform Convert
               Display " Output String:" String-Out
           Else
               Display "Invalid String Length Specified"
           End-If
           GoBack
            .
       Convert.
           Perform
             Varying Sub
               From 1 By 1
               Until Sub > String-Length
                   Move SI-Byte (Sub)  To DECBYTE
                   Divide DEC By 16
                     Giving Q
                     Remainder R
                   End-Divide
                   Add 1 to Q
                   Add 1 to R
                   Move HEXSTR (Q:1)  TO SO-Bytes (Sub) (1:1)
                   Move HEXSTR (R:1)  TO SO-ByteS (Sub) (2:1)
           END-Perform
            .
*** end of sample code
```

#### ↳ Re: Another sample, Another possible "component" or "user defined function"

- **From:** Duh_OZ <ozzy.kopec@gmail.com>
- **Date:** 2009-01-12T07:52:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<522b005a-9f9b-4f14-b84d-48457a043aac@r36g2000prf.googlegroups.com>`
- **References:** `<xXR9l.87521$zQ4.13002@en-nntp-02.dc1.easynews.com>`

```
On Jan 9, 6:27 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> For other reasons, I was looking at the presentation foils for a SHARE (IBM user
> group) presentation
…[3 more quoted lines elided]…
>  http://www-01.ibm.com/support/docview.wss?uid=swg27009580&aid=1
==========
MF 3.2.20

 Input String:HeLlo World
Output String:48654C6C6F20576F726C64
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
