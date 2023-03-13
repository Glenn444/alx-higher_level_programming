#!/usr/bin/bash/python3
def new_in_list(my_list, idx, element):
   list_original = my_list.copy()
   if ((idx < 0) or (idx > len(my_list)-1)):
       return list_original
   else:
       new_list = my_list.copy()
       new_list[idx] = element
       return new_list
