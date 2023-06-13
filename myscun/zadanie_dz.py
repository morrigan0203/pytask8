from pathlib import Path
import csv
import json
import pickle


def scan_dir(target: Path, res_list: list)->int:
    size_f = 0
    for path in Path(target).iterdir():
        # print(path, path.is_dir(), path.is_file(), path.name, path.absolute())
        if path.is_dir():
            size_f = size_f + scan_dir(path, res_list)
        else:
            size_f = size_f + path.stat().st_size
        info = {"name":path.name, "full_name":str(path.absolute()), "parent":path.parent.name, "type":"file" if path.is_file() else "directory", "size":size_f}
        res_list.append(info)
    return size_f

def write_csv(target: Path, name: str):
    data = []
    fullSize = scan_dir(target, data)
    field_names = ["name", "full_name","parent","type","size"]
    with open(name, 'w') as f:
        write = csv.DictWriter(f, fieldnames=field_names, quotechar='"', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        write.writeheader()
        write.writerows(data)

def write_json(target: Path, name: str):
    data = []
    fullSize = scan_dir(target, data)
    with open(name, 'w') as f:
        json.dump(data,f,indent=4)

def write_pickle(target: Path, name: str):
    data = []
    fullSize = scan_dir(target, data)
    with open(name, 'wb') as f:
        pickle.dump(data,f)





if __name__ == "__main__":
    scun_dir = Path(__file__).parent.parent
    print(scun_dir)
    write_csv(scun_dir, "./TesT_8/dir.csv")
    write_json(scun_dir, "./TesT_8/dir.json")
    write_pickle(scun_dir, "./TesT_8/dir.pickle")
