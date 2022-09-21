class Microcode:

    def squence(self):

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
        
        
