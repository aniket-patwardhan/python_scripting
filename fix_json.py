#! python3
# -*- coding: utf-8 -*-
"""
@author: Aniket
"""

import json
import os
import re
script_dir =os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'C:/Users/Aniket/Downloads/soleng_challenge_AniketPatwardhan/notes_sample.json')
file_path1 = os.path.join(script_dir, 'C:/Users/Aniket/Downloads/soleng_challenge_AniketPatwardhan/notes_fixed.json')
#read_json_file_from_source_code
with open(file_path, encoding="utf8") as read_json:
    read_content = json.load(read_json)
    notes_access = read_content['notes']
    
   #added_description_to_groups
    for notes_data in notes_access:
        group_access = notes_data['groups']
        for groups_data in group_access: 
            addon1 = {"description":"a group for Micro Caps"}
            addon2 = {"description":"a group for Large Caps"}
            addon3 = {"description":"a group for Small Caps"}
            addon4 = {"description":"a group for Global Teams"}
            if groups_data['id'] == 15 :
             data = groups_data
             data.update(addon1)
            elif groups_data['id'] == 20 :
             data = groups_data
             data.update(addon4)
            elif groups_data['id'] == 12 :
             data = groups_data
             data.update(addon2)
            elif groups_data['id'] == 19 :
             data = groups_data
             data.update(addon3)
             
             
    #update_ids_in_attachments
    for notes_data in notes_access:
        attachmentsID_access = notes_data['attachments']
        for attachmentsID_data in attachmentsID_access:
            html = attachmentsID_data['html_preview']
            fileID_access = attachmentsID_data['id']
            attachmentsID_data['id'] = attachmentsID_data['id'] + 100000 
            min = str(attachmentsID_data['id'])
            replaced_html_preview = re.sub('\d\d\d\d', min, html)
            attachmentsID_data['html_preview'] = replaced_html_preview
            previews = attachmentsID_data['previews']
            previews_data = []
            previews_data = [re.sub('\d\d\d\d', min, i) for i in previews]
            attachmentsID_data['previews'] = previews_data
  
new_json = json.dumps((read_content), sort_keys=True, indent=4)
            
with open(file_path1, 'w') as fix_file:
    fix_file.write(new_json)
    
    tick = set()
    for notes_data in notes_access:
        tags_access = notes_data['tags']
        for tags_data in tags_access:
            tick.add(tags_data)
            

for unique_tick in tick:
    print(unique_tick)