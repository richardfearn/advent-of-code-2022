ROCK, PAPER, SCISSORS = range(3)

LOSE, DRAW, WIN = range(3)

SHAPE_MAPPING = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

RESPONSE_MAPPING = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

SHAPE_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

OUTCOME_SCORES = {
    LOSE: 0,
    DRAW: 3,
    WIN: 6,
}

OUTCOME_MAPPING = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}


def part_1_answer(lines):
    total = 0

    for line in lines:
        values = line.split(" ")
        them = SHAPE_MAPPING[values[0]]
        us = RESPONSE_MAPPING[values[1]]

        if us == them:
            outcome = DRAW
        elif us == ROCK and them == SCISSORS:
            outcome = WIN
        elif us == PAPER and them == ROCK:
            outcome = WIN
        elif us == SCISSORS and them == PAPER:
            outcome = WIN
        else:
            outcome = LOSE

        shape_score = SHAPE_SCORES[us]
        outcome_score = OUTCOME_SCORES[outcome]
        round_score = shape_score + outcome_score
        total += round_score

    return total


def part_2_answer(lines):
    total = 0

    for line in lines:
        values = line.split(" ")
        them = SHAPE_MAPPING[values[0]]
        outcome = OUTCOME_MAPPING[values[1]]

        us = None

        if outcome == LOSE:
            if them == ROCK:
                us = SCISSORS
            elif them == PAPER:
                us = ROCK
            elif them == SCISSORS:
                us = PAPER

        elif outcome == DRAW:
            us = them

        elif outcome == WIN:
            if them == ROCK:
                us = PAPER
            elif them == PAPER:
                us = SCISSORS
            elif them == SCISSORS:
                us = ROCK

        shape_score = SHAPE_SCORES[us]
        outcome_score = OUTCOME_SCORES[outcome]
        round_score = shape_score + outcome_score
        total += round_score

    return total
