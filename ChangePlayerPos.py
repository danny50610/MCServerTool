import json
import argparse
import nbt
import os


def main():
    parser = argparse.ArgumentParser(description='修改玩家座標')
    parser.add_argument("username", help="Player name", type=str)
    parser.add_argument("dim", help="Target dim", type=int)
    parser.add_argument("x", help="Target x", type=float)
    parser.add_argument("y", help="Target y", type=float)
    parser.add_argument("z", help="Target z", type=float)
    args = parser.parse_args()

    with open('usernamecache.json') as f:
        uuid_to_username = json.load(f)

    target_uuid = None
    for uuid, username in uuid_to_username.items():
        if username == args.username:
            target_uuid = uuid

    print('Player uuid: ' + target_uuid)

    player_dat = nbt.nbt.NBTFile(os.path.join('world', 'playerdata', target_uuid + '.dat'), 'rb')
    player_dat['Dimension'].value = args.dim
    player_dat['Pos'][0].value = args.x
    player_dat['Pos'][1].value = args.y
    player_dat['Pos'][2].value = args.z

    player_dat.write_file(os.path.join('world', 'playerdata', target_uuid + '.dat'))
    print('Done')


if __name__ == '__main__':
    main()
