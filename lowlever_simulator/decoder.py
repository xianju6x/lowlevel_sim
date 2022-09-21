
latch_table0 = {
        0x00: {RL_PC:0,RL_PC=0,RL_DP=0,RL_SP=0;RL_A_LO=0,RL_B_LO=0,RL_},
        0x01: {},
        0x10: {},
        0x11: {}
    }

latch_table1 = {
        0x00: {},
        0x01: {},
        0x10: {},
        0x11: {}
    }

def latch():
    if LATCH[0] and ... LATCH[4] == 1:
        latch_tmp = LATCH[0:4]
    else == 0:
        latch_tmp = IR[5:7]
        latch_tmp[4y] = 0
    
    RL_C = 0
    RL_PC = 0
    RL_DP = 0
    ...
    RL_MDR = 0
    RL_PTB = 0
    if latch_tmp[4y] == 0:
        if FAULT_PENDING == 0 and CLKS = 1:
            if latch_tmp[0:3] = 0x0:
                
            elif latch_tmp[0:3] = 0x1:
                RL_C = 1
            elif latch_tmp[0:3] = 0x2:
                RL_PC = 1
            elif latch_tmp[0:3] = 0x3:
            elif latch_tmp[0:3] = 0x4:
            elif latch_tmp[0:3] = 0x5:
            elif latch_tmp[0:3] = 0x6:
            elif latch_tmp[0:3] = 0x7:

    elif latch_tmp[4y] == 1: 
        if FAULT_PENDING == 0 and CLKS = 1:
            if latch_tmp[0:3] = 0x0:
                RL_MDR = 1
            elif latch_tmp[0:3] = 0x1:
                RL_PTB = 1

    




def el():
    pass

def decode_mem_sig():
    pass 

def decode():
    latch()
    el()
    decode_mem_sig()
