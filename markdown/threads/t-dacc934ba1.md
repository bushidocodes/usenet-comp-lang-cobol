[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ODBC to MS-ACCESS

_1 message · 1 participant · 2000-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### ODBC to MS-ACCESS

- **From:** bithh@my-deja.com
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jr4u0$8ri$1@nnrp1.deja.com>`

```
I wonder if someone could give me some tips on how to formulate the
following SQL statements for the ODBC interface for MS-ACCESS:

1) EXEC SQL
     SELECT DEPTNAME, MGRNO
     INTO  :DEPTNAME, :MGRNO
     FROM DEPT
     WHERE DEPTNO = :DEPTNO
   END-EXEC

2)  EXEC SQL
      DECLARE C1 CURSOR FOR
        SELECT DEPTNO, DEPTNAME, MGRNO
        FROM DEPT
        WHERE ADMRDEPT LIKE 'AB%'
    END-EXEC

    EXEC SQL
      OPEN C1
    END-EXEC

    EXEC SQL
      FETCH C1
      INTO :DEPTNO, :DEPTNAME, :MGRNO
    END-EXEC

I am looking forward to an answer
thanks in advance


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
