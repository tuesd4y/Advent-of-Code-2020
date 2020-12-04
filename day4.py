from aocd import get_data
import re

# input
f = get_data(day=4, year=2020)


def parse(line: str):
    parts = re.findall(r'\S+', line.strip())
    l = {}
    for p in parts:
        key, value = p.split(':')
        l[key] = value
    return l


passports = [parse(line) for line in f.split('\n\n')]
# f = '''
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# '''.strip()
# passports = [parse(line) for line in f.split('\n\n')]
expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

count = 0
for p in passports:
    fail = False
    for f in expected_fields:
        if f != 'cid' and not (f in p):
            fail = True
    if not fail:
        count += 1

print(count)

expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

count = 0
for p in passports:
    fail = False
    for f in expected_fields:
        if f != 'cid' and not (f in p):
            fail = True
            continue
        if f == 'byr':
            try:
                byr = int(p['byr'])
                if byr < 1920 or byr > 2002:
                    fail = True
            except:
                fail = True
        if f == 'iyr':
            try:
                iyr = int(p['iyr'])
                if iyr < 2010 or iyr > 2020:
                    fail = True
            except:
                fail = True

        if f == 'eyr':
            try:
                eyr = int(p['eyr'])
                if eyr < 2020 or eyr > 2030:
                    fail = True
            except:
                fail = True

        if f == 'hgt':
            try:
                hgt = p['hgt']
                t = hgt[-2:]
                hgt = int(hgt[:-2])
                if t == 'in':
                    if hgt < 59 or hgt > 76:
                        fail = True

                elif t == 'cm':
                    if hgt < 150 or hgt > 193:
                        fail = True
                else:
                    fail = True
            except:
                fail = True

        if f == 'hcl':
            try:
                if not re.match(r'^#[abcdef0123456789]{6}$', p['hcl']):
                    fail = True
            except:
                fail = True

        if f == 'ecl':
            if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                fail = True

        if f == 'pid':
            if not re.match(r'^\d{9}$', p['pid']):
                fail = True

    if not fail:
        count += 1

print(count)
