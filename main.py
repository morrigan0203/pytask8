import myscun
from pathlib import Path

scun_dir = Path(__file__).parent.parent

myscun.write_csv(scun_dir, "./TesT_8/dir.csv")
myscun.write_json(scun_dir, "./TesT_8/dir.json")
myscun.write_pickle(scun_dir, "./TesT_8/dir.pickle")