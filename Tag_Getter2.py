import io
import os
def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    #print('Labels:')
    #print(labels)
    tag_list=[]
    for label in labels:
       tag_list.append(label.description)
    return(tag_list)


tag_list=detect_labels("/Users/vivekadrakatti/Downloads/naan-202-320x320-1.jpg")
#index 1 stores presence of Spaghetti, 2nd stores beans, 3rd stores naan
main_list=[0,0,0]
for i in tag_list:
    if( i == 'Spaghetti'):
        main_list[0]=1
    if( i== 'Bean'):
        main_list[1]=1
    if( i == 'Naan'):
        main_list[2]=1

print(main_list)



#print(master_list)
