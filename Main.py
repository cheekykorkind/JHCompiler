# coding: utf-8

'''
    Intermediate code generation은 생략하고 바로 x86 Assembly language를 생성한다.
'''
import sys;

from LexicalAnalysis.Scanner import Scanner;

if __name__ == "__main__":
    Scanner().start('C:\\JHCompilerTestData.txt');
