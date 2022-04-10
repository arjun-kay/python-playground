#
# CS6507 - Assignment - 1
# Due Date - By 08th March, 2021
#
# Written by - Arjun Krishnan
# 

import re

def find_matches(nfile, mrfile):
    
    # Fn takes 2 input files and prints out record details if there is 
    # match as per given conditions
    textfile = open(nfile, "r")
    nicholas_txt = textfile.read()
    textfile.close()
    
    textfile = open(mrfile, "r")
    mary_txt = textfile.read()
    textfile.close()   
    
    
    data_pattern = r"""Marriage .*\n\s*?in \d{4}\n\s*?(.*)\n\s*?(.*)\n\s*?(.*)\n\s*?(.*)\n\s*?(.*)\n\s*?(.*)\n"""
    record_pattern = r"(?P<Year>(?<=Year\s)\d{4}).*(?P<Quarter>(?<=Quarter\s)\d).*(?P<Volume>(?<=Volume No\s)\d+).*(?P<Page>(?<=Page No\s)\d+)"
    
    count = 0
    for m in re.finditer(data_pattern, nicholas_txt, re.MULTILINE):
        r_n = re.sub(r"[\t\n]+", " ", m.group())    
        count +=1
        data_nicholas = re.findall(record_pattern, r_n)[0]
        count_mary = 0
        for record in re.finditer(data_pattern, mary_txt, re.MULTILINE):
            count_mary += 1
            r_m = re.sub(r"[\t\n]+", " ", record.group())
            data_mary = re.findall(record_pattern, r_m)[0]
            if(data_nicholas == data_mary):
                name_n = re.findall(r"(?P<Name>(?<=Marriage of ).*(?=in)).*(?P<Area>(?<=Area ).*(?= Returns Year))", r_n)[0]
                name_m = re.findall(r"(?P<Name>(?<=Marriage of ).*(?=in))", r_m)[0]
                print("Possible match!")
                print("%s and %s in %s in %s \nQuarter = %s, Volume = %s, Page = %s\n"%(name_n[0].strip(),
                                                                                      name_m.strip(),
                                                                                      name_n[1].strip(),
                                                                                      data_mary[0],
                                                                                      data_mary[1],
                                                                                      data_mary[2],
                                                                                      data_mary[3]))


if __name__ == "__main__":
    nfile = "nicholas.txt"
    mrfile = "mary_roche.txt"
    find_matches(nfile, mrfile)