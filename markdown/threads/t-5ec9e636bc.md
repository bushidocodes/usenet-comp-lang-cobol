[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I need a sample program

_6 messages · 4 participants · 2002-12_

---

### I need a sample program

- **From:** zatlas@tact.com (ZATLAS)
- **Date:** 2002-12-23T13:01:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf59aa40.0212231301.68c5cc07@posting.google.com>`

```
Hi
I am new to oo COBOL. I learn best by example. Could somebody please
send me a sample of one main program that invokes one simple class
that does nothing special (maybe a method to change a variable and a
method to look at this variable but that's all.) I am sure I can build
on this basis.
My email address is zatlas@tact.com
I thank all in advance.
Happy holidays to all.
Z. Atlas
```

#### ↳ Re: I need a sample program

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-23T23:36:29
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e07a0e0$1_1@Usenet.com>`
- **References:** `<bf59aa40.0212231301.68c5cc07@posting.google.com>`

```
You will need to tell us what compiler and OS/hardware platform.

OO COBOL varies in the details between different implementations.

There should be sample programs with your compiler.

Pete.


ZATLAS <zatlas@tact.com> wrote in message
news:bf59aa40.0212231301.68c5cc07@posting.google.com...
> Hi
> I am new to oo COBOL. I learn best by example. Could somebody please
…[7 more quoted lines elided]…
> Z. Atlas



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: I need a sample program

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-24T06:41:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021224014120.09098.00000215@mb-ct.aol.com>`
- **References:** `<bf59aa40.0212231301.68c5cc07@posting.google.com>`

```
     you can find lots of tutorial and other stuff about procedural cobol or
about object oriented (oo) cobol on the wlndows software cd (cobol ) from
microfocus.  I think it costs about $ 100 and comes with full documentation.  
  I find the older procedural cobol programs easier to work with.  if you get
the above items you can also get it at 50 percent off by being a student in the
micro focus academic type program that they offer (discount for students).
      RonGlaz6@aol.com
```

#### ↳ Re: I need a sample program

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-12-28T02:01:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E0D05CE.136CB075@shaw.ca>`
- **References:** `<bf59aa40.0212231301.68c5cc07@posting.google.com>`

```


ZATLAS wrote:

> Hi
> I am new to oo COBOL. I learn best by example. Could somebody please
…[7 more quoted lines elided]…
> Z. Atlas

I agree. I too learn best from examples. I show the difference below,
between FACTORY only and Instance methods - but chances are 90% of your
coding will
relate to creating instances. Hope the following helps. Check your
compiler's reference manuals/on-line help for syntax.

Jimmy, Calgary AB

*>------------------------------------------------------------
Program-id. Demo1.

*> This is your 'Trigger' program to get OO started.

*>Repository.
Class-Control.          FactoryDemo   is class "facdemo"
                        InstanceDemo  is class "instdemo"
                        .
Working-storage section.
01 n                            pic 9(03).
   88 GoodValue                 value 1 thru 4.
   88 QuitValue                 value 0.
01 ws1.
  05 pic x(15) value "Good day".
  05 pic x(15) value "Bonjour".
  05 pic x(15) value "Guten Tag".
  05 pic x(15) value "Buonas diaz".
  05 pic x(15) value spaces.
01 ws2 redefines ws1.
  05 ws-Text pic x(15) occurs 5.
01 occurs 4.
   05 os-Instance             object reference.

Procedure Division.
perform varying n from 1 by 1 until n > 4
  invoke FactoryDemo "setTitleOne" using n, ws-Text(n)
End-perform
perform varying n from 1 by 1 until n > 4
  invoke FactoryDemo "displayTitleOne" using n
End-perform

*> Note : While the above works, it is NOT a GOOD IDEA to rely
*> upon FACTORY variables being consistent between invokes.
*> The following two approaches are 'SAFER'

perform varying n from 1 by 1 until n > 4
  invoke FactoryDemo "displayTitleTwo" using n
End-perform
move 5 to n
move "Good afternoon" to ws-Text(n)
invoke FactoryDemo "displayOther" using n, ws-Text(n)

*> Now INSTANCES. Where I have "InstanceDemo" below, you could
*> substitute Dialog, COBOL File, a record, DB Tables accessed
*> with SQL, lists (collections/dictionaries) etc.......
*> The following can be achieved in several different ways.

perform varying n from 1 by 1 until n > 4
  invoke InstanceDemo "new" using n, returning os-Instance(n)
End-perform
perform varying n from 1 by 1 until n > 4
  invoke os-Instance(n) "passTitle" using ws-Text(n)
End-perform
Display "Instances - Enter 1 to 4 or zero to Quit"
move 99 to n
perform GET-INSTANCES until QuitValue.

STOP RUN.

GET-INSTANCES.

accept n
Evaluate true
   when GoodValue
        invoke os-Instance(n) "displayTitle"
*> when ......
*> when ......
End-evaluate.
*>-------------------------------------------------------------
*>-------------------------------------------------------------

*> This class only has methods in FACTORY

Class-id.           FactoryDemo inherits from Base.

Class-Control.      FactoryDemo is class "facdemo"
                    .
*>-------------------------------------------------------------
FACTORY.
*>-------------------------------------------------------------
*>OBJECT-STORAGE SECTION.
WORKING-STORAGE SECTION.
01 T1.
   05 T2 pic x(15) occurs 4.
01 T3.
  05 pic x(15) value "Good day".
  05 pic x(15) value "Bonjour".
  05 pic x(15) value "Guten tag".
  05 pic x(15) value "Buonas diaz".
  05 pic x(15) value spaces.
01 T4 redefines T3.
  05 T5 pic x(15) occurs 5.
*>-------------------------------------------------------------
Method-id. "setTitleOne".
*>-------------------------------------------------------------
Linkage section.
01 n                pic 9(03).
01 lnk-Text         pic x(15).
Procedure Division using n, lnk-Text.
 move lnk-Text to T2(n)
End Method "setTitleOne".
*>-------------------------------------------------------------
Method-id. "displayTitleOne".
*>-------------------------------------------------------------
Linkage section.
01 n                    pic 9(03).
Procedure Division using n.
 display "Factory - The greeting is :- " T2(n)
End Method "displayTitleOne".
*>-------------------------------------------------------------
Method-id. "displayTitleTwo".
*>-------------------------------------------------------------
Linkage section.
01 n                            pic 9(03).
Procedure Division using n.
  display "Factory - The greeting is :- " T5(n)
End Method "displayTitleTwo".
*>-------------------------------------------------------------
Method-id. "displayOther".
*>-------------------------------------------------------------
Linkage section.
01 n                            pic 9(03).
01 lnk-Text                     pic x(15).
Procedure Division using n, lnk-Text.
 move lnk-Text to T5(n)
 invoke self "displayTitleTwo" using n
End Method "displayOther".
*>-------------------------------------------------------------
END FACTORY.
*>-------------------------------------------------------------
OBJECT.       *> NOT REQUIRED
*>-------------------------------------------------------------
END OBJECT.   *> NOT REQUIRED
*>-------------------------------------------------------------
END CLASS FactoryDemo.
*>-------------------------------------------------------------
*>-------------------------------------------------------------

*>  You create 'n' number of INSTANCES using the FACTORY as a
*> template (cookie cutter)

Class-id.           InstanceDemo inherits from Base.

*> Repository.
Class-Control.      InstanceDemo is class "instdemo"
                    .
*>-------------------------------------------------------------
FACTORY.
*>-------------------------------------------------------------
Method-id. "new".
*>-------------------------------------------------------------
Linkage section.
01 n                            pic 9(03).
01 lnk-Self                     object reference.
Procedure Division using n returning lnk-Self.
  invoke super "new" returning lnk-self
  invoke lnk-self "setN" using n
End Method "new".
*>-------------------------------------------------------------
END FACTORY.
*>-------------------------------------------------------------
OBJECT.
*>-------------------------------------------------------------
OBJECT-STORAGE SECTION.      *> NetExpress requires this syntax
*>WORKING-STORAGE SECTION.   *> to work correctly on instances
01 n                                pic 9(03).
01 ws-Message                       pic x(15).
*>-------------------------------------------------------------
Method-id. "displayTitle".
*>-------------------------------------------------------------
*> Note : Using Micro Focus format - a method can consist of
*> just the code
display "Instance # " n " The greeting is - "  ws-Message
End Method "displayTitle".
*>-------------------------------------------------------------
Method-id. "passTitle".
*>-------------------------------------------------------------
Linkage section.
01 lnk-Title                        pic x(15).
Procedure Division using lnk-Title.
 move lnk-Title to ws-Message
End Method "passTitle".
*>-------------------------------------------------------------
Method-id. "setN".
*>-------------------------------------------------------------
Linkage section.
01 lnk-n                            pic 9(03).
Procedure Division using lnk-n.
  move lnk-n to n
End Method "setN".
*>-------------------------------------------------------------
END OBJECT.
*>-------------------------------------------------------------
END CLASS InstanceDemo.
*>-------------------------------------------------------------
```

#### ↳ Re: I need a sample program

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2002-12-29T03:30:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021228223056.01967.00000040@mb-df.aol.com>`
- **References:** `<bf59aa40.0212231301.68c5cc07@posting.google.com>`

```
see my posting as follows
Kobol ..........
   posted recently.
it contains a sample program.
```

##### ↳ ↳ Re: I need a sample program

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-29T18:31:10
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e0f3ce0_5@Usenet.com>`
- **References:** `<bf59aa40.0212231301.68c5cc07@posting.google.com> <20021228223056.01967.00000040@mb-df.aol.com>`

```
Not good advice, Ron.

The sample program failed to compile because it had  basic errors in it
(Missing Headers...),

But, much more importantly, it is NOT an OO COBOL program and THAT is the
sample required.

Pete.


Ron Glazier <ronglaz6@aol.comnojunk> wrote in message
news:20021228223056.01967.00000040@mb-df.aol.com...
> see my posting as follows
> Kobol ..........
>    posted recently.
> it contains a sample program.
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
