[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus

_3 messages · 3 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus

- **From:** "charles" <ua-author-10059@usenetarchives.gap>
- **Date:** 1998-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdb020$ff32c000$2a3702c4@charlfre>`

```
I am looking for the file status codes.
Microfocus Cobol

Please help.
```

#### ↳ Re: Microfocus

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-07-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eda5d27ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb020$ff32c000$2a3702c4@charlfre>`
- **References:** `<01bdb020$ff32c000$2a3702c4@charlfre>`

```
In message <<01bdb020$ff32c000$2a3702c4@charlfre>> "Charles" writes:
› I am looking for the file status codes
› Microfocus Cobol
›
› Please help.

Which manuals have you looked in so far ?

Which version, in MF 3.2 check 'Error Messages' manual. The
Table of Contents on page v. gives 'File Status Codes' on
page 5-3.
```

#### ↳ Re: Microfocus

- **From:** "gene..." <ua-author-15604922@usenetarchives.gap>
- **Date:** 1998-07-15T20:47:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eda5d27ec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb020$ff32c000$2a3702c4@charlfre>`
- **References:** `<01bdb020$ff32c000$2a3702c4@charlfre>`

```
In article <01bdb020$ff32c000$2a3702c4@charlfre>,
"Charles" wrote:
› I am looking for the file status codes.
› Microfocus Cobol
›
› Please help.
›
File Status Codes

Code Meaning 00 Successful completion 02 Indexed files only.
One of two possibilities: For a READ statement, the key value for the current
key is equal to the value of that same key in the next record in the current
key of reference. For a WRITE or REWRITE statement, the record just written
created a duplicate key value for at least one alternate record key for which
duplicates are allowed. 04 The length of the record being processed does
not conform to the fixed file attributes for that file. 05 The
referenced optional file is not present at the time the OPEN statement is
executed. 07 Sequential files only. For an OPEN or CLOSE statement with
the REEL/UNIT phrase the referenced file is a non-reel/unit medium. 10
No next logical record exists. You have reached the end of the file. 14
Relative files only. The number of significant digits in the relative record
number is larger than the size of the relative key data item described for
that file. 21 Sequentially accessed files only. Indicates a sequence error.
The ascending key requirements of successive record key values has been
violated, or, the prime record key value has been changed by a COBOL program
between successful execution of a READ statement and execution of the next
REWRITE statement for that file. 22 Indexed and relative files only.
Indicates a duplicate key condition. Attempt has been made to store a record
that would create a duplicate key in the indexed or relative file OR a
duplicate alternate record key that does not allow duplicates. 23 Indicates
no record found. An attempt has been made to access a record, identified by a
key, and that record does not exist in the file. Alternatively a START or
READ operation has been tried on an optional input file that is not present.
24 Relative and indexed files only. Indicates a boundary violation
arising from one of the following conditions: an attempt is made to write
beyond the externally defined boundaries of a file; a sequential WRITE
operation has been tried on a relative file, but the number of significant
digits in the relative record number is larger than the size of the relative
key data item described for the file. 30 The I/O statement was
unsuccessfully executed as the result of a boundary violation for a
sequential file or as the result of an I/O error, such as a data check parity
error, or a transmission error. 34 The I/O statement failed because of a
boundary violation. This condition indicates that an attempt has been made to
write beyond the externally defined boundaries of a sequential file. 35
An OPEN operation with the I-O, INPUT, or EXTEND phrases has been tried on a
non-OPTIONAL file that is not present. 37 An OPEN operation has been tried
on a file which does not support the open mode specified in the OPEN
statement. 38 An OPEN operation has been tried on a file previously
closed with a lock. 39 A conflict has been detected between the fixed file
attributes and the attributes specified for that file in the program. 41
An OPEN operation has been tried on file already opened. 42 A CLOSE
operation has been tried on file already closed. 43 Files in sequential
access mode. The last I/O statement executed for the file, before the
execution of a DELETE or REWRITE statement, was not a READ statement. 44
A boundary violation exists. Possible violations are:- An attempt has been
made to WRITE or REWRITE a record that is larger than the largest, or smaller
than the smallest record allowed by the RECORD IS VARYING clause of the
associated file.- An attempt has been made to REWRITE a record to a file,
and the record is not the same size as the record being replaced. 46 A
sequential READ operation has been tried on a file open in the INPUT or I-O
mode but no valid next record has been established. 47 A READ or START
operation has been tried on a file not opened INPUT or I-O. 48 A WRITE
operation has been tried on a file not opened in the OUTPUT, I- O, or EXTEND
mode, or on a file open I-O in the sequential access mode. 49 A DELETE
or REWRITE operation has been tried on a file that is not opened I-O.

The example code that follows illustrates how to redefine a standard file
status so that it can be used as an extended file status. Assume for this
example that the input file does not exist - when the OPEN INPUT statement is
executed, a file status of 9/013 (ï¿½file not foundï¿½) is returned.

select in-file

assign to ï¿½user.datï¿½.
file status is file-status.
ï¿½
working-storage section.
01 file-status.
05 status-key-1 pic x.
05 status-key-2 pic x.
05 status-key-2-binary redefines status-key-2 pic 99 comp-x.
ï¿½
procedure division.
open input in-file
if file-status not = "00"
if status-key-1 = "9"
if status-key-2-binary = 13
display "File not found"
ï¿½

If you want to display the extended file status code, you need to move the
second byte of the file status data item to a display field large enough to
hold the maximum value 255:

select in-file

assign to ï¿½user.datï¿½
file status is file-status.
ï¿½
working-storage section.
01 ans74-file-status.
05 status-key-1 pic x.
05 status-key-2 pic x.
05 status-key-2-binary redefines status-key-2 pic 99 comp-x.
01 display-ext-status
05 filler pic xx value
"9/"
05 display-key 2 pic 999
ï¿½
procedure division.
open input in-file
if file-status not = "00"
display "Error. File status =" with no advancing
if status-key-1 = "9"

move status-key-2-binary to display-key-2
display display-ext-status
else
display file-status
end-if

Extended File Status Codes

When using ANSI'74 or ANSI'85 file status codes, the run-time system returns
extended file status codes if the extended file status is more specific.
Extended file status codes are of the form:
9/nnn
where nnn is one of the following values:

001 Insufficient buffer space. Could also indicate an out of memory
situation.
002 File not open when access tried.
003 Serial mode error.
004 Illegal file name.
005 Illegal device specification.
006 Attempt to write to a file opened for input.
007 Disk space exhausted.
008 Attempt to input from a file opened for output.
009 No room in directory (also, directory does not exist).
010 File name not supplied.
012 Attempt to open a file which is already open.
013 File not found.
014 Too many files open simultaneously.
015 Too many indexed files open.
016 Too many device files open.
017 Record error: probably zero length.
018 Read part record error: EOF before EOR or file open in wrong mode.
019 Rewrite error: open mode or access mode wrong.
020 Device or resource busy.
021 File is a directory.
022 Illegal or impossible access mode for OPEN.
023 Illegal or impossible access mode for CLOSE.
024 Disk I/O error.
025 Operating system data error.
026 Block I/O error.
027 Device not available.
028 No space on device.
029 Attempt to delete open file.
030 File system is read only.
031 Not owner of file.
032 Too many indexed files, or no such process.
033 Physical I/O error.
034 Incorrect mode or file descriptor.
035 Attempt to access a file with incorrect permission.
036 File already exists.
037 File access denied.
038 Disk not compatible.
039 File not compatible.
040 Language initialization not set up correctly.
041 Corrupt index file.
042 Attempt to write on broken pipe.
043 File information missing for indexed file.
045 Attempt to open an NLS file using an incompatible program.
047 Indexed structure overflow. (Could indicate that you have reached the
maximum number of duplicate keys.)
065 File locked.
066 Attempt to add duplicate record key to indexed file.
067 Indexed file not open.
068 Record locked.
069 Illegal argument to ISAM module.
070 Too many indexed files open.
071 Bad indexed file format.
072 End of indexed file.
073 No record found in indexed file.
074 No current record in indexed file.
075 Indexed data file name too long.
077 Internal ISAM module failure.
078 Illegal key description in indexed file.
081 Key already exists in indexed file.
100 Invalid file operation.
101 Illegal operation on an indexed file.
102 Sequential file with non-integral number of records.
104 Null file name used in a file operation.
105 Memory allocation error.
129 Attempt to access record zero of relative file.
135 File must not exist.
138 File closed with lock - cannot be opened.
139 Record length or key data inconsistency.
141 File already open - cannot be opened.
142 File not open - cannot be closed.
143 REWRITE/DELETE in sequential mode not preceded by successful READ.
146 No current record defined for sequential read.
147 Wrong open mode or access mode for READ/START.
148 Wrong open mode or access mode for WRITE.
149 Wrong open mode or access mode for REWRITE/ DELETE.
150 Program abandoned at user request.
151 Random read on sequential file.
152 REWRITE on file not opened I-O.
158 Attempt to REWRITE to a line-sequential file.
159 Malformed line sequential-file.
161 File header not found.
173 Called program not found.
180 End-of-file marker error.
182 Console input or console output open in wrong direction.
183 Attempt to open line sequential file for I-O.
188 File name too large.
193 Error in variable length count.
194 File size too large.
195 DELETE/REWRITE not preceded by a READ.
196 Record number too large in relative or indexed file.
210 File is closed with lock.
213 Too many locks.
218 Malformed MULTIPLE REEL/UNIT file.
219 Operating system shared file limit exceeded.





-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
