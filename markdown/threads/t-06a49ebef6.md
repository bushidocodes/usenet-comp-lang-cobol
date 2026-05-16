[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Best Practices - Cobol. Part 2.

_8 messages · 4 participants · 2003-02_

---

### Best Practices - Cobol. Part 2.

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-07T21:01:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e441e92.170760373@news.optonline.net>`

```
Best Practices - Cobol
Robert Wagner
[saved as plain text]

Chapter 12

Demo program

Suppose you are a new-hire in a smallish Cobol shop, placed in charge
of an existing system. The first thing you want to do is assess the
scope of your responsibility. That requires taking an inventory of
production programs. Hopefully your predecessor distinguished
production from one-time and occasional-use programs. If not, you will
have to devise a tool that logs every program executed, with first and
last date and number of times run. If the shop is Unix and Micro
Focus, this can be done easily by writing a script named COBRUN in
your home directory and making it first in everyone's PATH.

After you have isolated the production set, you will want an inventory
of which programs access which files, and whether they read or update
the files. That's what this Demo program does. It parses Cobol source
code and produces a report showing the relationships between programs
and files. Don't be surprised to find programs defining files they
never open and files they open but never access, thanks to
cut-and-paste coding, and files thet open for update but never update.
This is all superfluous code that you'll want to eliminate.

I developed this in one day under Micro Focus running on Sun Solaris,
then ported it with many changes to the free Fujitsu compiler running
on Windows, which took two days.

The Fujitsu Experience

The good

* Pointers and the Set verb work exactly the same as IBM and Micro
Focus. This is not documented. Ignore documentation about 'based'
structures. The syntax in the demo program is industry-standard.

* Documentation incorrectly says file name must be 8.3 DOS format.
File name may be any size, and may be preceded by path.

The bad

* Program sometimes abends when setting a structure pointer to null,
sometimes not. See the main loop in analysis-function for an example.
Stepping through words works, but stepping through lines abends when
pointer is set to null at the end.

* Program always abends on variable length structures (with length
inside). As a result, your program must waste memory by allocating the
maximum size.

* Method of allocating/freeing memory is not documented. See
malloc.cbl and mfree.cbl for code which does it. Fujitsu does not
document any system calls.

* Open extend does not work on ASCII (line sequential) files. Other
compilers do not have this problem.

* Cannot read softcopy documentation because the Common Ground reader
program on the CD is corrupt. There are pdf files on the CD which
comes with Teach Yourself Cobol in 24 Hours.

The ugly

* When calling system functions (statically bound) the program must be
in upper case and options NODLOAD and NOALPHA (program all upper case)
must be used. As a result, system calls must be in a separately
compiled dll. Other compilers do not require that.

* To get rid of annoying environment window, set envsetwindow to UNUSE
and save it.

* The demo requires a list of files to analyze. It is inconvenient to
get that list programmatically because system functions
FindFirst/FindNext are not documented, and would be difficult to
reverse engineer. Use pfdir.bat to build the list. Under Unix, I did
it with one line of code, which called 'SYSTEM' with an 'ls' command.

* Fujitsu requires identification division/program-id and will not
accept two-character program names. The Standard says program-id is
not required, program name is source file name, and puts no lower
limit on size of name.

* When using free-form, Fujitsu will not accept * in position 1 as a
comment. One must use *> The Standard says * should work. Perhaps
'variable format' would work as expected. I didn't try that option.

The Demo program reads your source code and produces a report
(progfile.txt) showing how each application program accesses files. It
actually works. Note how program-function processes *one* program and
line-function processes one line. This non-trivial program was written
as a tutorial in the use of telescoping program structure, linked
lists and good programming style.

All this code, except malloc and mfree, has been packaged as a single
source file, as described in chapter 6. It is one program with a
'main' and five functions. Placement of the 'end program' lines is
important. Yes, the program can analyze on its own source.

To compile with Fujitsu, go to Programming Staff, Tools, compiler, set
options to DLOAD, NOMAIN, APOST and SRF(FREE,FREE). Next go to linker,
input is pf2.obj, output pf2.exe. When linking malloc and mfree,
specify dll.

Before running pf2, run 'pfdir \targetdir' to construct a list of
programs to analyze. Pfdir.bat reads:

rem builds a list of source files for pf1
rem run this with directory as param e.g. pfdir ..\programs
echo %1\ >pffiles
dir/b %1\*.cbl >>pffiles
dir/b %1\*.cob >>pffiles

First we design dynamically allocated data structures -- linked list
entries -- which will be used by all programs and store them in a
Cobol 'copybook' named pfstruc.cpy.

*> Basic structures used by pf programs.
*> Occurs depending commented out because Fujitsu fails on variable length
*> structures

 01  root-variables.
     05  pf-return-code comp-5 pic s9(02).
         88  no-error           value 0.
         88  any-error          value 1 thru 99.
         88  application-error  value 20 thru 49.
         88  fatal-error                value 50 thru 99.
         88  end-of-file                value 10.
         88  end-of-all-files   value 11.
         88  i-give-up          value 20.
         88  file-open-error    value 23.
         88  no-file-selected   value 24.
         88  malloc-error       value 50.
     05  file-status                    pic  9(02).
     05  record-length          comp-5 pic s9(04).
     05  allocation-length      comp-5 pic s9(09).
     05  allocation-pointer     pointer.
     05  program-count  comp-5 pic s9(09).
     05  first-program          pointer.
     05  last-program           pointer.

 01  program-entry.
     05  program-length comp-5 pic s9(04).
     05  fixed-portion.
         10  previous-program   pointer.
         10  next-program       pointer.
         10  program-number     comp-5 pic s9(09).
         10  program-reporting-error   pic  x(08).
         10  line-count         comp-5 pic s9(09).
         10  program-name.
             15  program-name-byte occurs 64 pic x.
         10  previous-last-line pointer.
         10  first-file         pointer.
         10  last-file          pointer.
         10  first-line         pointer.
         10  last-line          pointer.
     05  path-file.
         10  path-file-byte occurs      256                             pic x.
*>       10  path-file-byte occurs 1 to 256 depending on program-length pic x.

 01  line-entry.
     05  line-length            comp-5 pic s9(04).
     05  fixed-portion.
         10  previous-line      pointer.
         10  next-line          pointer.
         10  line-number        comp-5 pic s9(09).
         10  word-count         comp-5 pic s9(04).
         10  first-word         pointer.
         10  last-word          pointer.
     05  line-text.
         10  line-byte occurs      256                          pic x.
*>       10  line-byte occurs 1 to 256 depending on line-length pic x.

 01  word-entry.
     05  word-length            comp-5 pic s9(04).
     05  fixed-portion.
         10  previous-word      pointer.
         10  next-word          pointer.
         10  word-number        comp-5 pic s9(04).
         10  word-col-from      comp-5 pic s9(04).
         10  word-col-to                comp-5 pic s9(04).
         10  word-trailing-spaces comp-5 pic s9(04).
     05  word-text.
         10  word-byte occurs      300                          pic x.
*>       10  word-byte occurs 1 to 300 depending on word-length pic x.

 01  file-entry.
     05  file-length            comp-5 pic s9(04).
     05  fixed-portion.
         10  previous-file            pointer.
         10  next-file                   pointer.
         10  file-select                 pointer.
         10  file-name                 pointer.
         10  file-organization     pointer.
         10  file-record               pointer.
         10  file-open-mode        pointer.
         10  file-read                   pointer.
         10  file-write                  pointer.


Now we write the top-level code.

@OPTIONS MAIN
@OPTIONS SRF(FREE,FREE)
 identification division.
 program-id. pf2.
*>author: Robert Wagner
*>  Inventory of programs and files,
*>   showing which programs read and write each file.
*>  This is the main function of the of process.
*>
*>  Speed: 150 programs containing 88K lines, 3M bytes
*>    Compiled with Micro Focus, run on 450 MHz 1-processor Sun Ultra 10 SPARC
*>        8 seconds, 50 milliseconds per program
*>    Compiled with Fujitsu 32-bit, run on 500 MHz Pentium 3
*>        12 seconds, 80 milliseconds per program
*>                      runs 30 seconds if search all is changed to search
*>
*>  structure:
*>  pf2                                 this
*>   program-function    constructs program entry, calls others
*>     word-function     constructs word entries, parser
*>      line-function    constructs line entries, reads input source code
*>     analysis-function constructs file entries, analyzer
*>     output-function   writes output file
*>       malloc                 allocates memory (dynamic)
*>       mfree                  deallocates memory (dynamic)
*>
 data division.
 working-storage section.
 01  unqualified-variables.
     05  allocation-length-local     comp-5   pic s9(09).
     05  allocation-pointer-local    pointer.

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division.
 main.
     move low-values to unqualified-variables
     perform construct-root-variables

     perform until end-of-all-files or fatal-error
         call 'program-function' using root-variables
     end-perform

     perform destroy-variables
     goback.

 construct-root-variables.
     move length of root-variables to allocation-length-local
     call 'malloc' using allocation-length-local, allocation-pointer-local
     if  allocation-pointer-local equal to null
         display 'pf error constructing root ' return-code
         goback
     end-if
     set address of root-variables to allocation-pointer-local
     move low-values to root-variables.
 destroy-variables.
     call 'mfree' using root-variables.


This is the manager-level code to process one source program.

 identification division.
 program-id. program-function.
*>author:. Robert Wagner
*>  Process one program
*>  reads pffiles to get the name of the program
*>  constructs program structure
*>  calls word-function and line-function to fill words and lines
*>  calls analysis-function to construct file entries
*>  calls output-function to write out file entries
*>  destroys a program's child structures -- words, lines, files
*>  destroys program structure
*>
 environment division.
 input-output section.
 file-control.
    select list-file assign to 'pffiles'
        organization is line sequential
         file status is file-status.

 data division.
 file section.
 fd  list-file.
 01  list-record.
     05  list-byte occurs 1 to 256 depending on filename-length pic x.

 working-storage section.
 01  persistent-variables.
     05  filler value low-value        pic  x(01).
         88  list-open value 'o'.
         88  list-closed value low-value.
     05  path-length            comp-5 pic s9(04).
 01  unqualified-variables.
     05 filename-length         comp-5 pic s9(04).
     05 n                       comp-5 pic s9(04).
     05 n1                      comp-5 pic s9(04).
     05 n2                      comp-5 pic s9(04).
     05 filler                         pic  x(01).
        88  end-of-lines value 'e'.
 01  hold-path.
     05  filler occurs 1 to 256 depending on path-length pic x.

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables.
 main.
     move low-values to unqualified-variables
     set no-error to true
     if  list-closed
         open input list-file
         if  file-status not equal to zero
             display 'error ' file-status ' opening pffiles'
             move file-status to pf-return-code
             goback
         end-if
         set list-open to true
         perform read-list
         move filename-length to path-length
         move list-record to hold-path
     end-if

     perform read-list
     perform construct-program

     perform until end-of-file or any-error
         call 'word-function' using root-variables, program-entry
     end-perform

     if  not end-of-file
         display 'error ' pf-return-code
         goback
     end-if

     set no-error to true
     call 'analysis-function'   using root-variables, program-entry
     call 'output-function' using root-variables, program-entry

     perform destroy-program-children

     goback.

 construct-program.
     compute allocation-length =
         length of fixed-portion of program-entry + 2 +
         path-length + filename-length
     compute allocation-length = length of program-entry *> Fujitsu
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf error constructing program ' return-code
         goback
     end-if
     if  first-program equal to null
         set first-program to allocation-pointer
     else
         set address of program-entry to last-program
         set next-program to allocation-pointer
     end-if
     set address of program-entry to allocation-pointer
     compute program-length = path-length + filename-length
     move low-values to fixed-portion of program-entry
     move last-program to previous-program
     move allocation-pointer to last-program
     add 1 to program-count
     move program-count to program-number
     move spaces to program-name
     perform varying n1 from filename-length by -1
         until n1 equal to zero or list-byte (n1) equal to '\'
         continue
     end-perform
     add 1 to n1
     move 1 to n2
     perform until list-byte (n1) equal to '.' or
         n1 greater than filename-length or n2 greater than 64
         move list-byte (n1) to program-name-byte (n2)
         add 1 to n1
         add 1 to n2
     end-perform
     move spaces to path-file
     string hold-path list-record delimited by size into path-file.

 destroy-program-children.
*> To prevent fragmentation, resources such as memory and files
*> should be released *> in the reverse order they were acquired.
     set address of file-entry to last-file
     perform until address of file-entry equal to null
         set allocation-pointer to previous-file
         call 'mfree' using file-entry
         set address of file-entry to allocation-pointer
     end-perform
     set first-file, last-file to null

     set address of line-entry to last-line
     perform until end-of-lines
         set address of word-entry to last-word
         perform until address of word-entry equal to null
             set allocation-pointer to previous-word
             call 'mfree' using word-entry
             set address of word-entry to allocation-pointer
         end-perform
         set allocation-pointer to previous-line
         call 'mfree' using line-entry
         if  allocation-pointer equal to null
             set end-of-lines to true
         else
             set address of line-entry to allocation-pointer
         end-if
     end-perform
     set first-line, last-line to null

     call 'mfree' using program-entry
     set first-program, last-program to null.

 read-list.
     move 256 to filename-length
     read list-file at end
         set end-of-all-files to true
         close list-file
         set list-closed to true
         goback
     end-read
     perform varying filename-length from 256 by -1
         until filename-length equal to zero or
               list-byte (filename-length) not equal to space
         continue
     end-perform.


A parser to extract the words on a line.

 identification division.
 program-id. word-function.
*>author. Robert Wagner.
*>  Parser. Constructs word entries.

 data division.
 working-storage section.
 01  unqualified-variables.
     05  n                    comp-5 pic s9(04).
     05  n1                   comp-5 pic s9(04).
     05  n2                   comp-5 pic s9(04).
     05  filler                      pic  x(01).
         88  in-a-word value 'w'.
         88 not-in-a-word value low-value.
     05  filler                      pic  x(01).
         88  cobol-character value 'c'.
         88  not-cobol-character value low-value.
     05  quote-character             pic  x(01).
     05  a-byte                      pic  x(01).
     05  lookahead-1                 pic  x(01).
     05  lookahead-2                 pic  x(01).

 01  a-word-area.
     05  a-word-length          comp-5 pic s9(04).
     05  a-word-col-from        comp-5 pic s9(04).
     05  a-word-col-to          comp-5 pic s9(04).
     05  a-word.
         10  a-word-byte occurs 1 to 300 depending on a-word-length pic x.

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables, program-entry.
 main.
     call 'line-function' using root-variables, program-entry
     if  any-error or last-line equal to previous-last-line
         goback
     end-if
     move low-values to unqualified-variables
     set address of line-entry to last-line
     set previous-last-line to last-line
     set address of word-entry to null

     perform varying n from 1 by 1 until n greater than line-length
*> process one byte
         move line-byte (n) to a-byte  *> for speed
         perform look-ahead
         if  (a-byte not less than 'a' and not greater than 'z') or
             (a-byte not less than 'A' and not greater than 'Z') or
             (a-byte not less than '0' and not greater than '9') or
             (a-byte equal to '-')
             set cobol-character to true
         else
             set not-cobol-character to true
         end-if
*> test whether this byte terminates the previous word
*> and  whether this byte begins or ends a quoted string
         if  not-cobol-character and quote-character equal to low-value
             if  in-a-word
                 perform end-word
             end-if
             if  a-byte equal to space and
                 address of word-entry not equal to null
                 add 1 to word-trailing-spaces
             end-if
             if  a-byte equal to x'22' or x'27'
                 move a-byte to quote-character
             end-if
         else
             if  a-byte equal to quote-character
                 move low-value to quote-character
             end-if
         end-if
*> put this byte into a word if not a space, test for *>
         evaluate true
             when quote-character not equal to low-value
                 perform put-byte-in-word
             when a-byte equal to space
                 continue
             when a-byte equal to '*' and lookahead-1 equal to '>'
                 move line-length to n
             when other
                 perform put-byte-in-word
                 if  not-cobol-character
                     perform end-word
                 end-if
         end-evaluate
     end-perform

     if  in-a-word
         perform end-word
     end-if

     goback.

 put-byte-in-word.
     if  not in-a-word
         perform start-word
     end-if
     move n to a-word-col-to
     add 1 to a-word-length
     move a-byte to a-word-byte (a-word-length).

 start-word.
     set in-a-word to true
     move zero to a-word-length
     move low-values to a-word-area
     move n to a-word-col-from, a-word-col-to.

 end-word.
     set not-in-a-word to true
     compute allocation-length =
         length of fixed-portion of word-entry + 2 + a-word-length
     compute allocation-length = length of word-entry  *> Fujitsu
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf error constructing word ' return-code
         goback
     end-if
     set address of word-entry to last-word
     if  first-word equal to null
         set first-word to allocation-pointer
     else
         set next-word to allocation-pointer
     end-if
     set address of word-entry to allocation-pointer
     move a-word-length to word-length
     move low-values to fixed-portion of word-entry
     move last-word to previous-word
     move allocation-pointer to last-word
     add 1 to word-count
     move word-count to word-number
     move a-word-col-from to word-col-from
     move a-word-col-to   to word-col-to
     move a-word to word-text.

 look-ahead.
     compute n1 = n + 1
     compute n2 = n + 2
     move space to lookahead-1, lookahead-2
     if  n1 not greater than line-length
         move line-byte (n1) to lookahead-1
         if  n2 not greater than line-length
             move line-byte (n2) to lookahead-2
         end-if
     end-if.


Finally, we read a line of source code. Significantly, this is at the bottom of
the program structure rather than the top.

 identification division.
 program-id. line-function.
*>author: Robert Wagner.
*>  Read a record. Constructs a line.

 environment division.
 input-output section.
 file-control.
    select input-file assign to path-file
        organization is line sequential
        file status is file-status.

 data division.
 file section.
 fd  input-file.
 01  input-record.
     05  input-byte occurs 256 pic x.
 01  input-record-fixedform.
     05  filler                         pic  x(07).
     05  cobol-text                     pic  x(65).
 01  input-record-option.
     05  filler                         pic  x(06).
     05  option-text                    pic  x(24).

 working-storage section.
 01  persistent-variables.
     05  filler value low-value         pic  x(01).
         88  file-open value 'y'.
         88  file-closed value low-value.
     05  filler value low-value         pic  x(01).
         88  free-form value 'f'.
         88  fixed-form value low-value.
 01  unqualified-variables.
     05  a-byte                         pic  x(01).

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables, program-entry.
 main.
     move low-values to unqualified-variables
     if  file-closed
         open input input-file
         if  file-status not equal to zero
             display 'open error ' file-status space path-file
             move file-status to pf-return-code
             goback
         end-if
         set file-open to true
         set fixed-form to true
     end-if

     perform read-a-record

     if  any-error
         close input-file
         set file-closed to true
         goback
     end-if

     if  (fixed-form and input-byte (7) not equal to '*') or
         (free-form  and input-byte (1) not equal to '*')
         perform construct-line
     end-if

     goback.

 read-a-record.
     read input-file at end
         move 10 to file-status
     end-read
     if  file-status not equal to zero
         move file-status to pf-return-code
     end-if.

 construct-line.
     if  option-text equal to '$SET SOURCEFORMAT"FREE"' or
         input-record-option equal to '@OPTIONS SRF(FREE,FREE)'
         set free-form to true
     end-if
     if  option-text equal to '$SET SOURCEFORMAT"FIXED"' or
         input-record-option equal to '@OPTIONS SRF(FIX,FIX)'
         set fixed-form to true
     end-if
     if  free-form
         perform varying record-length from 256 by -1
            until record-length equal to 1 or
                  input-byte (record-length) not equal to space
            continue
         end-perform
     else
         perform varying record-length from 72 by -1
            until record-length equal to 7 or
                  input-byte (record-length) not equal to space
            continue
         end-perform
         subtract 7 from record-length
     end-if
     compute allocation-length =
         length of fixed-portion of line-entry + 2 + record-length
     compute allocation-length = length of line-entry  *> Fujitsu
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf error constructing line ' return-code
         goback
     end-if
     set address of line-entry to last-line
     if  first-line equal to null
         set first-line to allocation-pointer
     else
         set next-line to allocation-pointer
     end-if
     set address of line-entry to allocation-pointer
     move record-length to line-length
     move low-values to fixed-portion of line-entry
     move last-line to previous-line
     move allocation-pointer to last-line
     add 1 to line-count
     move line-count to line-number
     if  free-form
         move input-record to line-text
     else
         move cobol-text to line-text
     end-if
     inspect line-text converting
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to
        'abcdefghijklmnopqrstuvwxyz'.
 end program line-function.
 end program word-function.


The brain of the system:

 identification division.
 program-id. analysis-function.
*>author: Robert Wagner
*>  Grammar (syntactical + lexical) analysis of Cobol program.
*>  Here is we look for the MEANING of Cobol words.
*>  Output is file entries.

 data division.
 working-storage section.
 01  persistent-variables.
     05  keyword-length value 100 comp-5  pic s9(04).
 01  unqualified-variables.
     05  hold-current-word       pointer.
     05  current-verb                   pic  x(30).
     05  a-word                         pic  x(30).
     05  other-words.
         10  current-fd                 pic  x(30).
         10  a-word-previous            pic  x(30).
     05  current-io-mod          pointer.
     05  current-record                 pic  x(30).
     05  filler                         pic  x(01).
         88  file-found value 'f'.
         88  file-not-found value low-value.
     05  filler                         pic  x(01).
         88  end-of-lines value 'e'.
 01  keyword-values.
     05  filler value 'accept'          pic  x(30).
     05  filler value 'add'             pic  x(30).
     05  filler value 'alter'           pic  x(30).
     05  filler value 'call'            pic  x(30).
     05  filler value 'cancel'          pic  x(30).
     05  filler value 'chain'           pic  x(30).
     05  filler value 'close'           pic  x(30).
     05  filler value 'commit'          pic  x(30).
     05  filler value 'compute'         pic  x(30).
     05  filler value 'continue'        pic  x(30).
     05  filler value 'delete'          pic  x(30).
     05  filler value 'display'         pic  x(30).
     05  filler value 'divide'          pic  x(30).
     05  filler value 'else'            pic  x(30).
     05  filler value 'enter'           pic  x(30).
     05  filler value 'entry'           pic  x(30).
     05  filler value 'evaluate'        pic  x(30).
     05  filler value 'examine'         pic  x(30).
     05  filler value 'exec'            pic  x(30).
     05  filler value 'exhibit'         pic  x(30).
     05  filler value 'exit'            pic  x(30).
     05  filler value 'fd'              pic  x(30).
     05  filler value 'go'              pic  x(30).
     05  filler value 'goback'          pic  x(30).
     05  filler value 'if'              pic  x(30).
     05  filler value 'initialize'      pic  x(30).
     05  filler value 'inspect'         pic  x(30).
     05  filler value 'linkage'         pic  x(30).
     05  filler value 'merge'           pic  x(30).
     05  filler value 'move'            pic  x(30).
     05  filler value 'multiply'        pic  x(30).
     05  filler value 'next'            pic  x(30).
     05  filler value 'on'              pic  x(30).
     05  filler value 'open'            pic  x(30).
     05  filler value 'perform'         pic  x(30).
     05  filler value 'read'            pic  x(30).
     05  filler value 'release'         pic  x(30).
     05  filler value 'return'          pic  x(30).
     05  filler value 'rewrite'         pic  x(30).
     05  filler value 'rollback'        pic  x(30).
     05  filler value 'search'          pic  x(30).
     05  filler value 'select'          pic  x(30).
     05  filler value 'service'         pic  x(30).
     05  filler value 'set'             pic  x(30).
     05  filler value 'sort'            pic  x(30).
     05  filler value 'start'           pic  x(30).
     05  filler value 'stop'            pic  x(30).
     05  filler value 'string'          pic  x(30).
     05  filler value 'subtract'        pic  x(30).
     05  filler value 'transform'       pic  x(30).
     05  filler value 'unlock'          pic  x(30).
     05  filler value 'unstring'        pic  x(30).
     05  filler value 'use'             pic  x(30).
     05  filler value 'working-storage' pic  x(30).
     05  filler value 'write'           pic  x(30).
     05  filler value high-values       pic  x(30).
 01  keyword-array redefines keyword-values.
     05  keyword-entry occurs 1 to 100 depending on keyword-length
             indexed x-keyword ascending key keyword-entry pic  x(30).
*>  Occurs 100 leaves plenty of room for expansion. If the actual
*>  number of lines was coded above, someone adding and deleting lines
*>  would have to change the number and get it exactly right.

*>  Redefines will cause a compiler warning that can be ignored.

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables, program-entry.
 main.
     move low-values to unqualified-variables
     if  keyword-length equal to 100
         set x-keyword to 1
         search keyword-entry
             when keyword-entry (x-keyword) equal to high-values
                 set keyword-length to x-keyword
         end-search
     end-if
     set address of line-entry to first-line

     perform until end-of-lines
*>       display 'line ' line-text
         set address of word-entry to first-word
         perform until address of word-entry equal to null
*>           display 'word ' word-text
             perform examine-word
             set address of word-entry to next-word
         end-perform
         if  next-line equal to null
             set end-of-lines to true
         else
             set address of line-entry to next-line
         end-if
     end-perform

     goback.

 examine-word.
     move word-text to a-word       *> for speed
     if  word-length equal to 1 and a-word equal to '.' and
         current-verb not = to 'fd' and 'working-storage' and 'linkage'
         move spaces to current-verb
     end-if
     search all keyword-entry
         when keyword-entry (x-keyword) equal to a-word
             move a-word to current-verb
             move spaces to other-words
             set file-not-found to true
     end-search
*> select file-name
     if  current-verb equal to 'select' and a-word-previous equal to
current-verb
         perform construct-file-entry
         set file-select to address of word-entry
     end-if
*> select ... assign to 'external name' or data-name
     if  current-verb equal to 'select' and a-word-previous equal to 'to'
         set file-name to address of word-entry
     end-if
*> select ... organization is indexed
     if  current-verb equal to 'select' and
         (a-word equal to
          'indexed'       or
          'line'          or
          'sequential'    or
          'relative') and
         file-organization equal to null
         set file-organization to address of word-entry
     end-if
*> fd file-name
     if  current-verb equal to 'fd' and a-word-previous equal to current-verb
         move a-word to current-fd
     end-if
*> fd ... 01 record-name
     if  current-verb equal to 'fd' and a-word-previous equal to '01'
         perform find-file-entry
         if  file-found
             set file-record to address of word-entry
         end-if
     end-if
*> if assign to data-name, get value of external name
     if  (current-verb equal to 'working-storage' or 'linkage') and
         a-word-previous equal to '01'
         move word-text to current-record
         perform find-file-entry-by-name
     end-if
     if  current-verb equal to 'working-storage' and
         (word-byte (1) equal to x'22' or x'27') and *> quote or apost
         file-found
         set file-name to address of word-entry
         set file-not-found to true
     end-if
*> open input file-name
     if  current-verb equal to 'open' and
         (a-word equal to
          'input'         or
          'output'        or
          'i-o'           or
          'extend')
         set current-io-mode to address of word-entry
     end-if
     if  current-verb equal to 'open'
         move word-text to current-fd
         perform find-file-entry
         if  file-found
             set file-open-mode to current-io-mode
         end-if
     end-if
*> read file-name
     if  current-verb equal to 'read' and a-word-previous equal to current-verb
         move word-text to current-fd
         perform find-file-entry
         if  file-found
             set file-read to address of word-entry
         end-if
     end-if
*> write record-name, delete file-name
     if  (current-verb equal to 'write' or 'rewrite' or 'delete') and
         a-word-previous equal to current-verb
         move word-text to current-record, current-fd
         if  current-verb equal to 'delete'
             perform find-file-entry
         else
             perform find-file-entry-by-record
         end-if
         if  file-found
             set file-write to address of word-entry
         end-if
     end-if
     move a-word to a-word-previous.
 find-file-entry.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-select
         if  address of word-entry not equal to null and
             word-text equal to current-fd
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 find-file-entry-by-record.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-record
         if  address of word-entry not equal to null and
             word-text equal to current-record
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 find-file-entry-by-name.
     set hold-current-word to address of word-entry
     set file-not-found to true
     set address of file-entry to first-file
     perform until address of file-entry equal to null or file-found
         set address of word-entry to file-name
         if  address of word-entry not equal to null and
             word-text equal to current-record
             set file-found to true
         else
             set address of file-entry to next-file
         end-if
     end-perform
     set address of word-entry to hold-current-word.
 construct-file-entry.
     compute allocation-length =
         length of fixed-portion of file-entry + 2
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf  error constructing file ' return-code
         goback
     end-if
     set address of file-entry to last-file
     if  first-file equal to null
         set first-file to allocation-pointer
     else
         set next-file to allocation-pointer
     end-if
     set address of file-entry to allocation-pointer
     move zero to file-length
     move low-values to fixed-portion of file-entry
     move last-file to previous-file
     move allocation-pointer to last-file.
 end program analysis-function.



Write file entries to the report

 identification division.
 program-id. output-function.
*>author. Robert Wagner.
*>  Write to the output file.
*>   Input is file entries built by analysis-function.
 environment division.
 input-output section.
 file-control.
    select output-file assign to 'progfile.txt'
        organization is line sequential
         file status is file-status.

 data division.
 file section.
 fd  output-file.
 01  output-record.
     05  select-out             pic  x(24).
     05  program-out            pic  x(46).
     05  open-mode-out          pic  x(06).
     05  read-out               pic  x(02).
     05  write-out              pic  x(02).
     05  name-out               pic  x(60).
     05  organization-out       pic  x(08).

 working-storage section.
 01  persistent-variables.
     05 filler value low-value  pic  x(01).
        88 file-open value 'y'.
        88 file-closed value low-value.

linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables, program-entry.
 main.
     if  file-closed
         open output output-file        *> Fujitsu does not support extend
         set file-open to true          *> so leave the file open
         if  file-status not equal to zero
             display 'error ' file-status ' opening output progfile'
             move file-status to pf-return-code
             goback
         end-if
     end-if
     set address of file-entry to first-file

     perform until end-of-files
         move spaces to output-record
         move program-name to program-out
         if  file-select not equal to null
             set address of word-entry to file-select
             move word-text to select-out
         end-if
         if  file-organization not equal to null
             set address of word-entry to file-organization
             move word-text to organization-out
         end-if
         if  file-open-mode not equal to null
             set address of word-entry to file-open-mode
             move word-text to open-mode-out
         end-if
         if  file-read not equal to null
             move 'r' to read-out
         end-if
         if  file-write not equal to null
             move 'w' to write-out
         end-if
         if  file-name not equal to null
             set address of word-entry to file-name
             move word-text to name-out
         end-if

         write output-record

         set address of file-entry to next-file
     end-perform

     goback.
 end program output-function.
 end program program-function.
 end program pf2.


These are service functions to allocate and deallocate memory. They are
separately compiled and linked as dll's.

@OPTIONS NOALPHA
@OPTIONS NODLOAD
 IDENTIFICATION DIVISION.
 PROGRAM-ID. MALLOC.
*> Author. Robert Wagner.
*>  Allocates memory.
*>  When calling system functions, which must be statically bound,
*>  compiler options NODLOAD and NOALPHA must be specified
*>  (program must be in upper case). As a result, system calls must be in
*>  separately compiled DLL's because you don't want your whole program in
*>  upper case.
*>  The limit on available memory is very large, above 40M on all operating
*> systems.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01  ALLOCATION-ATTRIBUTES VALUE ZERO COMP-5 PIC S9(09).
 LINKAGE SECTION.
 01  ALLOCATION-LENGTH                COMP-5 PIC S9(09).
 01  ALLOCATION-POINTER               COMP-5 PIC S9(09).
 PROCEDURE DIVISION USING ALLOCATION-LENGTH
     ALLOCATION-POINTER.
     CALL 'LocalAlloc' WITH STDCALL USING
         BY VALUE ALLOCATION-ATTRIBUTES
         BY VALUE ALLOCATION-LENGTH
     MOVE RETURN-CODE TO ALLOCATION-POINTER
     GOBACK.

@OPTIONS NOALPHA
@OPTIONS NODLOAD
 IDENTIFICATION DIVISION.
 PROGRAM-ID. MFREE.
*> Author. Robert Wagner.
*>  Release allocated memory.
*>   Use this to avoid memory leaks.
*>   See notes in malloc.cbl.
 DATA DIVISION.
 LINKAGE SECTION.
 01  OBJECT-TO-FREE                          PIC  X(01).
 PROCEDURE DIVISION USING OBJECT-TO-FREE.
     CALL 'LocalFree' WITH STDCALL USING OBJECT-TO-FREE
     GOBACK.
```

#### ↳ Re: Best Practices - Cobol. Part 2.

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-07T14:15:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b21b6q$2g6f$1@si05.rsvl.unisys.com>`
- **References:** `<3e441e92.170760373@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e441e92.170760373@news.optonline.net...

> * When using free-form, Fujitsu will not accept * in position 1 as a
> comment. One must use *> The Standard says * should work. Perhaps
> 'variable format' would work as expected. I didn't try that option.

Free-form source is a new feature of ISO/IEC 1989:2002, the COBOL standard
published just over two months ago.  While I believe Fujitsu plans to
introduce a compiler compliant with that standard, and while they may well
have introduced some features of that standard in their products before
introducing a fully-2002-compliant compiler, so far as I know these features
are treated as extensions to a compiler that is compliant with the PREVIOUS
standard.  I believe they WILL introduce a fully-2002-compliant compiler at
some point, but I do not believe such a product is yet available from them.

I know of only two COBOL standards that could reasonably be thought of as
"The Standard".

In ANSI X3.23-1985, there is only one reference format described (see Page
IV-41, 7.2, Reference Format Representation), and in that format the "*"
goes in the indicator area, fixed as Column 7.  Obviously, since this field
is one character long, Column 7 isn't big enough to contain "*>".

ISO/IEC 1989:2002 allows both fixed-form and free-form reference format.
Fixed-form reference format is pretty much the same as in the previous
standard in that the indicator area is one character at Column 7.  And while
floating indicators such as "*>" are allowed in fixed-form reference format,
fixed indicators (like "*") are explicitly disallowed in free-form reference
format (see Pages 22 and 23, introductory paragraphs under the topics 6.1,
Fixed indicators, and 6.2, Floating indicators).

Thus, neither ANSI X3.23-1985 nor ISO/IEC 1989:2002 allows "*" (without ">")
in Column 1 as a means of introducing a comment in any reference format.

Which "The Standard" is it that states this?

    -Chuck Stevens
```

##### ↳ ↳ Re: Best Practices - Cobol. Part 2.

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-07T23:23:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e443e08.178815890@news.optonline.net>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e441e92.170760373@news.optonline.net...
…[26 more quoted lines elided]…
>    -Chuck Stevens

I am oriented toward real-world experience. Heavy hitters Micro Focus, IBM,
Fujitsu and Realia all offered the interpretation of free-form I described, thus
I ASSUMED it was in the Standard. 

You are correct. Not for the first time, we have a disconnect between Standards
Commitee and the real world. 

Robert
```

###### ↳ ↳ ↳ Re: Best Practices - Cobol. Part 2.

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-07T18:22:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b21ik1$loi$1@slb1.atl.mindspring.net>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com> <3e443e08.178815890@news.optonline.net>`

```
Your statement

I am oriented toward real-world experience. Heavy hitters Micro Focus, IBM,
Fujitsu and Realia all offered the interpretation of free-form I described,
thus  I ASSUMED it was in the Standard.

>>> My response

HUH ???

Your whole "point" was that Fujitsu doesn't support it (this variation) of
using "*" in column 1 for free form reference format - and I "dare" you to
show me a clean compile with IBM (any compiler - any platform) that allows
for free-format - much less "*" in column 1 indicating a comment with free
format.  (I haven't looked at the Realia documentation, but I DOUBT that
they support this either)

(See below for "context")
```

###### ↳ ↳ ↳ Re: Best Practices - Cobol. Part 2.

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-07T17:15:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b21ln5$2n0a$1@si05.rsvl.unisys.com>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com> <3e443e08.178815890@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e443e08.178815890@news.optonline.net...

> You are correct. Not for the first time, we have a disconnect between
Standards
> Commitee and the real world.

Personally, I find allowing FLOATING indicators in FIXED form a really neat
feature.  I do think that if you're in FREE-FORM reference format it's
reasonable to expect that you'd conform to those rules, including the format
of comments intended for use in FREE-FORM reference format, namely, using
the FLOATING indicator "*>".

Otherwise there are some ambiguities.  I'm reasonably certain the following
demonstrates my point.  Consider each of the following source images as
starting in Column 1:
    123456 >>SOURCE FORMAT FREE
    COMPUTE A = B
    * C
    . *>

    >>SOURCE FORMAT FIXED
    123457     COMPUTE A = B
    123458     * C.  *>

Should these two examples produce the same result?  I contend that they
should.  If the "*" that's in Column 1 in the first example introduces a
comment, the whole line should be treated as a comment, and thus the two
COMPUTEs should produce different answers.  If you want "*" in Column 1 to
be a comment in the general case, you break multiplication and
exponentiation in arithmetic expressions, as well as floating-asterisk
PICTUREs.

I don't think that's all that great an idea, I don't think that's what the
programmer who (for whatever reason) coded such a thing had in mind, and I
don't think the casual reader of such a statement would presume right off
the top that A = B even if C is not equal to 1.

If you're in free-form reference format, and you want a comment in your
source, it's appropriate to use the format for comments that's appropriate
for use in free-form reference format, and I don't think requiring that, at
the expense of breaking PICTURE ***,***... as well as COMPUTE ... * and **,
is the "evidence of a disconnect between Standards Commitee and the real
world" that you claim it to be!

Maybe you as a COBOL programmer with a "wish list" for the standard don't
have to think about such possibilities, but the folks who are trying to
write rules that don't cause such bizarre side effects certainly do!

What implementations / platforms actually do treat the asterisk in Column 1
(without ">") as a comment?  And what do they do with PICTURE and arithmetic
expressions in those cases?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Best Practices - Cobol. Part 2.

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-09T12:01:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e464321.55646579@news.optonline.net>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com> <3e443e08.178815890@news.optonline.net> <b21ln5$2n0a$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[30 more quoted lines elided]…
>PICTUREs.

There are two schools of thought. One holds that line terminators can be
discarded, that the program can be regarded as a one-dimensional stream of
bytes. In that case, comments must be explicitly terminated, as seen in C's /*
.. */. 

The other holds that line terminators are significant. They terminate a comment,
as seen in C++'s "//"

If line breaks can terminate a comment, they should also be significant in
initiating one. 

Because COBOL subscribes to the second school of thought -- line break
terminates a comment -- it would be symmetrical to provide * in position 1 for
initiating one. 

>What implementations / platforms actually do treat the asterisk in Column 1
>(without ">") as a comment?  And what do they do with PICTURE and arithmetic
>expressions in those cases?

Realia and Micro Focus, in my personal experience, probably others. They expect
free-form text to start in position 2 rather than 1. I know, it's like the old
days except seven 'card columns' have been collapsed down to one. 

The chance of inadvertantly coding an * in column 1 is miniscule in real-world
practice. 

Robert
```

###### ↳ ↳ ↳ Re: Best Practices - Cobol. Part 2.

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-10T16:39:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b29gne$1q65$1@si05.rsvl.unisys.com>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com> <3e443e08.178815890@news.optonline.net> <b21ln5$2n0a$1@si05.rsvl.unisys.com> <3e464321.55646579@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e464321.55646579@news.optonline.net...

> If line breaks can terminate a comment, they should also be significant in
> initiating one.
>
> Because COBOL subscribes to the second school of thought -- line break
> terminates a comment -- it would be symmetrical to provide * in position 1
for
> initiating one.

COBOL does so only because the entire line is a comment -- allowing any
permissible characters in the comment.  The problem with asterisk in Column
1 of source images in free-form reference format is that you can't tell
whether it's a syntactic component or not.  An implementation that treats
Column 1 as a fixed-form reference indicator is not an implementation of
free-form reference format, it's an extension that's incompatible with
standard COBOL.

What character or mechanism terminates a line is up to the implementor.  It
may be a line feed, it may be a carriage return, it may be the end of the
physical record.  I don't agree that a leading "*" as an indication of a
comment is symmetrical with the end of the line, nor do I agree that a "*"
in Column 1 (but not a leading "*" that happens to be in Column 2) is
consistent with the idea of "free-form reference format.

I can see some benefit to the idea of providing "embedded comments" (in
addition to the 2002-standard "inline comments"), but such an implementation
would restrict the contents of such a comment because the syntax would of
necessity require a specific character or character sequence to terminate
the comment.

> The chance of inadvertantly coding an * in column 1 is miniscule in
real-world
> practice.

Minuscule in hand-coded programs, perhaps (but only perhaps).  But I've seen
many COBOL '74 and '85 programs in which all of the code is generated source
not intended for manual maintenance, and in which the generated source is as
dense as the compiler allows.  In such an environment, the generator would
have to be able to detect that the arithmetic expression it was about to
generate included a multiplication, and thus the generator would have to
"escape" to a new record to circumvent the ambiguity between the leading
asterisk as introducing a comment and the leading asterisk as a part of an
arithmetic expression.  In my particular case, a high percentage of the code
that the compilers I work with are required to compile is just such
generated code.   While it could be argued that no reasonable programmer
trying to create readable code would ever do such a thing, the underlying
assumption that every program being "consumed" by the COBOL compiler was
written by a human trying to produce a legible, elegant COBOL program is
simply invalid.  It may have been generated by a program designed to
conserve every bit of disk space with nary a side glance at legibility. The
rules of free-form reference format -- including the use of "floating"
indicators in that context -- actually make the job of the latter much
easier.


Note also that in '02 COBOL numbers can reach 31 (from 18) digits, and
picture character-strings can go up to 50 (from 30) characters.  Thus,
"***,***,***,***,***,***,***,***,***,***.99CR" is perfectly reasonable as a
numeric-edited PICTURE character-string in that dialect.  Try fitting that,
and much else, in a single line of a traditional 80-column-oriented source
images.

Even with free-form source images (which according to the standard can't
exceed 255 characters), it is not at all inconcievable that a programmer
would end up having the PICTURE in one source image and the associated
character-string on the next for similar formatting and pretty-text
alignment reasons.

Because the chances are minuscule does not mean that the compiler designer
need not provide for them, and I don't think the "right answer" is to treat
"*" in Column 1 of free-format reference format as introducing a comment
unless Column 2 contains ">".   And if the distinction is that "*" in Column
1 introduces a comment but "*" in Column 2 does not, well, folks, that's not
a FREE-form reference format, that's a variation of FIXED-form reference
format in which the sequence number field is simply deleted.   A free-form
reference format that is truly free form is not dependent on column
positions.   At all.

      -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Best Practices - Cobol. Part 2.

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-10T23:52:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302102352.5f3634a7@posting.google.com>`
- **References:** `<3e441e92.170760373@news.optonline.net> <b21b6q$2g6f$1@si05.rsvl.unisys.com> <3e443e08.178815890@news.optonline.net> <b21ln5$2n0a$1@si05.rsvl.unisys.com> <3e464321.55646579@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> There are two schools of thought. ... 
> as seen in C's /* .. */. 
> as seen in C++'s "//"

Actually C++ has both of these and many C implementions support //
 
> If line breaks can terminate a comment, they should also be significant in
> initiating one. 

Huh ? Why _should_ they ?
 
> Because COBOL subscribes to the second school of thought -- line break
> terminates a comment -- 

Actually Cobol changed from one to the other.  Originally Cobol had
the NOTE statement which started a comment ended by end of sentence or
end of paragraph.  later the column 7 '*' was introduced, and NOTE was
dropped.

> it would be symmetrical to provide * in position 1 for
> initiating one. 

In what way is '*' symetrical with \n ?
 
> Realia and Micro Focus, in my personal experience, probably others. They expect
> free-form text to start in position 2 rather than 1. I know, it's like the old
…[3 more quoted lines elided]…
> practice. 

What was poor about MF Cobolo is that when they introduced '*' in
Column 1 as a comment marker it also applied to fixed format source.

With older compilers columns 1-6 were completely ignored unless the
first line had a sequence number or somesuch.  Cols 1-6 thus could be
used, for example, for version control.

I was looking after some code that occasionally had notations in 1-6,
sometimes this began with an '*'.  The new compiler introduced some
strange bugs that had to be resolved by processing all the source code
to remove col 1-6, especially '*'s.

"Miniscule", I think not.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
