[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Null object

_2 messages · 2 participants · 1999-12_

---

### Null object

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386C18C6.7680EDFA@zip.com.au>`

```
I have a private note from Jimmy including a question about Null
Object.  I thought it might be interesting to the group to define this
clearly.  

I think it is a great way to think about your code, handy in and out
of OO code.  For example, in procedural cobol I have previously done a
call which filled out defaults when the read of a database failed,
making the rest of the program very easy.  I just did not have a name
for this technique.

A null object is one that shares the same interface as a normal object
but is not that object.  It is generally created statically (once and
only once) and referred to in place of that object when you do not
have one.

For example:

I have a company with employees, that is there is a set of employees. 
I also have another object that is an employee which is not in the set
of employees.  This object is used in place of an employee when I do
not have an incumbent in a position.  This employee has a surname of
'Vacant'.

When I want to print a structure chart I can now simply do it and the
position will show up as vacant.

very rough pseudo code

Before:
	if employee is null
		print employee-name
	else
		print "Vacant"


After:
	print employee-name.

It is when I access a set of positions the position must return a
valid object pointer not null.  If the position object returns null
then there is a programming error and an abort by the compiler
(dereferencing null) is a valid solution punishable by death of an
application.

There are times when you must know the difference (e.g. give me a list
of vacant positions).  In this case create a method that statically
returns true for a valid employee and false for the 'null' employee.

There may be many types of null objects in an application.  For
example Vacant positions and 'down sized' positions.  It is simply a
matter of creating a couple of instances that behave the way you want
them to.

For further reading please see:  Refactoring Martin Fowler ISBN
0-201-48567-2 page 260 and on.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Null object

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84ikh0$kq4$1@news.igs.net>`
- **References:** `<386C18C6.7680EDFA@zip.com.au>`

```
Interesting methodology.  Thank you.

Ken Foskey wrote in message <386C18C6.7680EDFA@zip.com.au>...
>I have a private note from Jimmy including a question about Null
>Object.  I thought it might be interesting to the group to define this
…[57 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
