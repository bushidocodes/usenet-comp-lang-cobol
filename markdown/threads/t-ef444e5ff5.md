[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q:NetExpress and DB2 Directives

_1 message · 1 participant · 2000-01_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Q:NetExpress and DB2 Directives

- **From:** Juergen@bop99.ping.de (Juergen Vetter)
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7W4jGCaWOtB@bop99.ping.de>`

```

I have to problems with NetExpress 3.0 and IBM UDB 5.x and the german
supports told me that my question is out of the support service (i can't  
agree with them).

Ok - here are the problems:
===========================
We have generate a DB2 Database with IBM UDB 5.2 in a NetExpress 3.0 Service  
Pack 1 and Windows NT Service Pack 3.0 environment.
We use a general USER.

But if i compile a cobol program with the direcitves NOACCESS,NOPRE,CTRACE i  
can see an error in the ctrace.logfile.

The precompiler want's to get access to a db2 object that should owned by  
myself. But we use a general user, so this access gets an error.

For example the general user is TEST and a view WORKER exists.
The precompiler wants to access to my own userid myid.worker instead of  
test.worker.

This isn't changed if i use the collection-id and user, password direktive.

I think the other problem is the same problem.
A compile with the directives access, pre isn't end successful.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
