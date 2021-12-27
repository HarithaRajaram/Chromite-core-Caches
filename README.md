# Chromite-core-Caches
This repository contains the python scripts to generate RISC-V Assembly for testing the Cache subsystem of the Chromite Core by InCore Semiconductors.
This repository can be initialised as a submodule in chromite_uatg_tests.

# Test Description is as follows
Fill the cache completely based on the size mentioned in the core64.yaml input.
Try to fill the fill-buffer completely.
Perform cache line thrashing
Perform cache set thrashing
Perform all possible types of load/store access (byte, hword, word, dword)
Perform a load/store hit in the RAMS
Perform a load/store hit in the Fill-buffer
Perform an 10 op
Perform a store-to-load forwarding scenario from the store-buffer
Perform a replacement on all sets.
Check if fence and fence.iwork properly
Check if performance counters are correctly incremented.
Check to see if we can perform simultaneous io and cached ops
    

File Format

├── README.md 
    Describes each test idea and the generation of ASM using Python 3.
    
├── uatg_dcache_fill_1.py 
    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations,jumps to the next set in each iteration.
    
├── uatg_dcache_fill_2.py 
    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations, jumps to the next line in each iteration.
    
├── uatg_dcache_fill_3.py 
    Generates ASM to fill the Data Cache by performing consecutive loads at different address locations, jumps to the next set in each iteration.
    
├── uatg_dcache_fill_4.py 
    Generates ASM to fill the Data Cache by performing consecutive loads at different address locations, jumps to the next line in each iteration.
    
├── uatg_dcache_fill_buffer_1.py 
    Generates ASM to fill the Fill Buffer post filling the Data Cache completely. Performs consecutive stores.
    
├── uatg_dcache_fill_buffer_2.py 
    Generates ASM to fill the Fill Buffer post filling the Data Cache completely. Performs consecutive loads.
    
├── uatg_dcache_line_thrashing.py 
    Generates ASM to perform Cache Line Thrashing.
    
├── uatg_dcache_load_store.py 
    Generates ASM to perform all types of load and store operations.
    
└── uatg_dcache_set_thrashing.py 
    Generates ASM to perform Cache Set Thrashing.
    
   
