# import os
# import json
# import torch
# from torch.utils.data import Dataset
# import torchvision.transforms as transforms
# from PIL import Image

# class COCO2017(Dataset):
#     def __init__(self, text_data_json, image_folder, num_images, split='train'):
#         self.image_folder = image_folder
#         self.annotations = None
#         with open(text_data_json, 'r') as f:
#             self.annotations = json.load(f)
#         self.captions = torch.load(f"{split}_tokenized_captions.pt")

#         self.transform = transforms.Compose([
#             transforms.Resize((64, 64)),
#             transforms.ToTensor(),
#         ])

#         self.images, self.file_names = self.preprocess_image(self.image_folder, self.annotations, num_images)

#         self.data = []
#         for i in range(len(self.images)):
#             for j in range(len(self.annotations[self.file_names[i]]['captions'])):
#                 self.data.append((self.images[i], self.captions[j]))

#     def __len__(self):
#         return len(self.images)
    
#     def __getitem__(self, idx):
#         return self.data[idx][0], self.data[idx][1]

#     def preprocess_image(self, folder, annotations, num_images):  
#         file_names = []
#         for annotation in list(annotations.keys())[0:num_images]:
#             if annotation.endswith(('.jpg')):
#                 file_names.append(annotation)

#         all_images = []
        
#         # if num_images != None:
#             # file_names = [f for f in os.listdir(folder)[0:num_images] if f.endswith(('.jpg'))]
#         for i in range(num_images):
#             image = Image.open(os.path.join(folder, file_names[i])).convert('RGB')
#             if self.transform:
#                 preprocessed_image = self.transform(image)
#             all_images.append(preprocessed_image)
#         # else:
#         #     # file_names = [f for f in os.listdir(folder) if f.endswith(('.jpg'))]
#         #     for filename in file_names:
#         #         image = Image.open(os.path.join(folder, filename)).convert('RGB')
#         #         if self.transform:
#         #             preprocessed_image = self.transform(image)
#         #         all_images.append(preprocessed_image)

#         return all_images, file_names

# # data = COCO2017('./train_annotations.json', './train2017', 10)
# # print(len(data))
# # for i in range(10):
# #     print(data[i][0].size(), data[i][1])










import os
import json
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from PIL import Image

class COCO2017(Dataset):
    def __init__(self, text_data_json, image_folder, num_images):
        self.image_folder = image_folder
        self.annotations = None
        with open(text_data_json, 'r') as f:
            self.annotations = json.load(f)
        self.transform = transforms.Compose([
            transforms.Resize((64, 64)),
            transforms.ToTensor(),
        ])

        self.images, self.file_names = self.preprocess_image(self.image_folder, self.annotations, num_images)

        self.data = []
        for i in range(len(self.images)):
            for caption in self.annotations[self.file_names[i]]['captions']:
                self.data.append((self.images[i], caption))

    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        return self.data[idx]

    def preprocess_image(self, folder, annotations, num_images):  
        file_names = []
        for annotation in list(annotations.keys())[0:num_images]:
            if annotation.endswith(('.jpg')):
                file_names.append(annotation)

        all_images = []
        
        # if num_images != None:
            # file_names = [f for f in os.listdir(folder)[0:num_images] if f.endswith(('.jpg'))]
        for i in range(num_images):
            image = Image.open(os.path.join(folder, file_names[i])).convert('RGB')
            if self.transform:
                preprocessed_image = self.transform(image)
            all_images.append(preprocessed_image)
        # else:
        #     # file_names = [f for f in os.listdir(folder) if f.endswith(('.jpg'))]
        #     for filename in file_names:
        #         image = Image.open(os.path.join(folder, filename)).convert('RGB')
        #         if self.transform:
        #             preprocessed_image = self.transform(image)
        #         all_images.append(preprocessed_image)

        return all_images, file_names

# # data = COCO2017('./train_annotations.json', './train2017', 10)
# # print(len(data))
# # for i in range(10):
# #     print(data[i][0].size(), data[i][1])