import re

class ValuesTokenClass:
    KeyWordReturn_var = 2
    PersonalVariableName = 3
    NumbersDigits_var = 4
    Colon_var = 5
    SemiColon_var = 7
    Str_var = 8
    bracketOpen_var = 9
    bracketClose_var = 10
    bracketFigureOpen_var = 11
    bracketFigureClose_var = 12
    KeyWordInt = 13
    KeyWOrdFloat = 14
    prefix_plus = 15
    minus = 16
    not_bit = 17
    not_logic = 18
    div_ost = 19
    div = 20
    mult = 21
    plus = 22
    bitR = 24
    bitL = 25
    bitAnd = 26
    bitOr = 27
    cmpeqeq = 28
    cmp_noeq = 29
    cmp_moreeq = 30
    cmp_more = 31
    cmp_less = 32
    cmp_less_eq = 33
    eq = 34
    coma = 35
    tern = 36
    do = 37
    while_cirle = 38
    xor_xor = 39
    coment = 40




class BoxTokens_Class:
    def __init__(self, typesToken_args: ValuesTokenClass, valueTokens_args: str):
        self.typesToken_args = typesToken_args
        self.valueTokens_args = valueTokens_args
    def __str__(self):
        return ("NameToken: " + str(self.typesToken_args) + ", ValueToken: " + str(self.valueTokens_args) + "\n")

class FixedDataTokens_Class ():
    def __init__(self, typeToken_args: ValuesTokenClass, DemoTypeTok, ifKeywordBool_Args = False):
        self.ifKeywordBool_Args = ifKeywordBool_Args
        self.typeToken_args = typeToken_args
        self.DemoTypeTok = DemoTypeTok

class NoFixedDataTokens_Class:
    def __init__(self, typeToken_args: ValuesTokenClass, DemoTypeTok: str):
        self.typeToken_args = typeToken_args
        self.DemoTypeTok = DemoTypeTok

class BoxNoFixedDataTokens_Class (NoFixedDataTokens_Class):
    def __init__(self, typeToken_args: ValuesTokenClass, sTr, DemoTypeTok: str = ""):
        super().__init__(typeToken_args, DemoTypeTok)
        self.RegularRe = re.compile(sTr)
        self.typeToken_args = typeToken_args

class FixedBoxDataToken:
    FixedBox_list = [
        FixedDataTokens_Class(ValuesTokenClass.KeyWordReturn_var, "return"),
        FixedDataTokens_Class(ValuesTokenClass.Colon_var, ":"),
        FixedDataTokens_Class(ValuesTokenClass.SemiColon_var, ";"),
        FixedDataTokens_Class(ValuesTokenClass.SemiColon_var, "\n"),
        FixedDataTokens_Class(ValuesTokenClass.bracketOpen_var, "("),
        FixedDataTokens_Class(ValuesTokenClass.bracketClose_var, ")"),
        FixedDataTokens_Class(ValuesTokenClass.bracketFigureOpen_var, "{"),
        FixedDataTokens_Class(ValuesTokenClass.bracketFigureClose_var, "}"),
        FixedDataTokens_Class(ValuesTokenClass.KeyWordInt, "int"),
        FixedDataTokens_Class(ValuesTokenClass.KeyWOrdFloat, "float"),
        FixedDataTokens_Class(ValuesTokenClass.prefix_plus, "++"),
        FixedDataTokens_Class(ValuesTokenClass.minus, "-"),
        FixedDataTokens_Class(ValuesTokenClass.not_logic, "!"),
        FixedDataTokens_Class(ValuesTokenClass.not_bit, "~"),
        FixedDataTokens_Class(ValuesTokenClass.div_ost, "%"),
        FixedDataTokens_Class(ValuesTokenClass.div, "/"),
        FixedDataTokens_Class(ValuesTokenClass.xor_xor, "^"),
        FixedDataTokens_Class(ValuesTokenClass.mult, "*"),
        FixedDataTokens_Class(ValuesTokenClass.plus, "+"),
        FixedDataTokens_Class(ValuesTokenClass.bitR, ">>"),
        FixedDataTokens_Class(ValuesTokenClass.bitL, "<<"),
        FixedDataTokens_Class(ValuesTokenClass.bitAnd, "&"),
        FixedDataTokens_Class(ValuesTokenClass.bitOr, "|"),
        FixedDataTokens_Class(ValuesTokenClass.cmpeqeq, "=="),
        FixedDataTokens_Class(ValuesTokenClass.eq, "="),
        FixedDataTokens_Class(ValuesTokenClass.cmp_more, ">"),
        FixedDataTokens_Class(ValuesTokenClass.cmp_moreeq, ">="),
        FixedDataTokens_Class(ValuesTokenClass.cmp_less, "<"),
        FixedDataTokens_Class(ValuesTokenClass.cmp_less_eq, "<="),
        FixedDataTokens_Class(ValuesTokenClass.cmp_noeq, "!="),
        FixedDataTokens_Class(ValuesTokenClass.coma, ","),
        FixedDataTokens_Class(ValuesTokenClass.tern, "?"),
        FixedDataTokens_Class(ValuesTokenClass.do, "do"),
        FixedDataTokens_Class(ValuesTokenClass.while_cirle, "while"),
        FixedDataTokens_Class(ValuesTokenClass.coment, "/*"),

        ]
    NoFixedBox_list = [
        BoxNoFixedDataTokens_Class(ValuesTokenClass.PersonalVariableName, "[a-zA-Z][a-zA-Z0-9]*"),
        BoxNoFixedDataTokens_Class(ValuesTokenClass.NumbersDigits_var, "(0|[1-9][0-9]*)+")
    ]

class FindTokens_Class:
    invertedWords_var = ['+', '&', '>>', '|', '/', '<', '^', '>', '%', '!=', '<<', '*', '<=', '>=', '==', "?", ":", "-", "~", "!", ";", ")", "(", ","]
    ListSkipSymvol = [" ", "\r", "\n", "\t"]
    BasketTokens_list = []
    CoordError_x = 0
    CoordError_y = 1

    def __init__(self, current_line: str):
        self.currentLine_var = current_line
        self.shredding()

        for i in range(len(self.BasketTokens_list) // 2):
            for i in range(len(self.BasketTokens_list)):
                if i == 0:
                    continue
                if self.BasketTokens_list[i - 1].valueTokens_args == "/" and self.BasketTokens_list[i].valueTokens_args == "/":
                    self.BasketTokens_list[i - 1].valueTokens_args = "//"
                    self.BasketTokens_list[i - 1].tag = 40
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == "+" and self.BasketTokens_list[i].valueTokens_args == "+":
                    self.BasketTokens_list[i - 1].valueTokens_args = "++"
                    self.BasketTokens_list[i - 1].tag = 22
                    del self.BasketTokens_list[i]
                    break

                if self.BasketTokens_list[i - 1].valueTokens_args == "<" and self.BasketTokens_list[i].valueTokens_args == "=":
                    self.BasketTokens_list[i - 1].valueTokens_args = "<="
                    self.BasketTokens_list[i - 1].tag = 33
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == ">" and self.BasketTokens_list[i].valueTokens_args == "=":
                    self.BasketTokens_list[i - 1].valueTokens_args = ">="
                    self.BasketTokens_list[i - 1].tag = 30
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == "=" and self.BasketTokens_list[i].valueTokens_args == "=":
                    self.BasketTokens_list[i - 1].valueTokens_args = "=="
                    self.BasketTokens_list[i - 1].tag = 28
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == ">" and self.BasketTokens_list[i].valueTokens_args == ">":
                    self.BasketTokens_list[i - 1].valueTokens_args = ">>"
                    self.BasketTokens_list[i - 1].tag = 25
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == "!" and self.BasketTokens_list[i].valueTokens_args == "=":
                    self.BasketTokens_list[i - 1].valueTokens_args = "!="
                    self.BasketTokens_list[i - 1].tag = 29
                    del self.BasketTokens_list[i]
                    break
                if self.BasketTokens_list[i - 1].valueTokens_args == "<" and self.BasketTokens_list[i].valueTokens_args == "<":
                    self.BasketTokens_list[i - 1].valueTokens_args = "<<"
                    self.BasketTokens_list[i - 1].tag = 24
                    del self.BasketTokens_list[i]
                    break
    def shredding(self):
        while self.checkVar_Func():
            temporaryVar = None
            temporaryVar = self.JumpWord_func()
            if temporaryVar != None:
                self.BasketTokens_list.append(temporaryVar)
                continue
            if not self.checkVar_Func():
                break
            temporaryVar = self.shreddingStableData()
            if temporaryVar is None:
                temporaryVar = self.shreddingDinamycData()
            if temporaryVar is None:
                temporaryVar1 = 0
                for j in self.currentLine_var[self.CoordError_x:]:
                    if j in self.invertedWords_var or j.isspace():
                        break
                    temporaryVar1 += 1
                if (self.currentLine_var[self.CoordError_x] == '"' and self.currentLine_var[self.CoordError_x + temporaryVar1 - 1] == '"'):
                    temporaryVar = BoxTokens_Class(ValuesTokenClass.Str_var, self.currentLine_var[self.CoordError_x: temporaryVar1 + self.CoordError_x])
                elif (self.currentLine_var[self.CoordError_x] == "'" and self.currentLine_var[self.CoordError_x + temporaryVar1 - 1] == "'"):
                    temporaryVar = BoxTokens_Class(ValuesTokenClass.Str_var, self.currentLine_var[self.CoordError_x: temporaryVar1 + self.CoordError_x])
                self.CoordError_x += temporaryVar1
            if temporaryVar is None:
                print("Помилка синтаксису, не існує токен: Строка: {}, Елемент: {}".format(self.CoordError_y, self.CoordError_x))
                print("{}{}{}".format(self.currentLine_var[:self.CoordError_x], self.currentLine_var[self.CoordError_x], self.currentLine_var[self.CoordError_x + 1:]))
                input()
                SystemExit
                return None
            self.BasketTokens_list.append(temporaryVar)

    def shreddingStableData(self) -> BoxTokens_Class:
        for i in FixedBoxDataToken.FixedBox_list:
            tempVar1 = i.DemoTypeTok
            countSymvols_in_words = len(tempVar1)
            if self.CoordError_x + countSymvols_in_words > len(self.currentLine_var) or self.currentLine_var[self.CoordError_x: countSymvols_in_words + self.CoordError_x] != tempVar1:
                continue
            if self.CoordError_x + countSymvols_in_words < len(self.currentLine_var) and i.ifKeywordBool_Args:
                Following_word = self.currentLine_var[self.CoordError_x + countSymvols_in_words]
                if Following_word == "_" or Following_word.isalnum():
                    continue
            self.CoordError_x += countSymvols_in_words
            if i.typeToken_args==7:
                self.CoordError_y +=1
            return BoxTokens_Class(i.typeToken_args, i.DemoTypeTok)
        return None

    def shreddingDinamycData(self) -> BoxTokens_Class:
        for i in FixedBoxDataToken.NoFixedBox_list:
            Var_counter = 0
            for j in self.currentLine_var[self.CoordError_x:]:
                if j in self.invertedWords_var or j.isspace():
                    break
                Var_counter += 1
            congruityVar = i.RegularRe.match(self.currentLine_var[self.CoordError_x: Var_counter + self.CoordError_x], 0)
            if (not congruityVar):
                continue
            self.CoordError_x += len(congruityVar.string)

            if i.typeToken_args == ValuesTokenClass.NumbersDigits_var:
                #print(congruityVar.string, 0)
                if congruityVar.string.isdigit() or (congruityVar.string[0]=="0" and congruityVar.string[1]=="x"):
                    return BoxTokens_Class(i.typeToken_args, int(congruityVar.string, 0))
                else:
                    return BoxTokens_Class(i.typeToken_args, float(congruityVar.string))
            return BoxTokens_Class(i.typeToken_args, congruityVar.string)
        return None

    def checkVar_Func(self) -> bool:
        return self.CoordError_x < len(self.currentLine_var)

    def JumpWord_func(self):
        while self.checkVar_Func() and (self.currentLine_var[self.CoordError_x] in self.ListSkipSymvol):
            self.CoordError_x += 1


class Parser:
    countargs = 0
    iter_oper = 0
    count_cmp = 0
    count_tern = 0
    Asm_result_text_str = ""
    Name_of_Procedure = []
    VariableName = []

    def __init__(self, analyzer: FindTokens_Class):
        self.AnalyzeLexem = FindTokens_Class
        self.BegAnalyzToken_Class()


    def BegAnalyzToken_Class(self):
        for i in range(len(self.AnalyzeLexem.BasketTokens_list)):
            if self.AnalyzeLexem.BasketTokens_list[i].typesToken_args == 4:
                self.AnalyzeLexem.BasketTokens_list[i].c = int(self.AnalyzeLexem.BasketTokens_list[i].valueTokens_args)
        tokensBox = self.AnalyzeLexem.BasketTokens_list

        self.ErrorPositionVert = 0
        self.ErrorPositionGoriz = 0
        try:

            """Пошук помилок вводу"""
            NotificationError = "Помилка синтаксису!"
            for i in range(len(tokensBox)):
                self.ErrorPositionGoriz = i
                bin_operat_list = ['+', '&', '>>', '|', '/', '<', '^', '>', '%', '!=', '<<', '*', '<=', '>=', '==', "?", ":"]
                un_op_list = ["-", "~", "!"]
                Key_list = ["return", "continue", "break"]
                if tokensBox[i].valueTokens_args in bin_operat_list:
                    NotificationError = "Синтаксична помилка, некоректно вказаний оператор"
                    assert tokensBox[i + 1].valueTokens_args not in bin_operat_list or tokensBox[i + 1].valueTokens_args not in Key_list
                if i > 0:
                    if tokensBox[i].valueTokens_args == "while":
                        NotificationError = "Помилка синтаксису, відсутній символ }"
                        assert tokensBox[i-1].valueTokens_args == "}"
                    if tokensBox[i-1].valueTokens_args == "while":
                        NotificationError = "Помилка синтаксису, відсутній символ ("
                        assert tokensBox[i].valueTokens_args == "("
                        NotificationError = "Помилка синтаксису, відсутній символ )"
                        check = 0
                        for k in tokensBox[i:]:
                            if k.valueTokens_args==")":
                                check = 1
                            if k.valueTokens_args==";":
                                break
                        assert check
                    if tokensBox[i-1].valueTokens_args == "do":
                        NotificationError = "Помилка синтаксису, відсутній символ {"
                        assert tokensBox[i].valueTokens_args == "{"
                    if tokensBox[i].valueTokens_args == "do":
                        NotificationError = "Помилка синтаксису, відсутній символ ;"
                        assert tokensBox[i-1].valueTokens_args == ";"
                    if tokensBox[i].valueTokens_args in bin_operat_list:
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i - 1].valueTokens_args not in Key_list
                    if tokensBox[i].valueTokens_args in bin_operat_list:
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i - 1].valueTokens_args not in bin_operat_list
                    if tokensBox[i-1].valueTokens_args in un_op_list:
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args not in bin_operat_list
                    if tokensBox[i-1].valueTokens_args in un_op_list:
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args != ";"
                    if tokensBox[i-1].valueTokens_args == ")":
                        NotificationError = "Помилка синтаксису, невистачає ;"
                        assert tokensBox[i].valueTokens_args != "}"
                    if tokensBox[i-1].valueTokens_args == "int":
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args != ";"
                    if tokensBox[i-1].valueTokens_args == "int":
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args != "float"
                    if tokensBox[i-1].valueTokens_args in un_op_list:
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args not in bin_operat_list
                    if tokensBox[i-1].valueTokens_args == "int":
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args != "float"
                    if tokensBox[i-1].valueTokens_args == "int":
                        NotificationError = "Помилка синтаксису, некорректний аргумент оператора, або відстуній аргумент"
                        assert tokensBox[i].valueTokens_args != "float"
                    if tokensBox[i].valueTokens_args == "?":
                        NotificationError = "Помилка синтаксису. Відсутня необхідна умова тернарного оператора"
                        check = 0
                        for k in tokensBox[i:]:
                            if k.valueTokens_args == ":":
                                check = 1
                            if k.valueTokens_args == ";":
                                break
                        assert check
                    if tokensBox[i].valueTokens_args == ":":
                        NotificationError = "Помилка синтаксису. Відсутня необхідна умова тернарного оператора"
                        check = 0
                        for k in tokensBox[i:0:-1]:
                            if k.valueTokens_args == "?":
                                check = 1
                            if k.valueTokens_args == ";":
                                break
                        assert check
                    if tokensBox[i].valueTokens_args == "?":
                        NotificationError = "Помилка синтаксису. відсутня умова у тернатрого оператора"
                        assert tokensBox[i-1].valueTokens_args != "="
                    if tokensBox[i].typesToken_args == 4:
                        NotificationError = "Помилка синтаксису"
                        assert tokensBox[i-1].typesToken_args != 4

                    if tokensBox[i].valueTokens_args in ["{", "}", ";"]:
                        self.ErrorPositionVert += 1
                if i > 4:
                    if (tokensBox[i-3].valueTokens_args==";" or tokensBox[i-3].valueTokens_args=="{")  and tokensBox[i-2].typesToken_args == 3 and tokensBox[i-1].valueTokens_args == "=" and tokensBox[i].typesToken_args == 4:
                        NotificationError = "Не вказаний тип змінної"
                        raise TypeError
        except:
            temp_var = 0
            res_txt = ""
            for i in range(len(tokensBox)):
                if i == self.ErrorPositionGoriz:
                    break
                if temp_var == self.ErrorPositionVert:
                    res_txt += str(tokensBox[i].valueTokens_args) + " "
                if tokensBox[i].valueTokens_args == "\n":
                    temp_var += 1
            position_element = len(res_txt) + 1

            print("Помилка: Строка: {}, Положення курсору: {}, Номер символу: {}\033[30m\n".format(
                    self.ErrorPositionVert + 1, self.ErrorPositionGoriz + 1, position_element))
            print("{}\n".format(NotificationError))
            for i in range(len(tokensBox)):

                if i == self.ErrorPositionGoriz:
                    print("\033[31m{}\033[30m".format(tokensBox[i].valueTokens_args), end=" ")
                else:
                    print(tokensBox[i].valueTokens_args, end=" ")
            input()
            raise SystemExit

        self.Asm_result_text_str += self.topAsmCode()
        self.Asm_result_text_str += self.InitializVariableAsmCode(tokensBox)

        skeep = 0
        check = 0
        tempery1 = 0
        for i in range(len(tokensBox)):
            if tokensBox[i].valueTokens_args=="{":
                if skeep == 0 and check == 0:
                    check = 1
                    count = 0
                    while 1:
                        if (tokensBox[i - count].valueTokens_args == "int" or tokensBox[i - count].valueTokens_args == "float") and tokensBox[i-count +1].typesToken_args ==3 and tokensBox[i-count +2].valueTokens_args =="(":
                            tempery1 = i - count
                            break
                        count += 1
                else:
                    skeep += 1
            if tokensBox[i].valueTokens_args=="}":
                if skeep != 0:
                    skeep -= 1
                    continue
                tempery2 = i
                check = 0
                self.Asm_result_text_str += self.AnalyzeFunctional(tokensBox[tempery1:tempery2])

        self.Asm_result_text_str += self.runProc(tokensBox)


    def topAsmCode(self):
        topAsm_str = r""".386
.model flat, stdcall
include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib

"""
        return topAsm_str
    def InitializVariableAsmCode(self, list_tok):
        AsmCode_str = ""
        check = 0
        for i in range(len(list_tok)):
            if i == 0 or i == 1:
                continue
            if (list_tok[i - 2].typesToken_args == 3 and list_tok[i - 1].valueTokens_args == "="):
                self.VariableName.append(list_tok[i - 2].valueTokens_args)
            if list_tok[i-2].valueTokens_args == "int" and list_tok[i-1].typesToken_args == 3 and list_tok[i].valueTokens_args == "(":
                check = 1
            if check == 1 and list_tok[i].valueTokens_args == ")":
                check = 0
            if check == 1 and list_tok[i].typesToken_args == 3:
                self.VariableName.append(list_tok[i].valueTokens_args)


        self.VariableName = list(set(self.VariableName))
        AsmCode_str += ".data\n\n"
        for i in self.VariableName:
            AsmCode_str += "{} dd ?\n".format(i)
        AsmCode_str += ".code\n\n"
        return AsmCode_str
    def AnalyzeFunctional(self, list_temp):
        resCodeAsm_str = ""
        ProcName_str = None

        # определение заголовка функции
        check = 0
        args_list = []
        for i in range(len(list_temp)):
            if i==0:
                continue
            if (list_temp[i-1].typesToken_args==13 or list_temp[i-1].typesToken_args==14) and list_temp[i].typesToken_args==3 and list_temp[i+1].valueTokens_args=="(":
                ProcName_str = list_temp[i].valueTokens_args
                resCodeAsm_str += "{} proc\n".format(ProcName_str)
                resCodeAsm_str += "push ebp;\nmov ebp, esp;\n"
                check = 1
            if check == 1 and list_temp[i+2].valueTokens_args == ")":
                check = 0
                self.count_args = len(args_list)
                iter = 4 + 4*self.count_args
                for k in args_list:
                    resCodeAsm_str += "mov eax, dword ptr[ebp + {}];\nmov {}, eax;\n".format(iter, k)
                    iter -= 4
                args_list = []
            if check == 1 and list_temp[i+2].typesToken_args == 3:
                args_list.append(list_temp[i+2].valueTokens_args)
        if ProcName_str==None:
            return ""


        # обработка тела
        while_check = 0
        ind = 0
        check = False
        for i in range(len(list_temp)):
            if list_temp[i].valueTokens_args == "do":
                resCodeAsm_str += "body_do_while:\n"
                while_check = 1
            if list_temp[i].valueTokens_args == "while":
                if list_temp[i+1].valueTokens_args == "(":
                    index_if_while = i + 2
            if list_temp[i].valueTokens_args == "continue" and while_check:
                resCodeAsm_str += "jmp conditional;\n"
            if list_temp[i].valueTokens_args == "break" and while_check:
                resCodeAsm_str += "jmp exit_while;\n"
            if list_temp[i].valueTokens_args == ")" and while_check:
                while_check = 0
                resCodeAsm_str += "conditional:\n"
                resCodeAsm_str += self.exprProcessing(list_temp[index_if_while: i], "")
                resCodeAsm_str += "pop eax;\ncmp eax, 0\njne body_do_while\nexit_while:\n"
            if list_temp[i].valueTokens_args=="=":
                name_var = list_temp[i-1].valueTokens_args
                check = True
                ind = i
            if list_temp[i].valueTokens_args == ";" and check:
                resCodeAsm_str += self.exprProcessing(list_temp[ind + 1: i], "")
                resCodeAsm_str += "\npop eax\nmov {}, eax\n".format(name_var, list_temp[i - 1].valueTokens_args)
                check = False


        # определение возврата функции
        ind = 0
        contrlVar = 0
        for i in range(len(list_temp)):
            if list_temp[i].typesToken_args==2:
                ind = i
                contrlVar = 1
                continue
            if list_temp[i].valueTokens_args == ";" and contrlVar:
                resCodeAsm_str += self.exprProcessing(list_temp[ind + 1: i], "")
                if self.count_args>0:
                    resCodeAsm_str += ("mov esp, ebp;\npop ebp\nret {}\n{} endp\n\n".format(self.count_args*4, ProcName_str))
                else:
                    resCodeAsm_str += ("mov esp, ebp;\npop ebp\nret\n{} endp\n\n".format(ProcName_str))
                contrlVar = 0
                ind = 0
                break

        return resCodeAsm_str

    def runProc(self,list_tok):
        text =""
        text += "\nstart:\n"

        text += "invoke main;\n"
        text += "invoke ExitProcess, eax;\n\nend start;"
        return text

    def exprProcessing(self, listLexems, textRes_str):
        unarMin2_list = ["-"]
        notLogicAndBit3_list = ["!", "~", "++"]
        mult_div4_list = ["/", "*", "%"]
        plusAndminus_list = ["-", "+"]
        bitRandL_list = ["<<", ">>"]
        bitAnd_list = ["&"]
        bitXor_list = ["^"]
        bitOr_list = ["|"]
        cmp_list = ["==", "!=", ">", ">=", "<", "<="]
        try:
            if listLexems[0].valueTokens_args == "(" and listLexems[-1].valueTokens_args == ")":
                listLexems = listLexems[1:-1]
        except:
            pass
        if len(listLexems) == 1:
            return "mov eax, {};\npush eax;\n".format(listLexems[0].valueTokens_args)
        for i in range(len(listLexems) - 1, -1, -1):
                if listLexems[i].valueTokens_args=="?":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\npop eax;\ncmp eax, 1;\nje iftrue{};\njmp iffalse{};\n{}\n\n".format(temp1,self.count_tern, self.count_tern, temp2, self.count_tern)
                    self.count_tern += 1
                    return textRes_str
        for i in range(len(listLexems) - 1, -1, -1):
                if listLexems[i].valueTokens_args==":":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "\niftrue{}:\n{}\njmp Exitif{}\niffalse{}:\n{}\nExitif{}:\n".format(self.count_tern, temp1, self.count_tern, self.count_tern, temp2, self.count_tern)
                    return textRes_str
        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in cmp_list:
                if listLexems[i].valueTokens_args=="==":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\n{}\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\nje skipeqeq{}\nmov eax, 0\nskipeqeq{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1

                    return textRes_str
                if listLexems[i].valueTokens_args=="!=":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\n{}\n\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\njne skipnoteq{}\nmov eax, 0\nskipnoteq{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1
                    return textRes_str
                if listLexems[i].valueTokens_args=="<=":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\n\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\njle skiplesseq{}\nmov eax, 0\nskiplesseq{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1
                    return textRes_str
                if listLexems[i].valueTokens_args=="<":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\n{}\n\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\njl skipless{}\nmov eax, 0\nskipless{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1
                    return textRes_str
                if listLexems[i].valueTokens_args==">=":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\n{}\n\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\njge skipmoreeq{}\nmov eax, 0\nskipmoreeq{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1

                    return textRes_str
                if listLexems[i].valueTokens_args==">":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)
                    textRes_str += "{}\n{}\n\npop ebx\npop eax;\ncmp eax, ebx; " \
                                   "\nmov eax, 1\njg skipmore{}\nmov eax, 0\nskipmore{}:\npush eax\n".format(temp1, temp2, self.count_cmp, self.count_cmp)
                    self.count_cmp += 1
                    return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in bitOr_list:
                temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                textRes_str += "{}\n{}\npop ebx;\npop eax;\nor eax, ebx;" \
                            "\npush eax;\n\n".format(temp1, temp2)
                return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in bitXor_list:
                temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                textRes_str += "{}\n{}\npop ebx;\npop eax;\nxor eax, ebx;" \
                            "\npush eax;\n\n".format(temp1, temp2)
                return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in bitAnd_list:
                temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                textRes_str += "{}\n{}\npop ebx;\npop eax;\nand eax, ebx;" \
                            "\npush eax;\n\n".format(temp1, temp2)
                return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in bitRandL_list:
                if listLexems[i].valueTokens_args=="<<":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\nshr eax, ebx;" \
                                "\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str

                if listLexems[i].valueTokens_args == "<<":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\nshl eax, ebx;" \
                                   "\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in plusAndminus_list:
                if listLexems[i].valueTokens_args == "+":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\nadd eax, ebx;" \
                                   "\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str

                if listLexems[i].valueTokens_args == "-":
                    if len(listLexems)<=2:
                        break
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\nsub eax, ebx;" \
                                   "\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in mult_div4_list:
                if listLexems[i].valueTokens_args == "/":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\ncdq;\nidiv " \
                            "ebx;\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str
                if listLexems[i].valueTokens_args == "%":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\ncdq;\nidiv " \
                            "ebx;\nmov eax, edx;\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str
                if listLexems[i].valueTokens_args == "*":
                    temp1 = self.exprProcessing(listLexems[:i], textRes_str)
                    temp2 = self.exprProcessing(listLexems[i + 1:], textRes_str)

                    textRes_str += "{}\n{}\npop ebx;\npop eax;\n\nimul eax, ebx;\npush eax;\n\n".format(temp1, temp2)
                    return textRes_str
                    return textRes_str
        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in unarMin2_list:
                if listLexems[i].valueTokens_args == "-":
                    temp = self.exprProcessing(listLexems[i + 1:len(listLexems)], textRes_str)
                    textRes_str += "{}\npop eax;\nneg eax;\npush eax\n\n".format(temp)
                    return textRes_str

        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].valueTokens_args in notLogicAndBit3_list:
                if listLexems[i].valueTokens_args == "!":
                    temp = self.exprProcessing(listLexems[i + 1:len(listLexems)], textRes_str)
                    textRes_str += "{}\npop eax;\ncmp eax, 0;\njne bNot{};\nmov eax, 1\njmp eNot{}\nbNot{}:\nmov eax, 0\neNot{}:\npush eax\n".format(temp, self.iter_oper, self.iter_oper, self.iter_oper, self.iter_oper)
                    self.iter_oper += 1
                    return textRes_str
                elif listLexems[i].valueTokens_args == "~":
                    temp = self.exprProcessing(listLexems[i + 1:len(listLexems)], textRes_str)
                    textRes_str += "{}\npop eax;\nnot eax;\npush eax\n".format(temp, textRes_str)
                    return textRes_str
                elif listLexems[i].valueTokens_args == "++":
                    temp = self.exprProcessing(listLexems[0:i], textRes_str)
                    textRes_str += "\n{}\npop eax;\nadd eax, 1;\npush eax\n".format(temp, textRes_str)
                    return textRes_str
        for i in range(len(listLexems) - 1, -1, -1):
            if listLexems[i].typesToken_args == 3:
                if i+1==len(listLexems):
                    break
                if listLexems[i+1].valueTokens_args == "(":
                    start = i + 2
                    finish = i + 2
                    for k in listLexems[i+2:]:
                        if k.valueTokens_args == ",":
                            textRes_str += "{}\n".format(self.exprProcessing(listLexems[start:finish], ""))
                            start = finish + 1
                        if k.valueTokens_args == ")":
                            textRes_str += "{}\n".format(self.exprProcessing(listLexems[start:finish], ""))
                            break
                        finish += 1
                    textRes_str += "invoke {};\n".format(listLexems[i].valueTokens_args)
                    return textRes_str
        return ""



text_var = open('InputProgram.txt', 'r')
cplusplustext = text_var.read()
exempLexer = FindTokens_Class(cplusplustext)

for i in exempLexer.BasketTokens_list:
    print(i, end="")

b = Parser(exempLexer)
print(b.Asm_result_text_str)

text_var = open('OutputProgram.asm', 'w')
text_var.write(b.Asm_result_text_str)
text_var.close()

input()
