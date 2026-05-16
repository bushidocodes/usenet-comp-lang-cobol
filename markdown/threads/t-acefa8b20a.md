[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Today's Bit of Corporate Advice

_1 message · 1 participant · 2005-01_

---

### [OT] Today's Bit of Corporate Advice

- **From:** docdwarf@panix.com
- **Date:** 2005-01-11T08:26:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cs0k69$duu$1@panix5.panix.com>`

```

Sometimes a good one comes up that just needs to be passed along.  Someone 
in a corner office asked me about some files that he wanted to pass along 
to the folks on the Unix/Oracle side of things here; I gave him the names 
of the datasets and then added the following to my email:

--begin quoted text:

Now for a bit of Free Advice (worth at least double what you pay for it) 
from a mainframe COBOL jockey who just also happens to be a certified 
Oracle DBA:  watch out for what you do with this stuff.  The files you 
have here are designed for flat-file batch processing (multiple record 
types and variable-length records), just like an old Firestone tire was 
designed to go on a T-model Ford used on the corduroy roads of backwoods 
Tennessee... fine for hauling feed and pulling stumps but if you try to 
put this tire on a BMW 645Ci for a 100+mph cruise down the Autobahn things 
might not be too happy.

Likewise... it might be wise to consider the design of the application 
which will take advantage of these data on the Unix side before one starts 
tossing data about; to ignore the variations and differences between the 
two platforms and assume an 'all ya gotta do is load it to a table' stance 
will, most likely, result in... unpleasant surprises for all involved, if 
not immediately then shortly after these huge masses of data begin to pile 
up.

--end quoted text

As much heed might be paid to this, of course, as was paid to Cassandra's 
predictions... but sometimes one just has to.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
