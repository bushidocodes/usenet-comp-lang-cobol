[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Expression evaluator using Interpreter Pattern

_3 messages · 3 participants · 2010-05_

---

### Expression evaluator using Interpreter Pattern

- **From:** Emerson <emersonlopes@gmail.com>
- **Date:** 2010-05-22T17:05:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f805f22-551d-4274-918d-b6f987371916@w3g2000vbd.googlegroups.com>`

```
Hi,

I've create a new design pattern example using OO Cobol that I would
like to share with you. This new example shows how to create an
arithmetic expression evaluator, so the application using it can
evaluate a formula such as:

((a + b) ^(c / d)) * e

or

a + b + c * (d - e)

There some limitations due the way the parser was built:

. Only one letter variables are supported
. There is no numeric literal support. All values must be hold in
variables
. Variables are case sensitive (a <> A)

Here is an example of how to use it:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAIN AS "ConsoleApplication1.Main".
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
       REPOSITORY.
           class ClassComputeFormula   as
"InterpreterPattern.ComputeFormula"
           class ClassContext          as
"InterpreterPattern.Context".

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  computeFormula    object reference ClassComputeFormula.
       01  context           object reference ClassContext.
       01  result            comp-2.
       01  displayResult     pic s9(09)v99.

       PROCEDURE DIVISION.
           invoke  ClassComputeFormula "NEW" returning computeFormula
           invoke  ClassContext "NEW" returning context

           invoke  computeFormula "SetExpression" using "((a ^ b) + c)
* d"

           invoke  context "CreateVariable" using "a", 10
           invoke  context "CreateVariable" using "b", 2
           invoke  context "CreateVariable" using "c", 2
           invoke  context "CreateVariable" using "d", 8.5

           invoke  computeFormula "SetContext" using context
           invoke  computeFormula "Evaluate" returning result

           move    result                 to  displayResult

           display displayResult

       END PROGRAM MAIN.


The OO Cobol code is an improved version of Partha Kuchana Java
Calculator sample : http://www.java2s.com/Code/Java/Design-Pattern/InterpreterPatternCalculator.htm

The article explaning the pattern implementation is under development
at www.100coolthings.net and should be available soon (I'm upgrading
the entire site infra), but the source code is available already at
http://www.codeplex.com/cobolRocks (Source section) .
```

#### ↳ Re: Expression evaluator using Interpreter Pattern

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-05-22T19:42:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jp-dnd2rnI-Y52XWnZ2dnUVZ_uidnZ2d@earthlink.com>`
- **References:** `<6f805f22-551d-4274-918d-b6f987371916@w3g2000vbd.googlegroups.com>`

```
Emerson wrote:
> Hi,
>
…[67 more quoted lines elided]…
> http://www.codeplex.com/cobolRocks (Source section) .

Thanks for the excellent example.

Here's another rendering using non-OO COBOL

       IDENTIFICATION DIVISION.
       PROGRAM-ID. FIDDLE.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
        01  MyFormula                 pic x(200) Global.
       01  Result            comp-2 Global.

       PROCEDURE DIVISION.

       Call "MakeFormula" USING MyFormula.
       Call "GET"
       Call "MULL"
       Call "PUT"
       EXIT PROGRAM.
```

##### ↳ ↳ Re: Expression evaluator using Interpreter Pattern

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-05-24T10:36:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a90b7725-21b9-455b-a802-495c9eae89b6@m33g2000vbi.googlegroups.com>`
- **References:** `<6f805f22-551d-4274-918d-b6f987371916@w3g2000vbd.googlegroups.com> <jp-dnd2rnI-Y52XWnZ2dnUVZ_uidnZ2d@earthlink.com>`

```
On May 23, 1:42 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Emerson wrote:
> > Hi,
…[91 more quoted lines elided]…
> - Show quoted text -

You won't get very far in programming umless you learn to obfuscate
your code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
