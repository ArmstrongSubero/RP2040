title= "inlineC.py" # http://docs.micropython.org/en/v1.9.3/pyboard/pyboard/tutorial/assembler.html
from rp2 import *
from machine import *
from time import *
import uarray

led= Pin(25,Pin.OUT)
led(1)
#sleep(2)
led(0)


@micropython.asm_thumb # works
def fun():
    mov(r0, 42) # movw hat nicht funktioniert
    add(r0, r0, 7) # nur kleine Werte <8

@micropython.asm_thumb # works
def asm_add(r0, r1):
    add(r0, r0, r1)

regdata = uarray.array('i',[
                0xd0000000 + 0x010, # 0 SIO OUT
                0xd0000000 + 0x018, # 4 SIO OUT_CLR
                0xd0000000 + 0x014, # 8 SIO OUT_SET
                1<<25 # 12 LED 
                ])

@micropython.asm_thumb
def led_peek(r0):
    mov(r1,r0)
    ldr(r2,[r1,0]) # register adress
    ldr(r0,[r2,0])

    
@micropython.asm_thumb
def led_on(r0):
    mov(r1,r0)
    ldr(r2,[r1,8]) # register address
    ldr(r0,[r1,12]) # mask data
    str(r0,[r2,0])

@micropython.asm_thumb
def led_off(r0):
    mov(r1,r0)
    ldr(r2,[r1,4]) # register address
    ldr(r0,[r1,12]) # mask data
    str(r0,[r2,0])


while True:
    print(title, fun(), asm_add(20_000_000,30))
    print(led_peek(regdata))
    print(led_on(regdata))
    print(led_peek(regdata))
    sleep(2)
    print(led_off(regdata))
    print(led_peek(regdata))
    sleep(2)

