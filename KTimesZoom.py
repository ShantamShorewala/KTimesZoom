# KTimesZoom
import Image
import numpy as np
imageFileName = raw_input("Enter the image name with absolute path")
pic=Image.open(imageFileName)
pic.show("Original")
copy=np.asarray(pic)

list1=copy.tolist()

height=len(list1)
width=len(list1[1])

print str(width)+"  "+str(height) 

print "The zoom factor should be >= 1"
point_x, point_y, scale = raw_input("Enter the pivot co-ordinates (x,y) and zooming factor separated using comma").split(',')

scale = int(scale)
pivot_x = int(point_x)
pivot_y = int(point_y)

if scale==1:
    pic.show()
else:
    if pivot_x>width or pivot_y>height:
        print "Pivot out of image boundary"
    else:
        rows=scale*(height-1)+1
        columns=scale*(width-1)+1

        a=(pivot_x)*scale+1
        b=a+width
        c=(pivot_y)*scale+1
        d=c+height

        if b>columns:
            b=columns
            a=columns-width
        if d>rows:
            d=rows
            c=rows-height

        list2=[[[0 for col in range(3)] for col in range(columns)] for col in range(rows)]
        list3=[[[0 for col in range(3)] for col in range(columns)] for col in range(rows)]
    
        for k in range(0,3):
            for j in range(0,width):
                n=0
                for i in range(0,height-1):
                    list2[n][j][k]=list1[i][j][k]
                    n=n+1
                    op=(abs(list1[i][j][k]-list1[i+1][j][k])/scale)
                    rgb=min(list1[i][j][k], list1[i+1][j][k])
                    for m in range(0,scale-1):
                        rgb=rgb+op
                        list2[n][j][k]=rgb
                        n=n+1

        for k in range(0,3):
            for i in range(0,rows):
                n=0
                for j in range(0,width-1):
                    list3[i][n][k]=list2[i][j][k]
                    n=n+1
                    op=(abs(list2[i][j][k]-list2[i][j+1][k])/scale)
                    rgb=min(list2[i][j][k], list2[i][j+1][k])
                    for m in range(0,scale-1):
                        list3[i][n][k]=rgb
                        n=n+1
                        rgb=rgb+op
                     
        for i in range(0,rows):
            for j in range(0,columns):
                for k in range(0,3):
                    list3[i][j][k]=int(list3[i][j][k])

        data=()
        for i in range(c,d):
            for j in range(a,b):
                    data+=(tuple(list3[i][j]),)

    img = Image.new('RGB',(width,height), "white")
    img.putdata(data)
    img.show("Zoomed")







