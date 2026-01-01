full_dot = '●'
empty_dot = '○'

def create_character(character_name, stats1, stats2, stats3):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"
    if not isinstance(stats1, int) or not isinstance(stats2, int) or not isinstance(stats3, int):
        return "All stats should be integers"
    if stats1 < 1 or stats2 < 1 or stats3 < 1:
        return "All stats should be no less than 1"
    if stats1 > 4 or stats2 > 4 or stats3 > 4:
        return "All stats should be no more than 4"
    if sum([stats1, stats2, stats3]) != 7:
        return "The character should start with 7 points"
    return f'{character_name}\nSTR {full_dot * stats1 + empty_dot * (10 - stats1)}\nINT {full_dot * stats2 + empty_dot * (10 - stats2)}\nCHA {full_dot * stats3 + empty_dot * (10 - stats3)}'

t = create_character('ren', 4, 2, 1)
print(t)