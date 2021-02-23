# -*- coding: utf-8 -*-

import sys
import os
import xml.etree.ElementTree as ET

class My_class(object):
    def __init__(self, directory_path):
        self.directory_path = directory_path
    
    def get_permissions(self):
        self.my_dic={}
        for dirpath, dirnames, self.files in os.walk(self.directory_path):
            for file_name in self.files:
                # build filename 
                file_path = dirpath + "/" + file_name

                #get file xml
                root = ET.parse(file_path).getroot()

                #get permissions from the xml file
                permissions = root.findall("uses-permission")
                self.build_dictionary(file_name,permissions)
                
    
    def build_dictionary(self, file_name, permissions):        
        #build array of permissions
        permissions_attributes = []
        for perm in permissions:
            for att in perm.attrib:
                permissions_attributes.append(perm.attrib[att]) 

        #format directory name
        begin = file_name.index('t_') + 2
        end = file_name.index('.xml')   
        self.my_dic[file_name[begin:end]] = permissions_attributes

    def get_unique_permission(self):
        self.unique_dic = {}
        for key in self.my_dic.keys():
            temp_dic = self.my_dic.copy()
            temp_dic.pop(key)
            self.unique_dic[key] = list(set(self.my_dic[key]).difference(*temp_dic.values()))

    def get_common_permissions(self):
        values = self.my_dic.values()
        self.common = set(values[0]).intersection(*values[1:])

    def print_header(self,header_phrase):
        print("===================\n")
        print(header_phrase)
        print("\n===================\n")
    
    def print_permissions_list(self):
        self.print_header("Permissões por APK")
        for key, value in self.my_dic.items():
            print(key + " : " + str(value) + "\n")


    def print_unique_permissions_list(self):
        self.print_header("Permissões únicas por APK")
        for key, value in self.unique_dic.items():
            print(key + " : " + str(value) + "\n")

    def print_common_permissions_list(self):
        self.print_header("Permissões comuns das APKs")
        print(list(self.common))
        print("\n")



if __name__=="__main__":
    try:
        directory_path = sys.argv[1]
    except IndexError:
        print "Nenhum arquivo foi identificado"
        sys.exit(1)
    
    handler = My_class(directory_path)
    handler.get_permissions()
    handler.get_unique_permission()
    handler.get_common_permissions()
    handler.print_permissions_list()
    handler.print_unique_permissions_list()
    handler.print_common_permissions_list()