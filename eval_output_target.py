from peamt import PEAMT
from pathlib import Path
import sys
import datetime

def main(
    output_filename: Path = Path("output.mid"),
    target_filename: Path = Path("target.mid"),
) -> float:
    eval = PEAMT()
    value = eval.evaluate_from_midi(
        target_filename.as_posix(), output_filename.as_posix()
    )
    return value


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage {sys.argv[0]} requires output and target as path names")
    else:
        output_filename: Path = Path(sys.argv[1])
        target_filename: Path = Path(sys.argv[2])
        try:
            result = main(output_filename, target_filename)
        except ValueError:
            result = 0.0
        with open(f"/app/data/result_{datetime.datetime.now()}.txt", "wt") as myfile:
           myfile.write(f"{result:1.04f}\n")
           myfile.close()
        print(f"{result:1.04f}")
