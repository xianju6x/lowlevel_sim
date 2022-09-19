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

            ##### microcode ##### 
            s_b = ! (NEXT[0] and NEXT[1] and NEXT[2] and NEXT[3] ... NEXT[7]) or fault_pending 
            s_a = ! (NEXT[0] or NEXT[1]) and ... !(NEXT[6] or NEXT[7]) and !fault_pending and branch 

            mpc_select = (0x2 and s_b << 1) or (s_a and 0x1)
            if mpc_select == 0x0:   # NEXT = 0xFF & fault_pending = 0 & branch = 0  
                MPC = encoder or s_b << 8 # branch, if branch = 1, execute the instruction, if branch = 0, MPC = 0x00(halt,fetch), execute next instruction
            elif mpc_select == 0x1: # NEXT = 0xFF
                MPC = R_IR or s_b << 8
            elif mpc_select = 0x2: # NEXT = 0x00
                MPC = encoder or s_b << 8  # interrupt(sync,at the end of an instruction) or fault(async, at any phase of an instruction)
            elif mpc_select = 0x3: # NEXT = 0x01 ~ 0xFE
                MPC = NEXT or s_b << 8

            microcode_rom0[MPC] ==> microcode0
            microcode_rom1[MPC] ==> microcode1
            microcode_rom2[MPC] ==> microcode2
            microcode_rom3[MPC] ==> microcode3
            microcode_rom4[MPC] ==> microcode4
            
            NEXT = microcode0
            
            ######################################
            decode
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
