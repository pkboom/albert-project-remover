from albert import *
import re
from os import path
from os import walk

__title__ = "Remove a project"
__version__ = "0.4.0"
__triggers__ = "rmrf "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

_dirs = [
    '/home/y/code',
    '/home/y/code/packages',
    '/home/y/code/albert-extensions'
]

def handleQuery(query):
    if not query.isTriggered or not query.isValid or not query.string:
        return

    projects = []

    for _dir in _dirs:
        for root, dirs, files in walk(_dir):
            for dir in dirs:
                projects.append(path.join(root, dir))

            for file in files:
                projects.append(path.join(root, file))
            break

    regexp = query.string.strip().replace(" ", ".*")

    items = []

    for project in projects:
        if re.search(regexp, project[(project.rfind('/') + 1):]): 
            print(project[(project.rfind('/') + 1):])
            items.append(Item(
                id=project,
                icon=icon,
                text=project[(project.rfind('/') + 1):],
                actions=[TermAction(
                    text="This action removes a project.", 
                    script='rm -rf {}'.format(project[(project.rfind('/') + 1):]), 
                    cwd='/home/y/code'
                )],
            ))

    return items
