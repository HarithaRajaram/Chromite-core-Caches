#Attributed to Gitlab repo on subsystem caches by Neel gala and caches code by Vishwa ,BK Karthik ,Ayush on github
# Chromite-core-Caches
This repository contains the python codes to generate RISC-V Assembly for testing the Cache subsystem of the Chromite Core by InCore Semiconductors.
This repository can be initialised as a submodule in chromite_uatg_tests.

# Test Description is as follows
Fill the cache completely based on the size mentioned in the core64.yaml input.

Try to fill the fill-buffer completely.

Perform all possible types of load/store access (byte, hword, word, dword)

Perform a load/store hit in the RAMS

Perform a load/store hit in the Fill-buffer

Perform a store-to-load forwarding scenario from the store-buffer

Perform a replacement on all sets.

Check if fence and fence.iwork properly

    

# File Format
Keeping in mind the structure of the index.yaml file the naming of the files is presented as follows.

├── README.md 
    Describes each test idea and the generation of ASM using Python 3.
    
├── uatg_cache_dcache_load_nl.py 

    Generates ASM to fill the Data Cache by performing consecutive loads in consecutive address locations and jumps to the next line in each iteration
    
    _Code Description_
    1)Check every consecutive address locations for data ,if an address is empty fill it with some data until the end of the line in each iteration and moves on        to the next line.
     
   
├── uatg_cache_dcache_load_ns.py 

     Generates ASM to fill the Data Cache by performing consecutive loads at consecutive address locations, jumps to the next set in each iteration.
     
     _Code Description_
     1)Check every consecutive address locations and performs consecutive loads until the end of the line in each iteration and moves on
         to the next set.
    
├── uatg_cache_dcache_store_nl.py 

    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations,jumps to the next set in each iteration.

     _Code Description_ 
     1)Check every consecutive address locations and performs consecutive stores until the end of the line in each iteration and moves on
         to the next line.
     
    
├── uatg_cache_dcache_store_ns.py 

    Generates ASM to fill the Data Cache by performing consecutive stores at different address locations, jumps to the next line in each iteration.

     _Code Description_ 
     1))Check every consecutive address locations and performs consecutive stores until the end of the line in each iteration and moves on
         to the next set.
