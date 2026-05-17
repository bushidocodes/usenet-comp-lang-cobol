[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VMS COBOL and Excel spreadsheets

_11 messages · 7 participants · 1998-01_

---

### VMS COBOL and Excel spreadsheets

- **From:** "bob evans" <ua-author-905144@usenetarchives.gap>
- **Date:** 1998-01-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34B7B124.D85BA843@sprintmail.com>`

```

Has anyone ever been able to create an Excel Spreadsheets using VMS COBOL?
I know that I can create a text delimited import file into Excel, but I need to
create an actual spreadsheet.
```

#### ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "bob berman" <ua-author-6589116@usenetarchives.gap>
- **Date:** 1998-01-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34B7B124.D85BA843@sprintmail.com>`
- **References:** `<34B7B124.D85BA843@sprintmail.com>`

```

Bob Evans wrote:
›
› Has anyone ever been able to create an Excel Spreadsheets using VMS COBOL?
› I know that I can create a text delimited import file into Excel, but I need to
› create an actual spreadsheet.

I don't know if VMS Cobol will support starting Excel via DDE, as
languages such as VB can.

Bob B
|----------------------------------------------------------------------|
|           Bob & Nancy  Berman  -   West Hartford, CT                 |
…[4 more quoted lines elided]…
|----------------------------------------------------------------------|
```

##### ↳ ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "g. vincent w. moore" <ua-author-17074583@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p2@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p2@usenetarchives.gap>`

```

› Bob Evans wrote:
›› 
›› Has anyone ever been able to create an Excel Spreadsheets using VMS COBOL?
›› I know that I can create a text delimited import file into Excel, but I need to
›› create an actual spreadsheet.

while it's *possible* to do, the actual conversion of data would take
some serious client server tinkering. first you would have to
send the file across, then change all the PC specific numbers to
VMS/VAX specific numbers, do the calculations and send it back.

i wondered this once myself about lotus, so i went to their website and
looked up their file format.

keep in mind that alot of VAX have *bigger* numbers than PC's, so
there probably would be no loss of precision.

however, this is most definitely not something you would do in cobol,
unless you have an excellent compiler.

maybe C. A simpler solution would be simply to buy a spreadsheet server,
i once read an article on one, it's called ez-base or something.
```

#### ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "joh..." <ua-author-14608346@usenetarchives.gap>
- **Date:** 1998-01-10T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34B7B124.D85BA843@sprintmail.com>`
- **References:** `<34B7B124.D85BA843@sprintmail.com>`

```

Have you considered letting Excel create the worksheets by directly
accessing the Cobol data. We have 1000's of customers who do it this
way daily using Easysoft ODBC.

More info at http://www.easysoft.com


John Kos
Easysoft


On Sat, 10 Jan 1998 12:34:29 -0500, Bob Evans
wrote:

› Has anyone ever been able to create an Excel Spreadsheets using VMS COBOL?
› I know that I can create a text delimited import file into Excel, but I need to
› create an actual spreadsheet.
›
```

#### ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34B7B124.D85BA843@sprintmail.com>`
- **References:** `<34B7B124.D85BA843@sprintmail.com>`

```

Bob Evans wrote:
› 
› Has anyone ever been able to create an Excel Spreadsheets using VMS
…[3 more quoted lines elided]…
› create an actual spreadsheet.

You could use our Relational Databridge for VMS client/server product to
use the VMS COBOL files as an ODBC data source. You then use the Data,
Get External Data command to bring the data in from the ODBC data
source. Assuming you have the COBOL descriptions of the data files
(FDs), you should be accessing VMS COBOL data files in a couple of hours
after opening the package.

If this doesn't solve the problem, then please describe the problem you
are trying to solve, since the possibilities for creating an "actual
spreadsheet" seem quite difficult.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

##### ↳ ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "bob evans" <ua-author-905144@usenetarchives.gap>
- **Date:** 1998-01-12T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p5@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p5@usenetarchives.gap>`

```



Tom Morrison wrote:

› Bob Evans wrote:
›› 
…[15 more quoted lines elided]…
› spreadsheet" seem quite difficult.

Having Excel access my COBOL files does NOT solve the problem.
I have VERY LAZY end users who do not want to do anything to get their own data.
They want the spreadsheet waiting for them in their PC the first thing when they
get in the morning. So I "HAVE TO" run a automated process that will build the
spreadsheet from a COBOL file (and in some cases SYBASE tables) and transfer the
said spreadsheet into a user's PC.

I could look into trying to automate the process from EXCEL using the user's PC
but I have very limited access to their machines. AND knowing my users, they
would probably turn off the PC overnight. (yes, I know, that causes a problem
with the file transfer idea overnight, but that I can work around)
```

###### ↳ ↳ ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1998-01-13T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p6@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p5@usenetarchives.gap> <gap-74df33a4ef-p6@usenetarchives.gap>`

```

On Tue, 13 Jan 1998 18:52:24 -0500, Bob Evans
wrote:

› Tom Morrison wrote:
 
›› Bob Evans wrote:
››› 
…[22 more quoted lines elided]…
› said spreadsheet into a user's PC.
 
› I could look into trying to automate the process from EXCEL using the user's PC
› but I have very limited access to their machines. AND knowing my users, they
› would probably turn off the PC overnight. (yes, I know, that causes a problem
› with the file transfer idea overnight, but that I can work around)

hmm. this is a complex problem.

i would expect you to convert data at the PC end as the mainframe
already does enough work.

ok, let's write a few ideas and specs:

go to the microsoft developer network and buy the excel software
libary extensions.

you will need to write a dll yourself which has these functions:

server_send_spreadsheet taking as parameters
pointer to the worksheet
a conversion file with 4 parameters in RAM
(probably handled easily as a Windows List_indexed_type unless
you have thousands of variables)

variable_name_to_search_for_in_worksheet
directionx, directiony
PIC clause
variable_server_name

you want to copy the worksheet, and place this function
into a timer or thread temporarily, as waiting for
the conversion might take sometime and freeing
up excel as soon as possible is good.

this searches a worksheets cells for text containing the
variable (or saved under a filename)
tell the server to prepare to receive worksheet
while found
tell the server to prepare to receieve
move indexed_variables_location to
temp_location
add directionx and directiony to temp_location
perform until temp is empty
tell the server here is a variable
convert the temp_location
send that temp_location
tell the server the variable have been sent
tell the server the worksheet has been sent


add_excel_spreadsheet_cell taking as parameters
location_X, location_Y,
worksheet_number_z, char array of data,
char array of pic_float_specs or sybase specs



the reason to use a char array for data is that it allows easy
expansion.

pic_float_specs is simply a string of the variable beginning after the
'PIC' clause such as 'S9v9'.

convert pic_float_specs into uppercase.
check if your hash_table_variable_exists

convert your data, using the pic_float_specs, to a float.
add the float to the spreadsheet
format the number
from the bought spreadsheet library
according to PIC_float_spec


Excel_message_handler taking no parameters
this simply intercepts excel when it attempts to close a
worksheet and determines if it is a worksheet that VMS uses.
if so, it calls the send_to_server program
when it recieves an Excel Close Program, it executes the
kill_worksheet_specs function



these functions are also in your server/client class
get_cell
this gives you the formula for a cell

send_keys_to_cell_from_server
this sends keys to a cell
(it's a fast method of writing the formula)

update_dll
downloads dll to a temp file
crc-checks it twice
closes Excel (if running)
waits until excel's worksheet
dll thread has finished
renames it the current file and reboots windows


kill_worksheet_specs
removes the indexed file


this is just a basic spec, but what you are asking for is probably not
sold as a software product yet. you probably have to have it done
customly. and it looks like a year long project.

write the functions out in a hierarchy so you can see the overall
design better.

you are going to need programmers who know the following:

spreadsheet

C (to read (excel library, networking library (if in C) )
floating point specifications)

Cobol (to write the dll interface to excel library as well as make it
1 language only)

client/server

SYBASE

you also will need some type of the following:
Cobol for Windows
Cobol for VMS
Cobol networking extensions
Excel Developer Library
Windows Programming Book
VMS Programming Book

so you are talking about 6 programmers, if they all have enough
overlap, and are given these specs. try to write the entire library in
1 language, if at all possible.

after you have the library, it should be easy to implement whatever
you want across the network.

you might also want to add a scheduling function so that it updates
the server every so often.


the primary advantage of having this library is that even if all your
users use different excel functions, adding formulas and sending keys
to worksheets is such a basic function, that you can practically send
and receive from any version.

i didn't finish the specs, but you get the idea...

gvw··.@ix.··m.com remove the spam
```

###### ↳ ↳ ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-01-13T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p6@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p5@usenetarchives.gap> <gap-74df33a4ef-p6@usenetarchives.gap>`

```

Bob Evans wrote:
› 
› Tom Morrison wrote:
…[26 more quoted lines elided]…
› Having Excel access my COBOL files does NOT solve the problem.

But it probably does. Do your PCs have network access to the VMS
machine? If so, read on...

› [snip] So I "HAVE TO" run a automated process that will
› build the
…[8 more quoted lines elided]…
› would probably turn off the PC overnight. 

Excel has an ODBC add-in that would allow you to write an Excel macro to
use ODBC to pull the data from the COBOL files and Sybase tables. While
not an Excel expert, I do believe there is an "auto open" feature that
runs a macro upon opening a sheet (or workbook, or whatever its called
now). Assuming this is true, your Excel sheet could automagically pull
in the new data upon opening. Worst case, you could have a button on
the sheet titled "Update Data", which would do the same thing.

Another possibility: On a PC that you _do_ control, use Excel macros to
automate the above process, saving the result as a regular Excel file
which can then be broadcast (perhaps via e-mail) to those who want it.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

###### ↳ ↳ ↳ Re: VMS COBOL and Excel spreadsheets

_(reply depth: 4)_

- **From:** "g. moore" <ua-author-16342207@usenetarchives.gap>
- **Date:** 1998-01-13T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p8@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p5@usenetarchives.gap> <gap-74df33a4ef-p6@usenetarchives.gap> <gap-74df33a4ef-p8@usenetarchives.gap>`

```

Tom Morrison wrote:
› 
› Bob Evans wrote:
…[43 more quoted lines elided]…
›› would probably turn off the PC overnight.
 
› Excel has an ODBC add-in that would allow you to write an Excel macro to
› use ODBC to pull the data from the COBOL files and Sybase tables.  While
…[4 more quoted lines elided]…
› the sheet titled "Update Data", which would do the same thing.

hmm, that sounds like the best option yet. maybe you should check out
the microsoft.com website under excel and see exactly what they have.

the problem is that excels macros may go so slow they tie up the
mainframe when up / downloading....

i believe the poster also asked to send the variables back at the end.

slight customization, especially a network buffer in the macro, should
take care of this problem...
```

###### ↳ ↳ ↳ Re: VMS COBOL and Excel spreadsheets

_(reply depth: 5)_

- **From:** "g. moore" <ua-author-16342207@usenetarchives.gap>
- **Date:** 1998-01-14T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-74df33a4ef-p9@usenetarchives.gap>`
- **References:** `<34B7B124.D85BA843@sprintmail.com> <gap-74df33a4ef-p5@usenetarchives.gap> <gap-74df33a4ef-p6@usenetarchives.gap> <gap-74df33a4ef-p8@usenetarchives.gap> <gap-74df33a4ef-p9@usenetarchives.gap>`

```

G. Moore wrote:

››››› Has anyone ever been able to create an Excel Spreadsheets using
››› VMS
››››› COBOL?

in all cases, that databridge product will save you about 50% of the
work.

you will still need a programmer to connect the ODBC specs to Excel,
and to keep track of what is done in case you want to add another
PC.
```

#### ↳ Re: VMS COBOL and Excel spreadsheets

- **From:** "joh..." <ua-author-14608346@usenetarchives.gap>
- **Date:** 1998-01-15T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-74df33a4ef-p11@usenetarchives.gap>`
- **In-Reply-To:** `<34B7B124.D85BA843@sprintmail.com>`
- **References:** `<34B7B124.D85BA843@sprintmail.com>`

```

Easysoft ODBC for RMS. We have thousands of clients accessing Cobol
data direct from spreadsheets. No programing required.

http://www/easysoft.com

On Sat, 10 Jan 1998 12:34:29 -0500, Bob Evans
wrote:

› Has anyone ever been able to create an Excel Spreadsheets using VMS COBOL?
› I know that I can create a text delimited import file into Excel, but I need to
› create an actual spreadsheet.
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
