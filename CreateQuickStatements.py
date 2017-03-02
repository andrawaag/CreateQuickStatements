import pandas as pd
import numpy as np
import pprint

df = pd.read_csv('GL.csv')
#pprint.pprint(df)

vvd = "Q239333"
pvdd = "Q663535"
groenlinks = "Q667680"
sgp = "Q60172"

political_party = sgp
for index, row in df.iterrows():
    if row[10] == "-1":
        print("CREATE")
        qid = "LAST"
        print(qid+"\tLen\t\""+row[9].replace("nl:","")+"\"")
        print(qid + "\tLnl\t\"" + row[9].replace("nl:", "") + "\"")
        print(qid + "\tDen\t\"Dutch politician\"")
        print(qid + "\tDnl\t\"Politicus\"")
        print(qid + "\tP31\tQ5")
    else:
        qid = row[10]
    print(qid+"\tP3602\tQ16061881\tP1268\t"+political_party+"\tP1545\t\""+str(row[0])+"\"\tS854\t\"https://www.kiesraad.nl/binaries/kiesraad/documenten/rapporten/2017/2/definitieve-kandidatenlijsten-tk-2017/definitieve-kandidatenlijsten-tk2017-kieskring-s-gravenhage/osv3-9_Definitieve+kandidatenlijsten_TK2017_sGravenhage.pdf\"")
    if row[8]=="m":
        print(qid + "\tP21\tQ6581097\tS854\t\"https://www.kiesraad.nl/binaries/kiesraad/documenten/rapporten/2017/2/definitieve-kandidatenlijsten-tk-2017/definitieve-kandidatenlijsten-tk2017-kieskring-s-gravenhage/osv3-9_Definitieve+kandidatenlijsten_TK2017_sGravenhage.pdf\"")
    if row[8]=="v":
        print(qid + "\tP21\tQ6581072\tS854\t\"https://www.kiesraad.nl/binaries/kiesraad/documenten/rapporten/2017/2/definitieve-kandidatenlijsten-tk-2017/definitieve-kandidatenlijsten-tk2017-kieskring-s-gravenhage/osv3-9_Definitieve+kandidatenlijsten_TK2017_sGravenhage.pdf\"")
    print(qid + "\tP551\t" + str(row[12]) + "\tS854\t\"https://www.kiesraad.nl/binaries/kiesraad/documenten/rapporten/2017/2/definitieve-kandidatenlijsten-tk-2017/definitieve-kandidatenlijsten-tk2017-kieskring-s-gravenhage/osv3-9_Definitieve+kandidatenlijsten_TK2017_sGravenhage.pdf\"")
    print(qid + "\tP102\t" + political_party + "\tS854\t\"https://www.kiesraad.nl/binaries/kiesraad/documenten/rapporten/2017/2/definitieve-kandidatenlijsten-tk-2017/definitieve-kandidatenlijsten-tk2017-kieskring-s-gravenhage/osv3-9_Definitieve+kandidatenlijsten_TK2017_sGravenhage.pdf\"")
