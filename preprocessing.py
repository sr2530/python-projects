import json
import numpy as np
import random

random.seed(0)

with open('./annotations_trainval2017/captions_train2017.json', 'r') as f:
    all_captions = json.load(f)

# dict_keys(['info', 'licenses', 'images', 'annotations'])
print(all_captions['images'][0])
print(all_captions['annotations'][1])
print(len(all_captions['images']))

all_images = all_captions['images']
random.shuffle(all_images)
training_idxs = random.sample(range(len(all_images)), int(0.7 * len(all_images)))

train_images = [all_images[i] for i in training_idxs]
val_images = [all_images[i] for i in range(len(all_images)) if i not in training_idxs]


# Map image ID to all info
train_imgid_to_info = {}
# Map caption to file_name and image ID
captions_to_filename = {}

for i in range(len(train_images)):
    train_imgid_to_info[train_images[i]['id']] = {'file_name': train_images[i]['file_name'], 'captions': [], 'image_id': train_images[i]['id']}

for i in range(len(all_captions['annotations'])):
    if all_captions['annotations'][i]['image_id'] in train_imgid_to_info:
        train_imgid_to_info[all_captions['annotations'][i]['image_id']]['captions'].append(all_captions['annotations'][i]['caption'])
        captions_to_filename[all_captions['annotations'][i]['caption']] = {'file_name': train_imgid_to_info[all_captions['annotations'][i]['image_id']]['file_name'],
                                                                            'image_id': all_captions['annotations'][i]['image_id']}


# Map image file name to a mapping with keys file_name, captions, and image id
train_image_file_to_info = {}
for i in range(len(train_images)):
    train_image_file_to_info[train_images[i]['file_name']] = train_imgid_to_info[train_images[i]['id']]

with open('train_annotations.json', 'w') as f:
    json.dump(train_image_file_to_info, f)
with open('train_caption2filename.json', 'w') as f:
    json.dump(captions_to_filename, f)


# Map image ID to all info
val_imgid_to_info = {}
# Map caption to file_name and image ID
val_captions_to_filename = {}

for i in range(len(val_images)):
    val_imgid_to_info[val_images[i]['id']] = {'file_name': val_images[i]['file_name'], 'captions': [], 'image_id': val_images[i]['id']}

for i in range(len(all_captions['annotations'])):
    if all_captions['annotations'][i]['image_id'] in val_imgid_to_info:
        val_imgid_to_info[all_captions['annotations'][i]['image_id']]['captions'].append(all_captions['annotations'][i]['caption'])
        val_captions_to_filename[all_captions['annotations'][i]['caption']] = {'file_name': val_imgid_to_info[all_captions['annotations'][i]['image_id']]['file_name'],
                                                                            'image_id': all_captions['annotations'][i]['image_id']}


# Map image file name to a mapping with keys file_name, captions, and image id
val_image_file_to_info = {}
for i in range(len(val_images)):
    val_image_file_to_info[val_images[i]['file_name']] = val_imgid_to_info[val_images[i]['id']]

with open('val_annotations.json', 'w') as f:
    json.dump(val_image_file_to_info, f)
with open('val_caption2filename.json', 'w') as f:
    json.dump(val_captions_to_filename, f)