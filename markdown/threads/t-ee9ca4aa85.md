[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using NetExpress Dictionary Collection Class

_1 message · 1 participant · 1998-07_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### Using NetExpress Dictionary Collection Class

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-07-01T17:31:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ne9rs$adq$1@nnrp1.dejanews.com>`

```

I am trying to use the dictionary collection class
I am getting a little confused and the samples
do not do exactly what I would like to do. I have
a need to do a key/data pair which is what the
dictionary is good for. The key data pair I
would like is defined as

key pic s9(15) comp-3.
data pic s9(9) comp-3.

The problem is I am not sure which intrinsic
data type to use since there is not a comp3
that I know of. It would be okay to use
comp5 I just wasnt sure if it would hold
the 15 significant digits I need. I tried
creating these data types as just a key of
pic x(8) and data of pic x(5) and redefining the
area on adds and pulls etc.

The whole point is I would like to be able to
load up the collection class and then register
a call back to use the select method against
that collection.

Any suggestions. Here is my sample EXE program
calling a sample class that really does the work.

Class-Control.
myDictionary is class "mydict"
.
*
WORKING-STORAGE SECTION.
*
01 aDictionary object reference value null.
*
PROCEDURE DIVISION.
*
invoke myDictionary "New" returning aDictionary.
*
invoke aDictionary "Initialization".
*
invoke aDictionary "Finalize" returning aDictionary.
*
stop run.

$set linkcount(512)
*
Identification Division.
class-id. myDictionary
inherits from Base.
*
Environment Division.
Object Section.
*
*****************************************************************
* Identify all of the classes that will be used **
*****************************************************************
*
Class-Control.
myDictionary is class "mydict"
Dictionary is class "dictinry"
CobolComp5 is class "comp5"
CallBack is class "callback"
CobolPicX is class "picx"
Association is class "associtn"
Base is class "base"
.
*
class-object.
Object-Storage Section.
End class-object.
*
OBJECT.
Data Division.
Object-Storage Section.
*
copy "78Levels".
copy "typedefs".
*
01 keySize pic x(4) comp-5 value 8.
01 dataSize pic x(4) comp-5 value 5.
01 keyTemplate object reference value null.
01 dataTemplate object reference value null.
01 dictionaryTemplate object reference value null.
01 aDictionary object reference value null.
01 resultDictionary object reference value null.
01 searchMethod object reference value null.
01 dictionarySize pic x(4) comp-5 value 50.
01 resultSize pic s9(9) comp-5 value 0.
01 displaySize pic -9(9).
*
01 keyToMatch pic x(8) value '11111111'.
*
copy V24PC204.
*
Procedure Division.
*
Method-ID. "initialization".
Environment Division.
Input-Output Section.
File-Control.
*
Data Division.
File Section.
Working-Storage Section.
Linkage Section.
*
Procedure Division.
*
*****************************************************************
* Register Call Backs **
*****************************************************************
*
invoke CallBack "New" using self "searchSequence "
returning searchMethod.
*
Invoke self "createCollection".
*
Invoke self "add".
*
Invoke aDictionary "do" using searchMethod
returning resultDictionary.
*
Invoke resultDictionary "size" returning resultSize.
*
move resultSize to displaySize.
*
display displaySize " Record(s) Matched".
*
End Method "initialization".
*
Method-ID. "createCollection".
Environment Division.
Input-Output Section.
File-Control.
*
Data Division.
File Section.
Working-Storage Section.
*
Procedure Division.
*
invoke CobolPicx "NewClass" using keySize
returning keyTemplate.
*
invoke CobolPicx "NewClass" using dataSize
returning dataTemplate.
*
invoke Association "newClass" using keyTemplate
dataTemplate
returning dictionaryTemplate
*
invoke Dictionary "ofValues" using dictionaryTemplate
dictionarySize
returning aDictionary.
*
End Method "createCollection".
*
Method-ID. "searchSequence".
Environment Division.
Input-Output Section.
File-Control.
*
Data Division.
File Section.
Working-Storage Section.
*
01 dKey pic 9(8).
*
Linkage Section.
*
01 lsKey pic x(8).
01 lsData pic x(5).
*
Procedure Division using lsKey lsData.
*
display ' Key('lsKey')'.
display 'Data('lsData')'.
*
End Method "searchSequence".
*
Method-ID. "add".
Working-Storage Section.
*
01 key1 pic x(8) value '11111111'.
01 key2 pic x(8) value '22222222'.
01 key3 pic x(8) value '33333333'.
01 key4 pic x(8) value '44444444'.
01 data1 pic x(5) value 'AAAAA'.
01 data2 pic x(5) value 'BBBBB'.
01 data3 pic x(5) value 'CCCCC'.
01 data4 pic x(5) value 'DDDDD'.
*
Procedure Division.
*
invoke aDictionary "atPut" using Key1 Data1.
invoke aDictionary "atPut" using Key2 Data2.
invoke aDictionary "atPut" using Key3 Data3.
invoke aDictionary "atPut" using Key4 Data4.
*
End Method "add".
*
Method-ID. "Finalize".
Working-Storage Section.
*
01 nullRef object reference value null.
*
Procedure Division.
*
invoke super "finalize" returning nullRef.
*
End Method "Finalize".
*
END OBJECT.
END CLASS myDictionary.


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
