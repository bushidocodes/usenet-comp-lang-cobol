[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem using java with cobol

_1 message · 1 participant · 2006-04_

---

### Problem using java with cobol

- **From:** "awosy" <wardmaenhout@skynet.be>
- **Date:** 2006-04-28T13:21:40+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4451fac3$0$2133$ba620e4c@news.skynet.be>`

```
Hey

I need to pass parameter to a cobol program with I start from a java program.
I was able to run an cobol program that doesn't use parameters already but i'm stuck now

this is my java code i use to run a cobol program that doesn't need parameters

public class TestRunCobol 
{
	private static ShowText txtProg;
	
	public static void main(String[] args) 
	{
		txtProg = new ShowText();
		txtProg.run();
	}
}

And this is the cobol program to which i want to pass 1 parameter (String value)

IDENTIFICATION DIVISION.
PROGRAM-ID. ShowText.
ENVIRONMENT DIVISION.
DATA DIVISION.
       WORKING-STORAGE SECTION.
               01 break pic x.
       LINKAGE SECTION.
              01 param1 object reference "java.lang.String".
PROCEDURE DIVISION USING by value param1.
Main.
       Display "Parameter passed: " param1
       accept break from console
       Stop run. 

can somebody tell me what i have to do in my java code to pass the String value?


--------------=  Posted using GrabIt  =----------------
------=  Binary Usenet downloading made easy =---------
-=  Get GrabIt for free from http://www.shemes.com/  =-
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
