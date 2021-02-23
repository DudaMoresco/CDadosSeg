# -*- coding: utf-8 -*-

import pefile
import sys
import os

class My_class(object):
    def __init__(self, directory_path):
        self.directory_path = directory_path
    
    def get_executable_sections(self,pe):
        executable_sections = []
        for section in pe.sections:
            characteristics = getattr(section, 'Characteristics')
            if characteristics & 0x00000020 > 0 or characteristics & 0x20000000 > 0:
                executable_sections.append(section.Name.rstrip('\x00'))
        
        return executable_sections

    def buil_dict(self):
        self.my_dic={}
        for dirpath, dirnames, self.files in os.walk(self.directory_path):
            for file_name in self.files:
                # build filename 
                file_path = dirpath + "/" + file_name
                pe = pefile.PE(file_path)
                self.my_dic[file_name] = self.get_executable_sections(pe)

    def print_header(self,header_phrase):
        print("===================\n")
        print(header_phrase)
        print("\n===================\n")
    
    def print_executable_sections_list(self):
        self.print_header("Seções executáveis por PE")
        for key, value in self.my_dic.items():
            print(key + " : " + str(value) + "\n")


if __name__=="__main__":
    try:
        directory_path = sys.argv[1]
    except IndexError:
        print "Nenhum diretório foi identificado"
        sys.exit(1)
    
    handler = My_class(directory_path)
    handler.buil_dict()
    handler.print_executable_sections_list()
    