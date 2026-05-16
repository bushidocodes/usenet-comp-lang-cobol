[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Functions - arguement input and "type" of returned value

_1 message · 1 participant · 2003-04_

---

### Functions - arguement input and "type" of returned value

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-15T14:01:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7hkup$rsh$1@slb9.atl.mindspring.net>`

```
Given recent "discussions" on "integer" and similar things, I thought that I
would point out the fact that the '89 ANSI Intrinsic Function Amendment
provided a table showing what type of arguments (input) each function would
accept and what the TYPE of the returned value is.  For an online version of
a SIMILAR (not identical - as it includes many IBM extensions - functions
and returned types) see,

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR10/7.1.2

However, from the ISO 2002 Standard, the following information describing
the types of returned values MIGHT help others to understand how/when COBOL
(or at least Standard COBOL) uses terms such as "integer"

NOTE WELL:
   This list includes some types of functions that do *NOT* exist in the '89
Amendment - but were introduced in the 2002 Standard.  For a full view of
all the 2002 Standard functions, see page 566 and following

"15.1 Types of functions

Types of intrinsic functions are:

1) Alphanumeric functions. These are of the class and category alphanumeric.
The number of character positions
in this data item is specified in the function definition. Alphanumeric
functions have an implicit usage display.
Unless stated otherwise in the definition of a function, the data item is
represented in the alphanumeric coded
character set in effect when the function is referenced at runtime.

2) Boolean functions. These are of the class and category boolean. The
number of boolean positions in this data
item is specified in the function definition. Boolean functions have an
implicit usage bit.

3) National functions. These are of the class and category national. The
number of character positions in this data
item is specified in the function definition. National functions have an
implicit usage national. Unless stated
otherwise in the definition of a function, the data item is represented in
the national coded character set in
effect when the function is referenced at runtime.

4) Numeric functions. These are of the class and category numeric. A numeric
function has an operational sign.

5) Integer functions. These are of the class and category numeric. An
integer function has an operational sign
and no digits to the right of the decimal point.

6) Index functions. These are of the class and category index."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
