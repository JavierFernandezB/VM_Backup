import os
from time import sleep
import shutil



FULL_PATH = "D:\\"
FOLDER_VM = 'Virtual Machines\\'
FOLDER_BAK = 'vmachine.bak\\'



def clear():
    os.system('cls')

def main():
    def back():
        sleep(1)
        clear()
        main()

    os.chdir('D:\\')
    
    print("""
    option 1 create backup
    option 2 restore machine
    option 3 check backups 
    option 4 check machines
    option 5 delete backup
    option 6 delete machine
    option 7 exit
    """)
    option = int(input('Number: '))
    
    if option is not None:
        #do something
        
        if option == 1:
            os.chdir(FOLDER_VM)
            clear()
            print('chose the vmare \n ')
            machines = {}
            for idx, i in enumerate(os.listdir(),start=1):
                print(idx, ": ",i)
                machines[str(idx)] = i
            
            print('\n')
            machine = input('Vm name: ')
            print(machines)
            print(machines[machine])
            if machines[machine] in os.listdir():
                
                #check for premade backups
                EXSIST = False
                os.chdir(FULL_PATH+FOLDER_BAK)
                for bak in os.listdir():
                    if bak == machines[machine]:
                        print('backup alredy exist')
                        EXSIST = True
                    else:
                        EXSIST = False
                if not EXSIST:
                    #DO 
                    os.chdir(FULL_PATH+FOLDER_VM)
                    print('starting to coping files may take a while \n dont stop the procces if you dont want to get the bak corrupted')
                    shutil.copytree(FULL_PATH + FOLDER_VM + machines[machine],FULL_PATH+FOLDER_BAK+machines[machine]+"\\",dirs_exist_ok=True)
                    clear()
                    print('Done')
                    back()
            
        elif option == 2:
            os.chdir(FULL_PATH+FOLDER_BAK)
            clear()
            machines = {}
            for idx, i in enumerate(os.listdir(),start=1):
                print(idx, ": ",i)
                machines[str(idx)] = i

            restore = input('Chose Backup: ')
            if machines[restore] in os.listdir():
                #DO
                if os.path.exists(FULL_PATH+FOLDER_VM+machines[restore]):
                    delete = input('Folder exist you want to delete: Yes/No ')
                    delete.strip()
                    if delete == 'Yes':
                        print('deleting folder')
                        shutil.rmtree(FULL_PATH+FOLDER_VM+machines[restore])
                        print('Done')
                        sleep(0.5)
                        clear()
                        print('Restoring Folder dont stop process pls')
                        shutil.copytree(FULL_PATH+FOLDER_BAK+machines[restore],FULL_PATH + FOLDER_VM + machines[restore])
                        print('Done restored')
                        back()
                    elif delete == 'No':
                        back()
                    else:
                        print('wrong answer')
                        back()
                else:
                    print('Coping...')
                    shutil.copytree(FULL_PATH+FOLDER_BAK+machines[restore],FULL_PATH + FOLDER_VM + machines[restore])
                    clear()
                    print('Done')
            else:
                print('folder dont exist')
        
        elif option == 3:
            clear()
            os.chdir(FULL_PATH+FOLDER_BAK)
            if os.listdir():
                print('Those are the backups ')

                for bak in os.listdir():
                    print(bak)
            else:
                print('no backups')
            print('Showing backups for 5 sec')
            sleep(4)
            back()
        elif option == 4:
            clear()
            os.chdir(FULL_PATH+FOLDER_VM)
            if os.listdir():
                print('Machines: \n')
                os.chdir(FULL_PATH+FOLDER_VM)
                for bak in os.listdir():
                    print(bak)
            else:
                print('no machines')
            print('Showing machines for 5 sec')
            sleep(4)
            back()
        elif option == 5:
            clear()
            os.chdir(FULL_PATH+FOLDER_BAK)
            machines = {}
            for idx, i in enumerate(os.listdir(),start=1):
                print(idx, ": ",i)
                machines[str(idx)] = i
            
            chosen = input('Chose backup for delete: ')
            if machines[chosen] in os.listdir():
                ask = input('You are sure?: Yes/No ')
                ask.strip()
                if ask == 'Yes':
                    print('Deleting...')
                    shutil.rmtree(FULL_PATH+FOLDER_BAK+machines[chosen])
            else:
                print('folder dont exist')
            back()
        elif option == 6:
            clear()
            os.chdir(FULL_PATH+FOLDER_VM)
            machines = {}
            for idx, i in enumerate(os.listdir(),start=1):
                print(idx, ": ",i)
                machines[str(idx)] = i
            
            chosen = input('Chose Vmachine for delete: ')
            if machines[chosen] in os.listdir():
                ask = input('You are sure?: Yes/No ')
                ask.strip()
                if ask == 'Yes':
                    print('Deleting...')
                    
                    shutil.rmtree(FULL_PATH+FOLDER_VM+machines[chosen])
                    clear()
                    print('Done')
            else:
                print('folder dont exist')
            back()
        elif option == 7:
            print('Bye')
            exit()
            
    else:
        print('you chose a wrong response')



if __name__ == "__main__":
    main()
