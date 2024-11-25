isPyperclip = False

try:
    import pyperclip

    isPyperclip = True
except:
    print("Please install pyperclip, for better experience")
    pass

commandBlock_commandWorkpiece = """summon minecraft:falling_block ~ ~1 ~ {BlockState:{Name:"redstone_block"},Time:1,Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,BlockState:{Name:"activator_rail"},Time:1,Passengers:[replace77k46gob8cCH%eQNwcc8Zk9Vxw,{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:"kill @e[type=command_block_minecart,distance=..3]"}'},{id:command_block_minecart,Command:'setblock ~ ~2 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}'}]}]}]}"""
command_workpiece = "{id:command_block_minecart,Command:'replace77k46gob8cCH%eQNwcc8Zk9Vxw'}"
rep = 'replace77k46gob8cCH%eQNwcc8Zk9Vxw'
commands = []


def createCommand(commandBlock_commandWorkpiece, command_workpiece, commands, replaceStr=rep):
    str_command = ''
    for x in commands:
        str_command += command_workpiece.replace(replaceStr, x) + ','
    str_command = str_command[:-1]
    return commandBlock_commandWorkpiece.replace(replaceStr, str_command)


while 1:
    tmp = input('Enter command (\'\' for end): ')
    if tmp != '':
        commands.append(tmp.replace('/', ''))
    else:
        command = createCommand(commandBlock_commandWorkpiece, command_workpiece, commands)
        print(command)
        if isPyperclip:
            pyperclip.copy(command)
        input()
        break
