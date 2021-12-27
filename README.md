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

Check to see if we can perform simultaneous IO and cached ops
    

# File Format

├── README.md 
    Describes each test idea and the generation of ASM using Python 3.
    
├── uatg_dcache_load_nl.py 

    Generates ASM to fill the Data Cache by performing consecutive loads at different address locations, jumps to the next line in each iteration
    
    _Code Description_
     1)Perform a fence operation to clear out the data cache subsystem and the fill buffer.
     2)Perform several load operations to fill up the cache
     3)In each iteration, we visit the next way in the same set.
     4)Once all the ways in a set are touched, we visit the next set.
     The total number of iterations is parameterized based on YAML input
     
   
├── uatg_dcache_load_ns.py 

     Generates ASM to fill the Data Cache by performing consecutive loads at different address locations, jumps to the next line in each iteration.
     
     _Code Description_
     1)Perform a fence operation to clear out the data cache subsystem and the fill buffer.
     2)Load some data into a temporary register and perform several load operations to fill up the cache.
     3)Each loop in ASM has an unconditional jump back to that label, a branch takes us out of the loop.
     4)Each iteration, we visit the next set.
     The total number of iterations is parameterized based on YAML input.
    
├── uatg_dcache_store_nl.py 

    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations,jumps to the next set in each iteration.

     _Code Description_ 
     1)Perform a fence operation to clear out the data cache subsystem and the fill buffer.
     2)In each iteration, we visit the next way in the same set.
     3)Once all the ways in a set are touched, we visit the next set.
     The total number of iterations is parameterized based on YAML input.
    
├── uatg_dcache_store_ns.py 

    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations, jumps to the next line in each iteration.

     _Code Description_ 
     1)Perform a fence operation to clear out the data cache subsystem and the fill buffer.
     2)Load some data into a temporary register and perform numerous store operations to fill up the cache.
     3)Each loop in ASM has an unconditional jump back to that label, a branch takes us out of the loop.
     4)Each iteration, we visit the next set.
     The total number of iterations is parameterized based on YAML input.
    
