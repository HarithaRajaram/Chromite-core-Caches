# Chromite-core-Caches
This repository contains the python scripts to generate RISC-V Assembly for testing the Cache subsystem in the Chromite Core by InCore Semiconductors.
This repository can be initialised as a submodule in chromite_uatg_tests.

File Format

├── README.md 
    Describes each test idea and the generation of ASM using Python 3.
├── uatg_dcache_fill_1.py 
    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations, jumps to the next set in each iteration.
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
