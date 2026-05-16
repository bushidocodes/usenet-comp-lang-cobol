[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# a challenge for mf-cobol wizards

_7 messages · 4 participants · 2000-01 → 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### a challenge for mf-cobol wizards

- **From:** mark_f_edwards@my-deja.com
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86nu3j$2sc$1@nnrp1.deja.com>`

```
hello all-

i would like to get all the filenames in a particular directory
into a program table (or array).

one method was to do:

  CALL "SYSTEM"  USING  BY REFERENCE
              "  ls  -1  >/tmp/mark "
  END-CALL
  open input tmp-file .....

but this seemed really sloppy.

does mf-cobol have a library call to do this, or does the system call
have some way to return values into working-storage??

a prize awaits the best solution!

thx,
mark.edwards@sunh.com


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: a challenge for mf-cobol wizards

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388fd898_2@news1.prserv.net>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com>`

```
Test

<mark_f_edwards@my-deja.com> wrote in message
news:86nu3j$2sc$1@nnrp1.deja.com...
> hello all-
>
…[22 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: a challenge for mf-cobol wizards

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388fd90f_1@news1.prserv.net>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com>`

```
You want to use the Micro Focus x"91" Function 69 call.  I have enclosed a
code snippet to get you started.  The code may not be totally complete, but
it will give you a good idea of how to use the API call.  I have been using
this routine since 1994, and on OS/2, Win95/NT/2000.

The internal sort is used to sort the returned file list - you can omit if
you don't need it.  You can also narrow it down to just retrieve individual
items - files, subdirs, hidden files, etc...

Hope it helps, and let me know about the prize - better yet, keep the prize
and check out our company web-site at www.c-cubed.net.  We offer lots of
things for MVS Host Offloading using Micro Focus Cobol, as well as a VB
interface to MVS...  I'm done with the sales pitch... :-)

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net

C-Cubed Inc.
3629 North Morning Dove
Mesa, AZ  85207
Web:   http://www.c-cubed.net

Code Snippet:

       input-output section.
       file-control.

           select sort-file
               assign                  to 'sorttemp'
               sort status             is sort-status.

           select extlist-file
               assign                  to dynamic ws-extlist-path
               organization            is line sequential
               file status             is ws-status.

       data division.
       file section.

       sd  sort-file.
       01  sort-rec.
           03  sort-file-type          pic x.
               88  sort-file-type-subdir           value 'S'.
               88  sort-file-type-file             value 'F'.
           03  sort-attribute          pic 9(2).
           03  sort-time               pic 9(4).
           03  sort-date               pic 9(4).
           03  sort-size               pic 9(8).
           03  sort-file-name          pic x(255).

       fd  extlist-file.
       01  extlist-record.
           03  er-file-type            pic x.
               88  er-file-type-subdir             value 'S'.
               88  er-file-type-file               value 'F'.
           03  er-attribute            pic 9(2).
           03  er-time                 pic 9(4).
           03  er-date                 pic 9(4).
           03  er-size                 pic 9(8).
           03  er-filler1              pic x.
           03  er-file-name-base-extn  pic x(12).
           03  er-filler2              pic x.
           03  er-file-name-full       pic x(255).

       working-storage section.

       01  ws-miscellaneous.
           03  ws-ole32-dll-ptr        procedure-pointer.
           03  ws-cubed-name           pic x(8)   value 'c3comfil'.
           03  ws-drive-info           pic x(4)  comp-x.
           03  ws-bit-mask             pic x(4)  comp-x.
           03  ws-temp-mask            pic x(4)  comp-x.
           03  ws-toupper-length       pic 9(9)  comp-5 value 772.
           03  ws-os2-status           pic  9(4) comp-x.
           03  ws-idx                  pic s999  comp.
           03  ws-len                  pic s999  comp.
           03  ws-x91-function         pic x     comp-x.
               88  ws-x91-function-69                   value 69.
               88  ws-x91-function-35                   value 35.
           03  ws-save-attribute       pic x     comp-x.
           03  ws-garbage              pic x(2).
           03  ws-extn-cnt             pic s9    comp-5.
           03  filler                  pic x.
               88  eof-infile                    value 'Y'.
               88  not-eof-infile                value 'N'.
           03  ws-extlist-path         pic x(255).

       01  ws-switches.
           03  ws-status.
               05  ws-status-1         pic x.
               05  ws-status-2         pic 99    comp-x.

           03  sort-status.
               05  sort-status-1       pic x.
               05  sort-status-2       pic 99    comp-x.

           03  ws-function-switch      pic x.
               88  ws-function-dialog            value 'D'.
               88  ws-function-file              value 'F'.

           03  first-time-switch       pic x     value 'y'.
               88  first-time                    value 'y'.
               88  not-first-time                value 'n'.

       01  ws-drive-table-count        pic s99   value +26.
       01  ws-drive-table-data.
           03  filler  value 'A:\'     pic x(3).
           03  filler  value 'B:\'     pic x(3).
           03  filler  value 'C:\'     pic x(3).
           03  filler  value 'D:\'     pic x(3).
           03  filler  value 'E:\'     pic x(3).
           03  filler  value 'F:\'     pic x(3).
           03  filler  value 'G:\'     pic x(3).
           03  filler  value 'H:\'     pic x(3).
           03  filler  value 'I:\'     pic x(3).
           03  filler  value 'J:\'     pic x(3).
           03  filler  value 'K:\'     pic x(3).
           03  filler  value 'L:\'     pic x(3).
           03  filler  value 'M:\'     pic x(3).
           03  filler  value 'N:\'     pic x(3).
           03  filler  value 'O:\'     pic x(3).
           03  filler  value 'P:\'     pic x(3).
           03  filler  value 'Q:\'     pic x(3).
           03  filler  value 'R:\'     pic x(3).
           03  filler  value 'S:\'     pic x(3).
           03  filler  value 'T:\'     pic x(3).
           03  filler  value 'U:\'     pic x(3).
           03  filler  value 'V:\'     pic x(3).
           03  filler  value 'W:\'     pic x(3).
           03  filler  value 'X:\'     pic x(3).
           03  filler  value 'Y:\'     pic x(3).
           03  filler  value 'Z:\'     pic x(3).
       01  filler redefines ws-drive-table-data.
           03  ws-drive-table occurs 26 times
                                       pic x(3).

       01  ws-subroutines.
           03  renfile-sub    pic x(15)   value 'cbl_rename_file'.
           03  copyfile-sub   pic x(15)   value 'cbl_copy_file'.
           03  delfile-sub    pic x(15)   value 'cbl_delete_file'.
           03  splitfle-sub   pic x(18)   value 'cbl_split_filename'.
           03  joinfle-sub    pic x(17)   value 'cbl_join_filename'.
           03  readdriv-sub   pic x(13)   value 'pc_read_drive'.
           03  read-dir-sub   pic x(12)   value 'cbl_read_dir'.
           03  logical-and    pic x(12)   value 'cbl_and'.
           03  loctfile-sub   pic x(15)   value 'cbl_locate_file'.
           03  finddriv-sub   pic x(14)   value 'pc_find_drives'.
           03  booland-sub    pic x(8)    value 'cbl_and'.
           03  lowrcase-sub   pic x(11)   value 'cbl_tolower'.
           03  cob32api-sub   pic x(8)    value 'cob32api'.

      * Sending area for X"91" function 69 calls.
       01 find-file-sending-info.
          05 ffs-action                pic x    comp-x.
             78 ffs-find-first-file             value 0.
             78 ffs-find-next-file              value 1.
             78 ffs-find-terminate              value 2.
             78 ffs-find-matching               value 3.
          05 ffs-file-type             pic 9(2) comp-x.
             78 ffs-normal                      value 0.
             78 ffs-read-only                   value 1.
             78 ffs-hidden                      value 2.
             78 ffs-system                      value 4.
             78 ffs-volume-label                value 8.
             78 ffs-subdirectory                value 16.
             78 ffs-archived                    value 32.
      * This selection will retrieve all but sub-directories and volume
      * labels.  Turn on the individual bits of the type that you want
      * to select.
             78 ffs-nrhsa-attributes            value 39.
          05 ffs-filename.
             07 ffs-filename-first     pic x.
             07 filler                 pic x(254).

      * Receiving area for X"91" function 69 calls.
       01 find-file-returned-info.
           03  ffr-error               pic x    comp-x.
           03  ffr-handle              pic x(2) comp-x.
           03  ffr-attribute           pic x    comp-x.
           03  ffr-time                pic x(2) comp-x.
           03  ffr-date                pic x(2) comp-x.
           03  ffr-size                pic x(4) comp-x.
           03  ffr-filename.
               05  ffr-filename-78.
                   07  ffr-filename-2  pic xx.
                   07  filler          pic x(76).
               05  filler              pic x(177).


        Procedure Division.

       0000-main  section.
           perform 3100-files-load-to-file.
           perform 4100-subdirs-load-to-file.
       0000-exit.
           exit.


       3100-files-load-to-file  section.
           set ws-function-file        to true.

           sort sort-file
               on ascending key sort-file-name
               input  procedure is 3500-files-get-list
               output procedure is 3501-files-sort-list.
       3100-exit.
           exit.


      * This section will obtain the list of files from the Operating
      * System.
       3500-files-get-list  section.
           move zero                   to ffr-handle.
           move ffs-find-first-file    to ffs-action.
           move ffs-nrhsa-attributes   to ffs-file-type.
           move +0                     to ffr-error.
           move '00'                   to ws-status.
           set ws-x91-function-69      to true.

           perform
           varying ws-idx from +1 by +1
           until (ffr-error equal 1)
           or    (sort-status not equal '00')

      * Call Micro Focus Scan Directory Function:
               perform 7999-call-x91-func69

      * Mask of the Directory bit to determine if this is a Directory:
               move ffr-attribute      to ws-save-attribute
               move ffs-subdirectory   to ffs-file-type
               call logical-and using ffs-file-type
                                      ws-save-attribute
                                      by value 2
               end-call

      * If this is not a subdirectory, then check for volume label:
               if ws-save-attribute equal 0
                   move ffr-attribute      to ws-save-attribute
                   move ffs-volume-label   to ffs-file-type
                   call logical-and using ffs-file-type
                                          ws-save-attribute
                                          by value 2
                   end-call

      * If this is not Volume Info, then restore original attribute:
                   if ws-save-attribute equal 0
                       move ffr-attribute  to ws-save-attribute
                   end-if
               end-if

               move ws-save-attribute  to ffr-attribute

      * If not a Directory or Volume Label, then it's a valid file name:
               evaluate true
                   when ffr-attribute equal ffs-subdirectory
                   when ffr-attribute equal ffs-volume-label
                   when ffr-error greater than 0
                       continue

                   when ws-idx greater than +300
                       move 1              to ffr-error

                   when other
                       move length of ffr-filename to ws-toupper-length
                       call lowrcase-sub using ffr-filename
                                      by value ws-toupper-length
                       end-call
                       set  sort-file-type-file    to true
                       move ffr-filename   to sort-file-name
                       move ffr-attribute  to sort-attribute
                       move ffr-time       to sort-time
                       move ffr-date       to sort-date
                       move ffr-size       to sort-size
                       release sort-rec
               end-evaluate

               move ffs-find-next-file to ffs-action
           end-perform.

           move ffs-filename           to wjfi-disp-buffer.
           move +0                     to ws-idx.
       3500-files-get-exit.
           exit.


       3501-files-sort-list  section.
           perform
           until (sort-status not equal '00')
               return sort-file
                   at end
                       move '10'       to sort-status
               end-return

               evaluate true
                   when sort-status not equal '00'
                       continue

                   when ws-function-file
                       move sort-file-type to er-file-type
                       move sort-file-name to er-file-name-base-extn
                       move sort-attribute to er-attribute
                       move sort-time      to er-time
                       move sort-date      to er-date
                       move sort-size      to er-size
                       move spaces         to er-filler1
                       move spaces         to er-filler2
                       move spaces         to er-file-name-full
                       string
                           wjfi-path-buffer    delimited by space
                           '\'                 delimited by size
                           sort-file-name      delimited by space
                           into er-file-name-full
                       end-string
                       write extlist-record

                   when ws-function-dialog
                       add +1              to ws-idx
                       move sort-file-name to c3comfil-subdir-entry
                       move 'g300-files-insert-entry' to ds-procedure
                       perform 8001-call-dialog

                       if ws-idx greater than +300
                           move 'Only a partial list of files is being d
      -                         'isplayed!  Please enter a more qualifie
      -                         'd search criteria after selecting "Ok".
      -                         '..'
                               to c3comfil-file-path
                           move '99'               to ws-status
                           move 'g200-max-files'   to ds-procedure
                           perform 8001-call-dialog
                           move 1                  to ffr-error
                       end-if
               end-evaluate
           end-perform.
       3501-exit.
           exit.

       4100-subdirs-load-to-file  section.
           set ws-function-file        to true.

           sort sort-file
               on ascending key sort-file-name
               input  procedure is 4500-subdirs-get-list
               output procedure is 4501-subdirs-sort-list.
       4100-exit.
           exit.


      * This section will obtain the list of files from the Operating
      * System.
       4500-subdirs-get-list  section.
           evaluate true
               when wjfi-path-buffer(3:1) equal space
                   move '\'            to ws-garbage
               when wjfi-path-buffer(4:1) equal space
                   move space          to ws-garbage
               when other
                   move '\'            to ws-garbage
           end-evaluate.

           move spaces                 to ffs-filename.
           string
               wjfi-path-buffer        delimited by space
               ws-garbage              delimited by space
               '*.*'                   delimited by size
               into ffs-filename
           end-string.

      * The following code will build the subdirectory list.  This code
      * works in Dos, Windows, and OS/2 environments:
           move zero                   to ffr-handle.
           move ffs-find-first-file    to ffs-action.
           move ffs-subdirectory       to ffs-file-type.
           move +0                     to ffr-error.
           move '00'                   to ws-status.
           set ws-x91-function-69      to true.

           perform
           until (ffr-error equal 1)
           or    (sort-status not equal '00')
      * Call Micro Focus Scan Directory Function:
               perform 7999-call-x91-func69

      * Mask of the Directory bit to determine if this is a Directory:
               call logical-and using ffs-file-type
                                      ffr-attribute
                                      by value 2

      * If this is a subdirectory, then add it to the list for display:
               evaluate true
                   when ffr-attribute not equal ffs-subdirectory
                   when ffr-error not equal 0
                       continue

                   when other
                       move length of ffr-filename to ws-toupper-length
                       call lowrcase-sub using ffr-filename
                                      by value ws-toupper-length
                       end-call
                       set  sort-file-type-subdir  to true
                       move ffr-filename   to sort-file-name
                       move ffr-attribute  to sort-attribute
                       move ffr-time       to sort-time
                       move ffr-date       to sort-date
                       move ffr-size       to sort-size
                       release sort-rec
               end-evaluate

               move ffs-find-next-file to ffs-action
           end-perform.

           move ffs-filename           to wjfi-disp-buffer.
           move +0                     to ws-idx.
       4500-exit.
           exit.


       4501-subdirs-sort-list  section.
           perform
           until (sort-status not equal '00')
               return sort-file
                   at end
                       move '10'       to sort-status
               end-return

               evaluate true
                   when sort-status not equal '00'
                       continue

                   when ws-function-file
                       move sort-file-type to er-file-type
                       move sort-file-name to er-file-name-base-extn
                       move sort-attribute to er-attribute
                       move sort-time      to er-time
                       move sort-date      to er-date
                       move sort-size      to er-size
                       move spaces         to er-filler1
                       move spaces         to er-filler2
                       move spaces         to er-file-name-full
                       string
                           wjfi-path-buffer    delimited by space
                           '\'                 delimited by size
                           into er-file-name-full
                       end-string
                       write extlist-record

                   when ws-function-dialog
                       move sort-file-name to c3comfil-subdir-entry
                       move 'g400-subdirs-insert-entry' to ds-procedure
                       perform 8001-call-dialog

               end-evaluate
           end-perform.
       4501-exit.
           exit.

       7999-call-x91-func69  section.
           move spaces                 to ffr-filename.

           call x"91"          using find-file-returned-info
                                     ws-x91-function
                                     find-file-sending-info
           end-call.

           if ffr-error not equal 0
               move 1                  to ffr-error
           end-if.
       7999-exit.
           exit.


----- Original Message -----
From: <mark_f_edwards@my-deja.com>
Newsgroups: comp.lang.cobol
Sent: Wednesday, January 26, 2000 2:56 PM
Subject: a challenge for mf-cobol wizards


> hello all-
>
…[22 more quoted lines elided]…
> Before you buy.


<mark_f_edwards@my-deja.com> wrote in message
news:86nu3j$2sc$1@nnrp1.deja.com...
> hello all-
>
…[22 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: a challenge for mf-cobol wizards

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86oq3n$oee$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com> <388fd90f_1@news1.prserv.net>`

```

"Lucas, Todd" <todd.lucas@ibm.net> wrote in message
news:388fd90f_1@news1.prserv.net...
> You want to use the Micro Focus x"91" Function 69 call.  I have enclosed a
> code snippet to get you started.  The code may not be totally complete,
but
> it will give you a good idea of how to use the API call.  I have been
using
> this routine since 1994, and on OS/2, Win95/NT/2000.


<anip>

    But does it work on unix?
```

#### ↳ Re: a challenge for mf-cobol wizards

- **From:** PAL3000 <pauldub*REMOVETHIS*@home.com>
- **Date:** 2000-01-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TkCQOJMv76iYlpRFyeduqbcvDU3H@4ax.com>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com>`

```
You can call C programs from MF Cobol, and pass arrays back an forth.
Check the web site and manuals for some examples.  

Paul

On Wed, 26 Jan 2000 22:56:53 GMT, mark_f_edwards@my-deja.com wrote:

>hello all-
>
…[22 more quoted lines elided]…
>Before you buy.

--------------------------------------
To reply by email, please take out 
*REMOVETHIS* from my email address
```

##### ↳ ↳ Re: a challenge for mf-cobol wizards

- **From:** jgill_1@my-deja.com
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86tj1k$6dk$1@nnrp1.deja.com>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com> <TkCQOJMv76iYlpRFyeduqbcvDU3H@4ax.com>`

```
I have written an assembler program that I call from MF-Cobol 3.2
that retrieves the file names from any directory. You can use
wild cards in your selection procedure.
If interested, E-mail me:  John Gill        jdgill@juno.com






In article <TkCQOJMv76iYlpRFyeduqbcvDU3H@4ax.com>,
  PAL3000 <pauldub*REMOVETHIS*@home.com> wrote:
> You can call C programs from MF Cobol, and pass arrays back an forth.
> Check the web site and manuals for some examples.
…[34 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: a challenge for mf-cobol wizards

- **From:** mark_f_edwards@my-deja.com
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<877i8i$339$1@nnrp1.deja.com>`
- **References:** `<86nu3j$2sc$1@nnrp1.deja.com>`

```


 well, it would appear that i win my own prize!

 it seems that a pipe can be created via:

  display 'dd_command'  upon environment-name
  display '< ls -1 '    upon environment-value

 and open up a line sequential file named: 'command'

 i got this example off of the merant page.  let me know if interested.

thx,  me


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
