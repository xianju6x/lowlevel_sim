from decoder import decode

LOW = 0
RAISE = 1
HIGH = 2
FALL = 3

s_clks = LOW
s_clkm = LOW
s_rd = LOW

is_running == True

class Registers:
    R_A
    R_B
    R_C
    R_DP
    R_SP
    R_SSP
    R_PC
    R_PTB
    
    def set_r_a(self):
        pass

def run():

    while is_running:

        if s_clks  == RAISE and s_clkm == FALL:

            s_clkm = FALL
            s_clks = HIGH

        elif s_clks == HIGH and s_clkm == LOW:
            latch[0:3] ==> L_singanls
            
            #### latch register ####
            Z_BUS ==> R_A | R_B | R_C | R_DP | R_SP | R_SSP | R_MAR
            Z_BUS ==> MAR
            Z_BUS | D_BUS ==> MDR
    
            ### page table ###
            L_BUS ==> R_PTB
            R_PTB + MAR ==> PAGE_TABLE
            if write_page:
                L_BUS ==> PAGE_TABLE[L_BUS+MAR] 

            ### interrupt vector ###
            encoder_tmp ==> encoder

            s_clkm = LOW
            s_clks = FALL
            
        elif s_clks == FALL and s_clkm == RAISE:

            Microcode.squence() 
            ######################################
            decode()
            ######################################
            ##### memory #####
            PAGE_TABLE ==> ADDR_BUS + Faults 
            ADDR_BUS ==> memory | device
            if _RW:
                memory[ADDR_BUS] | device[ADDR_BUS] ==> DBUS
            if _WR:
                D_BUS ==> memory[ADDR_BUS] | device[ADDR_BUS]

            ##### register #####
            R_A | R_B | R_C | R_DP | R_SP | R_SSP | R_MAR ==> L_BUS
            MAR ==> L_BUS
            microcode[15:16] ==> IMM
            IMM ==> R_BUS
            MDR ==> L_BUS | R_BUS | D_BUS
            
            ##### alu #####
            R_BUS + L_BUS ==> ALU ==> Z_BUS + Status
            Status + Faults ==> MSW
            MSW ==> L_BUS
            
            ##### IR ######
            if inst == RAISE:
                D_BUS ==> R_IR

            ##### tpc #####
            R_TPC ==> L_BUS
            L_BUS ==> R_TPC
            
            ##### interrupt #####
            IVEC_base ==> encoder_tmp

            s_clkm = RAISE
            s_clks = LOW

        elif s_clks == LOW and s_clkm == HIGH:

            s_clkm = HIGH
            s_clks = RAISE
