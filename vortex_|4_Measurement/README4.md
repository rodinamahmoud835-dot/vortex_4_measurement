{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0

This task measures real-world lengths/heights in an image using a known reference length.  \
The user clicks **two points** on the reference object, enters the real reference length in **cm**, then the program measures any other distance by clicking **two points** again\
\
How it works \
- First 2 clicks => reference pixel distance => compute scale  \
  `scale = real_cm / pixel_distance`\
- Next 2 clicks => measured length  \
  `measured_cm = pixel_distance * scale`\
\
\
Video:\
https://drive.google.com/file/d/1YrzAJHjp5X-viRI2F7kgDTCAl6lNqWiI/view?usp=sharing}
