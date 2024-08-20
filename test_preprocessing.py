import json

# Get test dataset captions
with open('./annotations_trainval2017/captions_val2017.json', 'r') as f:
    test_captions = json.load(f)

# dict_keys(['info', 'licenses', 'images', 'annotations'])
# print(test_captions['images'][0])
# print(test_captions['annotations'][1])

# Map image ID to all info
test_imgid_to_info = {}
# Map caption to file_name and image ID
captions_to_filename = {}

for i in range(len(test_captions['images'])):
    test_imgid_to_info[test_captions['images'][i]['id']] = {'file_name': test_captions['images'][i]['file_name'], 'captions': [], 'image_id': test_captions['images'][i]['id']}

for i in range(len(test_captions['annotations'])):
    test_imgid_to_info[test_captions['annotations'][i]['image_id']]['captions'].append(test_captions['annotations'][i]['caption'])
    captions_to_filename[test_captions['annotations'][i]['caption']] = {'file_name': test_imgid_to_info[test_captions['annotations'][i]['image_id']]['file_name'],
                                                                        'image_id': test_captions['annotations'][i]['image_id']}


# Map image file name to a mapping with keys file_name, captions, and image id
test_image_file_to_info = {}
for i in range(len(test_captions['images'])):
    test_image_file_to_info[test_captions['images'][i]['file_name']] = test_imgid_to_info[test_captions['images'][i]['id']]

with open('test_annotations.json', 'w') as f:
    json.dump(test_image_file_to_info, f)
with open('test_caption2filename.json', 'w') as f:
    json.dump(captions_to_filename, f)