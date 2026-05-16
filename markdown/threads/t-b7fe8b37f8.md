[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO: 101 encapsulation

_1 message · 1 participant · 2000-01_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO: 101 encapsulation

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3874595C.F4029B2@zip.com.au>`

```
Encapsulation as a word implies two things:  grouping and protection.  
We encapsulate our family in a car and move the whole car and contents
on holidays with us.  On the trip we are protected by a steel body.

Procedural encapsulation.

When we write a suite we typically will not write a single program
rather a series of programs, each program has a specific task, a
report, an update screen, etc.  Each program encapsulates a specific
function.

A lot of us extend this concept by creating modules to do functions
encapsulating our hard work so that we can reuse it many times, for
example creating a screen, hiding a screen, etc.

Sometimes these tools work really well as a module.  For example I
look up a postcode using a module, the first call checks it's status
buffers the postcodes into memory and subsequent calls use the
buffered copy of the table.  I could easily replace this with a
database call, a isam table, or even data entry.  This means that I
can totally replace the concept of postcode look up in all my programs
quickly, reliably, and not change any other part of the program.

There are times that modules require a bit more cleverness.  For
example a reporting module (now let's not discuss report writer, it's
an easily understood example).  This is a problem I solved in another
language so I can define it quickly.

Define the problem:

I want a module that allows up to 3 reports to be concurrently
written.  Each report will have standard heading data set by the
program and format standard heading lines based upon that data.  Each
report will have sub headings, which may change during the execution
of the report, these will appear on each page (where defined), and
finally report lines.  The report lines will be grouped and passed as
one entity each group will be kept on a page.

Interface:
  initialize:
     report filenames
     header info
  output:
     report number
     sub heading lines (and count)
     detail lines (and count)
  finalize:
     close up the files, etc.

OK now how do we achieve this in our system:

 a) provide three calls passing information in global space
 b) provide a single call with a code to tell us which function.

The first method allows the users of the system to tap into our data
and modify it without us knowing about it.  What happens when we need
to create 5 reports?

The second method breaks cohesion.  We send in information that
controls how the module is executed.  This is considered 'bad' by
structured programming guru's.

How does OO improve this situation.  We can wrap the report into a
class each instance of that class can be exactly one report.  The data
for each report is stored in the object's data area and can only be
updated by methods that the class designer allows.  This means:

	object - report
	        data:
                        filename and file descriptor
			page count
                        line count
			heading details
		methods:
			initialize
			write
			close

I can now create as many reports as I want.  I can also add a method
to retrieve the original filename without affecting any user of the
class.

This packaging of the data and object is the basis of OO.  The ability
to create many instances and, with care, those instances working
reliably no matter how many there.  There is no conflict between the
internal data.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
