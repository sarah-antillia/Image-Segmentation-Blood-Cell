
# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Copyright 2023 antillia.com Toshiyuki Arai

import os
import sys
import glob
import shutil

import traceback
import random

def create_mini_test(images_dir, masks_dir, output_images_dir, output_masks_dir, num=20):
   # Listup *.png image files not including *.jpg
   image_files = glob.glob(images_dir + "*.png")
   random.seed = 137

   random.shuffle(image_files)
   print("image_files len {}".format(len(image_files)))

   test_image_files = random.sample(image_files, num)
   for image_file in test_image_files:
     basename = os.path.basename(image_file)
     mask_file = os.path.join(masks_dir, basename)
     if os.path.exists(mask_file):
       shutil.copy2(image_file, output_images_dir)
       print("Copied {} to {}".format(image_file, output_images_dir))
       shutil.copy2(mask_file,  output_masks_dir)
       print("Copied {} to {}".format(mask_file, output_masks_dir))
     else:
        print("Not found corresponding mask_file {} to image_file {}".format(mask_file, image_file))


if __name__ == "__main__":
  try:
    images_dir = "./New folder/Original/"
    masks_dir  = "./New folder/Mask/"

    output_images_dir = "./mini_test/images/"
    output_masks_dir  = "./mini_test/masks/"

    if os.path.exists(output_images_dir):
      shutil.rmtree(output_images_dir)
    if not os.path.exists(output_images_dir):
      os.makedirs(output_images_dir)

    if os.path.exists(output_masks_dir):
      shutil.rmtree(output_masks_dir)
    if not os.path.exists(output_masks_dir):
      os.makedirs(output_masks_dir)

    create_mini_test(images_dir, masks_dir, output_images_dir, output_masks_dir)

  except:
    traceback.print_exc()
