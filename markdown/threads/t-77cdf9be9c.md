[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Run cobol shared object using dlsym on AIX4.2 then SIGSEGV

_1 message · 1 participant · 1997-07_

---

### Run cobol shared object using dlsym on AIX4.2 then SIGSEGV

- **From:** "you" <ua-author-10579@usenetarchives.gap>
- **Date:** 1997-07-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5q7m9b$maa@reader.seed.net.tw>`

```

Hi Sir:
Has anyone can help me to solve following problem:
(1) My OS is AIX4.2, MF COBOL is cobol v3.2.31L-e
PRN=2XCLY/EDJ:7a.1a.11.04a, PTI=NLSv
(2) case 1: use following link command to link main program
cob -xo test.x main.o -Q"-bexpall" -Q"-brtl" -ldl
AP1, AP2 are COBOL PROGRAMs. and compile/link step are:
cob -cx ap1.cob
cob -cx ap2.cob
ld -o ap1.so ap1.o -bnoentry -bE:ap1.exp -G -lc
ld -o ap2.so ap2.o -bnoentry -bE:ap2.exp -G -lc
main(): call following function
dlopen("AP1.so")-->dlsym("AP1")-->execute AP1-->dlclose()
dlopen("AP2.so")-->dlsym("AP2")-->execute AP2-->dlclose()
dlopen("AP1.so")-->dlsym("AP1")-->execute AP1-->dlclose()
==> Execute test.x --> OK
(3) case 2: use following link command
cob -g -xo test.x main.o \
-L$(ORACLE_HOME)/lib $(COBSQLINTF) $(PROLDLIBS)\-->(ORACLE LIBs)
-ldl
-Q"-bexpall" -Q"-brtl"
==> we link main program with ORACLE LIBs, but we don't use any
ORACLE function. Execute test.x then occur following error message:
dlopen("AP1.so")-->dlsym("AP1")-->execute AP1-->dlclose()
dlopen("AP2.so")-->dlsym("AP2")-->execute AP2-->dlclose()
dlopen("AP1.so")-->dlsym("AP1")-->execute AP1(error in this step)
--> Segmentation fault in mFt_xe_sru_get at 0xd025256c
0xd025256c (mFt_xe_sru_get+0x58) 88630003 lbz r3,0x3(r3)

Thanks
Chih Liang Wu. 1997/7/12
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
