'''
django code smells detection tool
By qing he 2594216h
'''

import pandas as pd
from file_extractor import walk_path
import astCheck
import parse
from threshold import smells_metrics_thresholds

#detect the code smells
def detect_smells(path):
    detected_codesmells = [] #store the code smells into list
    for file_name in walk_path(path):
        print(file_name)
        try:
            astContent = parse.parse_file(file_name)
        except:
            continue
        myast = astCheck.MyAst()
        myast.fileName = file_name
        myast.visit(astContent)
        for item in myast.result:
            if item[0] == 1:
                if int(item[3])>=smells_metrics_thresholds['Long Parameter List'][0]:
                    detected_codesmells.append([path,item[1],item[2],'Long Parameter List'])
                    continue
            elif item[0] == 2:
                if int(item[3])>=smells_metrics_thresholds['Long Method'][0]:
                    detected_codesmells.append([path,item[1],item[2],'Long Method'])
                    continue
            elif item[0] == 3:
                if int(item[3])>=smells_metrics_thresholds['Large Class'][0]:
                    detected_codesmells.append([path,item[1],item[2],'Large Class'])
                    continue
    return detected_codesmells

def main():
    # Add project absolute path
    absolute_path = "/Users/heqing/Downloads/DjangoBlog-master"
    codesmells = detect_smells(absolute_path)
    df = pd.DataFrame(codesmells)
    try:
        df.columns=["Project path","File name","Line number","Code smell name"]
    except:
        print("There is no code smells in this project.")
    df.to_csv('codesmell.csv')   #save the df to the csv file
    
main()
