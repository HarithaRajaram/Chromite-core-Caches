#Attributed to Gitlab repo on subsystem caches by Neel gala and caches code by Vishwa ,BK Karthik ,Ayush on github
from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import Dict, Union, Any, List
import re
import os
import random

class uatg_cache_dcache_fill(IPlugin):
    def __init__(self):
        super().__init__()
        self._sets = 64
        self._word_size = 8
        self._block_size = 8
        self._ways = 4
    
    def execute(self,core_yaml,isa_yaml):
        	d_cache=core_yaml['dcache_configuration']
        	d_cache_en=d_cache['instantiate']
        	self.sets=d_cache['sets']
        	self.word_size=d_cache['word_size']
        	self.block_size=d_cache['block_size']
        	self.ways=d_cache['ways']
          
    def generate_asm(self) -> List[Dict[str, str]]:
        asm+='fillc:'
        for i in range(self._cache_size):
	        asm+=f'\n\tlw t0, 0(t1)\n\taddi t1, t1, {self._sets*self._block_size*self._word_size}\n'
  
  
  return [{
            'asm_code': asm,
            'asm_data': asm_data,
            'asm_sig': '',
            'compile_macros': []
        }]

    def check_log(self, log_file_path, reports_dir):
        return None

    def generate_covergroups(self, config_file):
        return ''

