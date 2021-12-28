#Attributed to Gitlab repo on subsystem caches by Neel gala and caches code by Vishwa ,BK Karthik ,Ayush on github

from yapsy.IPlugin import IPlugin
from ruamel.yaml import YAML
import uatg.regex_formats as rf
from typing import Dict, Union, Any, List
import re
import os
import random

class uatg_dcache_strore_nl(IPlugin):
    def init(self):
        super().init()
        self._sets = 64
        self._word_size = 8
        self._block_size = 8
        self._ways = 4
    
    def execute(self, core_yaml, isa_yaml):
        _dcache_dict = core_yaml['dcache_configuration']
        _dcache_en = _dcache_dict['instantiate']
        self._sets = _dcache_dict['sets']
        self._word_size = _dcache_dict['word_size']
        self._block_size = _dcache_dict['block_size']
        self._ways = _dcache_dict['ways']

    def check_log(self, log_file_path, reports_dir):
        f = open(log_file_path, "r")
        log_file = f.read()
        f.close()

        test_report = {
                "dcache_strore_nl_report": {
                    'Doc': "ASM should have filled the cache of size {0}. This report verifies that.".format(self._sets * self._word_size * self._block_size * self._ways / 8)
                    'Execution status': ''
                    }
                }

    def generate_covergroups(self, config_file):
        ''

    def generate_asm(self) -> List[Dict[str, str]]:

        asm_data = random.randrange(16**8)

        for i in range (self._block_size * self._sets * self._ways*2):
            asm_data += f'\n\tlw t0, 0(t1)\n\taddi t1, t1, {self._sets*self._block_size*self._word_size}\n'
        
    	asm_end = "end:\n\tnop\n"
  

        return [{
            'asm_code': asm,
            'asm_data': asm_data,
            'asm_sig': '',
            'compile_macros': compile_macros
        }]
