{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red195\green123\blue90;\red19\green20\blue21;\red174\green176\blue183;
\red89\green158\blue96;\red71\green149\blue242;\red92\green96\blue103;\red117\green114\blue185;\red38\green157\blue169;
}
{\*\expandedcolortbl;;\csgenericrgb\c76471\c48235\c35294;\csgenericrgb\c7451\c7843\c8235;\csgenericrgb\c68235\c69020\c71765;
\csgenericrgb\c34902\c61961\c37647;\csgenericrgb\c27843\c58431\c94902;\csgenericrgb\c36078\c37647\c40392;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c14902\c61569\c66275;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 import \cf4 cv2\
\cf2 import \cf4 math\
\
img = cv2.imread(\cf5 "Resources/image1.jpeg"\cf4 )\
\
points = []\
scale = \cf2 None\
\
def \cf6 mouse\cf4 (event, x, y, \cf7 flags\cf4 , \cf7 param\cf4 ):\
    \cf2 global \cf4 points, scale\
\
    \cf2 if \cf4 event == cv2.EVENT_LBUTTONDOWN:\
        points.append((x, y))\
\
        \cf2 if \cf8 len\cf4 (points) == \cf9 2\cf4 :\
            x1, y1 = points[\cf9 0\cf4 ]\
            x2, y2 = points[\cf9 1\cf4 ]\
\
            dx = x2 - x1\
            dy = y2 - y1\
            distance = math.sqrt(dx*dx + dy*dy)\
\
            \cf2 if \cf4 scale \cf2 is None\cf4 :\
                \cf8 print\cf4 (\cf5 "Reference pixel distance:"\cf4 , distance)\
                real_cm = \cf8 float\cf4 (\cf8 input\cf4 (\cf5 "Enter reference length in cm: "\cf4 ))\
                scale = real_cm / distance\
                \cf8 print\cf4 (\cf5 "Scale"\cf4 , scale)\
            \cf2 else\cf4 :\
                measured_cm = distance * scale\
                \cf8 print\cf4 (\cf5 "length:"\cf4 , measured_cm, \cf5 "cm"\cf4 )\
\
            points = []\
\
cv2.imshow(\cf5 "Image"\cf4 , img)\
cv2.setMouseCallback(\cf5 "Image"\cf4 , mouse)\
cv2.waitKey(\cf9 0\cf4 )\
\
}