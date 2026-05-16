[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A question about REPLACE statement

_2 messages · 2 participants · 2002-07_

---

### A question about REPLACE statement

- **From:** heyanchun@163.net (He Yanchun)
- **Date:** 2002-07-16T21:07:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96959ca4.0207162007.24f4f4e@posting.google.com>`

```
Can i use REPLACE statement to replace a KEY WORD in the ENVIRONMENT
DIVISION(Input-Output Section).

Such as 
           SELECT 2100-DATA-FILE ASSIGN TO AS2100
                  ORGANIZATION   IS SEQUENTIAL
                  ACCESS         IS SEQUENTIAL
                  FILE STATUS    IS W2100-SEQ-FILE-STATUS .

Can i change "ORGANIZATION   IS SEQUENTIAL" to "ORGANIZATION   IS LINE
SEQUENTIAL".


Best Regards,
He Yanchun
```

#### ↳ Re: A question about REPLACE statement

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-07-17T04:40:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D34F5F5.D8257B7@shaw.ca>`
- **References:** `<96959ca4.0207162007.24f4f4e@posting.google.com>`

```


He Yanchun wrote:

> Can i use REPLACE statement to replace a KEY WORD in the ENVIRONMENT
> DIVISION(Input-Output Section).
…[11 more quoted lines elided]…
> He Yanchun

Yes you can - but YOU WILL GET INTO TROUBLE !!!!! You can't switch
*existing* file formats between ISAM, Relative, Sequential or Line
Sequential - it just wont work. You could play with the copy/replace
syntax to achieve what you want - but I don't believe it is worth the
effort.

You would be much better off with the following type of approach if you
want to be flexible in creating a set of file definitions :-

*>-------------- myISAM.cpy ------------------ ----------------

     select                 (tag)-File
     assign                 (tag)-Filename
     organization         indexed
     access                 dynamic
     record key           (tag)-PrimeKey
     file status              ws-fileStatus.

*>-------------------------------------------------------------

Assume you wanted the above ISAM for a CUSTOMER file :-

copy "myISAM.cpy" replacing ==(tag)== by ==CUS==. (or ==Customer==)

Note that you can have the actual filename in Working Storage together
with the file-status. Under normal circumstances you really shouldn't need
more than one file-status field, as you are checking this for the
*current* file on which you are doing an access.

Do the same type of thing for Relative, Sequential and Line Sequential :-

     select                 (tag)-File
     assign                 (tag)-Filename
     organization           relative
     access                 dynamic
     relative key           ws-RelativeKey

Note : ws-RelativeKey is in Working Storage

     Select               (tag)-File
     assign               (tag)-filename
     organization      sequential
     access              sequential
     file status          ws-filestatus.

     Select               (tag)-File
     assign               (tag)-filename
     organization      line sequential
     access              sequential
     file status          ws-filestatus.

PS: where did you learn to code :-

          SELECT 2100-DATA-FILE ASSIGN TO AS2100

It's horrible and meaningless and an absolute nightmare for somebody who
has to do maintenance on your program at  02:00 hours ! Pick clear and
simple names "CustomerFile", "TransactionFile", "InventoryFile" ,
"CustomerISAM" etc.....

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
