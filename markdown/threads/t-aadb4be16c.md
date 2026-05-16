[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing from M/F COBOL

_7 messages · 6 participants · 2008-03 → 2008-04_

---

### Printing from M/F COBOL

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2008-03-31T09:23:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`

```
Hi Chaps

An avid reader of this forum for years. Very interesting at times.

I have a question I am sure somebody can help me with.

I currently look after a customer who use all HP laser printers. 20
years ago we embedded PCL code to control these printers. Setting
landscape/portrait, duplex pages, the odd underline and bold bits.
When we moved to M/F Netexpress 3.1 we adopted the PC_PRINTER routines
and send a 'raw' file to the printer. I now have a new 'customer'
asking for some system and I am going to need to print for them. I
can't expect them to use HP printers here so what are my options. I
assume the PCL language is a HP thing and other printers won't
understand it.

Any ideas?

Thanks

Rud
```

#### ↳ Re: Printing from M/F COBOL

- **From:** pcsjih@comcast.net
- **Date:** 2008-03-31T10:30:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2aae6469-32d8-4e51-b8c7-b7213815b65f@a1g2000hsb.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`

```
On Mar 31, 12:23 pm, razor <irudd...@blueyonder.co.uk> wrote:
> Hi Chaps
>
…[18 more quoted lines elided]…
> Rud

Be sure that printer PCL compatable. It's usually written in the
specs. If the printer has a parallel port, it will be PCL
compatable.

jh
www.payrollpc.com
```

#### ↳ Re: Printing from M/F COBOL

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-03-31T11:53:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2779c773-1b5b-4862-88a5-f0af90ee78e5@c19g2000prf.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`

```
On Apr 1, 5:23 am, razor <irudd...@blueyonder.co.uk> wrote:
> Hi Chaps
>
…[12 more quoted lines elided]…
> understand it.

I tend to do all my printing, or other output, using templates
wherever possible. Templates contain all the formatting information
plus tags where the data items are to be substituted. For repeated
data there are several ways to achieve this, one way is the have the
template divided into named sections and the program calls for that
section as many times as required. Another way is to pass a table from
the program to the templating routine to cater for the repeating
groups.

Generally the data is passed as 'name:value' pairs in a table where
'name' relates to the tagname in the template and 'value' is to
replace the tag. This table may also need 'type' and 'length'. The
'type' may need to indicate that there is a series of values in a
second table if that mechanism is used.

Different templates can be used depending on the printer being
addressed. This is a matter of knowing the type of the printer
required and then naming the templates appropriately as report.type.
Then if you want a webpage output, or XML, or a PDF, or a CSV file, it
is only (!!) a matter of creating an appropriate template and having a
notional 'printer' of that type with the templating routines writing
to a disk file.

On Unix/Linux with CUPS printing system all printing can be Postscript
regardless of the actual printer capability as drivers will convert to
PCL or plain text as required, so templates can be fragments of
Postscript, though it also works if you output PCL or plain text to a
PCL printer.

For graphics type output forms (such as invoices) I use a slightly
different mechanim by drawing the postscript form with a vector
drawing program (I use tgif, it is old but reliable). Each output
field is signalled with a tag that is extended to the correct width
and length and set to the required font and other attributes. This
would be difficult to handle in Cobol so the program uses a template
to write out a merge file and a C program is actioned to merge the
data items into the form.

Actually, many years ago, I used JetForm under DOS (actually a
Multiuser DOS) with good results by having the program write a merge
file for that and then used my C program to replace JFMerge when I
needed Postscript. So the merge file mechanism is based on the
requirements of that. To illustrate how old that JetForm is, the
designer runs under Windows 2 and won't run on Windows 95 so I still
have a Windows 3.11 install (which will run Win2 programns) on a
virtual machine in case I needed to rework forms still in use.
```

#### ↳ Re: Printing from M/F COBOL

- **From:** Thane <thaneh@softwaresimple.com>
- **Date:** 2008-04-03T20:02:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20483544-ee57-49c7-b993-9c52a2ec8abc@x41g2000hsb.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`

```
Check out Cobol Form Print at http://www.flexus.com.  This will allow
you to print as you desire on any windows based printer.

On Mar 31, 11:23 am, razor <irudd...@blueyonder.co.uk> wrote:
> Hi Chaps
>
…[18 more quoted lines elided]…
> Rud
```

#### ↳ Re: Printing from M/F COBOL

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2008-04-07T11:50:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47f9eebe$0$2957$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com>`

```
razor a ï¿½crit :
> Hi Chaps
>
…[19 more quoted lines elided]…
>   

I do a lot of printing using PostScript. All the PostScript code is 
generated using methods from a OO Cobol library. The code has been 
developed using NetExpress and is an attempt to translate into Cobol the 
very good pslib library written in C. Maybe it is possible to 
encapsulate directly the C library but I could succeed in that 
direction.  So, I wrote a native Cobol library from scratch.
With Postscript, you can print text, draw graphics, embed images. It is 
quite simple to understand.
You can send the result to any PostScript printer from any system. Under 
Windows and Linux, GSView allows you to see the output on the screen.
Although not perfect - but excepted Jean-Sebastien Bach, what is perfect 
in this world ?! -, we use it daily without any problem.
The code is available at http://pscoblib.sourceforge.net/ if you need it.

Regards.


Alain
```

##### ↳ ↳ Re: Printing from M/F COBOL

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2008-04-24T08:50:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75544c31-c2ca-44ae-af4e-1199437137a4@b1g2000hsg.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com> <47f9eebe$0$2957$ba620e4c@news.skynet.be>`

```
Thanks for your suggestions.

I decided to stick with the PC_PRINTER routines. I have a few o/s
problems though that I hope maybe somebody has already had to resolve
in the past.

Problem one is where I print invoices or other reports. At the start
we have some control characters to set the font, orientation, pitch,
etc. Something like this.

01  LANDSCAPE.
    03 FILLER                 PIC 9(2) COMP VALUE 27.
    03 FILLER                 PIC X(16) VALUE
              "&l1o8d0l66p0e66F".

Using the PC_PRINT routines I can't do this obviously, especially not
if its going to a non-PCL printer. The PC_PRINT routines don't allow
me to print control characters (rightly so). I think I can resolve
this using the PC_PRINTER_SET_FONT call so thats ok. I may just
generate one print program that interprets these settings from the
existing printed reports and converts the to SET_FONT calls.


Problem two is that I want to print 'boxes' using line drawing
characters. I can't seem to get this working. I have experimented
using the PC_PRINTER_OPEN call by setting the 'flags' to
'11' (Normally set to '1' which just allows selection of a printer)
which brings up a printer font window that allows me to select
different fonts. But none of these allows me to print 'lines'. I
suspect I am barking up the wrong tree doing it this way so any help
will be appreciated.

Problem three is that sometimes in mid line I want to print some
characters in bold. The way I do this at the moment is by inserting
the PCL control characters at the right point in the print line. For
examplke:

   03  FILLER          PIC X(15) VALUE "NORMAL TEXT".
   03  FILLER          PIC 99 COMP VALUE 27.
   03  FILLER          PIC X(4) VALUE "(s4B".
   03  FILLER          PIC X(15) VALUE "BOLD TEXT".
   03  FILLER          PIC 99 COMP VALUE 27.
   03  FILLER          PIC X(4) VALUE "(s0B".
   03  FILLER          PIC X(15) VALUE "NORMAL TEXT".

Long winded maybe, but its been around 15 years, running on DOS vers
3, now on XP with a ScreenIO based interface. Looks wonderful.

Any ideas on how I can resolve this one?

Many thanks
```

###### ↳ ↳ ↳ Re: Printing from M/F COBOL

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2008-04-24T23:21:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8C8Qj.219200$pM4.194032@pd7urf1no>`
- **In-Reply-To:** `<75544c31-c2ca-44ae-af4e-1199437137a4@b1g2000hsg.googlegroups.com>`
- **References:** `<d02ed9d2-9012-429b-ab39-67c4484810f6@a22g2000hsc.googlegroups.com> <47f9eebe$0$2957$ba620e4c@news.skynet.be> <75544c31-c2ca-44ae-af4e-1199437137a4@b1g2000hsg.googlegroups.com>`

```
razor wrote:
> Thanks for your suggestions.
> 
…[48 more quoted lines elided]…
> Many thanks

As you are obviously using Net Express sign up for their Answer Forum, 
where you can get some help to specific queries, plus also check their 
KnowledgeBase; their site also includes PC-Printing examples.

Can't help you much myself as my PC was recently 'hospitalised' and now 
I have to get a new Request Key for N/E which was corrupted - so I 
currently can't even get into NE for Help, to view or test !

Problem 1 - you can't mess around mixing DOS style control characters 
with what PC_PRINT routines do. You have to do all your settings with 
PC_PRINT.

Problem 2 - Line drawing; not currently having access to NE I'm pretty 
sure you can't do this although you can print bitmaps. You will have to 
check with Micro Focus to see if there is a routine. (Bear in mind 
PC_PRINT is a set of 'popular' needs and not an all singin' all dancin' 
bit of software). Lookup up something like text2pdf, (recently listed 
here in CLC ) which allows more flexibility. If it is a need to put a 
box frame around sections of an invoice, text2pdf or others like it, 
will allow you to do this.

Problem 3 - Mid Line changing fonts. No problem (1) send a line with 
standard font/spacing and use my 'WriteAndPause' below; (2) Send a line 
with your Bold Font and again use the 'WriteAndPause' (3) send print 
'WriteAndNewline'

Whichever approach I would strongly support having your print routines 
in a separately called program/invoked class. No access to NE, so I 
can't update following. But on reflection when sending something like a 
printer header block, be it 1, 2, 3.....15 standard lines I would send 
the strings of text as an Ordered collection of objects to a 
called/invoked header routine, including fonts, size, bold etc., signal 
flags per line. The receiving method 'unpacks' each object in the 
collection to a printable text string. (That is - using class 
CharacterArray - a text string from the caller program/class is 
converted to an object and added to an OrderedCollection which is passed 
to the printing program. The receiving class then 'unpacks' individual 
objects, (using callback/iteration 'do') against the collection using 
class CharacterArray to prepare a text string for PC_PRINT.

I'm sure the last paragraph is as clear as mud - but should you wish to 
pursue, I don't mind giving it a shot to suit your needs, (other than 
that line printing gizmo - if you only need horizontals you can send a 
blank line UNDERLINED). But I'll need access to NE before I can help you.

Take the following as is, and It doesn't list quite all of the PC_PRINT 
routines.

Jimmy, Calgary AB


        *>----------------------- pcprint.cbl ---------------------------
	NE V 3.1

        Class-id.             PCprint
			     inherits from Base.

        Class-control.        PCprint             is class "pcprint"

			     CharacterArray	 is class "chararry"
			     MessageBox 	 is class "msgbox"
			      .

        *>---------------------------------------------------------------
        *> This class includes the following Micro Focus PC_PRINT
        *> routines

        *>  PC_PRINTER_CLOSE          Close a printer channel
        *>  PC_PRINTER_CONTROL        Send a printer command to a printer
        *>+ PC_PRINTER_DEFAULT_FONT   Set the default font
        *>+ PC_PRINTER_DEFAULT_NAME   Set the default printer
        *>+ PC_PRINTER_DEFAULT_PROPERTIES Set one or more properties
        *>  PC_PRINT_FILE             Print a file
        *>  PC_PRINTER_FREE_BMP       Free bitmap from memory
        *>+ PC_PRINTER_GET_COLOR      Set printer color
        *>+ PC_PRINTER_GET_FONT       Set printer font
        *>  PC_PRINTER_INFO           Get printer information
        *>  PC_PRINTER_LOAD_BMP       Load bitmap into memory
        *>  PC_PRINTER_OPEN           Open a printer channel
        *>+ PC_PRINTER_REDIRECTION_PROC
        *>                            Register a user function to be
        *>                            called when a program uses
        *>                            OPEN OUTPUT syntax.
        *>  PC_PRINTER_SET_COLOR      Set printer color
        *>+ PC_PRINTER_SET_DEFAULT    Set a process-wide default
        *>  PC_PRINTER_SET_FONT       Set printer font
        *>  PC_PRINTER_WRITE          Write text to a printer
        *>  PC_PRINTER_WRITE_BMP      Write bitmap to a printer


        *>--------------------------------------------------------------
        *>FACTORY.
        *>---------------------------------------------------------------
        *>END FACTORY.
        *>-------------------------------------------------------------
        OBJECT.
        *>-------------------------------------------------------------
        OBJECT-STORAGE SECTION. *>(COBOL 200X = WORKING-STORAGE SECTION)

        01 ws-PrintInfoStructure.
          05 PrintStructSize          pic x(4) comp-5 value 52.
          05 Printhdc                 pic x(4) comp-5.
          05 Printhps                 pic x(4) comp-5.
          05 Printorientation         pic x(4) comp-5.
          05 Printrows                pic x(4) comp-5.
          05 Printcols                pic x(4) comp-5.
          05 PrintRowsLeft            pic x(4) comp-5.
          05 PrintMaxHoriz            pic x(4) comp-5.
          05 PrintMaxVert             pic x(4) comp-5.
          05 PrintMinHoriz            pic x(4) comp-5.
          05 PrintMinVert             pic x(4) comp-5.
          05 PrintCurrHoriz           pic x(4) comp-5.
          05 PrintCurrVert            pic x(4) comp-5.

        01 ws-PrinterHandle          pic x(4) comp-5.
        01 ws-PrintWindowHandle      pic x(4) comp-5.
        01 ws-result                 pic x(4) comp-5.
        01 ws-StatusCode             pic x(4) comp-5.

        *>-------------------------------------------------------------
        01 os-Parent                 object reference.

        *>-------------------------------------------------------------
        Method-id. "checkPrinterStatus".
        *>-------------------------------------------------------------
        Local-Storage section.
        01 PrintCommand                pic x(4) comp-5.
	 88 Abort		      value 1.
	 88 ThrowPage		      value 2.
	 88 FlushBuffers	      value 3.
	 88 NewLine		      value 4.

        Procedure Division.

	if ws-StatusCode <> zeroes
	   move 99 to ws-result
	   invoke self "PrintError"
	   set Abort to true
	   call "PC_PRINTER_CONTROL"  using	ws-PrinterHandle
				      by value	PrintCommand
				      returning ws-StatusCode
	   call "PC_PRINTER_CLOSE"    using	ws-PrinterHandle
				      returning ws-StatusCode
	else move zeroes to ws-result
	End-if
        End Method "checkPrinterStatus".
        *>--------------------------------------------------------
        Method-id. "closePrinter".
        *>-------------------------------------------------------------

	   call "PC_PRINTER_CLOSE"    using	ws-PrinterHandle
				      returning ws-StatusCode
        End Method "closePrinter".
        *>--------------------------------------------------------------
        Method-id. "getLinecount".
        *>-------------------------------------------------------------
        Local-Storage section.
        01 ls-result                         pic x(4) comp-5.
        Linkage section.
        01 lnk-LineCount                     pic x(4) comp-5.

        Procedure Division returning lnk-LineCount.

	 invoke self "PrinterInfo" returning ls-result

	 if ls-result = zeroes
             move PrintRowsLeft to lnk-LineCount
	 End-if
        End Method "getLinecount".
        *>-------------------------------------------------------------
        Method-id. "openPrinter".
        *>-------------------------------------------------------------
        Linkage section.

        *>  Printflags :-

        *> bit 0  Display a printer control dialog to allow you to define
        *>        the printer characteristics (cannot be used with bit 2
        *>        or bit 3)
        *> bit 1  Display a font dialog box to allow you to define the
        *>        default font for the document
        *> bit 2  Print in portrait orientation (cannot be used with bit
        *>        0 or bit 3)
        *> bit 3  Print in landscape orientation (cannot be used with bit
        *>        0 or bit 2)
        *> bit 4  Display a progress indicator dialog box

        *>  78 NoDialog		      value	0.
        *>  78 ControlDialog	      value	1.
        *>  78 FontDialog	      value    10.
        *>  78 Portrait		      value   100.
        *>  78 Landscape 	      value  1000.
        *>  78 ProgressIndicator       value 10000.

        01 PrintDocument.
	  05 PrintTitleLen	      pic x(2) comp-5.
	  05 PrintTitle		      pic x(65).
        01 Printflags                  pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using     PrintDocument
				    by value PrintFlags
			  returning lnk-result.

            move zeroes to ws-PrinterHandle, ws-PrintWindowHandle
	   call "PC_PRINTER_OPEN"     using	ws-PrinterHandle
						PrintDocument
				      by value	PrintFlags
				      by value	ws-PrintWindowHandle
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result

        End Method "openPrinter".
        *>------------------------------------------------------------
        Method-id. "pageThrow".
        *>------------------------------------------------------------
        *>
        *> This is used for laser printers when printing 'back-to-back'
        *> or when wanting to throw a blank page between separate parts
        *> of a report

        *> Note : It is the calling program(class) that checks that the
        *> printed report exceeds more than two pages

        Local-Storage section.
        01 ls-Command                  pic x(4) comp-5.
	 88 ThrowPage		      value 2.
        01 pages-remainder             pic x(4) comp-5.
        Linkage section.
        01 lnk-pages                   pic x(4) comp-5.
        01 lnk-ErrorCode               pic x(4) comp-5.
        Procedure Division using     lnk-pages
			  returning lnk-ErrorCode.

	move zeroes to lnk-ErrorCode
         compute pages-remainder = function rem (lnk-pages, 2)

         if pages-remainder <> zeroes
            set ThrowPage to true
            invoke self "printCommand"
                 using by value ls-Command
                 returning lnk-ErrorCode
         End-if

        End Method "pageThrow".
        *>------------------------------------------------------------
        Method-id. "printAfile".
        *>-------------------------------------------------------------

        *>filename :  Group Item :-
        *>file-name-length pic x(2) comp-5
        *>file-text        picx(n) - space/null terminated
        *>
        *>Document-Title-Length pic x(2) comp-5.
        *>Document-Title-Text   pic x(n).
        *>
        *>Flags :-
        *>bit 0 Display printer control dialog(Can't use with bits 2 & 3)
        *>bit 1 Display a font dialog box
        *>bit 2 Print in portrait orientation (can't use with bits 0 & 3)
        *>bit 3 Print in landscape orientation(can't use with bits 0 & 2)
        *>bit 4 Display a progress indicator dialog box

        Linkage section.
        01 PCprintName.
           05 PCprintnameLength     pic x(2) comp-5.
           05 PCprintnameText       pic x(100).
        01 PrintTitle.
           05 PrintTitleLength        pic x(2) comp-5.
           05 PrintTitleText          pic x(65).
        01 Printflags                 pic x(4) comp-5.
        01 lnk-result                 pic x(4) comp-5.

        Procedure Division using PCprintName
                                 PrintTitle
				by value PrintFlags
			  returning lnk-result.

            call "PC_PRINT_FILE"       using     PCprintname
                                                 PrintTitle
				      by value	PrintFlags
				      by value	ws-PrintWindowHandle
				      returning ws-StatusCode

	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result

        End Method "printAfile".
        *>--------------------------------------------------------------
        Method-id. "printCommand".
        *>-------------------------------------------------------------
        Linkage section.
        01 PrintCommand                pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using by value PrintCommand
			  returning lnk-result.

	   call "PC_PRINTER_CONTROL"  using	ws-PrinterHandle
				      by value	PrintCommand
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result
        End Method "printCommand".
        *>--------------------------------------------------------
        Method-id. "PrintError".
        *>-------------------------------------------------------------
        working-storage section.
        01 PE1.
	  05 pic x(40) value "01 Couldn't open printer device         ".
	  05 pic x(40) value "02 Invalid printer control code         ".
	  05 pic x(40) value "03 No device associated with handle     ".
	  05 pic x(40) value "04 Out of memory while printing         ".
	  05 pic x(40) value "05 Failed to open file                  ".
	  05 pic x(40) value "06 Disk full while spooling file        ".
	  05 pic x(40) value "07 Aborted. Job not sent to spooler.    ".
	  05 pic x(40) value "08 Printer info badly constructed       ".
	  05 pic x(40) value "09 No default printer found             ".
	  05 pic x(40) value "10 Error when displaying dialog         ".
	  05 pic x(40) value "11 Write failure                        ".
	  05 pic x(40) value "12 No fonts found compatible to printer ".
	  05 pic x(40) value "13 The font requested does not exist    ".
	  05 pic x(40) value "14 User aborted print job               ".
	  05 pic x(40) value "15 Reserved - Unspecified error         ".
	  05 pic x(40) value "16 Reserved - Unspecified error         ".
	  05 pic x(40) value "17 Reserved - Unspecified error         ".
	  05 pic x(40) value "18 Failed to load bitmap                ".
	  05 pic x(40) value "19 Invalid bitmap id                    ".
	  05 pic x(40) value "20 Failed to free bitmap                ".
	  05 pic x(40) value "21 Failed to print bitmap               ".
	  05 pic x(40) value "22 Bad parameter                        ".
           05 pic x(40) value "23 User Cancel or Internal error        ".

        01 PE2 redefines PE1.
	  05 PE3 occurs 23	    pic x(40).

        Local-Storage section.
        01 ls-length                         pic x(4) comp-5.
        01 ls-MsgBox			    object reference.
        01 ls-string			    object reference.
        01 ls-text			    pic x(40).


	move PE3 (ws-StatusCode) to ls-text
	invoke MessageBox "new" using os-Parent returning ls-MsgBox
	invoke ls-MsgBox "SetLabelZ" using z"Printer Error"  & x"00"
	move length of ls-text to ls-length
	invoke CharacterArray "withlengthvalue"
	       using ls-length ls-text returning ls-string
	invoke ls-MsgBox "setMessage" using ls-string
	invoke ls-MsgBox "setTypeCritical"
	invoke ls-MsgBox "Cancel"
	invoke ls-MsgBox "show"
	invoke ls-MsgBox "finalize" returning ls-MsgBox
        End Method "PrintError".
        *>----------------------------------------------------------
        Method-id. "PrinterInfo".
        *>-------------------------------------------------------------
        Linkage section.
        01 lnk-result                 pic x(4) comp-5.

        Procedure Division returning lnk-result.

	   call "PC_PRINTER_INFO"     using	ws-PrinterHandle
						ws-PrintInfoStructure
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result
        End Method "PrinterInfo".
        *>---------------------------------------------------------------
        Method-id. "setDefaultFont".
        *>--------------------------------------------------------------

        *> font-family-name    Group item defined as:
        *>   (a)name-len      pic x(2) comp-5.
        *>   (b)name-text     pic x(n).
        *>
        *> font-size       Numeric literal or pic x(4) comp-5.
        *>                 If the point size is zero the font
        *>                 is reset to the system defaults.
        *>
        *> FontStyle :     Numeric literal or pic x(4) comp-5.

        *>  78 Regular                 value    0.
        *>  78 Italic                  value    1.      bit 0  Italic
        *>  78 Underline               value   10.      bit 1  Underline
        *>  78 Strikeout               value  100.      bit 2  Strikeout
        *>  78 Bold                    value 1000.      bit 3  Bold


        Linkage section.
        01 FontFamily.
           05 FontFamilyLength              pic x(2) comp-5.
           05 FontFamilyText                pic x(40).
        01 FontSize                         pic x(4) comp-5.
        01 FontStyle                        pic x(4) comp-5.
        01 lnk-result                       pic x(4) comp-5.

        Procedure Division using           FontFamily
                                 by value  FontSize
                                 by value  FontStyle
                                 returning lnk-result.

            call "PC_PRINTER_DEFAULT_FONT"  using FontFamily
                                                  by value FontSize
                                                  by value FontStyle
                                            returning ws-StatusCode
	   invoke self "checkPrinterStatus"
            move ws-result to lnk-result

        End Method "setDefaultFont".
        *>-------------------------------------------------------------
        Method-id. "setFont".
        *>-------------------------------------------------------------
        Linkage section.

        *> FontStyle :-

        *>  78 Regular		      value    0.
        *>  78 Italic		      value    1.      bit 0  Italic
        *>  78 Underline 	      value   10.      bit 1  Underline
        *>  78 Strikeout 	      value  100.      bit 2  Strikeout
        *>  78 Bold		      value 1000.      bit 3  Bold

        01 FontFamily.
	  05 FontNameLen	      pic x(2) comp-5.
	  05 FontNameText	      pic x(20).
        01 FontSize                    pic x(4) comp-5.
        01 FontStyle                   pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using FontFamily
				by value FontSize
				by value FontStyle
			  returning lnk-result.

	   call "PC_PRINTER_SET_FONT" using	ws-PrinterHandle
                                                 FontFamily
                                       by value  FontSize
                                       by value  FontStyle
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result
        End Method "setFont".
        *>-------------------------------------------------------------
        Method-id. "setParent".
        *>-------------------------------------------------------------
        Linkage section.
        01 lnk-parent		       object reference.
        Procedure Division using lnk-parent.
          set os-Parent to lnk-parent
        End Method "setParent".
        *>--------------------------------------------------------------
        Method-id. "writeAndPause".
        *>-------------------------------------------------------------
        Linkage section.
        01 PrintBuffer		      pic x(185).
        01 PrintBufferLen              pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using PrintBuffer
				by value PrintBufferLen
			  returning lnk-result.

	   call "PC_PRINTER_WRITE"    using	ws-PrinterHandle
						PrintBuffer
				      by value	PrintBufferLen
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"
	   move ws-result to lnk-result
        End Method "writeAndPause".
        *>--------------------------------------------------------------
        Method-id. "writeAndNewline".
        *>-------------------------------------------------------------
        Local-Storage section.
        01 ls-return                   pic x(4) comp-5.
        01 PrintCommand                pic x(4) comp-5.
	 88 Abort		      value 1.
	 88 ThrowPage		      value 2.
	 88 FlushBuffers	      value 3.
	 88 NewLine		      value 4.
        Linkage section.
        01 PrintBuffer		      pic x(185).
        01 PrintBufferLen              pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using PrintBuffer
				by value PrintBufferLen
			  returning lnk-result.

	   call "PC_PRINTER_WRITE"    using	ws-PrinterHandle
						PrintBuffer
				      by value	PrintBufferLen
				      returning ws-StatusCode
	   invoke self "checkPrinterStatus"

	   if	 ws-result = zeroes
		 set Newline to true
		 invoke self "printCommand"
			using by value PrintCommand returning ls-return
		  move ls-return to lnk-result

	   else move ws-result to lnk-result
	   End-if
        End Method "writeAndNewline".
        *>--------------------------------------------------------------
        Method-id. "writeBlankLine".
        *>-------------------------------------------------------------
        Local-Storage section.
        01 x                           pic x(4) comp-5.
        01 PrintBuffer		      pic x(185).
        01 PrintBufferLen              pic x(4) comp-5.
        Linkage section.
        01 n                           pic x(4) comp-5.
        01 lnk-result                  pic x(4) comp-5.

        Procedure Division using n
			  returning lnk-result.

	   move spaces to PrintBuffer
	   move 1      to PrintBufferLen
	   perform varying x from 1 by 1 until x > n
                    or lnk-result <> zeroes

	     invoke self "writeAndNewline"
                      using            PrintBuffer
                             by value  PrintBufferLen
                      returning        lnk-result
	   End-perform

        End Method "writeBlankLine".
        *>---------------------------------------------------------------

        END OBJECT.
        END CLASS PCprint.

*---------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
