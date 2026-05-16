[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# D - problem with program

_10 messages · 5 participants · 1999-04_

---

### D - problem with program

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990414135500.00319.00000681@ng-fp1.aol.com>`

```
        Here is what the problem is: I am trying 
        to delete all values input for stock#1 in 
        A121-EnterStockData by setting
        them to 0's but its giving me an error.                                
                              
        I also need to change any single field
        in A12E-updatestockdata, for ex: from 1 to 2.


       IDENTIFICATION DIVISION.

       PROGRAM-ID. blah-blah.
 

       ENVIRONMENT DIVISION.

       CONFIGURATION SECTION.
       SOURCE-COMPUTER. Compaq-Presario-7170.
       OBJECT-COMPUTER. Compaq-Presario-7170.

       INPUT-OUTPUT SECTION.

       FILE-CONTROL.

           SELECT BookStock
           ASSIGN TO DISK
               ORGANIZATION IS INDEXED
               ACCESS MODE  IS DYNAMIC
               RECORD KEY   IS BookStockKey
               FILE STATUS  IS BookStockStatus.



       DATA DIVISION.

       FILE SECTION.

       FD BookStock
          VALUE OF FILE-ID IS "BOOKSTOC.DAT".

       01 BookStockRecord.
          05 BookStockKey.
             10 BookStockStocknum PIC 9(3).
          05 BookStockCodesell    PIC X(5).
          05 BookStockCodehire    PIC X(5).
          05 BookStockLevelhire   PIC 9.
          05 BookStockLevelsell   PIC 9(3).



       WORKING-STORAGE SECTION.

      * 
      * General Constants                        
      *                                                                  
       78  ItIsFalse    VALUE 0.
       78  ItIsTrue     VALUE 1.


      *
      * File Input\Output Control Constants                 
      *                                                                  
       78  IOisSuccessful VALUE "00".

      *                                                                 
      * Flow of Control Constants                     
      *                                                                  
       78  StockFileWillBeMaintained VALUE 1.
       78  QuitProgram               VALUE 2.
      *
       78  AddStockData      VALUE 1.
       78  UpdateStockData   VALUE 2.
       78  DeleteStockData   VALUE 3.
       78  ViewStockData     VALUE 4.
       78  QuitStockMenu     VALUE 5.

      *                                                                  
      * Flow of Control Switches                       
      *                                                                  
       77  FatalIOErrorHasOccured     PIC 9(001).
       77  MainProcessIsOver          PIC 9(001).
       77  StockFileMaintenanceIsOver PIC 9.

      *                                                                  
      * General Variables                         
      *                                                                  

       77  BookStockStatus PIC X(2).
       77  ResponseOfUser  PIC 9.

       01 WBookStockRecord.
          05 WBookStockKey.
             10 WBookStockStocknum PIC 9(3).
          05 WBookStockCodesell    PIC X(5).
          05 WBookStockCodehire    PIC X(5).
          05 WBookStockLevelhire   PIC 9.
          05 WBookStockLevelsell   PIC 9(3).


 
       PROCEDURE DIVISION.

      *                                                                  
      * DECLARATIONS                             
      *                                                                  

       DECLARATIVES.

       INPUT-OUTPUT-ERROR SECTION.
           USE AFTER STANDARD ERROR PROCEDURE ON I-O.
       CheckFatalErrors.
           Move ItIsTrue to FatalIOErrorHasOccured.
           Perform A113-EndProgram

       END DECLARATIVES.

      *                                                                  
      * Main Procedure                          
      *                                                                  
       A000-ProgramStockCon.
           Perform A111-StartProgram.
           Perform A112-DoMainProcess.
           Perform A113-EndProgram.

      *                                                                  
      * Start Program                           
      *                                                                  
       A111-StartProgram.
           Move ItIsFalse to FatalIOErrorHasOccured.
           Perform A11Q-CheckIfFilesExist.
           Perform A114-OpenBookStock.

      *                                                                  
      * Check if files exist                         
      *                                                                  

       A11Q-CheckIfFilesExist.
           Open Input BookStock.
           If BookStockStatus = IOisSuccessful
               Perform A11J-CloseBookStockFile
           Else
               Display " "
               Display "Data has not yet been created!"
               Display " "
               Display "1)Create the data  2)Quit the program"
               Accept ResponseOfUser
               IF ResponseOfUser < StockFileWillBeMaintained or
                  ResponseOfUser > QuitProgram THEN
                  Display ResponseOfUser " is an invalid response!"
                  Display "Please try again."
                  Display " "
                  Perform A11Q-CheckIfFilesExist
               ELSE
                  Perform A11R-ExecuteSelectedFunction
           End-if.

      *                                                                  
      * Close BookStock                         
      *                                                                  
       A11J-CloseBookStockFile.
           Close BookStock.
           If BookStockStatus not = IOisSuccessful
               Perform A11K-FatalError
           End-If.

      *                                                                  
      *  Fatal Error                       
      *                                                                  

       A11K-FatalError.
           Display "Fatal error in A11K ".
           Stop Run.

      *                                                                  
      * Executes Selected Function                      
      *                                                                  
       A11R-ExecuteSelectedFunction.
               if ResponseOfUser = StockFileWillBeMaintained
                                   Perform A11S-CreateFiles
               else
                                   Perform A11T-ExitProgram
               end-if.
      *                                                                  
      * Creates Files                           
      *                                                                  

       A11S-CreateFiles.
           Perform A11U-CreateBookStock.

      *                                                                  
      * Create BookStock                          
      *                                                                  

       A11U-CreateBookStock.
           Open Output BookStock.
           If BookStockStatus = IOisSuccessful
               Perform A11J-CloseBookStockFile
           Else
               Perform A11V-FatalError
           End-If.

      *                                                                  
      *  Fatal Error                       
      *                                                                  

       A11V-FatalError.
           Display "Fatal error in A11V ".
           Display "BookStockStatus = " BookStockStatus.
           Stop Run.

      *                                                                  
      * Exit Program                           
      *                                                                  

       A11T-ExitProgram.
           Display " ".
           Display "goodbye!".
           Stop Run.


      *
      * Open BookStock                           
      *                                                                  

       A114-OpenBookStock.
           Open i-o BookStock.
           If BookStockStatus not = IOisSuccessful
               Perform A117-FatalError
           End-If.
      
      *                                                                  
      *  Fatal Error                       
      *                                                                  

       A117-FatalError.
           Display ResponseOfUser " is an invalid response.".
           Display " ".
      *    Perform A000-ProgramStockCon.
           Stop Run.

      *                                                                  
      * Do Main Process                         
      *                                                                  

       A112-DoMainProcess.
           Move ItIsFalse to MainProcessIsOver.
           Perform A11B-MainProcess.

      *                                                                  
      *  Main Process                        
      *                                                                  

       A11B-MainProcess.
           Perform A11C-MainProcess
           until MainProcessIsOver = ItIsTrue.

       A11C-MainProcess.
           Perform A11D-DisplayMainMenu.
           Perform A11F-ExecuteSelectedFunction.
      
      *                                                                  
      * Display Main Menu                         
      *                                                                  

       A11D-DisplayMainMenu.
           Display " ". 
           Display "Your choice: ".
           Display "1)Main Menu 2)End Program".
           Accept ResponseOfUser.

      *                                                                  
      * Execute Selected Function                      
      *                                                                  

       A11F-ExecuteSelectedFunction.
               if ResponseOfUser = StockFileWillBeMaintained
                                   Perform A11G-MaintainStockFile.
               if ResponseOfUser = QuitProgram
                   Move ItIsTrue to MainProcessIsOver
               else
                   Display ResponseOfUser " is an invalid response!"
                   Display "Please try again."
                   Display " "
               End-If.

      *                                                                  
      * Maintain Stock File                        
      *                                                                  
       A11G-MaintainStockFile.
           Move ItIsFalse to StockFileMaintenanceIsOver.
           Perform A12B-DoMaintainStockFile.

      *                                                                  
      * Do Maintain Stock File                       
      *                                                                  
       A12B-DoMaintainStockFile.
           Perform A12C-DoMaintainStockFile
           until StockFileMaintenanceIsOver = ItIsTrue.

       A12C-DoMaintainStockFile.
           Perform A12H-GetUserChoice.
           Perform A12I-ExecuteSelectedFunction.

      *                                                                  
      * Get User Choice                         
      *                                                                  

       A12H-GetUserChoice.
           Display " "
           Display "1)Add record    2)Update record"
           Display "3)Delete Record 4)View record"
           Display"           5)Quit"
           Accept ResponseOfUser.

      *                                                                  
      * Execute Selected Function                      
      *                                                                  

       A12I-ExecuteSelectedFunction.
           Evaluate True
               When ResponseOfUser = AddStockData
                                   Perform A12D-AddStockData 
               When ResponseOfUser = UpdateStockData
                                   Perform A12E-UpdateStockData 
               When ResponseOfUser = DeleteStockData
                                   Perform A12F-DeleteStockData 
               When ResponseOfUser = ViewStockData                
                                   Perform A12G-ViewStockRecord 
               When ResponseOfUser = QuitStockMenu
                   Move ItIsTrue to StockFileMaintenanceIsOver
               When other
                   Display ResponseOfUser " is an invalid response!"
                   Display "Please try again."
                   Display " "
           End-Evaluate.

      *                                                                  
      * Add Stock Data                           
      *                                                                  
       A12D-AddStockData.
           Perform A121-EnterStockData.
           Perform A122-FillStockRecord.
           Write BookStockRecord.
           If BookStockStatus not = IOisSuccessful
               Perform A123-FatalError
           End-If.

      *                                                                  
      * Enter Stock Data                         
      *                                                                  
       A121-EnterStockData.
           Display "Enter NUMBER OF STOCK: ".
           Accept  WBookStockStocknum.
           Display "Enter Book CODE SELL: ".
           Accept  WBookStockCodesell.
           Display "Enter Book CODE HIRE: ".
           Accept  WBookStockCodehire.
           Display "Enter STOCK LEVEL HIRE: ".
           Accept  WBookStockLevelhire.
           Display "Enter STOCK LEVEL SELL: ".
           Accept  WBookStockLevelsell.

      *                                                                  
      * Write Stock Record                         
      *                                                                  
       A122-FillStockRecord.
           Move WBookStockStocknum  to BookStockStocknum.
           Move WBookStockCodesell  to BookStockCodesell.
           Move WBookStockCodehire  to BookStockCodehire.
           Move WBookStockLevelhire to BookStockLevelhire.
           Move WBookStockLevelsell to BookStockLevelsell.

      *                                                                  
      *  Fatal Error                       
      *                                                                  
       A123-FatalError.
           Display "Fatal error in A123 ".
           Display "BookStockStatus = " BookStockStatus.
           Stop Run.

      *                                                                  
      * Update Stock Data                        
      *                                                                  

       A12E-UpdateStockData.
           Display "This function is not completed yet,".
           Display "Please strike >ENTER< to continue.".
           Stop " ".

      *
      * Delete Hired Books File                       
      *                                                                  
       A12F-DeleteStockData.
           Display "Enter NUMBER OF STOCK to delete: ".
           Accept WBookStockStocknum.
           MOVE   WBookStockStocknum to BookStockStocknum.
           MOVE   0 to 
                        BookStockCodesell 
                        BookStockCodehire 
                        BookStockLevelhire 
                        BookStockLevelsell.
      *    Perform A122-FillStockRecord.
           Write BookStockRecord.
           Perform A12J-MoveStockRecordToDisplay.

      *    If BookStockStatus not = IOisSuccessful
      *        Perform A123-FatalError
      *    End-If.

           Perform A12K-DisplayStockRecord.
                   

      *                                                                  
      * View Stock Record                        
      *                                                                  
       A12G-ViewStockRecord.
           Display "Enter NUMBER OF STOCK: ".
           Accept WBookStockStocknum.
           Move WBookStockStocknum to BookStockStocknum.
           Read BookStock.
           If BookStockStatus = IOisSuccessful
               Perform A12J-MoveStockRecordToDisplay
               Perform A12K-DisplayStockRecord
           Else
      *        Display "Stock record#: " WBookStockStocknum
      *        Display "is not found in the file."
           End-If.
      *    Stop run.


      *                                                                  
      * Move Stock Record to Display Variables              
      *                                                                  

       A12J-MoveStockRecordToDisplay.
           Move BookStockStocknum  to WBookStockStocknum.
           Move BookStockCodesell  to WBookStockCodesell.
           Move BookStockCodehire  to WBookStockCodehire.
           Move BookStockLevelhire to WBookStockLevelhire.
           Move BookStockLevelsell to WBookStockLevelsell.

      *                                                                  
      * Display Stock Record                         
      *                                                                  
       A12K-DisplayStockRecord.
           Display "NUMBER OF STOCK : " WBookStockStocknum.
           Display "Book CODE SELL  : " WBookStockCodesell.
           Display "Book CODE HIRE  : " WBookStockCodehire.
           Display "STOCK LEVEL HIRE: " WBookStockLevelhire.
           Display "STOCK LEVEL SELL: " WBookStockLevelsell.

      *                                                                  
      * End Program                          
      *                                                                  

       A113-EndProgram.
           If FatalIOErrorHasOccured = ItIsTrue
               Perform A11P-AbnormalEnd
           End-if.
           Perform A11J-CloseBookStockFile.
           Display "Program has ended successfully.".
           Stop Run.

      *                                                                  
      * Delete Record Error                         
      *                                                                  
       A11P-AbnormalEnd.
           Display "Book Code#: " WBookStockStocknum
           Display "is not found in the data record."
           Display " "
           Perform A12H-GetUserChoice.


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

#### ↳ Re: D - problem with program

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990414163351.11454.00001022@ng-ch1.aol.com>`
- **References:** `<19990414135500.00319.00000681@ng-fp1.aol.com>`

```
oh, man...where do I begin.... :-)
```

##### ↳ ↳ Re: D - problem with program

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990415160416.14942.00001122@ng01.aol.com>`
- **References:** `<19990414163351.11454.00001022@ng-ch1.aol.com>`

```
>Subject: Re: D - problem with program
>From: twymer@aol.com (Twymer)
…[4 more quoted lines elided]…
>

Yes, please begin at the beginning.

PS: are you trying to make a point?


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

##### ↳ ↳ Re: D - problem with program

- **From:** john_meyer@my-dejanews.com
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g4so8$520$1@nnrp1.dejanews.com>`
- **References:** `<19990414135500.00319.00000681@ng-fp1.aol.com> <19990414163351.11454.00001022@ng-ch1.aol.com>`

```
In article <19990414163351.11454.00001022@ng-ch1.aol.com>,
  twymer@aol.com (Twymer) wrote:
> oh, man...where do I begin.... :-)


Let me guess, you're crying over all the 77s too.  My teacher would shoot me
if I ever used that many 77s.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: D - problem with program

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqqR2.22295$cq3.938173@news.uswest.net>`
- **References:** `<19990414135500.00319.00000681@ng-fp1.aol.com>`

```
Dupavoy,

What error are you getting?


Sincerely,
     Chris Osborne


Dupavoy <dupavoy@aol.combatSPAM> wrote in message
news:19990414135500.00319.00000681@ng-fp1.aol.com...
>         Here is what the problem is: I am trying
>         to delete all values input for stock#1 in
…[54 more quoted lines elided]…
>        78  ItIsTrue     VALUE 1.

Well, I'm only working with VS/COBOL II release 4 from IBM, but I
don't think a 78 level is a part of COBOL.  Is this a vendor
extension?


>
>       *
…[420 more quoted lines elided]…
>
```

##### ↳ ↳ Re: D - problem with program

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990415160533.14942.00001123@ng01.aol.com>`
- **References:** `<hqqR2.22295$cq3.938173@news.uswest.net>`

```
Dupavoy <dupavoy@aol.combatSPAM> wrote in message
news:19990414135500.00319.00000681@ng-fp1.aol.com...
>         Here is what the problem is: I am trying
>         to delete all values input for stock#1 in
>         A121-EnterStockData by setting
>         them to 0's but its giving me an error.
>



Subject: Re: D - problem with program
From: "ChrisOsborne" <chris_n_osborne@yahoo.com>
Date: 4/15/99 1:45 PM EST
Message-id: <hqqR2.22295$cq3.938173@news.uswest.net>

Dupavoy,

What error are you getting?


Sincerely,
     Chris Osborne<<

--The error within the program.
It just doesnt set 0's to the values.





***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

###### ↳ ↳ ↳ Re: D - problem with program

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9031EC35E7D0DEBD.58278C30117F9AEC.E328660C402D96DE@library-proxy.airnews.net>`
- **References:** `<hqqR2.22295$cq3.938173@news.uswest.net> <19990415160533.14942.00001123@ng01.aol.com>`

```
On 15 Apr 1999 20:05:33 GMT, dupavoy@aol.combatSPAM (Dupavoy)
enlightened us:

>Dupavoy <dupavoy@aol.combatSPAM> wrote in message
>news:19990414135500.00319.00000681@ng-fp1.aol.com...
…[34 more quoted lines elided]…
>*******************************************                                
Okay, I'm confused.  Here is your A121 routine:

  *                                                                  
      * Enter Stock Data                         
      *

       A121-EnterStockData.
           Display "Enter NUMBER OF STOCK: ".
           Accept  WBookStockStocknum.
           Display "Enter Book CODE SELL: ".
           Accept  WBookStockCodesell.
           Display "Enter Book CODE HIRE: ".
           Accept  WBookStockCodehire.
           Display "Enter STOCK LEVEL HIRE: ".
           Accept  WBookStockLevelhire.
           Display "Enter STOCK LEVEL SELL: ".
           Accept  WBookStockLevelsell.

Nowhere do I see you moving zero to any field.  Are you saying that
you enter 0 for each field on the screen yet when you write the record
the value of the fields in the record is not 0?  I see the paragraph
where you have moved the W..... fields to the B...... fields.  So, if
you dump the record you have just added, what do you see in the
fields?

Regards,


Regards,

          ////
         (o o)
-oOO--(_)--OOo-

For Sale: Parachute. Only used once, never opened, small stain.

 Steve
```

###### ↳ ↳ ↳ Re: D - problem with program

_(reply depth: 4)_

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990419145624.22743.00002658@ng143.aol.com>`
- **References:** `<9031EC35E7D0DEBD.58278C30117F9AEC.E328660C402D96DE@library-proxy.airnews.net>`

```
>>                          
Okay, I'm confused.  Here is your A121 routine:

  *                                                                  
      * Enter Stock Data                         
      *

       A121-EnterStockData.
           Display "Enter NUMBER OF STOCK: ".
           Accept  WBookStockStocknum.
           Display "Enter Book CODE SELL: ".
           Accept  WBookStockCodesell.
           Display "Enter Book CODE HIRE: ".
           Accept  WBookStockCodehire.
           Display "Enter STOCK LEVEL HIRE: ".
           Accept  WBookStockLevelhire.
           Display "Enter STOCK LEVEL SELL: ".
           Accept  WBookStockLevelsell.

Nowhere do I see you moving zero to any field.  Are you saying that
you enter 0 for each field on the screen yet when you write the record
the value of the fields in the record is not 0?  I see the paragraph
where you have moved the W..... fields to the B...... fields.  So, if
you dump the record you have just added, what do you see in the
fields?
<<

--The reason I want to move 0's to the fields is to delete the input from them
when the user chooses the delete option.  I thought about moving spaces to
those fields as well.  
 anyway, if I enter Hamlet, how do I change this field to Moby Dick?

***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

###### ↳ ↳ ↳ Re: D - problem with program

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-04-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UzJR2.147$HP5.4452@news.uswest.net>`
- **References:** `<hqqR2.22295$cq3.938173@news.uswest.net> <19990415160533.14942.00001123@ng01.aol.com>`

```
Dupavoy,

My apologies, I thought that . . .

"by setting them to 0's but its giving me an error."

. . . meant that when the program went to set 0's, it crashed or
abended with an error.


Okay, down in A12F-DeleteStockData, the program seems to set
everything correctly, but then it executes the fill paragraph
A122-FillStockRecord, which moves working storage values into many of
the fields the program just set to 0.  That might be the problem, but
if it isn't (because no part of the program has yet put anything in
those working storage fields), try changing the WRITE command after
the perform of the fill paragraph to the REWRITE command.



Sincerely,
     Chris Osborne


Dupavoy <dupavoy@aol.combatSPAM> wrote in message
news:19990415160533.14942.00001123@ng01.aol.com...
> Dupavoy <dupavoy@aol.combatSPAM> wrote in message
> news:19990414135500.00319.00000681@ng-fp1.aol.com...
…[35 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: D - problem with program

_(reply depth: 4)_

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990421151049.17377.00000034@ng04.aol.com>`
- **References:** `<UzJR2.147$HP5.4452@news.uswest.net>`

```
>> >         Here is what the problem is: I am trying
>> >         to delete all values input for stock#1 in
>> >         A121-EnterStockData by setting
>> >         them to 0's or spaces but its giving me >> >an error.

I fixed this error, now I want to use the reserved word 'delete' to delete the
entire record.  How do I use it instead of using:
Move spaces to WBooktitle
                             Wbookauthor
                              Wbookprice
                              


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
