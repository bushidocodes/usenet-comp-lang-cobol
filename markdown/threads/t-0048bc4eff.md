[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SCREEN SECTION and ACCEPT ecxamples.

_7 messages · 3 participants · 2005-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### SCREEN SECTION and ACCEPT ecxamples.

- **From:** john@wexfordpress.com
- **Date:** 2005-08-06T15:03:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com>`

```
All my COBOL manuals and books wre written before screen handling
became standardized. I can find good examples of displaying pretty
thing on the screen but none showing how you ACCEPT data in a SCREEN
environment. In addition to the mechanics of same there are some
gotchas when the whole screen is accepted at once, or so I read on the
newsgroup.

Can someone point me to a fairly simple worked example of a data screen
DISPLAYed and then the data thereon ACCEPTed? I have a newer book on
order
but it isn't here yet.

I am using TinyCobol on a Slackware system.

John Culleton,
AKA Rip Van Winkle.
```

#### ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-06T16:42:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123371772.289181.55770@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com>`

```
> Can someone point me to a fairly simple worked example
> of a data screen DISPLAYed and then the data thereon
> ACCEPTed?

When doing Accept/display I generally accept each field in turn
allowing back field.
```

##### ↳ ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** john@wexfordpress.com
- **Date:** 2005-08-07T10:31:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123435913.964782.161290@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123371772.289181.55770@g44g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com> <1123371772.289181.55770@g44g2000cwa.googlegroups.com>`

```
Excellent. I presume you ACCEPT the field as it is described in the
SCREEN but validate  the corresponding field in WORKING-STORAGE.  Did I
guess right?

John C.
```

##### ↳ ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** john@wexfordpress.com
- **Date:** 2005-08-07T10:32:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123435920.605306.242800@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123371772.289181.55770@g44g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com> <1123371772.289181.55770@g44g2000cwa.googlegroups.com>`

```
Excellent. I presume you ACCEPT the field as it is described in the
SCREEN but validate  the corresponding field in WORKING-STORAGE.  Did I
guess right?

John C.
```

###### ↳ ↳ ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-08-07T11:54:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123440841.623766.292100@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123435920.605306.242800@g14g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com> <1123371772.289181.55770@g44g2000cwa.googlegroups.com> <1123435920.605306.242800@g14g2000cwa.googlegroups.com>`

```
Hi,

Yes, after you have accepted the screen from the endUser, then you can
validate all
of his/her data entry in the working-storage section (which is the
variables you have used
in the screen to receive the data input).

Additionally, some screen-section syntax can further help you with the
validation task
automatically, for example, the syntax FULL will force the endUser to
enter data and fill
the entire receiving field to match its length. Case in point:

	WORKING-STORAGE SECTION.

	01  300-ACTIVE-NUMERIC.
		05  300-ZIPCODE	        PIC 9(5) VALUE 0.

	SCREEN SECTION.

	01  INPUT-SCREEN AUTO.
		05  LINE 12 COLUMN 21    HIGHLIGHT 'ZIP CODE: '.
		05  ZIPCODE                     REVERSE-VIDEO PIC Z(5)
				         USING 300-ZIPCODE FULL.

The endUser must enter five digits in the zipCode field in order for
him/her to proceed to
the next entry field, otherWise the system will sound a beep and will
NOT continue.

Kellie.
```

###### ↳ ↳ ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-08-07T15:24:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123453499.738779.254730@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123435920.605306.242800@g14g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com> <1123371772.289181.55770@g44g2000cwa.googlegroups.com> <1123435920.605306.242800@g14g2000cwa.googlegroups.com>`

```
I do not use SCREEN SECTION at all but have the screen areas in W-S.
The 'background' is defined as an 01 with a series of 03 with the VALUE
clauses, so it may be 2000 characters long - 25 x 80.  This is
redefined as PIC X(2000) for the DISPLAY AT 0101.  The screen is then
redefined again with FILLERs for everything except the input fields.
This is DISPLAYed to show the input fields - on a group DISPLAY AT 0101
only the non-FILLER are displayed.

I then accept each field in turn in a perform loop that uses
field-number to indicate which field I am on:
  MOVE 1 TO field-number
  PERFORM UNTIL field-number > 7
     IF field-number = 1
          ACCEPT first-field AT position
          PERFORM Check-keys
          (check-keys will test function-keys and may set
           field-number to 99 (exit) or subtract 1 (previous)
           or ...)
          IF field-number = 1
               validate field
               if ok
                   add 1 to field-number
              end-if
          end-if
        end-if

        if field-number = 2
            .....

This is rather tedious and it also sets the colours using PERFORM
Screen-xx where xx may be BG (background) FG (foreground, IN (input
field), err (error) etc.

For this I developed some simple code generating programs that take a
text file that has the layout and a list of field definitions and
creates a W-S screen area, code blocks for accepting the fields and so
on. eg (though it will probably wrap horribly):

*PREFIX
PM-
*FIELDS
- screenfield,order,movefield,type,paragraph,text
IKEY,0,P1-Key
IGroup,1,P1-Group,,PROC-GROUP,Product Group code - Scan for help, F6 to
delete product
DGROUP,0
IDim,30,P1-Dim,,,Use 'Y' to indicate non stock
IDesc,2,P1-Descr,PROC-DESC,,Description for Invoices
IClass,31,P1-Class,,,Product Classification
IBarCode,3,P1-BarCode,,PROC-BarCode,Barcode of product
IUNIT,32,P1-Unit,,,Unit
IBulk,4,P1-BulkRef,,,Product code of Bulk stock
ILabel,5,P1-Label-Ref,,,Product code of Label stock
ICarton,5,P1-Carton-Ref,,,Product code of Carton stock

IStdCost,6,P1-Cost1,4,,Standard cost
ITaxCode,33,P1-TaxCode,,Proc-Tax,Tax Code
DTaxRATE,0
IAveCost,6,P1-Cost2,4,,Average Cost
IDisc,34,P1-Disc,,PROC-DISC,Discountable Y/N
ILastCost,6,P1-Cost3,4,,Last cost
IPrice1,7,P1-Price(1),2,,Price 1
IPrice2,7,P1-Price(2),2,,Price 2
IPrice3,7,P1-Price(3),2,,Price 3
IRetail,8,P1-RetPrice,2,,Suggested Retail price

Isup,9,P1-Supplier,,Proc-Supplier,Supplier code - scan for next
DSup,0
IMinimum,35,P1-MinStock,0,,Minimum stock level required
ISCode,10,P1-Sup-Code,,,Supplier's code
ISDesc,11,P1-Sup-Desc,,,Supplier's description
ISPrice,12,P1-Sup-Price,2,,Supplier's price FOB or CIF
ISPer,13,P1-Sup-Per,0,,Price per quantity
ISCurr,14,P1-Sup-Curr,,PROC-CURR,Supplier's price currency
DSCurr,0
IOrigin,15,P1-Origin,,PROC-ORIGIN,Country of Origin
DOrigin,0
IDutyRate,16,P1-Duty-Rate,2,,Duty Rate

*SCREEN
-------------------------------------------------------------------------------
Product Code  [%%%%%]                                        PRODUCT
MAINTENANCE

Group         [%%]    %%%%%%%%%%%%%%%%%%%%%%%%%%      Non-Dimishing [%]
Description   [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]    Class         [%]
Barcode       [%%%%%%%%%%%%%]                         Unit
[%%%]
Bulk Stock    [%%%%%]
Label Stock   [%%%%%]
Carton Stock  [%%%%%]
Standard Cost [%%%%%%%%]                              Tax Code      [%]
  %%%%%
Average Cost  [%%%%%%%%]                              Discountable  [%]
Last Cost     [%%%%%%%%]
Prices        [%%%%%%%%] [%%%%%%%%] [%%%%%%%%]
Retail Price  [%%%%%%%%]

Supplier ..   [%%%]   %%%%%%%%%%%%%%%%%%%%%%%%%%      Minimum
[%%%%%%]
Vendor Part   [%%%%%%%%%%%%%%%%%%]
  Description [%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]
FOB Price     [%%%%%%%%]
Price per     [%%%%%%]
Currency code [%%]   %%%%%%%%%%%%%%%%%%
Origin        [%%%%] %%%%%%%%%%%%%%%%%%
Duty Rate     [%%%%%]
-------------------------------------------------------------------------------
*END


```

#### ↳ Re: SCREEN SECTION and ACCEPT ecxamples.

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-08-06T23:30:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1123396223.513007.51120@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com>`
- **References:** `<1123365829.804683.308590@g44g2000cwa.googlegroups.com>`

```
Hi,

Here is a sample code for Accept/Dispaly statement for microFocus
Cobol:

       IDENTIFICATION  DIVISION.
       PROGRAM-ID.     SAMPLE.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       SOURCE-COMPUTER. IBM-ATX.
       OBJECT-COMPUTER. IBM-ATX.
       SPECIAL-NAMES.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

       DATA DIVISION.
       FILE SECTION.

       WORKING-STORAGE SECTION.

       01  300-ACTIVE-SPACES  VALUE SPACES.
           05  300-COMPANY-NAME       PIC X(30).
           05  300-LAST-NAME                PIC X(25).
           05  300-FIRST-NAME               PIC X(15).
           05  300-MAIL-ADDRESS          PIC X(30).


       SCREEN SECTION.

       01  CLEAR-SCREEN.
           05  BLANK SCREEN BACKGROUND-COLOR 5 FOREGROUND-COLOR 7.

       01  INPUT-SCREEN AUTO.
           05  BACKGROUND-COLOR 5 FOREGROUND-COLOR 7.
           05  LINE 6  COLUMN 22    HIGHLIGHT 'COMPANY: '.
           05  COMPANY-NAME       REVERSE-VIDEO PIC X(30)
                                                  USING
300-COMPANY-NAME.
           05  LINE 7  COLUMN 20    HIGHLIGHT 'LAST NAME: '.
           05  LAST-NAME               REVERSE-VIDEO PIC X(25)
                                                  USING 300-LAST-NAME.
           05  LINE 8  COLUMN 19    HIGHLIGHT 'FIRST NAME: '.
           05  FIRST-NAME               REVERSE-VIDEO PIC X(15)
                                                   USING
300-FIRST-NAME.
           05  LINE 9  COLUMN 22    HIGHLIGHT 'ADDRESS: '.
           05  MAIL-ADDRESS         REVERSE-VIDEO PIC X(30)
                                                  USING
300-MAIL-ADDRESS.


       PROCEDURE DIVISION.
       100-MAIN-MODULE.

            DISPLAY CLEAR-SCREEN.
            DISPLAY INPUT-SCREEN.
            ACCEPT  INPUT-SCREEN.
            STOP RUN.

You could also code the Accept/Display statement like this:

	display "Enter your last name:  "    at 1010.
	accept lastName                           at 1033.
	display "Enter your first name:  "    at 1110.
	accept firstName                           at 1133.
	display "Enter your address:     "    at 1210.
	accept mailing-address                  at 1233.
	stop run.

Hope these information helps,

Kellie.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
