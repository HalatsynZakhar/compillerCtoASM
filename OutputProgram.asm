.386
.model flat, stdcall
include \masm32\include\kernel32.inc
include \masm32\include\user32.inc
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\user32.lib

.data

b dd ?
operation dd ?
a dd ?
result dd ?
.code

calculator proc
push ebp;
mov ebp, esp;
mov eax, dword ptr[ebp + 16];
mov a, eax;
mov eax, dword ptr[ebp + 12];
mov operation, eax;
mov eax, dword ptr[ebp + 8];
mov b, eax;
mov eax, 1;
push eax;

pop eax;
neg eax;
push eax


pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 1;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq0
mov eax, 0
skipeqeq0:
push eax

pop eax;
cmp eax, 1;
je iftrue0;
jmp iffalse0;

iftrue0:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
and eax, ebx;
push eax;


jmp Exitif0
iffalse0:
mov eax, result;
push eax;

Exitif0:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 2;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq1
mov eax, 0
skipeqeq1:
push eax

pop eax;
cmp eax, 1;
je iftrue1;
jmp iffalse1;

iftrue1:
mov eax, 10;
push eax;

jmp Exitif1
iffalse1:
mov eax, result;
push eax;

Exitif1:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 3;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq2
mov eax, 0
skipeqeq2:
push eax

pop eax;
cmp eax, 1;
je iftrue2;
jmp iffalse2;

iftrue2:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
xor eax, ebx;
push eax;


jmp Exitif2
iffalse2:
mov eax, result;
push eax;

Exitif2:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 4;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq3
mov eax, 0
skipeqeq3:
push eax

pop eax;
cmp eax, 1;
je iftrue3;
jmp iffalse3;

iftrue3:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
cdq;
idiv ebx;
push eax;


jmp Exitif3
iffalse3:
mov eax, result;
push eax;

Exitif3:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 5;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq4
mov eax, 0
skipeqeq4:
push eax

pop eax;
cmp eax, 1;
je iftrue4;
jmp iffalse4;

iftrue4:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
cdq;
idiv ebx;
mov eax, edx;
push eax;


jmp Exitif4
iffalse4:
mov eax, result;
push eax;

Exitif4:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 6;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq5
mov eax, 0
skipeqeq5:
push eax

pop eax;
cmp eax, 1;
je iftrue5;
jmp iffalse5;

iftrue5:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;

imul eax, ebx;
push eax;


jmp Exitif5
iffalse5:
mov eax, result;
push eax;

Exitif5:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 7;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq6
mov eax, 0
skipeqeq6:
push eax

pop eax;
cmp eax, 1;
je iftrue6;
jmp iffalse6;

iftrue6:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
add eax, ebx;
push eax;


jmp Exitif6
iffalse6:
mov eax, result;
push eax;

Exitif6:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 8;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq7
mov eax, 0
skipeqeq7:
push eax

pop eax;
cmp eax, 1;
je iftrue7;
jmp iffalse7;

iftrue7:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx;
pop eax;
sub eax, ebx;
push eax;


jmp Exitif7
iffalse7:
mov eax, result;
push eax;

Exitif7:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 9;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq8
mov eax, 0
skipeqeq8:
push eax

pop eax;
cmp eax, 1;
je iftrue8;
jmp iffalse8;

iftrue8:
mov eax, a;
push eax;

mov eax, b;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq9
mov eax, 0
skipeqeq9:
push eax

jmp Exitif8
iffalse8:
mov eax, result;
push eax;

Exitif8:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 10;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq10
mov eax, 0
skipeqeq10:
push eax

pop eax;
cmp eax, 1;
je iftrue9;
jmp iffalse9;

iftrue9:
mov eax, a;
push eax;

mov eax, b;
push eax;


pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
jne skipnoteq11
mov eax, 0
skipnoteq11:
push eax

jmp Exitif9
iffalse9:
mov eax, result;
push eax;

Exitif9:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 11;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq12
mov eax, 0
skipeqeq12:
push eax

pop eax;
cmp eax, 1;
je iftrue10;
jmp iffalse10;

iftrue10:
mov eax, a;
push eax;

mov eax, b;
push eax;


pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
jl skipless13
mov eax, 0
skipless13:
push eax

jmp Exitif10
iffalse10:
mov eax, result;
push eax;

Exitif10:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 12;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq14
mov eax, 0
skipeqeq14:
push eax

pop eax;
cmp eax, 1;
je iftrue11;
jmp iffalse11;

iftrue11:
mov eax, a;
push eax;

mov eax, b;
push eax;


pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
jle skiplesseq15
mov eax, 0
skiplesseq15:
push eax

jmp Exitif11
iffalse11:
mov eax, result;
push eax;

Exitif11:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 13;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq16
mov eax, 0
skipeqeq16:
push eax

pop eax;
cmp eax, 1;
je iftrue12;
jmp iffalse12;

iftrue12:
mov eax, a;
push eax;

mov eax, b;
push eax;


pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
jg skipmore17
mov eax, 0
skipmore17:
push eax

jmp Exitif12
iffalse12:
mov eax, result;
push eax;

Exitif12:



pop eax
mov result, eax
mov eax, operation;
push eax;

mov eax, 14;
push eax;

pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
je skipeqeq18
mov eax, 0
skipeqeq18:
push eax

pop eax;
cmp eax, 1;
je iftrue13;
jmp iffalse13;

iftrue13:
mov eax, a;
push eax;

mov eax, b;
push eax;


pop ebx
pop eax;
cmp eax, ebx; 
mov eax, 1
jge skipmoreeq19
mov eax, 0
skipmoreeq19:
push eax

jmp Exitif13
iffalse13:
mov eax, result;
push eax;

Exitif13:



pop eax
mov result, eax
mov eax, result;
push eax;
mov esp, ebp;
pop ebp
ret 12
calculator endp

main proc
push ebp;
mov ebp, esp;
mov eax, 5;
push eax;

pop eax
mov a, eax
mov eax, 0;
push eax;

pop eax
mov operation, eax
mov eax, 5;
push eax;

pop eax
mov b, eax
mov eax, a;
push eax;

mov eax, operation;
push eax;

mov eax, b;
push eax;

invoke calculator;
mov esp, ebp;
pop ebp
ret
main endp


start:
invoke main;
invoke ExitProcess, eax;

end start;