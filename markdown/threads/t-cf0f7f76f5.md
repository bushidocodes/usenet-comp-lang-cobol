[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Oracle optimization

_1 message · 1 participant · 2008-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Oracle optimization

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-29T20:49:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o4cu345f2r4fs8n84ppkidn7d926sf71bt@4ax.com>`

```
I wanted to delete duplicates from a non-indexed temp table containing 30K rows, 100 of
which were duplicates. First I wrote a simple self join:

delete from &temp4 where customer_id in 
(select b. customer_id from &temp4 a, &temp4 b
 where b.customer_id = a.customer_id
     and b.rowid > a.rowid
);

The statement ran 5 minutes, which is far too long (on an HP SuperDome with 16 'parallels'
and 1 TB memory). It appeared to be doing a cartesian join, although the plan did not say
so.

After I rewrote it this way, it ran in less than one second:
     
delete from &temp4
where rowid in
(select rowid from
 (select rowid, customer_id,
  rank() over (partition by customer_id order by rowid) as place_in_set
from
  (select rowid, customer_id from &temp4
   where customer_id in
   (select customer_id
    from &temp4
    group by customer_id having count(*) > 1
   )
  )
 )
 WHERE place_in_set > 1
); 

This is the sort of obfuscation the Oracle 9i optimizer forces you to write to get
acceptable performance. 

The larger script, written 100% in PL/SQL, was a weekly job that ran for eight days. After
the first rewrite, as 12 steps of straight SQL, it ran in 1 hour on 3 machines/databases,
20 hours on a 4th which seemed no different from the other 3. After applying techniques
like the above, it now runs in 5-15 minutes on all 4. The only difference was rewriting
SQL. I didn't add indexes, partition tables nor change functionality. All the job does is
find and fix the tax jurisdiction on a hundred customers per week. 

Optimization tips:

1. Operate on SETS, not individual rows. Do not use cursors. 

2. ORDERED lets you wrest control from the optimizer and specify join order manually.
Applies to SQL that joins more than two tables. Little known fact: if any table in a query
does not have statistics (normal for temp tables), you get rule based optimization,
despite Oracle's statement that it's no longer available. EXPLAIN does not tell you it's
using rule based. Rule based is available, you just can't make it the global default any
longer.  Sometimes it's better than cost based; other times it's terrible. 

You must use this if you're joining more than five tables, because the number of
permutations will exceed the (default) limit causing the optimizer to stop looking
prematurely. 

3. If a complex query is too slow, break it into simpler queries that store intermediate
results in temp tables. In theory, this should never be necessary; in practice, it can
work wonders. But first try the complex query, with subselects and multiple unions.

4. PARALLEL divides the query and runs parts of it in parallel on the server, sometimes
even when the table is not partitioned. Do not use the amateurish technique of dividing it
yourself, typically on one digit of a number, and running parallel client processes. You
need to say  'alter session enable parallel dml;' AND put a parallel hint on each table.
You do not get parallelism by default.  Gotchas: you must commit after a parallel update
step and sequences don't work right with parallel on.

5. APPEND inserts new rows at the end of a table instead of merging them. Much faster.

6. NOLOGGING when creating a new table.

7. USE_HASH. Hash joins are faster than sorts and nested loop joins, despite what the
optimizer thinks. 

8. optimizer_index_cost_adj is usually set too high or low. It strongly influences the
optimizer's decision on whether to use full table scans vs. indexes. The default is 100,
which causes too many index operations (for batch). Most DBAs set it to 20, which causes
too many full table scans. You can adjust it with 'alter session set
optimizer_index_cost_adj = 50'. This one change can be a magic bullet. The parameter does
nothing if CPU Costing (introduced in Oracle 10) is enabled. For finer control, you can
specify FULL or INDEX on individual tables. 

9. Use EXPLAIN PLAN to see the optimizer's strategy, but don't believe its numbers. Before
Oracle 10, the optimizer had no way of knowing how many rows a select would return,  so
its estimated row counts and costs  could be way off.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
