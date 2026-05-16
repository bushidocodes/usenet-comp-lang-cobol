[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Blanking out 2nd line of Ctrl Break

_5 messages · 5 participants · 1999-04 → 1999-05_

---

### Blanking out 2nd line of Ctrl Break

- **From:** dginc@tds.net
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gcln3$cnp@news2.tds.net>`

```
how do you blank out say the person name you have a single ctrl break on.  
like i want to print my report and ctrl break after each name, but i want it 
to print the name only on the first line any time after the first line if 
there is more records for that person leave only the name field blank, once 
new name is started same with it, print once and blank name on any record 
after it.
thanks
```

#### ↳ Re: Blanking out 2nd line of Ctrl Break

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3729DF76.704D@saif.com>`
- **References:** `<7gcln3$cnp@news2.tds.net>`

```
dginc@tds.net wrote:
> 
> how do you blank out say the person name you have a single ctrl break on.
…[5 more quoted lines elided]…
> thanks

Define a new variable (PREVIOUS-NAME) in working storage.

RECORD-READ-PROCESSING:
     PREVIOUS-NAME = RECORD-NAME
     READ NEXT RECORD

PRINT-PROCESSING:
     IF PREVIOUS-NAME NOT = RECORD-NAME
        move RECORD-NAME to name print area
     ELSE
        move spaces      to name print area
     END-IF
     print the detail line


You could also modify this a bit so it would also print the
name if you are printing the first detail line of a new page.

Pete
```

#### ↳ Re: Blanking out 2nd line of Ctrl Break

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3729E6DA.B6ADE1F0@NOSPAMhome.com>`
- **References:** `<7gcln3$cnp@news2.tds.net>`

```
dginc@tds.net wrote:
> 
> how do you blank out say the person name you have a single ctrl break on.
…[5 more quoted lines elided]…
> thanks

Try something like this:

  read file
  move 'garbage' to hold-name                      
  perform print-routine until file-eof
...
print-routine.
  if file-name = hold-name
     move space   to print-name
  else
     perform print-new-name
     move file-name   to print-name
                         hold-name
  end-if
  perform print detail-line
```

#### ↳ Re: Blanking out 2nd line of Ctrl Break

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gcvvk$oa6$1@news.igs.net>`
- **References:** `<7gcln3$cnp@news2.tds.net>`

```
You would do something like the following:

      perform report-customer-transaction-set until
          there-are-no-more-transactions.

  report-customer-transaction-set.
      perform report-customer-name.
      perform report-customer-transaction.

  report-customer-name.
      if customer-name is equal to last-customer-name
          continue
      else
          perform do-actual-printing
          move customer-name to last-customer-name.

  report-customer-transaction.
       perform do-actual-printing-two.
       perform get-next-transaction.

dginc@tds.net wrote in message <7gcln3$cnp@news2.tds.net>...
>how do you blank out say the person name you have a single ctrl break on.
>like i want to print my report and ctrl break after each name, but i want
it
>to print the name only on the first line any time after the first line if
>there is more records for that person leave only the name field blank, once
>new name is started same with it, print once and blank name on any record
>after it.
>thanks
```

#### ↳ Re: Blanking out 2nd line of Ctrl Break

- **From:** Ed Milne <emilne@my-dejanews.com>
- **Date:** 1999-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gdipg$po8$1@nnrp1.dejanews.com>`
- **References:** `<7gcln3$cnp@news2.tds.net>`

```
In article <7gcln3$cnp@news2.tds.net>,
  dginc@tds.net wrote:
> how do you blank out say the person name you have a single ctrl break on.
> like i want to print my report and ctrl break after each name, but i want it
…[3 more quoted lines elided]…
> after it.

If you don't want to code all the logic manually, you could use the report
writer to produce the report and stick a GROUP INDICATE clause on the field.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
