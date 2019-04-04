# This ipynb file is adapted from https://github.com/wagonhelm/TF_ObjectDetection_API/blob/master/ChessObjectDetection.ipynb
##import skimage
import numpy as np
##from skimage import io, transform
import os
import shutil
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import tensorflow as tf
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import urllib.request
import urllib.error



root = os.getcwd()
imagePath = os.path.join(root, 'images')
labelsPath = os.path.join(root, 'labels')
linksPath = os.path.join(imagePath, 'imageLinks')
trainPath = os.path.join(imagePath, 'train')
testPath = os.path.join(imagePath, 'test')

os.chdir(root)

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob('/Users/vivekadrakatti/Documents/Food_Detection/data' + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():

    for i in [trainPath, testPath]:
        image_path = i
        folder = os.path.basename(os.path.normpath(i))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('data/'+folder+'.csv', index=None)
        print('Successfully converted xml to csv.')

main()
