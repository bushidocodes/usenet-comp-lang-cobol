[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] My First C# (warning - long post)

_62 messages · 8 participants · 2007-01 → 2007-02_

---

### [OT] My First C# (warning - long post)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-01-30T19:00:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET>`

```
Here 'tis.  It looks like there's a little word-wrapping going on - I 
wasn't really attentive to ensuring that I didn't go past 80 on some lines.

What this does...
  - Counts lines of code, along with "executable" and "commented" lines
  - Creates a cross-reference between programs and procs (copybooks). 
All our procs are named Annn-something (where A is a letter and nnn is a 
three-digit number).  For programs, we parse copy statements, and for 
procs, we parse perform statements.  (This gives us the ability, from 
our CM system, to generate a list of proc dependencies.)
  - Creates a cross-reference between programs/procs and reject codes. 
The system we support uses a table of reject codes with associate 
narratives.  When a code is changed, all program owners who are affected 
must sign off.  This xref enables that, as well as finding rejects that 
are not used by any programs - these numbers can be reused.
  - Creates a cross-references between programs/procs and called 
procedures.  It can be used for many different things.
  - [TODO] Creates a cross-reference between programs/procs and database 
records/tables and fields/columns.  (This is the missing "cull" stuff.)

Some notes as well...
  - the "cull" stuff isn't done yet, so if the method has "cull" in the 
name, ignore it.  (There are a few utility methods under the cull stuff.)
  - I've replaced our server names and passwords with placeholders, for 
obvious reasons.
  - I really, REALLY, *REALLY* dislike the auto-formatting that VS2005 
does with putting the braces on the line under the declaration. 
However, that's our shop standard, so that's what this looks like.
  - I've tried to comment things as I go along, but this isn't a 
finished product.  If you see a spot where more comments would be 
helpful, feel free to identify them to me...
  - Having to have a "break" after the "default" case on a switch is 
BS...  but I digress...

Here we go - 824 lines....

-8<-----

using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Text;

namespace CodeStats
{
     public class CodeStatistics
     {
         // Properties (public instance variables)
         bool    updatedStats  = false;
         String  elementId     = "";
         int     locTotal      = 0;
         int     locExecutable = 0;
         int     locCommented  = 0;

         // Private instance variables
         protected SqlConnection dbConn;
         protected SqlConnection dbHelp;
         protected char          elementType    = ' ';
         protected String        elementSubType = "";
         protected String        fileName       = "";
         protected bool          inComment      = false;
         protected List<String>  programID      = new List<String>();
         protected String[]      cobolKeywords =
             {"ACCEPT","ACCESS","ACQUIRE","ADD","ADVANCING","AFTER","ALL",
             "ALPHABET","ALPHABETIC","ALPHABETIC-LOWER","ALPHABETIC-UPPER",
 
"ALPHANUMERIC","ALPHANUMERIC-EDITED","ALSO","ALTER","ALTERNATE",
 
"AND","ANY","APPLY","ARE","AREA","AREAS","ASCENDING","ASSIGN","AT",
             "AUTHOR","BEFORE","BINARY","BINARY-1","BIT","BLANK","BLOCK",
             "BOTTOM","BY","BYTE-I18N","CALL","CANCEL","CD","CF","CH",
             "CHARACTER","CHARACTERS","CLASS","CLASS-NAME","CLOCK-UNITS",
             "CLOSE","COBOL","CODE","CODE-SET","COLLATING","COLUMN","COMMA",
             "COMMON","COMMON-STORAGE","COMMUNICATION","COMP","COMP-1",
             "COMP-2","COMPUTATIONAL","COMPUTATIONAL-1","COMPUTATIONAL-2",
 
"COMPUTE","CONFIGURATION","CONTAINS","CONTENT","CONTINUE","CONTROL",
             "CONTROLS","CONVERTING","COPY","CORR","CORRESPONDING","COUNT",
             "CURRENCY","DATA","DATE","DATE-COMPILED","DATE-WRITTEN","DAY",
             "DAY-OF-WEEK","DE","DEBUG-CONTENTS","DEBUG-ITEM","DEBUG-LINE",
             "DEBUG-NAME","DEBUG-SUB-1","DEBUG-SUB-2","DEBUG-SUB-3",
 
"DEBUGGING","DECIMAL-POINT","DECLARATIVES","DELETE","DELIMITED",
             "DELIMITER","DENSITY","DEPART","DEPENDING","DESCENDING",
             "DESTINATION","DETAIL","DISABLE","DISP","DISP-2","DISP-I18N",
             "DISPLAY","DISPLAY-2","DIVIDE","DIVISION","DOWN","DUPLICATE",
             "DYNAMIC","EGI","ELSE","EMI","EMPTY","ENABLE","END","END-ADD",
 
"END-CALL","END-COMPUTE","END-DELETE","END-DIVIDE","END-EVALUATE",
             "END-IF","END-MULTIPLY","END-OF-PAGE","END-PERFORM","END-READ",
 
"END-RECEIVE","END-RETURN","END-REWRITE","END-SEARCH","END-STRING",
             "END-SUBTRACT","END-UNSTRING","END-WRITE","ENTER","ENTRY",
             "ENVIRONMENT","EOP","EQUAL","ERROR","ESI","EVALUATE","EVERY",
             "EXCEPTION","EXDEF","EXEC","EXIT","EXREF","EXTEND","EXTERNAL",
 
"FALSE","FD","FETCH","FILE","FILE-CONTROL","FILLER","FINAL","FIND",
 
"FIRST","FOOTING","FOR","FREE","FROM","FUNCTION","GENERATE","GET",
 
"GIVING","GLOBAL","GO","GREATER","GROUP","HEADING","HIGH-VALUE",
 
"HIGH-VALUES","I-O","I-O-CONTROL","IDENTIFICATION","IF","IMPART",
 
"IN","INDEX","INDEXED","INDICATE","INITIAL","INITIALIZE","INPUT",
 
"INPUT-OUTPUT","INSERT","INSPECT","INSTALLATION","INTO","INVALID",
             "INVOKE","IS","JUST","JUSTIFIED","KEEP","KEY","LABEL","LAST",
             "LEADING","LEFT","LENGTH","LESS","LIMIT","LIMITS","LINAGE",
 
"LINAGE-COUNTER","LINE","LINE-COUNTER","LINES","LINKAGE","LOCALE",
 
"LOCK","LOG","LOW-VALUE","LOW-VALUES","MEMORY","MERGE","MESSAGE",
             "MODE","MODE-1","MODE-2","MODE-3","MODE-4","MODIFY","MODULES",
 
"MOVE","MULTIPLE","MULTIPLY","NATIVE","NEGATIVE","NEXT","NO","NOT",
 
"NUMBER","NUMERIC","NUMERIC-EDITED","OBJECT-COMPUTER","OCCURS","OF",
 
"OFF","OMITTED","ON","OPEN","OPTIONAL","OR","ORDER","ORGANIZATION",
             "OTHER","OUTPUT","OVERFLOW","OWNER","PACKED-DECIMAL","PADDING",
 
"PAGE","PAGE-COUNTER","PERFORM","PF","PH","PIC","PICTURE","PLUS",
             "POINTER","POINTS","POSITION","POSITIVE","PRINTING","PRIOR",
 
"PROCEDURE","PROCEDURES","PROCEED","PROGRAM","PROGRAM-ID","PURGE",
             "QUEUE","QUOTE","QUOTES","RANDOM","RANK","RD","READ","RECEIVE",
             "RECORD","RECORDING","RECORDS","REDEFINES","REEL","REFERENCE",
 
"REFERENCES","RELATIVE","RELEASE","REMAINDER","REMOVAL","REMOVE",
             "RENAMES","REPLACE","REPLACING","REPORT","REPORTING","REPORTS",
 
"RERUN","RESERVE","RESET","RETURN","REVERSED","REWIND","REWRITE",
 
"RF","RH","RIGHT","ROUNDED","RUN","SAME","SD","SEARCH","SECTION",
 
"SECURITY","SEGMENT","SEGMENT-LIMIT","SELECT","SEND","SENTENCE",
             "SEQUENTIAL","SET","SIGN","SIZE","SORT","SORT-MERGE","SOURCE",
             "SOURCE-COMPUTER","SPACE","SPACES","SPECIAL-NAMES","STANDARD",
 
"STANDARD-1","STANDARD-2","START","STATUS","STOP","STORE","STRING",
             "SUB-QUEUE-1","SUB-QUEUE-2","SUB-QUEUE-3","SUBTRACT","SUM",
             "SUPPRESS","SYMBOLIC","SYNC","SYNCHRONIZED","TABLE","TALLYING",
             "TAPE","TERMINAL","TERMINATE","TEST","TEXT","THAN","THEN",
 
"THROUGH","THRU","TIME","TIMES","TO","TOP","TRAILING","TRUE","TYPE",
 
"UNIT","UNSTRING","UNTIL","UP","UPON","USAGE","USE","USING","VALUE",
 
"VALUES","VARYING","WHEN","WITH","WORDS","WORKING-STORAGE","WRITE",
 
"ZERO","ZEROES","ZEROS","+","-","*","/","**",">","<","=",">=","<="};

         // Constuctor for no parameter
         public CodeStatistics(String csServerName)
         {
             openSqlConnection(csServerName);
         }

         // Constructor for passed Element ID
         public CodeStatistics(String csServerName, String csElementId)
         {
             openSqlConnection(csServerName);
             retrieveElementInfo(csElementId);
         }

         // Establish the element for this class instance
         public void retrieveElementInfo(String reiElementId)
         {
             // Retrieve the information about the passed program
             SqlCommand cmd = new SqlCommand("SELECT element_id, 
element_type, element_subtype, server_name "
                 + "FROM active_elements "
                 + "WHERE element_id = '" + reiElementId.Trim() + "'", 
dbConn);
             SqlDataReader dr = cmd.ExecuteReader();
             if (dr.Read())
             {
                 elementType    = 
Convert.ToChar(dr["element_type"].ToString().Trim().Substring(0,1));
                 elementSubType = dr["element_subtype"].ToString().Trim();
                 fileName       = dr["server_name"].ToString().Trim();
                 elementId      = reiElementId;
             }
             dr.Close();
             dr.Dispose();
         }

         // Update the statistics for the element ID
         public void updateStatistics(String usPath, String usProcessName)
         {
             if (File.Exists(usPath + fileName))
             {
                 String textLine = "";

                 // Depending on the type, clear out the cross-reference 
tables
                 switch (elementType)
                 {
                     case 'P':
                     case 'L':
                         SqlCommand scDel = new SqlCommand();
                         scDel.Connection = dbConn;

                         // Delete item/proc xref
                         scDel.CommandText = "DELETE FROM Proc_Prog_Xref 
WHERE ProgName = '" + elementId + "'";
                         scDel.ExecuteNonQuery();

                         // Delete item/reject xref
                         scDel.CommandText = "DELETE FROM RejectsXref 
WHERE program = '" + elementId + "'";
                         scDel.ExecuteNonQuery();

                         // Delete item/call xref
                         scDel.CommandText = "DELETE FROM 
sdp_CSCI_Call_Xref WHERE Element_ID = '" + elementId + "'";
                         scDel.ExecuteNonQuery();

                         // Delete cull information
                         scDel.CommandText = "DELETE FROM 
sdp_Dbe_Csci_Xref WHERE CSCI = '" + elementId + "'";
                         scDel.ExecuteNonQuery();
                         scDel.CommandText = "DELETE FROM 
sdp_Dbr_Csci_Xref WHERE CSCI = '" + elementId + "'";
                         scDel.ExecuteNonQuery();

                         scDel.Dispose();
                         break;
                 }

                 StreamReader file = File.OpenText(usPath + fileName);

                 while (!file.EndOfStream)
                 {
                     textLine = file.ReadLine().ToUpper();

                     if ((elementType != 'P') && (elementType != 'L'))
                     {
                         textLine = textLine.Trim();
                     }

                     countLine(textLine); // Count this line as a "line 
of code"

                     switch(elementType)
                     {
                         case 'P':
                         case 'L':
                             textLine = textLine.Replace(",", " 
").Replace(".", " ").Trim();
                             updateProcXref(textLine);
                             updateRejectXref(textLine, usProcessName);
                             updateCallXref(textLine);
                             //updateCull(textLine);
                             break;
                     }

                 }

                 file.Close();
                 file.Dispose();

                 if (programID.Count > 0)
                 {   // Delete any references to calls if the target is 
defined in the program (i.e., nested subprograms)
                     SqlCommand scDelete = new SqlCommand();

                     scDelete.CommandText = "DELETE FROM 
sdp_CSCI_CALL_Xref "
                         + "WHERE Element_ID = '" + elementId + "' "
                             + "AND Call_Name IN ('";
                     for (int i = 0; i < programID.Count; i++)
                     {
                         scDelete.CommandText += programID[i] + "'";
                         if (i < (programID.Count - 1))
                         {
                             scDelete.CommandText += ",'";
                         }
                     }
                     scDelete.CommandText += ")";
                     scDelete.Connection = dbConn;
                     scDelete.ExecuteNonQuery();
                     scDelete.Dispose();
                 }

                 // Update LOC in the CSCS database
                 SqlCommand sc = new SqlCommand("UPDATE Active_Elements "
                     + "SET   Commented_Lines  = " + 
locCommented.ToString()
                         + ", Executable_Lines = " + 
locExecutable.ToString()
                         + ", Total_Lines      = " + locTotal.ToString()
                     + "WHERE Element_ID = '" + elementId + "'", dbConn);
                 sc.ExecuteNonQuery();
                 sc.Dispose();
             }
         }

         protected void countLine(String clLine)
         {
             String commentStart  = "";
             String commentEnd    = "";
             String commentSingle = "";

             // A line is a line...
             locTotal++;

             if (clLine != "")
             {
                 switch(elementType)
                 {
                     case 'P':
                     case 'L':
                         // COBOL
                         if ((clLine.Length > 6) && 
(clLine.Substring(6,1) == "*"))
                         {
                             locCommented++;
                         }
                         else
                         {
                             locExecutable++;
                         }
                         break;

                     case 'G':
                         // GUI
                         if ((elementSubType == "HTML") || 
(elementSubType == "CSS") || (elementSubType == "XML"))
                         {
                             commentStart = "<!--";
                             commentEnd   = "-->";
                         }
                         else
                         {
                             if (elementSubType == "XSLT")
                             {
                                 commentStart = "<xsl:comment>";
                                 commentEnd   = "</xsl:comment>";
                             }
                             else
                             {
                                 if (elementSubType == "JS")
                                 {
                                     commentStart  = "/*";
                                     commentEnd    = "*/";
                                     commentSingle = "//";
                                 }
                             }
                         }

                         if ((commentStart == "") && (commentEnd == "") 
&& (commentSingle == ""))
                         {   // We don't look for comments - if it's not 
blank, it's executable
                             locExecutable++;
                         }
                         else
                         {
                             if (inComment)
                             {   // We're in a multi-line comment
                                 locCommented++;
                                 if (clLine.IndexOf(commentEnd) >= 0)
                                 {   // This is the last line of the 
multi-line comment
                                     inComment = false;
                                 }
                             }
                             else
                             {
                                 if (clLine.IndexOf(commentStart) >= 0)
                                 {
                                     if (clLine.IndexOf(commentEnd) == -1)
                                     {   // Start of a multi-line comment
                                         inComment = true;
                                     }
                                     if ((clLine.IndexOf(commentStart) 
== 0))
                                     {   // Nothing before the comment - 
the entire line is commented
                                         locCommented++;
                                     }
                                     else
                                     {   // Something before the comment 
- count the line as executable
                                         locExecutable++;
                                     }
                                 }
                                 else
                                 {
                                     if ((commentSingle != "") && 
(clLine.IndexOf(commentSingle) >= 0))
                                     {
                                         if 
(clLine.IndexOf(commentSingle) == 0)
                                         {   // The entire line is a comment
                                             locCommented++;
                                         }
                                         else
                                         {   // Only the end of the line 
is commented
                                             locExecutable++;
                                         }
                                     }
                                     else
                                     {
                                         locExecutable++;
                                     }
                                 }
                             }
                         }
                         break;

                     case 'R':
                         // Runstreams
                         if ((elementSubType == "IPF") && 
(clLine.Substring(0,1) == "@"))
                         {   // IPF comment character
                             locCommented++;
                         }
                         else
                         {
                             if ((elementSubType == "QLP") && 
(clLine.Substring(0,1) == "*"))
                             {   // QLP comment character
                                 locCommented++;
                             }
                             else
                             {   // Apply ECL comment rules
                                 if ((clLine.Length > 2) && 
((clLine.Substring(0,3) == "@ .") || (clLine.Substring(0,3) == "@. ")))
                                 {   // ECL comment character
                                     locCommented++;
                                 }
                                 else
                                 {
                                     locExecutable++;
                                 }
                             }
                         }
                         break;

                     case 'Q':
                         // IQ/U Runstreams
                         if (clLine.Substring(0,1) == ".")
                         {
                             locCommented++;
                         }
                         else
                         {
                             locExecutable++;
                         }
                         break;

                     default:
                         // Anything else, a non-blank line is executable
                         locExecutable++;
                         break;
                 }
             }
         }

         protected void updateProcXref(String upxLine)
         {
             // For this to work right, we need all items separated by 
only one space
             upxLine = normalizeSpace(upxLine);

             switch (elementType)
             {
                 case 'P':
                     // Establish the cross-reference based on copy 
statement
                     if ((upxLine.Length > 6) && (upxLine.Substring(0,5) 
== "COPY "))
                     {
                         String[] words  = upxLine.Split(' ');
                         String[] pieces = words[1].Split('-');

                         if (isElement(pieces[0]))
                         {   // See if this is already in the 
cross-reference
                             SqlCommand scCheck = new SqlCommand("SELECT 
ProgName FROM Proc_Prog_Xref "
                                 + "WHERE   ProgName   = '" + elementId 
+ "' "
                                     + "AND ProcName   = '" + pieces[0] 
+ "' "
                                     + "AND EntryPoint = '" + words[1] 
+ "'", dbConn);
                             SqlDataReader drCheck = 
scCheck.ExecuteReader();
                             if (!drCheck.HasRows)
                             {   // Add this program/proc to the table
                                 executeSQL("INSERT INTO Proc_Prog_Xref "
                                     + "(ProgName, ProcName, Passive, 
EntryPoint) "
                                     + "VALUES ('" + elementId + "','" + 
pieces[0] + "',0,'" + words[1] + "')");
                             }
                             drCheck.Close();
                             drCheck.Dispose();
                             scCheck.Dispose();
                         }
                     }
                     break;

                 case 'L':
                     // Establish the cross-reference based on perform 
statement
                     if ((upxLine.Length > 9) && (upxLine.Substring(0,8) 
== "PERFORM "))
                     {
                         String[] words  = upxLine.Split(' ');
                         String[] pieces = words[1].Split('-');

                         // Don't count performs of the proc itself
                         if ((pieces[0] != elementId) && 
(isElement(pieces[0])))
                         {   // See if this is already in the xref
                             SqlCommand scCheck = new SqlCommand("SELECT 
ProgName FROM Proc_Prog_Xref "
                                 + "WHERE ProgName = '" + elementId + "' "
                                     + "AND ProcName = '" + pieces[0] + 
"'", dbConn);
                             SqlDataReader drCheck = 
scCheck.ExecuteReader();
                             if (!drCheck.HasRows)
                             {
                                 executeSQL("INSERT INTO Proc_Prog_Xref "
                                     + "(ProgName, ProcName, Passive, 
EntryPoint) "
                                     + "VALUES ('" + elementId + "','" + 
pieces[0] + "',1,NULL)");
                             }
                             drCheck.Close();
                             drCheck.Dispose();
                             scCheck.Dispose();
                         }
                     }
                     break;
             }
         }

         protected void updateRejectXref(String urxLine, String 
urxProcessName)
         {
             Int32 rejectCode;

             // Get rid of extra spaces
             urxLine = normalizeSpace(urxLine);

             if ((urxLine.IndexOf("REJCDE") >= 0) && 
(urxLine.IndexOf("MOVE ") >= 0))
             {   // Line is "MOVE [something] TO REJCDE"
                 String[] words = urxLine.Split(' ');
                 if (Int32.TryParse(words[1], out rejectCode))
                 {
                     // Mask off narratives to get the lowest 4 digits
                     rejectCode = rejectCode % 10000;

                     if (rejectCode > 0)
                     {   // Is this reject already in the xref?
                         SqlCommand scCheck = new SqlCommand("SELECT 
program FROM RejectsXref "
                             + "WHERE program = '" + elementId + "' "
                                 + "AND reject_num = " + 
rejectCode.ToString(), dbConn);
                         SqlDataReader drCheck = scCheck.ExecuteReader();
                         if (!drCheck.HasRows)
                         {   // Insert it
                             executeSQL("INSERT INTO RejectsXref "
                                 + "(program, reject_num, last_updated, 
last_updated_by) "
                                 + "VALUES ('" + elementId + "'," + 
rejectCode.ToString()
                                 + ",current_timestamp,'" + 
urxProcessName + "')");
                         }
                         drCheck.Close();
                         drCheck.Dispose();
                         scCheck.Dispose();
                     }
                 }
             }
         }

         protected void updateCallXref(String ucxLine)
         {
             String[] words = normalizeSpace(ucxLine).Split(' ');

             // Check for "PROGRAM-ID"
             if (words[0] == "PROGRAM-ID")
             {   // Save these off - we'll delete them at the end
                 programID.Add(words[1]);
             }

             if ((words.Length > 1) && (words[0] == "CALL"))
             {
                 if ((words[1].Substring(0,1) == "\"") || 
(words[1].Substring(0,1) == "'"))
                 {   // Calling a literal - this is one we'll store
                     String callName = 
words[1].Substring(1,words[1].Length - 2);

                     SqlCommand scCheck = new SqlCommand("SELECT 
Element_ID FROM sdp_CSCI_CALL_Xref "
                         + "WHERE Element_ID = '" + elementId + "' "
                             + "AND Call_Name = '" + callName + "'", 
dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();
                     if (!drCheck.HasRows)
                     {   // It's not there - insert it
                         executeSQL("INSERT INTO sdp_CSCI_CALL_Xref "
                             + "(Element_ID, Call_Name) "
                             + "VALUES ('" + elementId + "','" + 
callName + "')");
                     }
                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();
                 }
             }
         }

         protected void updateCull(String ucLine)
         {
             ucLine = normalizeSpace(ucLine);

             if (   (ucLine.IndexOf("FETCH ")  >= 0) || 
(ucLine.IndexOf("FIND ")   >= 0)
                 || (ucLine.IndexOf("MODIFY ") >= 0) || 
(ucLine.IndexOf("STORE ")  >= 0)
                 || (ucLine.IndexOf("DELETE ") >= 0) || 
(ucLine.IndexOf("INSERT ") >= 0)
                 || (ucLine.IndexOf("REMOVE ") >= 0))
             {
                 updateCullRecord(ucLine);
             }
             else
             {
                 // Split up the words, and check for a DMS field name 
or R-proc data name
                 String[] words = ucLine.Split(' ');
                 for (int i = 0; i < words.Length; i++)
                 {
                     if ((!isCobolKeyword(words[i])) && 
(!hasSymbols(words[i])))
                     {
                         updateCullItem(words[i], ucLine);
                     }
                 }
             }
         }

         // Update DML records in cull
         protected void updateCullRecord(String ucrLine)
         {
             String[] words  = ucrLine.Split(' ');
             Int32    word   = 0;
             String   column = "";

             // --- CHECK #1 --- record name //

             // Find the word where we're doing the DML
             while ((words[word] != "FETCH")  && (words[word] != "FIND")
                 && (words[word] != "MODIFY") && (words[word] != "STORE")
                 && (words[word] != "DELETE") && (words[word] != "INSERT")
                 && (words[word] != "REMOVE") && (word < words.Length))
             {
                 word++;
             }

             if ((word < (words.Length - 2))
                 && ((   words[word + 1] == "FIRST") || (words[word + 1] 
== "NEXT")
                     || (words[word + 1] == "PRIOR") || (words[word + 1] 
== "LAST")))
             {   // "FETCH FIRST xxx", etc.
                 word++;
             }

             if ((word < (words.Length - 2)) && (words[word + 1] != 
"RECORD"))
             {
                 // Determine the proper column name
                 if ((words[word] == "FETCH") || (words[word] == "FIND"))
                 {
                     column = "Fetches";
                 }
                 else
                 {
                     if (words[word] == "MODIFY")
                     {
                         column = "Modifies";
                     }
                     else
                     {
                         column = words[word].ToLower() + "s";
                     }
                 }

                 // The next word may be a record name
                 String recordName = words[++word];

                 // Is this name a valid record?
                 SqlCommand scRecChk = new SqlCommand("SELECT 
record_name FROM dms_records "
                     + "WHERE record_name = '" + recordName + "'", dbHelp);
                 SqlDataReader drRecChk = scRecChk.ExecuteReader();

                 if (drRecChk.HasRows)
                 {   // Does the record already exist in the 
cross-reference?
                     SqlCommand scCheck = new SqlCommand("SELECT CSCI 
FROM sdp_Dbr_Csci_Xref "
                         + "WHERE Dbr = '" + recordName + "' "
                             + "AND Csci = '" + elementId + "'", dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();

                     if (!drCheck.HasRows)
                     {   // Add a new zeroed-out row
                         SqlCommand scInsert = new SqlCommand("INSERT 
INTO sdp_Dbr_Csci_Xref "
                             + "(Dbr, Csci, Fetches, Modifies, Inserts, 
Stores, Removes, Deletes) "
                             + "VALUES ('" + recordName + "','" + 
elementId + "',0,0,0,0,0,0)", dbConn);
                         scInsert.ExecuteNonQuery();
                         scInsert.Dispose();
                     }

                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();

                     // Update this count
                     SqlCommand scUpdate = new SqlCommand("UPDATE 
sdp_Dbr_Csci_Xref "
                         + "SET " + column + " = " + column + " + 1 "
                         + "WHERE Dbr = '" + recordName + "' "
                             + "AND Csci = '" + elementId + "'", dbConn);
                     scUpdate.ExecuteNonQuery();
                     scUpdate.Dispose();
                 }

                 drRecChk.Close();
                 drRecChk.Dispose();
                 scRecChk.Dispose();
             }

             // --- CHECK #2 --- set name //

             if ((ucrLine.IndexOf(" SET") >= 0) || (ucrLine.IndexOf("VIA 
") >= 0))
             {
                 String setName = "";

                 // Find the word "via" or "set"
                 word = 0;
                 while ((words[word] != "VIA") && (words[word] != "SET"))
                 {
                     word++;
                 }

                 if ((words[word] == "SET") && (word > 0))
                 {   // "FETCH xxx WITHIN xxxx SET", "REMOVE xxxx FROM 
xxxxx SET", etc.
                     setName = words[--word];
                 }
                 else
                 {
                     if ((words[word] == "VIA") && (word < (words.Length 
-1)))
                     {   // "FETCH xxx VIA xxxx USING xxxx" format statement
                         setName = words[++word];
                     }
                 }

                 if (setName != "")
                 {
                     // Is this a valid set name?
                     SqlCommand scSetChk = new SqlCommand("SELECT 
set_name FROM dms_sets "
                         + "WHERE set_name = '" + setName + "'", dbHelp);
                     SqlDataReader drSetChk = scSetChk.ExecuteReader();

                     if (drSetChk.HasRows)
                     {
                         // What column name do we update?
                         column = "";

                         if ((ucrLine.IndexOf("FETCH ") >= 0) || 
(ucrLine.IndexOf("FIND ") >= 0))
                         {   column = "Fetches";
                         }
                         else
                         {   if (ucrLine.IndexOf("INSERT") >= 0)
                             {   column = "Inserts";
                             }
                             else
                             {   if (ucrLine.IndexOf("REMOVE") >= 0)
                                 {   column = "Removes";
                                 }
                             }
                         }

                         if (column != "")
                         {   // Does it already exist in the 
cross-reference?
                             SqlCommand scCheck = new SqlCommand("SELECT 
Dbr FROM sdp_Dbr_Csci_Xref "
                                 + "WHERE Dbr = '" + setName + "'", dbConn);
                             SqlDataReader drCheck = 
scCheck.ExecuteReader();

                             if (!drCheck.HasRows)
                             {   // Insert a new blank row
                                 SqlCommand scInsert = new 
SqlCommand("INSERT INTO sdp_Dbr_Csci_Xref "
                                     + "(Dbr, Csci, Fetches, Modifies, 
Inserts, Stores, Removes, Deletes) "
                                     + "VALUES ('" + setName + "','" + 
elementId + "',0,0,0,0,0,0)", dbConn);
                                 scInsert.ExecuteNonQuery();
                                 scInsert.Dispose();
                             }

                             drCheck.Close();
                             drCheck.Dispose();
                             scCheck.Dispose();

                             SqlCommand scUpdate = new 
SqlCommand("UPDATE sdp_Dbr_Csci_Xref "
                                 + "SET " + column + " = " + column + " 
+ 1 "
                                 + "WHERE Dbr = '" + setName + "' "
                                     + "AND Csci = '" + elementId + "'", 
dbConn);
                             scUpdate.ExecuteNonQuery();
                             scUpdate.Dispose();
                         }
                     }

                     drSetChk.Close();
                     drSetChk.Dispose();
                     scSetChk.Dispose();
                 }
             }
         }

         protected void updateCullItem(String uciWord, String uciLine)
         {
             bool used    = false;
             bool updated = false;

             // Check to see if the word starts with "R" and has a dash, 
and is not this proc
             if ((uciWord.Substring(0,1) == "R") && 
(uciWord.Substring(3,1) == "-")
                 && (uciWord.Substring(0,4) != elementId))
             {
                 if (uciLine.IndexOf("PERFORM") >= 0)
                 {   // We've got a paragraph name performed
                     SqlCommand scTables = new SqlCommand("SELECT 
DISTINCT table_name rt "
                         + "FROM rdms_tables rt, rdms_table_columns rtc "
                         + "WHERE rt.table_name = rtc.table_name "
                             + "AND rtc.r_proc_element_name LIKE '" + 
uciWord.Substring(0,4) + "%'",dbHelp);
                     SqlDataReader drTables = scTables.ExecuteReader();

                     while(drTables.HasRows)
                     {   // See if this table already exists in the cull 
look-up
                         int i = 0; // !WORK this is crap
                     }
                 }
                 else
                 {
                     if (uciLine.IndexOf("MOVE") >= 0)
                     {
                         if (uciLine.IndexOf("TO") > 
uciLine.IndexOf(uciWord))
                         {
                             used = true;
                         }
                         else
                         {
                             updated = true;
                         }
                     }
                     else
                     {
                         updated = true;
                     }
                 }
             }
             else
             {   // See if the word is a valid DMS field
             }
         }

         // Establish connections with the database
         protected void openSqlConnection(String oscServerName)
         {
             String connString = "";

             if (oscServerName == "") {
                 oscServerName = "[servername]";
             }

             connString = "server=" + oscServerName + 
";database=[database];User ID=[user];Password=[password];";
             dbConn = new SqlConnection(connString);
             dbConn.Open();

             connString = 
connString.Replace("[database],"[another-database]");
             dbHelp = new SqlConnection(connString);
             dbHelp.Open();
         }

         public String cscsRegValue(String crvKey)
         {
             SqlCommand crvCmd = new SqlCommand("SELECT reg_value "
                 + "FROM sdp_registry "
                 + "WHERE reg_key = '" + crvKey + "'", dbConn);
             SqlDataReader crvDR = crvCmd.ExecuteReader();
             if (crvDR.Read())
             {
                 return(crvDR["reg_value"].ToString().Trim());
             }
             else
             {
                 return("");
             }
         }

         protected void executeSQL(String esText)
         {
             SqlConnection esConn = new 
SqlConnection(dbConn.ConnectionString + "password=[password];");
             SqlCommand    esCmd  = new SqlCommand(esText, esConn);
             esConn.Open();
             esCmd.ExecuteNonQuery();
             esCmd.Dispose();
             esConn.Close();
             esConn.Dispose();
         }

         // Eliminates all embedded spaces more than one
         protected String normalizeSpace(String nsText)
         {
             String workText = nsText;

             while (workText.IndexOf("  ") >= 0)
             {
                 workText = workText.Replace("  "," ");
             }
             return(workText);
         }

         // Returns "true" if the text passed is an element in CSCS
         protected bool isElement(String ieText)
         {
             Boolean itExists = false;

             SqlCommand ieCmd = new SqlCommand("SELECT Actv_Ind FROM 
Active_Elements "
                 + " WHERE Element_ID = '" + ieText + "'", dbConn);
             SqlDataReader ieDR  = ieCmd.ExecuteReader();
             if (ieDR.HasRows) {
                 itExists = true;
             }
             ieDR.Close();
             ieDR.Dispose();
             ieCmd.Dispose();

             return(itExists);
         }

         // Returns "true" if the word passed is a COBOL keyword
         protected bool isCobolKeyword(String ickText)
         {
             Int32 i = 0;
             while ((i < cobolKeywords.Length) && (ickText != 
cobolKeywords[i]))
             {
                 i++;
             }
             if (i < cobolKeywords.Length)
             {
                 return(true);
             }
             else
             {
                 return(false);
             }
         }

         // Returns "true" if the words passed has symbols in it
         protected bool hasSymbols(String hsText)
         {
             if (   (hsText.IndexOf("(")  >= 0) || (hsText.IndexOf(")") 
 >= 0)
                 || (hsText.IndexOf("\"") >= 0) || (hsText.IndexOf("'") 
 >= 0)
                 || (hsText.IndexOf("_")  >= 0))
             {
                 return(true);
             }
             else
             {
                 return(false);
             }
         }

     }
}
```

#### ↳ Re: My First C# (warning - long post)

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-01-31T13:54:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170280452.064733.60560@v45g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET>`

```
On Jan 31, 1:00 am, LX-i <lxi0...@netscape.net> wrote:
> Here 'tis.  It looks like there's a little word-wrapping going on - I
> wasn't really attentive to ensuring that I didn't go past 80 on some lines.
…[33 more quoted lines elided]…
>


Snipped code....

(Take these comments as good will ones, not character destroying..etc)

Ok so a quick scan through tells me that this class....

Whilst 'doing' one job of analysing the code files, is actually
several (currently) hidden classes working together. This is backed up
by the large number of IFs Switch statements, loops and repeated code.

The style of coding is more procedural than OO.  This is evident when
we have large methods, containing multple 'if' blocks or/and 'Switch'
statements.

A general guideline to use for OO methods, is to keep their size to no
more than 10 lines  (including whitespace, empty lines etc).

Lots of string literals embedded within the code, making the
maintenance of the program difficult. - These strings (esp db ones)
are better moved into a property file or constants.

However, all is not lost... I'll try and briefly show how using a
series of small changes, we can kepp your code compiling, running and
working, whilst slowly changing the design to be OO instead of
Procedural....

So lets start with the large methods...  within your class there are
numerous occurrences of code duplication...

for example, several places you create an SQLCommand, insert some data
then close and dispose:

      SqlCommand scCheck = new SqlCommand("....
                    ... dbConn);

      SqlDataReader drCheck = scCheck.ExecuteReader();
      if (!drCheck.HasRows)
      {   // It's not there - insert it
             executeSQL("...");
       }
       drCheck.Close();
       drCheck.Dispose();
       scCheck.Dispose();

If you moved (aka Refactored) this chunk of code into its own method,
and then did the same with all other occurrences of similar code,
you'd soon see that there are numerous small private methods doing the
same basic job, just with different data.

Your IDE will even do the extraction for you....  highlight some code
with the mouse and right click, somewhere there will be a 'refactor'
menu option with something like 'extract method...' on it.

Once we have these small methods , we can then remove all of them but
One, and Pass It The Data to use...  we do this, one method at a
time.

Another useful technique is to change inline comments into the names
of private methods, and move the code there...

time for another example...

     // Update DML records in cull
         protected void updateCullRecord(String ucrLine)
         {

             // --- CHECK #1 --- record name //
             checkRecordName(...)

             // --- CHECK #2 --- set name //
             checkSetName(...)

         }


Once again, select the code blocks to extract( the code between each
comment)  and use your IDEs refactoring tool to extract method...

Once you have broken your methods down into sizes of no more than 10
lines, you will probably have 10, 20 or more little methods working
together to do the job as it currently does.

Now, the next step is to find the groupings of these methods that
naturally fit into their own class.

So for example.....

All of the db related methods are retrieving/inserting data, but
actually don't need to be part of the CodeStatistics class.  Indeed,
moving those db related methods into their own class called
StatisticsModel?  StatisticsDataSource?  StatisticsGateway? (Gateway
is a design pattern...) means the Responsibility of getting and
updating the db is now in its own class, and that new class has only
one Responsibility.

time for a break....(aka kids playing up... ;-)  )

Andrew
```

##### ↳ ↳ Re: My First C# (warning - long post)

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-01-31T17:01:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170291697.002493.111010@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1170280452.064733.60560@v45g2000cwv.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com>`

```
On Jan 31, 9:54 pm, "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote:
> On Jan 31, 1:00 am, LX-i <lxi0...@netscape.net> wrote:
>
…[5 more quoted lines elided]…
> > What this does...
....

> time for a break....(aka kids playing up... ;-)  )
>
> Andrew

Ok, so I downloaded and installed vs2005 express, loaded your class
and started using the 'refactoring -> extract method' right click menu
option....

Here's what I've got so far....(if you paste it into your
vs2005...you'll need to spend a few minutes sorting out the line wraps
that posting it to here causes...)

More tomorrow....


using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Text;

namespace CodeStats
{
     public class CodeStatistics
     {
         // Properties (public instance variables)
         bool    updatedStats  = false;
         String  elementId     = "";
         int     locTotal      = 0;
         int     locExecutable = 0;
         int     locCommented  = 0;

         // Private instance variables
         protected SqlConnection dbConn;
         protected SqlConnection dbHelp;
         protected char          elementType    = ' ';
         protected String        elementSubType = "";
         protected String        fileName       = "";
         protected bool          inComment      = false;
         protected List<String>  programID      = new List<String>();
         protected String[]      cobolKeywords =
 
{"ACCEPT","ACCESS","ACQUIRE","ADD","ADVANCING","AFTER","ALL",
             "ALPHABET","ALPHABETIC","ALPHABETIC-LOWER","ALPHABETIC-
UPPER",

"ALPHANUMERIC","ALPHANUMERIC-EDITED","ALSO","ALTER","ALTERNATE",

"AND","ANY","APPLY","ARE","AREA","AREAS","ASCENDING","ASSIGN","AT",
 
"AUTHOR","BEFORE","BINARY","BINARY-1","BIT","BLANK","BLOCK",
             "BOTTOM","BY","BYTE-I18N","CALL","CANCEL","CD","CF","CH",
             "CHARACTER","CHARACTERS","CLASS","CLASS-NAME","CLOCK-
UNITS",
             "CLOSE","COBOL","CODE","CODE-
SET","COLLATING","COLUMN","COMMA",
             "COMMON","COMMON-
STORAGE","COMMUNICATION","COMP","COMP-1",
 
"COMP-2","COMPUTATIONAL","COMPUTATIONAL-1","COMPUTATIONAL-2",

"COMPUTE","CONFIGURATION","CONTAINS","CONTENT","CONTINUE","CONTROL",
 
"CONTROLS","CONVERTING","COPY","CORR","CORRESPONDING","COUNT",
             "CURRENCY","DATA","DATE","DATE-COMPILED","DATE-
WRITTEN","DAY",
             "DAY-OF-WEEK","DE","DEBUG-CONTENTS","DEBUG-ITEM","DEBUG-
LINE",
             "DEBUG-NAME","DEBUG-SUB-1","DEBUG-SUB-2","DEBUG-SUB-3",

"DEBUGGING","DECIMAL-POINT","DECLARATIVES","DELETE","DELIMITED",
             "DELIMITER","DENSITY","DEPART","DEPENDING","DESCENDING",
             "DESTINATION","DETAIL","DISABLE","DISP","DISP-2","DISP-
I18N",
 
"DISPLAY","DISPLAY-2","DIVIDE","DIVISION","DOWN","DUPLICATE",
             "DYNAMIC","EGI","ELSE","EMI","EMPTY","ENABLE","END","END-
ADD",

"END-CALL","END-COMPUTE","END-DELETE","END-DIVIDE","END-EVALUATE",
             "END-IF","END-MULTIPLY","END-OF-PAGE","END-PERFORM","END-
READ",

"END-RECEIVE","END-RETURN","END-REWRITE","END-SEARCH","END-STRING",
             "END-SUBTRACT","END-UNSTRING","END-
WRITE","ENTER","ENTRY",
 
"ENVIRONMENT","EOP","EQUAL","ERROR","ESI","EVALUATE","EVERY",
 
"EXCEPTION","EXDEF","EXEC","EXIT","EXREF","EXTEND","EXTERNAL",

"FALSE","FD","FETCH","FILE","FILE-CONTROL","FILLER","FINAL","FIND",

"FIRST","FOOTING","FOR","FREE","FROM","FUNCTION","GENERATE","GET",

"GIVING","GLOBAL","GO","GREATER","GROUP","HEADING","HIGH-VALUE",

"HIGH-VALUES","I-O","I-O-CONTROL","IDENTIFICATION","IF","IMPART",

"IN","INDEX","INDEXED","INDICATE","INITIAL","INITIALIZE","INPUT",

"INPUT-OUTPUT","INSERT","INSPECT","INSTALLATION","INTO","INVALID",
 
"INVOKE","IS","JUST","JUSTIFIED","KEEP","KEY","LABEL","LAST",
 
"LEADING","LEFT","LENGTH","LESS","LIMIT","LIMITS","LINAGE",

"LINAGE-COUNTER","LINE","LINE-COUNTER","LINES","LINKAGE","LOCALE",

"LOCK","LOG","LOW-VALUE","LOW-VALUES","MEMORY","MERGE","MESSAGE",
 
"MODE","MODE-1","MODE-2","MODE-3","MODE-4","MODIFY","MODULES",

"MOVE","MULTIPLE","MULTIPLY","NATIVE","NEGATIVE","NEXT","NO","NOT",

"NUMBER","NUMERIC","NUMERIC-EDITED","OBJECT-COMPUTER","OCCURS","OF",

"OFF","OMITTED","ON","OPEN","OPTIONAL","OR","ORDER","ORGANIZATION",
             "OTHER","OUTPUT","OVERFLOW","OWNER","PACKED-
DECIMAL","PADDING",

"PAGE","PAGE-COUNTER","PERFORM","PF","PH","PIC","PICTURE","PLUS",
 
"POINTER","POINTS","POSITION","POSITIVE","PRINTING","PRIOR",

"PROCEDURE","PROCEDURES","PROCEED","PROGRAM","PROGRAM-ID","PURGE",
 
"QUEUE","QUOTE","QUOTES","RANDOM","RANK","RD","READ","RECEIVE",
 
"RECORD","RECORDING","RECORDS","REDEFINES","REEL","REFERENCE",

"REFERENCES","RELATIVE","RELEASE","REMAINDER","REMOVAL","REMOVE",
 
"RENAMES","REPLACE","REPLACING","REPORT","REPORTING","REPORTS",

"RERUN","RESERVE","RESET","RETURN","REVERSED","REWIND","REWRITE",

"RF","RH","RIGHT","ROUNDED","RUN","SAME","SD","SEARCH","SECTION",

"SECURITY","SEGMENT","SEGMENT-LIMIT","SELECT","SEND","SENTENCE",
             "SEQUENTIAL","SET","SIGN","SIZE","SORT","SORT-
MERGE","SOURCE",
             "SOURCE-COMPUTER","SPACE","SPACES","SPECIAL-
NAMES","STANDARD",

"STANDARD-1","STANDARD-2","START","STATUS","STOP","STORE","STRING",
             "SUB-QUEUE-1","SUB-QUEUE-2","SUB-
QUEUE-3","SUBTRACT","SUM",
 
"SUPPRESS","SYMBOLIC","SYNC","SYNCHRONIZED","TABLE","TALLYING",
 
"TAPE","TERMINAL","TERMINATE","TEST","TEXT","THAN","THEN",

"THROUGH","THRU","TIME","TIMES","TO","TOP","TRAILING","TRUE","TYPE",

"UNIT","UNSTRING","UNTIL","UP","UPON","USAGE","USE","USING","VALUE",

"VALUES","VARYING","WHEN","WITH","WORDS","WORKING-STORAGE","WRITE",

"ZERO","ZEROES","ZEROS","+","-","*","/","**",">","<","=",">=","<="};

         // Constuctor for no parameter
         public CodeStatistics(String csServerName)
         {
             openSqlConnection(csServerName);
         }

         // Constructor for passed Element ID
         public CodeStatistics(String csServerName, String
csElementId)
         {
             openSqlConnection(csServerName);
             retrieveElementInfo(csElementId);
         }

         // Establish the element for this class instance
         public void retrieveElementInfo(String reiElementId)
         {
             // Retrieve the information about the passed program
             SqlCommand cmd = new SqlCommand("SELECT element_id,
element_type, element_subtype, server_name "
                 + "FROM active_elements "
                 + "WHERE element_id = '" + reiElementId.Trim() + "'",
dbConn);
             SqlDataReader dr = cmd.ExecuteReader();
             if (dr.Read())
             {
                 elementType    =
Convert.ToChar(dr["element_type"].ToString().Trim().Substring(0,1));
                 elementSubType =
dr["element_subtype"].ToString().Trim();
                 fileName       = dr["server_name"].ToString().Trim();
                 elementId      = reiElementId;
             }
             dr.Close();
             dr.Dispose();
         }

         // Update the statistics for the element ID
         public void updateStatistics(String usPath, String
usProcessName)
         {
             if (File.Exists(usPath + fileName))
             {
                 String textLine = "";

                 clearOutCrossReferenceTables();

                 textLine = parseFile(usPath, usProcessName,
textLine);

 
deleteAnyReferencesToCallsIfTheTargetIsDefinedInTheProgram();

                 updateLocInTheCscsDatabase();
             }
         }

         private void updateLocInTheCscsDatabase()
         {
             // Update LOC in the CSCS database
             SqlCommand sc = new SqlCommand("UPDATE Active_Elements "
                 + "SET   Commented_Lines  = " +
locCommented.ToString()
                     + ", Executable_Lines = " +
locExecutable.ToString()
                     + ", Total_Lines      = " + locTotal.ToString()
                 + "WHERE Element_ID = '" + elementId + "'", dbConn);
             sc.ExecuteNonQuery();
             sc.Dispose();
         }

         private void
deleteAnyReferencesToCallsIfTheTargetIsDefinedInTheProgram()
         {
             if (programID.Count > 0)
             {   // Delete any references to calls if the target is
defined in the program (i.e., nested subprograms)
                 SqlCommand scDelete = new SqlCommand();

                 scDelete.CommandText = "DELETE FROM
sdp_CSCI_CALL_Xref "
                     + "WHERE Element_ID = '" + elementId + "' "
                         + "AND Call_Name IN ('";
                 for (int i = 0; i < programID.Count; i++)
                 {
                     scDelete.CommandText += programID[i] + "'";
                     if (i < (programID.Count - 1))
                     {
                         scDelete.CommandText += ",'";
                     }
                 }
                 scDelete.CommandText += ")";
                 scDelete.Connection = dbConn;
                 scDelete.ExecuteNonQuery();
                 scDelete.Dispose();
             }
         }

         private String parseFile(String usPath, String usProcessName,
String textLine)
         {
             StreamReader file = File.OpenText(usPath + fileName);

             while (!file.EndOfStream)
             {
                 textLine = file.ReadLine().ToUpper();

                 if ((elementType != 'P') && (elementType != 'L'))
                 {
                     textLine = textLine.Trim();
                 }

                 countLine(textLine); // Count this line as a "line of
code"

                 switch (elementType)
                 {
                     case 'P':
                     case 'L':
                         textLine = textLine.Replace(",", "
").Replace(".", " ").Trim();
                         updateProcXref(textLine);
                         updateRejectXref(textLine, usProcessName);
                         updateCallXref(textLine);
                         //updateCull(textLine);
                         break;
                 }

             }

             file.Close();
             file.Dispose();
             return textLine;
         }

         private void clearOutCrossReferenceTables()
         {
             // Depending on the type, clear out the cross-reference
tables
             switch (elementType)
             {
                 case 'P':
                 case 'L':
                     SqlCommand scDel = new SqlCommand();
                     scDel.Connection = dbConn;

                     // Delete item/proc xref
                     scDel.CommandText = "DELETE FROM Proc_Prog_Xref
WHERE ProgName = '" + elementId + "'";
                     scDel.ExecuteNonQuery();

                     // Delete item/reject xref
                     scDel.CommandText = "DELETE FROM RejectsXref
WHERE program = '" + elementId + "'";
                     scDel.ExecuteNonQuery();

                     // Delete item/call xref
                     scDel.CommandText = "DELETE FROM
sdp_CSCI_Call_Xref WHERE Element_ID = '" + elementId + "'";
                     scDel.ExecuteNonQuery();

                     // Delete cull information
                     scDel.CommandText = "DELETE FROM
sdp_Dbe_Csci_Xref WHERE CSCI = '" + elementId + "'";
                     scDel.ExecuteNonQuery();
                     scDel.CommandText = "DELETE FROM
sdp_Dbr_Csci_Xref WHERE CSCI = '" + elementId + "'";
                     scDel.ExecuteNonQuery();

                     scDel.Dispose();
                     break;
             }
         }

         protected void countLine(String clLine)
         {
             String commentStart  = "";
             String commentEnd    = "";
             String commentSingle = "";

             // A line is a line...
             locTotal++;

             if (clLine != "")
             {
                 switch(elementType)
                 {
                     case 'P':
                     case 'L':
                         lineOfCobolCode(clLine);
                         break;

                     case 'G':
                         linesOfGuiCode(clLine, ref commentStart, ref
commentEnd, ref commentSingle);
                         break;

                     case 'R':
                         linesOfRunstreamsCode(clLine);
                         break;

                     case 'Q':
                         linesOfIquRunstreamsCode(clLine);
                         break;

                     default:
                         // Anything else, a non-blank line is
executable
                         locExecutable++;
                         break;
                 }
             }
         }

         private void linesOfIquRunstreamsCode(String clLine)
         {
             // IQ/U Runstreams
             if (clLine.Substring(0, 1) == ".")
             {
                 locCommented++;
             }
             else
             {
                 locExecutable++;
             }
         }

         private void linesOfRunstreamsCode(String clLine)
         {
             // Runstreams
             if ((elementSubType == "IPF") && (clLine.Substring(0, 1)
== "@"))
             {   // IPF comment character
                 locCommented++;
             }
             else
             {
                 if ((elementSubType == "QLP") && (clLine.Substring(0,
1) == "*"))
                 {   // QLP comment character
                     locCommented++;
                 }
                 else
                 {   // Apply ECL comment rules
                     if ((clLine.Length > 2) && ((clLine.Substring(0,
3) == "@ .") || (clLine.Substring(0, 3) == "@. ")))
                     {   // ECL comment character
                         locCommented++;
                     }
                     else
                     {
                         locExecutable++;
                     }
                 }
             }
         }

         private void linesOfGuiCode(String clLine, ref String
commentStart, ref String commentEnd, ref String commentSingle)
         {
             determineLanguageCommentTags(ref commentStart, ref
commentEnd, ref commentSingle);

             if ((commentStart == "") && (commentEnd == "") &&
(commentSingle == ""))
             {   // We don't look for comments - if it's not blank,
it's executable
                 locExecutable++;
             }
             else
             {
                 if (inComment)
                 {   // We're in a multi-line comment
                     locCommented++;
                     if (clLine.IndexOf(commentEnd) >= 0)
                     {   // This is the last line of the multi-line
comment
                         inComment = false;
                     }
                 }
                 else
                 {
                     if (clLine.IndexOf(commentStart) >= 0)
                     {
                         countNewMultiLineComment(clLine,
commentStart, commentEnd);
                     }
                     else
                     {
                         countSingleLineComments(clLine,
commentSingle);
                     }
                 }
             }
         }

         private void countNewMultiLineComment(String clLine, String
commentStart, String commentEnd)
         {
             if (clLine.IndexOf(commentEnd) == -1)
             {   // Start of a multi-line comment
                 inComment = true;
             }
             if ((clLine.IndexOf(commentStart) == 0))
             {   // Nothing before the comment  - the entire line is
commented
                 locCommented++;
             }
             else
             {   // Something before the comment - count the line as
executable
                 locExecutable++;
             }
         }

         private void countSingleLineComments(String clLine, String
commentSingle)
         {
             if ((commentSingle != "") &&
(clLine.IndexOf(commentSingle) >= 0))
             {
                 if (clLine.IndexOf(commentSingle) == 0)
                 {   // The entire line is a comment
                     locCommented++;
                 }
                 else
                 {   // Only the end of the line is commented
                     locExecutable++;
                 }
             }
             else
             {
                 locExecutable++;
             }
         }

         private void determineLanguageCommentTags(ref String
commentStart, ref String commentEnd, ref String commentSingle)
         {
             // GUI
             if ((elementSubType == "HTML") || (elementSubType ==
"CSS") || (elementSubType == "XML"))
             {
                 commentStart = "<!--";
                 commentEnd = "-->";
             }
             else
             {
                 if (elementSubType == "XSLT")
                 {
                     commentStart = "<xsl:comment>";
                     commentEnd = "</xsl:comment>";
                 }
                 else
                 {
                     if (elementSubType == "JS")
                     {
                         commentStart = "/*";
                         commentEnd = "*/";
                         commentSingle = "//";
                     }
                 }
             }
         }

         private void lineOfCobolCode(String clLine)
         {
             // COBOL
             if ((clLine.Length > 6) && (clLine.Substring(6, 1) ==
"*"))
             {
                 locCommented++;
             }
             else
             {
                 locExecutable++;
             }
         }

         protected void updateProcXref(String upxLine)
         {
             // For this to work right, we need all items separated by
only one space
             upxLine = normalizeSpace(upxLine);

             switch (elementType)
             {
                 case 'P':
 
establishTheCrossReferenceBasedOnCopyStatement(upxLine);
                     break;

                 case 'L':
 
establishTheCrossReferenceBasedOnPerformStatement(upxLine);
                     break;
             }
         }

         private void
establishTheCrossReferenceBasedOnPerformStatement(String upxLine)
         {
             // Establish the cross-reference based on perform
statement
             if ((upxLine.Length > 9) && (upxLine.Substring(0, 8) ==
"PERFORM "))
             {
                 String[] words = upxLine.Split(' ');
                 String[] pieces = words[1].Split('-');

                 // Don't count performs of the proc itself
                 if ((pieces[0] != elementId) &&
(isElement(pieces[0])))
                 {   // See if this is already in the xref
                     SqlCommand scCheck = new SqlCommand("SELECT
ProgName FROM Proc_Prog_Xref "
                         + "WHERE ProgName = '" + elementId + "' "
                             + "AND ProcName = '" + pieces[0] + "'",
dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();
                     if (!drCheck.HasRows)
                     {
                         executeSQL("INSERT INTO Proc_Prog_Xref "
                             + "(ProgName, ProcName, Passive,
EntryPoint) "
                             + "VALUES ('" + elementId + "','"
                             + pieces[0] + "',1,NULL)");
                     }
                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();
                 }
             }
         }

         private void
establishTheCrossReferenceBasedOnCopyStatement(String upxLine)
         {
             // Establish the cross-reference based on copy statement
             if ((upxLine.Length > 6) && (upxLine.Substring(0, 5) ==
"COPY "))
             {
                 String[] words = upxLine.Split(' ');
                 String[] pieces = words[1].Split('-');

                 if (isElement(pieces[0]))
                 {   // See if this is already in the cross-reference
                     SqlCommand scCheck = new SqlCommand("SELECT
ProgName FROM Proc_Prog_Xref "
                         + "WHERE   ProgName   = '" + elementId + "' "
                             + "AND ProcName   = '" + pieces[0] + "' "
                             + "AND EntryPoint = '" + words[1] + "'",
dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();
                     if (!drCheck.HasRows)
                     {   // Add this program/proc to the table
                         executeSQL("INSERT INTO Proc_Prog_Xref "
                             + "(ProgName, ProcName, Passive,
EntryPoint) "
                             + "VALUES ('" + elementId + "','" +
                             pieces[0] + "',0,'" + words[1] + "')");
                     }
                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();
                 }
             }
         }

         protected void updateRejectXref(String urxLine, String
urxProcessName)
         {
             Int32 rejectCode;

             // Get rid of extra spaces
             urxLine = normalizeSpace(urxLine);

             if ((urxLine.IndexOf("REJCDE") >= 0) &&
(urxLine.IndexOf("MOVE ") >= 0))
             {   // Line is "MOVE [something] TO REJCDE"
                 String[] words = urxLine.Split(' ');
                 if (Int32.TryParse(words[1], out rejectCode))
                 {
                     // Mask off narratives to get the lowest 4 digits
                     rejectCode = rejectCode % 10000;

                     if (rejectCode > 0)
                     {   // Is this reject already in the xref?
                         SqlCommand scCheck = new SqlCommand("SELECT
program FROM RejectsXref "
                             + "WHERE program = '" + elementId + "' "
                                 + "AND reject_num = " +
rejectCode.ToString(), dbConn);
                         SqlDataReader drCheck =
scCheck.ExecuteReader();
                         if (!drCheck.HasRows)
                         {   // Insert it
                             executeSQL("INSERT INTO RejectsXref "
                                 + "(program, reject_num,
last_updated, last_updated_by) "
                                 + "VALUES ('" + elementId + "'," +
rejectCode.ToString()
                                 + ",current_timestamp,'" +
urxProcessName + "')");
                         }
                         drCheck.Close();
                         drCheck.Dispose();
                         scCheck.Dispose();
                     }
                 }
             }
         }

         protected void updateCallXref(String ucxLine)
         {
             String[] words = normalizeSpace(ucxLine).Split(' ');

             // Check for "PROGRAM-ID"
             if (words[0] == "PROGRAM-ID")
             {   // Save these off - we'll delete them at the end
                 programID.Add(words[1]);
             }

             if ((words.Length > 1) && (words[0] == "CALL"))
             {
                 if ((words[1].Substring(0,1) == "\"") ||
(words[1].Substring(0,1) == "'"))
                 {   // Calling a literal - this is one we'll store
                     String callName =
words[1].Substring(1,words[1].Length - 2);

                     SqlCommand scCheck = new SqlCommand("SELECT
Element_ID FROM sdp_CSCI_CALL_Xref "
                         + "WHERE Element_ID = '" + elementId + "' "
                             + "AND Call_Name = '" + callName +
"'",dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();
                     if (!drCheck.HasRows)
                     {   // It's not there - insert it
                         executeSQL("INSERT INTO sdp_CSCI_CALL_Xref "
                             + "(Element_ID, Call_Name) "
                             + "VALUES ('" + elementId + "','" +
callName + "')");
                     }
                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();
                 }
             }
         }

         protected void updateCull(String ucLine)
         {
             ucLine = normalizeSpace(ucLine);

             if (   (ucLine.IndexOf("FETCH ")  >= 0) ||
(ucLine.IndexOf("FIND ")   >= 0)
                 || (ucLine.IndexOf("MODIFY ") >= 0) ||
(ucLine.IndexOf("STORE ")  >= 0)
                 || (ucLine.IndexOf("DELETE ") >= 0) ||
(ucLine.IndexOf("INSERT ") >= 0)
                 || (ucLine.IndexOf("REMOVE ") >= 0))
             {
                 updateCullRecord(ucLine);
             }
             else
             {
 
splitUpTheWordsAndCheckForDmsFieldNameOrRprocDataName(ucLine);
             }
         }

         private void
splitUpTheWordsAndCheckForDmsFieldNameOrRprocDataName(String ucLine)
         {
             // Split up the words, and check for a DMS field name or
R-proc data name
             String[] words = ucLine.Split(' ');
             for (int i = 0; i < words.Length; i++)
             {
                 if ((!isCobolKeyword(words[i])) && (!
hasSymbols(words[i])))
                 {
                     updateCullItem(words[i], ucLine);
                 }
             }
         }

         // Update DML records in cull
         protected void updateCullRecord(String ucrLine)
         {
             String[] words  = ucrLine.Split(' ');
             Int32    word   = 0;
             String   column = "";

             // --- CHECK #1 --- record name //

             checkRecordName(words, ref word, ref column);

             // --- CHECK #2 --- set name //

             checkSetname(ucrLine, words, ref word, ref column);
         }

         private void checkSetname(String ucrLine, String[] words, ref
Int32 word, ref String column)
         {
             if ((ucrLine.IndexOf(" SET") >= 0) ||
(ucrLine.IndexOf("VIA ") >= 0))
             {
                 String setName = "";

                 // Find the word "via" or "set"
                 word = 0;
                 while ((words[word] != "VIA") && (words[word] !=
"SET"))
                 {
                     word++;
                 }

                 if ((words[word] == "SET") && (word > 0))
                 {   // "FETCH xxx WITHIN xxxx SET", "REMOVE xxxx FROM
xxxxx SET", etc.
                     setName = words[--word];
                 }
                 else
                 {
                     if ((words[word] == "VIA") && (word <
(words.Length - 1)))
                     {   // "FETCH xxx VIA xxxx USING xxxx" format
statement
                         setName = words[++word];
                     }
                 }

                 if (setName != "")
                 {
                     // Is this a valid set name?
                     SqlCommand scSetChk = new SqlCommand("SELECT
set_name FROM dms_sets "
                         + "WHERE set_name = '" + setName + "'",
dbHelp);
                     SqlDataReader drSetChk =
scSetChk.ExecuteReader();

                     if (drSetChk.HasRows)
                     {
                         // What column name do we update?
                         column = "";

                         if ((ucrLine.IndexOf("FETCH ") >= 0) ||
(ucrLine.IndexOf("FIND ") >= 0))
                         {
                             column = "Fetches";
                         }
                         else
                         {
                             if (ucrLine.IndexOf("INSERT") >= 0)
                             {
                                 column = "Inserts";
                             }
                             else
                             {
                                 if (ucrLine.IndexOf("REMOVE") >= 0)
                                 {
                                     column = "Removes";
                                 }
                             }
                         }

                         if (column != "")
                         {   // Does it already exist in the cross-
reference?
                             SqlCommand scCheck = new
SqlCommand("SELECT Dbr FROM sdp_Dbr_Csci_Xref "
                                 + "WHERE Dbr = '" + setName + "'",
dbConn);
                             SqlDataReader drCheck =
scCheck.ExecuteReader();

                             if (!drCheck.HasRows)
                             {   // Insert a new blank row
                                 SqlCommand scInsert = new
SqlCommand("INSERT INTO sdp_Dbr_Csci_Xref "
                                     + "(Dbr, Csci, Fetches, Modifies,
Inserts, Stores, Removes, Deletes) "
                                     + "VALUES ('" + setName + "','" +
elementId + "',0,0,0,0,0,0)", dbConn);
                                 scInsert.ExecuteNonQuery();
                                 scInsert.Dispose();
                             }

                             drCheck.Close();
                             drCheck.Dispose();
                             scCheck.Dispose();

                             SqlCommand scUpdate = new
SqlCommand("UPDATE sdp_Dbr_Csci_Xref "
                                 + "SET " + column + " = " + column +
" + 1 "
                                 + "WHERE Dbr = '" + setName + "' "
                                     + "AND Csci = '" + elementId +
"'", dbConn);
                             scUpdate.ExecuteNonQuery();
                             scUpdate.Dispose();
                         }
                     }

                     drSetChk.Close();
                     drSetChk.Dispose();
                     scSetChk.Dispose();
                 }
             }
         }

         private void checkRecordName(String[] words, ref Int32 word,
ref String column)
         {
             // Find the word where we're doing the DML
             while ((words[word] != "FETCH") && (words[word] !=
"FIND")
                 && (words[word] != "MODIFY") && (words[word] !=
"STORE")
                 && (words[word] != "DELETE") && (words[word] !=
"INSERT")
                 && (words[word] != "REMOVE") && (word <
words.Length))
             {
                 word++;
             }

             if ((word < (words.Length - 2))
                 && ((words[word + 1] == "FIRST") || (words[word + 1]
== "NEXT")
                     || (words[word + 1] == "PRIOR") || (words[word +
1] == "LAST")))
             {   // "FETCH FIRST xxx", etc.
                 word++;
             }

             if ((word < (words.Length - 2)) && (words[word + 1] !=
"RECORD"))
             {
                 // Determine the proper column name
                 if ((words[word] == "FETCH") || (words[word] ==
"FIND"))
                 {
                     column = "Fetches";
                 }
                 else
                 {
                     if (words[word] == "MODIFY")
                     {
                         column = "Modifies";
                     }
                     else
                     {
                         column = words[word].ToLower() + "s";
                     }
                 }

                 // The next word may be a record name
                 String recordName = words[++word];

                 // Is this name a valid record?
                 SqlCommand scRecChk = new SqlCommand("SELECT
record_name FROM dms_records "
                     + "WHERE record_name = '" + recordName + "'",
dbHelp);
                 SqlDataReader drRecChk = scRecChk.ExecuteReader();

                 if (drRecChk.HasRows)
                 {   // Does the record already exist in the cross-
reference?
                     SqlCommand scCheck = new SqlCommand("SELECT CSCI
FROM sdp_Dbr_Csci_Xref "
                         + "WHERE Dbr = '" + recordName + "' "
                             + "AND Csci = '" + elementId + "'",
dbConn);
                     SqlDataReader drCheck = scCheck.ExecuteReader();

                     if (!drCheck.HasRows)
                     {   // Add a new zeroed-out row
                         SqlCommand scInsert = new SqlCommand("INSERT
INTO sdp_Dbr_Csci_Xref "
                             + "(Dbr, Csci, Fetches, Modifies,
Inserts, Stores, Removes, Deletes) "
                             + "VALUES ('" + recordName + "','" +
elementId + "',0,0,0,0,0,0)", dbConn);
                         scInsert.ExecuteNonQuery();
                         scInsert.Dispose();
                     }

                     drCheck.Close();
                     drCheck.Dispose();
                     scCheck.Dispose();

                     // Update this count
                     SqlCommand scUpdate = new SqlCommand("UPDATE
sdp_Dbr_Csci_Xref "
                         + "SET " + column + " = " + column + " + 1 "
                         + "WHERE Dbr = '" + recordName + "' "
                             + "AND Csci = '" + elementId + "'",
dbConn);
                     scUpdate.ExecuteNonQuery();
                     scUpdate.Dispose();
                 }

                 drRecChk.Close();
                 drRecChk.Dispose();
                 scRecChk.Dispose();
             }
         }

         protected void updateCullItem(String uciWord, String uciLine)
         {
             bool used    = false;
             bool updated = false;

             // Check to see if the word starts with "R" and has a
dash, and is not this proc
             if ((uciWord.Substring(0,1) == "R")
                 && (uciWord.Substring(3,1) == "-")
                 && (uciWord.Substring(0,4) != elementId))
             {
                 if (uciLine.IndexOf("PERFORM") >= 0)
                 {   // We've got a paragraph name performed
                     SqlCommand scTables = new SqlCommand("SELECT
DISTINCT table_name rt "
                         + "FROM rdms_tables rt, rdms_table_columns
rtc "
                         + "WHERE rt.table_name = rtc.table_name "
                         + "AND rtc.r_proc_element_name LIKE '"
                         + uciWord.Substring(0,4) + "%'",dbHelp);
                     SqlDataReader drTables =
scTables.ExecuteReader();

                     while(drTables.HasRows)
                     {   // See if this table already exists in the
cull look-up
                         int i = 0; // !WORK this is crap
                     }
                 }
                 else
                 {
                     if (uciLine.IndexOf("MOVE") >= 0)
                     {
                         if (uciLine.IndexOf("TO") >
uciLine.IndexOf(uciWord))
                         {
                             used = true;
                         }
                         else
                         {
                             updated = true;
                         }
                     }
                     else
                     {
                         updated = true;
                     }
                 }
             }
             else
             {   // See if the word is a valid DMS field
             }
         }

         // Establish connections with the database
         protected void openSqlConnection(String oscServerName)
         {
             String connString = "";

             if (oscServerName == "") {
                 oscServerName = "[servername]";
             }

             connString = "server=" + oscServerName +
";database=[database];User ID=[user];Password=[password];";
             dbConn = new SqlConnection(connString);
             dbConn.Open();

             connString = connString.Replace("[database]","[another-
database]");
             dbHelp = new SqlConnection(connString);
             dbHelp.Open();
         }

         public String cscsRegValue(String crvKey)
         {
             SqlCommand crvCmd = new SqlCommand("SELECT reg_value "
                 + "FROM sdp_registry "
                 + "WHERE reg_key = '" + crvKey + "'", dbConn);
             SqlDataReader crvDR = crvCmd.ExecuteReader();
             if (crvDR.Read())
             {
                 return(crvDR["reg_value"].ToString().Trim());
             }
             else
             {
                 return("");
             }
         }

         protected void executeSQL(String esText)
         {
             SqlConnection esConn = new
SqlConnection(dbConn.ConnectionString + "password=[password];");
             SqlCommand    esCmd  = new SqlCommand(esText, esConn);
             esConn.Open();
             esCmd.ExecuteNonQuery();
             esCmd.Dispose();
             esConn.Close();
             esConn.Dispose();
         }

         // Eliminates all embedded spaces more than one
         protected String normalizeSpace(String nsText)
         {
             String workText = nsText;

             while (workText.IndexOf("  ") >= 0)
             {
                 workText = workText.Replace("  "," ");
             }
             return(workText);
         }

         // Returns "true" if the text passed is an element in CSCS
         protected bool isElement(String ieText)
         {
             Boolean itExists = false;

             SqlCommand ieCmd = new SqlCommand("SELECT Actv_Ind FROM
Active_Elements "
                 + " WHERE Element_ID = '" + ieText + "'", dbConn);
             SqlDataReader ieDR  = ieCmd.ExecuteReader();
             if (ieDR.HasRows) {
                 itExists = true;
             }
             ieDR.Close();
             ieDR.Dispose();
             ieCmd.Dispose();

             return(itExists);
         }

         // Returns "true" if the word passed is a COBOL keyword
         protected bool isCobolKeyword(String ickText)
         {
             Int32 i = 0;
             while ((i < cobolKeywords.Length) && (ickText !=
cobolKeywords[i]))
             {
                 i++;
             }
             if (i < cobolKeywords.Length)
             {
                 return(true);
             }
             else
             {
                 return(false);
             }
         }

         // Returns "true" if the words passed has symbols in it
         protected bool hasSymbols(String hsText)
         {
             if (   (hsText.IndexOf("(")  >= 0) ||
(hsText.IndexOf(")")  >= 0)
                 || (hsText.IndexOf("\"") >= 0) ||
(hsText.IndexOf("'")  >= 0)
                 || (hsText.IndexOf("_")  >= 0))
             {
                 return(true);
             }
             else
             {
                 return(false);
             }
         }

     }

}
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-01-31T22:29:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET>`
- **In-Reply-To:** `<1170291697.002493.111010@h3g2000cwc.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com>`

```
andrewmcdonagh wrote:
> Ok, so I downloaded and installed vs2005 express, loaded your class
> and started using the 'refactoring -> extract method' right click menu
…[4 more quoted lines elided]…
> that posting it to here causes...)

Very cool.  I'll be going from this (probably shortening some of those 
method names), but I like it.  :)

[snipped to save bits]
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 4)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-01T03:13:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170328381.191570.78970@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET>`

```
On Feb 1, 4:29 am, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
> > Ok, so I downloaded and installed vs2005 express, loaded your class
…[11 more quoted lines elided]…
>

Cool!

Yeah those names are a bit long (but then again, you only have to type
them once as intellisense will create them for you every other time),
but I did it deliberately to show the technique of 'convert comments
into private method names' to get you started on 'self documenting'
code.

I'll continue to play with the class over the next few days when I get
time and post the new versions on here....  (I'm thinking we'll
transition to something like a dozen small classes working
together....)

This exercise is good for me too, as I've never used c# before, only
read about it...

:)

Once we have this out of the way...the next biggest priority on your
learning curve, should be how to develop code that has a full suite of
automated Unit tests - NUnit is the unit testing framework of choice
for .Net and should even be integrated into vs2005....  Normally I
wouldn't do any code changes like these without a suite of unit tests
to show me instantly if I break something... but one leasson at a
time.

Cheers

Andrew

Andrew
Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-01T08:17:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1b282$45c1f66f$454920f8$21345@KNOLOGY.NET>`
- **In-Reply-To:** `<1170328381.191570.78970@q2g2000cwa.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170328381.191570.78970@q2g2000cwa.googlegroups.com>`

```
andrewmcdonagh wrote:
> Cool!
> 
…[4 more quoted lines elided]…
> code.

That's cool.  I tend to comment a lot - more than any other programmer 
in our shop.  (We proved that by looking at the output from this class - 
my commenting average is between 22% and 28% compared to executable 
lines in COBOL...)

> I'll continue to play with the class over the next few days when I get
> time and post the new versions on here....  (I'm thinking we'll
…[4 more quoted lines elided]…
> read about it...

I appreciate it - I'm glad it's helping you too.  Of course, I'm sort of 
learning the two together, but I've been surprised how much Java works 
in C# - and if it doesn't work, it probably just has a different name.

> Once we have this out of the way...the next biggest priority on your
> learning curve, should be how to develop code that has a full suite of
…[4 more quoted lines elided]…
> time.

I'll have to look into that.  How should I put this - code "robustness" 
has been an issue with some of our .net pages.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 4)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-04T15:03:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170630207.802313.39030@l53g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET>`

```
On Feb 1, 4:29 am, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
> > Ok, so I downloaded and installed vs2005 express, loaded your class
…[9 more quoted lines elided]…
>

snipped...

Hi,

So here's the next instalment - not a big change (haven't had the time
over the weekend).

So the conversation about the keywords drew my attention to it
properly for the first time...as I was looking at the large methods
before. Once saw what the array was being used for and the
'isCobolKeyword()' method, I saw that here was one of our first
Responsabilities that needs to be pulled out into its own class.  As
you had already created the private method 'isCobolKeyword()' this was
even easier for me than other refactrings. It also shows that you are
already looking at the design with a view to creating discrete logical
parts.

So the refactoring I did was....

1) Create a new Interface called 'KeywordDictionary'
    with a single method 'isKeyword(String keyword)

2) Create a new Class called CobolKeywordDictionary
2.1)   Copied the large keyword array into this new class.
2.2)   Copied the 'isCobolKeyword(String ictText) method into this new
class.
2.3)   Changed the copied method's name to match the Interface's
method (i.e 'isKeyword(String ictText)' )
2.4)   Renamed the method parameter to be more self commenting:
'ictText' became  'keyword'

Note: At this point, I haven't changed a single line of the
CodeStatistics class, and so it STILL compiles and works!

3) Create a new member variable within CodeStatistics class, like so:

        private KeywordDictionary keywordDictionary = new
CobolKeywordDictionary();

4) Searched through CodeStatistics class for all usages of its own
'isCobolKeyword(xyz)' and replaced it with
'keywordDictionary.isKeyword(xyz) '

5) Now the CodeStatistics own keyword array and its 'isCobolKeyword'
methods are unused, and so we delete them.

All along, through out this refactoring, the code continued to build
and work.  And making the switch from old to new was the last step.

So, you might ask 'why the interface?'  good question!

There is no current need for it, but my OO and Unit testing sense
tends to say create an interface more often than not - it will pay for
itself sooner rather than later.
Besides, Interfaces do not incur any runtime performance costs (that
are worth caring about).

What i mean about OO sense, is that now we have separated the
Responsibility of specifying what a KeywordDictionary 'is', compared
to its implementation - CobolKeywordDictionary in our case, or later,
HtmlKeywordDictionary, JavaKeywordDictionary, etc....

>From a unit testing sense, it means I can write a unit test for my
CobolKeywordDictionary, by using the class directly, I dont need to
test it, by creating an instance of something that just happens to use
it (CodeStatistics in our case).

HTH

Andrew

---------------------------------------------------------------------------------

The latest code:


using System;
using System.Collections.Generic;
using System.Text;

namespace CodeStats
{

    interface KeywordDictionary
    {
        bool isKeyword(String keyword);
    }
}


----------------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Text;

namespace CodeStats
{
    class CobolKeywordDictionary : KeywordDictionary
    {

        private String[] cobolKeywords =
             {"ACCEPT",........snipped...to save space

                 "ZEROS","+","-","*","/","**",">","<","=",">=","<="};

        public bool isKeyword(String keyword)
        {
            Int32 i = 0;
            while ((i < cobolKeywords.Length) && (keyword !=
cobolKeywords[i]))
            {
                i++;
            }
            if (i < cobolKeywords.Length)
            {
                return (true);
            }
            else
            {
                return (false);
            }
        }
    }
}




----------------------------------------------------------------------------------------------------------------------------------
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Text;

namespace CodeStats
{
    public class CodeStatistics
    {
        // Properties (public instance variables)
        bool updatedStats = false;
        String elementId = "";
        int locTotal = 0;
        int locExecutable = 0;
        int locCommented = 0;

        // Private instance variables
        protected SqlConnection dbConn;
        protected SqlConnection dbHelp;
        protected char elementType = ' ';
        protected String elementSubType = "";
        protected String fileName = "";
        protected bool inComment = false;
        protected List<String> programID = new List<String>();

        private KeywordDictionary keywordDictionary = new
CobolKeywordDictionary();

        // Constuctor for no parameter
        public CodeStatistics(String csServerName)
        {
            openSqlConnection(csServerName);
        }

        // Constructor for passed Element ID
        public CodeStatistics(String csServerName, String csElementId)
        {
            openSqlConnection(csServerName);
            retrieveElementInfo(csElementId);
        }

        // Establish the element for this class instance
        public void retrieveElementInfo(String reiElementId)
        {
            // Retrieve the information about the passed program
            SqlCommand cmd = new SqlCommand("SELECT element_id,
element_type, element_subtype, server_name "
                + "FROM active_elements "
                + "WHERE element_id = '" + reiElementId.Trim() + "'",
dbConn);
            SqlDataReader dr = cmd.ExecuteReader();
            if (dr.Read())
            {
                elementType =
Convert.ToChar(dr["element_type"].ToString().Trim().Substring(0, 1));
                elementSubType =
dr["element_subtype"].ToString().Trim();
                fileName = dr["server_name"].ToString().Trim();
                elementId = reiElementId;
            }
            dr.Close();
            dr.Dispose();
        }

        // Update the statistics for the element ID
        public void updateStatistics(String usPath, String
usProcessName)
        {
            if (File.Exists(usPath + fileName))
            {
                String textLine = "";

                clearOutCrossReferenceTables();

                textLine = parseFile(usPath, usProcessName, textLine);

 
deleteAnyReferencesToCallsIfTheTargetIsDefinedInTheProgram();

                updateLocInTheCscsDatabase();
            }
        }

        private void updateLocInTheCscsDatabase()
        {
            // Update LOC in the CSCS database
            SqlCommand sc = new SqlCommand("UPDATE Active_Elements "
                + "SET   Commented_Lines  = " +
locCommented.ToString()
                    + ", Executable_Lines = " +
locExecutable.ToString()
                    + ", Total_Lines      = " + locTotal.ToString()
                + "WHERE Element_ID = '" + elementId + "'", dbConn);
            sc.ExecuteNonQuery();
            sc.Dispose();
        }

        private void
deleteAnyReferencesToCallsIfTheTargetIsDefinedInTheProgram()
        {
            if (programID.Count > 0)
            {   // Delete any references to calls if the target is
defined in the program (i.e., nested subprograms)
                SqlCommand scDelete = new SqlCommand();

                scDelete.CommandText = "DELETE FROM sdp_CSCI_CALL_Xref
"
                    + "WHERE Element_ID = '" + elementId + "' "
                        + "AND Call_Name IN ('";
                for (int i = 0; i < programID.Count; i++)
                {
                    scDelete.CommandText += programID[i] + "'";
                    if (i < (programID.Count - 1))
                    {
                        scDelete.CommandText += ",'";
                    }
                }
                scDelete.CommandText += ")";
                scDelete.Connection = dbConn;
                scDelete.ExecuteNonQuery();
                scDelete.Dispose();
            }
        }

        private String parseFile(String usPath, String usProcessName,
String textLine)
        {
            StreamReader file = File.OpenText(usPath + fileName);

            while (!file.EndOfStream)
            {
                textLine = file.ReadLine().ToUpper();

                if ((elementType != 'P') && (elementType != 'L'))
                {
                    textLine = textLine.Trim();
                }

                countLine(textLine); // Count this line as a "line of
code"

                switch (elementType)
                {
                    case 'P':
                    case 'L':
                        textLine = textLine.Replace(",", "
").Replace(".", " ").Trim();
                        updateProcXref(textLine);
                        updateRejectXref(textLine, usProcessName);
                        updateCallXref(textLine);
                        //updateCull(textLine);
                        break;
                }

            }

            file.Close();
            file.Dispose();
            return textLine;
        }

        private void clearOutCrossReferenceTables()
        {
            // Depending on the type, clear out the cross-reference
tables
            switch (elementType)
            {
                case 'P':
                case 'L':
                    SqlCommand scDel = new SqlCommand();
                    scDel.Connection = dbConn;

                    // Delete item/proc xref
                    scDel.CommandText = "DELETE FROM Proc_Prog_Xref
WHERE ProgName = '" + elementId + "'";
                    scDel.ExecuteNonQuery();

                    // Delete item/reject xref
                    scDel.CommandText = "DELETE FROM RejectsXref WHERE
program = '" + elementId + "'";
                    scDel.ExecuteNonQuery();

                    // Delete item/call xref
                    scDel.CommandText = "DELETE FROM
sdp_CSCI_Call_Xref WHERE Element_ID = '" + elementId + "'";
                    scDel.ExecuteNonQuery();

                    // Delete cull information
                    scDel.CommandText = "DELETE FROM sdp_Dbe_Csci_Xref
WHERE CSCI = '" + elementId + "'";
                    scDel.ExecuteNonQuery();
                    scDel.CommandText = "DELETE FROM sdp_Dbr_Csci_Xref
WHERE CSCI = '" + elementId + "'";
                    scDel.ExecuteNonQuery();

                    scDel.Dispose();
                    break;
            }
        }

        protected void countLine(String clLine)
        {
            String commentStart = "";
            String commentEnd = "";
            String commentSingle = "";

            // A line is a line...
            locTotal++;

            if (clLine != "")
            {
                switch (elementType)
                {
                    case 'P':
                    case 'L':
                        lineOfCobolCode(clLine);
                        break;

                    case 'G':
                        linesOfGuiCode(clLine, ref commentStart, ref
commentEnd, ref commentSingle);
                        break;

                    case 'R':
                        linesOfRunstreamsCode(clLine);
                        break;

                    case 'Q':
                        linesOfIquRunstreamsCode(clLine);
                        break;

                    default:
                        // Anything else, a non-blank line is
executable
                        locExecutable++;
                        break;
                }
            }
        }

        private void linesOfIquRunstreamsCode(String clLine)
        {
            // IQ/U Runstreams
            if (clLine.Substring(0, 1) == ".")
            {
                locCommented++;
            }
            else
            {
                locExecutable++;
            }
        }

        private void linesOfRunstreamsCode(String clLine)
        {
            // Runstreams
            if ((elementSubType == "IPF") && (clLine.Substring(0, 1)
== "@"))
            {   // IPF comment character
                locCommented++;
            }
            else
            {
                if ((elementSubType == "QLP") && (clLine.Substring(0,
1) == "*"))
                {   // QLP comment character
                    locCommented++;
                }
                else
                {   // Apply ECL comment rules
                    if ((clLine.Length > 2) && ((clLine.Substring(0,
3) == "@ .") || (clLine.Substring(0, 3) == "@. ")))
                    {   // ECL comment character
                        locCommented++;
                    }
                    else
                    {
                        locExecutable++;
                    }
                }
            }
        }

        private void linesOfGuiCode(String clLine, ref String
commentStart, ref String commentEnd, ref String commentSingle)
        {
            determineLanguageCommentTags(ref commentStart, ref
commentEnd, ref commentSingle);

            if ((commentStart == "") && (commentEnd == "") &&
(commentSingle == ""))
            {   // We don't look for comments - if it's not blank,
it's executable
                locExecutable++;
            }
            else
            {
                if (inComment)
                {   // We're in a multi-line comment
                    locCommented++;
                    if (clLine.IndexOf(commentEnd) >= 0)
                    {   // This is the last line of the multi-line
comment
                        inComment = false;
                    }
                }
                else
                {
                    if (clLine.IndexOf(commentStart) >= 0)
                    {
                        countNewMultiLineComment(clLine, commentStart,
commentEnd);
                    }
                    else
                    {
                        countSingleLineComments(clLine,
commentSingle);
                    }
                }
            }
        }

        private void countNewMultiLineComment(String clLine, String
commentStart, String commentEnd)
        {
            if (clLine.IndexOf(commentEnd) == -1)
            {   // Start of a multi-line comment
                inComment = true;
            }
            if ((clLine.IndexOf(commentStart) == 0))
            {   // Nothing before the comment  - the entire line is
commented
                locCommented++;
            }
            else
            {   // Something before the comment - count the line as
executable
                locExecutable++;
            }
        }

        private void countSingleLineComments(String clLine, String
commentSingle)
        {
            if ((commentSingle != "") &&
(clLine.IndexOf(commentSingle) >= 0))
            {
                if (clLine.IndexOf(commentSingle) == 0)
                {   // The entire line is a comment
                    locCommented++;
                }
                else
                {   // Only the end of the line is commented
                    locExecutable++;
                }
            }
            else
            {
                locExecutable++;
            }
        }

        private void determineLanguageCommentTags(ref String
commentStart, ref String commentEnd, ref String commentSingle)
        {
            // GUI
            if ((elementSubType == "HTML") || (elementSubType ==
"CSS") || (elementSubType == "XML"))
            {
                commentStart = "<!--";
                commentEnd = "-->";
            }
            else
            {
                if (elementSubType == "XSLT")
                {
                    commentStart = "<xsl:comment>";
                    commentEnd = "</xsl:comment>";
                }
                else
                {
                    if (elementSubType == "JS")
                    {
                        commentStart = "/*";
                        commentEnd = "*/";
                        commentSingle = "//";
                    }
                }
            }
        }

        private void lineOfCobolCode(String clLine)
        {
            // COBOL
            if ((clLine.Length > 6) && (clLine.Substring(6, 1) ==
"*"))
            {
                locCommented++;
            }
            else
            {
                locExecutable++;
            }
        }

        protected void updateProcXref(String upxLine)
        {
            // For this to work right, we need all items separated by
only one space
            upxLine = normalizeSpace(upxLine);

            switch (elementType)
            {
                case 'P':
 
establishTheCrossReferenceBasedOnCopyStatement(upxLine);
                    break;

                case 'L':
 
establishTheCrossReferenceBasedOnPerformStatement(upxLine);
                    break;
            }
        }

        private void
establishTheCrossReferenceBasedOnPerformStatement(String upxLine)
        {
            // Establish the cross-reference based on perform
statement
            if ((upxLine.Length > 9) && (upxLine.Substring(0, 8) ==
"PERFORM "))
            {
                String[] words = upxLine.Split(' ');
                String[] pieces = words[1].Split('-');

                // Don't count performs of the proc itself
                if ((pieces[0] != elementId) &&
(isElement(pieces[0])))
                {   // See if this is already in the xref
                    SqlCommand scCheck = new SqlCommand("SELECT
ProgName FROM Proc_Prog_Xref "
                        + "WHERE ProgName = '" + elementId + "' "
                            + "AND ProcName = '" + pieces[0] + "'",
dbConn);
                    SqlDataReader drCheck = scCheck.ExecuteReader();
                    if (!drCheck.HasRows)
                    {
                        executeSQL("INSERT INTO Proc_Prog_Xref "
                            + "(ProgName, ProcName, Passive,
EntryPoint) "
                            + "VALUES ('" + elementId + "','"
                            + pieces[0] + "',1,NULL)");
                    }
                    drCheck.Close();
                    drCheck.Dispose();
                    scCheck.Dispose();
                }
            }
        }

        private void
establishTheCrossReferenceBasedOnCopyStatement(String upxLine)
        {
            // Establish the cross-reference based on copy statement
            if ((upxLine.Length > 6) && (upxLine.Substring(0, 5) ==
"COPY "))
            {
                String[] words = upxLine.Split(' ');
                String[] pieces = words[1].Split('-');

                if (isElement(pieces[0]))
                {   // See if this is already in the cross-reference
                    SqlCommand scCheck = new SqlCommand("SELECT
ProgName FROM Proc_Prog_Xref "
                        + "WHERE   ProgName   = '" + elementId + "' "
                            + "AND ProcName   = '" + pieces[0] + "' "
                            + "AND EntryPoint = '" + words[1] + "'",
dbConn);
                    SqlDataReader drCheck = scCheck.ExecuteReader();
                    if (!drCheck.HasRows)
                    {   // Add this program/proc to the table
                        executeSQL("INSERT INTO Proc_Prog_Xref "
                            + "(ProgName, ProcName, Passive,
EntryPoint) "
                            + "VALUES ('" + elementId + "','" +
                            pieces[0] + "',0,'" + words[1] + "')");
                    }
                    drCheck.Close();
                    drCheck.Dispose();
                    scCheck.Dispose();
                }
            }
        }

        protected void updateRejectXref(String urxLine, String
urxProcessName)
        {
            Int32 rejectCode;

            // Get rid of extra spaces
            urxLine = normalizeSpace(urxLine);

            if ((urxLine.IndexOf("REJCDE") >= 0) &&
(urxLine.IndexOf("MOVE ") >= 0))
            {   // Line is "MOVE [something] TO REJCDE"
                String[] words = urxLine.Split(' ');
                if (Int32.TryParse(words[1], out rejectCode))
                {
                    // Mask off narratives to get the lowest 4 digits
                    rejectCode = rejectCode % 10000;

                    if (rejectCode > 0)
                    {   // Is this reject already in the xref?
                        SqlCommand scCheck = new SqlCommand("SELECT
program FROM RejectsXref "
                            + "WHERE program = '" + elementId + "' "
                                + "AND reject_num = " +
rejectCode.ToString(), dbConn);
                        SqlDataReader drCheck =
scCheck.ExecuteReader();
                        if (!drCheck.HasRows)
                        {   // Insert it
                            executeSQL("INSERT INTO RejectsXref "
                                + "(program, reject_num, last_updated,
last_updated_by) "
                                + "VALUES ('" + elementId + "'," +
rejectCode.ToString()
                                + ",current_timestamp,'" +
urxProcessName + "')");
                        }
                        drCheck.Close();
                        drCheck.Dispose();
                        scCheck.Dispose();
                    }
                }
            }
        }

        protected void updateCallXref(String ucxLine)
        {
            String[] words = normalizeSpace(ucxLine).Split(' ');

            // Check for "PROGRAM-ID"
            if (words[0] == "PROGRAM-ID")
            {   // Save these off - we'll delete them at the end
                programID.Add(words[1]);
            }

            if ((words.Length > 1) && (words[0] == "CALL"))
            {
                if ((words[1].Substring(0, 1) == "\"") ||
(words[1].Substring(0, 1) == "'"))
                {   // Calling a literal - this is one we'll store
                    String callName = words[1].Substring(1,
words[1].Length - 2);

                    SqlCommand scCheck = new SqlCommand("SELECT
Element_ID FROM sdp_CSCI_CALL_Xref "
                        + "WHERE Element_ID = '" + elementId + "' "
                            + "AND Call_Name = '" + callName + "'",
dbConn);
                    SqlDataReader drCheck = scCheck.ExecuteReader();
                    if (!drCheck.HasRows)
                    {   // It's not there - insert it
                        executeSQL("INSERT INTO sdp_CSCI_CALL_Xref "
                            + "(Element_ID, Call_Name) "
                            + "VALUES ('" + elementId + "','" +
callName + "')");
                    }
                    drCheck.Close();
                    drCheck.Dispose();
                    scCheck.Dispose();
                }
            }
        }

        protected void updateCull(String ucLine)
        {
            ucLine = normalizeSpace(ucLine);

            if ((ucLine.IndexOf("FETCH ") >= 0) ||
(ucLine.IndexOf("FIND ") >= 0)
                || (ucLine.IndexOf("MODIFY ") >= 0) ||
(ucLine.IndexOf("STORE ") >= 0)
                || (ucLine.IndexOf("DELETE ") >= 0) ||
(ucLine.IndexOf("INSERT ") >= 0)
                || (ucLine.IndexOf("REMOVE ") >= 0))
            {
                updateCullRecord(ucLine);
            }
            else
            {
 
splitUpTheWordsAndCheckForDmsFieldNameOrRprocDataName(ucLine);
            }
        }

        private void
splitUpTheWordsAndCheckForDmsFieldNameOrRprocDataName(String ucLine)
        {
            // Split up the words, and check for a DMS field name or R-
proc data name
            String[] words = ucLine.Split(' ');
            for (int i = 0; i < words.Length; i++)
            {
                if ((! keywordDictionary.isKeyword(words[i])) && (!
hasSymbols(words[i])))
                {
                    updateCullItem(words[i], ucLine);
                }
            }
        }

        // Update DML records in cull
        protected void updateCullRecord(String ucrLine)
        {
            String[] words = ucrLine.Split(' ');
            Int32 word = 0;
            String column = "";

            // --- CHECK #1 --- record name //

            checkRecordName(words, ref word, ref column);

            // --- CHECK #2 --- set name //

            checkSetname(ucrLine, words, ref word, ref column);
        }

        private void checkSetname(String ucrLine, String[] words, ref
Int32 word, ref String column)
        {
            if ((ucrLine.IndexOf(" SET") >= 0) ||
(ucrLine.IndexOf("VIA ") >= 0))
            {
                String setName = "";

                // Find the word "via" or "set"
                word = 0;
                while ((words[word] != "VIA") && (words[word] !=
"SET"))
                {
                    word++;
                }

                if ((words[word] == "SET") && (word > 0))
                {   // "FETCH xxx WITHIN xxxx SET", "REMOVE xxxx FROM
xxxxx SET", etc.
                    setName = words[--word];
                }
                else
                {
                    if ((words[word] == "VIA") && (word <
(words.Length - 1)))
                    {   // "FETCH xxx VIA xxxx USING xxxx" format
statement
                        setName = words[++word];
                    }
                }

                if (setName != "")
                {
                    // Is this a valid set name?
                    SqlCommand scSetChk = new SqlCommand("SELECT
set_name FROM dms_sets "
                        + "WHERE set_name = '" + setName + "'",
dbHelp);
                    SqlDataReader drSetChk = scSetChk.ExecuteReader();

                    if (drSetChk.HasRows)
                    {
                        // What column name do we update?
                        column = "";

                        if ((ucrLine.IndexOf("FETCH ") >= 0) ||
(ucrLine.IndexOf("FIND ") >= 0))
                        {
                            column = "Fetches";
                        }
                        else
                        {
                            if (ucrLine.IndexOf("INSERT") >= 0)
                            {
                                column = "Inserts";
                            }
                            else
                            {
                                if (ucrLine.IndexOf("REMOVE") >= 0)
                                {
                                    column = "Removes";
                                }
                            }
                        }

                        if (column != "")
                        {   // Does it already exist in the cross-
reference?
                            SqlCommand scCheck = new
SqlCommand("SELECT Dbr FROM sdp_Dbr_Csci_Xref "
                                + "WHERE Dbr = '" + setName + "'",
dbConn);
                            SqlDataReader drCheck =
scCheck.ExecuteReader();

                            if (!drCheck.HasRows)
                            {   // Insert a new blank row
                                SqlCommand scInsert = new
SqlCommand("INSERT INTO sdp_Dbr_Csci_Xref "
                                    + "(Dbr, Csci, Fetches, Modifies,
Inserts, Stores, Removes, Deletes) "
                                    + "VALUES ('" + setName + "','" +
elementId + "',0,0,0,0,0,0)", dbConn);
                                scInsert.ExecuteNonQuery();
                                scInsert.Dispose();
                            }

                            drCheck.Close();
                            drCheck.Dispose();
                            scCheck.Dispose();

                            SqlCommand scUpdate = new
SqlCommand("UPDATE sdp_Dbr_Csci_Xref "
                                + "SET " + column + " = " + column + "
+ 1 "
                                + "WHERE Dbr = '" + setName + "' "
                                    + "AND Csci = '" + elementId +
"'", dbConn);
                            scUpdate.ExecuteNonQuery();
                            scUpdate.Dispose();
                        }
                    }

                    drSetChk.Close();
                    drSetChk.Dispose();
                    scSetChk.Dispose();
                }
            }
        }

        private void checkRecordName(String[] words, ref Int32 word,
ref String column)
        {
            // Find the word where we're doing the DML
            while ((words[word] != "FETCH") && (words[word] != "FIND")
                && (words[word] != "MODIFY") && (words[word] !=
"STORE")
                && (words[word] != "DELETE") && (words[word] !=
"INSERT")
                && (words[word] != "REMOVE") && (word < words.Length))
            {
                word++;
            }

            if ((word < (words.Length - 2))
                && ((words[word + 1] == "FIRST") || (words[word + 1]
== "NEXT")
                    || (words[word + 1] == "PRIOR") || (words[word +
1] == "LAST")))
            {   // "FETCH FIRST xxx", etc.
                word++;
            }

            if ((word < (words.Length - 2)) && (words[word + 1] !=
"RECORD"))
            {
                // Determine the proper column name
                if ((words[word] == "FETCH") || (words[word] ==
"FIND"))
                {
                    column = "Fetches";
                }
                else
                {
                    if (words[word] == "MODIFY")
                    {
                        column = "Modifies";
                    }
                    else
                    {
                        column = words[word].ToLower() + "s";
                    }
                }

                // The next word may be a record name
                String recordName = words[++word];

                // Is this name a valid record?
                SqlCommand scRecChk = new SqlCommand("SELECT
record_name FROM dms_records "
                    + "WHERE record_name = '" + recordName + "'",
dbHelp);
                SqlDataReader drRecChk = scRecChk.ExecuteReader();

                if (drRecChk.HasRows)
                {   // Does the record already exist in the cross-
reference?
                    SqlCommand scCheck = new SqlCommand("SELECT CSCI
FROM sdp_Dbr_Csci_Xref "
                        + "WHERE Dbr = '" + recordName + "' "
                            + "AND Csci = '" + elementId + "'",
dbConn);
                    SqlDataReader drCheck = scCheck.ExecuteReader();

                    if (!drCheck.HasRows)
                    {   // Add a new zeroed-out row
                        SqlCommand scInsert = new SqlCommand("INSERT
INTO sdp_Dbr_Csci_Xref "
                            + "(Dbr, Csci, Fetches, Modifies, Inserts,
Stores, Removes, Deletes) "
                            + "VALUES ('" + recordName + "','" +
elementId + "',0,0,0,0,0,0)", dbConn);
                        scInsert.ExecuteNonQuery();
                        scInsert.Dispose();
                    }

                    drCheck.Close();
                    drCheck.Dispose();
                    scCheck.Dispose();

                    // Update this count
                    SqlCommand scUpdate = new SqlCommand("UPDATE
sdp_Dbr_Csci_Xref "
                        + "SET " + column + " = " + column + " + 1 "
                        + "WHERE Dbr = '" + recordName + "' "
                            + "AND Csci = '" + elementId + "'",
dbConn);
                    scUpdate.ExecuteNonQuery();
                    scUpdate.Dispose();
                }

                drRecChk.Close();
                drRecChk.Dispose();
                scRecChk.Dispose();
            }
        }

        protected void updateCullItem(String uciWord, String uciLine)
        {
            bool used = false;
            bool updated = false;

            // Check to see if the word starts with "R" and has a
dash, and is not this proc
            if ((uciWord.Substring(0, 1) == "R")
                && (uciWord.Substring(3, 1) == "-")
                && (uciWord.Substring(0, 4) != elementId))
            {
                if (uciLine.IndexOf("PERFORM") >= 0)
                {   // We've got a paragraph name performed
                    SqlCommand scTables = new SqlCommand("SELECT
DISTINCT table_name rt "
                        + "FROM rdms_tables rt, rdms_table_columns rtc
"
                        + "WHERE rt.table_name = rtc.table_name "
                        + "AND rtc.r_proc_element_name LIKE '"
                        + uciWord.Substring(0, 4) + "%'", dbHelp);
                    SqlDataReader drTables = scTables.ExecuteReader();

                    while (drTables.HasRows)
                    {   // See if this table already exists in the
cull look-up
                        int i = 0; // !WORK this is crap
                    }
                }
                else
                {
                    if (uciLine.IndexOf("MOVE") >= 0)
                    {
                        if (uciLine.IndexOf("TO") >
uciLine.IndexOf(uciWord))
                        {
                            used = true;
                        }
                        else
                        {
                            updated = true;
                        }
                    }
                    else
                    {
                        updated = true;
                    }
                }
            }
            else
            {   // See if the word is a valid DMS field
            }
        }

        // Establish connections with the database
        protected void openSqlConnection(String oscServerName)
        {
            String connString = "";

            if (oscServerName == "")
            {
                oscServerName = "[servername]";
            }

            connString = "server=" + oscServerName +
";database=[database];User ID=[user];Password=[password];";
            dbConn = new SqlConnection(connString);
            dbConn.Open();

            connString = connString.Replace("[database]", "[another-
database]");
            dbHelp = new SqlConnection(connString);
            dbHelp.Open();
        }

        public String cscsRegValue(String crvKey)
        {
            SqlCommand crvCmd = new SqlCommand("SELECT reg_value "
                + "FROM sdp_registry "
                + "WHERE reg_key = '" + crvKey + "'", dbConn);
            SqlDataReader crvDR = crvCmd.ExecuteReader();
            if (crvDR.Read())
            {
                return (crvDR["reg_value"].ToString().Trim());
            }
            else
            {
                return ("");
            }
        }

        protected void executeSQL(String esText)
        {
            SqlConnection esConn = new
SqlConnection(dbConn.ConnectionString + "password=[password];");
            SqlCommand esCmd = new SqlCommand(esText, esConn);
            esConn.Open();
            esCmd.ExecuteNonQuery();
            esCmd.Dispose();
            esConn.Close();
            esConn.Dispose();
        }

        // Eliminates all embedded spaces more than one
        protected String normalizeSpace(String nsText)
        {
            String workText = nsText;

            while (workText.IndexOf("  ") >= 0)
            {
                workText = workText.Replace("  ", " ");
            }
            return (workText);
        }

        // Returns "true" if the text passed is an element in CSCS
        protected bool isElement(String ieText)
        {
            Boolean itExists = false;

            SqlCommand ieCmd = new SqlCommand("SELECT Actv_Ind FROM
Active_Elements "
                + " WHERE Element_ID = '" + ieText + "'", dbConn);
            SqlDataReader ieDR = ieCmd.ExecuteReader();
            if (ieDR.HasRows)
            {
                itExists = true;
            }
            ieDR.Close();
            ieDR.Dispose();
            ieCmd.Dispose();

            return (itExists);
        }



        // Returns "true" if the words passed has symbols in it
        protected bool hasSymbols(String hsText)
        {
            if ((hsText.IndexOf("(") >= 0) || (hsText.IndexOf(")") >=
0)
                || (hsText.IndexOf("\"") >= 0) || (hsText.IndexOf("'")
>= 0)
                || (hsText.IndexOf("_") >= 0))
            {
                return (true);
            }
            else
            {
                return (false);
            }
        }

    }

}
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-04T19:42:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<446be$45c68b84$454920f8$5139@KNOLOGY.NET>`
- **In-Reply-To:** `<1170630207.802313.39030@l53g2000cwa.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com>`

```
andrewmcdonagh wrote:
> 
> 1) Create a new Interface called 'KeywordDictionary'
…[9 more quoted lines elided]…
> 'ictText' became  'keyword'

I like!  I had been doing some working with namespaces and the like - I 
took what you did, and some research prompted by Pete's comment about 
the Dictionary class, and twisted it a bit.  There is a List<T> class as 
well, which doesn't require key/value combinations, and has a "Contains" 
method.  This is what it looks like now...

-8<--

using System;
using System.Collections.Generic;
using System.Text;

namespace CSCS.Util
{
     class CobolKeywordDictionary : KeywordDictionary
     {
         // This is loaded with the keywords from the below table
         private List<String> cobolKeywords = new List<String>();

         // A list of COBOL keywords
         private String[] keywords =
         {   [oh yeah]
         };

         public CobolKeywordDictionary()
         {
             for (int i = 0; i < keywords.Length; i++)
             {
                 cobolKeywords.Add(keywords[i]);
             }

         }
         public bool isKeyword(String keyword)
         {
             return cobolKeywords.Contains(keyword.ToUpper());
         }
     }
}

->8--

I could still have the keywords in a separate XML file - but with the 
reluctance of our customers to embrace new technology, that keyword list 
won't be changing anytime soon.

This is really cool stuff!  The intent of this look-up is to keep us 
from hitting the database to determine if the name is a database name. 
However, it just hit me when I was typing this e-mail - I could make 
DataSets from the database tables, convert them to lists, and use the 
list lookups for the cull building!  No repetitive database access!

(You were just the witness to a huge light coming on in my head...  And 
no, it's not just the glare from where I don't have hair there 
anymore...  ;)  )

I had tried to implement the above with a predicate, but it seemed like 
cheating.  Since I can't pass a parameter to the predicate method, I had 
created a private String that I set to the keyword, then used the 
StartsWith method on that string.  My problem with that, though, is that 
"ACC" came back as true, since "ACCEPT" starts with "ACC".  I was going 
to put a second check in there, using EndsWith, and then I said to 
myself, this needs a "Contains" method or something.  :)  Looks like I 
wasn't alone.

And - your inteface - I could come up with something like

NetworkRecordKeywordDictionary : KeywordDictionary
NetworkItemKeywordDictionary : KeywordDictionary
RelationalTableKeywordDictionary : KeywordDictionary
RelationalItemKeywordDictionary : KeywordDictionary

I actually *will* use a dictionary on the relational items, as I'll have 
a proc data name (ex. R119-Home-ELC) that references an actual database 
name (HOME_ELC in the HOME_USER table).  I may have to add another 
method to the interface for those, or change the return type - of 
course, I guess at that point it's not really using the 
KeywordDictionary interface.  :)

Man - I'm excited.  :)  I really wish that there was a generic way to 
code, though, that didn't have to know about what sort of database 
backend you have.  SqlDataAdapter is the DataAdapter for SQL Server, 
while OdbcDataAdapter is the one for ODBC.  If I could "genericise" (is 
that a word?) those in the code, and just have it use whatever type of 
connection I passed to it, I could actually run this against a copy of 
the SQL Server database on my laptop (in MySQL or Access or something 
else).  (And yes, I know I could just code it with ODBC, but I don't 
want it to run generically in production when there are libraries 
specifically enhanced for it.)

> So, you might ask 'why the interface?'  good question!
> 
…[14 more quoted lines elided]…
> it (CodeStatistics in our case).

That's great.  :)  I appreciate the list of steps you took in 
refactoring the code, too - I haven't commented about the process much 
because I so excited about the results, but I wanted you to know that I 
did read it, and understand why you did what you did.

Thanks again for a great post, and lots of help!  :)  Before you know 
it, I'll be able to put C# on my resume!  (Not that they look at resumes 
in the military...)
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 6)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-05T12:58:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170709103.296774.93650@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<446be$45c68b84$454920f8$5139@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET>`

```
On Feb 5, 1:42 am, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
>

snipped

>
> I like!  I had been doing some working with namespaces and the like - I
…[39 more quoted lines elided]…
> ->8--


Thats ok, but the performance is going to suffer.

Every time you create an instance of this class, its going to:

1) Create a Array of the string literals
2) Copy that array one by one into a List

Then everytime you call 'isKeyword()' on your class, it asks the List
if it contains the keyword.  Which basically is going to loop through
its internal data structure, one at a time until it find the keyword
or finishes not finding it..



Where as......


using System;
using System.Collections.Generic;
using System.Text;

namespace CodeStats
{
    class FastCobolKeywordDictionary : KeywordDictionary
    {
        static Dictionary<String, String> keywords = new
Dictionary<string,string>();

        // Static Constructor - means it will be called
        // once and only once, sometime between when the
        // program begins and the class is instantiated.

        static FastCobolKeywordDictionary()
        {
            //...
            keywords.Add("AUTHOR", null);
            keywords.Add("BEFORE", null);
            keywords.Add("BINARY-1", null);
            // ....

        }

        public bool isKeyword(String keyword)
        {
            return keywords.ContainsKey(keyword);
        }

    }
}

This class has a 'static constructor', which is called once and only
once by the runtime system for you, at some point between the program
starting and the first usage  of the class.

Plus, when 'isKeyword()' is called, it asks the Dictionary if it
contains the keyword, which does a super fast lookup, which out
looping through the entire collection.

Dictionarys (And Hashtables) internally separate their contents into
buckets based upon the hashcode of the Key. So when asked
'ContainsKey(...) they only need to look in the relevant (small)
bucket for a match, instead of the entire collection.






>
> I could still have the keywords in a separate XML file - but with the
> reluctance of our customers to embrace new technology, that keyword list
> won't be changing anytime soon.

Sure and personally I wouldn't bother, it doesn't strike me like
something that would change very often.

>
> This is really cool stuff!  The intent of this look-up is to keep us
…[8 more quoted lines elided]…
>

oh ok...be care, this caching technique is widely know and so are its
problems.

e.g. when are updates applied to cache,
concurrency issues
etc...

> I had tried to implement the above with a predicate, but it seemed like
> cheating.  Since I can't pass a parameter to the predicate method, I had
…[6 more quoted lines elided]…
>

Yes best to just use '==' as this checks the string values rather than
their references.

> And - your inteface - I could come up with something like
>
…[10 more quoted lines elided]…
> KeywordDictionary interface.  :)

note sure I follow you here...

The interface is there to generalise the method, so if you change it
to specialise again, then you code will need to

  if (cobol)
      return cobolKeywordDictionary.isKeyword(something);
  else
      return someOtherKeywordDictionary.isKeyword(Someting,
andSomethingElse);

always try to 'push' the knowledge of which one to call, to the other
class (Our keyword dictionaries in this case), that way we can simply

  someDictionary.isKeyword(something);


>
> Man - I'm excited.  :)  I really wish that there was a generic way to
…[9 more quoted lines elided]…
>

And that is a great technique - One I'd endorse.... which a twist...as
above. push the knowledge of the Connection to the data source class
itself, or pass it when you create an instance of the class.

I tend to always abstract the data reading/writing behind a general
purpose 'plain old c# ' interface, and let the implementors of that
interface decide how/where to  get their data from.

e.g.


   interface LineCountReporter
   {
       void WriteTotalLineCount(String sourceFilename, int32
lineCount);
   }


   class MySqlLineCountReporter : LineCountReporter
   {

       public MySqlLineCountReporter
       {
          dbConnection =  //  set the dbConnection here...
       }

       // provide the connection at object creation time only.
       public MySqlLineCountReporter(Connection connection)
       {
          dbConnection =  connection
       }
       public void WriteTotalLineCount(String sourceFilename, int32
lineCount)
       {

            // use MySql database code to write to a table.
       }
   }



>
>
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-05T22:11:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YXNxh.129392$5l2.119463@fe02.news.easynews.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com>`

```
Just to "tie in" with my OO COBOL "collection classes" thread.

If anyone understands the OO COBOL specification AND this thread, am I correct 
that *IF* one were doing this in COBOL that using the FACTORY Working-Storage 
would "solve" the problem that Andrew mentions about,

" Thats ok, but the performance is going to suffer.

 Every time you create an instance of this class, its going to: ..."

It is my understanding (limited as it is) that this is the point of (COBOL) 
"factory" data (as opposed to method data).
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-06T14:30:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52q41vF1pcjb4U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <YXNxh.129392$5l2.119463@fe02.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:YXNxh.129392$5l2.119463@fe02.news.easynews.com...
> Just to "tie in" with my OO COBOL "collection classes" thread.
>
…[6 more quoted lines elided]…
> Every time you create an instance of this class, its going to: ..."

Yes. That is correct. The factory can be used as Static (one time) storage. 
You can also declare stuff in there as a PUBLIC PROPERTY (implicit GLOBAL 
with GET SET methods generated by COBOL.) I have code that does this in OO 
COBOL. The problem is that if you want to use these properties with DotNET 
in C# (for example), you can't. The Interop services don't handle Factory 
properties. (I don't know whether they handle Factory Methods, but I expect 
they don't...) I'm looking for a better solution for this currently; 
meantime, I have to pass what was a factory property to each of the Class 
Methods. (Once the method has it, it can store and retrieve it in the 
Factory definition and this works OK...)

>
> It is my understanding (limited as it is) that this is the point of 
> (COBOL) "factory" data (as opposed to method data).

No. Factory seems to be very misunderstood in OO COBOL.  What you mention is 
ONE of the points for using Factory, there are others. (For instance (oops, 
sorry, unconscious pun...:-)), you can use Factory Methods to do common 
support functions that are required by a number of Methods, but which you 
don't want instantiated every time a Method is instantiated. You can use 
Factory to hold GLOBAL non-instance variables (like a count of the number of 
objects currently generated, running control totals across all instances, 
limited only by your imagination :-). It isn't just about static storage.

Pete.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-05T20:45:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET>`
- **In-Reply-To:** `<1170709103.296774.93650@q2g2000cwa.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com>`

```
andrewmcdonagh wrote:
> On Feb 5, 1:42 am, LX-i <lxi0...@netscape.net> wrote:
>> andrewmcdonagh wrote:
>>
> 
> snipped

Ouch!  ;)

>>          // This is loaded with the keywords from the below table
>>          private List<String> cobolKeywords = new List<String>();
…[62 more quoted lines elided]…
> bucket for a match, instead of the entire collection.

Ah...  I shied away from that because I thought, "I don't need a 
key-value pair - just the value."  Would it still be acceptably 
efficient to do the Add()s off the array defined in the constructor?  I 
could convert it to hard-coded Add()s, that would be easy enough.

Also, regarding the above - would there be anything wrong with making 
isKeyword() a static method as well?  Then, you wouldn't actually have 
to create an object - you could just say something like

if (FastCobolKeywordDictionary.isKeyword(words[i])) {
     // do something really cool
}

I did that today with the NormalizeSpace method - I created a class 
called CSCSFuncs (as plain Funcs was already taken), and made 
NormalizeSpace() a class method.

(As a *way* aside, I found out that my web host, for $1 more a month, 
offers ASP.NET with SQL Server 2005.  I'm really tempted to cough up the 
extra $12 to start working with some of my websites with this.  Plus, 
the plan still include PHP and MySQL, so my current stuff should 
continue to work as-is.  That way, I'd be able to get more experience in 
the environment.)

>> This is really cool stuff!  The intent of this look-up is to keep us
>> from hitting the database to determine if the name is a database name.
…[10 more quoted lines elided]…
> problems.

These wouldn't updateable.  Basically, I've got to look at every word in 
a COBOL program to see if it's a database name.  By excluding keywords, 
I would not have to "hit the database" for those, which reduces my 
database access time.  Ditto for words with symbols.  All I'm doing is 
looking to see if that word is in the database of "database words".  If 
it is, I determine how it's being used (we track used vs. updated, 
although it's kind of weak because an update of the group level item 
updates all the elementary items; I think that the existing retrieval 
walks up the hierarchy if you ask it to), then update the count.

I may have opportunity to use datasets for the update counts - but, I 
would be AcceptChanges()ing often.  Also, this process runs when a user 
checks in a piece of source code - and, I can say with near certainty 
that two people are going to be checking in the same item at the same 
time!  :)  (If they are, we have other problems...)

(And yes, I know that this is "the original intent" of the code, which 
may be changed over the years...  Maybe straight ExecuteSQL()s would be 
better (wrapped in another class, of course).)

>> And - your inteface - I could come up with something like
>>
…[12 more quoted lines elided]…
> note sure I follow you here...

I'm not sure I followed myself...  :)

> The interface is there to generalise the method, so if you change it
> to specialise again, then you code will need to
…[10 more quoted lines elided]…
>   someDictionary.isKeyword(something);

Unless I return an array...  Hmmm...  [blink]  Man, my power bill is 
going to be sky-high this month!  :)

But yes, I agree - the lookup for the relational items probably wouldn't 
be an isKeyword() call, because I'm not implementing the interface if I 
make an isKeyword() method that doesn't return a "bool" value, right?

>> Man - I'm excited.  :)  I really wish that there was a generic way to
>> code, though, that didn't have to know about what sort of database
…[47 more quoted lines elided]…
>    }

I guess I'm not seeing this...  How does this help me run the code on my 
laptop against MySQL, e-mail to work, and run it on our server there 
against SQL Server?  (I don't mean this to sound as harsh as it probably 
does, but I can't think of another way to word the question...  Like I 
said, I'm probably just not connecting the dots.)

Thanks again...  :)  I think I'm going to have to figure out how to use 
Google Groups, because I don't want to lose this newsgroup in a couple 
of weeks when my cable modem is disconnected!
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 8)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-07T07:01:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170860507.619175.248120@a34g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET>`

```
On Feb 6, 2:45 am, LX-i <lxi0...@netscape.net> wrote:

snippetty snip

>
> Ah...  I shied away from that because I thought, "I don't need a
> key-value pair - just the value."  Would it still be acceptably
> efficient to do the Add()s off the array defined in the constructor?  I
> could convert it to hard-coded Add()s, that would be easy enough.

Yes, given that the contents are only loaded once, it might be worth
doing purely from the 'readability point of view.

One thing though....  I would have expected an 'addAll(Object[]) '
method like the Java collections have, so to save you from having to
code it.

>From a Design point of view, this population loop is a Responsability
that does not below with the KeyWordDictionary and so would be best
moved into its own class, with a choice of designs being:

1) Using Inheritence -
   class ExtendedDictionary : Dictionary
   {
       public void addAll(....)
       {
           foreach (entry)
               add( entry, entry);
        }
    }


2 Use Delegation

  class DictionaryFactory
  {

     public Dicitionary createFrom(Object[] elements)
     {
        Dicitionary dictionary = new Dictionary();

        for (int i = 0; i < keywords.Length; i++)
        {
            dictionaryAdd(keywords[i], keywords[i]);
        }

     }
  }
   }

>
> Also, regarding the above - would there be anything wrong with making
…[7 more quoted lines elided]…
>

Wrong...  such a subjective term....

So, as I see it (YMMV) at the very highest level of our design this is
a Procedural approach and we are aiming for an OO one.

With the procedural approach, I can't use polymorphism to determine
which keyworddictionary to use, whereas I can with the OO approach.

Procedural example...

public void makeAnimalSound(Animal animal)
{
   if(animal.getType() == Dog)
   {
       DogNoiseGenerator.bark();
   }
   else if (animal.,getType() == Cat)
   {
      CatNoiseGenerator.meeow();
   }
}

OO Example....(where the noisegenerators are used in a polymorphic
way)

public void makeAnimalSound(Animal animal)
{
    AnimalNoiseGenerator noiseGenerator = dictionary.get
(animal.getType() );
    noiseGenerator.makeNoise();
}



> I did that today with the NormalizeSpace method - I created a class
> called CSCSFuncs (as plain Funcs was already taken), and made
> NormalizeSpace() a class method.
>

Personally I always favour Instance Methods over (static) Class
Methods because of this 'subsitutability' benefit. There is nothing to
be gained from worrying about the memory or cpu usage from creating
one of this objects vs calling a static method.


Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 8)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-07T08:46:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170866774.475993.133730@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET>`

```
On Feb 6, 2:45 am, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
> > On Feb 5, 1:42 am, LX-i <lxi0...@netscape.net> wrote:

> > And that is a great technique - One I'd endorse.... which a twist...as
> > above. push the knowledge of the Connection to the data source class
…[40 more quoted lines elided]…
>

It helps, because depending upon a runtime flag, your application can
use either MySQL or SQL data. accessing classes.

By abstracting 'how' we talk to a db, from the actual talking, we can
use different mechanisms.

So, in your code base, we have the dbUtils class with aset of static
methods.  If we  created an Interface with the same methods on it and
changed the current dbUtils static methods to instance methods (by
deleting the 'static keyword) we can then use polymorphism to decide
which actual db to connect to.

e.g.

interface DbUtils
{
  public void recordLinesOfComments();
  ...

}

class MySqlDbUtils : dbUtils
{


  public void recordLinesOfComments()
   {
     ....
    }

   ....
}


class SqlDbUtils : dbUtils
{


  public void recordLinesOfComments()
   {
     ....
    }

   ....
}



class OracleDbUtils : dbUtils
{


  public void recordLinesOfComments()
   {
     ....
    }

   ....
}


Once you have these set of classes that implement the DB agnostic
interface your application just then needs to decide which one to
create an instance of to use.  This could be done in the apps main
class, using a commandline paramerter, machine name, environment
variable, etc.

This technique is known as 'Inversion of Control'.  Instead of the
control over what implementation to use being hard coded, we invert
that control by making it runtime configurable.

hth

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-07T19:27:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26887$45ca7c91$454920f8$3587@KNOLOGY.NET>`
- **In-Reply-To:** `<1170866774.475993.133730@q2g2000cwa.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com>`

```
andrewmcdonagh wrote:

[snip]
> 
> interface DbUtils
…[50 more quoted lines elided]…
> variable, etc.

So, I've got basically the same thing 4 different times, depending on 
the database I'm hitting.  I don't guess there's any way around that, 
but I do understand the flexibility it gets.  The dots are connected 
now.  :)  And, as I don't think I'm going to finish what I'm trying to 
do here before I leave, this will help me set up the database on my machine.

(And, I should be able to make the other sets of code by replacing 
"SqlConnection" with "OdbcConnection", "SqlDataAdapter" with 
"OdbcDataAdapter", etc.)


> This technique is known as 'Inversion of Control'.  Instead of the
> control over what implementation to use being hard coded, we invert
> that control by making it runtime configurable.

That's definitely what I was looking for.  :)  Thanks again for breaking 
it down for me.

(Did you look at the "second C#" post - and if so, does it look like I'm 
on the right track?)
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 10)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-08T09:04:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170954277.185118.185740@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<26887$45ca7c91$454920f8$3587@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET>`

```
On Feb 8, 1:27 am, LX-i <lxi0...@netscape.net> wrote:

snipped...

> That's definitely what I was looking for.  :)  Thanks again for breaking
> it down for me.

My pleasure...
>
> (Did you look at the "second C#" post - and if so, does it look like I'm
> on the right track?)

I've given it a quick scan but will need to have another look before
commenting.  Might be worth while you  posting an update ...but if we
can keep it in this thread, it will help keep the topic focused and
together.

The one main OO design point that you should eventually spot from
where I'm taking you, is that numerous small classes with a single
responsibility, when working together, can create a very simple but
powerful design, with lots of code reuse.

As a top of head metric, my designs tend to consist of 40% of classes
containing a single method, which is no longer than a dozen lines of
code.  Another 55% would contain at most 6 methods, with the remaining
5% of classes having more than 6 methods.

The 95% classes would having  methods of no more than a dozen lines
and all hold onto the **Single Responsibility Principle. The last 5%
would be 'dodgy' and need refactoring...but then lifes too short and
we do have to actually ship stuff!

Regards

Andrew
**  Single Responsibility Principle - http://www.objectmentor.com/
resources/articles/srp.pdf
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-09T11:56:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<531o4vF1pgouiU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170954277.185118.185740@q2g2000cwa.googlegroups.com...
> On Feb 8, 1:27 am, LX-i <lxi0...@netscape.net> wrote:
>
…[35 more quoted lines elided]…
>

I can't tell you what a relief it was to read these articles :-)

For some time now I have been trying to explain that an OO approach removes 
the need for source code maintenance in the traditional sense. Classes and 
methods should be encapsulated and "do what they do". When change is 
required it should be new interfaces or extensions and NOT an internal 
change to already working code. Apart from the obvious benefit of NOT 
requiring regression testing, this approach also simplifies maintaining 
applications. I came to learn this by working with COM component development 
over a number of  years.

Most people here, coming from a procedural background where the whole point 
of good coding practice is to ensure that source code is easily maintained, 
and one of the reasons for using COBOL in the first place is its 
"self-documenting" nature, simply thought I was crazy.

Write applications then don't change the code? Impossible!

Of course, it isn't impossible and I've been doing it for some years now. I 
see it as one of the most compelling arguments for using OO.

After a number of clumsy attempts to explain myself, I simply gave up... 
It's like trying to explain the concept of "red" to a person who has been 
blind since birth...

I have never studied the computer science covered in these articles, but 
arrived at the same conclusions just by empirical practice.

This is the first tme I have seen some of the things I know innately, 
expressed in a tangible and easily assimilable form. OK, there is a heap of 
new jargon and acronyms, but the pure light of the underlying principles 
shines through like a beacon.

I strongly recommend any COBOL programmer who is labouring under the burden 
of heavy regression testing to at least browse the first article. (I 
especially liked his description of "software rot" and what causes it :-)) 
Here is a direct link:

http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf

For me, the quote of the week is:

"The Open Closed Principle (OCP)

A module should be open for extension but closed for modification.

Of all the principles of object oriented design, this is the most important. 
It originated
from the work of Bertrand Meyer. It means simply this: We should write our 
modules
so that they can be extended, without requiring them to be modified. In 
other
words, we want to be able to change what the modules do, without changing 
the
source code of the modules."

Now, I wish I'd thought of that... :-)

Pete.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 12)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-08T15:19:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170976759.429298.131560@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<531o4vF1pgouiU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net>`

```
On Feb 8, 10:56 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote in message
>
…[100 more quoted lines elided]…
> Pete.



Glad you liked them...  yes for me the OCP and SRP are two of the most
important ones to start out with.

Robert martin (the author) regularly hangs out in comp.object.
(indeed he's having a hard time of it lately with an anti-oo crowd
trying to poke wholes in OO through him).

Do note though...that these principles whilst very easy to use and
design in an OO language, can also work in some procedural languages,
especially C. For years now, Unix and Window's worlds have been using
Libraries as part of applications (think DLLs).  These libraries are
loaded at runtime and are called via generic references (pointers to
functions typically).  This allowed us to create version 1.0 of our
app, ship it and move on. Then later when a bug was found, we could
just ship a new library instead of the whole app.

Two other principles I keep in my bag of tricks are:

1) 'Favour delegation over inheritance'
   People tend to use inheritance for code reuse instead of modelling
a relationship between two classes.
   Take a look at one of my latest posts to Daniel which shows how he
could move the population of a Hashtable into its own class.
   Using delegation, its basically allows for a relationship between
two classes to be Dynamic(made at runtime)  instead of Inheritance,
which is static(made at compile time)

2) Favour polymorphism over type checking.
    I see a lot of people write code that asks an object for its type
and then do something specific for that type.  This approach whilst
useful for a very small limited number of areas (Abstract Factories
are the main), quickly leads  to a brittle (low cohesive and tightly
coupled) design.

Regards

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-09T13:12:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<531silF1qandcU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <1170976759.429298.131560@v33g2000cwv.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170976759.429298.131560@v33g2000cwv.googlegroups.com...

<snipped>
>> > **  Single Responsibility Principle -http://www.objectmentor.com/
>> > resources/articles/srp.pdf
…[83 more quoted lines elided]…
> especially C.

Yes, the ideas can also be applied to COBOL design, that's why I encouraged 
people here to read them. Nevertheless, the fact remains it is EASIER to 
implement these ideas in a framework which is designed to support them. 
Hence OO...


> For years now, Unix and Window's worlds have been using
> Libraries as part of applications (think DLLs).  These libraries are
…[4 more quoted lines elided]…
>

Yes. Exactly how COM components work. It is the detached and stable 
interface wrapping that allows this to work, using the principles outlined 
in the articles.

I have been extolling the virtues of component based development here for 
some years now. The idea of building systems from "LEGO" blocks (read .dlls) 
definitely works for me. Finding recently that I can still reuse these 
components in a DotNET environment with C# has been a major factor in 
deciding to move away from COBOL. Unmanaged code allows me to leverage my 
investment in these components while I gradually move to a fully managed 
scenario.

> Two other principles I keep in my bag of tricks are:
>
> 1) 'Favour delegation over inheritance'
>   People tend to use inheritance for code reuse instead of modelling
> a relationship between two classes.

I can't remember the last time I explicitly used inheritance. In Java, 
EXTENDS makes it easy and is useful, but in C# the inheritance tends to be 
more implicit. I have only got onto delegation fairly recently and am still 
understanding it. I knew Java events used a delegation model but never 
really understood what it implied. Since learning C# I have a much better 
grasp of it, but it is still early days for me. I can see your point and 
will keep this in mind.

>   Take a look at one of my latest posts to Daniel which shows how he
> could move the population of a Hashtable into its own class.
>   Using delegation, its basically allows for a relationship between
> two classes to be Dynamic(made at runtime)  instead of Inheritance,
> which is static(made at compile time)

I did see that and agree it is a better approach.

>
> 2) Favour polymorphism over type checking.
…[5 more quoted lines elided]…
>

Hmmm... hadn't thought about that. In C# you HAVE to be careful with typing 
or the code won't compile. I don't think this precludes an abstract approach 
though. I have some reservations about polymorphism (unless it is achieved 
via separate interfaces). I don't like passing parameters to methods; I 
prefer to get and set properties, then simply invoke the method without 
parameters. This keeps a more simple external interface, but I'm grrdually 
bending this as I understand more about polymorphism. It isn't a rule; more 
of a guideline... :-)

Andrew, thanks again for the great posts you have been making and for 
sharing your in depth experience here. I've certainly learned from them and 
I'm sure others have too.

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-09T03:41:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C3Syh.189491$jd2.135823@fe09.news.easynews.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net>`

```
WithOUT getting into the whole procedural vs OO debate,  the recent posts in 
this thread really DO remind me of "highly-modularized" procedural code that was 
becoming semi-common in the late 80's and 90's (before COBOL lost its 
"glitter").  In several IBM mainframe shops (which is what I knew best in those 
days), the use of dynamic CALL statements with sub-programs with procedure 
division  that "could print on a single page of laser paper" gained a certain 
(good and bad) reputation.  OBVIOUSLY, the same goal of "encapsulating" logic 
(and reuse of existing logic) was behind this.

It may or may not have anything to do with why OO hasn't caught on with IBM 
mainframers, but the "highly-modularized" approach turned out to be a VERY bad 
decision for some shops that were early implementors of IBM's LE (and, yes, I 
still think it is similar to .NET CLR).  In early IBM LE environments, the 
overhead for doing "dynamic CALL" statements in COBOL was HORRENDOUS (especially 
between old and new programs).  Therefore, these "highly modularized" 
applications came to screaming halts in actual mainframe production 
environments.  No change to code, just to run-times. (FYI, this has improved in 
recent years.  See LE "XPLINK" for example)

This may (or may not) have anything to do with why mainframers are "hesitant" to 
move to many classes with small method applications.

(Just my $.02)
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-10T02:34:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<533bj7F1r5ruaU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:C3Syh.189491$jd2.135823@fe09.news.easynews.com...
> WithOUT getting into the whole procedural vs OO debate,  the recent posts 
> in this thread really DO remind me of "highly-modularized" procedural code 
…[20 more quoted lines elided]…
> (Just my $.02)

As you say, this is speculation. I didn't know that LE caused performance 
problems with DYNAMIC calls and am astonished to hear it. It was common 
practice on a number of European mainframe sites where I worked, to design 
COBOL systems this way because of the flexibility and ease of maintenance; I 
can't believe IBM were unaware of this and allowed LE to perform badly in 
this area. (I DO believe it because you said it.)

As for such an experience causing hesitancy in moving to OO, I seriously 
doubt it.

<broken record> MODULAR programming is NOT OO </broken record>... there are 
some similarities, but there are differences also. The differences are 
subtle, yet extremely important.

To decide that a bad experience with Modular programming presages a bad 
experience with OO is like deciding that if the Christmas pudding is burned, 
the tree will catch fire.

Pete.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 14)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-09T12:59:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12spdp4n9or4i9a@corp.supernews.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <533bj7F1r5ruaU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:533bj7F1r5ruaU1@mid.individual.net...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
> news:C3Syh.189491$jd2.135823@fe09.news.easynews.com...
> > WithOUT getting into the whole procedural vs OO debate,  the recent
posts
> > in this thread really DO remind me of "highly-modularized" procedural
code
> > that was becoming semi-common in the late 80's and 90's (before COBOL
lost
> > its "glitter").  In several IBM mainframe shops (which is what I knew
best
> > in those days), the use of dynamic CALL statements with sub-programs
with
> > procedure division  that "could print on a single page of laser paper"
> > gained a certain (good and bad) reputation.  OBVIOUSLY, the same goal of
…[3 more quoted lines elided]…
> > IBM mainframers, but the "highly-modularized" approach turned out to be
a
> > VERY bad decision for some shops that were early implementors of IBM's
LE
> > (and, yes, I still think it is similar to .NET CLR).  In early IBM LE
> > environments, the overhead for doing "dynamic CALL" statements in COBOL
> > was HORRENDOUS (especially between old and new programs).  Therefore,
> > these "highly modularized" applications came to screaming halts in
actual
> > mainframe production environments.  No change to code, just to
run-times.
> > (FYI, this has improved in recent years.  See LE "XPLINK" for example)
> >
…[8 more quoted lines elided]…
> COBOL systems this way because of the flexibility and ease of maintenance;
I
> can't believe IBM were unaware of this and allowed LE to perform badly in
> this area. (I DO believe it because you said it.)
…[4 more quoted lines elided]…
> <broken record> MODULAR programming is NOT OO </broken record>... there
are
> some similarities, but there are differences also. The differences are
> subtle, yet extremely important.

First, Mr Klein did not use the term "modular programming".

Second, "modular programming" may refer to something
specific (historically) or something generic (more recently).
Mr Klein's use ("highly-modularized") suggests generic.

Third, your use of "OO" is unclear. "OO" is used often
as an adjective, not as a noun and, as a noun, it is synonymous
with object-oriented design; thus, I am unable to determine
whether you intended the word "programming" as the noun
that "OO" modifies (MP is not OOP) or, if you intended
"design" (MP is not OOD).

Generically, modular programming includes all means for
decomposing computer programming problems into modules
(more easily manageable pieces of data and code); except,
procedural decomposition, which does not separate data.

Thus, structured design, functional decomposition, types
(user-defined and abstract data), object-oriented design, etc.,
are, generically, types of modular programming.

Not all modular programming is object-oriented design; but
all object-oriented design is modular programming ... at least
generically!
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-10T11:22:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<534aglF1qc54mU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <533bj7F1r5ruaU1@mid.individual.net> <12spdp4n9or4i9a@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:12spdp4n9or4i9a@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[56 more quoted lines elided]…
> First, Mr Klein did not use the term "modular programming".

CLARIFICATION for those who live in a world of rigid definitions...(Great 
idf you want to have pedantic debates, not so good if you just want to 
discuss opinions.)

1. I was using Modular in the generic sense, as I believe that was what Bill 
intended in his post..

2. OO was intended as "Object Orientation" and, as such, covers OOD and OOP
>
> Second, "modular programming" may refer to something
> specific (historically) or something generic (more recently).
> Mr Klein's use ("highly-modularized") suggests generic.

So you agree he intended generic. Why would you then not take my response as 
generic?
>
> Third, your use of "OO" is unclear. "OO" is used often
…[4 more quoted lines elided]…
> "design" (MP is not OOD).

Hopefully the above clarifies this.
>
> Generically, modular programming includes all means for
> decomposing computer programming problems into modules
> (more easily manageable pieces of data and code); except,
> procedural decomposition, which does not separate data.

Well that's your definition. I don't disagree, but it really doesn't matter 
in the context of this particular discussion.
>
> Thus, structured design, functional decomposition, types
…[5 more quoted lines elided]…
> generically!


The point I was making was that I'm heartily sick of hearing people say that 
OO is a re-invention of modular programming. It isn't and, having used both 
for considerable periods of my life, I recognise the differences.

That's really all I have to say on this.

Pete.


>
>
>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 16)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-09T20:26:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12sq80557ce9sef@corp.supernews.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <533bj7F1r5ruaU1@mid.individual.net> <12spdp4n9or4i9a@corp.supernews.com> <534aglF1qc54mU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:534aglF1qc54mU1@mid.individual.net...
[snip]
> The point I was making was that I'm heartily sick of hearing people say
that
> OO is a re-invention of modular programming. It isn't and, having used
both
> for considerable periods of my life, I recognise the differences.

When you said as much recently, I found no reason
to object. I completely missed that point, this time,
and still don't see it. <g>

> That's really all I have to say on this.

Your choice! <g>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-12T07:55:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8nv0t297tmc6t3p6vk8tgun6lncm8g9060@4ax.com>`
- **References:** `<1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <533bj7F1r5ruaU1@mid.individual.net> <12spdp4n9or4i9a@corp.supernews.com> <534aglF1qc54mU1@mid.individual.net>`

```
On Sat, 10 Feb 2007 11:22:11 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>The point I was making was that I'm heartily sick of hearing people say that 
>OO is a re-invention of modular programming. It isn't and, having used both 
>for considerable periods of my life, I recognise the differences.

It isn't a re-invention of modular programming.   But it is modular,
and it is programming. 

And in a world where people use "database" to mean just about
anything, we need to specify when we want to exclude the more general
definitions if we expect good communications.   --- even in a
programming news group, where "general" excludes non programmers.

This happens all over, not just in data processing.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 17)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-12T14:06:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12t1etphplr7v55@corp.supernews.com>`
- **References:** `<1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <533bj7F1r5ruaU1@mid.individual.net> <12spdp4n9or4i9a@corp.supernews.com> <534aglF1qc54mU1@mid.individual.net> <8nv0t297tmc6t3p6vk8tgun6lncm8g9060@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:8nv0t297tmc6t3p6vk8tgun6lncm8g9060@4ax.com...
> On Sat, 10 Feb 2007 11:22:11 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
>
> >The point I was making was that I'm heartily sick of hearing people say
that
> >OO is a re-invention of modular programming. It isn't and, having used
both
> >for considerable periods of my life, I recognise the differences.
>
> It isn't a re-invention of modular programming.   But it is modular,
> and it is programming.

Modular programming is not programming. It is, generically,
any design method (for partitioning the programming task
into modules) implemented by means of programming.
Design is not programming!

The first use of "modular programming" dates from 1968
and appears to have included only those methods that
were lumped into "functional decomposition". About 1974,
modular programming included "structured design", which
used a different notation to present the design. By the
early-1980s, the definition expanded to include all methods
for "data-hiding".

Thus, OO is not a re-invention of modular programming.
It is modular programming!

OO extends modular programming in the same sense that
"radial tires" extends "tires", which previously included
"solid rubber tires", "bias-ply tires", etc.; or "jet aircraft"
extends "aircraft", which previously included
"propeller-driven aircraft", "gliders", "helicopters", etc.

The hesitancy that some appear to have for including
OO in modular programming may result from the belief
"OO is so much better than previous methods that it
does not deserve to be in the same class".

So make certain that your child's tricycle and your
wheelbarrow are equipped with radial tires--they are
so much better! <g>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 13)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-09T11:27:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<533so5F1qja4bU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com>`

```
William M. Klein<wmklein@nospam.netcom.com> 02/08/07 8:41 PM >>>
>WithOUT getting into the whole procedural vs OO debate,  the recent posts
in 
>this thread really DO remind me of "highly-modularized" procedural code
that was 
>becoming semi-common in the late 80's and 90's (before COBOL lost its 
>"glitter").  In several IBM mainframe shops (which is what I knew best in
those 
>days), the use of dynamic CALL statements with sub-programs with procedure

>division  that "could print on a single page of laser paper" gained a
certain 
>(good and bad) reputation.  OBVIOUSLY, the same goal of "encapsulating"
logic 
>(and reuse of existing logic) was behind this.
>
>It may or may not have anything to do with why OO hasn't caught on with IBM

>mainframers, but the "highly-modularized" approach turned out to be a VERY
bad 
>decision for some shops that were early implementors of IBM's LE (and, yes,
I 
>still think it is similar to .NET CLR).  In early IBM LE environments, the

>overhead for doing "dynamic CALL" statements in COBOL was HORRENDOUS
(especially 
>between old and new programs).  Therefore, these "highly modularized" 
>applications came to screaming halts in actual mainframe production 
>environments.  No change to code, just to run-times. (FYI, this has
improved in 
>recent years.  See LE "XPLINK" for example)
>
>This may (or may not) have anything to do with why mainframers are
"hesitant" to 
>move to many classes with small method applications.
>
>(Just my $.02)

I am still a fan of 'shared subroutines', though with some caveats. 
Performance is not one of them, though.  I've never done any empirical
testing, but I've never noticed much in the way of performance degradation
when using them.

In any case, my biggest problem with using them is lack of flexibility when
"extending" them.  Let me give a real world example...

We have a subroutine called TXND.  It's goal is to take in "transaction
data" from a database and return a formatted transaction description.

 01  TXND-SUBROUTINE                  PIC X(8)  VALUE 'TXND'.   
 01  TXND-LINKAGE-AREA.                                         
                                                                
     05 TXND-PASSED-DATA.                                       
        10  TXND-CALLER-ID            PIC X(8).                 
        10  TXND-CURRENT-SUBROUTINE   PIC X(12).                
        10  TXND-COMPRESS-LINE-SW     PIC X.                    
            88  TXND-COMPRESS-LINES             VALUE  'Y'.     
        10  TXND-1LOC-DESC-SW         PIC X.                    
            88  1LOC-DESC-WANTED                VALUE  'Y'.     
        10  TXND-MSTR-SEGMENT         PIC X(1500).              
        10  TXND-TRAN-SEGMENT         PIC X(50).                
        10  TXND-DESC-SEGMENT         PIC X(55).                
                                                                
     05 TXND-RETURNED-DATA.                                     
        10  TXND-SHORT-DESC           PIC X(10).                
        10  TXND-LONG-DESC-1          PIC X(75).                
        10  TXND-LONG-DESC-2          PIC X(75).           
        10  TXND-LONG-DESC-3          PIC X(75).           
        10  TXND-SHORT-DESC-NUM       PIC 9(9).            
        10  TXND-CONVERTED-CHECK-SW   PIC X.               
            88  TXND-CONVERTED-CHECK            VALUE  'Y'.
        10  TXND-ICM-TRAN-TYPE        PIC X(10).           
        10  FILLER                    PIC X(50).           


PROCEDURE DIVISION.
*   after retreiving the "master segment", a "transaction segment" and a
"transaction 'description' segment" from the database.
*   (the transaction description segment is really just an extension of the
transaction segment with additional information that is needed for some, but
not all, transactions)
     MOVE DMDMSTR                   TO TXND-MSTR-SEGMENT      
     MOVE DMDTRAN                   TO TXND-TRAN-SEGMENT      
     MOVE TRANS-DESCRIPTION-SEGMENT TO TXND-DESC-SEGMENT      
     MOVE 'CICSDD11'                TO TXND-CALLER-ID         
     MOVE 'N'                       TO TXND-COMPRESS-LINE-SW  
     MOVE 'N'                       TO TXND-CONVERTED-CHECK-SW
     CALL TXND-SUBROUTINE USING TXND-LINKAGE-AREA             

Originally when this subroutine was designed the 05 level TXND-RETURNED-DATA
did not include the TXND-CONVERTED-CHECK-SW and TXND-ICM-TRAN-TYPE fields. 
When these were added later it required a recompile of every program that
called this subroutine, even if those programs did not care about the new
fields.

Obviously this is the reason for the now 50 bytes of filler.  But of course
50 bytes is just a wild guess as to what may be needed in the future.

With OO it's much more dynamic, in that the invoked class creates the
storage, rather than the invoking program, so there is (I believe!) no need
for silly things like filler in anticipation of future needs.

Now I didn't write the TXND routine, but I imagine that if I were to rewrite
it I might do something like this...

***BEGIN TXNDLINK COPYBOOK***
 01 TXND-PASSED-DATA.                                       
    05  TXND-PASSED-DATA-LEN      COMP PIC S9(4).
    05  TXND-CALLER-ID            PIC X(8).                 
    05  TXND-CURRENT-SUBROUTINE   PIC X(12).                
    05  TXND-COMPRESS-LINE-SW     PIC X.                    
        88  TXND-COMPRESS-LINES             VALUE  'Y'.     
    05  TXND-1LOC-DESC-SW         PIC X.                    
        88  1LOC-DESC-WANTED                VALUE  'Y'.     
    05  TXND-MSTR-SEGMENT         PIC X(1500).              
    05  TXND-TRAN-SEGMENT         PIC X(50).                
    05  TXND-DESC-SEGMENT         PIC X(55).                
                                                            
 01 TXND-RETURNED-DATA.                                     
    05  TXND-RETURNED-DATA-LEN    COMP PIC S9(4).
    05  TXND-SHORT-DESC           PIC X(10).                
    05  TXND-LONG-DESC-1          PIC X(75).                
    05  TXND-LONG-DESC-2          PIC X(75).           
    05  TXND-LONG-DESC-3          PIC X(75).           
    05  TXND-SHORT-DESC-NUM       PIC 9(9).            
    05  TXND-CONVERTED-CHECK-SW   PIC X.               
        88  TXND-CONVERTED-CHECK            VALUE  'Y'.
    05  TXND-ICM-TRAN-TYPE        PIC X(10).           
***END TXNDCOPYBOOK***
---------------------------------------
 WORKING-STORAGE SECTION.
 COPY TXNDLINK.
 PROCEDURE DIVISION.

     MOVE LENGTH OF TXND-PASSED-DATA TO TXND-PASSED-DATA-LEN
     MOVE LENGTH OF TXND-RETURNED-DATA TO TXND-RETURNED-DATA-LEN
     CALL TXND-SUBROUTINE USING TXND-PASSED-DATA
                                TXND-RETURNED-DATA

TXND itself would look something like this:

 PROGRAM-ID. TXND.
 WORKING-STORAGE SECTION.
 COPY TXNDLINK.
 LINKAGE SECTION.
 01  PASSED-DATA.
     05  PASSED-DATA-LEN               COMP PIC S9(4).
     05  PASSED-DATA-AREA.
         10                            PIC X OCCURS 1 TO 9999
                                       DEPENDING ON PASSED-DATA-LEN.
 01  RETURNED-DATA.
     05  RETURNED-DATA-LEN             COMP PIC S9(4).
     05  RETURNED-DATA-AREA.
         10                            PIC X OCCURS 1 TO 9999
                                       DEPENDING ON RETURNED-DATA-LEN.

 PROCEDURE DIVISION USING PASSED-DATA, RETURNED-DATA. 
     MOVE PASSED-DATA TO TXND-PASSED-DATA
     MOVE RETURNED-DATA TO TXND-RETURNED-DATA
     PERFORM MAINLINE
     MOVE TXND-PASSED-DATA TO PASSED-DATA
     MOVE TXND-RETURNED-DATA TO RETURNED-DATA
     EXIT PROGRAM.

 MAINLINE.
*    DO STUFF HERE USING TXND-PASSED-DATA AND SETTING TXND-RETURNED-DATA

END PROGRAM TXND.

I don't like the need for the calling program to set those length fields,
but I guess that's a minor complaint.  If my COBOL supported the ANY LENGTH
phrase I think that would eliminate the need for the LEN fields altogether,
since (I guess) COBOL would implicitly pass the length values.  That would
be very nice!

Of course even this method is not without it's problems.  If a field,
particularly a numeric field, is added to the PASSED-DATA area you would
have to make sure to check that field for valid values prior to utilizing
it, otherwise assume some sort of default.

And then imagine that we want to change the three "LONG-DESC" fields from 75
bytes to 100.  Well, now we're recompiling everything again!  Or adding new
fields to the end.

More than anything, this kind of thing gives me a desire for "object
oriented programming".  The fields in TXND-PASSED-DATA would be input
properties and the fields in TXND-RETURNED-DATA would be output properties.

Anyway, if anyone can see anything wrong with my thoughts about how to 'fix'
my TXND routine without the use of OO COBOL I'd be interested, as I may well
make these changes at some point.  Or at least to something similar for
future subroutines we might develop.

Another thing that would be nice is if COBOL had a way of counting the
number of parameters passed to it.  Actually, I think the OPTIONAL and
OMITTED, were they availible in my COBOL, would work.  Something like the
following:

PROGRAM-ID. MY-SUBR.
PROCEDURE DIVISION USING REQUIRED-FIELD1, REQUIRED-FIELD2, OPTIONAL
OPTIONAL-FIELD1, OPTIONAL OPTIONAL-FIELD2.

IF OPTIONAL-FIELD-1 NOT OMITTED
    MOVE SOMETHING TO OPTIONAL-FIELD1
END-IF

----
* IN CALLING PROGRAM...
CALL 'MY-SUBR' USING FIELD1, FIELD2
CALL 'MY-SUBR' USING FIELD1, FIELD2, FIELD3
CALL 'MY-SUBR' USING FIELD1, FIELD2, OMITTED, FIELD4

But given that this is *not* available, other than passing a field
containing the number of fields passed, is there anything I can do?

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-02-10T00:57:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HL8zh.229$Jl.113@newsread3.news.pas.earthlink.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:C3Syh.189491$jd2.135823@fe09.news.easynews.com...
> WithOUT getting into the whole procedural vs OO debate,  the recent posts 
> in this thread really DO remind me of "highly-modularized" procedural code 
…[24 more quoted lines elided]…
> wmklein <at> ix.netcom.com

<snip>

I just do NOT buy the "highly-modularized approach is bad for performance 
idea". Most performance problems are localized in a very small percentage of 
the code. Without a performance monitoring tool most programmers guess wrong 
about where the bottlenecks are. How many shops let application programmers 
have access to tools like Strobe? In the absence of a monitoring tool, if 
you can roll your own timing routines, then modular code can be an asset in 
locating the slowest parts of code. In my experience if you do know where 
the time is being spent the fact that the code is modularized does not 
usually prevent a programmer from using the many techniques available to 
optimize the code. YMMV.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-10T03:35:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44bzh.214597$8R1.205013@fe04.news.easynews.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <HL8zh.229$Jl.113@newsread3.news.pas.earthlink.net>`

```
I agree that CALL performance is not the most common problem for (IBM mainframe) 
performance, but ever since the days when VS COBOL II first came out, this HAS 
been one place (especially dynamic CALL statement) where IBM has heard lots of 
negative comments from customers.  Recent (about OS/390 1.7 or so) and later 
LE's have had much better performance than earlier versions.  Today, I rarely 
hear of this being a serious problem - but I know it is still something that IBM 
looks at.

For those who haven't looked at the IBM performance guide, you might want to 
check out the section on CALL performance.  Some extracts include,

"When using CALLs, be sure to consider using nested programs when possible. The 
performance of a CALL
to a nested program is faster than an external static CALL; external dynamic 
calls are the slowest. CALL
identifier is slower than dynamic CALL literal."

and

"Performance considerations for using CALLs (measuring CALL overhead only):

    CALL to nested programs was 50% to 60% faster than static CALL.
    Static CALL literal was 45% to 55% faster than dynamic CALL literal.
    Static CALL literal was 60% to 65% faster than dynamic CALL identifier.
    Dynamic CALL literal was 15% to 25% faster than dynamic CALL identifier.

Note: These tests measured only the overhead of the CALL (i.e., the subprogram 
did only a GOBACK);
thus, a full application that does more work in the subprograms may have 
different results."

That last note ties in with Charles' comment as very few programs loop thru CALL 
statements that don't do much.  However, when you do have "highly modularized" 
(in the sense of using COBOL CALL statement), this performance may gain 
visibility.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-10T19:55:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5358j7F1r4bbaU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <HL8zh.229$Jl.113@newsread3.news.pas.earthlink.net> <44bzh.214597$8R1.205013@fe04.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:44bzh.214597$8R1.205013@fe04.news.easynews.com...
>I agree that CALL performance is not the most common problem for (IBM 
>mainframe) performance, but ever since the days when VS COBOL II first came 
…[87 more quoted lines elided]…
>

The point being missed in all of the above is HOW LONG the worst case 
scenario takes. If it is measured in milliseconds, then the percentages are 
only meaningful where thousands of looping dynamic calls are made... not, in 
my experience, a "usual" scenario.

If it is measured in seconds, then there is some cause for concern.

I can honestly say I have never worked on a site where dynamic call overhead 
was even a consideration.

Very surprised to hear that LE degraded it.

Pete.


>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-12T08:10:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h001t25birr710ue2dh3pgermtl0qml0be@4ax.com>`
- **References:** `<446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net> <C3Syh.189491$jd2.135823@fe09.news.easynews.com> <HL8zh.229$Jl.113@newsread3.news.pas.earthlink.net>`

```
On Sat, 10 Feb 2007 00:57:11 GMT, "Charles Hottel"
<chottel@earthlink.net> wrote:

>I just do NOT buy the "highly-modularized approach is bad for performance 
>idea".

And I certainly do not buy "bad for performance" means the same thing
it meant when I started programming four decades ago.    

Within mainframe CoBOL, I see that we have problems when we have
standards that still exist from old performance costs instead of new
performance costs.

CPU time is much cheaper than it was back then, while labor and
opportunity costs are relatively more expensive.   This process will
continue.    A program that is ready today but takes more CPU time can
be more cost effective for its lifetime than a more efficient program
that won't be ready until next month, as it is used this month to make
money for the company.   Of course we generally aren't talking about
40 year program lifetimes here.

>Most performance problems are localized in a very small percentage of 
>the code.

I still believe that some basic performance enhancing of I/O and loop
design is worth-while.   But it isn't as worth-while as it used to be.

========

The U.S. opened up economically with the development of canals to its
interior.   Canals were much more efficient than roads.   But canals
were more expensive to build, and didn't adjust to transportation
needs.   So gradually rail took over, also cheaper than roads.   But
they also weren't flexible, and their initial cost was higher.   While
canals, railroads (and also sea going transport) still exist and do
lots of business - the flexibility of trucks has meant that we don't
have a Montgomery Wards built around a train station shipping out to
your local train station - the goods are in your local mall.

Nowadays, people expect their data on their laptop today - even though
they just decided what they want.   So we optimize our data processing
to give it to them in the most efficient way.   This "most efficient"
means - buy a bigger CPU and more bandwidth - they're cheap.   And set
up procedures that give them secure, accurate data *now*.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 12)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-09T03:45:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171021549.168468.245330@a34g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<531o4vF1pgouiU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net>`

```
On Feb 8, 10:56 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote in message
>
…[81 more quoted lines elided]…
>
....
>
> Pete.

Oh, BTW, this is an extract from Bobs excellent book Agile software
development http://www.amazon.co.uk/Software-Development-Principles-
Patterns-Practices/dp/0135974445/sr=8-14/qid=1171021059/
ref=sr_1_14/202-5327192-4527047?ie=UTF8&s=books
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-09T09:35:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g68ps252vvpv0ciat2ghual6tvs6qaietb@4ax.com>`
- **References:** `<98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <531o4vF1pgouiU1@mid.individual.net>`

```
On Fri, 9 Feb 2007 11:56:29 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>For some time now I have been trying to explain that an OO approach removes 
>the need for source code maintenance in the traditional sense. Classes and 
…[5 more quoted lines elided]…
>over a number of  years.

We've been modifying our granularity of our programs forever.    We
replaced machine language with assembler with compiled.    When our
compiler company changes the code behind the COMPUTE command, we
assume it has been fully tested and do not do regression testing for
all of the programs that have COMPUTE in them.

Well, the granularity is bigger.   If OO is working right, instead of
the COMPUTE command, we now have a Compute object.    The supplied
libraries are bigger and we're more a bit more likely to be bitten
when they change than when the COMPUTE command changes - but we're
still pretty safe.

But we're more likely to be bitten when a CoBOL copy member gets
changed, or a CoBOL called program gets changed.   And we're more
likely to get bitten when a local shop object gets changed.   So lots
of shops avoid using much re-use of our objects.   Complex
environments such as that which Microsoft has to create Windows end up
with bugs within objects.    But we really don't have a choice.   We
are in those complex environments and have to ride the wave.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-08T22:06:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48308$45cbf353$454920f8$14019@KNOLOGY.NET>`
- **In-Reply-To:** `<1170954277.185118.185740@q2g2000cwa.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com>`

```
andrewmcdonagh wrote:
> 
> The one main OO design point that you should eventually spot from
…[12 more quoted lines elided]…
> we do have to actually ship stuff!

heh - true...

> **  Single Responsibility Principle - http://www.objectmentor.com/
> resources/articles/srp.pdf

Thanks for this site - that stuff is great!  I see that I'm still not 
thinking about things quite in an OO manner.  However, the stuff on that 
site is helping.  :)
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 12)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-12T04:19:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171282741.746868.320110@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<48308$45cbf353$454920f8$14019@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET>`

```
On Feb 9, 4:06 am, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
>
…[23 more quoted lines elided]…
>

Daniel,

Can you post the latest version of the code, as I think so long has
passed its not worth me looking at what I think is your current code.

Cheers

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-14T09:50:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET>`
- **In-Reply-To:** `<1171282741.746868.320110@s48g2000cws.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET> <1171282741.746868.320110@s48g2000cws.googlegroups.com>`

```
andrewmcdonagh wrote:
> Daniel,
> 
> Can you post the latest version of the code, as I think so long has
> passed its not worth me looking at what I think is your current code.

It'll be a bit.  As I type packers are putting all my worldly goods into 
boxes.  :)  The "my second C#" post is still the most recent - I've been 
trying to wrap up everything at work and at home (which I'm starting to 
think is an impossibility), so I haven't had too much time to revisit 
that particular code.

(I have changed the DbUtil.cs file to be an interface, and created a 
SqlDbUtil.cs file with the SQL Server implementation.  I am also in the 
process of changing the "string SQL together" methods to use parameters, 
so as to make them not liable to SQL injection attacks.)

Also, I'm also going to try putting Vista on my laptop, as it has a 
64-bit processor and supposedly Vista is good at actually utilizing it. 
  (It'll probably be like "What?  You want more than *half* of me to do 
something?!?!")  Besides, I'm not happy with the way it's partitioned, 
and if I repartition, I'd have to reload the OS anyway...

Once I do that, I'm going to create a fully-functioning version of CSCS 
(the system this code supports) on my machine, and I'll be able to make 
changes and see if they work.  I'll keep you updated here...
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-14T08:59:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rdc6t2t3kma6v5q7ppsau3mvqjrjhi2c0f@4ax.com>`
- **References:** `<446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET> <1171282741.746868.320110@s48g2000cws.googlegroups.com> <2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET>`

```
On Wed, 14 Feb 2007 09:50:10 -0600, LX-i <lxi0007@netscape.net> wrote:

> Besides, I'm not happy with the way it's partitioned, 
>and if I repartition, I'd have to reload the OS anyway...

I've upgraded Partition Magic over the years, but may be finished with
partition changing.

Especially if I go Mac.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 15)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-14T11:43:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2f40d$45d34a40$454920f8$15601@KNOLOGY.NET>`
- **In-Reply-To:** `<rdc6t2t3kma6v5q7ppsau3mvqjrjhi2c0f@4ax.com>`
- **References:** `<446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET> <1171282741.746868.320110@s48g2000cws.googlegroups.com> <2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET> <rdc6t2t3kma6v5q7ppsau3mvqjrjhi2c0f@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 14 Feb 2007 09:50:10 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[6 more quoted lines elided]…
> Especially if I go Mac.

Macs don't use partitions?
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-14T11:20:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ck6t2ha72n7ce5qobkb78ecpa30a788qt@4ax.com>`
- **References:** `<ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET> <1171282741.746868.320110@s48g2000cws.googlegroups.com> <2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET> <rdc6t2t3kma6v5q7ppsau3mvqjrjhi2c0f@4ax.com> <2f40d$45d34a40$454920f8$15601@KNOLOGY.NET>`

```
On Wed, 14 Feb 2007 11:43:31 -0600, LX-i <lxi0007@netscape.net> wrote:

>> I've upgraded Partition Magic over the years, but may be finished with
>> partition changing.
…[3 more quoted lines elided]…
>Macs don't use partitions?

I don't think I can use Partition Magic on a Mac.   It also appears
that the advantage of partitioning is less with a Mac - but it is also
more work than it was worth in the past on a Windows machine. 

But I am still new at Macintoshes.   My wife got hers last month. She
has Parallels which allows her to set up virtual partitions for
different operating systems.

Ever since Windows came out, I have had it on D:, figuring that
separating the OS with programs and data was a good thing.   But it's
harder and harder to do this as more things use the registry.
Upgrading Windows machines has been tough, although I have read that
the Vista upgrade is closer to being a new installation.

I have also had Windows machines with an OS/2 partition, but on a Mac,
I can do that under Parallels (although now I would use Linux
instead).
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 14)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-19T11:23:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1171913019.707494.96310@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <446be$45c68b84$454920f8$5139@KNOLOGY.NET> <1170709103.296774.93650@q2g2000cwa.googlegroups.com> <ae0d3$45c7ebd5$454920f8$13598@KNOLOGY.NET> <1170866774.475993.133730@q2g2000cwa.googlegroups.com> <26887$45ca7c91$454920f8$3587@KNOLOGY.NET> <1170954277.185118.185740@q2g2000cwa.googlegroups.com> <48308$45cbf353$454920f8$14019@KNOLOGY.NET> <1171282741.746868.320110@s48g2000cws.googlegroups.com> <2d5b9$45d32fb0$454920f8$21290@KNOLOGY.NET>`

```
On Feb 14, 3:50 pm, LX-i <lxi0...@netscape.net> wrote:
> andrewmcdonagh wrote:
> > Daniel,
…[4 more quoted lines elided]…
> It'll be a bit.  As I type ...........

>
> (I have changed the DbUtil.cs file to be an interface, and created a
…[3 more quoted lines elided]…
>

I haven't had time to look through the code since your message, so
hopefully you are nearly ready to post a new complete version. (if you
want to...)

In the meantime, here's some (personal) guidelines for helping to see
refactorings to make when faced with a large class......

Its likely that the class is doing more than one job (i.e. has more
than one Responsibility) when...
  1) If there are lots(more than 5) member variables
  2) If there are lots of (more than 5) public methods
  3) If there are lots of (more than 5) private methods
  4) The entire class code contains more than 5 'if' statements (this
includes a Switch with more than 5 'case' statements.
  5) The entire class code contains more than 5 loop statements (For,
While, Do statements).

When ever one or more of these Guidelines are broken, I look for ways
of extracting the related code out into its own class.

A good starting point is to look for relationships between groups of
member variables or methods.

e.g.  a class with AddWidget, EditWidget, DeleteWidget,
ReportWidgetsSold, ReportWidgetsReturned methods could be broken into
a WidgetStore (add, edit, delete) and WidgetReporter classes

So in your codes example, I see a Source code parser, using a number
of small classes that know what to do with an individual piece of
source code (eg Java Comment, Cobol Comment, C# Comment classes, A
Language keyword Dictionary (Java Dict., Cobol Dict. etc) a number of
database CRUD classes for mapping between the OO world and the
Relational DB., etc...

These are guidelines though, not rules...

Regards

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-05T15:33:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52njcdF1pgrekU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com>`

```
Andrew,

I haven't had time to go through this in detail,  but the approach is very 
impressive.

You are demonstrating at a code level some of the most important concepts of 
OO.

Great stuff!

Pete

<snipped to save space>
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 6)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-05T02:28:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170671335.661227.165220@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<52njcdF1pgrekU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <52njcdF1pgrekU1@mid.individual.net>`

```
On Feb 5, 2:33 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Andrew,
>
…[10 more quoted lines elided]…
> <snipped to save space>

Thanks Pete,

If I'd been given the original code as part of work I probably would
have just redesigned the single class into the dozen or so
collaborating classes in one shoot, though still using the
Refactoring, keep it building, approach. But having mentored several
teams over the years I've found a step by step process can help show
not only the why, but also the 'how'.

The only difficulty is finding a level that is not patronsing...as
everyone has different skill levels.

Glad you are enjoying it.

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-02-05T23:52:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZqPxh.19082$pQ3.13224@newsread4.news.pas.earthlink.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <52njcdF1pgrekU1@mid.individual.net> <1170671335.661227.165220@v33g2000cwv.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170671335.661227.165220@v33g2000cwv.googlegroups.com...

<snip>

I just want to say that I am enjoying this thread greatly!

 Andrew your approach to helping Daniel is great also, expecially in a world 
where so many have a first instinct to just be critical. Yor way seems more 
like a caring teacher leading gently in the right direction.

Daniel you are doing very well. Do not worry that the first code you posted 
was called "procedure oriented". You have to crawl befoe you can walk. Don 
Higgins of z390 fame redid his assembler and macro processor from COBOL to 
Java and it looked procedural to me at first, but it still provided a great 
capability with far fewer lines of code than the COBOL version. Since then 
he has added more features and in the process the code looks more and more 
object oriented. With Adrews and others help you are geeting more and more 
real experience with objects.

Thanks to all for an excellent thread!
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 8)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-07T08:26:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170865585.775106.101930@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<ZqPxh.19082$pQ3.13224@newsread4.news.pas.earthlink.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <52njcdF1pgrekU1@mid.individual.net> <1170671335.661227.165220@v33g2000cwv.googlegroups.com> <ZqPxh.19082$pQ3.13224@newsread4.news.pas.earthlink.net>`

```
On Feb 5, 11:52 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
> "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote in message
>
…[19 more quoted lines elided]…
> Thanks to all for an excellent thread!

Thanks Charles,

I find it very tiresome when people are overtly negative.

On the java forums there's numerous 'forum police' whose sole postings
consist of telling people off for
1) Top posting
2) not quoting
3) off topics
4) the colour of their shirts...

My life is to short to worry about these things.

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 9)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-02-09T00:06:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7WOyh.20025$pQ3.7751@newsread4.news.pas.earthlink.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com> <1170291697.002493.111010@h3g2000cwc.googlegroups.com> <98ea6$45c16cb9$454920f8$30045@KNOLOGY.NET> <1170630207.802313.39030@l53g2000cwa.googlegroups.com> <52njcdF1pgrekU1@mid.individual.net> <1170671335.661227.165220@v33g2000cwv.googlegroups.com> <ZqPxh.19082$pQ3.13224@newsread4.news.pas.earthlink.net> <1170865585.775106.101930@j27g2000cwj.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170865585.775106.101930@j27g2000cwj.googlegroups.com...
> On Feb 5, 11:52 pm, "Charles Hottel" <chot...@earthlink.net> wrote:
>> "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote in message
…[45 more quoted lines elided]…
>

Yes I read the java newsgroups and I think it is just futile to try and 
control what other people do. It takes much less energy to just ignore these 
things and then you can invest that energy in things that are more 
interesting.
```

##### ↳ ↳ Re: My First C# (warning - long post)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-01-31T22:27:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd520$45c16c3c$454920f8$30045@KNOLOGY.NET>`
- **In-Reply-To:** `<1170280452.064733.60560@v45g2000cwv.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <1170280452.064733.60560@v45g2000cwv.googlegroups.com>`

```
andrewmcdonagh wrote:
> 
> (Take these comments as good will ones, not character destroying..etc)

of course...  :)

> Ok so a quick scan through tells me that this class....
> 
> Whilst 'doing' one job of analysing the code files, is actually
> several (currently) hidden classes working together. This is backed up
> by the large number of IFs Switch statements, loops and repeated code.

Heh - I really thought I had eliminated repeated code.  (In seeing your 
revisions, I realized I hadn't.)

> The style of coding is more procedural than OO.  This is evident when
> we have large methods, containing multple 'if' blocks or/and 'Switch'
> statements.

I wasn't really pleased with the size of some of the methods, but it 
seemed silly to have 30 methods to do the same thing.  I guess it's not 
after all.

> A general guideline to use for OO methods, is to keep their size to no
> more than 10 lines  (including whitespace, empty lines etc).
…[3 more quoted lines elided]…
> are better moved into a property file or constants.

Are you referring here to the SQL stuff, or the element subtypes?  (The 
subtypes come from a database, and a bunch of other stuff is tied to 
that, so I can't change them.)

> So lets start with the large methods...  within your class there are
> numerous occurrences of code duplication...
…[19 more quoted lines elided]…
> same basic job, just with different data.

I hadn't thought about that.  The other guy in our office has made a 
control that he uses on his ASP.NET web pages, and it has an executeSQL 
method.  :)

> Another useful technique is to change inline comments into the names
> of private methods, and move the code there...

Hmmm...  An interesting thought.  So, maybe I'm thinking OO to a point, 
but not brining the thing full circle?

> Now, the next step is to find the groupings of these methods that
> naturally fit into their own class.
…[9 more quoted lines elided]…
> one Responsibility.

How would I do that?  I've heard that over and over - "separate data 
access from business logic".  I guess I'm asking how I would go about 
it.  Would there be a bunch of methods in there, hiding the datareaders 
with some other iterator?

See if this would be more OO - this would be a second class, one for the 
database stuff.  According to VS, this is syntactically sound...

// This class is responsible for database stuff
public class DBstuff {
     static public SqlConnection newConnection() {
         SqlConnection conn = new SqlConnection();
         conn.ConnectionString = "[whatever]";
         conn.Open();
         return conn;
     }
     static public SqlDataReader newReader(String sql, SqlConnection conn) {
         SqlCommand sc = new SqlCommand(sql);
         return sc.ExecuteReader();
     }
     static public void closeReader(SqlDataReader sdr) {
         sdr.Close();
         sdr.Dispose();
     }
     static public void closeConnection(SqlConnection conn) {
         conn.Close();
         conn.Dispose();
     }
}
// This class is responsible for telling if an item exists
public class ItemExistance : DBstuff {

     ItemExistance() {
     }

     static public bool ItemExists(String element) {
         bool itExists;
         String sql = "SELECT element_id "
             + "FROM active_elements "
             + "WHERE element_id = '" + element + "'";
         SqlConnection myConn = newConnection();
         SqlDataReader dr = newReader(sql, myConn);
         if (dr.HasRows) {
             itExists = true;
         } else {
             itExists = false;
         }
         closeReader(dr);
         closeConnection(myConn);
         return itExists;
     }
}

I'm still not sure how to separate the data readers...  Would the method 
just return a data reader, and the other method could run it as it does 
today?

More to come...
```

#### ↳ Re: [OT] My First C# (warning - long post)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-01T15:58:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52d3ahF1nt1otU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET>`

```
Hi Daniel,

Unfortunately, much as I'd like to, I'm just too busy at the moment to 
analyse this properly.

Fortunately, Andrew is doing so (I had a quick look at his comments and 
endorse them 100%) and one set of criticisms is probably all you need on a 
first attempt :-)

I formed some first impressions from a quick look (before I saw Andrew's 
comments.... :-)) and they were as follows:

1. It is a procedural translation into an OO environment. Even down to the 
"Working-storage" at the top of the Class... :-)

2. You show an excellent grasp of using functions and, at the nitty-gritty 
level you have it sussed. (I think you may be over-using Trim()...
"Convert.ToChar(dr["element_type"].ToString().Trim().Substring(0,1))" seems 
a bit unnecessary to me, when all you are wanting is one byte, but I haven't 
checked the details...:-)

3. The embedded SQL is just a hangover from procedural code; it is 
inefficient and ugly.  Think in tiers; separate data access from business 
logic. Treat db connections as precious; don't hold them any longer than you 
need to. I posted a link previously which outlines the C# approach and it is 
quite different from the procedural embedded SQL approach. (Since my own 
stuff is now working, I can also confirm that it is VERY fast...)

4.  I think you are very lucky to have someone like Andrew looking at it. I 
read his comments and agree almost entirely. (I think 10 lines is  a bit too 
rigid a rule, but the principle is correct.). In OO, as in most online 
processing, "small is beautiful"... Andrew's point about refactoring is an 
excellent one and I wouldn't have thought of that as a good way to improve 
what you have; I've learned from this interchange :-)

5. You deserve credit for posting ANY code here, and to post a first 
attempt, is brave and  admirable. I know you won't take the comments to 
heart in a negative way.

6. You might think about offloading a lot of the literals into external 
data. C# provides a number of places where you can put stuff... System 
collections, XML files, configuration data, to name a few. The COBOL 
Reserved Word list could be an XML file that gets loaded once at startup, 
rather than being embedded in the program.

I use an XML file to "remember" the last used state of an app. so the user 
doesn't have to keep re-keying it if they plan on processing against the 
same database... but this is only one way, and possibly not even the best. 
It has the advantage that things like connection strings and static SQL can 
be changed from outside the program. C# makes it a doddle to manipulate XML.

SUMMARY:

For my money, you need to start thinking in terms of a production line. 
Think about a series of (small) machines (components) that take scrap metal 
in one end and push knives and forks out the other. Each machine carries out 
another step in the process, each machine does exactly what it does, and 
functionality does not overlap. (Think encapsulation and "black boxes"). 
Some machines provide support functions to machines on the main line, but 
for each machine, the goals it must achieve are clear, and the primary focus 
for it, from which it must not be distracted by having to do ancilliary and 
support functions (like accessing databases). Think of machines in each 
layer (tier) of the production process. (A component needs to validate, 
retrieve, or update certain data? It should focus on what it is going to DO 
with that data and leave the "lower order" functions to other components who 
deal with that. It can simply activate a "retriever" and know that what 
comes back is valid and timely or whatever...) Activate the retriever; take 
what it returns, get on with what this component is really about...:-)

The major diference between OO and procedural processing is that procedural 
code tends to not even start processing until EVERYTHING is defined in data 
terms, and these data definitions then drive the processing. With OO, only 
the data necessary for a specific function is required at any given moment, 
and the data and the manipulation of it is "encapsulated" into a specific 
object.  OO objects neither know nor care what other OO Objects are doing. 
They are focussed on achieving their own design goals and that is all that 
matters. Communication with the outside world is by means of messages and 
interfaces.

Still, you have demonstrated a really good grasp of the language itself, the 
program works, and it can be made more elegant fairly easily. All in all, 
pretty good for a first attempt :-)

Pete.



"LX-i" <lxi0007@netscape.net> wrote in message 
news:68bfe$45bfea28$454920f8$29351@KNOLOGY.NET...
> Here 'tis.  It looks like there's a little word-wrapping going on - I 
> wasn't really attentive to ensuring that I didn't go past 80 on some 
…[1044 more quoted lines elided]…
> man who's offended by a God he doesn't believe in?" - Brad Stine
```

##### ↳ ↳ Re: [OT] My First C# (warning - long post)

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-01-31T22:45:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8eb1$45c17062$454920f8$31633@KNOLOGY.NET>`
- **In-Reply-To:** `<52d3ahF1nt1otU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Hi Daniel,
> 
…[5 more quoted lines elided]…
> first attempt :-)

I'm a big guy (well, metaphorically).  I can take it.

> I formed some first impressions from a quick look (before I saw Andrew's 
> comments.... :-)) and they were as follows:
> 
> 1. It is a procedural translation into an OO environment. Even down to the 
> "Working-storage" at the top of the Class... :-)

Aw man, cut me some slack - show me a COBOL program with less than 15 
working-storage variables!  :)  (The reason I did this that way, 
especially for the block of private ones, was just so that the memory 
didn't have to be loaded every time.  Can you imagine loading that array 
of COBOL keywords every time isCobolKeyword is called?)

> 2. You show an excellent grasp of using functions and, at the nitty-gritty 
> level you have it sussed. (I think you may be over-using Trim()...
> "Convert.ToChar(dr["element_type"].ToString().Trim().Substring(0,1))" seems 
> a bit unnecessary to me, when all you are wanting is one byte, but I haven't 
> checked the details...:-)

You'd think that you could cast a substring of one character TO a 
character, wouldn't you?  Yes, the Trim() is probably extra now, but 
that was my attempt to get it to quit griping at me that I had given it 
a "String", when it wanted a "char".  (I know in Java you can't do a 
switch on a string - I'm guessing that it's that way in C# as well.  If 
not, then I spent 20 minutes wasting my time...  :>  Which wouldn't 
surprise me to find out...)

> 3. The embedded SQL is just a hangover from procedural code; it is 
> inefficient and ugly.  Think in tiers; separate data access from business 
…[3 more quoted lines elided]…
> stuff is now working, I can also confirm that it is VERY fast...)

See my post to Andrew on this topic - how?

> 4.  I think you are very lucky to have someone like Andrew looking at it. I 
> read his comments and agree almost entirely. (I think 10 lines is  a bit too 
…[3 more quoted lines elided]…
> what you have; I've learned from this interchange :-)

I really appreciate him doing it.

I realized today how much of a geek I am.  I have Visual C# 2005 Express 
Edition, Eclipse (for Java 2 1.5), Fujitsu COBOL, and Visual SlickEdit 
all on one machine.  Wow...

> 5. You deserve credit for posting ANY code here, and to post a first 
> attempt, is brave and  admirable. I know you won't take the comments to 
> heart in a negative way.

I won't.  Of course, that's also why I posted my list of caveats before 
the code - there are things about it I don't like, but when the IDE or 
shop standards enforce "style", it's hard to take any complaints about 
it personally.

> 6. You might think about offloading a lot of the literals into external 
> data. C# provides a number of places where you can put stuff... System 
> collections, XML files, configuration data, to name a few. The COBOL 
> Reserved Word list could be an XML file that gets loaded once at startup, 
> rather than being embedded in the program.

I was thinking that there *had* to be a better way to do that.  Can you 
make a static XML that gets "built into" (whatever the C# term for that 
would be) the .dll file?

> For my money, you need to start thinking in terms of a production line. 
> Think about a series of (small) machines (components) that take scrap metal 
…[12 more quoted lines elided]…
> what it returns, get on with what this component is really about...:-)

I'd really love to do this...  Gotta get the grey matter aligned properly...

> Still, you have demonstrated a really good grasp of the language itself, the 
> program works, and it can be made more elegant fairly easily. All in all, 
> pretty good for a first attempt :-)

Thanks.  It really is a piece of cake - I've converted three ASPs to 
ASP.NET/C# pages in 2 days (6 if you count the little ones I'm working 
on now).  It took me a little over a day on the first one, then it just 
clicked.  Of course, it's probably still procedural C#, but it's fast.  :)

This DB abstraction layer would be good for our system as a whole.  The 
entire thing will be ASP.NET/C# when we're (er, I guess that should be 
"they're") done.  I'm guessing that, once I get that built, we would 
just give it a namespace (maybe CSCS.DataUtilities or something like 
that), then import, er, "using" it in our classes/pages?
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-02T01:50:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52e60aF1n7so3U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:d8eb1$45c17062$454920f8$31633@KNOLOGY.NET...
> Pete Dashwood wrote:
>> Hi Daniel,
…[17 more quoted lines elided]…
> working-storage variables!  :)

I did cut you some slack... Have a look at properties if you really want 
global variables
(The reason I did this that way,
> especially for the block of private ones, was just so that the memory 
> didn't have to be loaded every time.  Can you imagine loading that array 
> of COBOL keywords every time isCobolKeyword is called?)
>
No, and I wouldn't do it... :-)

>> 2. You show an excellent grasp of using functions and, at the 
>> nitty-gritty level you have it sussed. (I think you may be over-using 
…[11 more quoted lines elided]…
> find out...)

Don't make Java assumptions about C#. You can certainly switch on a char or 
string, (as long as they are constant). When it "gripes" at you, there is a 
reason. I consider these gripes as a voice saying: "Pete, you are about to 
learn something..." :-) Fortunately, as the learning process proceeds, the 
voice becomes less insistent. But you have to listen to it, do the homework, 
and not just look for a way to dismiss it as an irritation... :-)

Here's a sample from live code that covers Casting string to Char, setting 
up a Global property, and managing a COBOL data block in C#...

            }

            private  string _IBreturn;

            // A read-write instance property:

            public  string IBreturn

            {

                get

                {

                    return _IBreturn;

                }

                set

                {

                    _IBreturn = value;

                    _IBreturn = _IBreturn.PadRight(5, char.Parse("0"));

                    _IntBlock = _IBreturn +

                                _IntBlock.Substring

                                   (_IBreturn.Length,_IntBlock.Length - 
_IBreturn.Length);

                }

            }

(As you can see, I do not share your aversion to braces surrounding code 
blocks being on a new line, and I actually find this helpful...)

The "set" method inserts a Pic x(5) return code into the start of an 
interface block, defined  as a COBOL structure of 8192 bytes (this is for 
compatibility with COM BSTRING type.)

The return code must be padded with zeroes if it does not occupy the full 5 
bytes. Although _IBreturn is a string, it must be padded with Chars. You may 
consider this is "cheating" so here's a direct cast to char, also taken from 
live code :-)...

            string temp = ", [";

            char[] trimChars = temp.ToCharArray();





(There is no need for ConvertTo, SubString or Trim as any string contains 
the knowledge to cast itself to a char array...)





The final action of the "set" method above is to update the COBOL interface 
block with the new return code. Note that the return code is a private field 
that cannot be accessed other than by means of the get and set methods; the 
public copy of the field automatically uses these methods when it is 
referenced. You could argue that this is unnecessary; why not just slice a 
subtring of  _intBlock when you want the return code?  It is unwieldy to 
keep referencing substrings of an 8K string simply to get 5 bytes. Keeping 
each field in the block separate as a private property and updating the 
block when they get changed, by means of their set methods, seems to work 
pretty well. I can aso "audit" the integrity of the block because I have 
each field of it as a separate entity. The entire block can be easily 
reconstructed from these fields and that might not be so easy if it is being 
sliced left right and centre. Finally, this approach lends itself to 
automation and can be easily generated  from COBOL definitions.



But, most importantly of all, the code that deals with the fields in the 
block can simply reference them, and the block is automatically updated if 
any of the fields are changed (remember what I said about support methods 
doing the lower-order tasks?) so there is no concern about "housekeeping" 
when working on these fields and, because they are public properties, they 
are visible to all methods of the Class.



It's kind of like "intelligent working-storage"... :-)

>
>> 3. The embedded SQL is just a hangover from procedural code; it is 
…[7 more quoted lines elided]…
> See my post to Andrew on this topic - how?



Did you even look at the article I referenced? :-) It not only explains How, 
it shows WHY :-)



Setting a connection and issuing SQL is pretty unavoidable, but after that 
there is a big difference between using a SQL reader and using a 
DataAdapter/DataSet. The DataSet has methods and properties that are really 
useful (and cool :-)). You simply don't get them if you just write embedded 
SQL or open a cursor. The DataAdapter allows you to process everythng and 
only apply the updates at the end when you are satisfied - the DataSet 
automatically notifies errors if you change something incorrectly.



Have a look at the Data facilities in VS 2005. If you know what you're going 
to be accessing, it will build the code for you in minutes. My stuff is 
completely dynamic and designed to work with any database of a given family, 
so I need to know what the structure is at runtime. DataSet methods and 
properties give me that. It was really problematic for me NOT to be able to 
use the facilities in VS 2005 because of the unknown nature of what I would 
be accessing. Time and again I realised that the IDE would generate the code 
if I could simply tell it what I wanted. I spent many hours combing the 
support and help to understand the new (to me) concepts and finally get what 
I needed. I still can't believe it actually works, but it does :-)




>
>> 4.  I think you are very lucky to have someone like Andrew looking at it. 
…[10 more quoted lines elided]…
> on one machine.  Wow...



 A REAL geek would be able to write Fortran in ALL of them... :-)


>
>> 5. You deserve credit for posting ANY code here, and to post a first 
…[37 more quoted lines elided]…
>



Some of the above was intended to help in this area and to put my money 
where my mouth is...:-)  I really am so busy at the moment (I'm 
force-feeding new information and concepts into myself , as well as 
developing, so I'm pretty tired by the end of the day), but I'd like to try 
and contribute if I can.




>> Still, you have demonstrated a really good grasp of the language itself, 
>> the program works, and it can be made more elegant fairly easily. All in 
…[6 more quoted lines elided]…
>



At this point, it really doesn't matter whether it is technically elegant or 
REAL OO... it works. As you write more of it and consider more approaches, 
you'll pick up the OO stuff.


> This DB abstraction layer would be good for our system as a whole.  The 
> entire thing will be ASP.NET/C# when we're (er, I guess that should be 
…[3 more quoted lines elided]…
>



Something like that, certainly...



Pete.
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-01T08:51:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET>`
- **In-Reply-To:** `<52e60aF1n7so3U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:d8eb1$45c17062$454920f8$31633@KNOLOGY.NET...
…[20 more quoted lines elided]…
> global variables

I thought that's what they were...  Isn't that how you define 
properties?  "public [type] [name]"?

(And, I know you were cutting me some slack - I was just being silly...)

> (The reason I did this that way,
>> especially for the block of private ones, was just so that the memory 
…[3 more quoted lines elided]…
> No, and I wouldn't do it... :-)

Along those lines - is there a better way to search through an array 
other than "for (int i = 0; i < array.length; i++)"?

>> You'd think that you could cast a substring of one character TO a 
>> character, wouldn't you?  Yes, the Trim() is probably extra now, but that 
…[11 more quoted lines elided]…
> and not just look for a way to dismiss it as an irritation... :-)

I did look at it as a learning experience.  I was just frustrated at the 
time because I had a 700-line+ file of C# that wouldn't execute because 
of this one little problem.

> Here's a sample from live code that covers Casting string to Char, setting 
> up a Global property, and managing a COBOL data block in C#...
…[36 more quoted lines elided]…
>             }

So you put braces after the variable declaration?  That's the first time 
I've seen that structure.  :)

> (As you can see, I do not share your aversion to braces surrounding code 
> blocks being on a new line, and I actually find this helpful...)

Yeah, and you code in SECTIONs too!  ;)

Of course I'm kidding - that just goes to show that different folks have 
different ideas of what "readable" is.  My biggest complaint in how much 
north-south real estate it takes up on my screen.  I guess if my methods 
were more of a proper size, I wouldn't have to scroll to see them. 
Maybe that's a corollary to the 10-line rule - if you can't see it at 
one time in the editor, it's too big!

(Is it double-spaced in the IDE, or was that just what happened when you 
pasted it into the newsreader?)

> The "set" method inserts a Pic x(5) return code into the start of an 
> interface block, defined  as a COBOL structure of 8192 bytes (this is for 
> compatibility with COM BSTRING type.)

Why did you use char.Parse("0") instead of just '0'?

> The return code must be padded with zeroes if it does not occupy the full 5 
> bytes. Although _IBreturn is a string, it must be padded with Chars. You may 
…[5 more quoted lines elided]…
>             char[] trimChars = temp.ToCharArray();

No, no cheating comment from me...  :)  I wonder if

dr["element_type"].ToString().ToCharArray()[0]

would do what I was trying to do there?

> The final action of the "set" method above is to update the COBOL interface 
> block with the new return code. Note that the return code is a private field 
…[11 more quoted lines elided]…
> automation and can be easily generated from COBOL definitions.

That makes sense to me.  It's a similar concept to a few tables we have 
in our database at work.  They hold "interface parameters", and since 
the paramaters vary for each interface, we have it broken down for each 
format.  It certainly beats reference modification...  especially when 
the next guy comes along and doesn't know that the number of days to 
keep transaction history for this interface is in columns 4-6...  :)

>>> 3. The embedded SQL is just a hangover from procedural code; it is 
>>> inefficient and ugly.  Think in tiers; separate data access from business 
…[8 more quoted lines elided]…
> it shows WHY :-)

I looked at it, and I sort of understand how they did it...  I'm going 
to play with some things over the next few days.  I'll post what I find, 
with hopefully enough COBOL references that the other folks won't toss 
me out on my head.  :)

> Setting a connection and issuing SQL is pretty unavoidable, but after that 
> there is a big difference between using a SQL reader and using a 
…[15 more quoted lines elided]…
> I needed. I still can't believe it actually works, but it does :-)

In looking at things back and forth in writing this reply, it's starting 
to click.

>>> 4.  I think you are very lucky to have someone like Andrew looking at it. 
>>> I read his comments and agree almost entirely. (I think 10 lines is  a 
…[10 more quoted lines elided]…
>  A REAL geek would be able to write Fortran in ALL of them... :-)

OK - I guess I'm safe...  ;)

>> I'd really love to do this...  Gotta get the grey matter aligned 
>> properly...
…[5 more quoted lines elided]…
> and contribute if I can.

I appreciate it.  Don't stay up late on my account.  :)

>> This DB abstraction layer would be good for our system as a whole.  The 
>> entire thing will be ASP.NET/C# when we're (er, I guess that should be 
…[4 more quoted lines elided]…
> Something like that, certainly...

Cool...  :)
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-01T15:31:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52f827F1n712jU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET>`

```
LX-i<lxi0007@netscape.net> 02/01/07 7:51 AM >>>
>
>Along those lines - is there a better way to search through an array 
>other than "for (int i = 0; i < array.length; i++)"?

I'm not sure specifically what you are referring to, but, if we assume the
above code is something like
string array[] = new string[10];
for (int i = 0; i < array.length; i++)
{
    doSomething(array[i]);
}

You can replace it with

foreach (string s in array)
{
    doSomething(s);
}

Is that what you're looking for?

http://www.c-sharpcorner.com/UploadFile/mahesh/WorkingWithArrays111420050603
54AM/WorkingWithArrays.aspx 

MF Net Express 5.0 has something similar for COBOL, which I'll post from
home.

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 6)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-01T14:37:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170369420.683487.228460@h3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<52f827F1n712jU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52f827F1n712jU1@mid.individual.net>`

```
On Feb 1, 10:31 pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> LX-i<lxi0...@netscape.net> 02/01/07 7:51 AM >>>
>
…[35 more quoted lines elided]…
> FirstBank Data Corporation - Lakewood, CO  USA

Good call, the other approach is to use Predicates....

see:  http://www.c-sharpcorner.com/UploadFile/vandita/
PredicatesInArray10232006063515AM/PredicatesInArray.aspx

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-02-01T16:34:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52fbp3F1ltjv4U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52f827F1n712jU1@mid.individual.net> <1170369420.683487.228460@h3g2000cwc.googlegroups.com>`

```
andrewmcdonagh<andrewmcdonagh@gmail.com> 02/01/07 3:37 PM >>>
>On Feb 1, 10:31 pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
>wrote:
…[5 more quoted lines elided]…
>> I'm not sure specifically what you are referring to, but, if we assume
the
>> above code is something like
>> string array[] = new string[10];
…[18 more quoted lines elided]…
>PredicatesInArray10232006063515AM/PredicatesInArray.aspx

Definitely cool.  I had never heard of it before.  Nice use of a delegate.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-01T19:31:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e23d4$45c29473$454920f8$1034@KNOLOGY.NET>`
- **In-Reply-To:** `<1170369420.683487.228460@h3g2000cwc.googlegroups.com>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52f827F1n712jU1@mid.individual.net> <1170369420.683487.228460@h3g2000cwc.googlegroups.com>`

```
andrewmcdonagh wrote:
> Good call, the other approach is to use Predicates....
> 
> see:  http://www.c-sharpcorner.com/UploadFile/vandita/
> PredicatesInArray10232006063515AM/PredicatesInArray.aspx

I found that article, actually, while looking for "array find C#" (I 
believe).  I didn't understand it - I know it works for the "Starts 
With", but I didn't see how it would help me in my "is this a keyword" 
method.
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-01T19:12:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64fe7$45c29000$454920f8$6932@KNOLOGY.NET>`
- **In-Reply-To:** `<52f827F1n712jU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52f827F1n712jU1@mid.individual.net>`

```
Frank Swarbrick wrote:
> LX-i<lxi0007@netscape.net> 02/01/07 7:51 AM >>>
>> Along those lines - is there a better way to search through an array 
…[8 more quoted lines elided]…
> }

Not quite...  but close enough.

> You can replace it with
> 
…[5 more quoted lines elided]…
> Is that what you're looking for?

Sort of.  I've been doing some digging, and had found foreach() - I also 
found the DataSet's ReadXml method.  This is what I've got at the 
current time...

         protected DataSet keywords = new DataSet();
...
         // This is executed in the constructor
         protected void fillCobolKeywords() {
             keywords.ReadXml("cobol_keywords.xml");
         }
...
         // Returns "true" if the word passed is a COBOL keyword
         protected bool isCobolKeyword(String ickText)
         {
             bool      ick = false;
             DataTable dt  = keywords.Tables[0];

             foreach (DataRow dr in dt.Rows)
             {
                 if (dr[0].ToString() == ickText)
                 {
                     ick = true;
                 }
             }

             return ick;
         }

With this, though, if the keyword is "ACCEPT", it's still plowing 
through 350+ entries before returning.  Could (should) I short-circuit 
it and return true in the loop - something like this...

         // Returns "true" if the word passed is a COBOL keyword
         protected bool isCobolKeyword(String ickText)
         {
             DataTable dt  = keywords.Tables[0];

             foreach (DataRow dr in dt.Rows)
             {
                 if (dr[0].ToString() == ickText)
                 {
                     return true;
                 }
             }

             return false;
         }

I appreciate the suggestion.  foreach is pretty cool - I've used it in 
PHP quite a bit.  I guess what I was looking for was an array.search 
method or something that may apply a more efficient searching algorithm 
than just "gimme one - is this it? nope, gimme another one - is this it? 
nope..." etc.

(The only reason I'm concerned with this sort of efficiency is that this 
...er... whatever it is (class/component/process masquerading as OO) 
will run as part of a page post from our .NET CM site.  If I'm 
rebuilding the indexes, it doesn't matter if it takes 20 seconds per 
program - but in that web page, it would be unacceptable.)

Hmm....  Maybe this needs to be a separate thread...  Can an ASP.NET 
page spawn a thread that runs after the response has been sent to the 
user?  Sounds like I've got more digging to do....  I wish I wasn't 
moving in 2 weeks!  It seems like there's just too much to consider - I 
guess there's got to be something for the person who comes after me to 
do.  :)
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-02T12:32:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52fbl0F1o57gtU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET...
> Pete Dashwood wrote:
>> "LX-i" <lxi0007@netscape.net> wrote in message 
…[24 more quoted lines elided]…
> "public [type] [name]"?

No. Those are global variables. Click on Help in VS2005 and then click 
"index". Enter "properties"... Or start with this direct local link:

ms-help://MS.VSExpressCC.v80/MS.NETFramework.v20.en/dv_csref/html/f7f67b05-0983-4cdb-96af-1855d24c967c.htm

>
> (And, I know you were cutting me some slack - I was just being silly...)
…[10 more quoted lines elided]…
>

Yes, "foreach". I think Frank has covered it.

>>> You'd think that you could cast a substring of one character TO a 
>>> character, wouldn't you?  Yes, the Trim() is probably extra now, but 
…[17 more quoted lines elided]…
>

Yeah, I know... been there :-) Nevertheless, patience is an essential part 
of the learning process...

>> Here's a sample from live code that covers Casting string to Char, 
>> setting up a Global property, and managing a COBOL data block in C#...
…[44 more quoted lines elided]…
> Yeah, and you code in SECTIONs too!  ;)

Touche!  (Nevertheless, my code works... :-))
>
> Of course I'm kidding - that just goes to show that different folks have 
…[4 more quoted lines elided]…
> in the editor, it's too big!

Absolutely. Now you're getting it. Small is beautiful.
>
> (Is it double-spaced in the IDE, or was that just what happened when you 
> pasted it into the newsreader?)

No, it's the  bloody newsreader. I was tempted to post in HTML but I realise 
most people don't have their newsreaders configured for it.

>
>> The "set" method inserts a Pic x(5) return code into the start of an 
…[3 more quoted lines elided]…
> Why did you use char.Parse("0") instead of just '0'?

Because '0' wouldn't work...? :-)

>
>> The return code must be padded with zeroes if it does not occupy the full 
…[12 more quoted lines elided]…
> would do what I was trying to do there?

Why not try it and see? The empirical approach always trumps the theoretical 
one... :-)

>
>> The final action of the "set" method above is to update the COBOL 
…[38 more quoted lines elided]…
>

I strongly recommend some experimentation.

>> Setting a connection and issuing SQL is pretty unavoidable, but after 
>> that there is a big difference between using a SQL reader and using a 
…[21 more quoted lines elided]…
>
Excellent! It will take a little time. It is a journey of many small 
steps... Each method you write will be "better" than the last one.

For myself, I can see the difference in what I write today and what I wrote 
even 5 weeks ago. In a year, I'll probably be embarrassed by what I have and 
want to rewrite the lot... :-) At this stage, as I mentioned earlier, 
elegance is only of passing interest. The prime criterion is that it works. 
When it works, it not only builds confidence, but it also buys time to do 
further study and make the next round even better.

<remainder snipped>

Pete.
```

###### ↳ ↳ ↳ Re: [OT] My First C# (warning - long post)

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-02-01T19:42:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cdef$45c296f3$454920f8$15447@KNOLOGY.NET>`
- **In-Reply-To:** `<52fbl0F1o57gtU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52fbl0F1o57gtU1@mid.individual.net>`

```
Pete Dashwood wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET...
…[4 more quoted lines elided]…
> "index". Enter "properties"... Or start with this direct local link:

I found that.  (BTW, that's just another plus of the IDE - the F1 help 
is really helpful!)

>>> The "set" method inserts a Pic x(5) return code into the start of an 
>>> interface block, defined  as a COBOL structure of 8192 bytes (this is for 
…[3 more quoted lines elided]…
> Because '0' wouldn't work...? :-)

Must be that managed vs. unmanaged stuff...  I can assign '0' to a char 
variable.  I believe you - I wonder what the difference is?

> Excellent! It will take a little time. It is a journey of many small 
> steps... Each method you write will be "better" than the last one.

OK - here's what I've got for one of the methods.  I'm not sure that 
this looks right...

         protected DataSet itemInfo = new DataSet();
...
         // Establish the element for this class instance
         public void retrieveElementInfo(String reiElementId)
         {
             // Retrieve the information about the passed program
             String sql = "SELECT * "
                 + "FROM active_elements "
                 + "WHERE element_id = '" + reiElementId.Trim() + "'";
             SqlDataAdapter da = new SqlDataAdapter(sql, dbConn);
             da.Fill(itemInfo);

             if (itemInfo.Tables.Count > 0)
             {
                 elementType    = 
itemInfo.Tables[0].Rows[0]["element_type"].ToString().ToCharArray()[0];
                 elementSubType = 
itemInfo.Tables[0].Rows[0]["element_subtype"].ToString().Trim();
                 fileName       = 
itemInfo.Tables[0].Rows[0]["server_name"].ToString().Trim();
                 elementId      = reiElementId.Trim();
             }
         }

(We have to trim the stuff coming out of the database because it's 
defined as char instead of varchar...)
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 7)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-02T03:46:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170416819.673830.134600@k78g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4cdef$45c296f3$454920f8$15447@KNOLOGY.NET>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52fbl0F1o57gtU1@mid.individual.net> <4cdef$45c296f3$454920f8$15447@KNOLOGY.NET>`

```
On Feb 2, 1:42 am, LX-i <lxi0...@netscape.net> wrote:
> Pete Dashwood wrote:
> > "LX-i" <lxi0...@netscape.net> wrote in message
…[66 more quoted lines elided]…
> a man who's offended by a God he doesn't believe in?" - Brad Stine

Quick suggestion about your COBOL keywords....  instead of using an
XML file, or raw array, you'll get much better (near constant time)
lookup performance if you use a single in memory HashTable collection.
Hashtables use two objects, one is a 'key' and the other a 'value'.
Unfortunately the c# library doesn't have a Java HashSet, which has
the same behaviour as hastables, but is for storing keys only.

 // Create a new hash table.
 Hashtable cobolKeywords = new Hashtable();

 // Add some elements to the hash table.
 // hashtable does not allow
 // duplicate keys, but values can be duplicates.
 cobolKeywords.Add("ACCEPT", "ACCEPT ");
 cobolKeywords.Add("ACCESS", "ACCESS");
 cobolKeywords.Add("ACQUIRE", "ACQUIRE");
 cobolKeywords.Add("ADD", "ADD");
 ...

  // The Item property is the default property, so you
  // can omit its name when accessing elements.
  Console.WriteLine("The value for Add = ", cobolKeywords["ADD"]   );

  // ContainsKey can be used to test keys before inserting them.
  if (! cobolKeywords.ContainsKey("BEFORE"))
  {
     cobolKeywords.Add("BEFORE", "BEFORE");
     Console.WriteLine("Value added for key = \"ht\": {0}",
cobolKeywords["ht"]);
  }

  // When you use foreach to enumerate hash table elements,
  // the elements are retrieved as KeyValuePair objects.

  foreach( DictionaryEntry de in cobolKeywords)
  {
      Console.WriteLine("Key = {0}, Value = {1}", de.Key, de.Value);
  }

   // To get the values alone, use the Values property.
   ICollection valueColl = cobolKeywords.Values;

   // The elements of the ValueCollection are strongly typed
   // with the type that was specified for hash table values.

   foreach( string s in valueColl )
   {
         Console.WriteLine("Value = {0}", s);
   }
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-03T13:20:12+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52i2ptF1p0u25U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52fbl0F1o57gtU1@mid.individual.net> <4cdef$45c296f3$454920f8$15447@KNOLOGY.NET> <1170416819.673830.134600@k78g2000cwa.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170416819.673830.134600@k78g2000cwa.googlegroups.com...
> On Feb 2, 1:42 am, LX-i <lxi0...@netscape.net> wrote:
>> Pete Dashwood wrote:
<snip>

> Quick suggestion about your COBOL keywords....  instead of using an
> XML file, or raw array, you'll get much better (near constant time)
…[4 more quoted lines elided]…
>
Er...not necessarily... :-)

Although C# supports the Hashtable function (so Java folks can remain 
comfortable...:-)),  it is much better to use the C# Dictionary Class 
because it doesn't require boxing and unboxing of objects.

Furthermore, the Dictionary Class DOES support a collection of Keys and 
Values as separate entities, if you want this.

I have no issue with the approach (it's very good), but would strongly 
recommend Dictionary, rather than Hashtable.

(Check out the VS 2005 Help index for "Dictionary"...)

> // Create a new hash table.
> Hashtable cobolKeywords = new Hashtable();
…[40 more quoted lines elided]…
>

Really good sample code above, Andrew. Good stuff!

Pete.
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

_(reply depth: 9)_

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-04T15:11:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170630684.528050.207950@m58g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<52i2ptF1p0u25U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <d8eb1$45c17062$454920f8$31633@KNOLOGY.NET> <52e60aF1n7so3U1@mid.individual.net> <19a17$45c1fe8b$454920f8$23261@KNOLOGY.NET> <52fbl0F1o57gtU1@mid.individual.net> <4cdef$45c296f3$454920f8$15447@KNOLOGY.NET> <1170416819.673830.134600@k78g2000cwa.googlegroups.com> <52i2ptF1p0u25U1@mid.individual.net>`

```
On Feb 3, 12:20 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "andrewmcdonagh" <andrewmcdon...@gmail.com> wrote in message
>
…[25 more quoted lines elided]…
>

Yeah I saw Dictionary, though I thought that autoboxing would not
happen with String objects... this is my Java expo making me assume
things not necessary correct in c#.

nice one though!

snipped...

> >   }
>
> Really good sample code above, Andrew. Good stuff!
>
> Pete.

Cheers, though it wasn't mine, I copied it from MSDN and edited to fit
with our topic of keywords...
```

##### ↳ ↳ Re: My First C# (warning - long post)

- **From:** "andrewmcdonagh" <andrewmcdonagh@gmail.com>
- **Date:** 2007-02-01T03:15:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1170328519.918232.91880@j27g2000cwj.googlegroups.com>`
- **In-Reply-To:** `<52d3ahF1nt1otU1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net>`

```
On Feb 1, 2:58 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Hi Daniel,
>
…[5 more quoted lines elided]…
> first attempt :-)

Thanks Pete.



snipped

>
> 4.  I think you are very lucky to have someone like Andrew looking at it. I
> read his comments and agree almost entirely. (I think 10 lines is  a bit too
> rigid a rule, but the principle is correct.).

In the words of Captain Barbosa from Pirates of the Caribbean...

'..They are so much Rules as Guidelines...'

;-)

Andrew
```

###### ↳ ↳ ↳ Re: My First C# (warning - long post)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-02T12:39:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52fc1tF1mqen1U1@mid.individual.net>`
- **References:** `<68bfe$45bfea28$454920f8$29351@KNOLOGY.NET> <52d3ahF1nt1otU1@mid.individual.net> <1170328519.918232.91880@j27g2000cwj.googlegroups.com>`

```

"andrewmcdonagh" <andrewmcdonagh@gmail.com> wrote in message 
news:1170328519.918232.91880@j27g2000cwj.googlegroups.com...
> On Feb 1, 2:58 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
>

 Not at all. I 've found your posts very useful and I know Daniel is getting 
much from them. Appreciate you taking the time to share  your experience and 
expertise; it's what forums are for.
>
>
…[13 more quoted lines elided]…
> ;-)

Run!!! :-)

It was a great film.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
