[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trees

_1 message · 1 participant · 2004-05_

---

### Trees

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-01T23:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4094241b.163724348@news.optonline.net>`

```
*           I'll take Sorts And Lists for a thousand, Alex
*
* [Continued from sorts.cbl]
*
* Sorting is not an end in itself. The reason WHY we sort things is to
* increase the speed of looking things up. This program and timing
* analysis compares the total time to organize entries PLUS the time to
* find entries.
*
* Trees are another way to organize data for rapid lookups. Although not
* a sort in the usual sense, a tree can be mechanically transformed into
* an ordered list. We will see two techniques for doing that.
*
* The advantage of tree over list is that trees can be updated with
* insertions and deletions. A table can be updated only by copying the
* whole table to another location. Think of sequential files. A linked
* list can be updated rapidly, but lookups must be serial, which is slow.
*
* Trees program
*
* Features: Entry in place of paragraph name
*           Typedef
*           Pointers
*           Dynamic memory allocation
*
* In the course of writing more than a million lines of production
* Cobol, your humble reporter has been frustrated by the inability to
* pass parameters to Perform. Cobol programmers are forever writing:
*
* move xxx to foo-input
* perform convert-foo
* move foo-output to xxx
*
* What we want to say is:
*
* perform convert-foo using xxx
*
* We can .. in two ways. One way is Nested Programs, shown in sorts.cbl.
* Another is using Entry instead of paragraph names, which adds no additional
* lines of code .. at most, one line for the goback.
*
* Another advantage of Entry is that it permits recursion, automatically
* constructing and destroying variables in local-storage for each
* instance. Perform may allow recursion, but you must maintain the data stack
* yourself.
*
* Typedef lets you create a template for complex structures, then use
* it by writing a single word. Compared to copybooks, Typedef is cleaner,
* easier to read and more flexible. For example, 'node' could be 01 level
* in one place and 10 level in another. You can't do that with copybooks.
*
* Pointers have been in the ANSI Cobol standard since 1985, yet Cobol
* programmers seldom use them. The advantage of dynamic lists over
* tables created with Occurs is no practical limit on the number of
* entries. Occurs makes you guess at the maximum number, preallocates
* the worst case, and causes an abend when the maximum is exceeded.
* There is no logical reason to set a maximum unless you need the speed
* of a Search All.
*
* Test 6. Tree build
*
* Feature: Tree structure
*
* The test inserts entries into a tree. Test 10 will measure
* this time plus lookups.
*
* Test 7. Search All
*
* Measures the speed of binary lookups on a table. It is included so
* we can add to the analysis 2+7, 3+7, etc.
*
* Test 8. Tree to table
*
* Feature: Recursion
*
* The test converts a tree to a list, and thence to a table, using a
* recursive technique widely used during the 1970's. For each node, it
* converts the left and right sub-nodes (children) to lists by calling
* itself, then pastes the three lists -- Left, node, Right -- into a
* single list. It is easy to understand. Unfortunately, it runs slowly
* due to runtime overhead for recursion.
*
* Note the use of local-storage. These variables are on the stack. The
* Cobol runtime constructs a new set for every call, and destroys a set
* for every goback. Local-storage is also used to make a program
* reentrant i.e. capable of being multi-threaded.
*
* Building a tree and then converting it to a list is another sort
* algorithm.
*
*
* Test 9. Tree to table, faster
*
* Feature: Rotations
*
* Rotations are rearrangements of three nodes in order to change the
* geometry of a tree. Rightward rotation converts a left link into
* a right link; leftward rotation does the opposite. If we do enough
* right rotations, all left links will become null. All nodes will
* be on a single branch on the right side. Our tree will have become a
* linked list.
*
* Is this faster than the algorithm in problem 8? Yes, it is four times
* faster. Although rotations were known in the '70s, using them to
* transform a tree to a list was first described by Stout & Warren in
* 1986.
*
*
*     Rightward Rotation           Leftward Rotation
*     Before       After           Before        After
*        A         A
*         \         \                 A          A
*          B         C                 \          \
*         / \       / \                 B          C
*        C             B               / \        / \
*       / \           / \                 C      B
*          1         1                   / \    / \
*                                       1          1
*
* Test 10. Tree lookup
*
* Measures the time to build an unbalanced tree and do lookups on it.
*
*
* Test 11. Balancing a tree
*
* Feature: Balancing algorithm
*
* The tree we built in test 6 is unbalanced. Branch lengths range from 5
* nodes to 35. It is also incomplete or sparse. Leaves -- nodes with
* fewer than two children -- are distributed throughout the tree. Lookups
* would be faster if we could balance the tree by making all branches the
* same length, plus or minus one, and push all leaves to the bottom layer.
* The theoretical lookup speed on a balanced tree is log2(N) - (log2(N)/N)/2),
* the same as a binary table search.
*
* The first step in tree balancing is converting it to one branch,
* sometimes called a vine, as we did in test 9. We can then transform
* that branch into a balanced and complete tree by doing leftward
* rotations. They must be done just right. If we do too few, the tree
* will lean to the right; too many will make it left to the left. If we
* do too many at high levels, the result will be a skinny tree with a
* few very long branches.
*
* The algorithm used was first described (almost) by A. Colin Day in
* 1976, then refined by Rolfe in 2002. It calculates the number of
* bottom layer leaves, and walks the right leg doing that many leftward
* rotations. For each complete layer above the bottom, the number of
* rotations is the number of nodes on that layer. The result is a
* perfectly balanced tree.
*
* Doesn't all this balancing consume more time than it saves? By
* coincidence, our test case is sitting on the breakeven point. When
* the number of lookups exceeds the number of nodes, balancing is
* warranted. Our tree has 50,000 nodes and we did 50,000 lookups. The
* unbalanced build and look time in test 10 is equal to the balanced
* build and look time in test 11.
*
* Conclusion
*
* The winner is radix-insertion, convert to table, use binary lookup.
* Finishing second through fifth are the tree-oriented methods.
* Last place goes to the Micro Focus sort, almost three times slower.
* ---------------------------------------------------------------------


      $SET SOURCEFORMAT"FREE"
      $SET NOBOUND
      $SET OPT"2"
      $SET NOTRUNC
      $SET IBMCOMP
      $SET NOCHECK
 identification division.
 program-id. Trees.
 author. Robert Wagner.
* Compare speed of four tree builds and lookups.

* results: Sun SPARC, 1.8 GHz, each test was run ten times.
*                                     --- ratio ---
*  Sort only                           2.   3.   4.   5.
*  1. Micro Focus file sort     3.7   1.0  1.5  7.4  9.3
*  2. Micro Focus table sort    3.8        1.5  7.6  9.5
*  3. qsort()                   2.5             5.0  6.3
* 9-7 tree, to list             1.5
*  4. radix-insertion, to table  .5                  1.3
*  5. radix-insertion (list)     .4                 best
*
*  Misc
*  6. build tree time           1.4
*  7. search all time           1.3                     ratio to best
*                                                          4+7
*  Sort followed by search all or tree lookup
* 2+7 MF table sort, search     5.1                        2.8
* 3+7 qsort()                   3.8                        2.1
*  8. tree, to table, search    3.5                        1.9
*  9. tree, to table faster     2.9                        1.6
* 10. tree, lookup (unbalanced) 2.6                        1.4
* 11. tree, balance, lookup     2.6                        1.4
* 4+7 radix-insertion, table    1.8                        best

 data division.
 working-storage section.
* The data being sorted.
* This is input to the sort and output for those returning a table.
 01  test-data.
     05  radix-columns               comp  pic s9(02).
     05  test-number                 comp  pic s9(02).
     05  card      occurs 50001 indexed
            x-n first-n last-n previous-n-0 previous-n-1 previous-n-2 x-last
            ascending key sort-key.
         10  sort-key.
             15  key-column occurs 15 indexed x-c comp-x pic xx.
         10  next-n                             index.
         10  next-n-1                           index.

 01  initialization-data.
     05  init-columns value zero     comp  pic s9(02).
     05  init-number  value zero     comp  pic s9(02).
     05  init-card occurs 50001 indexed i-n i-next i-last.
         10  init-key.
             15  init-key-1                pic v9(18).
             15  init-key-2                pic v9(12).
         10  init-next                     index.
         10  init-next-1                   index.

 01  timer-variables.
     05  repeat-factor value 10      comp  pic s9(09).
     05  previous-key                      pic  x(30).
     05  card-count                  comp  pic s9(09).
     05  start-time.
         10  start-hours                   pic  9(02).
         10  start-minutes                 pic  9(02).
         10  start-seconds                 pic  9(02).
         10  start-hundredths              pic  9(02).
     05  end-time.
         10  end-hours                     pic  9(02).
         10  end-minutes                   pic  9(02).
         10  end-seconds                   pic  9(02).
         10  end-hundredths                pic  9(02).
     05  elapsed-time                      pic  z(04).9.

* Tree sort variables
 01  node typedef.
     05  node-data      pic  x(30).
     05  node-left      pointer.
     05  node-right     pointer.
 01  new-data           node.
 01  tree-root          pointer.
 01  last-left          pointer.
 01  last-right         pointer.
 01  entry-count comp   pic s9(09).
 01  tree-size   comp   pic s9(09).
 01  iterations  comp   pic s9(09).
 01  super-root         node.

 local-storage section.
 01  left-list          pointer.
 01  right-list         pointer.

 linkage section.
 01  root               pointer.
 01  a                  node.
 01  b                  node.
 01  c                  node.

 procedure division.
   perform construct-data

   display ' 6. Tree sort N log2(N)/2'
   move 6 to init-number
   perform timer-on
   perform repeat-factor times
       perform initialize-test-data
       call 'tree-sort'
   end-perform
   perform timer-off
   call 'tree-to-list-by-recursion' using tree-root
   call 'list-to-table' using tree-root
   perform verify-sort

   display ' 8. Tree and search all'
   move 8 to init-number
   perform timer-on
   perform repeat-factor times
       perform initialize-test-data
       call 'tree-sort'
       call 'tree-to-list-by-recursion' using tree-root
       call 'list-to-table' using tree-root
       call 'search-lookup'
   end-perform
   perform timer-off
   perform verify-sort

   display ' 9. Tree, faster table, search all'
   move 9 to init-number
   perform timer-on
   perform repeat-factor times
       perform initialize-test-data
       call 'tree-sort'
       call 'tree-to-list-by-rotation' using tree-root
       call 'list-to-table' using tree-root
       call 'search-lookup'
   end-perform
   perform timer-off
   perform verify-sort

   display ' 7. Search time'
   move 7 to init-number
   perform timer-on
   perform repeat-factor times
       call 'search-lookup'
   end-perform
   perform timer-off

   display '10. Tree and lookup in unbalanced tree'
   move 10 to init-number
   perform timer-on
   perform repeat-factor times
       perform initialize-test-data
       call 'tree-sort'
       call 'tree-lookup'
   end-perform
   perform timer-off

   display '11. Tree and lookup in balanced tree'
   move 11 to init-number
   perform timer-on
   perform repeat-factor times
       perform initialize-test-data
       call 'tree-sort'
       call 'tree-to-list-by-rotation' using tree-root
       call 'list-to-balanced-tree' using tree-root
       call 'tree-lookup'
   end-perform
   perform timer-off

   goback

 . construct-data.
   set x-last, i-last to 50001
   perform varying i-n from 1 by 1 until i-n > i-last
       compute init-key-1 (i-n) = function random
       compute init-key-2 (i-n) = function random
       set i-next to i-n
       set i-next up by 1
       set init-next (i-n) to i-next
       set init-next-1 (i-n) to i-last
   end-perform
   move high-values to init-card (i-last)

 . initialize-test-data.
   move initialization-data to test-data
   set first-n to 1

 . verify-sort.
   move zero to previous-key, card-count
   set x-n to first-n
   if  x-n equal to x-last
       display 'test failed, no first'
   end-if
   perform until x-n equal to x-last
       if  sort-key (x-n) not greater than previous-key
           display 'test failed '
               previous-key space sort-key (x-n)
           set x-n to x-last
       else
           move sort-key (x-n) to previous-key
           if  init-columns not equal to zero
               set x-n to next-n (x-n)
           else
               set x-n up by 1
           end-if
           add 1 to card-count
       end-if
   end-perform
   if  card-count not equal to 50000
       display 'test failed, count is ' card-count
   end-if

 . timer-on.
     accept start-time from time
 . timer-off.
     accept end-time from time
     compute elapsed-time rounded =
        (((((((end-hours * 60) +
           end-minutes) * 60) +
           end-seconds) * 100) +
           end-hundredths) -
         ((((((start-hours * 60) +
           start-minutes) * 60) +
           start-seconds) * 100) +
           start-hundredths)) / 100
     display  elapsed-time ' seconds'
 . end-paragraph.

* 6. Performance of tree sort.
* Convert an unordered table to a tree.        .
 . entry 'tree-sort'.
     set tree-root to null
     perform varying x-n from 1 by 1 until x-n equal to x-last
         move sort-key (x-n) to node-data in new-data
         call 'tree-insert' using tree-root
     end-perform
     goback

* 6. Insert a new node into a tree.
* Searches the tree to a leaf.
* Constructs a new leaf linked to the previous leaf.
* When using recursive calls, time is 5.9
* When using non-recursive perform, time is 1.4 -- 4.2 times faster
 . entry 'tree-insert' using root.
     perform until root equal to null
         set address of a to root
         evaluate node-data in new-data
             when less than node-data in a
               set address of root to address of node-left in a
             when greater than node-data in a
               set address of root to address of node-right in a
             when other
                 display 'duplicate ' node-data in new-data
                 exit perform
         end-evaluate
     end-perform
     if  root equal to null
         call 'malloc' using by value length of a returning root *> constructor
         set address of a to root
         move low-values to a
         move node-data in new-data to node-data in a
     end-if
     goback

* 8. Convert the tree to a linked list, recursively. This algorithm is
* intuitively obvious, but recursive calls are slow. A faster
* solution is below.

 . entry 'tree-to-list-by-recursion' using root.
      if  root equal to null
          goback
      end-if
      set address of a to root

* Convert left and right sub-trees to linked lists.
      set left-list to node-left in a
      set right-list to node-right in a
      call 'tree-to-list-by-recursion' using left-list
      call 'tree-to-list-by-recursion' using right-list

* Make root a list of one entry
      set node-left  in a to root
      set node-right in a to root

* Link the three lists together
      call 'tree-append' using left-list, by value root
      call 'tree-append' using left-list, by value right-list
      set root to left-list
      goback

* 8. Splice two linked lists
* Input: two circular linked lists
* Output: a single linked list
 . entry 'tree-append' using root b.
     if  root equal to null
         set root to address of b
         goback
     end-if
     if  address of b equal to null
         goback
     end-if
     set address of a to root

     set last-left  to node-left in a
     set last-right to node-left in b

     call 'tree-join' using last-left,  b
     call 'tree-join' using last-right, a

     goback

* 8. Join two list nodes so the second follows the first.
 . entry 'tree-join' using root b.
     set address of a to root
     set node-right in a to address of b
     set node-left  in b to address of a
     goback

* 9 & 11. Convert a tree to a linked list by rightward rotations.
* Same result as above, runs four times faster, has less code.
* Not intuitively obvious.
* A rightward rotation looks like this:
*
*    Before       After
*       A         A
*        \         \
*         B         C
*        / \       / \
*       C   3         B
*      / \           / \
*         1         1
*
* We keep rotating B until its left link is null, then take a step
* down the right leg. When finished all left links are null.
* The tree is a single branch containing all nodes. In other words,
* the right side of root is a linked list.
*
 . entry 'tree-to-list-by-rotation' using root.
     move low-values to super-root
     set node-right in super-root to root
     set address of a to address of super-root
     set address of b to root
     move zero to entry-count
     perform until address of b equal to null
* If nothing on the left, walk down the right side
         if  node-left in b equal to null
             set address of a to address of b
             set address of b to node-right in b
             add 1 to entry-count
         else
* else do a rightward rotation
             set address of c to node-left in b
             set node-left in b to node-right in c
             set node-right in c to address of b
             set address of b to address of c
             set node-right in a to address of c
         end-if
    end-perform
    set root to node-right in super-root
    goback

* 8 & 9. Convert a linked list to a table
 . entry 'list-to-table' using root.
     set address of a to root
     perform varying x-n from 1 by 1 until x-n = x-last
       move node-data in a to sort-key (x-n)
       set address of a to node-right in a
*      call 'free' using by value node-left in a *> destructor
*       Above line commented out because it causes the program to abend
*       at the very end. Appears to be a call stack leak in Solaris.
     end-perform
     goback

* 11. Convert a linked list to a balanced tree

* Starting with the linked list created above, we will make a balanced
* and complete tree by applying leftward rotations.

* Balanced means all branches are the same length, plus or minus one.
* Complete means all nodes have two branches, except the bottom leaves.


* A leftward rotation looks like this:
*
*    Before           After
*
*       A             A
*        \             \
*         B             C
*        / \           / \
*           C         B
*          / \       / \
*         1             1

 . entry 'list-to-balanced-tree' using root.
* Construct a temporary super-root so there's no special handling for root
     move low-values to super-root
     set node-right in super-root to root

* Find the nearest power of 2 above the table size. In this case 65,536.
* The height of our tree will be log2(that number) = 16
* Do rotations for the incomplete bottom level
* The number of iterations is the number of occupied leaves
     move 1 to tree-size
     perform until tree-size greater than entry-count
         compute tree-size = tree-size + tree-size + 1
     end-perform
     compute iterations = entry-count - (tree-size / 2)
     call 'rotate-left' using super-root

* Do a rotation for each of other (15) complete levels
* The number of iterations is the number of nodes at the level
     move tree-size to iterations
     perform until iterations not greater than 1
         divide 2 into iterations
         call 'rotate-left' using super-root
     end-perform

    set root to node-right in super-root
    goback

 . entry 'rotate-left' using a.
     set address of b to node-right in a
     perform iterations times
         set address of b to node-right in a
         if  node-right in a equal to null or
             node-right in b equal to null
             exit perform
         end-if
         set address of c    to node-right in b
         set node-right in a to node-right in b
         set node-right in b to node-left in c
         set node-left in c to address of b
         set address of a to address of c
     end-perform
     goback

* 7. Lookup 50,000 items in table
 . entry 'search-lookup'.
     perform varying i-n from 1 by 1 until i-n equal to i-last
         move init-key (i-n) to node-data in new-data
         call 'search-find'
     end-perform
     goback

* 7. Lookup one item in table using Search All
 . entry 'search-find'.
     search all card
         at end display 'not found ' node-data in new-data
         when sort-key (x-n) equal to node-data in new-data
             continue
     end-search
     goback

* 10 & 11. Lookup 50,000 items in tree
 . entry 'tree-lookup'.
     perform varying i-n from 1 by 1 until i-n equal to i-last
         move init-key (i-n) to node-data in new-data
         call 'tree-find' using tree-root
     end-perform
     goback

* 10 & 11. Find one item in tree, non-recursively
 . entry 'tree-find' using root.
     set address of a to root
     perform until address of a equal to null
         evaluate node-data in new-data
             when less than node-data in a
               set address of a to node-left in a
             when greater than node-data in a
               set address of a to node-right in a
             when equal to node-data in a
                 exit perform
         end-evaluate
     end-perform
     goback
 .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
