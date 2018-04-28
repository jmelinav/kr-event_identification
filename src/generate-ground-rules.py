PATH = "../data/"
print("test")

import os

OBJECT_DICT = {
    "Person" :'P',
    "Tree" :'T',
    "BBQ_Oven":'BBQ',
    "Car1" : "C1_",
    "Car2" : "C2_",
    "Dog" : 'D',
    "Frisbee" : 'F',
    "Shelter1" : 'S1_',
    "Shelter2" : 'S2_',
    "Table_Seat": 'TBl',
    "Trash_Bin1" : 'BIN1_',
    "Trash_Bin2" : 'BIN2_',
    "Building":'BLD',
    "Info_Booth":'IB',
    "Desk":'DSK',
    "Box":'B'
}

FILE_NAMES =["outputID_GOPR0060.txt", "outputID_GOPR0062.txt","outputID_GOPR0064.txt","outputID_GOPR0065.txt",
             "outputID_GOPR0069.txt","outputID_GOPR0070.txt"]

for name in FILE_NAMES:
    output_file_name = name.split(".")[0]+".db"
    with open(os.path.join(PATH, name)) as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    with open(output_file_name,"w") as f:
        for x in content:
            columns = x.split()
            #print(columns)
            id = columns[0]
            xmin = columns[1]
            ymin = columns[2]
            xmax = columns[3]
            ymax = columns[4]
            x_mid = str(int((int(xmin)+int(xmax))/2))
            y_mid = str(int((int(ymin) + int(ymax)) / 2))
            frame_no = columns[5]
            object = columns[9].replace('"','')
            object_info = OBJECT_DICT.get(object)+id
            position_info = "PositionOf(" + object_info + "," + x_mid + "," + y_mid + "," + frame_no + ")\n"
            #print(position_info, len(columns))
            f.write(position_info)
            if len(columns) > 10:
                group = columns[10].replace('"','')
                #f.write(group)
                group_num = group[len(group)-1]
                group = group[0:len(group)-1]
            #print(id,xmin,ymin,xmax,ymax,object,group,group_num)
        f.close()
            #exit(0)