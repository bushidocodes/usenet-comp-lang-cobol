[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus Cobol: How to stop cursor from moving?

_2 messages · 2 participants · 2002-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### Micro Focus Cobol: How to stop cursor from moving?

- **From:** ah_dallas@hotmail.com (D.T.H.)
- **Date:** 2002-07-20T18:11:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dac5a01e.0207201711.269741f4@posting.google.com>`

```
Hello Micro Focus experts, 
I have a Micro focus Cobol screen that looks like the following:
  _   customer name 1
  _   Customer name 2
  _   customer name 3
  _   Customer name ..
  _   Customer name n
This screen has a selection field and a name field.  The selection
field is a enterable field so the user can move the cursor next to the
customer and press
enter to display more information on the selected customer.  Each page
on the
screen allows 14 displayable lines.  

My problem is that, if I am at the last screen and there are only 3
customers left to be displayed, how can I prevent the user from moving
the cursor down to line #4, #5 and so on?

Appreciate any suggestion either to my email ah_dallas@hotmail.com or
posted here.

Thanks, DTH
```

#### ↳ Re: Micro Focus Cobol: How to stop cursor from moving?

- **From:** "ames J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-21T01:51:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D3A14A4.DF37B627@shaw.ca>`
- **References:** `<dac5a01e.0207201711.269741f4@posting.google.com>`

```


"D.T.H." wrote:

> Hello Micro Focus experts,
> I have a Micro focus Cobol screen that looks like the following:
…[19 more quoted lines elided]…
> Thanks, DTH

If only I could find some of my old screen code.... <G>. What you are
doing is akin to emulating a Listbox in a Windows Dialog. Using GUIs - if
the user selects from the list - with GUI-ing you are able to test if
there is an 'entry/index' at Line/Element x of the list - if not, ignore.

So you have a parallel problem. You've set yourself a maximum of 14
entries for display, so I'm assuming you are reading a file into a W/S
Table - with an OCCURS 1 to 14 depending on ws-MaxList and you are also
using the OCCURS clause in your Screen Section ? Each time you build your
table to display, you store the maximum number of entries, (ws-MaxList).
For 'full' screens this will always be 14. In the case of your last
display, your ws-MaxList =  3 - just don't allow user to select beyond 3,
i.e., they may select 4 or 5, so -   (a) Either ignore or (b) Give them an
error message.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
