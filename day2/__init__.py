SHAPE_MAPPING = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

RESPONSE_MAPPING = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

SHAPE_SCORES = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

OUTCOME_SCORES = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}

OUTCOME_MAPPING = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


def part_1_answer(lines):
    total = 0

    for line in lines:
        values = line.split(" ")
        them = SHAPE_MAPPING[values[0]]
        us = RESPONSE_MAPPING[values[1]]

        if us == them:
            outcome = "draw"
        elif us == "rock" and them == "scissors":
            outcome = "win"
        elif us == "paper" and them == "rock":
            outcome = "win"
        elif us == "scissors" and them == "paper":
            outcome = "win"
        else:
            outcome = "lose"

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

        if outcome == "lose":
            if them == "rock":
                us = "scissors"
            elif them == "paper":
                us = "rock"
            elif them == "scissors":
                us = "paper"

        elif outcome == "draw":
            us = them

        elif outcome == "win":
            if them == "rock":
                us = "paper"
            elif them == "paper":
                us = "scissors"
            elif them == "scissors":
                us = "rock"

        shape_score = SHAPE_SCORES[us]
        outcome_score = OUTCOME_SCORES[outcome]
        round_score = shape_score + outcome_score
        total += round_score

    return total
