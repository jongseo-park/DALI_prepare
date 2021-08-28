import os
import string
import random
import argparse

parser = argparse.ArgumentParser (description="For dali - import")

# Arguments

parser.add_argument("--dalipath", required=True, default=None, help="Path to Dalilite (.../DaliLite.v5/)")
parser.add_argument("--pdbpath", required=False, default=None, help="Set the path to pdb files (.../pdb/)")
parser.add_argument("--datpath", required=False, default=None, help="Set the path to DAT (.../DAT/)")


parser.add_argument("--pdbspath", required=False, default=None, help="Set the path to directory containing folders having pdb files (.../pdbs/)")


parser.add_argument("--renamer", required=False, default="n", help="Renamer (y/n)")
parser.add_argument("--importer", required=False, default="n", help="Importer (y/n)")
parser.add_argument("--listmaker", required=False, default="n", help="listmaker (y/n)")
parser.add_argument("--renamer2", required=False, default="n", help="Renamer2 (y/n)")

args = parser.parse_args()


# Functions

def renamer (pdbpath = args.pdbpath):

    file_list = os.listdir(pdbpath)
    file_list_pdbs = [file for file in file_list if file.endswith(".pdb")]

    a = len (file_list_pdbs)

    string_pool = string.ascii_lowercase + string.digits


    result = []

    for i in range(a+1):
        a1 = random.choice (string_pool)
        a2 = random.choice (string_pool)
        a3 = random.choice (string_pool)
        a4 = random.choice (string_pool)
        a5 = a1 + a2 + a3 + a4
        while a5 in result:
            a1 = random.choice (string_pool)
            a2 = random.choice (string_pool)
            a3 = random.choice (string_pool)
            a4 = random.choice (string_pool)
            a5 = a1 + a2 + a3 + a4
        result.append(a5)

    for i, j in zip (file_list_pdbs, result):
        os.rename (f"{pdbpath}/" + i, f"{pdbpath}/" + j + ".pdb")
        with open (f"{pdbpath}/rename.txt", "a") as list:
            list.write(i)
            list.write("----------")
            list.write(j + "\n")            

    print ("Renamer - Done !")



def importer (dalipath = args.dalipath, pdbpath = args.pdbpath, datpath = args.datpath):

    file_list = os.listdir(pdbpath)
    file_list_pdbs = [file for file in file_list if file.endswith(".pdb")]

    for i in file_list_pdbs:
        a = i.replace (".pdb", "")
        os.system (f"{dalipath}/bin/import.pl --pdbfile {pdbpath}/{i} --pdbid {a} --dat {datpath} --clean")

    print ("Importer - Done !")



def listmaker (dalipath = args.dalipath, datpath = args.datpath):

    file_list = os.listdir (datpath)
    file_list_dats = [file for file in file_list if file.endswith(".dat")]
    
    for i in file_list_dats:
        with open ("./dat.list", "a") as list:
            a = i.replace (".dat", "")
            list.write(a + "\n")

    print ("listmaker - Done !")




def renamer2 (pdbspath = args.pdbspath):

    direc = []

    for i in os.listdir(pdbspath):
        if os.path.isdir (os.path.join(pdbspath, i)):
            direc.append(i)


    r = []

    for i in direc:
        path = f"{pdbspath}/{i}"
        file_list = os.listdir(path)
        file_list_pdbs = [file for file in file_list if file.endswith(".pdb")]
        r.append(file_list_pdbs)

    string_pool = string.ascii_lowercase + string.digits

    total = []

    for x, y in zip (direc, r):
        z = []
        l = len(y)
        for i in range(l+1):
            a1 = random.choice (string_pool)
            a2 = random.choice (string_pool)
            a3 = random.choice (string_pool)
            a4 = random.choice (string_pool)
            a5 = a1 + a2 + a3 + a4
            while a5 in total:
                a1 = random.choice (string_pool)
                a2 = random.choice (string_pool)
                a3 = random.choice (string_pool)
                a4 = random.choice (string_pool)
                a5 = a1 + a2 + a3 + a4
            z.append(a5)
            total.append(a5)


        for i, j in zip (y, z):
            os.rename (f"{pdbspath}/{x}/" + i, f"{pdbspath}/{x}/" + j + ".pdb")
            with open (f"{pdbspath}/{x}.txt", "a") as list:
                list.write(i)
                list.write("----------")
                list.write(j + "\n")

    print ("Renamer2 - Done !")



if __name__ == '__main__':
    if args.renamer == "y" and args.importer == "n" and args.listmaker == "n" and args.renamer2 == "n":
        renamer (pdbpath = args.pdbpath)

    elif args.renamer == "n" and args.importer == "y" and args.listmaker == "n" and args.renamer2 == "n":
        importer (dalipath = args.dalipath, pdbpath = args.pdbpath, datpath = args.datpath)

    elif args.renamer == "n" and args.importer == "n" and args.listmaker == "y" and args.renamer2 == "n":
        listmaker (dalipath = args.dalipath, datpath = args.datpath)

    elif args.renamer == "n" and args.importer == "n" and args.listmaker == "n" and args.renamer2 == "y":
        renamer2 (pdbspath = args.pdbspath)

    else:
        print ("Please select only one (renamer or importer or listmaker")

    print ("Finished !")