# coding: utf-8
import re;
'''
    id: Alpha[Alpha|Digit]*
    int: Digit+ | "-" Digit+
    Alpha: [A-Z] | [a-z]
    Digit: [0-9]
'''
class Token():
    def __init__(self, type, lexeme):
        self.type = type;
        self.lexeme = lexeme;


''' 
    상태 0 : 초기상태
    상태 0->1 : Digit가 들어오면 1이 됨.
    상태 0->2 : -가 들어오면 2가 됨.
    상태 0->3 : Alpha가 들어오면 1이 됨.
    1->2 : Digit가 들어오면 됨. 그 외는 전부 에러 처리.
    2->2 : Digit가 들어오면 됨. 그 외는 전부 에러 처리.
    3->3 : Alpha,Digit만 허용. 그 외는 전부 에러 처리.
''' 
class Scanner():
    def __init__(self):
        print('Start Scanning');

    def start(self, fileLocation):
        f = open(fileLocation, 'r');
        numberPattern = re.compile('[0-9]');
        alphaPattern = re.compile('[a-zA-Z]');
        minusPattern = re.compile('-');
    
        while True:
            line = f.readline();
            self.statusNumber = 0;
            if not line: break;
            for char in line:
                # 한 line의 가장 첫번째 문자를 읽어서 판단함.
                if self.statusNumber == 0:
                    if numberPattern.match(char):
                        self.statusNumber = 1

                    elif minusPattern.match(char):
                        self.statusNumber = 2
                        
                    elif alphaPattern.match(char):
                        self.statusNumber = 3

                # 1->2 : Digit가 들어오면 됨. 그 외는 전부 에러 처리.
                # 2->2 : Digit가 들어오면 됨. 그 외는 전부 에러 처리.
                elif self.statusNumber == 1 or self.statusNumber == 2:
                    if not numberPattern.match(char): continue;    
                    self.statusNumber = 2;
                    
                # 3->3 : Alpha,Digit만 허용. 그 외는 전부 에러 처리.
                elif self.statusNumber == 3:
                    if alphaPattern.match(char) or numberPattern.match(char):
                        self.statusNumber = 3;
                        
            self.tokenize(self.statusNumber, line);
        f.close();
        
    '''
            마지막 상태  0 : 에러
            마지막 생태 1 : Token type = int
            마지막 상태 2 : Token type = int
            마지막 생태 3 : Token type = id
    '''
    def tokenize(self, finalStatus, line):
        if(finalStatus == 0):
            print('final status : 0, error.');
            
        elif(finalStatus == 1 or finalStatus == 2):
            t = Token('int', line);
            print(t.type +' : '+t.lexeme);
            
        elif(finalStatus == 3):
            t = Token('id', line);
            print(t.type +' : '+t.lexeme);

        