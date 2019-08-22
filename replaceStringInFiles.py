
import os
path = 'F:\\academics\Projects\Automatic Question Generation'
folder = os.fsencode(path)
for filename in os.listdir(folder):
    filename = filename.decode("utf-8")
    if filename.endswith(".txt"):
        fin = open(filename, "rt")
        data = fin.read()
        data = data.replace('_array00_', '_master-column-header_')
        data = data.replace('_master-column-header-singluar_', '_master-column-header-singular_')
        data = data.replace('_array00-plural_', '_master-column-header-plural_')
        fin.close()
        
        fin = open(filename, "wt")
        fin.write(data)
        fin.close()





path = 'F:\\academics\Projects\Automatic Question Generation\\templates'
folder = os.fsencode(path)
for filename in os.listdir(folder):
    filename = filename.decode("utf-8")
    print(filename)
    if filename.endswith(".txt"):
        fin = open(filename, "rt")
        data = fin.read()
        data = data.replace('_array00_', '_master-column-header_')
        data = data.replace('_array00-singluar_', '_master-column-header-singular_')
        data = data.replace('_array00-plural_', '_master-column-header-plural_')
        fin.close()
        
        fin = open(filename, "wt")
        fin.write(data)
        fin.close()
