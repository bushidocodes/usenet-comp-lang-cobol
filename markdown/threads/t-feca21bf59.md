[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# XML and Legacy

_26 messages · 15 participants · 2003-07_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future) · [`Web, XML, modern integration`](../topics.md#web)

---

### XML and Legacy

- **From:** FCEMBRANELLI <member32677@dbforums.com>
- **Date:** 2003-07-07T12:08:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3081306.1057579690@dbforums.com>`

```

Hi,

I need some suggestions about the following issue :

How can i generate Xml strings in Cobol in an adequate
format for load in Recordsets (ADO 2.6) ? Do i have to do
that manually or there is some easier way to create the
Xml ?

We are using CICS (Cobol) and Db2 database. We intend to
consume the Xml in ASP 3.0 with ADO recordsets.

[]'s

Felipe Cembranelli
```

#### ↳ Re: XML and Legacy

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-07T22:44:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f09f597.119633993@news.optonline.com>`
- **References:** `<3081306.1057579690@dbforums.com>`

```
FCEMBRANELLI <member32677@dbforums.com> wrote:

>
>Hi,
…[9 more quoted lines elided]…
>consume the Xml in ASP 3.0 with ADO recordsets.

Look at XML Thunder
http://www.canamsoftware.com/product/xml_thunder/index.html

It's a Cobol code generator whose code should compile on mainframe.

XML began as a data interchange language.Then people piggy-backed BAD
programming languages. For example  RRFW component of RRD, which uses Reverse
Polish Notation. That's not XML, that's an attempt to legitimize a bad language.
```

#### ↳ Re: XML and Legacy

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-07-07T17:19:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0307071619.30a9093f@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com>`

```
FCEMBRANELLI <member32677@dbforums.com> wrote

> How can i generate Xml strings in Cobol in an adequate
> format for load in Recordsets (ADO 2.6) ? Do i have to do
> that manually or there is some easier way to create the
> Xml ?

I generate XML using templating.  Actually the program neither knows
nor cares that it is XML, HTML, EDIFACT or printed report, that is the
nature of templating.

Given a set of data assign a name or code to each piece and sort out
which are the repeating groups.  Then have a text file containg the
format required (eg XML) with tags where the data is to be
substituted.  I use something like <!%name%> for the tags.  An XML
template may look like:

..
<product code="<!%pcode%>">
   <description><!%descrip%></description>
   <supplier code="<!%supplier%>">
       <suppdesc><!%suppdesc></suppdesc>
       <cost><!%suppcost%></cost>
   </supplier>
   ... 
</product>
Read in the template, for each line pick out the tags and substitute
the value. Repeat groups can be handled by dividing the template into
sections and repeating some sections, or by having tags that affect an
index and cause cycling.

<stock>
    <product code="<!%pcode%>">
<!%.s%><location bin="<!%bin%>"><!%count%>
       </location>
<!%+s%><!%!s%>
    </product>
</stock>
Here the '.s' tag sets the repeat point to be cycled.  The 's'
represent an index to a table in the program where there is also a
limit indicating the number of entries in the table.  The '+s' tag
indicates increment the s index.  The '!s" tag indicates comapre to
limit and if not reached repeat back to the cycle point.

It may take a bit of coding to get it right but then it can be used
for just about any output including HTML, printed forms, and the
template can be changed to suit whatever the program can output.

Making the template processor a separate program and having a table
relating the tag name to generalised data areas can make it even more
flexible.  Just set up the tables in a program, give it a template
name and get the output.
```

##### ↳ ↳ Re: XML and Legacy

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-08T01:25:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z4pOa.43586$0v4.2997905@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0307071619.30a9093f@posting.google.com...
| FCEMBRANELLI <member32677@dbforums.com> wrote
|
…[49 more quoted lines elided]…
| name and get the output.

Nice solution.

My first thought was use Report Writer, not as flexible though.
```

##### ↳ ↳ Re: XML and Legacy

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-08T21:06:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0a8a0e_3@news.athenanews.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com>`

```
As an adjunct to Richard's excellent solution...

I use exactly the same principle to generateDynamic HTML as well as XML
(which I am just getting into).

Have a "tagged skeleton" ("template" if you like...) with Form variable
Names in it (surrounded by a tag; mine is "//cobol//" so if there was a
variable called "descrip" it would appear in the skeleton as
"//cobol//descrip//cobol//"), pass a table of form variable Values to it and
execute the following code:

 IDENTIFICATION DIVISION.
 PROGRAM-ID. 'putHTML'.
*AUTHOR. Peter E. C. Dashwood.
*DATE_WRITTEN. February 2002..
*
* This program Takes an HTML Skeleton file containing COBOL variables and
* generates dynamic HTML by replacing the COBOL Variables and writing a
* new output HTML file called "dynamicHTML.asp".
*
* The output file will be picked up by using "Client pull". (The CGI Program
* which calls 'putHTML' will write a header that causes this.)
*
* Note that the output file may include Server Side Includes and so it
* has to be an ".STM" or ".ASP" file.
*
* INPUTS:
*
* 1. A name/value table containing the names and values of the COBOL
*    variables to be replaced.
*
*    For example:
*    //COBOL//a-variable//COBOL//
*
*    If "a-variable" is to contain "this is some text", then the
*    name/variable table will contain an entry with:
*    "a-variable" in the name and "this is some text" in the text.
*
* 2. The name of the HTML skeleton file which contains the COBOL Variables.
*    This can be a full path or just a filename if the skeleton is in the
same
*    directory on the server where the executing CGI program resides.
*
*    Be careful NOT to duplicate COBOL Variable names in this file...
*
* OUTPUTS:
*
* 1. A new .ASP file of "converted" HTML with the COBOL
*    variables replaced with their respective values.
*
 ENVIRONMENT DIVISION.
 configuration section.
 source-computer. IBM-PC.
 object-computer. IBM-PC.
 input-output section.
 file-control.
     select INFILE assign INFILE-NAME
                 organization is line sequential
                 access mode is sequential.
     select OUTFILE assign "dynHTML.asp"
                 organization is line sequential
                 access mode is sequential.

*------------------------  DATA   DIVISION  ---------------------
 DATA DIVISION.
 file section.
 FD   INFILE
                  LABEL RECORDS STANDARD
                  DATA RECORD is INPUT-RECORD.
 01   INPUT-RECORD               pic x(300).



 FD   OUTFILE
                  RECORD IS VARYING IN SIZE FROM 1 TO 300
                  DEPENDING ON OUTPUT-LEN
                  LABEL RECORDS STANDARD
                  DATA RECORD is OUTPUT-RECORD.
 01   OUTPUT-RECORD              pic x(300).

 WORKING-STORAGE SECTION.
 01  field-1 pic x(7).
 01  field-2 pic x(50).
 01  field-3 pic x(8).

 01  record-counts.
     12 in-count                 pic s9(9) comp-5.
     12 out-count                pic s9(9) comp-5.
     12 display-count            pic 9(9).

 01  end-flag                    pic x.
     88 not-finished             value zero.
     88 finished                 value '1'.

 01  in-work-chars.
     12 in-char pic x occurs 300
                      indexed by ic-x1.
 01  in-work redefines in-work-chars pic x(300).
 01  out-work.
     12 out-char pic x occurs 300
                      indexed by oc-x1.

 01  arithmetic-fields usage comp-5.
     12 INPUT-LEN  pic 9(3).
     12 OUTPUT-LEN        pic 9(3).
     12 IN-POS  pic s9(3).
     12 OUT-POS    pic s9(3).
     12 LEN   pic s9(3).
     12 NAME-START pic s9(3).
     12 ic-x1-n  pic s9(3).
     12 REMAINING-INPUT   pic s9(3).

 01  name-work  pic x(30).
 01  value-work  pic x(100).


 LINKAGE SECTION.
 01  name-value-table.
     12 nv-entry occurs 50
                    indexed by nv-x1.
        15 nv-name       pic x(30).
        15 nv-value      pic x(100).





* name of the HTML or XML Skeleton file...
 01  INFILE-NAME pic x(50).

 01  nv-result         pic x.
     88 nv-OK              value '0'.
     88 nv-name-not-found  value '1'.


 PROCEDURE DIVISION  USING    name-value-table
                              INFILE-NAME
                              nv-result.



* PROCEDURE DIVISION.
 MAIN SECTION.
 a000.
     perform startup-housekeeping
     perform main-logic until finished
     perform close-down
     .
 a999.
     exit program.
*-----------------------------------------------------------
 STARTUP-HOUSEKEEPING            section.
 sh000.

*
     open input INFILE
          output OUTFILE
     initialize record-counts
     set not-finished to TRUE
     set nv-OK to TRUE
     .
 sh999.
     exit.
*-----------------------------------------------------------
 MAIN-LOGIC                      section.
 ml000.
     read INFILE into in-work
        at end
           set finished to TRUE
           go to ml999
     end-read
     add 1 to in-count
     compute INPUT-LEN = function STORED-CHAR-LENGTH (in-work)
     move spaces to out-work
     move INPUT-LEN to OUTPUT-LEN
     set ic-x1 to 1
     set oc-x1 to 1
*
*   Check for COBOL Variables and convert...
*
     perform until ic-x1 > INPUT-LEN
        set IN-POS to ic-x1
        set ic-x1-n to ic-x1
        compute REMAINING-INPUT = INPUT-LEN - IN-POS + 1
        inspect in-work (IN-POS:REMAINING-INPUT)
           tallying ic-x1-n
                for characters before '//COBOL//'
        compute LEN = ic-x1-n - IN-POS
        set OUT-POS to oc-x1
        move in-work (IN-POS:LEN) to out-work (OUT-POS:)
*        add 1 to LEN
        set oc-x1 up by LEN
        set ic-x1 to ic-x1-n

        if ic-x1 NOT > INPUT-LEN
           set ic-x1 up by 9
* points to the COBOL Variable name...(1st position).
* extract the name to a work area for searching against the nv table...
           set NAME-START to ic-x1
           set ic-x1-n to ic-x1
           compute REMAINING-INPUT = INPUT-LEN - NAME-START + 1
           inspect in-work (NAME-START:REMAINING-INPUT)
             tallying ic-x1-n
               for characters before '//COBOL//'
           compute LEN = ic-x1-n - NAME-START
           set ic-x1 to ic-x1-n
           move spaces to name-work
           move in-work (NAME-START:LEN) to name-work
           set nv-x1 to 1
           search nv-entry
              at end
                 set nv-name-not-found to TRUE
                 move spaces to output-record
                 string
                   'Name not found during translate='
                      delimited by size
                   name-work
                      delimited by space
                         into output-record
                 end-string
                 write output-record
                 set finished to TRUE
                 set ic-x1 to 999
                 exit perform
              when
                  nv-name (nv-x1) = name-work
                     move nv-value (nv-x1) to value-work
           end-search
* get the length of the value for inserting to the output string...
           move zero to LEN
           inspect function reverse (value-work)
             tallying LEN
                for leading spaces
           compute LEN = 100 - LEN
           set OUT-POS to oc-x1
           move value-work (1:LEN) to out-work (OUT-POS:)
*           add 1 to LEN
           set oc-x1 up by LEN
* move input pointer over the second //COBOL// and recycle...
           set ic-x1 up by 9
        end-if
     end-perform
     if OUTPUT-LEN = zero
        move 1 to OUTPUT-LEN
     end-if
     if OUTPUT-LEN < oc-x1
        set OUTPUT-LEN to oc-x1
        add 1 to OUTPUT-LEN
     end-if

     write output-record from out-work
     add 1 to out-count
     .
 ml999.
     exit.
*----------------------------------------------------------
 CLOSE-DOWN                      section.
 cd000.
     close INFILE
           OUTFILE
*     move in-count to display-count
*     display "Records read    =" display-count
*     move out-count to display-count
*     display "Records written =" display-count
*     display space
*     display "END OF RUN"
     .
 cd999.
     exit.
*----------------    END OF PROGRAM 'putHTML' ----------------

The above code will read line sequential file (skeleton) records of up to
300 bytes, and translate the variables, expanding or shrinking the oputput
as necessary. Only the necessary length of the output is written.

It runs very fast and has proven very useful.

Pete.

<snip> of  description of Richard's very similar solution.
```

###### ↳ ↳ ↳ Re: XML and Legacy

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-07-08T12:57:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0307081157.4d4e6139@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote 

> I use exactly the same principle to generateDynamic HTML as well as XML
> (which I am just getting into).
…[5 more quoted lines elided]…
> execute the following code:

I was doing templating a couple of decade ago for laying out printed
forms.  It was important to keep columnar positioning even when fields
were small, so I had at that time used tags in the form %XX where each
tag only occupied 3 characters.  Substition was done until end of
value or finding a non-space in the template line.  This allowed
truncation rather than overwriting a field tag.

Moving this to HTML I decided to use <!%name%> as this is a comment in
HTML (not in XML) so if there was no 'name' field and substition
didn't take place it would be commented away.

> * This program Takes an HTML Skeleton file containing COBOL variables and
> * generates dynamic HTML by replacing the COBOL Variables and writing a
> * new output HTML file called "dynamicHTML.asp".

The actual output mechanism may vary, my code may write to a file or
display it for sending via the server, or print it, or all 3.

> * The output file will be picked up by using "Client pull". (The CGI Program
> * which calls 'putHTML' will write a header that causes this.)
>
> * Note that the output file may include Server Side Includes and so it
> * has to be an ".STM" or ".ASP" file.

I do my own 'server side includes' within the code as the template is
read into the template table.  This allows tags in the include file
too.

.ASP requires it to be MS server doesn't it?  I use my code with
Linux/Apache, Windows/Xitami, SCO/Netscape and it was originally
developed for OS/2/IBMServer (and then OS/2/Xitami).  There are only a
few trivial differences between all these.

> *    Be careful NOT to duplicate COBOL Variable names in this file...

That seems a strange limitation. I often have tags repeated to get,
say, the table heading also in the title.

>  MAIN-LOGIC                      section.
>  ml000.
…[3 more quoted lines elided]…
>            go to ml999
              ^^^^^^  <snigger!>
>      end-read

>      compute INPUT-LEN = function STORED-CHAR-LENGTH (in-work)

Let me guess - Fujitsu 4+ ?

[....]

>      write output-record from out-work

I pre-read the template file into a table of lines and process any
directives as I do so.  Generally I allow '#' in col 1 as a comment
line to be ignored, and '*' as a directive, so I have '*INCLUDE
filename' to bring in common file parts.  I also allow the template to
be subdivided using '*SUB name'.  As the template is read into the
table the subsection names are stored in another table with the line
numbers that apply - start and end.

The first call to the program reads the template and sets up the
tables. Subsequent calls to it will output one subsection by name
doing field substitution.  Subsections may be skipped or repeated as
required.

There would be a header and a trailer subsection, and then can be a
tablehead and tableend with a tablerow that may be output several
times, each with a different table of tag:value pairs.  There may be a
tablenone subsection which is only output when there will be no
tablerows to output.

This caters for repitition (or caters for it in one way - I have other
ways too).
```

###### ↳ ↳ ↳ Re: XML and Legacy

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-09T11:55:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0b5a9a_1@news.athenanews.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0307081157.4d4e6139@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> Moving this to HTML I decided to use <!%name%> as this is a comment in
> HTML (not in XML) so if there was no 'name' field and substition
> didn't take place it would be commented away.

That's a good idea.

I chose //COBOL// because Fujitsu have software that is supposed to process
this. It never worked for me, and that is why I wrote my own. (that is
another reason I posted the code here...there are probably people in the
forum who struck the same problems I did with processing dynamic HTML using
the Fujitsu standard software... This might help...)

>
> > * This program Takes an HTML Skeleton file containing COBOL variables
and
> > * generates dynamic HTML by replacing the COBOL Variables and writing a
> > * new output HTML file called "dynamicHTML.asp".
…[3 more quoted lines elided]…
>

Yes, it isn't to hard to modify the above to support this. I wrote this code
in an afternoon to solve a problem I was having with CGI programming and the
supplied Fujitsu software not working. It was never intended to be
comprehensive.

> > * The output file will be picked up by using "Client pull". (The CGI
Program
> > * which calls 'putHTML' will write a header that causes this.)
> >
> > * Note that the output file may include Server Side Includes and so it
> > * has to be an ".STM" or ".ASP" file.
>

> I do my own 'server side includes' within the code as the template is
> read into the template table.  This allows tags in the include file
> too.
>

I don't like re-inventing the wheel <G>. The Browser supports SSI so I use
it. (I don't think you're "wrong" for not doing so..<G>)

> .ASP requires it to be MS server doesn't it?

Yes, and that is the environment I was developing for. It is pretty easy to
make the output whatever you want it to be, depending on whatever you input
on the skeleton.


> I use my code with
> Linux/Apache, Windows/Xitami, SCO/Netscape and it was originally
> developed for OS/2/IBMServer (and then OS/2/Xitami).  There are only a
> few trivial differences between all these.
>

Good for you! As I noted above this was an "afternoon" solution intended for
a specific environment. It works and it is very easy to amend it for other
environments.

> > *    Be careful NOT to duplicate COBOL Variable names in this file...
>
> That seems a strange limitation. I often have tags repeated to get,
> say, the table heading also in the title.

Yes, that requirement is no longer true. (A classic case of the comments not
being updated <G>). I have several cases where skeletons contain multiple
copies of the same tag and they all function perfectly well, as you would
expect.
>
> >  MAIN-LOGIC                      section.
…[5 more quoted lines elided]…
>               ^^^^^^  <snigger!>

Gimme a break <G>!

> >      end-read
>
…[3 more quoted lines elided]…
>

You're not guessing and you are correct. For people not fortunate enough to
have the latest Fujitsu environment, you could replace this statement with
the "standard" INSPECT...REVERSED (there is an example of this lower down in
the code.)

<Snipped description that sounds really good>

Pete.
```

###### ↳ ↳ ↳ inspect reverse (was Re: XML and Legacy)

_(reply depth: 5)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-09T16:20:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bei4g7$4mqmb$1@ID-184804.news.dfncis.de>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com>`

```
Peter E.C. Dashwood<dashwood@enternet.co.nz> 07/08/03 05:55PM >>>
>You're not guessing and you are correct. For people not fortunate enough
to
>have the latest Fujitsu environment, you could replace this statement with
>the "standard" INSPECT...REVERSED (there is an example of this lower down
in
>the code.)

regarding your example:
inspect function reverse (value-work) tallying LEN for leading spaces

Quite useful, but I wish the new COBOL standard had this also:
inspect value-work tallying LEN for trailing spaces

It seems so obvious and useful that I have to wonder why it was missed.

Even nicer might be:
inspect value-work tallying LEN for all characters before trailing spaces

which would help you avoid:
compute LEN = length of value-work - LEN

Ah well...



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T10:38:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0c9a0b_4@news.athenanews.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:bei4g7$4mqmb$1@ID-184804.news.dfncis.de...
>
> regarding your example:
…[15 more quoted lines elided]…
>
Agree absolutely. These would be useful and logical extensions of COBOL.

The Fujitsu function  "function STORED-CHAR-LENGTH (in-work)" is also a
useful tool (but it does limit you to Fujitsu if you use it.)

Maybe one day we'll see all of these thngs as part of Standard COBOL...

"'Tis a consummation devoutly to be wished..."

Pete.


>
>
…[3 more quoted lines elided]…
> FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-07-09T23:19:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Up1Pa.14492$BM.4677381@newssrv26.news.prodigy.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3f0c9a0b_4@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f0c9a0b_4@news.athenanews.com...
>
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
…[4 more quoted lines elided]…
> > inspect value-work tallying LEN for all characters before trailing
spaces
>
> The Fujitsu function  "function STORED-CHAR-LENGTH (in-work)" is also a
…[4 more quoted lines elided]…
> "'Tis a consummation devoutly to be wished..."

And just what terminates the 'stored characters?' Space? 0x00 ??? Any
unprintable? Something you define in SPECIAL-NAMES?

COBOL's fixed size data buffers are designed to support trailing spaces
...in a fixed-length dataname...  it cannot simultaneously be designed to
support variable-length data. This is a classic, "defecate or relinquish
your seat upon the porcelain throne" deal.

Perahps what you'd really want is..........
01 FILLER
      05 in-work         USAGE STRING.
     .....

.. for variable-length data. Implementors could use any mechanism they
desire to, well, "implement" this.

Should probably add a companion function:

        MOVE FUNCTION STRING-LENGTH (usage-string-data-item) TO  foo....

MCM
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T12:34:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0cb5ad_8@news.athenanews.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3f0c9a0b_4@news.athenanews.com> <Up1Pa.14492$BM.4677381@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:Up1Pa.14492$BM.4677381@newssrv26.news.prodigy.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f0c9a0b_4@news.athenanews.com...
…[6 more quoted lines elided]…
>

Nope. Just the fact that there aren't any more of them.

Why complicate it?

> COBOL's fixed size data buffers are designed to support trailing spaces
> ...in a fixed-length dataname...  it cannot simultaneously be designed to
> support variable-length data.

It can't if you are rigid about what it can and cannot do.

I have no problem with using the function above. I know it is not the
ultimate "string handling" function you seem to be advocating, but it works
very well in the places where I have used it.


>This is a classic, "defecate or relinquish
> your seat upon the porcelain throne" deal.
>
Why? I never sat on the throne in the first place <G>? At no point have I
advocated this as the "ultimate solution". All I said was I find it useful.

> Perahps what you'd really want is..........

I don't really want ANYTHING more than I have already, Michael.

However, some of what is already available is NOT standard COBOL (You know
how much I really worry about the COBOL Standard...<G>)

> 01 FILLER
>       05 in-work         USAGE STRING.
…[8 more quoted lines elided]…
>

Yes, these facilities also would be useful.

(Remember to flush when you leave...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 8)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-07-11T11:28:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0307111028.3ed23ce2@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3f0c9a0b_4@news.athenanews.com> <Up1Pa.14492$BM.4677381@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<Up1Pa.14492$BM.4677381@newssrv26.news.prodigy.com>...

> Perahps what you'd really want is..........
> 01 FILLER
>       05 in-work         USAGE STRING.
>      .....

I believe at least part of this functionality is planned for the next
revision to the COBOL standard, though the current proposals do not
reflect the syntax suggested above.  Related, and also planned for the
next revision, is the ability to declare a true variable-size table
embedded in a record.

> .. for variable-length data. Implementors could use any mechanism they
> desire to, well, "implement" this.
…[4 more quoted lines elided]…
> 

If USAGE STRING were added to the standard (and/or WHEN similar or
equivalent functionality, regardless of what the syntax is, is added
to the standard), I'd expect FUNCTION LENGTH to reflect the current
length of such an item.  I'm not sure what having a *separate*
function for this would accomplish, given that FUNCTION LENGTH already
reflects the number of character positions the item named as argument
occupies.  Am I missing something?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-09T20:10:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beieen$v9q$1@slb6.atl.mindspring.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3f0c9a0b_4@news.athenanews.com>`

```
If you have (when you have?) a 2002 compliant compiler, it will be a "piece
of cake" to create such routines as EITHER user-defined functions OR
methods.  In fact, with "enhanced" REPLACE features, you probably could
"single source" code to be used as EITHER a method or a user-defined
function.

It wouldn't surprise me at all ASSUMING that there are 2002 compliant
compilers if some "bright" vendor didn't come up with an entire set of
"string handling" user-defined functions "for sale".
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 6)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-09T19:14:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0CB000.8070905@Netscape.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de>`

```
Frank Swarbrick wrote:
> regarding your example:
> inspect function reverse (value-work) tallying LEN for leading spaces
> 
> Quite useful, but I wish the new COBOL standard had this also:
> inspect value-work tallying LEN for trailing spaces
                                       ^^^^^^^^
This was removed in the COBOL 85 standard.  I'm not sure why - though 
"function reverse" works well too.

> Even nicer might be:
> inspect value-work tallying LEN for all characters before trailing spaces
> 
> which would help you avoid:
> compute LEN = length of value-work - LEN

One COBOL supports Function Stored-Char-Length (seems like I've seen 
that from PECD, so I'd bet it's Fujitsu that supports that).  That keeps 
you from doing the extra math too...
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-09T20:17:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beiesf$rdj$1@slb9.atl.mindspring.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net>`

```
What do you think was removed in the '85 Standard?

 Inspect ... TALLYING is definitely part of the '85 Standard. INSPECT ...
"for trailing" has never been a part of any ANSI/ISO COBOL Standard.  See my
separate note on what has and has not been "selected" for the next Standard
(trailing was CONSIDERED but not selected)
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 8)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-10T17:12:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0DE4B4.7060608@Netscape.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <beiesf$rdj$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:
> What do you think was removed in the '85 Standard?
> 
…[3 more quoted lines elided]…
> (trailing was CONSIDERED but not selected)

I guess I mis-assumed.  I could have sworn I saw it in our COBOL 74 
compiler, but didn't in COBOL 85.  However, I just looked it up in the 
COBOL 74 compiler, and it's not in there either.  My apologies to all...

(and why was trailing rejected?  It would be very handy, especially if 
you could say something like "Inspect data-name tallying count-var for 
characters before trailing space"  :> )
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 9)_

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-07-11T15:58:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<benbuu$71csc$2@ID-184804.news.uni-berlin.de>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <beiesf$rdj$1@slb9.atl.mindspring.net> <3F0DE4B4.7060608@Netscape.net>`

```
LX-i<LXi0007@Netscape.net> 07/10/03 04:12PM >>>
>William M. Klein wrote:
>> What do you think was removed in the '85 Standard?
>> 
>>  Inspect ... TALLYING is definitely part of the '85 Standard. INSPECT
...
>> "for trailing" has never been a part of any ANSI/ISO COBOL Standard.  See
my
>> separate note on what has and has not been "selected" for the next
Standard
>> (trailing was CONSIDERED but not selected)
>
…[6 more quoted lines elided]…
>characters before trailing space"  :> )

Hey, I already mentioned that one!  :-)

I guess the solution, sans the 'trailing' modifier, is to use something like
this:
INSPECT FUNCTION REVERSE(MY-STRING) FOR CHARACTERS AFTER LEADING SPACES

So given a MY-STRING PIC X(20) VALUE 'FRANK SWARBRICK     ' it would
interrogate '     KCIRBRAWS KNARF' and return a value of 15.  Wouldn't it? 
I didn't try it.  We only recently started using COBOL for VSE/ESA, which is
the VSE compiler than implements intrinsic functions, so I have not had
occasion to try this out yet.  Seems like it should work, though.  I think
it will be useful for my current project, in any case (which is why I had
mentioned the desire for 'before trailing spaces').

TTYL,



--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 10)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-12T09:33:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh0726og6humbc@corp.supernews.com>`
- **In-Reply-To:** `<benbuu$71csc$2@ID-184804.news.uni-berlin.de>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <beiesf$rdj$1@slb9.atl.mindspring.net> <3F0DE4B4.7060608@Netscape.net> <benbuu$71csc$2@ID-184804.news.uni-berlin.de>`

```
Frank Swarbrick wrote:
> I guess the solution, sans the 'trailing' modifier, is to use something like
> this:
> INSPECT FUNCTION REVERSE(MY-STRING) FOR CHARACTERS AFTER LEADING SPACES

That's a darn good idea - I'm going to try it.  I'll let you know what I 
find...  :)
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 7)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-07-10T09:20:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0307100820.4482edde@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net>`

```
LX-i <LXi0007@Netscape.net> wrote in message news:<3F0CB000.8070905@Netscape.net>...

> > Quite useful, but I wish the new COBOL standard had this also:
> > inspect value-work tallying LEN for trailing spaces
>                                        ^^^^^^^^
> This was removed in the COBOL 85 standard.  I'm not sure why - though 
> "function reverse" works well too.

I agree with Bill that this wasn't in the '85 standard, or the '02
standard.  In general, the COBOL standards folks don't treat adding
yet another way of accomplishing something that COBOL already does as
being of critical priority.

In the specific case of INSPECT, I don't see any functional
differences between the hypothetical
    INSPECT value-work 
        TALLYING trailing-spaces FOR TRAILING SPACES 
and the actual 
    INSPECT FUNCTION REVERSE (value-work) 
        TALLYING trailing-spaces FOR LEADING SPACES 
and, unless the implementor provides some sort of "backwards compare"
in the hardware, I don't see the potential for much of a performance
difference either.

To stretch a metaphor, having power driver's seat controls on the
driver's door, the steering wheel, the console and the remote alarm
pendant might be a really neat ergonomic idea, but it's not likely to
be given the attention that, say, a more efficient engine or a
side-curtain airbag would in terms of priority.

I know a number of people have proposed INSPECT <x> ... TRAILING ...,
and it remains on the candidates list for consideration for inclusion
in future revisions to the standard, but so far as I know nobody has
been able to come up with a case in which INSPECT FUNCTION REVERSE
(<x>) ... LEADING ..., or some simple sequence involving it, fails to
provide equivalent functionality.  And without such a case, what's the
point?   If anybody's confused about the FUNCTION REVERSE method,
comments have been around for a very long time in COBOL, and even
"inline" comments are now available.



the dCOBOL's basic power increased rather than  NEW FEATURES being
added rather than alternative ways of doing the same thing.
, and only microscopically-different resource consumption, 

    
> 
> > Even nicer might be:
…[19 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-10T12:11:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bek6nu$88$1@slb9.atl.mindspring.net>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <c60a0b82.0307100820.4482edde@posting.google.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:c60a0b82.0307100820.4482edde@posting.google.com...
> LX-i <LXi0007@Netscape.net> wrote in message
news:<3F0CB000.8070905@Netscape.net>...
>
<snip>
> I know a number of people have proposed INSPECT <x> ... TRAILING ...,
> and it remains on the candidates list for consideration for inclusion
…[8 more quoted lines elided]…
>

Chuck,
  Although I agree with you for INSPECT ... TALLYING, I am *not* certain
that in a "strictly conforming" '85 or '02 compiler that INSPECT ...
REPLACING will work (in a defined way) with FUNCTION REVERSE

I believe (but am not positive of this) that the REPLACING action would
impact the "temporary data item" created by the function and NOT the
original item itself - if it were allowed at all.  I think (but am still
uncertain about this) that SR(1) on page 90 of the 2002 Standard makes this
non-conforming when it says,

"1) A function-identifier shall not be specified as a receiving operand."

Notice that SR(8) on page 464 ONLY applies to Format 1 (no REPLACING phrase)
and that GR(1) does NOT say that identifier-1 *is* a sending operand, only
that it is treated as one FOR PURPOSES of determining the length.

It seems to me that the MOST common request is for "tallying" trailing
"spaces" (or whatever) but the ability to also REPLACE such characters is -
at least - questionable with the current FUNCTION REVERSE technique.
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T17:47:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bek8qk$i6i$1@peabody.colorado.edu>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <c60a0b82.0307100820.4482edde@posting.google.com> <bek6nu$88$1@slb9.atl.mindspring.net>`

```

On 10-Jul-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

>   Although I agree with you for INSPECT ... TALLYING, I am *not* certain
> that in a "strictly conforming" '85 or '02 compiler that INSPECT ...
> REPLACING will work (in a defined way) with FUNCTION REVERSE

However, once you know the tally, you can use reference modification to do a
move.
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 9)_

- **From:** charles.stevens@unisys.com (Chuck Stevens)
- **Date:** 2003-07-11T08:22:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c60a0b82.0307110722.50d9cd95@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <c60a0b82.0307100820.4482edde@posting.google.com> <bek6nu$88$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<bek6nu$88$1@slb9.atl.mindspring.net>...

> Chuck,
>   Although I agree with you for INSPECT ... TALLYING, I am *not* certain
…[10 more quoted lines elided]…
> 

Yes, I agree.  See below.  

> Notice that SR(8) on page 464 ONLY applies to Format 1 (no REPLACING phrase)
> and that GR(1) does NOT say that identifier-1 *is* a sending operand, only
> that it is treated as one FOR PURPOSES of determining the length.

Yes.  I'm not sure it matters to my point.  

> It seems to me that the MOST common request is for "tallying" trailing
> "spaces" (or whatever) but the ability to also REPLACE such characters is -
> at least - questionable with the current FUNCTION REVERSE technique.

True.  The request in this thread was for TALLYING, not REPLACING.  In
all honesty, I've never yet heard a convincing defense of a real
*practical need* for REPLACING TRAILING, much less the likes of
REPLACING TRAILING ... BEFORE INITIAL ... .   Using FUNCTION REVERSE
into a temporary (I suspect even an "in-place" replacement might be
legal -- the way the function's defined, it doesn't look to me like it
could be considered an overlap) used as the target of the INSPECT, and
then doing FUNCTION REVERSE again once the INSPECT is done, strikes me
as no less clear and, in the case of some of the more complex
"after-before-phrase" combinations, quite a bit clearer.

Of the several requests I've seen for this feature in INSPECT, each of
them seems to have been "driven" by the need for "INSPECT dataname
TALLYING tally-item FOR TRAILING SPACES"; every capability beyond that
seems to have been based on the desire for symmetry and elegance in
the syntax -- "now that we have TALLYING FOR TRAILING we really ought
to have REPLACING TRAILING, and mixing LEADING and TRAILING in the
same tallying-phrase, or among multiple TALLYING and REPLACING phrases
in the same INSPECT.

I haven't yet seen *anything useful* in the proposed syntax that
fundamentally enhances functionality beyond what can be done now, and
any complex example I can think of for the new syntax is arguably more
confusing and more error-prone than the current code.

To paraphrase a fifties-Jaguar-fanatic friend's comment about
Mercedes-Benz engineering during the fifties, INSPECT ... TRAILING
strikes me as a maximally complicated solution to a minimal problem. 
I think anything I'd *want* to do with TRAILING I can do with LEADING
and FUNCTION REVERSE.

I agree that INSPECT ... TALLYING ... FOR TRAILING SPACES would be
useful.  But I can do that now using FUNCTION REVERSE.

What else *useful* could you do with TRAILING that *can't* be done
with either (a) an "inline" FUNCTION REVERSE as the argument to the
INSPECT or (b) a pair of FUNCTION REVERSE calls, one before and one
after the INSPECT?  Would the TRAILING syntax actually be clearer?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: inspect reverse (was Re: XML and Legacy)

_(reply depth: 8)_

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2003-07-10T19:51:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ktjPa.23$ID.10@newssvr23.news.prodigy.com>`
- **References:** `<3081306.1057579690@dbforums.com> <217e491a.0307071619.30a9093f@posting.google.com> <3f0a8a0e_3@news.athenanews.com> <217e491a.0307081157.4d4e6139@posting.google.com> <3f0b5a9a_1@news.athenanews.com> <bei4g7$4mqmb$1@ID-184804.news.dfncis.de> <3F0CB000.8070905@Netscape.net> <c60a0b82.0307100820.4482edde@posting.google.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:c60a0b82.0307100820.4482edde@posting.google.com...
> LX-i <LXi0007@Netscape.net> wrote in message
news:<3F0CB000.8070905@Netscape.net>...
>
> > > Quite useful, but I wish the new COBOL standard had this also:
…[3 more quoted lines elided]…
> > "function reverse" works well too.
[snip]
> and, unless the implementor provides some sort of "backwards compare"
> in the hardware, I don't see the potential for much of a performance
> difference either.

Chuck, when you consider Bill's response to this post, you can see one
difference.

Quite obviously, one can generate reasonably good code for doing a "backward
compare" if the source language conveys the intent of the programmer;
hardware is not the problem.  Now one could optimize INSPECT FUNCTION
REVERSE as if it implied a mere reversal of the comparison/replacement
operations, but as Bill has pointed out, this has some danger.  I think that
a straightforward TRAILING makes a lot of sense, is sought by a lot of
programmers, is readable, and is not in the language because....well, I dare
not speculate.  ;-)

Consider the similarity of a MOVE with overlapping source and destination.
Now, if we assume that a programmer really wants to have a MOVE with
overlapping operands, then it should behave 'correctly' rather than
arbitrarily.  While not within the standard, a reasonable implementor will
determine in which 'direction' the operand has to be moved and adjust the
code generation accordingly.
```

#### ↳ Re: XML and Legacy

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-07T20:23:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307071923.4e8856eb@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com>`

```
As further follow up:

http://www-3.ibm.com/software/data/db2/extenders/xmlext/


FCEMBRANELLI <member32677@dbforums.com> wrote in message news:<3081306.1057579690@dbforums.com>...
> Hi,
> 
…[12 more quoted lines elided]…
> Felipe Cembranelli
```

#### ↳ Re: XML and Legacy

- **From:** hhinman <member30421@dbforums.com>
- **Date:** 2003-07-15T05:29:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3110837.1058247255@dbforums.com>`
- **References:** `<3081306.1057579690@dbforums.com>`

```

Here is an example of using .NET XML and streaming Classes in a Fujitsu
NetCOBOL for .NET that creates xml into a text file and then reads it
back in and formats it to display to the console:
-Howard

IDENTIFICATION  DIVISION.
       CLASS-ID. COBOLXML AS "COBOLXML.COBOLXML".
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
       REPOSITORY.
           CLASS XmlTextReader AS "System.Xml.XmlTextReader"
           CLASS XmlTextWriter AS "System.Xml.XmlTextWriter"
           ENUM FORMATTING AS "System.Xml.Formatting"
           PROPERTY PROP-FORMATTING AS "Formatting"
           PROPERTY PROP-INDENTED AS "Indented"
           PROPERTY PROP-NAME AS "Name"
           PROPERTY PROP-VALUE AS "Value"
           ENUM XmlNodeType AS "System.Xml.XmlNodeType"
           PROPERTY PROP-READ AS "Read"
           PROPERTY PROP-DEPTH AS "Depth"
           PROPERTY PROP-PREFIX AS "Prefix"
           PROPERTY PROP-ATTRIBUTECOUNT AS "AttributeCount"
           PROPERTY Attribute AS "Attribute"
           PROPERTY ProcessingInstruction AS "ProcessingInstruction"
           PROPERTY MoveToNextAttribute AS "MoveToNextAttribute"
           PROPERTY PROP-HASATTRIBUTES AS "HasAttributes"
           PROPERTY Element AS "Element"
           PROPERTY Whitespace AS "Whitespace"
           PROPERTY PROP-TEXT AS "Text".


       STATIC.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       PROCEDURE DIVISION.
       METHOD-ID. MAIN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 COBOLXMLOBJ OBJECT REFERENCE COBOLXML.
       01 DOCUMENT  PIC X(15) VALUE "newbooks.xml".
       01 JUNK PIC X VALUE SPACE.
       PROCEDURE DIVISION.
           INVOKE COBOLXML "NEW" RETURNING COBOLXMLOBJ.
           INVOKE COBOLXMLOBJ "Run" USING DOCUMENT.
           DISPLAY "Hit Enter To Quit".
           ACCEPT JUNK FROM CONSOLE.
       END METHOD MAIN.
       END STATIC.
       OBJECT.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       PROCEDURE DIVISION.

       METHOD-ID. Run.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MyXmlTextWriter OBJECT REFERENCE XmlTextWriter.
       01 MyXmlTextReader OBJECT REFERENCE XmlTextReader.
       01 BOOLEAN-TRUE  PIC 1 USAGE BIT VALUE B"1".
       01 BOOLEAN-FALSE PIC 1 USAGE BIT VALUE B"0".
       LINKAGE SECTION.
       01 args PIC X(15).
       PROCEDURE DIVISION USING args.
           INVOKE XmlTextWriter "NEW" USING args NULL RETURNING
           MyXmlTextWriter.

           SET PROP-FORMATTING OF MyXmlTextWriter TO PROP-INDENTED OF
           FORMATTING.
           INVOKE MyXmlTextWriter "WriteStartDocument" USING
           BOOLEAN-FALSE.
           INVOKE MyXmlTextWriter "WriteDocType" USING "bookstore",
           NULL, "books.dtd", NULL.
           INVOKE MyXmlTextWriter "WriteComment" USING "This file
           represents another fragment of a book store inventory
           database".
           INVOKE MyXmlTextWriter "WriteStartElement" USING "bookstore".
           INVOKE MyXmlTextWriter "WriteStartElement" USING
           "book", NULL.
           INVOKE MyXmlTextWriter "WriteAttributeString" USING "genre",
           "autobiography".
           INVOKE MyXmlTextWriter "WriteAttributeString" USING
           "publicationdate", "1979".
           INVOKE MyXmlTextWriter "WriteAttributeString" USING "ISBN",
           "0-7356-0562-9".
           INVOKE MyXmlTextWriter "WriteElementString" USING "title",
           NULL, "The Autobiography of Mark Twain".
           INVOKE MyXmlTextWriter "WriteStartElement" USING
           "Author", NULL.
           INVOKE MyXmlTextWriter "WriteElementString" USING
           "first-name", "Mark".
           INVOKE MyXmlTextWriter "WriteElementString" USING
           "last-name", "Twain".
           INVOKE MyXmlTextWriter "WriteEndElement".
           INVOKE MyXmlTextWriter "WriteElementString" USING
           "price", "7.99".
           INVOKE MyXmlTextWriter "WriteEndElement".
           INVOKE MyXmlTextWriter "WriteEndElement".

           INVOKE MyXmlTextWriter "Flush".
           INVOKE MyXmlTextWriter "Close".

           INVOKE XmlTextReader "NEW" USING args RETURNING
           MyXmlTextReader.
           INVOKE SELF "FormatXml" USING MyXmlTextReader args.
           DISPLAY SPACES.
           DISPLAY "Processing of the file ", args, " complete.".
           INVOKE MyXmlTextReader "Close".


       END METHOD Run.

       METHOD-ID. FormatXml.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 piCount         PIC 99 VALUE ZERO.
       01 docCount        PIC 99 VALUE ZERO.
       01 commentCount    PIC 99 VALUE ZERO.
       01 elementCount    PIC 99 VALUE ZERO.
       01 attributeCount  PIC 99 VALUE ZERO.
       01 textCount       PIC 99 VALUE ZERO.
       01 whitespaceCount PIC 99 VALUE ZERO.
       01 BOOLEAN-TRUE  PIC 1 USAGE BIT VALUE B"1".
       01 BOOLEAN-FALSE PIC 1 USAGE BIT VALUE B"0".
       01 BOOLEAN-RESULT PIC 1 USAGE BIT VALUE B"0".
       01 BOOLEAN-RESULT2 PIC 1 USAGE BIT VALUE B"0".
       LINKAGE SECTION.
       01 reader OBJECT REFERENCE XmlTextReader.
       01 filename PIC X(15).
       PROCEDURE DIVISION USING reader filename.
           INVOKE reader "Read" RETURNING BOOLEAN-RESULT2

           PERFORM WITH TEST BEFORE UNTIL BOOLEAN-RESULT2 =
           BOOLEAN-FALSE
               EVALUATE NodeType OF reader
                   WHEN ProcessingInstruction OF XmlNodeType
                       INVOKE SELF "CobFormat" USING reader
                       "ProcessingInstruction"
                       ADD 1 TO piCount

                    WHEN DocumentType OF XmlNodeType
                       INVOKE SELF "CobFormat" USING reader
                       "DocumentType"
                       ADD 1 TO docCount

                    WHEN Comment OF XmlNodeType
                       INVOKE SELF "CobFormat" USING reader "Comment"
                       ADD 1 TO commentCount

                    WHEN Element OF XmlNodeType
                       INVOKE SELF "CobFormat" USING reader "Element"
                       ADD 1 TO elementCount
                       MOVE BOOLEAN-TRUE TO BOOLEAN-RESULT
                       INVOKE reader "MoveToNextAttribute" RETURNING
                       BOOLEAN-RESULT
                       PERFORM UNTIL BOOLEAN-RESULT = BOOLEAN-FALSE
                           INVOKE SELF "CobFormat" USING reader
                           "Attribute"
                           INVOKE reader "MoveToNextAttribute" RETURNING
                           BOOLEAN-RESULT
                       END-PERFORM

                       SET BOOLEAN-RESULT TO PROP-HASATTRIBUTES OF
                       reader
                       IF BOOLEAN-RESULT = BOOLEAN-TRUE
                           ADD PROP-ATTRIBUTECOUNT OF reader TO
                           attributeCount
                       END-IF

                    WHEN PROP-TEXT OF XmlNodeType
                       INVOKE SELF "CobFormat" USING reader "Text"
                       ADD 1 TO textCount

                    WHEN Whitespace OF XmlNodeType
                       ADD 1 TO whitespaceCount

               END-EVALUATE
               INVOKE reader "Read" RETURNING BOOLEAN-RESULT2
           END-PERFORM.

           DISPLAY SPACES.
           DISPLAY "Statistics for {0} file", filename.
           DISPLAY SPACES.
           DISPLAY "ProcessingInstruction: ",  piCount.
           DISPLAY "DocumentType: ", docCount.
           DISPLAY "Comment: ", commentCount.
           DISPLAY "Element: ", elementCount.
           DISPLAY "Attribute: ", attributeCount.
           DISPLAY "Text: ", textCount.
           DISPLAY "Whitespace: ", whitespaceCount.
           EXIT METHOD.
       END METHOD FormatXml.

       METHOD-ID. CobFormat.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 MY-COUNT  PIC S9(9) COMP-5 VALUE 0.
       01 NUM1      PIC 9 VALUE ZERO.
       01 NUM2      PIC 9 VALUE ZERO.
       01 pPREFIX   PIC X(255) VALUE SPACES.
       01 pNAME     PIC X(255) VALUE SPACES.
       01 pVALUE    PIC X(255) VALUE SPACES.
       01 DISPLAY-STRING PIC X(81) VALUE SPACES.
       LINKAGE SECTION.
       01 reader OBJECT REFERENCE XmlTextReader.
       01 NodeType PIC X(65).
       PROCEDURE DIVISION USING reader NodeType.
           MOVE PROP-DEPTH OF reader TO NUM1.
           MOVE PROP-ATTRIBUTECOUNT OF reader TO NUM2.
           DISPLAY NUM1, " ", NUM2, " " WITH NO ADVANCING.
           MOVE PROP-DEPTH OF reader TO MY-COUNT.
           PERFORM MY-COUNT TIMES
               DISPLAY X"09" WITH NO ADVANCING
           END-PERFORM.
           SET pPREFIX TO PROP-PREFIX OF reader.
           SET pNAME TO PROP-NAME OF reader.
           SET pVALUE TO PROP-VALUE OF reader.
           MOVE ALL SPACES TO DISPLAY-STRING.
           STRING pPREFIX DELIMITED BY "   ",
                  NodeType DELIMITED BY SPACE,
                  "<",
                  pNAME DELIMITED BY "   ",
                  ">",
                  pVALUE DELIMITED BY "   "
             INTO DISPLAY-STRING.
           DISPLAY DISPLAY-STRING.
           EXIT METHOD.
       END METHOD CobFormat.
       END OBJECT.
       END CLASS COBOLXML.

Here is the text file it creates:

 <?xml version="1.0" standalone="no" ?>
  <!DOCTYPE bookstore (View Source for full doctype...)>
- <!-- This file represents another fragment of a book store
  inventory database
  -->
- <bookstore>
   - <book genre="autobiography" publicationdate="1979"
     ISBN="0-7356-0562-9">
     <title>The Autobiography of Mark Twain</title>
-    <Author>
       <first-name>Mark</first-name>
       <last-name>Twain</last-name>
      </Author>
     <price>7.99</price>
    </book>
  </bookstore>
```

#### ↳ Re: XML and Legacy

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-07-15T21:09:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0307152009.4f7274ae@posting.google.com>`
- **References:** `<3081306.1057579690@dbforums.com>`

```
FCEMBRANELLI <member32677@dbforums.com> wrote in message news:<3081306.1057579690@dbforums.com>...
> Hi,
> 
…[12 more quoted lines elided]…
> Felipe Cembranelli

Felipe, Since you are using ADO (2.6), I thought it to be appropriate
to also show you an ADO.NET approach to working with XML.

This ADO.NET approach to working with XML is not in contradiction to
the System.XML classes approach shown in Howards great post (found in
this same thread). It is simply another choice. There are some
situations where one or the other is a better fit. It's good to know
that .NET exposes many choices. I must mention that you can go "much
further" with XML using the System.XML classes (demonstrated in
Howard's post). Yet, at the same time, it does depend on how "far" you
need to go. There are times when the ADO.NET Dataset XML features will
take you "far enough" <grin>

Notice in the code sample below that the data is first loaded into a
ADO.NET Dataset. Then, the XML friendly functions exposed by the
ADO.NET Dataset are used. For those new to .NET, a Dataset is
basically a collection of Data Tables. A Data Table is much like the
ADO Recordset that you are using. An ADO.NET Dataset is both a
relational and a Hierarchical view of data - both at the same time.

000010* Sample Code demonstrating ADO.NET's support for XML Technology
000020 IDENTIFICATION DIVISION.
000030 PROGRAM-ID. MAIN.
000040 ENVIRONMENT DIVISION.
000050 CONFIGURATION SECTION.
000060 REPOSITORY.
000070* .NET Framework Classes
000080    CLASS SqlConnection  AS
"System.Data.SqlClient.SqlConnection"
000090     CLASS SqlDataAdapter As
"System.Data.SqlClient.SqlDataAdapter"
000100     CLASS SqlCommand As "System.Data.SqlClient.SqlCommand"
000110     CLASS DataSet    As "System.Data.DataSet"
000120     CLASS DataTable  AS "System.Data.DataTable"
000130     CLASS DataRow    As "System.Data.DataRow"
000140     CLASS DataColumn AS "System.Data.DataColumn"
000150     CLASS SystemType        AS "System.Type"
000160     CLASS DataColumnArray   AS "System.Data.DataColumn[]"
000170
000180     CLASS Sys-Integer      AS "System.Int32"
000190     CLASS Sys-String       AS "System.String"
000200     CLASS Sys-Object       AS "System.Object"    
000210
000220* .NET Framework Properties 
000230     PROPERTY PROP-ConnectionString AS "ConnectionString"
000240     PROPERTY PROP-Connection       AS "Connection"
000250     PROPERTY PROP-CommandText      AS "CommandText"
000260     PROPERTY PROP-SelectCommand    AS "SelectCommand"
000270     PROPERTY PROP-Columns          AS "Columns"
000280     PROPERTY PROP-Tables           AS "Tables"
000290     PROPERTY PROP-DataType         AS "DataType"
000300     PROPERTY PROP-ColumnName       AS "ColumnName"
000310     PROPERTY PROP-Item             AS "Item"
000320     PROPERTY PROP-PrimaryKey       AS "PrimaryKey"
000330     PROPERTY PROP-Unique           AS "Unique"
000340     PROPERTY PROP-IgnoreSchema     AS "IgnoreSchema"
000350
000360* .NET Framework Enumerations 
000370     ENUM     ENUM-XmlWriteMode     AS
"System.Data.XmlWriteMode".
000380
000390 DATA DIVISION.
000400 WORKING-STORAGE SECTION.
000410   77 mySqlConnection   OBJECT REFERENCE SqlConnection.
000420   77 mySqlDataAdapter  OBJECT REFERENCE SqlDataAdapter.
000430   77 mySqlCommand      OBJECT REFERENCE SqlCommand.
000440   77 myDataSet1        OBJECT REFERENCE DataSet.
000450   77 myDataSet2        OBJECT REFERENCE DataSet.
000460   77 myDataTable       OBJECT REFERENCE DataTable.
000470   77 myDataColumn      OBJECT REFERENCE DataColumn.
000480   77 myPrimaryKeyColumn  OBJECT REFERENCE DataColumn.
000490   77 myPrimaryKeyColumns OBJECT REFERENCE DataColumnArray.
000500   77 myENUM-XmlWriteMode OBJECT REFERENCE ENUM-XmlWriteMode.
000510
000520   77 mySys-String  OBJECT REFERENCE Sys-String.
000530   77 mySys-Integer OBJECT REFERENCE Sys-Integer.
000540   77 mySys-Object  OBJECT REFERENCE Sys-Object.
000550   77 myXmlFile     OBJECT REFERENCE Sys-String.
000560   77 myDisplayString PIC x(38550).
000570   77 myInt           PIC S9(9) COMP-5.
000580   77 myOtherInt      PIC S9(9) COMP-5.
000590   01 NULL-X          PIC X(1).
000600 PROCEDURE DIVISION.
000610
000620     Perform 0000-OptionalPreTableBuild.
000630    Perform 1000-UseSqlDataAdapter.
000640     Perform 2000-ReadWriteXML.
000650     DISPLAY " "
000660     
000670     DISPLAY "Enter X and Press Enter to Exit.".
000680     ACCEPT NULL-X.
000690     Stop Run.
000700     
000710************************************************
000720   0000-OptionalPreTableBuild.
000730*  It is possible to obtain the "schema" or table structure
000740*  directly/automatically from the SQL Server Database
000750*  This section is added for training purposes.
000760*  The information found in this section would be critical
000770*  in the case of building a disconnected .NET dataset
000780*  that may have a non-SQL Server Data Source.
000790
000800* Create a new DataTable.
000810     INVOKE DataTable "NEW" USING BY VALUE "myCustomers"
000820         RETURNING myDataTable.
000830
000840* Create 1st myDataColumn.
000850     INVOKE DataColumn "NEW" RETURNING myDataColumn.
000860     SET PROP-DataType OF myDataColumn TO
000870         SystemType::"GetType"("System.String").
000880     SET PROP-ColumnName OF myDataColumn TO "CustomerID".
000890     SET PROP-Unique OF myDataColumn TO B"1".
000900     INVOKE PROP-Columns OF myDataTable "Add" 
000910       USING BY VALUE myDataColumn.
000920     
000930* Create 2nd myDataColumn.
000940     INVOKE DataColumn "NEW" RETURNING myDataColumn.
000950     SET PROP-DataType OF myDataColumn TO
000960         SystemType::"GetType"("System.String").
000970     SET PROP-ColumnName OF myDataColumn TO "CompanyName".
000980     INVOKE PROP-Columns OF myDataTable "Add" 
000990       USING BY VALUE myDataColumn.
001000     
001010* Create 3rd myDataColumn.
001020     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001030     SET PROP-DataType OF myDataColumn TO
001040         SystemType::"GetType"("System.String").
001050     SET PROP-ColumnName OF myDataColumn TO "ContactName".
001060     INVOKE PROP-Columns OF myDataTable "Add" 
001070       USING BY VALUE myDataColumn.
001080     
001090* Create 4th myDataColumn.
001100     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001110     SET PROP-DataType OF myDataColumn TO
001120         SystemType::"GetType"("System.String").
001130     SET PROP-ColumnName OF myDataColumn TO "ContactTitle".
001140     INVOKE PROP-Columns OF myDataTable "Add" 
001150       USING BY VALUE myDataColumn.
001160     
001170* Create 5th myDataColumn.
001180     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001190     SET PROP-DataType OF myDataColumn TO
001200         SystemType::"GetType"("System.String").
001210     SET PROP-ColumnName OF myDataColumn TO "Address".
001220     INVOKE PROP-Columns OF myDataTable "Add" 
001230       USING BY VALUE myDataColumn.
001240     
001250* Create 6th myDataColumn.
001260     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001270     SET PROP-DataType OF myDataColumn TO
001280         SystemType::"GetType"("System.String").
001290     SET PROP-ColumnName OF myDataColumn TO "City".
001300     INVOKE PROP-Columns OF myDataTable "Add" 
001310       USING BY VALUE myDataColumn.
001320     
001330* Create 7th myDataColumn.
001340     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001350     SET PROP-DataType OF myDataColumn TO
001360         SystemType::"GetType"("System.String").
001370     SET PROP-ColumnName OF myDataColumn TO "Region".
001380     INVOKE PROP-Columns OF myDataTable "Add" 
001390       USING BY VALUE myDataColumn.
001400     
001410* Create 8th myDataColumn.
001420     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001430     SET PROP-DataType OF myDataColumn TO
001440         SystemType::"GetType"("System.String").
001450     SET PROP-ColumnName OF myDataColumn TO "PostalCode".
001460     INVOKE PROP-Columns OF myDataTable "Add" 
001470       USING BY VALUE myDataColumn.
001480     
001490* Create 9th myDataColumn.
001500     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001510     SET PROP-DataType OF myDataColumn TO
001520         SystemType::"GetType"("System.String").
001530     SET PROP-ColumnName OF myDataColumn TO "Country".
001540     INVOKE PROP-Columns OF myDataTable "Add" 
001550       USING BY VALUE myDataColumn.
001560     
001570* Create 10th myDataColumn.
001580     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001590     SET PROP-DataType OF myDataColumn TO
001600         SystemType::"GetType"("System.String").
001610     SET PROP-ColumnName OF myDataColumn TO "Phone".
001620     INVOKE PROP-Columns OF myDataTable "Add" 
001630       USING BY VALUE myDataColumn.
001640      
001650* Create 11th myDataColumn.
001660     INVOKE DataColumn "NEW" RETURNING myDataColumn.
001670     SET PROP-DataType OF myDataColumn TO
001680         SystemType::"GetType"("System.String").
001690     SET PROP-ColumnName OF myDataColumn TO "Fax".
001700     INVOKE PROP-Columns OF myDataTable "Add" 
001710       USING BY VALUE myDataColumn.
001720     
001730* Assign primary key column to "CustomerID" column.
001740     INVOKE DataColumnArray "NEW" USING BY VALUE 1
001750         RETURNING myPrimaryKeyColumns.
001760     INVOKE PROP-Columns OF myDataTable "get_Item" 
001770       USING BY VALUE "CustomerID"
001780       RETURNING myPrimaryKeyColumn.
001790     INVOKE myPrimaryKeyColumns "Set" 
001800       USING BY VALUE 0 myPrimaryKeyColumn.
001810     SET PROP-PrimaryKey OF myDataTable TO myPrimaryKeyColumns.
001820     
001830* Reference the DataSet.
001840     INVOKE DataSet "NEW" RETURNING myDataSet1.
001850* Associate the Table with the Dataset.
001860     INVOKE PROP-Tables OF myDataSet1 "Add" 
001870       USING BY VALUE myDataTable.
001880
001890************************************************
001900   1000-UseSqlDataAdapter.
001910   
001920*  Reference Data Provider Objects
001930  INVOKE SqlConnection "NEW"  RETURNING  mySqlConnection 
001940      INVOKE SqlDataAdapter "NEW" RETURNING  mySqlDataAdapter 
001950      INVOKE SqlCommand "NEW"     RETURNING  mySqlCommand
001960      
001970*  Prepare to Connect to SQL Server Database
001980*  using Connection String
001990      SET PROP-ConnectionString OF mySqlConnection TO
002000      "user id=sa;pwd=;Database=northwind;Server=(LOCAL)"
002010  
002020*  Associate the Command Object with the Connection Object
002030      SET PROP-Connection OF mySqlCommand TO mySqlConnection    
002040*  Associate the Command Object with intended SQL Statement
002050      SET PROP-CommandText OF mySqlCommand TO "Select * from
Customers"
002060*  Associate the DataAdapter Object with the Command Object
002070      SET PROP-SelectCommand OF mySqlDataAdapter TO mySqlCommand
002080
002090*  Have the DataAdapter Object Execute the SQL Statement and
002100*  store the result set in a DataSet DataTable named myCustomers
002110     INVOKE mySqlDataAdapter "Fill" 
002120       USING BY VALUE myDataSet1, "myCustomers"
002130
002140*  Close the Database Connection
002150      INVOKE mySqlConnection "Close".
002160      
002170      SET mySqlConnection TO NULL.
002180      SET mySqlDataAdapter TO NULL.
002190      SET mySqlCommand TO NULL.
002200      SET myDataTable TO NULL.
002210
002220************************************************
002230   2000-ReadWriteXML.
002240   
002250*  The following XML file will be saved on your harddisk.
002260*  You can locate it in the local application BIN folder
002270      SET myXmlFile TO "myCustomers.xml"
002280   
002290*  Demonstrate the usage of the WriteXml method
002300*  Write out an XML file that originated as relational data
002310      SET myENUM-XmlWriteMode 
002320     TO PROP-IgnoreSchema OF ENUM-XmlWriteMode
002330      INVOKE myDataSet1 "WriteXml" USING BY VALUE 
002340       myXmlFile, myENUM-XmlWriteMode
002350 
002360*  Demonstrate the usage of the ReadXml method
002370*  Load a 2nd Dataset from the saved XML file
002380  INVOKE DataSet "NEW" RETURNING myDataSet2
002390      INVOKE myDataSet2 "ReadXml" USING BY VALUE myXmlFile
002400 
002410*  Demonstrate the usage of the GETXML method
002420*  Extract data from the Dataset in XML format
002430     INVOKE myDataSet2 "GetXml" RETURNING mySys-String
002440     SET myDisplayString TO mySys-String
002450     DISPLAY myDisplayString.
002460     
002470 END PROGRAM MAIN.


Note: The code sample above was borrowed from my book ("COBOL and
Visual
Basic on .NET: A Guide for the Reformed Mainframe Programmer". 
Chapter 12). By the way, this same source code is downloadable from
the Apress site
(http://www.apress.com/book/supplementDownload.html?bID=112&sID=956).


- regards.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
