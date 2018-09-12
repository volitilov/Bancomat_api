# cli.py

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import sys, os, shutil, bankomat

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class App:
    def __init__(self):
        self.app_folder = os.path.dirname(bankomat.__file__)+'/app/'

    def init(self):
        src = self.app_folder
        where = os.getcwd()

        for src_folder, list_folder, files in os.walk(src):
            if os.path.basename(src_folder) == '__pycache__':
                shutil.rmtree(src_folder)

        try:
            for item in os.listdir(src):
                if item != '__pycache__':
                    s = os.path.join(src, item)
                    d = os.path.join(where, item)

                    if os.path.isdir(s):
                        shutil.copytree(s, d)
                    else:
                        shutil.copy2(s, d)

            os.system('echo "\n[ \033[92mTrue\033[0m ] - работа выполнена\n"')
        
        except FileExistsError:
            os.system('echo "\n[ \033[31mFalse\033[0m ] - вы уже инициализировали данные\n"')

app = App()

def main():
    src = os.getcwd()
    if len(sys.argv) == 2 and sys.argv[1].lower() == 'init':
        app.init()
    else:
        print('Usage: bankomat init')
        


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
    main()
