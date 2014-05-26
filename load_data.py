#!/usr/bin/env python
# coding=utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appsystem.settings")
from tags.models import *

TAG_FILE = "tags.txt"
def generate_tags(tag_file=TAG_FILE):
    '''generate app tag from local file'''
    with open(tag_file, 'r') as tf:
        for line in tf:
            attr_list = line.strip().split(';')
            app_name = attr_list[0]
            for tag in attr_list[1:]:
                tag_name, tag_score = tag.split(":")
                yield (app_name, tag_name, float(tag_score))

def insert_tags(tags):
    for app_tag in tags:
        a, t, at= None, None, None
        try:
            a = App.objects.get(app_name=app_tag[0])
        except App.DoesNotExist :
            a = App(app_name=app_tag[0])
            a.save()
        try:
            t = Tag.objects.get(tag_name=app_tag[1])
        except Tag.DoesNotExist :
            t = Tag(tag_name=app_tag[1], tag_type='regular')
            t.save()
        apptag = AppTag(app=a, tag=t, score=app_tag[2]) 
        apptag.save()

def test_generate_tags():
    tmp = open('test.txt', 'w')
    tmp.write("facebook;video:1.2;new friend:0.2;friend:2\n")
    tmp.write("twitter;news:1.2;people:0.2;friend:2")
    tmp.close()
    tags = generate_tags("test.txt")
    for t in tags:
        print t

def main():
    insert_tags(generate_tags(TAG_FILE))

if __name__ == "__main__":
    main()

