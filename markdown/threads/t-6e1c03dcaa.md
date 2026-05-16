[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help with tables

_2 messages · 2 participants · 2008-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: help with tables

- **From:** canela <vferr094@alumni.uottawa.ca>
- **Date:** 2008-01-28T17:36:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a22f701b-f7c5-4c66-8c9a-e07a34a2caa6@c4g2000hsg.googlegroups.com>`
- **References:** `<f6204afb-bfeb-4859-a6bd-7a4460bda996@c4g2000hsg.googlegroups.com>`

```
okay I am thinking of doing something like this:

- storing the very first value of table 1 into table 2
so say:
idx-table2 = 1
temp-idx-table2

idx-table1 = 1
size-table1 = 500

say earlier in time i stored the first name from table1 into table 2

right before i enter this section i will

add 1 to idx-table2 (so say second time around =2)
temp-idx-table2 = 1

Perform varying 1 by 1 until ( idx-table1 > size-table1 )

  Move '0' to ws-name-found

  Perform varying 1 by 1 until ( temp-idx-table2 > (idx-table2 - 1) )
    If ws-results2-name(temp-idx-table2) = ws-results1-name(idx-
table1)
       Move '1' to ws-name-found
    end-if
  end-perform

  If ws-name-found = '0'
     Move ws-results1-name(idx-table1) to ws-results2-name(idx-table2)
     Add 1 to idx-table2
  end-if
end-perform.

I am not sure if there is something better than this. Sorry to
bother :P
```

#### ↳ Re: help with tables

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-29T01:39:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnm048$820$1@reader2.panix.com>`
- **References:** `<f6204afb-bfeb-4859-a6bd-7a4460bda996@c4g2000hsg.googlegroups.com> <a22f701b-f7c5-4c66-8c9a-e07a34a2caa6@c4g2000hsg.googlegroups.com>`

```
In article <a22f701b-f7c5-4c66-8c9a-e07a34a2caa6@c4g2000hsg.googlegroups.com>,
canela  <vferr094@alumni.uottawa.ca> wrote:
>okay I am thinking of doing something like this:

Please do something like your own homework.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
