[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Demo: multithreading

_16 messages · 6 participants · 2004-05_

---

### Demo: multithreading

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-22T19:56:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40afadcf.145490899@news.optonline.net>`

```
*           Why are trees chopped down but wood chopped up?
*
* [Continued from trees.cbl]
*
* This demo of multithreading continues the theme of sorts and trees. It
* builds an unbalanced tree using parallel threads, then does lookups in
* parallel.
*
* There are three reasons to use multithreading:
*
* 1. To do parallel processing on multiple CPUs, as shown here.
* 2. To separate the User Interface from processing, to make
*    your application more responsive.
* 3. To handle real-time events (a variant of 2.).
*
* Multithreading is functionally the same as multitasking. The technical
* differences are one process id vs. many, and different semantics
* for starting, managing and communicating between tasks. Micro Focus
* supports multithreading with Cobol verbs start and wait, as well as a
* function library. In addition, a Cobol program can directly call the
* OS supplied threads library (where function names start with thr_).
*
* Multithreading was invented by Sybase in the late '80s to help their
* database run faster. Although tasks and threads are both dispatched by
* the operating system, some people thought a thread switch would be
* faster than a task switch. That's not true, they run at the same
* speed. But threading offers the possibility of avoiding thread
* switches by intelligently managing synchronization within the threads
* library. When that's done, threading is faster. Other reasons to use
* threading rather than tasking are Cobol library support, more robust
* synchronization and management features and because it's the norm in
* other cultures. If you write a Cobol function that will be called by
* Java or Oracle, it must be thread-safe because it WILL be in a thread.
* (That's also true of CICS and DB2, but they make you thread-safe
* automatically. You don't need to do anything special.)
*
* Multithreading in Cobol is available on Unix, Windows, NT (W2K, XP),
* OS/400, VMS, OS/2 and IBM mainframe .. since 2001 Enterprise Cobol 3.0.
*
* Making a program thread-safe requires two changes: a Local-Storage
* section to put variables on the stack, and locking Working-Storage
* (shared memory) variables before changing them. Micro Focus offers two
* compiler options.
*
* REENTRANT(2) puts Working-Storage and all compiler-generated variables
* the stack. REENTRANT(2) will make any program thread-safe by merely
* adding this option, but the threads cannot communicate with each
* other because they don't share memory. You don't have to worry about
* locks because nothing is shared.
*
* REENTRANT(1) gives real multithreading with shared Working-Storage.
*
* Reentrant(1) programs must avoid compiler-generated variables because
* they will not be put on the stack. For this reason, I changed the data
* structure from linked list to table. Linked lists require setting
* 'address of' variables (aka BLL cells), which would be shared by all
* threads. The change made it run faster -- 2.6 for case 10 went down to
* 1.7 for case 12, which is faster than the previous winner,
* radix-insertion sort.
*
* When building a tree with parallel processing, we must lock forward
* pointers before updating them to prevent 'collisions' -- two threads
* updating the same pointer at the same time. This demo shows two
* techniques for doing that. Case 13 uses mutex (mutual exclusion), the
* lowest level, fastest and universally available of the synchronization
* tools in the threads library. The others, not used here, are monitor,
* semaphore and event, which are functionally similar to mutex.
*
* A mutex is a 'token' that can have only one owner. This demo uses
* 50,000 mutexes, one per node. Before updating a node, it asks for
* exclusive ownership of the node's mutex. If ownership cannot be
* obtained, it asks the thread library to put the thread to sleep until
* the mutex is available. Then it updates the node and releases the
* mutex.
*
* Case 14 uses a novel method of self-synchronization. Rather than
* calling a library function, it avoids collisions by simply
* manipulating flags in shared memory. It uses an array of busy
* indicators, one per thread, puts its quarter on the edge of the pool
* table, then counts the number of quarters up there. If the result is
* 1, it MAY be the exclusive owner. However, while it was counting
* ..5..6..7.. another thread may have put a quarter in slot 1. Wouldn't
* thread 1 count 2 quarters and give up for awhile? Not necessarily.
* Thread 1 may be suspended during its counting. By the time it wakes
* up, this thread's quarter has been removed. To handle that case, the
* program checks whether the pointer is still zero after counting one
* stakeholder. It will see the pointer deposited by this thread and
* thereby avoid a collision.
*
* The speed difference between the two methods is dramatic. Case 13,
* mutex, took 5.9 seconds -- 3.3 times slower than single-threading.
* Case 14 took .6 seconds, 3 times faster than single-threading, on a
* machine with 4 CPUs. The mutex function overhead defeats
* multitasking's promise of higher speed due to parallel processing.
* However, self-synchronization delivers the expected performance.
*
* It is interesting to compare this demo's performance under two thread
* libraries: the typical one delivered with Solaris 5 and a 'hot' one
* from Solaris 8.
*                    Typical        Hot
* Speed (case 13)        8.0        5.9
* Collisions           1,000         30
* Task switches/sec    5,000        200
*
* How can a thread library reduce switching and collisions? For one,
* by managing the concurrency level. On a machine with 4 CPUs, 4 threads
* will run faster than 10. The other 6 just cause 'thrashing'. Collisions
* were reduced by 'spinning mutexes'. When the program tries to lock on
* a busy mutex, the thread library predicts when the mutex will be free,
* then goes .. wait .001 .. try to lock .. wait .001 .. try to lock.
* Since it doesn't return 'busy', the program doesn't count the spins as
* collisions, nor do they cause thread switches.
*
* This demo also illustrates templates and user-defined data types,
* which are in cblproto.cpy. It contains templates for Micro Focus
* functions such as CBL_MUTEX_ACQUIRE. If parameter types on the CALL do
* not match the template, the compiler issues an error. Good thing,
* because the Server Express 2.2 manual contains numerous errors. It
* would have taken a long time to find them without the template (or the
* 4.0 manual, which is correct).

---------------------------------------------------------------------
* compile: cob -xgt forest.cbl

      $SET SOURCEFORMAT"FREE"
      $SET NOBOUND
      $SET OPT(2)
      $SET NOTRUNC
      $SET IBMCOMP
      $SET NOCHECK
      $SET NOPARAMCOUNTCHECK
      $SET FASTCALLS
      $SET REENTRANT(1)
      $SET NOSERIAL
      $SET NOFIXOPT
      $SET FASTLINK

      copy 'cblproto.cpy'. *> important: function prototypes and new data types
 Identification division.
 program-id. Forest.
 author. Robert Wagner.
*                       Multithreading demo.

* results: Sun SPARC, 1.8 GHz, 4 CPU, each test was run ten times.
*                                     
*  Multithreaded tree build and lookup (similar to 10.) 
*                                                              ratio to 4+7
* 12. single-threaded               1.7                          .9
* 13. multithreaded with mutex  5.9                        3.3
* 14. self-synchronized              .6                          .3

* -- Results from previous demos ----
*                                     --- ratio ---
*  Sort only                                    2.   3.   4.   5.
*  1. Micro Focus file sort     3.7   1.0  1.5  7.4  9.3
*  2. Micro Focus table sort  3.8          1.5  7.6  9.5
*  3. qsort()                        2.5                 5.0  6.3
* 9-7 tree, to list                 1.5                        3.8
*  4. radix-insertion, to table  .5                        1.3
*  5. radix-insertion (list)        .4                       best
*
*  Misc
*  6. build tree time               1.4
*  7. search all time               1.3                     ratio to best
*                                                                     4+7
*  Sort followed by search all or tree lookup
* 2+7 MF table sort, search      5.1                        2.8
* 3+7 qsort()                           3.8                        2.1
*  8. tree, to table, search        3.5                        1.9
*  9. tree, to table faster           2.9                        1.6
* 10. tree, lookup (unbalanced) 2.6                        1.4
* 11. tree, balance, lookup       2.6                        1.4
* 4+7 radix-insertion, table        1.8                        best

 data division.
 working-storage section.

* This is the data.
 01  data-area.
     05  data-key occurs 50000.
         10  data-key-1                  pic v9(18).
         10  data-key-2                  pic v9(12).

* Data structure for a node
 01  node typedef.
     05  node-left-right occurs 2 comp    pic s9(09).
     05  node-mutex                       cblt-pointer.
     05  node-lock occurs 10      comp    pic s9(02).

* This is the tree
 01  tree-area.
     05  collisions occurs 3      comp    pic s9(09).
     05  one-node  occurs 50000           node.

 01  unqualified-variables.
     05  n-limit                  comp    pic s9(09).
     05  i                        comp    pic s9(09).
     05  thread-limit             comp    pic s9(02).
     05  thread-number            comp    pic s9(02).
     05  test-id                  comp    pic s9(02).
     05  repeat-factor            comp    pic s9(02).
     05  inserts                  comp    pic s9(09).
     05  thread-id occurs 10              thread-pointer.
     05  mutex-flags-0                    cblt-os-flags.
     05  mutex-flags-1                    cblt-os-flags.
     05  simultaneous-threads     comp    pic s9(02).
     05  maximum-threads          comp    pic s9(02).

 01  timer-variables.
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
     05  collisions-edited-area.
         10  collisions-edited occurs 3    pic  z(05).

 local-storage section.
 01  n            comp   pic s9(09).
 01  c            comp   pic s9(09).
 01  p            comp   pic s9(09).
 01  p-left-right comp   pic s9(09).
 01  t-inserts    comp   pic s9(09).
 01  node-locks   comp   pic s9(02).
 01  t            comp   pic s9(02).

 linkage section.
 01  this-thread  comp   pic s9(02).

 procedure division.
   perform construct-data

   display '12. Single-threaded'
   move 1 to thread-number, thread-limit
   move 12 to test-id
   perform timer-on
   perform repeat-factor times
       move low-values to tree-area
       call 'build-a-tree' using thread-number
       call 'tree-lookup' using thread-number
   end-perform
   perform timer-off

   display '13. Multithreaded with mutex'
   move 10 to thread-limit
   move 13 to test-id
   perform fix-concurrency
   perform timer-on
   perform repeat-factor times
       perform build-a-forest
       perform tree-lookup-threads
   end-perform
   perform timer-off

   display '14. Multithreaded, self-synchronized'
   move 14 to test-id
   perform timer-on
   perform repeat-factor times
       perform build-a-forest
       perform tree-lookup-threads
   end-perform
   perform timer-off

   goback

 . construct-data.
     move low-values to unqualified-variables
     move 10 to repeat-factor
*> Do not hardcode 50,000 here. Get node count from data description.
     compute n-limit = length of data-area / length of data-key
     perform varying i from 1 by 1 until i > n-limit
         compute data-key-1 (i) = function random
         compute data-key-2 (i) = function random
     end-perform

*> Some thread managers set the concurrency level automatically,
*> others expect you to set it. Build a forest using defaults.
*> If the number of threads is 1, set it to thread-limit + 2.
*> Non-automatic thread managers usually create two extra threads --
*> one for the thread manager and one for main(). Good thread managers
*> usually have no extras. This demo took 8.0 under a bad
*> manager vs. 5.9 under a good one.

 . fix-concurrency.
   perform build-a-forest
   if  maximum-threads equal to 1 and
       thread-limit greater than 1
       add 2 to thread-limit
       display 'Threads not working. '
               'Setting concurrency to ' thread-limit
       call 'thr_setconcurrency' using by value thread-limit
       subtract 2 from thread-limit
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
     move collisions (1) to collisions-edited (1)
     move collisions (2) to collisions-edited (2)
     move collisions (3) to collisions-edited (3)
     display  'time: ' elapsed-time
       ' collisions: ' collisions-edited-area


*> 13-14. Construct threads to do Build
 . build-a-forest.
     move low-values to tree-area
*> Construct a mutex for each node
     if  test-id equal to 13
         perform varying i from 1 by 1 until i greater than n-limit
             call "CBL_MUTEX_OPEN_INTRA" using
                 by reference node-mutex (i)
                 by value     mutex-flags-0
                 on exception
                     display 'error constructing mutex ' return-code
             end-call
         end-perform
     end-if
     move 1 to inserts *> root requires no insertion
*> Start threads
     perform varying thread-number from 1 by 1
         until thread-number > thread-limit
         start 'build-a-tree'
             using by content thread-number
             identified by thread-id (thread-number)
             on exception
                 display 'Thread creation failed ' return-code
                     space thread-number
         end-start
     end-perform
*> Wait for threads to finish
     perform varying thread-number from 1 by 1
         until thread-number > thread-limit
         wait for thread-id (thread-number)
             on exception
                 display 'Thread wait failed ' return-code
     end-perform
*> Destroy mutexes
     if  test-id equal to 13
         perform varying i from 1 by 1 until i greater than n-limit
             call "CBL_MUTEX_CLOSE" using
                 by value     node-mutex (i)
                 on exception
                     display 'error destroying mutex ' return-code
             end-call
         end-perform
     end-if
*    display 'inserts ' inserts
 . end-paragraph

*> 12-14. Build a tree
*> 12    Single-threaded call
*> 13-14 Multiple instances called by thread manager
*>   CODE FROM HERE TO THE END MUST BE THREAD-SAFE
 . entry 'build-a-tree' using this-thread.
      add 1 to simultaneous-threads
      if  simultaneous-threads > maximum-threads
          move simultaneous-threads to maximum-threads
      end-if
     move zero to t-inserts
     perform varying n from this-thread by thread-limit until n > n-limit
         move 1 to c
         perform build-a-branch
     end-perform
     add t-inserts to inserts
     subtract 1 from simultaneous-threads
     goback

*> Insert a new node into a tree.
*> Searches the tree to a leaf.
*> Constructs a new leaf linked to the previous leaf.
 . build-a-branch.
*> Entry 1 is the tree root, not linked from a parent node.
     if  n equal to 1
         exit paragraph
     end-if
*> Find a leaf.
     perform find-a-node
     if  c not equal to zero
         display 'duplicate ' n
         exit paragraph
     end-if
*> Lock the parent we are about to update.
     evaluate test-id
         when 13
             move 1 to mutex-flags-1
             call "CBL_MUTEX_ACQUIRE" using
                 by value     node-mutex (p)
                 by value     mutex-flags-1
             if  return-code not equal to zero
                 add 1 to collisions (1)
                 call "CBL_MUTEX_ACQUIRE" using
                     by value     node-mutex (p)
                     by value     mutex-flags-0
                     on exception
                         display 'acquire error ' p c return-code
                         add 1 to collisions (1)
                         go to collision-recovery
             end-if
         when 14
             perform count-locks-on-this-node
             perform until node-locks equal to 1
                 add 1 to collisions (1)
                 move zero to node-lock (p, this-thread)
                 call "CBL_THREAD_YIELD"
                 perform count-locks-on-this-node
             end-perform
     end-evaluate
*> Check for update by another thread almost in synch with this.
*> Why is this necessary for test 13? Because another thread
*> may have updated the parent between the exit from find-a-node
*> and the acquisition of the mutex.
     if  node-left-right (p, p-left-right) not equal to zero
*        display 'near miss ' n node-left-right (p, p-left-right)
         add 1 to collisions (2)
         go to collision-recovery
     end-if
*> Fanfare -- the action we've been preparing for: link parent to this.
     move n to node-left-right (p, p-left-right)
*> Unlock the parent.
     perform unlock-the-parent
*> Check again for collision not caught above. If detected, the locks
*> are not 100% leak-proof. This demo detects no tertiary collisions.
     if  node-left-right (p, p-left-right) not equal to n
*        display 'unacceptable risk ' n space node-left-right (p, p-left-right)
         add 1 to collisions (3)
         go to collision-recovery
     end-if
     add 1 to t-inserts

 . count-locks-on-this-node.
     move 1 to node-lock (p, this-thread)
     move zero to node-locks
     perform varying t from 1 by 1 until t greater than thread-limit
         add node-lock (p, t) to node-locks
     end-perform

 . unlock-the-parent.
     evaluate test-id
         when 13
             call "CBL_MUTEX_RELEASE" using
                 by value     node-mutex (p)
                 on exception
                     display 'error releasing mutex ' return-code
             end-call
         when 14
             move zero to node-lock (p, this-thread)
     end-evaluate

 . collision-recovery.
     perform unlock-the-parent
*> If my link 'stuck' to parent, remove it.
     if  node-left-right (p, p-left-right) equal to n
         move zero to node-left-right (p, p-left-right)
     end-if
*> Wait for the other thread to get out of the way.
*> It may be helpful here to wait a random or thread-specific duration.
*> Testing showed that to be unnecessary in this demo.
     call "CBL_THREAD_YIELD"
*> Restart search at the parent node.
     move p to c
     go to build-a-branch

*> 13-14. Construct threads to do lookup
 . tree-lookup-threads.
*> Start threads
     perform varying thread-number from 1 by 1
         until thread-number > thread-limit
         start 'tree-lookup'
             using by content thread-number
             identified by thread-id (thread-number)
             on exception
             display 'Thread creation failed ' return-code
                 space thread-number
         end-start
     end-perform
*> Wait for threads to finish
     perform varying thread-number from 1 by 1
         until thread-number > thread-limit
         wait for thread-id (thread-number)
             on exception
                 display 'Thread wait failed ' return-code
     end-perform
 . end-paragraph

*> Lookup 50,000 items in tree
*> 12    Single-threaded call
*> 13-14 Multiple instances called by thread manager
 . entry 'tree-lookup' using this-thread.
     perform varying n from this-thread by thread-limit until n > n-limit
         move 1 to c
         perform find-a-node
         if  c equal to zero
             display 'not found ' n
             call 'abort'
         end-if
     end-perform
     goback
*> 12-14. Find one item in tree.
*> On exit, c points to the node or zero, p points to its parent
 . find-a-node.
     perform until c equal to zero
         move c to p
         evaluate data-key (n)
             when less than data-key (c)
               move 1 to p-left-right
             when greater than data-key (c)
               move 2 to p-left-right
             when other
                 exit perform
         end-evaluate
         move node-left-right (p, p-left-right) to c
     end-perform
 .
```

#### ↳ Re: Demo: multithreading

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-22T23:08:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405222208.451245dd@posting.google.com>`
- **References:** `<40afadcf.145490899@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 

> * Multithreading was invented by Sybase in the late '80s to help their
> * database run faster. 

I think that you are quite far away from reality:

""" 1966 

[26] The UNIVAC division of Sperry Rand Corporation delivers the first
multiprocessor 1108. Each contains up to 3 CPUs and 2 I/O controllers;
its EXEC 8 operating system provides interface for multithread program
execution.

---------------- """"

> * Although tasks and threads are both dispatched by
> * the operating system, some people thought a thread switch would be
> * faster than a task switch.

I don't know _anyone_ that thought that.  What they _did_ think is
that creating a new thread would be much faster than creating a new
task.  I recall when the ICL 2900 VME/B introduced threads.  A new VM
task took around a million instructions to create while a thread
within an existing VM was just a few thousand.  VME/B was using
threads in their servers in the early 70s.

> * The speed difference between the two methods is dramatic. Case 13,
> * mutex, took 5.9 seconds -- 3.3 times slower than single-threading.
> * Case 14 took .6 seconds, 3 times faster than single-threading, on a
> * machine with 4 CPUs. 

Presumably the machine was doing nothing else at the time.  If it was
running a normal mix of jobs, as you say: hundreds of tasks, then the
chance of getting the use of 2 CPUs at the same time is negligable.
```

##### ↳ ↳ Re: Demo: multithreading

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-05-23T03:34:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DIGsApHpveKE092yn@visi.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com>`

```
Here in comp.lang.cobol, riplin@Azonic.co.nz (Richard)
spake unto us, saying:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[10 more quoted lines elided]…
>execution.

In a UNIVAC 1100 programming context, the writing of a multithreaded
application was sometimes referred to as "multiactivity" programming.

I knew people at Unisys (the folks who continue to market that mainframe
architecture as part of their Clearpath product line) who were writing
such code in the early 80's, and the concept had been around a *LONG*
time even at that point in time.

An excellent example for the curious is FANG, a file utility I've used
myself a little under OS2200, and which was written back in the early
1970's on (strangely enough) a UNIVAC 1108.

For the curious, the online FANG source browser can be found here:

  http://www.fourmilab.ch/documents/univac/fang/

Note: FANG is not written in COBOL, but in OS1100's ASM assembler (at
least I don't think it's SLEUTH or MASM).
```

##### ↳ ↳ Re: Demo: multithreading

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-05-23T16:42:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8qka40245m@news3.newsguy.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com>`

```

In article <217e491a.0405222208.451245dd@posting.google.com>, riplin@Azonic.co.nz (Richard) writes:
> robert.deletethis@wagner.net (Robert Wagner) wrote 
> 
…[10 more quoted lines elided]…
> execution.

Smotherman dates the invention of multithreading at 1950, with more
extensive developments during the '50s.[1]

> > * Although tasks and threads are both dispatched by
> > * the operating system, some people thought a thread switch would be
…[4 more quoted lines elided]…
> task.

For some OSes, threading was introduced primarily for faster context
switches (and ease of sharing data among threads of execution), not
faster process creation.  Modern Unixes that support Copy-on-Write
semantics for fork(2), assisted by capable modern MMUs, have
relatively cheap process creation, for example.

Northrup notes at various points that cheaper context switches were
a major argument for adding threading to Unix.[2]  So I'm afraid it's
not correct to say that the "faster context switch" argument was never
made.

On the other hand, for OSes with relatively expensive process creation
(such as OS/2 and Windows), task creation cost was definitely a major
driver.  And in both the Unix and the OS/2 / Windows cases IPC
performance was a concern.

In some implementations (the fairly dreadful Linux one, in kernels
prior to 2.6, for example), there's little difference between process
and thread context switches, since threads are basically just processes
sharing the same address space.

1. http://www.cs.clemson.edu/~mark/multithreading.html
2. Charles J Northrup, _Programming with UNIX Threads_ (Wiley, 1996),
   xiv, 36, etc.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-23T22:55:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40b1214d.88253462@news.optonline.net>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <c8qka40245m@news3.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote:


>In some implementations (the fairly dreadful Linux one, in kernels
>prior to 2.6, for example), there's little difference between process
>and thread context switches, since threads are basically just processes
>sharing the same address space.

The Solaris version of mpstat, which reports a lot of low-level statistics about
processor performance, does not distinguish between process and thread switches.
It reports a single number for both labelled csw (context switches).
```

##### ↳ ↳ Re: Demo: multithreading

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-23T22:55:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40b1248b.89083228@news.optonline.net>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[10 more quoted lines elided]…
>execution.

I should have said 'The first Unix thread library was written by Sybase ...'

Does anyone dispute that?

>> * The speed difference between the two methods is dramatic. Case 13,
>> * mutex, took 5.9 seconds -- 3.3 times slower than single-threading.
…[5 more quoted lines elided]…
>chance of getting the use of 2 CPUs at the same time is negligable.

This is a 'glass half full/half empty' issue. Single-threaded programs are
always in worst-case mode, even when the machine is idle. My attitude is use as
many resources as you can. Let the task manager, threads library and priorities
resolve contention, if any. Written that way, my program will run at maximum
speed when the machine would otherwise be idle.

There _were_ hundreds of processes running against my timing tests, but they
weren't doing anything. They were using 3% of CPUs time and generating 300
context switches/sec. That's sleep mode. I consider a system busy when it's
using more than 50% and 5,000 context switches.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-23T20:12:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405231912.35165f9@posting.google.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> I should have said 'The first Unix thread library was written by Sybase ...'
> 
> Does anyone dispute that?

They may well have written a library, but as a technique it was done
in Unix well before the 'late 80s'. Whether they wrote the _first_
library is not necessarily determinable.  Perhaps many others wrote
libraries but didn't tell you (or indeed anyone) about them.
 
> >Presumably the machine was doing nothing else at the time.  If it was
> >running a normal mix of jobs, as you say: hundreds of tasks, then the
> >chance of getting the use of 2 CPUs at the same time is negligable.
 
> This is a 'glass half full/half empty' issue. Single-threaded programs are
> always in worst-case mode, even when the machine is idle. My attitude is use as
> many resources as you can. Let the task manager, threads library and priorities
> resolve contention, if any. Written that way, my program will run at maximum
> speed when the machine would otherwise be idle.

There are many good uses for multi-threading.  In the case of a DBMS
and of a Web Server these are receiving many arbitrary requests from
many clients and creating a new request on each client's behalf is
sensible to allow concurrent processing of varying requirements.  The
nature of the program and it continuous use makes the cost of
multi-threading worth while.

Typical Cobol programs, including your selected 'candidate' do not fit
any of the 'good uses'.  They especially do not present any benefit
over, say, starting a second jobstream, and running several programs
together.  The cost of writing multi-threading code for such trivial
tasks as producing 3 reports, and having this in every such program
simply does not represent useful ROI.

For your 'candidate' multi-threader, here is how I would do it (if it
really was a requirement):

     Modify the program to only process once and take one parameter 
           - the file name.
     bash> candidate MT.DTA & candidate HG.DTA & candidate HG1.DTA &

Not that I believe that it will run any faster end-to-end than its
existing structure, which at least, should have the advantage of
despooling the first report after MT.DTA has been processed rather
than having to wait until the I/O
for all thre has fought itself into submission and then having to
despool all 3.


> There _were_ hundreds of processes running against my timing tests, but they
> weren't doing anything. 

Exactly.  Run your tests when it is doing typical work.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 4)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-05-24T23:47:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8u1hv021dr@news1.newsguy.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com>`

```

In article <217e491a.0405231912.35165f9@posting.google.com>, riplin@Azonic.co.nz (Richard) writes:
> robert.deletethis@wagner.net (Robert Wagner) wrote
> 
…[5 more quoted lines elided]…
> libraries but didn't tell you (or indeed anyone) about them.

The comp.os.research FAQ, in its section on the history of threading,
claims that Unix "lightweight" processes with shared address space
(ie preemptively-scheduled threads) "date[] back to the very late 70s
or early 80s, i.e. to the first `microkernels' (Thoth (precursor of
the V-kernel and QNX), Amoeba, Chorus, the RIG-Accent-Mach family,
etc)".[1]  It doesn't mention thread library implementations, but I
think the safest thing to say is that it's not clear when threads were
introduced to Unix as a facility for normal user-mode programs (as
opposed to kernel tasks).


1. http://www.serpentine.com/~bos/os-faq/FAQ-1.html#The-history-of-threads
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-24T23:40:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405242240.6d858597@posting.google.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com> <c8u1hv021dr@news1.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote 

> I think the safest thing to say is that it's not clear when threads were
> introduced to Unix as a facility for normal user-mode programs (as
> opposed to kernel tasks).

Marc J. Rochkind in 'Advanced Unix Programming' 1985 describes
creating processes using shared memory in Sys V and Xenix 3, including
how they are in use in DBMSes. It also discusses fork() and that this
is enormously expensive because it is cloning the parent.  However,
the code segments can be read-only and shared, and data segment pages
can be marked in some versions as 'copy on write' which delays, or
even avoids, copying these until the new process actually tries to
write to these.

These seem to describe user space 'lightweight' threads adequately.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-05-26T21:36:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c932l7018k1@news3.newsguy.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com> <c8u1hv021dr@news1.newsguy.com> <217e491a.0405242240.6d858597@posting.google.com>`

```

In article <217e491a.0405242240.6d858597@posting.google.com>, riplin@Azonic.co.nz (Richard) writes:
> 
> Marc J. Rochkind in 'Advanced Unix Programming' 1985 describes
…[8 more quoted lines elided]…
> These seem to describe user space 'lightweight' threads adequately.

I'd have to disagree.  Shared memory can be used to implement
threading in a fashion; that's sort of what Linux (prior to 2.6)
does.  It's a lousy approach, but you can get something like threads.
However, that's not how the Unix International MPWG (multiprocessing
working group, I believe) designed the thread model for SVR4.2 MP,
which is what Solaris and later POSIX threads were largely based on.
Those were true intraprocess threads, not multiple processes sharing
address space.  Nor was any DCE threads implementation I'm familiar
with based on multiple processes and shared memory.  And the various
pure-user- space threads implementations, whatever API they were
based on, were of necessity intra-process (since they couldn't play
any address- space tricks - they just scheduled threads within a
process by swapping contexts).

fork, with or without copy-on-write, is pretty much beside the point.
CoW fork removed some of the impetus for multithreading (since it
made forking a new process cheaper) - as well as removing much of the
justification for vfork - but it didn't provide lightweight processes
in the sense that the UI or Solaris threading implementations used
the term.  Those were "lightweight" in the sense that switching
between them was very inexpensive because the address space didn't
change.

Of course, the (much later) Linux threading implementation did use
clone(), which is basically an enhanced fork(), to implement threads
- but Linux "threads" are hardly lightweight.

It appears to me that it's still an open question when multithreading
was first available in a Unix variant for normal processes.  The best
evidence I've found so far - the comp.os.research FAQ - suggests that
it was much earlier than 1988, though, in the various microkernel
implementations.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 4)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-25T09:22:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40b30b42.213701332@news.optonline.net>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote

>There are many good uses for multi-threading.  In the case of a DBMS
>and of a Web Server these are receiving many arbitrary requests from
…[10 more quoted lines elided]…
>simply does not represent useful ROI.

Supercomputers have hundreds of CPUs. Do you think they're running hundreds of
batch jobs? Do you think they're processing hundreds of database queries? No,
they're running one program that's launched hundreds of threads.

>For your 'candidate' multi-threader, here is how I would do it (if it
>really was a requirement):
…[10 more quoted lines elided]…
>despool all 3.

Waiting for disk I/O is a holdover from the past. When opening a file of
moderate size, modern machines suck the whole file into a cache.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-25T13:03:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405251203.14a542a2@posting.google.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com> <40b30b42.213701332@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> Supercomputers have hundreds of CPUs. Do you think they're running hundreds of
> batch jobs? Do you think they're processing hundreds of database queries? No,
> they're running one program that's launched hundreds of threads.

Which is _not_ a 'typical Cobol program' that read through a file
sequentially and prints a report.

While there _are_ many good uses for multi-threading, your 'idea' that
every program should use it is just wrong.  What characterises
processes that can be threaded is the degree that they can be
asynchronous.  In a GUI the user can press whatever button they want
at any time.  In a server a request can arrive from any client in any
order.  In a super-computer the parallel calculations are handed out
and the results return when they are completed.

Data processing in 'traditional Cobol programs' isn't like that.  Now
it may be that the applications can be rewritten to be like that, by
being redesigned and re-implemented, but your suggestion that existing
code should be made multi-threaded is just nonsense.  It will not be
faster.

In any case your machine has only 4 CPUs and has hundreds or thousands
of tasks.

> Waiting for disk I/O is a holdover from the past. When opening a file of
> moderate size, modern machines suck the whole file into a cache.

It is still 'disk I/O'.  It still has to wait for the heads to move,
the disk to rotate under the heads, the blocks to transfer.  If the
OPEN causes all those transfers to take place then some other task
will have to wait until it has completed in order to have the specific
blocks that it wants come under the read head.

And exactly _what_ is 'moderate size' ?
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 5)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-05-26T21:04:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c930oj01n4o@news1.newsguy.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com> <40b30b42.213701332@news.optonline.net>`

```

In article <40b30b42.213701332@news.optonline.net>, robert.deletethis@wagner.net (Robert Wagner) writes:
> 
> Supercomputers have hundreds of CPUs. Do you think they're running hundreds of
> batch jobs? Do you think they're processing hundreds of database queries? No,
> they're running one program that's launched hundreds of threads.

Most supercomputer applications I've seen aren't.  They're either
running large, generally non-parallizable calculation problems on a
single very fast CPU (this is typically on Cray or similar hardware),
or they're running parallel problems using one single-threaded
process per CPU on a cluster system, with MPI or a similar mechanism
for coordination and data transfer.

MMP supercomputer designs are relatively uncommon now.  Clusters are
much more popular, because they're much cheaper, thanks to economies
of scale for general-purpose computers.

In any case, multithreading as it's typically used in application
programming - with threads created ad hoc for any task that might
take significant time, preemptive scheduling, no CPU binding, MxN
user-kernel relationship, etc - would be terrible for the sort of
large CPU-bound jobs that supercomputers are used to address.  Even
when a supercomputer is running a multithreaded application, it's
unlikely to look like the sort of multithreaded application most
people see.  (It should have exactly one kernel thread per CPU, each
bound to a CPU and to a single user thread, preferably without
preemptive scheduling, and the job partitioned so that
synchronization isn't necessary until the partition has been
processed.)

I'll say it again: multithreading is for programmer convenience.
It's rarely the best route to better performance.
```

###### ↳ ↳ ↳ Re: Demo: multithreading

_(reply depth: 6)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-27T01:21:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40b5406e.358407324@news.optonline.net>`
- **References:** `<40afadcf.145490899@news.optonline.net> <217e491a.0405222208.451245dd@posting.google.com> <40b1248b.89083228@news.optonline.net> <217e491a.0405231912.35165f9@posting.google.com> <40b30b42.213701332@news.optonline.net> <c930oj01n4o@news1.newsguy.com>`

```
Damn, you're good. Thanks for the CS knowledge you bring to this forum. Keep it
up.
```

#### ↳ Re: multithreading

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-05-23T13:13:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UpOdnVE8LMBIdC3dRVn-hA@giganews.com>`
- **References:** `<40afadcf.145490899@news.optonline.net>`

```
> *
> * Multithreading was invented by Sybase in the late '80s to help their
> * database run faster.

The first true multi-tasking operating system (Human V2.0, codename "Woman")
was deployed about 7,000 years ago, according to ancient document.

It employed selective memory, non-linear programming, and inductive logic.
In use, it often spawns derivative processes. We still use it today.
```

##### ↳ ↳ Re: multithreading

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-24T20:11:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10b57cnigvrqr40@corp.supernews.com>`
- **In-Reply-To:** `<UpOdnVE8LMBIdC3dRVn-hA@giganews.com>`
- **References:** `<40afadcf.145490899@news.optonline.net> <UpOdnVE8LMBIdC3dRVn-hA@giganews.com>`

```
JerryMouse wrote:

>>*
>>* Multithreading was invented by Sybase in the late '80s to help their
…[7 more quoted lines elided]…
> In use, it often spawns derivative processes. We still use it today.

Yeah, but spawning those child processes is EXPENSIVE!!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
