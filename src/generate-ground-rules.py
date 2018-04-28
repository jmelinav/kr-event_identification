PATH = "../data/"
print("test")

import os

OBJECT_DICT = {
    "Person" :'p',
    "Tree" :'t',
    "BBQ_Oven":'bbq',
    "Car1" : "c1_",
    "Car2" : "c2_",
    "Dog" : 'd',
    "Frisbee" : 'f',
    "Shelter1" : 's1_',
    "Shelter2" : 's2_',
    "Table_Seat": 'tbl',
    "Trash_Bin1" : 'bin1_',
    "Trash_Bin2" : 'bin2_',
    "Building":'bld',
    "Info_Booth":'ib',
    "Desk":'d',
    "Box":'b'
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