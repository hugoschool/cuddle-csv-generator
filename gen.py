#!/usr/bin/env python3
# /// script
# dependencies = [
#   "Faker",
# ]
# ///

from faker import Faker
from enum import Enum
import random

fake = Faker()

SEPARATOR = ";"
CHINESE_CHARS = [
    "的",
    "了",
    "在",
    "和",
    "是",
    "有",
    "个",
    "上",
    "中",
    "为",
    "年",
    "这",
    "他",
    "日",
    "对",
    "也",
    "要",
    "我",
    "地",
    "到",
    "说",
    "我们",
    "就",
    "人",
    "不",
    "等",
    "工作",
    "月",
    "将",
    "与",
]

class Type(Enum):
    Bool = 1
    Int = 2
    Uint = 3
    Float = 4
    String = 5

def get_random_type():
    return random.choice(list(Type))

def get_random_value_of_type(t: Type):
    if t == Type.Bool:
        if random.randint(0, 1) == 0:
            return "false"
        else:
            return "true"

    if t == Type.Int:
        return random.randint(-500000, 500000)

    if t == Type.Uint:
        return random.randint(0, 1000000)

    if t == Type.Float:
        return "{:.2f}".format(random.random() * random.randint(0, 100000))

    if t == Type.String:
        return fake.word()

def basic_csv(f):
    rowsNb = random.randint(5, 25)
    colsTypes = []
    colsNb = random.randint(5, 25)

    for i in range(0, colsNb):
        colsTypes.append(get_random_type())
        f.write(fake.word())
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            f.write(str(get_random_value_of_type(colsTypes[i])))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols and {rowsNb} rows")

def missing_header(f):
    rowsNb = random.randint(5, 10)
    colsTypes = []
    colsNb = random.randint(5, 10)
    missedHeader = 0

    for i in range(0, colsNb):
        colsTypes.append(get_random_type())
        if i % 2 == random.randint(0, 1):
            f.write(fake.word())
        else:
            missedHeader += 1
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            f.write(str(get_random_value_of_type(colsTypes[i])))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols with {missedHeader} missed header and {rowsNb} rows")

def inconsistent_row_length(f):
    rowsNb = random.randint(5, 10)
    colsTypes = []
    colsNb = random.randint(5, 10)

    for i in range(0, colsNb):
        colsTypes.append(get_random_type())
        f.write(fake.word())
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            if i % 2 == random.randint(0, 1):
                f.write(str(get_random_value_of_type(colsTypes[i])))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols and {rowsNb} rows with inconsistent rows")

def huge_rows_csv(f):
    rowsNb = random.randint(100000, 150000)
    colsTypes = []
    colsNb = random.randint(5, 10)

    for i in range(0, colsNb):
        colsTypes.append(get_random_type())
        f.write(fake.word())
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            f.write(str(get_random_value_of_type(colsTypes[i])))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols and {rowsNb} rows")

def huge_cols_csv(f):
    rowsNb = random.randint(5, 7)
    colsTypes = []
    colsNb = random.randint(100000, 150000)

    for i in range(0, colsNb):
        colsTypes.append(get_random_type())
        f.write(fake.word())
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            f.write(str(get_random_value_of_type(colsTypes[i])))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols and {rowsNb} rows")

def non_ascii(f):
    rowsNb = random.randint(50, 100)
    colsNb = random.randint(50, 100)

    for i in range(0, colsNb):
        f.write(fake.word())
        if i != colsNb - 1:
            f.write(SEPARATOR)

    f.write("\n")

    for _ in range(0, rowsNb):
        for i in range(0, colsNb):
            f.write(random.choice(CHINESE_CHARS))
            if i != colsNb - 1:
                f.write(SEPARATOR)
        f.write("\n")

    print(f"Wrote file with {colsNb} cols and {rowsNb} rows")

def main():
    GEN_FOLDER="generated"

    for i in range(0, 5):
        with open(f"{GEN_FOLDER}/basic{i + 1}.csv", "w+") as f:
            basic_csv(f)

    with open(f"{GEN_FOLDER}/empty.csv", "w+") as f:
        f.write("")

    with open(f"{GEN_FOLDER}/missing_header.csv", "w+") as f:
        missing_header(f)

    with open(f"{GEN_FOLDER}/inconsistent_row_length.csv", "w+") as f:
        inconsistent_row_length(f)

    with open(f"{GEN_FOLDER}/huge_rows.csv", "w+") as f:
        huge_rows_csv(f)

    with open(f"{GEN_FOLDER}/huge_cols.csv", "w+") as f:
        huge_cols_csv(f)

    with open(f"{GEN_FOLDER}/non_ascii.csv", "w+") as f:
        non_ascii(f)

if __name__ == "__main__":
    main()
