[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed files...

_3 messages · 3 participants · 1998-12_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed files...

- **From:** Quan Ngo <le_spaceboy@usa.net>
- **Date:** 1998-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3679DD4D.255A14E6@usa.net>`

```
Hi,

What does an indexed file supposed to look like...?

if you have let's say this kind of data to index:

    1200420401
    1202420411
    1207420919
    1208420919
    1209420919
    1215420912
    1220420912
    1225420911

with the following, the record key being SECTION-NUM:

 DATA DIVISION.
 FILE SECTION.
 FD SECTIONS-FILE-IN     LABEL RECORDS ARE STANDARD
                         RECORD CONTAINS 10 CHARACTERS.
 01 SECTIONS-REC-IN.
    05 SECTION-NUM-IN               PIC X(4).
    05 COURSE-NUM-IN                PIC X(6).


I get in my indexed file a bunch of odd characters, is it normal?
I can see the data I indexed though.

ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
1202420411ï¿½
1207420919ï¿½
1208420919ï¿½
1209420919ï¿½
...

Thanx.
```

#### ↳ Re: Indexed files...

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74qe2.236$bJ4.448695@news2.mia>`
- **References:** `<3679DD4D.255A14E6@usa.net>`

```
The internal format of indexed files is almost always proprietary to
the specific compiler.  Unless you happen to know the format, it is
really pointless to examine the file in the manner as you have below.
Would you examine a Microsoft Access file in the same way and expect
to understand what you see? :-)
```

#### ↳ Re: Indexed files...

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3681456f.0@news3.uswest.net>`
- **References:** `<3679DD4D.255A14E6@usa.net>`

```
I'll prefix this whole thing with: I work on an IBM mainframe running
MVS/XA, COBOL II, and some version or other of VSAM.

If you are referring to a file indexed by a key (instead of a relative
record number), and you need to create such a file with data you have at
hand, you need to do a few things.

1-Decide what information in each record makes it different from every other
record.  This will be the "key".  That "key" will be identified in your
COBOL as a elementary or sub-group item under some 01 level group item
(unless, somehow, your key is the entire record).  On the SELECT statement,
you have to name that same data-item (no PIC on the SELECT, just the name).

2-You usually run the IDCAMS utility to create a "definition record"
(cluster, in vsam talk).  Then you run your COBOL program, and the program
on the operating system get together with various vsam routines (and the
data in the cluster) to start putting new records into the indexed file
whenever WRITE statements occur.

3-Once you have your key field defined in the record layout, and the key
field named on the SELECT statement (this is assuming you are taking data
from a flat file and putting into the indexed file), you need to make sure
the data in the flat file is ready to be loaded.  What do I mean by "ready"?
Well, the data in the key field (at least on mainframes), MUST be in
ascending order.  You ask why?  Especially when indexed files are capable of
inserting records anywhere depending on their key value?  Well, usually when
you load records to an indexed file, you don't access that file RANDOMly.
Why?  Because if all you are doing is putting one record in after another,
the overhead of RANDOM processing can be very slow.  If you specify
SEQUENTIAL, and have all those flat file records in order by ascending key
field value, then your data load will go much faster.

4-What will your data "look like"?  Using either an editor capable of
reading your implementation of indexed files (or, as one person has already
recommended, reversing the process I just mentioned (that is, unload your
indexed files to a sequential file)), it should look just the same as when
you you were able to look at it in the original sequential file.  On my
system, when I use FileAid to look at indexed files, it separates the key
fields from other fields with an empty column, and changes the color of the
characters in those fields to highlight them.


  Quan Ngo wrote in message <3679DD4D.255A14E6@usa.net>...
  Hi,
  What does an indexed file supposed to look like...?

  if you have let's say this kind of data to index:

      1200420401
      1202420411
      1207420919
      1208420919
      1209420919
      1215420912
      1220420912
      1225420911

  with the following, the record key being SECTION-NUM:

   DATA DIVISION.
   FILE SECTION.
   FD SECTIONS-FILE-IN     LABEL RECORDS ARE STANDARD
                           RECORD CONTAINS 10 CHARACTERS.
   01 SECTIONS-REC-IN.
      05 SECTION-NUM-IN               PIC X(4).
      05 COURSE-NUM-IN                PIC X(6).


  I get in my indexed file a bunch of odd characters, is it normal?
  I can see the data I indexed though.

  �����������������������������������������������������������������
  1202420411�
  1207420919�
  1208420919�
  1209420919�
  ...

  Thanx.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
