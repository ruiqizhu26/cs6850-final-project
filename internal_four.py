from distribution import Distribution


d2i = Distribution.direct2indirect


d = Distribution(['u1v', 'u2v', 'u3v', 'u4v'], ['UNu1u2', 'UNu1u3', 'UNu1u4', 'UNu2u3', 'UNu2u4', 'UNu3u4'])
d.add_constraint([{'EE': None, 'II': []}], 1)


A_is_u1 = [
    {'EE': ['u1v'], 'II': []},
    {'EE': ['u1v', 'u2v'], 'II': []},
    {'EE': ['u1v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u2v'], 'II': [d2i('u1u2')]},
    {'EE': ['u2v'], 'II': [d2i('u1u3'), d2i('u3u2')]},
    {'EE': ['u2v'], 'II': [d2i('u1u4'), d2i('u4u2')]},
    {'EE': ['u2v'], 'II': [d2i('u1u3'), d2i('u3u4'), d2i('u4u2')]},
    {'EE': ['u2v'], 'II': [d2i('u1u4'), d2i('u4u3'), d2i('u3u2')]},
    {'EE': ['u3v'], 'II': [d2i('u1u3')]},
    {'EE': ['u3v'], 'II': [d2i('u1u2'), d2i('u2u3')]},
    {'EE': ['u3v'], 'II': [d2i('u1u4'), d2i('u4u3')]},
    {'EE': ['u3v'], 'II': [d2i('u1u2'), d2i('u2u4'), d2i('u4u3')]},
    {'EE': ['u3v'], 'II': [d2i('u1u4'), d2i('u4u2'), d2i('u2u3')]},
    {'EE': ['u4v'], 'II': [d2i('u1u4')]},
    {'EE': ['u4v'], 'II': [d2i('u1u2'), d2i('u2u4')]},
    {'EE': ['u4v'], 'II': [d2i('u1u3'), d2i('u3u4')]},
    {'EE': ['u4v'], 'II': [d2i('u1u2'), d2i('u2u3'), d2i('u3u4')]},
    {'EE': ['u4v'], 'II': [d2i('u1u3'), d2i('u3u2'), d2i('u2u4')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u1u2')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u1u3')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u1u4'), d2i('u4u2')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u1u4'), d2i('u4u3')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u1u2')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u1u4')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u1u3'), d2i('u3u2')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u1u3'), d2i('u3u4')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u1u3')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u1u4')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u1u2'), d2i('u2u3')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u1u2'), d2i('u2u4')]},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': [d2i('u1u2')]},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': [d2i('u1u3')]},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': [d2i('u1u4')]},
]

A_is_u2 = [
    {'EE': ['u2v'], 'II': []},
    {'EE': ['u1v', 'u2v'], 'II': []},
    {'EE': ['u2v', 'u3v'], 'II': []},
    {'EE': ['u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v'], 'II': [d2i('u2u1')]},
    {'EE': ['u1v'], 'II': [d2i('u2u3'), d2i('u3u1')]},
    {'EE': ['u1v'], 'II': [d2i('u2u4'), d2i('u4u1')]},
    {'EE': ['u1v'], 'II': [d2i('u2u3'), d2i('u3u4'), d2i('u4u1')]},
    {'EE': ['u1v'], 'II': [d2i('u2u4'), d2i('u4u3'), d2i('u3u1')]},
    {'EE': ['u3v'], 'II': [d2i('u2u3')]},
    {'EE': ['u3v'], 'II': [d2i('u2u1'), d2i('u1u3')]},
    {'EE': ['u3v'], 'II': [d2i('u2u4'), d2i('u4u3')]},
    {'EE': ['u3v'], 'II': [d2i('u2u1'), d2i('u1u4'), d2i('u4u3')]},
    {'EE': ['u3v'], 'II': [d2i('u2u4'), d2i('u4u1'), d2i('u1u3')]},
    {'EE': ['u4v'], 'II': [d2i('u2u4')]},
    {'EE': ['u4v'], 'II': [d2i('u2u1'), d2i('u1u4')]},
    {'EE': ['u4v'], 'II': [d2i('u2u3'), d2i('u3u4')]},
    {'EE': ['u4v'], 'II': [d2i('u2u1'), d2i('u1u3'), d2i('u3u4')]},
    {'EE': ['u4v'], 'II': [d2i('u2u3'), d2i('u3u1'), d2i('u1u4')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u2u1')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u2u3')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u2u4'), d2i('u4u1')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u2u4'), d2i('u4u3')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u2u1')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u2u4')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u2u3'), d2i('u3u1')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u2u3'), d2i('u3u4')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u2u3')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u2u4')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u2u1'), d2i('u1u3')]},
    {'EE': ['u3v', 'u4v'], 'II': [d2i('u2u1'), d2i('u1u4')]},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': [d2i('u2u1')]},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': [d2i('u2u3')]},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': [d2i('u2u4')]},
]

A_is_u3 = [
    {'EE': ['u3v'], 'II': []},
    {'EE': ['u1v', 'u3v'], 'II': []},
    {'EE': ['u2v', 'u3v'], 'II': []},
    {'EE': ['u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v'], 'II': [d2i('u3u1')]},
    {'EE': ['u1v'], 'II': [d2i('u3u2'), d2i('u2u1')]},
    {'EE': ['u1v'], 'II': [d2i('u3u4'), d2i('u4u1')]},
    {'EE': ['u1v'], 'II': [d2i('u3u2'), d2i('u2u4'), d2i('u4u1')]},
    {'EE': ['u1v'], 'II': [d2i('u3u4'), d2i('u4u2'), d2i('u2u1')]},
    {'EE': ['u2v'], 'II': [d2i('u3u2')]},
    {'EE': ['u2v'], 'II': [d2i('u3u1'), d2i('u1u2')]},
    {'EE': ['u2v'], 'II': [d2i('u3u4'), d2i('u4u2')]},
    {'EE': ['u2v'], 'II': [d2i('u3u1'), d2i('u1u4'), d2i('u4u2')]},
    {'EE': ['u2v'], 'II': [d2i('u3u4'), d2i('u4u1'), d2i('u1u2')]},
    {'EE': ['u4v'], 'II': [d2i('u3u4')]},
    {'EE': ['u4v'], 'II': [d2i('u3u1'), d2i('u1u4')]},
    {'EE': ['u4v'], 'II': [d2i('u3u2'), d2i('u2u4')]},
    {'EE': ['u4v'], 'II': [d2i('u3u1'), d2i('u1u2'), d2i('u2u4')]},
    {'EE': ['u4v'], 'II': [d2i('u3u2'), d2i('u2u1'), d2i('u1u4')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u3u1')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u3u2')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u3u4'), d2i('u4u1')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u3u4'), d2i('u4u2')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u3u1')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u3u4')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u3u2'), d2i('u2u1')]},
    {'EE': ['u1v', 'u4v'], 'II': [d2i('u3u2'), d2i('u2u4')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u3u2')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u3u4')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u3u1'), d2i('u1u2')]},
    {'EE': ['u2v', 'u4v'], 'II': [d2i('u3u1'), d2i('u1u4')]},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': [d2i('u3u1')]},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': [d2i('u3u2')]},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': [d2i('u3u4')]},
]

A_is_u4 = [
    {'EE': ['u4v'], 'II': []},
    {'EE': ['u1v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u4v'], 'II': []},
    {'EE': ['u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v'], 'II': [d2i('u4u1')]},
    {'EE': ['u1v'], 'II': [d2i('u4u2'), d2i('u2u1')]},
    {'EE': ['u1v'], 'II': [d2i('u4u3'), d2i('u3u1')]},
    {'EE': ['u1v'], 'II': [d2i('u4u2'), d2i('u2u3'), d2i('u3u1')]},
    {'EE': ['u1v'], 'II': [d2i('u4u3'), d2i('u3u2'), d2i('u2u1')]},
    {'EE': ['u2v'], 'II': [d2i('u4u2')]},
    {'EE': ['u2v'], 'II': [d2i('u4u1'), d2i('u1u2')]},
    {'EE': ['u2v'], 'II': [d2i('u4u3'), d2i('u3u2')]},
    {'EE': ['u2v'], 'II': [d2i('u4u1'), d2i('u1u3'), d2i('u3u2')]},
    {'EE': ['u2v'], 'II': [d2i('u4u3'), d2i('u3u1'), d2i('u1u2')]},
    {'EE': ['u3v'], 'II': [d2i('u4u3')]},
    {'EE': ['u3v'], 'II': [d2i('u4u1'), d2i('u1u3')]},
    {'EE': ['u3v'], 'II': [d2i('u4u2'), d2i('u2u3')]},
    {'EE': ['u3v'], 'II': [d2i('u4u1'), d2i('u1u2'), d2i('u2u3')]},
    {'EE': ['u3v'], 'II': [d2i('u4u2'), d2i('u2u1'), d2i('u1u3')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u4u1')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u4u2')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u4u3'), d2i('u3u1')]},
    {'EE': ['u1v', 'u2v'], 'II': [d2i('u4u3'), d2i('u3u2')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u4u1')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u4u3')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u4u2'), d2i('u2u1')]},
    {'EE': ['u1v', 'u3v'], 'II': [d2i('u4u2'), d2i('u2u3')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u4u2')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u4u3')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u4u1'), d2i('u1u2')]},
    {'EE': ['u2v', 'u3v'], 'II': [d2i('u4u1'), d2i('u1u3')]},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': [d2i('u4u1')]},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': [d2i('u4u2')]},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': [d2i('u4u3')]},
]


# Probability sum of outcomes from which A = {u1} can reach v is 1/2
d.add_constraint(A_is_u1, 1/2)
# Probability sum of outcomes from which A = {u2} can reach v is 1/2
d.add_constraint(A_is_u2, 1/2)
# Probability sum of outcomes from which A = {u3} can reach v is 1/2
d.add_constraint(A_is_u3, 1/2)
# Probability sum of outcomes from which A = {u4} can reach v is 1/2
d.add_constraint(A_is_u4, 1/2)

# Probability sum of outcomes from which A = {u1, u2} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u2, 3/4)
# Probability sum of outcomes from which A = {u1, u3} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u3, 3/4)
# Probability sum of outcomes from which A = {u1, u4} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u4, 3/4)
# Probability sum of outcomes from which A = {u2, u3} can reach v is 3/4
d.add_constraint(A_is_u2 + A_is_u3, 3/4)
# Probability sum of outcomes from which A = {u2, u4} can reach v is 3/4
d.add_constraint(A_is_u2 + A_is_u4, 3/4)
# Probability sum of outcomes from which A = {u3, u4} can reach v is 3/4
d.add_constraint(A_is_u3 + A_is_u4, 3/4)

# Probability sum of outcomes from which A = {u1, u2, u3} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u3, 3/4)
# Probability sum of outcomes from which A = {u1, u2, u4} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u4, 3/4)
# Probability sum of outcomes from which A = {u1, u3, u4} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u3 + A_is_u4, 3/4)
# Probability sum of outcomes from which A = {u2, u3, u4} can reach v is 3/4
d.add_constraint(A_is_u2 + A_is_u3 + A_is_u4, 3/4)

# Probability sum of outcomes from which A = {u1, u2, u3, u4} can reach v is 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u3 + A_is_u4, 3/4)


d.find()