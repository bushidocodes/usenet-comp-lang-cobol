[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol assignment

_1 message · 1 participant · 1997-04_

---

### Cobol assignment

- **From:** "djam..." <ua-author-650730@usenetarchives.gap>
- **Date:** 1997-04-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33647aae.297532@news.clara.net>`

```

I would be much gratefull if I can get some help in sovling the
assignment below:
A stock movement transaction file is to be sequentiaaly processed.
The transaction records on the file are in part number order. The
part number is to be checked against a stock master file. Any
transactions for parts not on the master file are to be printed out on
an error report. The stock holding is to be adjusted according to the
quantity of the movement and whether the movement was an issue from
stock or a reciept into stock.
If the stock balance is reduced below the minimum stock holding level
or increased above the maximum stock holding level then a copy of the
stock record is wriiten to a separate disk file for later processing.
Please note that this a to be performed sequentially and that none of
the files are indexed or relative.
I have written my code to the point where the trans-file is read and
checked agaisnt the master-file ie:
evaluate true
when tpartno = mpartno
adjust stock on master record
perform read-trans-file
when tpartno
write error-rec from trans-file
end-evaluate

How do I go about checking the stock balance?
thank you
dja··.@cl··a.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
