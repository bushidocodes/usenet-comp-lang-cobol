[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data Structure Reusability

_2 messages · 2 participants · 2008-05_

---

### Data Structure Reusability

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-05-14T00:28:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b855a6fe-c5f9-4cc3-9853-5df12929d3ae@m3g2000hsc.googlegroups.com>`

```
I want to use one Data-Structure in different places along my code.
(Microsoft & Fujitso COBOL for windows 5.0)

I write my Data-Structure in "cfSTRC.cob" as:

      * Attention! <<<DG name>>> in the COPIED place HAVE TO
SPECIFIED !!!!
      * 01 CIF-DG.
          03    CIF-Name.
               05   First-Name  pic X(20)   value ' '.
               05   Last-Name   pic X(20)   value ' '.
          03    CIF-No          pic 9(10)   value  0.
          03    CIF-Address     pic X(50)   value ' '.
          03    Filler          pic X(300).

Also wrote the code below in "cfPARAM.cob" for use in Sub-Programs.

      * Attention! <<<DG name>>> in the COPIED place HAVE TO
SPECIFIED !!!!
      * 01 CIF-DG.
          02    CIF-Count       pic 999 value 0.
          02    CIF-Data occurs 1 to 200 times
                           depending on CIF-Count.
                   copy 'cfSTRC.cob'.

Then I wrote this code in my "cfDISP.cbl" for display CIF.

       01   CIF-Data-Temp.
               copy 'cfSTRC.cob'.
       01   CIF-Array.
               copy 'cfPARAM.cob'.
       linkage section.
       01   CIF-Param.
               copy 'cfPARAM.cob'.

Compiler error message was:

    43                     depending on CIF-Count.
*   5-S******************************************
**    User-name CIF-COUNT not unique
*      CIF-COUNT
*   5-S*********
**    User-name CIF-COUNT not unique
*      CIF-COUNT
*   5-S*********
**    User-name CIF-COUNT not unique
* Checking complete - errors found

If we pre-process COPY commands in the code by hand, it's related to
CIF-Param.

Now, I have two questions:
1- What is the COBOL programming strategy for code re-usability?
Specially, in the Data-Structures arena.

2- Is there any way to handle duplications like this? I interested in
reusing my code as long as possible. Can anyone in this way?
```

#### ↳ Re: Data Structure Reusability

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-14T06:01:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4hl245d93ntp32alnljmrfmiql05pv831@4ax.com>`
- **References:** `<b855a6fe-c5f9-4cc3-9853-5df12929d3ae@m3g2000hsc.googlegroups.com>`

```
On Wed, 14 May 2008 00:28:34 -0700 (PDT), amir <ahsharif@gmail.com> wrote:

>I want to use one Data-Structure in different places along my code.
>(Microsoft & Fujitso COBOL for windows 5.0)
…[54 more quoted lines elided]…
>reusing my code as long as possible. Can anyone in this way?

CIF-COUNT is qualified 'implicitly' under the 2002 Cobol standard. Unfortunately, that has
not been implemented yet. Maybe in another six years. Temporarily, you have to qualify it
explicitly.

          02    CIF-Count       pic 999 value 0.
          02    CIF-Data occurs 1 to 200 times
                           depending on CIF-Count in Here.
                   copy 'cfSTRC.cob'.

       01   CIF-Array.
               copy 'cfPARAM.cob' replacing Here by CIF-Array.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
