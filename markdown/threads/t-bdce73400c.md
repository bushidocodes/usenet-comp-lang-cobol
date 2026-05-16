[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# y2k code expansion II

_2 messages · 2 participants · 1999-10_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### y2k code expansion II

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ht8ZODPzHno=NTSkfcjDBYR+TOt6@4ax.com>`

```
i also was wondering, if you came across the following code, would
this handle it?

01 trans-mmddyy.
*transaction date in mmddyy format
	05 mmdd		pic 9999.
	05 yy		pic 99.
*01 years-difference	pic 99.

*becomes

01 years-difference	pic s99.
*not a field in a file

01 cur-date.
	05 cc		pic 99.
	05 yy		pic 99.
	05 rest-data	pic 9(17).


	move function current-date to cur-date

subtract-years.
	*subtract 		yy of trans-mmddyy 
	*		from 	yy of cur-date
	*		giving	years-difference
				
	*becomes
	subtract		yy of trans-mmddyy
			from	yy of cur-date
			giving years-difference


	if years-difference is negative
		multiply years-difference by	-1
	end-if
	*anyone know an absolute value function?

	.


newsreader is lagged. please reply via email 
to gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: y2k code expansion II

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vi1mo$3f8_001@news.netdirect.net>`
- **References:** `<Ht8ZODPzHno=NTSkfcjDBYR+TOt6@4ax.com>`

```
In article <Ht8ZODPzHno=NTSkfcjDBYR+TOt6@4ax.com>,
   G Moore <gvwmoore@spam.ix.netcom.com> wrote:
+i also was wondering, if you came across the following code, would
+this handle it?

Check it and see; it's pretty straightforward. Sheesh.
[snip]
+	subtract		yy of trans-mmddyy
+			from	yy of cur-date
+			giving years-difference
+
Suppose trans-mmddyy is 123199, and cur-date is 20000101...
Do the subtraction. You get a negative number, for sure.
+
+	if years-difference is negative
+		multiply years-difference by	-1
+	end-if

Does inverting the sign produce the desired result?

+	*anyone know an absolute value function?
+
Did you ever wonder what happens if you move a negative value to an unsigned 
field ?
+
+newsreader is lagged. please reply via email 
+to gvwmoore@spam.ix.netcom.com remove the spam

Ask questions on Usenet, read the answers on Usenet.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
