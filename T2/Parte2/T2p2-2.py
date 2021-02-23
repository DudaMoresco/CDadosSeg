# -*- coding: utf-8 -*-

import pefile 
import sys

class My_class(object):
    def __init__(self, file1_path, file2_path):
        self.file1_path = file1_path
        self.file2_path = file2_path

    def load_files(self):
        self.file1_pe = pefile.PE(self.file1_path, fast_load=True)
        self.file2_pe = pefile.PE(self.file2_path, fast_load=True)

    def build_sections(self, sections):
        result_sections = []

        for section in sections:
            result_sections.append(section.Name.rstrip('\x00'))

        return result_sections
    
    def get_sections(self):
        self.my_dic = {}

        self.my_dic[self.file1_path] = self.build_sections(self.file1_pe.sections)
        self.my_dic[self.file2_path] = self.build_sections(self.file2_pe.sections)

    def get_unique_sections(self):
        self.unique_dic = {}
        self.unique_dic[self.file1_path] = list(set(self.my_dic[self.file1_path]).difference(self.my_dic[self.file2_path]))
        self.unique_dic[self.file2_path] = list(set(self.my_dic[self.file2_path]).difference(self.my_dic[self.file1_path]))

    def get_common_sections(self):
        values = self.my_dic.values()
        self.common = set(values[0]).intersection(*values[1:])

    def print_header(self,header_phrase):
        print("===================\n")
        print(header_phrase)
        print("\n===================\n")
    
    def print_sections_list(self):
        self.print_header("Seções por PE")
        for key, value in self.my_dic.items():
            print(key + " : " + str(value) + "\n")


    def print_unique_sections_list(self):
        self.print_header("Seções únicas por PE")
        for key, value in self.unique_dic.items():
            print(key + " : " + str(value) + "\n")

    def print_common_sections_list(self):
        self.print_header("Seções comuns das PEs")
        print(list(self.common))
        print("\n")

if __name__=="__main__":
    try:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
    except IndexError:
        print "Dois arquivos devem ser passados"
        sys.exit(1)

    handler = My_class(file1_path, file2_path)
    handler.load_files()
    handler.get_sections()
    handler.get_unique_sections()
    handler.get_common_sections()
    handler.print_sections_list()
    handler.print_unique_sections_list()
    handler.print_common_sections_list()
